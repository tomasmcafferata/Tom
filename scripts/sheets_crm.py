"""
Google Sheets CRM — manages leads in a single master Google Sheet.

Sheet columns:
A: Lead Email
B: Lead Name
C: Company
D: Client
E: Campaign
F: Inbox
G: Status (New Reply | Interested | In Conversation | Meeting Booked | Not Interested | OOO | Bounce)
H: Classification
I: First Reply Date
J: Last Reply Date
K: Reply Count
L: Last Reply Snippet
M: Generated Draft
N: Notes
"""

import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Columns (1-indexed to match Sheets)
COL = {
    "email": 1,
    "name": 2,
    "company": 3,
    "client": 4,
    "campaign": 5,
    "inbox": 6,
    "status": 7,
    "classification": 8,
    "first_reply": 9,
    "last_reply": 10,
    "reply_count": 11,
    "last_snippet": 12,
    "draft": 13,
    "notes": 14,
}

HEADERS = [
    "Lead Email", "Lead Name", "Company", "Client", "Campaign",
    "Inbox", "Status", "Classification", "First Reply Date",
    "Last Reply Date", "Reply Count", "Last Reply Snippet",
    "Generated Draft", "Notes"
]

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


class SheetsCRM:
    def __init__(self, sheet_id: str, credentials_path: str):
        creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
        self.gc = gspread.authorize(creds)
        self.spreadsheet = self.gc.open_by_key(sheet_id)
        self._ensure_sheet_setup()

    def _ensure_sheet_setup(self):
        """Create the Leads sheet with headers if it doesn't exist."""
        try:
            self.sheet = self.spreadsheet.worksheet("Leads")
        except gspread.exceptions.WorksheetNotFound:
            self.sheet = self.spreadsheet.add_worksheet("Leads", rows=1000, cols=len(HEADERS))

        # Check if headers exist
        first_row = self.sheet.row_values(1)
        if not first_row or first_row[0] != HEADERS[0]:
            self.sheet.update("A1", [HEADERS])
            # Bold headers formatting
            self.sheet.format("A1:N1", {"textFormat": {"bold": True}})
            print("  [OK] Created Leads sheet with headers.")

    def find_lead_row(self, email: str, campaign: str) -> int | None:
        """Find the row number for a lead (by email + campaign combo). Returns None if not found."""
        all_emails = self.sheet.col_values(COL["email"])
        all_campaigns = self.sheet.col_values(COL["campaign"])

        # Pad campaigns list to match emails length
        while len(all_campaigns) < len(all_emails):
            all_campaigns.append("")

        for i, (e, c) in enumerate(zip(all_emails, all_campaigns)):
            if e.lower() == email.lower() and c == campaign:
                return i + 1  # 1-indexed
        return None

    def add_or_update_lead(self, lead: dict) -> int:
        """
        Add a new lead or update an existing one.
        Returns the row number.

        lead dict keys: email, name, company, client, campaign, inbox,
                        status, classification, reply_snippet, draft
        """
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        row_num = self.find_lead_row(lead["email"], lead.get("campaign", ""))

        if row_num:
            # Update existing lead
            self.sheet.update_cell(row_num, COL["last_reply"], now)
            self.sheet.update_cell(row_num, COL["last_snippet"], lead.get("reply_snippet", "")[:200])
            self.sheet.update_cell(row_num, COL["classification"], lead.get("classification", ""))
            self.sheet.update_cell(row_num, COL["status"], lead.get("status", "In Conversation"))

            # Increment reply count
            current_count = self.sheet.cell(row_num, COL["reply_count"]).value
            new_count = int(current_count or 0) + 1
            self.sheet.update_cell(row_num, COL["reply_count"], new_count)

            # Update draft if provided
            if lead.get("draft"):
                self.sheet.update_cell(row_num, COL["draft"], lead["draft"][:500])

            print(f"  [UPDATE] Row {row_num}: {lead['email']}")
            return row_num
        else:
            # New lead
            new_row = [
                lead.get("email", ""),
                lead.get("name", ""),
                lead.get("company", ""),
                lead.get("client", ""),
                lead.get("campaign", ""),
                lead.get("inbox", ""),
                lead.get("status", "New Reply"),
                lead.get("classification", ""),
                now,   # first reply
                now,   # last reply
                1,     # reply count
                lead.get("reply_snippet", "")[:200],
                lead.get("draft", "")[:500],
                "",    # notes
            ]
            self.sheet.append_row(new_row, value_input_option="USER_ENTERED")
            row_num = len(self.sheet.col_values(COL["email"]))
            print(f"  [NEW] Row {row_num}: {lead['email']}")
            return row_num

    def get_stale_leads(self, stale_days: int = 2) -> list:
        """Get leads that haven't replied in `stale_days` and are still active."""
        all_rows = self.sheet.get_all_records()
        stale = []
        now = datetime.now()

        for i, row in enumerate(all_rows):
            status = row.get("Status", "")
            if status not in ("New Reply", "Interested", "In Conversation"):
                continue

            last_reply = row.get("Last Reply Date", "")
            if not last_reply:
                continue

            try:
                last_dt = datetime.strptime(last_reply, "%Y-%m-%d %H:%M")
                delta = (now - last_dt).days
                if delta >= stale_days:
                    stale.append({**row, "_row_num": i + 2})  # +2 for header + 0-index
            except ValueError:
                continue

        return stale

    def update_cell(self, row: int, column_name: str, value: str):
        """Update a single cell by row number and column name."""
        col = COL.get(column_name)
        if col:
            self.sheet.update_cell(row, col, value)
