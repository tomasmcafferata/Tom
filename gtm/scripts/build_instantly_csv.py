#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INSTANTLY CSV BUILDER  (generic, per-client, column-agnostic)
=============================================================
Reads the Lead Sheet, selects the qualified cohort for a campaign, and writes an
Instantly-ready import CSV. It is a DUMB MAPPER: it generates no copy. Whatever
personalization columns exist in the Sheet (e.g. `ai_first_line`, written by Clay) are
carried through as Instantly custom variables. Works for template-only (A), AI-line (B),
or full-AI-body (C) campaigns — it just maps the columns that exist.

Cohort selection (the gate):
  - status != disqualified
  - icp_tier (holds Clay's icp_fit) in {strong, medium}
  - email present                        (must be reachable — no point sending without it)
  - do_not_contact != TRUE
  - cooling_until empty or in the past    (respect the cooldown)
  - optional: icp_segment == --segment

Usage:
  py -3 gtm/scripts/build_instantly_csv.py --client NDC --segment ploteo
  py -3 gtm/scripts/build_instantly_csv.py --client NDC --segment ploteo --campaign rebrand
  py -3 gtm/scripts/build_instantly_csv.py --client NDC --fit strong        # tighten the gate
  py -3 gtm/scripts/build_instantly_csv.py --client NDC --limit 5           # sample

Output: gtm/leads/output/instantly_<client>[_<segment>][_<campaign>]_<date>.csv
Review the CSV, then upload to Instantly by hand (the approval gate is you).
"""

import argparse
import csv
import os
import sys
from datetime import date, datetime

# Reuse the connection layer from prescreen.py (same dir) — DRY config + auth.
from prescreen import load_config, connect, OUTPUT_DIR

# Sheet column -> Instantly CSV header. Extra columns become Instantly custom variables
# ({{header}} in the sequence). Columns absent from the Sheet are skipped with a warning,
# which is what makes this robust across A/B/C personalization levels. Override with --fields.
DEFAULT_FIELD_MAP = {
    "email":          "email",            # required by Instantly
    "first_name":     "first_name",
    "last_name":      "last_name",
    "company":        "company_name",
    "company_domain": "website",
    "industry":       "industry",
    "ai_first_line":  "ai_first_line",    # level B: Clay-written personalization line
    "triggers_found": "trigger_detail",   # for {{trigger_detail}} in the copy
}


def nonempty(v) -> bool:
    return bool(str(v or "").strip())


def cooldown_passed(v) -> bool:
    """cooling_until: empty passes; a past date passes; a future date blocks."""
    s = str(v or "").strip()
    if not s:
        return True
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%m/%d/%Y"):
        try:
            return datetime.strptime(s[:19], fmt).date() <= date.today()
        except ValueError:
            continue
    return True  # unparseable → don't block on it


def main():
    p = argparse.ArgumentParser(description="Build an Instantly import CSV (read-only mapper)")
    p.add_argument("--client", default="NDC")
    p.add_argument("--segment", default=None, help="Filter icp_segment (e.g. ploteo)")
    p.add_argument("--campaign", default=None, help="Label for the output filename")
    p.add_argument("--fit", default="strong,medium", help="icp_fit values to keep (comma-sep)")
    p.add_argument("--tab", default="Leads")
    p.add_argument("--limit", type=int, default=0, help="Sample first N rows (0 = all)")
    p.add_argument("--fields", default=None, help="Optional YAML field-map override")
    args = p.parse_args()

    fit_keep = {x.strip().lower() for x in args.fit.split(",") if x.strip()}

    field_map = DEFAULT_FIELD_MAP
    if args.fields:
        import yaml
        with open(args.fields, encoding="utf-8") as f:
            field_map = yaml.safe_load(f)

    cfg = load_config()
    sheet_id = cfg.get("lead_db_sheet_id")
    if not sheet_id:
        sys.exit("[ERROR] lead_db_sheet_id missing in config.yaml")
    gc = connect(cfg)
    ws = gc.open_by_key(sheet_id).worksheet(args.tab)
    rows = ws.get_all_records()
    n = len(rows)
    if n == 0:
        sys.exit("[ERROR] No leads in the tab.")
    headers = list(rows[0].keys())

    # Only map columns that actually exist in the Sheet (robust across A/B/C).
    present = {src: dst for src, dst in field_map.items() if src in headers}
    missing = [src for src in field_map if src not in headers]
    if missing:
        print(f"[warn] mapped columns not in Sheet, skipped: {missing}")

    kept = []
    excl = {"disqualified": 0, "fit": 0, "no_email": 0, "do_not_contact": 0,
            "cooldown": 0, "segment": 0}
    for r in rows:
        if str(r.get("status", "")).strip().lower() == "disqualified":
            excl["disqualified"] += 1; continue
        if str(r.get("icp_tier", "")).strip().lower() not in fit_keep:
            excl["fit"] += 1; continue
        if not nonempty(r.get("email")):
            excl["no_email"] += 1; continue
        if str(r.get("do_not_contact", "")).strip().upper() == "TRUE":
            excl["do_not_contact"] += 1; continue
        if not cooldown_passed(r.get("cooling_until")):
            excl["cooldown"] += 1; continue
        if args.segment and str(r.get("icp_segment", "")).strip().lower() != args.segment.lower():
            excl["segment"] += 1; continue
        kept.append({dst: r.get(src, "") for src, dst in present.items()})

    if args.limit and len(kept) > args.limit:
        kept = kept[:args.limit]

    seg = f"_{args.segment}" if args.segment else ""
    label = f"_{args.campaign}" if args.campaign else ""
    today = date.today().strftime("%Y-%m-%d")
    out = os.path.join(OUTPUT_DIR, f"instantly_{args.client}{seg}{label}_{today}.csv")

    print("\n" + "=" * 60)
    print(f"  INSTANTLY CSV — {args.client}{seg}{label}")
    print("=" * 60)
    print(f"  Read {n} leads. Cohort kept: {len(kept)}")
    print(f"  Excluded: {excl}")

    if not kept:
        print("\n  Nothing written. If 'fit'/'no_email' excluded everyone, enrichment")
        print("  hasn't run yet — Clay must write icp_tier (fit) + email first.")
        print("=" * 60 + "\n")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_headers = list(present.values())
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_headers)
        w.writeheader()
        w.writerows(kept)

    print(f"  Columns (Instantly vars): {out_headers}")
    print(f"  CSV: {out}")
    print(f"\n  Review it, then upload to Instantly by hand. Stop-on-reply: ON.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
