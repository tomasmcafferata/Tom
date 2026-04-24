"""
AI Response Generator — uses Claude to classify replies and generate response drafts.
Reads per-client context files (from market analysis) for deep knowledge.
"""

import os
import anthropic


class ResponseGenerator:
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"
        self._context_cache = {}

    def _load_context(self, context_file: str) -> str:
        """Load a client's context file (market analysis output)."""
        if not context_file:
            return ""
        if context_file in self._context_cache:
            return self._context_cache[context_file]
        if os.path.exists(context_file):
            with open(context_file) as f:
                content = f.read().strip()
            self._context_cache[context_file] = content
            return content
        return ""

    @staticmethod
    def _format_resources(resources: list) -> str:
        """Format resource links for the AI prompt."""
        if not resources:
            return "No resources available."
        lines = []
        for r in resources:
            name = r.get("name", "Document")
            url = r.get("url", "")
            if url and url != "REPLACE_ME":
                lines.append(f"- {name}: {url}")
        return "\n".join(lines) if lines else "No resources available."

    def classify_reply(self, reply_body: str) -> dict:
        """
        Classify an email reply into a category.
        Returns: {"classification": str, "status": str, "should_respond": bool}
        """
        message = self.client.messages.create(
            model=self.model,
            max_tokens=200,
            messages=[{
                "role": "user",
                "content": f"""Classify this email reply into exactly ONE category.
Reply ONLY with a JSON object, no other text.

Categories:
- "interested" — wants to learn more, asks questions, is positive
- "not_interested" — declines, unsubscribes, says no
- "ooo" — out of office / auto-reply
- "bounce" — delivery failure / invalid email
- "question" — asks a specific question about the offer
- "meeting" — wants to book a call / meeting

Email reply:
---
{reply_body[:1500]}
---

JSON format: {{"classification": "category", "status": "Interested|Not Interested|OOO|Bounce|In Conversation|Meeting Booked", "should_respond": true/false}}"""
            }]
        )

        text = message.content[0].text.strip()
        import json
        try:
            if "```" in text:
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
                text = text.strip()
            return json.loads(text)
        except json.JSONDecodeError:
            return {
                "classification": "unknown",
                "status": "New Reply",
                "should_respond": True
            }

    def generate_response(
        self,
        thread: list[dict],
        reply_body: str,
        client_name: str,
        tone: str,
        context_file: str = "",
        resources: list = None,
        classification: str = "",
    ) -> str:
        """
        Generate a response draft for an email reply.
        Uses the client's context file (market analysis) for deep knowledge.
        """
        context = self._load_context(context_file)
        context_block = f"\nCLIENT KNOWLEDGE BASE:\n{context[:3000]}\n" if context else ""

        resources_text = self._format_resources(resources or [])

        thread_text = ""
        for email in thread[-6:]:
            direction = "SENT" if email.get("is_sent") else "RECEIVED"
            thread_text += f"\n[{direction}] {email.get('body', email.get('text', ''))[:500]}\n---"

        message = self.client.messages.create(
            model=self.model,
            max_tokens=500,
            messages=[{
                "role": "user",
                "content": f"""You are writing a reply on behalf of {client_name}.

TONE: {tone}
{context_block}
RESOURCES TO SHARE (when the lead is interested or asks for more info):
{resources_text}

REPLY CLASSIFICATION: {classification}

THREAD SO FAR:
{thread_text}

LATEST REPLY TO RESPOND TO:
{reply_body[:1500]}

RULES:
- Keep it under 100 words
- Be natural and human — no corporate fluff
- Match the {tone} tone
- If they're interested, share the relevant resource link(s)
- If they ask a question, answer using your knowledge base, then share resources
- If they want to meet, suggest a time or ask for their availability
- Do NOT use placeholder brackets like [Name] — write a complete ready-to-send email
- Do NOT include a subject line — just the body
- Sign off naturally

Write the reply:"""
            }]
        )

        return message.content[0].text.strip()

    def generate_followup(
        self,
        lead_name: str,
        last_snippet: str,
        client_name: str,
        tone: str,
        context_file: str = "",
        resources: list = None,
        reply_count: int = 1,
    ) -> str:
        """Generate a follow-up for a lead that went silent."""
        context = self._load_context(context_file)
        context_block = f"\nCLIENT KNOWLEDGE BASE:\n{context[:2000]}\n" if context else ""
        resources_text = self._format_resources(resources or [])

        message = self.client.messages.create(
            model=self.model,
            max_tokens=300,
            messages=[{
                "role": "user",
                "content": f"""Write a short follow-up email. The lead replied before but went silent.

CLIENT: {client_name}
TONE: {tone}
{context_block}
RESOURCES: {resources_text}
LEAD NAME: {lead_name or "there"}
THEIR LAST MESSAGE: {last_snippet[:500]}
TOTAL REPLIES SO FAR: {reply_count}

RULES:
- Under 60 words
- Casual, not pushy
- Reference their last message naturally
- If appropriate, mention a resource link
- No placeholder brackets — write complete text
- Just the body, no subject line

Write the follow-up:"""
            }]
        )

        return message.content[0].text.strip()
