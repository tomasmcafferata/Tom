"""
AI Response Generator — uses Claude to classify replies and generate response drafts.
"""

import anthropic


class ResponseGenerator:
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

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
        # Parse JSON from response
        import json
        try:
            # Handle potential markdown wrapping
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
        service_description: str,
        scheduling_link: str,
        classification: str,
    ) -> str:
        """
        Generate a response draft for an email reply.
        Returns the draft text.
        """
        # Build thread context
        thread_text = ""
        for email in thread[-6:]:  # Last 6 emails for context
            direction = "SENT" if email.get("is_sent") else "RECEIVED"
            thread_text += f"\n[{direction}] {email.get('body', email.get('text', ''))[:500]}\n---"

        message = self.client.messages.create(
            model=self.model,
            max_tokens=500,
            messages=[{
                "role": "user",
                "content": f"""You are writing a reply on behalf of {client_name}.

TONE: {tone}
SERVICE: {service_description}
GOAL: Book a meeting. Scheduling link: {scheduling_link}
REPLY CLASSIFICATION: {classification}

THREAD SO FAR:
{thread_text}

LATEST REPLY TO RESPOND TO:
{reply_body[:1500]}

RULES:
- Keep it under 100 words
- Be natural and human — no corporate fluff
- Match the {tone} tone
- If they're interested, nudge toward booking a call
- If they ask a question, answer concisely then nudge toward a call
- If they want to book, make it easy with the link
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
        service_description: str,
        scheduling_link: str,
        reply_count: int,
    ) -> str:
        """Generate a follow-up for a lead that went silent."""
        message = self.client.messages.create(
            model=self.model,
            max_tokens=300,
            messages=[{
                "role": "user",
                "content": f"""Write a short follow-up email. The lead replied before but went silent.

CLIENT: {client_name}
TONE: {tone}
SERVICE: {service_description}
SCHEDULING LINK: {scheduling_link}
LEAD NAME: {lead_name or "there"}
THEIR LAST MESSAGE: {last_snippet[:500]}
TOTAL REPLIES SO FAR: {reply_count}

RULES:
- Under 60 words
- Casual, not pushy
- Reference their last message naturally
- Nudge toward booking a call
- No placeholder brackets — write complete text
- Just the body, no subject line

Write the follow-up:"""
            }]
        )

        return message.content[0].text.strip()
