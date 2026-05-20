"""
Import leads from the raw Google Drive read_file_content result.

Source columns:  profile_url, full_name, first_name, last_name,
                 headline, location_name, current_company, current_company_position

Maps to NDC leads model and POSTs to the Apps Script web app endpoint.
"""

import json
import re
import sys
import time
import requests
from datetime import date

# ── CONFIG ────────────────────────────────────────────────────────────────────

SOURCE_FILE = "/root/.claude/projects/-home-user-Tom/f102f0c2-6aab-4755-b3ef-bdb3a353c6a9/tool-results/mcp-221b98c8-87f0-44a9-8444-416f60b8541a-read_file_content-1779304684770.txt"
API_URL     = "https://script.google.com/macros/s/AKfycbwYyA627VT6kzv3HSyBCcHQo0K0zZUdxC2RUdlZTSKJRT_3PcRw3bkRhMB9RPBcp4e-pw/exec"
SECRET      = "ndc-leads-2026"
BATCH_SIZE  = 50
SOURCE_BATCH = str(date.today())


# ── PARSE ─────────────────────────────────────────────────────────────────────

def parse_leads(filepath):
    with open(filepath) as f:
        raw = json.load(f)["fileContent"]

    lines = raw.splitlines()

    # Find header row (content uses markdown escaped underscores: profile\_url)
    header_line = None
    for i, line in enumerate(lines):
        if "profile" in line and "headline" in line and "first" in line:
            header_line = i
            break

    if header_line is None:
        print("ERROR: header row not found")
        sys.exit(1)

    # Unescape markdown backslash escapes (e.g. profile\_url → profile_url)
    def unescape(s):
        return s.replace("\\_", "_").replace("\\-", "-")

    headers = [unescape(h.strip()) for h in lines[header_line].split("|") if h.strip()]
    print(f"Headers found: {headers}")

    leads = []
    for line in lines[header_line + 1:]:
        # Skip separator rows (:-:) and empty lines
        if not line.strip() or ":-:" in line:
            continue
        cells = [unescape(c.strip()) for c in line.split("|")]
        # Remove leading/trailing empty cells from the split
        cells = [c for c in cells if c != ""]
        if len(cells) < len(headers):
            continue
        row = dict(zip(headers, cells[:len(headers)]))
        leads.append(row)

    print(f"Parsed {len(leads)} leads from source")
    return leads


def map_lead(row):
    return {
        "linkedin_url":              row.get("profile_url", "").strip(),
        "first_name":                row.get("first_name", "").strip(),
        "last_name":                 row.get("last_name", "").strip(),
        "title":                     row.get("current_company_position", "").strip()
                                     or row.get("headline", "").strip(),
        "company":                   row.get("current_company", "").strip(),
        "location":                  row.get("location_name", "").strip(),
        # enrichment defaults (empty until Clay pass)
        "email":                     "",
        "company_size":              "",
        "industry":                  "",
        "enriched":                  "false",
        "email_confidence":          "",
        "company_intel":             "",
        # segmentation defaults
        "track":                     "base",
        "icp_segment":               "",
        "icp_score":                 "",
        "icp_tier":                  "",
        # lifecycle defaults (status/import_date set by buildRow in Apps Script)
        "source_type":               "linkedin_sales_nav",
        "source_batch":              SOURCE_BATCH,
        "campaign_count":            0,
        "do_not_contact":            "false",
    }


# ── POST ──────────────────────────────────────────────────────────────────────

def post_batch(leads_batch, batch_num, total_batches):
    payload = {
        "secret": SECRET,
        "action": "append",
        "leads":  leads_batch,
    }
    for attempt in range(4):
        try:
            resp = requests.post(API_URL, json=payload, timeout=60)
            data = resp.json()
            print(f"  Batch {batch_num}/{total_batches}: {data}")
            return data
        except Exception as e:
            wait = 2 ** attempt
            print(f"  Batch {batch_num} attempt {attempt+1} failed: {e} — retrying in {wait}s")
            time.sleep(wait)
    print(f"  Batch {batch_num} FAILED after 4 attempts")
    return None


def main():
    raw_leads = parse_leads(SOURCE_FILE)
    mapped    = [map_lead(r) for r in raw_leads]

    batches = [mapped[i:i+BATCH_SIZE] for i in range(0, len(mapped), BATCH_SIZE)]
    print(f"\nUploading {len(mapped)} leads in {len(batches)} batches of {BATCH_SIZE}...\n")

    total_added   = 0
    total_skipped = 0

    for i, batch in enumerate(batches, 1):
        result = post_batch(batch, i, len(batches))
        if result and result.get("ok"):
            total_added   += result.get("added",   0)
            total_skipped += result.get("skipped", 0)
        time.sleep(1)  # avoid Apps Script rate limits

    print(f"\n✓ Done — added: {total_added}, skipped (duplicates): {total_skipped}")


if __name__ == "__main__":
    main()
