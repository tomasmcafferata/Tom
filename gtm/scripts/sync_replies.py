#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYNC REPLIES → outbound Lead CRM
================================
One-way bridge. Reads the inbound Reply CRM (the email-response skill's sheet, READ-ONLY)
and writes each replier's outcome onto the matching lead in the outbound Leads tab
(match by email), so future campaigns don't re-contact someone who already replied or said
no. It does NOT touch the live email-response skill or its sheet.

Writes onto outbound Leads: status, reply_classification, last_contact_date, and
do_not_contact=TRUE for a hard no / bounce.

Usage:
    py -3 gtm/scripts/sync_replies.py                       # dry-run: report, no writes
    py -3 gtm/scripts/sync_replies.py --write               # persist to outbound Leads
    py -3 gtm/scripts/sync_replies.py --reply-sheet-id <id> # override reply CRM sheet

Verify: dry-run prints matched / unmatched counts + the status-change breakdown. Re-run
with --write to persist; nothing on the reply side is ever modified.
"""

import argparse
import os
import sys

# Reuse prescreen's config/auth + sheet helpers (DRY, drift-safe).
from prescreen import load_config, connect, col_letter, find_column, REPO_ROOT

# reply Status (lowercased) -> (outbound status, set do_not_contact)
STATUS_MAP = {
    "new reply":       ("replied", False),
    "interested":      ("interested", False),
    "in conversation": ("in_conversation", False),
    "meeting booked":  ("meeting_booked", False),
    "not interested":  ("not_interested", True),
    "ooo":             ("replied", False),
    "bounce":          ("bounced", True),
}


def load_env(path: str):
    """Minimal .env loader (reply CRM sheet id lives in GOOGLE_SHEET_ID)."""
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, _, v = line.partition("=")
                    os.environ.setdefault(k.strip(), v.strip())


def main():
    p = argparse.ArgumentParser(description="Sync inbound replies onto the outbound Lead CRM")
    p.add_argument("--write", action="store_true", help="Persist (default: dry-run)")
    p.add_argument("--reply-sheet-id", default=None,
                   help="Reply CRM sheet id (default: .env GOOGLE_SHEET_ID)")
    p.add_argument("--reply-tab", default="Leads", help="Reply CRM tab (default: Leads)")
    p.add_argument("--out-tab", default="Leads", help="Outbound tab (default: Leads)")
    args = p.parse_args()

    print("\n" + "=" * 60)
    print("  SYNC REPLIES -> outbound Lead CRM"
          + ("  [DRY-RUN]" if not args.write else "  [WRITE]"))
    print("=" * 60)

    load_env(os.path.join(REPO_ROOT, ".env"))
    reply_sheet_id = args.reply_sheet_id or os.environ.get("GOOGLE_SHEET_ID")
    if not reply_sheet_id:
        sys.exit("[ERROR] reply CRM sheet id missing. Set GOOGLE_SHEET_ID in .env or pass "
                 "--reply-sheet-id.")

    cfg = load_config()
    out_sheet_id = cfg.get("lead_db_sheet_id")
    if not out_sheet_id:
        sys.exit("[ERROR] lead_db_sheet_id missing in config.yaml")
    if reply_sheet_id == out_sheet_id:
        sys.exit("[ERROR] reply sheet id == outbound sheet id — pass the correct --reply-sheet-id.")

    gc = connect(cfg)

    print("\n[1/4] Reading reply CRM (read-only)...")
    try:
        reply_ws = gc.open_by_key(reply_sheet_id).worksheet(args.reply_tab)
        replies = reply_ws.get_all_records()
    except Exception as e:
        msg = str(e)
        hint = ("transient Google API error (5xx) — just re-run."
                if any(c in msg for c in ("503", "500", "502")) or "unavailable" in msg.lower()
                else "make sure the service account has access to that spreadsheet.")
        sys.exit(f"[ERROR] Cannot read reply CRM ({reply_sheet_id}, tab '{args.reply_tab}'): {e}\n"
                 f"        {hint}")
    print(f"      {len(replies)} reply records.")

    print("[2/4] Reading outbound Leads...")
    out_ws = gc.open_by_key(out_sheet_id).worksheet(args.out_tab)
    out_rows = out_ws.get_all_records()
    n = len(out_rows)
    headers = out_ws.row_values(1)
    print(f"      {n} outbound leads.")
    if n == 0:
        sys.exit("[ERROR] Outbound Leads tab is empty.")

    ci = {name: find_column(headers, name) for name in
          ("email", "status", "reply_classification", "last_contact_date", "do_not_contact")}

    # email -> outbound row index (0-based into out_rows; first occurrence wins)
    email_to_idx = {}
    for i, r in enumerate(out_rows):
        e = str(r.get("email", "")).strip().lower()
        if e:
            email_to_idx.setdefault(e, i)

    # Current column values — preserve unmatched rows, override only matched ones.
    status_col = [[str(r.get("status", "")).strip()] for r in out_rows]
    cls_col = [[str(r.get("reply_classification", "")).strip()] for r in out_rows]
    lcd_col = [[str(r.get("last_contact_date", "")).strip()] for r in out_rows]
    dnc_col = [[str(r.get("do_not_contact", "")).strip()] for r in out_rows]

    matched, unmatched = 0, 0
    changes = {}
    for rep in replies:
        email = str(rep.get("Lead Email", "")).strip().lower()
        if not email:
            continue
        idx = email_to_idx.get(email)
        if idx is None:
            unmatched += 1
            continue
        matched += 1
        out_status, set_dnc = STATUS_MAP.get(str(rep.get("Status", "")).strip().lower(),
                                             ("replied", False))
        status_col[idx] = [out_status]
        cls_col[idx] = [str(rep.get("Classification", "")).strip()]
        last_reply = str(rep.get("Last Reply Date", "")).strip()
        if last_reply:
            lcd_col[idx] = [last_reply]
        if set_dnc:                       # do_not_contact is sticky once set
            dnc_col[idx] = ["TRUE"]
        changes[out_status] = changes.get(out_status, 0) + 1

    print("[3/4] Matching by email...")
    print(f"      matched to outbound leads : {matched}")
    print(f"      no match (skipped)        : {unmatched}")
    print(f"      status changes            : {changes or '(none)'}")

    if not args.write:
        print("[4/4] DRY-RUN: outbound CRM not modified. Re-run with --write to persist.")
        print("=" * 60 + "\n")
        return
    if matched == 0:
        print("[4/4] Nothing matched — no write needed.")
        print("=" * 60 + "\n")
        return

    print("[4/4] Writing to outbound Leads...")
    def a1(name):
        return col_letter(ci[name])
    out_ws.update(range_name=f"{a1('status')}2:{a1('status')}{n+1}",
                  values=status_col, value_input_option="USER_ENTERED")
    out_ws.update(range_name=f"{a1('reply_classification')}2:{a1('reply_classification')}{n+1}",
                  values=cls_col, value_input_option="USER_ENTERED")
    out_ws.update(range_name=f"{a1('last_contact_date')}2:{a1('last_contact_date')}{n+1}",
                  values=lcd_col, value_input_option="USER_ENTERED")
    out_ws.update(range_name=f"{a1('do_not_contact')}2:{a1('do_not_contact')}{n+1}",
                  values=dnc_col, value_input_option="USER_ENTERED")
    print(f"      OK: {matched} leads updated (status / classification / last_contact / DNC).")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
