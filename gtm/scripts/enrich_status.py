#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENRICHMENT STATUS  (generic, per-client, read-only)
===================================================
After Clay enriches the non-disqualified pool (writes email + company fields back to
the Sheet via native sync), this report confirms WHAT landed and measures yield. It is
the gate before scoring (stage 4 drops leads with no email — no point scoring an
unreachable lead).

It touches nothing — pure read. Run it before Clay (baseline), and again after each
Clay run to watch coverage climb.

Usage:
    py -3 gtm/scripts/enrich_status.py                       # NDC, Leads tab
    py -3 gtm/scripts/enrich_status.py --client NDC --tab Leads
"""

import argparse
import collections
import sys

# Reuse the connection layer from prescreen.py (same dir) — single source of truth
# for config loading + service-account auth, so it stays DRY and replicable.
from prescreen import load_config, connect


def nonempty(v) -> bool:
    return bool(str(v or "").strip())


def main():
    parser = argparse.ArgumentParser(description="Enrichment status report (read-only)")
    parser.add_argument("--client", default="NDC", help="Client (informational only)")
    parser.add_argument("--tab", default="Leads", help="Source tab (default: Leads)")
    args = parser.parse_args()

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

    def is_disq(r):
        return str(r.get("status", "")).strip().lower() == "disqualified"

    disq = [r for r in rows if is_disq(r)]
    pool = [r for r in rows if not is_disq(r)]          # the enrich pool
    p = len(pool)

    with_email = [r for r in pool if nonempty(r.get("email"))]
    with_size = [r for r in pool if nonempty(r.get("company_size"))]
    with_ind = [r for r in pool if nonempty(r.get("industry"))]
    conf = collections.Counter(
        str(r.get("email_confidence", "")).strip() or "(blank)" for r in with_email)

    def pct(x, base):
        return f"{x} ({100 * x // base if base else 0}%)"

    print("\n" + "=" * 60)
    print(f"  ENRICHMENT STATUS — {args.client} (read-only)")
    print("=" * 60)
    print(f"  Total leads               : {n}")
    print(f"  Disqualified (excluded)   : {len(disq)}")
    print(f"  Enrich pool (kept)        : {p}")
    print(f"\n  POOL COVERAGE:")
    print(f"    With email (enriched)   : {pct(len(with_email), p)}")
    print(f"    Missing email           : {pct(p - len(with_email), p)}")
    print(f"    With company_size       : {pct(len(with_size), p)}")
    print(f"    With industry           : {pct(len(with_ind), p)}")
    print(f"\n  email_confidence (of enriched): {dict(conf)}")
    print(f"\n  Ready to score (has email): {len(with_email)}")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
