#!/usr/bin/env python3
"""
EMAIL RESPONSE AGGREGATOR
==========================
Polls Instantly for new campaign replies, classifies them,
logs leads to Google Sheets CRM, generates AI response drafts,
and creates drafts in the original inbox for review.

Usage:
    python main.py              # Run once (process new replies)
    python main.py --loop       # Run continuously (poll every N seconds)
    python main.py --followups  # Check for stale leads and generate follow-ups
"""

import os
import sys
import json
import time
import yaml
import argparse
from datetime import datetime

from instantly_client import InstantlyClient
from sheets_crm import SheetsCRM
from response_generator import ResponseGenerator
from draft_creator import GmailDraftCreator, OutlookDraftCreator


# =====================================================================
# STATE FILE — tracks which replies we've already processed
# =====================================================================
STATE_FILE = "state.json"


def load_state() -> dict:
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"last_timestamp": 0, "processed_ids": []}


def save_state(state: dict):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


# =====================================================================
# CONFIG
# =====================================================================
def load_config() -> dict:
    with open("config.yaml") as f:
        return yaml.safe_load(f)


def find_client_for_inbox(config: dict, inbox_email: str) -> dict | None:
    """Find which client owns a given inbox email."""
    for client in config["clients"]:
        for inbox in client["inboxes"]:
            if inbox["email"].lower() == inbox_email.lower():
                return client
    return None


def find_inbox_provider(config: dict, inbox_email: str) -> str:
    """Get the provider (google/microsoft) for an inbox."""
    for client in config["clients"]:
        for inbox in client["inboxes"]:
            if inbox["email"].lower() == inbox_email.lower():
                return inbox.get("provider", "google")
    return "google"


# =====================================================================
# MAIN PROCESSING
# =====================================================================
def process_replies(config: dict, instantly: InstantlyClient, crm: SheetsCRM,
                    ai: ResponseGenerator, gmail_drafts: GmailDraftCreator,
                    outlook_drafts: OutlookDraftCreator):
    """Fetch new replies, classify, update CRM, generate drafts."""
    state = load_state()
    print(f"\n{'='*60}")
    print(f"  CHECKING FOR NEW REPLIES — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*60}")

    replies = instantly.get_all_replies(since_timestamp=state["last_timestamp"])
    new_replies = [r for r in replies if r["message_id"] not in state["processed_ids"]]

    if not new_replies:
        print("  No new replies found.")
        return

    print(f"  Found {len(new_replies)} new replies.\n")

    for reply in new_replies:
        lead_email = reply["lead_email"]
        inbox_email = reply["to_inbox"]
        print(f"  --- Processing: {lead_email} → {inbox_email} ---")

        # 1. Find client
        client = find_client_for_inbox(config, inbox_email)
        if not client:
            print(f"  [SKIP] No client found for inbox {inbox_email}")
            state["processed_ids"].append(reply["message_id"])
            continue

        # 2. Classify the reply
        print(f"  Classifying reply...")
        classification = ai.classify_reply(reply["body"])
        print(f"  → {classification['classification']} (respond: {classification['should_respond']})")

        # 3. Update CRM
        print(f"  Updating CRM...")
        lead_data = {
            "email": lead_email,
            "name": reply.get("lead_name", ""),
            "company": "",  # Could extract from email domain
            "client": client["name"],
            "campaign": reply.get("campaign_name", reply.get("campaign_id", "")),
            "inbox": inbox_email,
            "status": classification.get("status", "New Reply"),
            "classification": classification.get("classification", "unknown"),
            "reply_snippet": reply["body"][:200],
        }

        # Extract company from email domain
        if "@" in lead_email:
            domain = lead_email.split("@")[1]
            if domain not in ("gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com"):
                lead_data["company"] = domain.split(".")[0].title()

        # 4. Generate response if needed
        if classification.get("should_respond", False):
            print(f"  Generating AI response draft...")
            thread = instantly.get_lead_thread(reply.get("campaign_id", ""), lead_email)
            draft_text = ai.generate_response(
                thread=thread,
                reply_body=reply["body"],
                client_name=client["name"],
                tone=client["tone"],
                service_description=client["service_description"],
                scheduling_link=client["scheduling_link"],
                classification=classification["classification"],
            )
            lead_data["draft"] = draft_text
            print(f"  Draft generated ({len(draft_text)} chars)")

            # 5. Create draft in inbox
            provider = find_inbox_provider(config, inbox_email)
            subject = reply.get("subject", "")
            if not subject.lower().startswith("re:"):
                subject = f"Re: {subject}"

            try:
                if provider == "google":
                    gmail_drafts.create_draft(
                        inbox_email=inbox_email,
                        to_email=lead_email,
                        subject=subject,
                        body=draft_text,
                        thread_id=reply.get("thread_id"),
                        in_reply_to=reply.get("message_id"),
                    )
                elif provider == "microsoft":
                    outlook_drafts.create_draft(
                        inbox_email=inbox_email,
                        to_email=lead_email,
                        subject=subject,
                        body=draft_text,
                    )
            except Exception as e:
                print(f"  [ERROR] Failed to create draft: {e}")
                print(f"  (Draft saved in CRM sheet for manual copy-paste)")
        else:
            print(f"  No response needed for {classification['classification']}")

        # 6. Save to CRM
        crm.add_or_update_lead(lead_data)

        # 7. Mark as processed
        state["processed_ids"].append(reply["message_id"])
        if reply.get("timestamp", 0) > state["last_timestamp"]:
            state["last_timestamp"] = reply["timestamp"]
        save_state(state)

        print()

    # Keep processed_ids list manageable (last 1000)
    state["processed_ids"] = state["processed_ids"][-1000:]
    save_state(state)
    print(f"  Done. Processed {len(new_replies)} replies.\n")


def process_followups(config: dict, crm: SheetsCRM, ai: ResponseGenerator,
                      gmail_drafts: GmailDraftCreator, outlook_drafts: OutlookDraftCreator):
    """Check for stale leads and generate follow-up drafts."""
    print(f"\n{'='*60}")
    print(f"  CHECKING FOR STALE LEADS — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*60}")

    stale_leads = crm.get_stale_leads(stale_days=2)
    if not stale_leads:
        print("  No stale leads found.")
        return

    print(f"  Found {len(stale_leads)} stale leads.\n")

    for lead in stale_leads:
        email = lead.get("Lead Email", "")
        inbox = lead.get("Inbox", "")
        client_name = lead.get("Client", "")
        print(f"  --- Follow-up: {email} ({client_name}) ---")

        # Find client config
        client = None
        for c in config["clients"]:
            if c["name"] == client_name:
                client = c
                break
        if not client:
            print(f"  [SKIP] Client config not found for {client_name}")
            continue

        # Generate follow-up
        followup_text = ai.generate_followup(
            lead_name=lead.get("Lead Name", ""),
            last_snippet=lead.get("Last Reply Snippet", ""),
            client_name=client["name"],
            tone=client["tone"],
            service_description=client["service_description"],
            scheduling_link=client["scheduling_link"],
            reply_count=int(lead.get("Reply Count", 1)),
        )

        # Create draft
        provider = find_inbox_provider(config, inbox)
        try:
            if provider == "google":
                gmail_drafts.create_draft(
                    inbox_email=inbox,
                    to_email=email,
                    subject=f"Re: Following up",
                    body=followup_text,
                )
            elif provider == "microsoft":
                outlook_drafts.create_draft(
                    inbox_email=inbox,
                    to_email=email,
                    subject=f"Re: Following up",
                    body=followup_text,
                )
        except Exception as e:
            print(f"  [ERROR] Failed to create follow-up draft: {e}")

        # Update CRM
        row = lead.get("_row_num")
        if row:
            crm.update_cell(row, "draft", followup_text[:500])
            crm.update_cell(row, "last_reply", datetime.now().strftime("%Y-%m-%d %H:%M"))
            crm.update_cell(row, "notes", f"Auto follow-up sent {datetime.now().strftime('%m/%d')}")

        print(f"  Follow-up draft created.\n")


# =====================================================================
# ENTRY POINT
# =====================================================================
def main():
    parser = argparse.ArgumentParser(description="Email Response Aggregator")
    parser.add_argument("--loop", action="store_true", help="Run continuously")
    parser.add_argument("--followups", action="store_true", help="Process stale lead follow-ups")
    args = parser.parse_args()

    # Load config
    config = load_config()

    # Initialize services
    print("Initializing services...")
    instantly = InstantlyClient(config["instantly_api_key"])
    crm = SheetsCRM(config["google_sheet_id"], config["google_credentials_path"])
    ai = ResponseGenerator(config["anthropic_api_key"])

    # Initialize draft creators
    gmail_drafts = GmailDraftCreator(
        credentials_path="credentials/gmail_oauth_credentials.json"
    )

    # Microsoft drafts (only if you have MS inboxes)
    outlook_drafts = None
    ms_config = config.get("microsoft", {})
    if ms_config:
        outlook_drafts = OutlookDraftCreator(
            client_id=ms_config.get("client_id", ""),
            tenant_id=ms_config.get("tenant_id", ""),
            client_secret=ms_config.get("client_secret", ""),
        )

    print("Services initialized.\n")

    if args.followups:
        process_followups(config, crm, ai, gmail_drafts, outlook_drafts)
        return

    if args.loop:
        interval = config.get("poll_interval_seconds", 300)
        print(f"Running in loop mode (every {interval}s). Press Ctrl+C to stop.\n")
        while True:
            try:
                process_replies(config, instantly, crm, ai, gmail_drafts, outlook_drafts)
            except KeyboardInterrupt:
                print("\nStopped.")
                break
            except Exception as e:
                print(f"\n  [ERROR] {e}\n  Retrying in {interval}s...")
            time.sleep(interval)
    else:
        process_replies(config, instantly, crm, ai, gmail_drafts, outlook_drafts)


if __name__ == "__main__":
    main()
