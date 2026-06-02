#!/usr/bin/env python3
"""
ONE-TIME SETUP — NDC Lead Database
====================================
Configures the Google Sheet with tabs, headers, formatting, and data validation.
Run once. Safe to re-run: skips tabs that already exist and re-applies headers.

Usage:
    python setup_sheet.py
"""

import gspread
from google.oauth2.service_account import Credentials
from gspread_formatting import (
    format_cell_range, CellFormat, TextFormat, Color,
    set_frozen, DataValidationRule, BooleanCondition,
    set_data_validation_for_cell_range
)

# ─── CONFIG ───────────────────────────────────────────────────────────────────

SHEET_ID = "1IE_KZpTBSzYE6i9_fCRcDptgpDjLh4ZXqBQOOW1jmQY"
CREDENTIALS_PATH = "credentials/service_account.json"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# ─── SCHEMA ───────────────────────────────────────────────────────────────────

LEADS_HEADERS = [
    # Identity
    "lead_id",          # A  hash(email+company), dedup key
    "email",            # B
    "first_name",       # C
    "last_name",        # D
    "title",            # E  exact LinkedIn title
    "company",          # F
    "company_size",     # G  employee range
    "industry",         # H  vertical
    "location",         # I
    "linkedin_url",     # J

    # Source
    "source_type",      # K  linkedhelper | exhibitor_list | manual
    "source_batch",     # L  filename or event name
    "import_date",      # M

    # Enrichment (Clay)
    "enriched",         # N  TRUE/FALSE
    "enrichment_date",  # O
    "email_confidence", # P  0-100
    "company_intel",    # Q  key account snippet from Clay

    # Segmentation
    "track",            # R  trigger | base
    "icp_segment",      # S  logistics | food_bev | healthcare | retail | tech | manufacturing | other
    "icp_score",        # T  0-100
    "icp_tier",         # U  1 | 2 | 3 | 0=disqualified

    # Lifecycle
    "status",           # V  see STATUS_VALUES
    "current_campaign", # W  Instantly campaign name
    "last_contact_date",# X
    "campaign_count",   # Y  total times contacted
    "cooling_until",    # Z  date eligible for re-engagement

    # Outcome
    "reply_classification", # AA  interested | question | meeting | not_interested | ooo | bounce
    "do_not_contact",       # AB  TRUE/FALSE — permanent block
    "notes",                # AC
]

CAMPAIGNS_HEADERS = [
    "campaign_id",          # auto-increment
    "campaign_name",        # e.g. "NDC — Logistics — Base — 2026-W21"
    "client",               # NDC
    "icp_segment",          # which segment this targets
    "track",                # trigger | base | re-engagement
    "sequence_name",        # which Instantly sequence
    "start_date",
    "end_date",
    "lead_count",           # leads uploaded to Instantly
    "sent_count",           # emails actually sent (from sync)
    "reply_count",
    "interested_count",
    "meeting_count",
    "bounce_count",
    "reply_rate",           # formula: reply_count/sent_count
    "instantly_campaign_id",# for API sync
    "notes",
]

PIPELINE_HEADERS = [
    "metric", "value", "notes"
]

STATUS_VALUES = [
    "new",
    "disqualified",
    "enriched",
    "queued",
    "active",
    "cooling",
    "replied",
    "interested",
    "meeting_booked",
    "converted",
    "not_interested",
    "unsubscribed",
    "bounced",
    "do_not_contact",
]

SEGMENT_VALUES = [
    "logistics",
    "food_bev",
    "healthcare",
    "retail",
    "tech",
    "manufacturing",
    "other",
]

TRACK_VALUES = ["trigger", "base"]

# ─── HELPERS ──────────────────────────────────────────────────────────────────

HEADER_FORMAT = CellFormat(
    backgroundColor=Color(0.18, 0.18, 0.18),   # dark grey
    textFormat=TextFormat(bold=True, foregroundColor=Color(1, 1, 1), fontSize=10),
)

SUBHEADER_FORMAT = CellFormat(
    backgroundColor=Color(0.9, 0.9, 0.9),
    textFormat=TextFormat(bold=True, fontSize=10),
)


def get_or_create_sheet(spreadsheet, title: str, rows: int = 2000, cols: int = 30):
    try:
        ws = spreadsheet.worksheet(title)
        print(f"  [EXISTS] Tab '{title}' — skipping creation")
        return ws
    except gspread.exceptions.WorksheetNotFound:
        ws = spreadsheet.add_worksheet(title=title, rows=rows, cols=cols)
        print(f"  [CREATED] Tab '{title}'")
        return ws


def apply_headers(ws, headers: list, color: CellFormat = None):
    ws.update("A1", [headers], value_input_option="USER_ENTERED")
    end_col = chr(ord("A") + len(headers) - 1) if len(headers) <= 26 else "AC"
    fmt = color or HEADER_FORMAT
    format_cell_range(ws, f"A1:{end_col}1", fmt)
    set_frozen(ws, rows=1)
    print(f"  [OK] Headers set ({len(headers)} columns)")


def add_dropdown_validation(ws, col_letter: str, values: list, start_row: int = 2, end_row: int = 2000):
    rule = DataValidationRule(
        BooleanCondition("ONE_OF_LIST", values),
        showCustomUi=True,
        strict=False,
    )
    set_data_validation_for_cell_range(ws, f"{col_letter}{start_row}:{col_letter}{end_row}", rule)
    print(f"  [OK] Dropdown validation on column {col_letter} ({len(values)} options)")


# ─── PIPELINE ROWS ────────────────────────────────────────────────────────────

def build_pipeline_rows(leads_tab: str = "Leads") -> list:
    """COUNTIF formulas that summarize the Leads tab."""
    L = leads_tab
    # status column is V (index 21, col 22)
    # track column is R (index 17, col 18)
    # icp_tier column is U (index 20, col 21)
    return [
        ["=== PIPELINE STATUS ===", "", ""],
        ["new",           f"=COUNTIF('{L}'!V:V,\"new\")",            "Not yet enriched"],
        ["disqualified",  f"=COUNTIF('{L}'!V:V,\"disqualified\")",   "ICP score too low"],
        ["enriched",      f"=COUNTIF('{L}'!V:V,\"enriched\")",       "Ready to queue"],
        ["queued",        f"=COUNTIF('{L}'!V:V,\"queued\")",         "Assigned to next campaign"],
        ["active",        f"=COUNTIF('{L}'!V:V,\"active\")",         "Currently in a campaign"],
        ["cooling",       f"=COUNTIF('{L}'!V:V,\"cooling\")",        "Waiting cooldown (90 days)"],
        ["replied",       f"=COUNTIF('{L}'!V:V,\"replied\")",        "Replied (any type)"],
        ["interested",    f"=COUNTIF('{L}'!V:V,\"interested\")",     "Positive reply"],
        ["meeting_booked",f"=COUNTIF('{L}'!V:V,\"meeting_booked\")", "Meeting confirmed"],
        ["converted",     f"=COUNTIF('{L}'!V:V,\"converted\")",      "Closed project"],
        ["not_interested",f"=COUNTIF('{L}'!V:V,\"not_interested\")", ""],
        ["unsubscribed",  f"=COUNTIF('{L}'!V:V,\"unsubscribed\")",   "Permanent - do not contact"],
        ["bounced",       f"=COUNTIF('{L}'!V:V,\"bounced\")",        "Hard bounce"],
        ["do_not_contact",f"=COUNTIF('{L}'!V:V,\"do_not_contact\")", "Permanent block"],
        ["", "", ""],
        ["=== TOTALS ===", "", ""],
        ["TOTAL LEADS",     f"=COUNTA('{L}'!A:A)-1",                         "Excludes header"],
        ["CONTACTABLE",     f"=COUNTIFS('{L}'!AB:AB,\"FALSE\",'{L}'!V:V,\"<>unsubscribed\",'{L}'!V:V,\"<>bounced\",'{L}'!V:V,\"<>do_not_contact\")", ""],
        ["AVAILABLE NOW",   f"=COUNTIFS('{L}'!V:V,\"enriched\")+COUNTIFS('{L}'!V:V,\"queued\")", "Ready for campaigns"],
        ["", "", ""],
        ["=== BY SEGMENT ===", "", ""],
        ["logistics",      f"=COUNTIF('{L}'!S:S,\"logistics\")",     ""],
        ["food_bev",       f"=COUNTIF('{L}'!S:S,\"food_bev\")",      ""],
        ["healthcare",     f"=COUNTIF('{L}'!S:S,\"healthcare\")",    ""],
        ["retail",         f"=COUNTIF('{L}'!S:S,\"retail\")",        ""],
        ["tech",           f"=COUNTIF('{L}'!S:S,\"tech\")",          ""],
        ["manufacturing",  f"=COUNTIF('{L}'!S:S,\"manufacturing\")", ""],
        ["other",          f"=COUNTIF('{L}'!S:S,\"other\")",         ""],
        ["", "", ""],
        ["=== BY TRACK ===", "", ""],
        ["trigger",  f"=COUNTIF('{L}'!R:R,\"trigger\")", "Event-based (exhibitor lists)"],
        ["base",     f"=COUNTIF('{L}'!R:R,\"base\")",    "Sales Navigator batch"],
        ["", "", ""],
        ["=== BY TIER ===", "", ""],
        ["Tier 1 (80-100)",  f"=COUNTIF('{L}'!U:U,1)", "Highest priority"],
        ["Tier 2 (60-79)",   f"=COUNTIF('{L}'!U:U,2)", ""],
        ["Tier 3 (40-59)",   f"=COUNTIF('{L}'!U:U,3)", "Batch only"],
        ["Disqualified (<40)",f"=COUNTIF('{L}'!U:U,0)","Excluded from campaigns"],
        ["", "", ""],
        ["=== CAPACITY ===", "", ""],
        ["Inboxes",          "4",   "NDC inboxes in Instantly"],
        ["Emails/inbox/day", "30",  "Conservative sending limit"],
        ["Sequence days",    "21",  "Campaign duration"],
        ["Sequence steps",   "4",   "Emails per lead"],
        ["Capacity/cycle",   "=B45*B46*B47/B48", "Leads per campaign cycle"],
    ]


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    print("\n" + "=" * 55)
    print("  NDC LEAD DATABASE — SHEET SETUP")
    print("=" * 55)

    # Auth
    creds = Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=SCOPES)
    gc = gspread.authorize(creds)
    spreadsheet = gc.open_by_key(SHEET_ID)
    print(f"\n  Connected: '{spreadsheet.title}'\n")

    # ── Tab 1: Leads ──────────────────────────────────────────
    print("[ Tab: Leads ]")
    leads_ws = get_or_create_sheet(spreadsheet, "Leads", rows=3000, cols=30)
    apply_headers(leads_ws, LEADS_HEADERS)

    # Dropdown validations
    # V = status (col 22, letter V)
    add_dropdown_validation(leads_ws, "V", STATUS_VALUES)
    # R = track (col 18)
    add_dropdown_validation(leads_ws, "R", TRACK_VALUES)
    # S = icp_segment (col 19)
    add_dropdown_validation(leads_ws, "S", SEGMENT_VALUES)

    # ── Tab 2: Campaigns ──────────────────────────────────────
    print("\n[ Tab: Campaigns ]")
    camp_ws = get_or_create_sheet(spreadsheet, "Campaigns", rows=500, cols=20)
    apply_headers(camp_ws, CAMPAIGNS_HEADERS)
    add_dropdown_validation(camp_ws, "D", SEGMENT_VALUES)  # icp_segment
    add_dropdown_validation(camp_ws, "E", ["trigger", "base", "re-engagement"])  # track

    # ── Tab 3: Pipeline ───────────────────────────────────────
    print("\n[ Tab: Pipeline ]")
    pipe_ws = get_or_create_sheet(spreadsheet, "Pipeline", rows=100, cols=5)
    apply_headers(pipe_ws, PIPELINE_HEADERS, color=SUBHEADER_FORMAT)

    # Write pipeline formulas
    pipeline_rows = build_pipeline_rows()
    pipe_ws.update("A2", pipeline_rows, value_input_option="USER_ENTERED")
    print(f"  [OK] {len(pipeline_rows)} pipeline rows written")

    # Format section headers in pipeline
    section_rows = [i + 2 for i, row in enumerate(pipeline_rows) if str(row[0]).startswith("===")]
    for row_num in section_rows:
        format_cell_range(pipe_ws, f"A{row_num}:C{row_num}", SUBHEADER_FORMAT)

    # ── Delete default Sheet1 if it exists ────────────────────
    try:
        default = spreadsheet.worksheet("Sheet1")
        spreadsheet.del_worksheet(default)
        print("\n  [OK] Removed default 'Sheet1'")
    except gspread.exceptions.WorksheetNotFound:
        pass

    print("\n" + "=" * 55)
    print("  SETUP COMPLETE")
    print(f"  Sheet: https://docs.google.com/spreadsheets/d/{SHEET_ID}")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()
