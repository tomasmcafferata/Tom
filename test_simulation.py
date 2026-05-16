#!/usr/bin/env python3
"""
Simulates a reply arriving from an Agupá campaign.
Tests the full flow: classify → generate draft → post to Slack → update CRM.
Skips Instantly (uses fake data instead).

Usage: python test_simulation.py
"""

import os
import json
import yaml


def _load_env_file():
    if os.path.exists(".env"):
        with open(".env") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, _, v = line.partition("=")
                    os.environ.setdefault(k.strip(), v.strip())


def _resolve_env_vars(obj):
    import re
    if isinstance(obj, str):
        match = re.fullmatch(r"\$\{(\w+)\}", obj)
        if match:
            return os.environ.get(match.group(1), obj)
        return re.sub(r"\$\{(\w+)\}", lambda m: os.environ.get(m.group(1), m.group(0)), obj)
    elif isinstance(obj, dict):
        return {k: _resolve_env_vars(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_resolve_env_vars(item) for item in obj]
    return obj


def main():
    _load_env_file()
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    config = _resolve_env_vars(config)

    print("\n" + "=" * 60)
    print("  SIMULATION TEST — Fake reply from Agupá campaign")
    print("=" * 60)

    # --- Fake reply ---
    fake_reply = {
        "lead_email": "maria.lopez@testcompany.com",
        "lead_name": "María López",
        "to_inbox": "agus@agupawood.com",
        "subject": "Re: Regalos corporativos para fin de año",
        "body": "Hola! Me interesa mucho lo que ofrecen. Somos una empresa de 150 empleados y estamos buscando regalos de fin de año que sean diferentes a lo que damos siempre. ¿Qué opciones tienen y en qué rango de precios se manejan? También me gustaría saber los tiempos de entrega.",
        "campaign_id": "sim-001",
        "campaign_name": "AGUPA-FDY-Simulation",
        "message_id": "sim-msg-001",
        "timestamp": 1747400000,
    }

    print(f"\n  Simulated reply:")
    print(f"    From: {fake_reply['lead_name']} <{fake_reply['lead_email']}>")
    print(f"    To:   {fake_reply['to_inbox']}")
    print(f"    Body: {fake_reply['body'][:100]}...")

    # Step 1: Find client
    print(f"\n  [Step 1] Finding client for inbox {fake_reply['to_inbox']}...")
    client = None
    for c in config["clients"]:
        for inbox in c["inboxes"]:
            if inbox["email"].lower() == fake_reply["to_inbox"].lower():
                client = c
                break
    if not client:
        print("  FAIL — no client found")
        return
    print(f"    → Client: {client['name']}")

    # Step 2: Classify
    print(f"\n  [Step 2] Classifying reply with AI...")
    from response_generator import ResponseGenerator
    ai = ResponseGenerator(config["anthropic_api_key"])
    classification = ai.classify_reply(fake_reply["body"])
    print(f"    → Classification: {classification['classification']}")
    print(f"    → Status: {classification.get('status', '?')}")
    print(f"    → Should respond: {classification.get('should_respond', '?')}")

    # Step 3: Generate response
    proposed_response = ""
    if classification.get("should_respond", False):
        print(f"\n  [Step 3] Generating AI response draft...")
        proposed_response = ai.generate_response(
            thread=[{"is_sent": True, "body": "Hacemos regalos corporativos artesanales en madera maciza con logo grabado en laser. ¿Te interesa saber más?"}],
            reply_body=fake_reply["body"],
            client_name=client["name"],
            tone=client["tone"],
            context_file=client.get("context_file", ""),
            resources=client.get("resources", []),
            classification=classification["classification"],
        )
        print(f"    → Draft ({len(proposed_response)} chars):")
        print(f"    ┌─────────────────────────────────────────────")
        for line in proposed_response.split("\n"):
            print(f"    │ {line}")
        print(f"    └─────────────────────────────────────────────")
    else:
        print(f"\n  [Step 3] Skipped — AI says no response needed.")

    # Step 4: Extract company
    domain = fake_reply["lead_email"].split("@")[1]
    company = domain.split(".")[0].title()

    # Step 5: Update CRM
    print(f"\n  [Step 4] Updating Google Sheets CRM...")
    from sheets_crm import SheetsCRM
    crm = SheetsCRM(config["google_sheet_id"], config["google_credentials_path"])
    lead_data = {
        "email": fake_reply["lead_email"],
        "name": fake_reply["lead_name"],
        "company": company,
        "client": client["name"],
        "campaign": fake_reply["campaign_name"],
        "inbox": fake_reply["to_inbox"],
        "status": classification.get("status", "New Reply"),
        "classification": classification.get("classification", "unknown"),
        "reply_snippet": fake_reply["body"][:200],
        "draft": proposed_response[:500] if proposed_response else "",
    }
    crm.add_or_update_lead(lead_data)
    print(f"    → Lead added/updated in sheet!")

    # Step 6: Post to Slack
    print(f"\n  [Step 5] Posting to Slack channel...")
    from email_sender import EmailSender
    from slack_handler import SlackHandler

    email_sender = EmailSender(
        gmail_credentials_path="credentials/gmail_oauth_credentials.json",
        clients_config=config.get("clients", []),
    )

    slack_config = config["slack"]
    slack = SlackHandler(
        bot_token=slack_config["bot_token"],
        app_token=slack_config["app_token"],
        channel_id=slack_config["channel_id"],
        email_sender=email_sender,
    )

    provider = "microsoft"
    subject = fake_reply.get("subject", "")
    if subject and not subject.lower().startswith("re:"):
        subject = f"Re: {subject}"

    slack.notify_new_reply({
        "lead_email": fake_reply["lead_email"],
        "lead_name": fake_reply["lead_name"],
        "company": company,
        "client_name": client["name"],
        "campaign": fake_reply["campaign_name"],
        "inbox_email": fake_reply["to_inbox"],
        "classification": classification.get("classification", "unknown"),
        "reply_body": fake_reply["body"],
        "proposed_response": proposed_response,
        "subject": subject,
        "thread_id": "",
        "message_id": fake_reply["message_id"],
        "provider": provider,
    })
    print(f"    → Message posted to Slack with Approve/Edit/Skip buttons!")

    print(f"\n" + "=" * 60)
    print(f"  SIMULATION COMPLETE")
    print(f"  Check your Slack channel and Google Sheet now!")
    print(f"=" * 60 + "\n")

    print("  Listening for button clicks (Approve/Edit/Skip)...")
    print("  Press Ctrl+C to stop.\n")
    slack.start()

    import time
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n  Stopped.")


if __name__ == "__main__":
    main()
