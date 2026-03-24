# Email Response Aggregator — Setup Guide

Step-by-step setup for someone with zero code experience.

---

## Step 0: Install Python

1. Go to https://www.python.org/downloads/
2. Download Python 3.11+ and install it
3. During install, **check "Add Python to PATH"**
4. Open Terminal (Mac) or Command Prompt (Windows)
5. Run: `python --version` — should show 3.11+

---

## Step 1: Install Dependencies

In your terminal, navigate to this project folder and run:

```bash
pip install -r requirements.txt
```

---

## Step 2: Get Your Instantly API Key

1. Log into https://app.instantly.ai
2. Go to **Settings → Integrations → API**
3. Copy your API key
4. Paste it in `config.yaml` under `instantly_api_key`

---

## Step 3: Set Up Google Sheets CRM

### Create the Sheet
1. Go to https://sheets.google.com and create a new spreadsheet
2. Name it "Email CRM" (or whatever you want)
3. Copy the Sheet ID from the URL:
   `https://docs.google.com/spreadsheets/d/`**THIS_PART**`/edit`
4. Paste it in `config.yaml` under `google_sheet_id`

### Create a Service Account (for Sheets access)
1. Go to https://console.cloud.google.com
2. Create a new project (e.g., "Email Aggregator")
3. Enable the **Google Sheets API**:
   - Search "Google Sheets API" in the search bar → Enable
4. Enable the **Google Drive API**:
   - Search "Google Drive API" → Enable
5. Create a Service Account:
   - Go to **APIs & Services → Credentials**
   - Click **Create Credentials → Service Account**
   - Name it "email-aggregator"
   - Click **Done**
6. Create a key:
   - Click on the service account you just created
   - Go to **Keys → Add Key → Create New Key → JSON**
   - Save the downloaded file as `credentials/service_account.json` in this project
7. Share your Google Sheet:
   - Open the JSON file and find the `client_email` field
   - Go to your Google Sheet → click **Share**
   - Paste the service account email and give it **Editor** access

---

## Step 4: Set Up Gmail Draft Creation (for Google inboxes)

### Create OAuth2 Credentials
1. In Google Cloud Console, go to **APIs & Services → Credentials**
2. Click **Create Credentials → OAuth Client ID**
3. If prompted, configure the OAuth consent screen:
   - User Type: **External**
   - App name: "Email Aggregator"
   - Add your email as a test user
4. Application type: **Desktop App**
5. Download the JSON file
6. Save it as `credentials/gmail_oauth_credentials.json`
7. Enable the **Gmail API**:
   - Search "Gmail API" in the search bar → Enable

### First Run Auth
The first time you run the script, it will open a browser window for each
Gmail inbox. Log in with that inbox's Google account and grant permission.
Tokens are saved so you only do this once per inbox.

---

## Step 5: Set Up Microsoft Outlook (for Microsoft inboxes, skip if none)

1. Go to https://portal.azure.com → **Azure Active Directory → App registrations**
2. Click **New Registration**
   - Name: "Email Aggregator"
   - Supported accounts: "Accounts in any organizational directory"
3. Note the **Application (client) ID** and **Directory (tenant) ID**
4. Go to **Certificates & secrets → New client secret** → copy the value
5. Go to **API permissions → Add permission → Microsoft Graph → Application permissions**
   - Add: `Mail.ReadWrite`
   - Click **Grant admin consent**
6. Add to `config.yaml`:

```yaml
microsoft:
  client_id: "YOUR_CLIENT_ID"
  tenant_id: "YOUR_TENANT_ID"
  client_secret: "YOUR_CLIENT_SECRET"
```

---

## Step 6: Get Your Anthropic API Key

1. Go to https://console.anthropic.com
2. Create an account and go to **API Keys**
3. Create a new key and copy it
4. Paste it in `config.yaml` under `anthropic_api_key`

**Cost**: ~$0.003 per reply classified + drafted. For 100 replies/month ≈ $0.30/month.

---

## Step 7: Configure Your Clients

Edit `config.yaml` — update each client's:
- `name` — how you refer to them
- `tone` — how the AI should write (e.g., "professional and friendly")
- `service_description` — one sentence about what they offer
- `scheduling_link` — their Calendly/Cal.com link
- `inboxes` — email + provider (google/microsoft)

---

## Step 8: Run It

### Process new replies once:
```bash
python main.py
```

### Run continuously (checks every 5 minutes):
```bash
python main.py --loop
```

### Generate follow-ups for stale leads:
```bash
python main.py --followups
```

### Run both on a schedule (recommended):
```bash
# Terminal 1: continuous reply processing
python main.py --loop

# Terminal 2: daily follow-ups (run once a day)
python main.py --followups
```

---

## How It Works

1. **Polls Instantly** for new campaign replies every 5 minutes
2. **Classifies** each reply (interested / not interested / OOO / bounce / question / meeting)
3. **Adds/updates** the lead in your Google Sheet CRM
4. **Generates** an AI response draft using Claude
5. **Creates a draft** in the original inbox (Gmail or Outlook)
6. **You review** the draft and hit send (or edit first)

---

## Google Sheet Columns

| Column | Description |
|--------|-------------|
| Lead Email | The lead's email |
| Lead Name | Auto-extracted from the reply |
| Company | Auto-extracted from email domain |
| Client | Which of your clients this is for |
| Campaign | Instantly campaign name |
| Inbox | Which inbox received the reply |
| Status | New Reply → Interested → In Conversation → Meeting Booked |
| Classification | AI classification (interested/not_interested/ooo/etc.) |
| First Reply Date | When they first replied |
| Last Reply Date | Most recent activity |
| Reply Count | Total replies in thread |
| Last Reply Snippet | Preview of their last message |
| Generated Draft | The AI-generated response |
| Notes | Your notes |

---

## Troubleshooting

**"No new replies found"** — Check that your Instantly API key is correct and you have active campaigns with replies.

**Gmail auth fails** — Make sure you added your email as a test user in the OAuth consent screen, and that the Gmail API is enabled.

**Google Sheets error** — Make sure you shared the sheet with the service account email (found in `credentials/service_account.json`).

**Microsoft auth fails** — Make sure admin consent was granted for Mail.ReadWrite permission.

---

## File Structure

```
├── config.yaml              ← Your settings (edit this)
├── credentials/
│   ├── service_account.json ← Google Sheets access
│   └── gmail_oauth_credentials.json ← Gmail draft access
├── main.py                  ← Run this
├── instantly_client.py      ← Instantly API
├── sheets_crm.py            ← Google Sheets CRM
├── response_generator.py    ← Claude AI drafts
├── draft_creator.py         ← Gmail/Outlook drafts
├── state.json               ← Auto-generated, tracks processed replies
├── requirements.txt
└── setup_guide.md           ← You are here
```
