"""
GTM Sequence Generator
======================
Researches a target company from its URL and generates a personalized
multi-step outbound email sequence using Claude AI.

Usage (standalone):
    python gtm_sequence.py https://enedece.com.ar/ --client "NDC" --steps 3

Usage (via main.py):
    python main.py --gtm https://enedece.com.ar/ --client "NDC"
"""

import re
import json
import argparse
import urllib.request
import urllib.error
from html.parser import HTMLParser

import anthropic


# =====================================================================
# HTML → plain text
# =====================================================================
class _TextExtractor(HTMLParser):
    """Strips HTML tags and collects visible text."""

    SKIP_TAGS = {"script", "style", "noscript", "head", "meta", "link"}

    def __init__(self):
        super().__init__()
        self._skip = 0
        self.chunks: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() in self.SKIP_TAGS:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag.lower() in self.SKIP_TAGS:
            self._skip = max(0, self._skip - 1)

    def handle_data(self, data):
        if self._skip == 0:
            text = data.strip()
            if text:
                self.chunks.append(text)

    def get_text(self) -> str:
        return " ".join(self.chunks)


def _fetch_website_text(url: str, max_chars: int = 4000) -> str:
    """
    Fetch a URL and return its visible text content (stripped of HTML).
    Returns an empty string on failure.
    """
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; GTMBot/1.0)"},
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except urllib.error.URLError as exc:
        print(f"  [WARN] Could not fetch {url}: {exc}")
        return ""

    parser = _TextExtractor()
    parser.feed(html)
    text = parser.get_text()

    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_chars]


# =====================================================================
# GTM Sequencer
# =====================================================================
class GTMSequencer:
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    # ------------------------------------------------------------------
    # Step 1 – Research
    # ------------------------------------------------------------------
    def research_company(self, url: str) -> dict:
        """
        Fetch the target company's website and use Claude to extract
        a structured company profile (name, industry, pain points, etc.)
        """
        print(f"  Fetching {url} …")
        raw_text = _fetch_website_text(url)

        if not raw_text:
            # Graceful fallback: derive domain name only
            domain = re.sub(r"https?://", "", url).split("/")[0]
            return {"name": domain, "domain": domain, "summary": "", "raw": ""}

        domain = re.sub(r"https?://", "", url).split("/")[0]

        print("  Analysing company with Claude …")
        message = self.client.messages.create(
            model=self.model,
            max_tokens=400,
            messages=[{
                "role": "user",
                "content": f"""Extract a company profile from the website text below.
Reply ONLY with a JSON object — no markdown, no extra text.

Website URL: {url}
Website text (truncated):
---
{raw_text}
---

JSON format:
{{
  "name": "Company name",
  "domain": "{domain}",
  "industry": "one-line industry description",
  "products_services": "brief description of what they offer",
  "target_customers": "who they sell to",
  "likely_pain_points": ["pain point 1", "pain point 2", "pain point 3"],
  "tone_cues": "formal/informal/technical/creative — inferred from the site"
}}"""
            }]
        )

        text = message.content[0].text.strip()
        try:
            if "```" in text:
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
                text = text.strip()
            profile = json.loads(text)
        except json.JSONDecodeError:
            profile = {"name": domain, "domain": domain}

        profile["raw"] = raw_text
        return profile

    # ------------------------------------------------------------------
    # Step 2 – Generate sequence
    # ------------------------------------------------------------------
    def generate_sequence(
        self,
        company_profile: dict,
        sender_name: str,
        sender_service: str,
        sender_tone: str,
        scheduling_link: str,
        num_steps: int = 3,
    ) -> list[dict]:
        """
        Generate a multi-step cold outbound email sequence personalised
        to the target company.

        Returns a list of dicts:
        [
          {"step": 1, "delay_days": 0, "subject": "...", "body": "..."},
          {"step": 2, "delay_days": 3, "subject": "...", "body": "..."},
          ...
        ]
        """
        profile_json = json.dumps({k: v for k, v in company_profile.items() if k != "raw"}, ensure_ascii=False, indent=2)

        print(f"  Generating {num_steps}-step email sequence …")
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1500,
            messages=[{
                "role": "user",
                "content": f"""You are writing a cold outbound email sequence on behalf of {sender_name}.

SENDER SERVICE: {sender_service}
SENDER TONE: {sender_tone}
SCHEDULING LINK: {scheduling_link}

TARGET COMPANY PROFILE:
{profile_json}

Write a {num_steps}-step cold email sequence to a decision-maker at the target company.
Reply ONLY with a JSON array — no markdown, no extra text.

Rules:
- Step 1: personalised opener, reference something specific from their business, soft CTA
- Step 2 (send 3 days later): brief follow-up, add a new angle or insight, CTA
- Step 3 (send 7 days later): final short bump, low-friction ask
- Each email under 120 words
- No placeholder brackets — write complete, ready-to-send emails
- Subject lines must be compelling and human (no clickbait)
- Sign off naturally as {sender_name}

JSON format:
[
  {{"step": 1, "delay_days": 0, "subject": "...", "body": "..."}},
  {{"step": 2, "delay_days": 3, "subject": "...", "body": "..."}},
  {{"step": 3, "delay_days": 7, "subject": "...", "body": "..."}}
]"""
            }]
        )

        text = message.content[0].text.strip()
        try:
            if "```" in text:
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
                text = text.strip()
            sequence = json.loads(text)
        except json.JSONDecodeError:
            print("  [WARN] Could not parse sequence JSON — returning raw text.")
            sequence = [{"step": 1, "delay_days": 0, "subject": "(see body)", "body": text}]

        return sequence

    # ------------------------------------------------------------------
    # Convenience: run full pipeline
    # ------------------------------------------------------------------
    def run(
        self,
        target_url: str,
        sender_name: str,
        sender_service: str,
        sender_tone: str,
        scheduling_link: str,
        num_steps: int = 3,
    ) -> tuple[dict, list[dict]]:
        """
        Full pipeline: research → generate.
        Returns (company_profile, sequence).
        """
        profile = self.research_company(target_url)
        sequence = self.generate_sequence(
            company_profile=profile,
            sender_name=sender_name,
            sender_service=sender_service,
            sender_tone=sender_tone,
            scheduling_link=scheduling_link,
            num_steps=num_steps,
        )
        return profile, sequence


# =====================================================================
# Pretty-print helpers
# =====================================================================
def print_profile(profile: dict):
    print("\n" + "=" * 60)
    print("  COMPANY PROFILE")
    print("=" * 60)
    for key, val in profile.items():
        if key == "raw":
            continue
        label = key.replace("_", " ").title()
        if isinstance(val, list):
            print(f"  {label}:")
            for item in val:
                print(f"    • {item}")
        else:
            print(f"  {label}: {val}")


def print_sequence(sequence: list[dict]):
    print("\n" + "=" * 60)
    print("  EMAIL SEQUENCE")
    print("=" * 60)
    for step in sequence:
        delay = step.get("delay_days", 0)
        timing = "Send immediately" if delay == 0 else f"Send after {delay} days"
        print(f"\n  ── Step {step['step']} ({timing}) ──")
        print(f"  Subject: {step['subject']}")
        print()
        for line in step["body"].split("\n"):
            print(f"  {line}")
    print()


# =====================================================================
# CLI entry point
# =====================================================================
def main():
    parser = argparse.ArgumentParser(description="GTM Sequence Generator")
    parser.add_argument("url", help="Target company URL (e.g. https://enedece.com.ar/)")
    parser.add_argument("--client", default="", help="Sender client name (matches config.yaml)")
    parser.add_argument("--steps", type=int, default=3, help="Number of emails in the sequence (default: 3)")
    parser.add_argument("--config", default="config.yaml", help="Path to config.yaml")
    args = parser.parse_args()

    # Load config
    import os
    import yaml

    def _load_env_file(path=".env"):
        if os.path.exists(path):
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, _, v = line.partition("=")
                        os.environ.setdefault(k.strip(), v.strip())

    def _resolve_env_vars(obj):
        if isinstance(obj, str):
            match = re.fullmatch(r"\$\{(\w+)\}", obj)
            if match:
                return os.environ.get(match.group(1), obj)
            return re.sub(r"\$\{(\w+)\}", lambda m: os.environ.get(m.group(1), m.group(0)), obj)
        elif isinstance(obj, dict):
            return {k: _resolve_env_vars(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [_resolve_env_vars(i) for i in obj]
        return obj

    _load_env_file()
    with open(args.config) as f:
        config = _resolve_env_vars(yaml.safe_load(f))

    # Pick client
    client_cfg = None
    if args.client:
        for c in config["clients"]:
            if c["name"].lower() == args.client.lower():
                client_cfg = c
                break
        if not client_cfg:
            print(f"  [ERROR] Client '{args.client}' not found in config. Available: "
                  + ", ".join(c["name"] for c in config["clients"]))
            raise SystemExit(1)
    else:
        client_cfg = config["clients"][0]
        print(f"  No --client specified. Using first client: {client_cfg['name']}")

    print(f"\n{'='*60}")
    print(f"  GTM SEQUENCE — {args.url}")
    print(f"  Sender: {client_cfg['name']}  |  Steps: {args.steps}")
    print(f"{'='*60}")

    sequencer = GTMSequencer(api_key=config["anthropic_api_key"])
    profile, sequence = sequencer.run(
        target_url=args.url,
        sender_name=client_cfg["name"],
        sender_service=client_cfg["service_description"],
        sender_tone=client_cfg["tone"],
        scheduling_link=client_cfg["scheduling_link"],
        num_steps=args.steps,
    )

    print_profile(profile)
    print_sequence(sequence)


if __name__ == "__main__":
    main()
