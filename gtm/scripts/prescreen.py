#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEAD PERSONA PRE-SCREEN  (generic, per-client)
==============================================
Free, pre-enrichment screen. Looks only at `title` + `location` (the data we already
have) and assigns a persona_tier so we decide HOW DEEP to enrich and never spend Clay
credits on leads the title already disqualifies.

This script is CLIENT-AGNOSTIC. The screening rules (keyword stems + geography) live in
clients/<client>/prescreen-rules.yaml — the executable mirror of that client's ICP.md.
To screen a different client: write their prescreen-rules.yaml and pass --client <name>.

Tiers (generic meaning; the keywords that define them are per-client):
    1  primary decision-maker            (enrich: YES)
    2  co-buyer / qualified influencer   (enrich: PROBABLE)
    3  ambiguous, needs enrichment to judge
    X  disqualified: wrong dept, no title, or outside the target geography

Usage:
    py -3 gtm/scripts/prescreen.py                       # dry-run (default): print + CSV
    py -3 gtm/scripts/prescreen.py --write               # also write verdict to the Sheet
    py -3 gtm/scripts/prescreen.py --client NDC --tab Leads

Verify: dry-run prints the tier distribution and writes a CSV you can open. The Sheet is
only touched with --write (status=disqualified for rejects, note tag on every row).
The write finds the status/notes columns BY HEADER NAME, so it is safe even if the sheet
column order has drifted. Nothing is overwritten silently.
"""

import os
import sys
import csv
import re
import argparse
from datetime import date

# ─── PATHS (resolved relative to repo root so it runs from anywhere) ──────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
CONFIG_PATH = os.path.join(REPO_ROOT, "gtm", "leads", "config.yaml")
OUTPUT_DIR = os.path.join(REPO_ROOT, "gtm", "leads", "output")


def client_rules_path(client: str) -> str:
    return os.path.join(REPO_ROOT, "gtm", "clients", client, "prescreen-rules.yaml")


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


# ─── RULES (loaded per client — see clients/<client>/prescreen-rules.yaml) ─────
def load_rules(client: str) -> dict:
    """Load + compile the per-client screening rules. Returns a dict of compiled regex
    patterns plus the geography config. Fails loudly on a missing file or a bad regex."""
    try:
        import yaml
    except ImportError:
        sys.exit("[ERROR] PyYAML not installed. Run: py -3 -m pip install pyyaml")

    path = client_rules_path(client)
    if not os.path.exists(path):
        sys.exit(f"[ERROR] Pre-screen rules not found for client '{client}': {path}\n"
                 f"        Create it (copy an existing clients/*/prescreen-rules.yaml).")
    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}

    try:
        tiers = raw["tiers"]
        geo = raw["geography"]
        compiled = {
            "tier1":              re.compile(tiers["tier1_title"], re.IGNORECASE),
            "disqualify":         re.compile(tiers["disqualify_title"], re.IGNORECASE),
            "encargado_qualified": re.compile(tiers["encargado_qualified"], re.IGNORECASE),
            "tier2":              re.compile(tiers["tier2_title"], re.IGNORECASE),
            "encargado_bare":     re.compile(tiers["encargado_bare"], re.IGNORECASE),
            "geo_hints":          tuple(h.lower() for h in geo["hints"]),
            "geo_allow_empty":    bool(geo.get("allow_empty", True)),
        }
    except KeyError as e:
        sys.exit(f"[ERROR] Pre-screen rules for '{client}' missing key: {e} (file: {path})")
    except re.error as e:
        sys.exit(f"[ERROR] Bad regex in pre-screen rules for '{client}': {e} (file: {path})")
    return compiled


def is_in_geo(location: str, rules: dict) -> bool:
    """Empty location passes (unknown, decide later) if allow_empty. Otherwise it must
    contain one of the client's geography hints."""
    loc = (location or "").strip().lower()
    if not loc:
        return rules["geo_allow_empty"]
    return any(h in loc for h in rules["geo_hints"])


def classify(title: str, location: str, rules: dict) -> tuple:
    """Return (persona_tier, label, reason). persona_tier is 1/2/3 or 'X'."""
    t = (title or "").strip()
    if not is_in_geo(location, rules):
        return ("X", "disqualified", f"outside target geography: {location.strip()}")
    if not t:
        return ("X", "disqualified", "no title")
    # Tier 1 wins over department disqualifiers: a title like "Director de operaciones y
    # desarrollo comercial" is a buyer, not a reject.
    if rules["tier1"].search(t):
        return (1, "primary_decision_maker", "primary ops/owner decision-maker")
    if rules["disqualify"].search(t):
        return ("X", "disqualified", "wrong department / non-buyer")
    if rules["encargado_qualified"].search(t):
        return (2, "qualified_influencer", "encargado with relevant area")
    if rules["tier2"].search(t):
        return (2, "co_buyer", "commercial/admin/marketing")
    if rules["encargado_bare"].search(t):
        return (3, "ambiguous", "bare 'Encargado' — ambiguous")
    return (3, "uncertain", "no rule matched — needs enrichment to judge")


# ─── SHEET HELPERS ─────────────────────────────────────────────────────────────
def col_letter(idx0: int) -> str:
    """0-based column index → A1 column letter(s). 0→A, 26→AA, 27→AB."""
    n = idx0 + 1
    s = ""
    while n:
        n, rem = divmod(n - 1, 26)
        s = chr(65 + rem) + s
    return s


def find_column(headers: list, name: str) -> int:
    """Return the 0-based index of a column by (case-insensitive) header name, or exit.
    Reading is header-keyed so it's safe; writing must NOT guess a position — if the
    column moved, a positional write would corrupt data. So we look it up and fail loud."""
    lower = [h.strip().lower() for h in headers]
    if name.lower() not in lower:
        sys.exit(f"[ERROR] Column '{name}' not found in sheet header. Headers: {headers}")
    return lower.index(name.lower())


# ─── CONFIG / CONNECTION ──────────────────────────────────────────────────────
def load_config() -> dict:
    try:
        import yaml
    except ImportError:
        sys.exit("[ERROR] PyYAML not installed. Run: py -3 -m pip install pyyaml")
    if not os.path.exists(CONFIG_PATH):
        sys.exit(f"[ERROR] Config not found: {CONFIG_PATH}")
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def connect(config: dict):
    try:
        import gspread
        from google.oauth2.service_account import Credentials
    except ImportError as e:
        sys.exit(f"[ERROR] Missing dependency: {e}. Run: py -3 -m pip install "
                 f"gspread google-auth")
    creds_rel = config.get("google_credentials_path", "credentials/service_account.json")
    creds_path = creds_rel if os.path.isabs(creds_rel) else os.path.join(REPO_ROOT, creds_rel)
    if not os.path.exists(creds_path):
        sys.exit(f"[ERROR] Credentials not found: {creds_path}")
    gc = gspread.authorize(Credentials.from_service_account_file(creds_path, scopes=SCOPES))
    return gc


# ─── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Lead persona pre-screen (per-client)")
    parser.add_argument("--client", default="NDC",
                        help="Client folder under gtm/clients/ (default: NDC). "
                             "Loads clients/<client>/prescreen-rules.yaml")
    parser.add_argument("--write", action="store_true",
                        help="Write verdict back to the Sheet (default: dry-run)")
    parser.add_argument("--tier3-in", action="store_true",
                        help="Count Tier 3 as enrichable in the pool total")
    parser.add_argument("--tab", default="Leads", help="Source tab (default: Leads)")
    args = parser.parse_args()

    print("\n" + "=" * 60)
    print(f"  LEAD PERSONA PRE-SCREEN — {args.client}"
          + ("  [DRY-RUN]" if not args.write else "  [WRITE]"))
    print("=" * 60)

    rules = load_rules(args.client)
    print(f"\n[1/5] Rules loaded: clients/{args.client}/prescreen-rules.yaml")

    config = load_config()
    sheet_id = config.get("lead_db_sheet_id")
    if not sheet_id:
        sys.exit("[ERROR] lead_db_sheet_id missing in config.yaml")

    print(f"[2/5] Connecting...")
    gc = connect(config)
    ws = gc.open_by_key(sheet_id).worksheet(args.tab)
    print(f"      Tab '{args.tab}' opened.")

    print(f"[3/5] Reading leads...")
    rows = ws.get_all_records()
    n = len(rows)
    print(f"      {n} leads read.")
    if n == 0:
        sys.exit("[ERROR] No leads in the tab — nothing to screen.")

    print(f"[4/5] Classifying...")
    tally = {1: 0, 2: 0, 3: 0, "X": 0}
    reasons = {}
    today = date.today().strftime("%Y-%m-%d")
    out_rows = []          # for CSV
    status_col = []        # new status value per row (for --write)
    notes_col = []         # new notes value per row (for --write)

    for r in rows:
        tier, label, reason = classify(str(r.get("title", "")), str(r.get("location", "")), rules)
        tally[tier] += 1
        reasons[label] = reasons.get(label, 0) + 1

        out_rows.append({
            "lead_id": r.get("lead_id", ""),
            "first_name": r.get("first_name", ""),
            "last_name": r.get("last_name", ""),
            "title": r.get("title", ""),
            "company": r.get("company", ""),
            "location": r.get("location", ""),
            "persona_tier": tier,
            "label": label,
            "reason": reason,
        })

        # Build write-back values (preserve existing, never clobber silently).
        existing_status = str(r.get("status", "")).strip() or "new"
        new_status = "disqualified" if tier == "X" else existing_status
        status_col.append([new_status])

        existing_notes = str(r.get("notes", "")).strip()
        tag = f"[prescreen {today}] tier={tier} {label}: {reason}"
        new_notes = f"{existing_notes} | {tag}" if existing_notes else tag
        notes_col.append([new_notes])

    # Write CSV artifact (always — this is what enrichment consumes to prioritize).
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    csv_path = os.path.join(OUTPUT_DIR, f"prescreen_{args.client}_{today}.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    # ─── Report ───────────────────────────────────────────────────────────────
    def pct(x):
        return f"{x:5} ({100 * x // n}%)" if n else "0"
    pool_core = tally[1] + tally[2]
    pool_full = pool_core + tally[3]
    print(f"[5/5] Done.\n")
    print("  PERSONA TIERS:")
    print(f"    Tier 1 (primary, enrich YES)         : {pct(tally[1])}")
    print(f"    Tier 2 (co-buyer / qualified)        : {pct(tally[2])}")
    print(f"    Tier 3 (ambiguous / uncertain)       : {pct(tally[3])}")
    print(f"    Disqualified (dept/geo/no-title)     : {pct(tally['X'])}")
    print(f"\n  ENRICH POOL:")
    print(f"    Core  (Tier 1+2)        : {pool_core} leads")
    print(f"    +Tier3 (if budget)      : {pool_full} leads")
    print(f"\n  Breakdown by label: {reasons}")
    print(f"  CSV written: {csv_path}")

    # ─── Write-back ─────────────────────────────────────────────────────────────
    if args.write:
        print(f"\n  Writing back to Sheet (status + notes)...")
        headers = ws.row_values(1)
        status_letter = col_letter(find_column(headers, "status"))
        notes_letter = col_letter(find_column(headers, "notes"))
        ws.update(range_name=f"{status_letter}2:{status_letter}{n+1}",
                  values=status_col, value_input_option="USER_ENTERED")
        ws.update(range_name=f"{notes_letter}2:{notes_letter}{n+1}",
                  values=notes_col, value_input_option="USER_ENTERED")
        dq = tally["X"]
        print(f"  OK: {n} rows tagged in notes (col {notes_letter}), "
              f"{dq} marked status=disqualified (col {status_letter}).")
    else:
        print(f"\n  DRY-RUN: Sheet not modified. Re-run with --write to persist.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
