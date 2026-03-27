# Email Response Aggregator — Setup Guide

Step-by-step setup. No code experience needed.

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

## Step 2: Set Up Slack (for reviewing & approving replies)

This is where you'll review all replies from one place.

### Create a Slack App

1. Go to https://api.slack.com/apps
2. Click **Create New App → From scratch**
3. Name: "Email Aggregator" — pick your workspace
4. You're now on the app settings page

### Enable Socket Mode (no public URL needed)

1. In the left sidebar, click **Socket Mode**
2. Toggle it **ON**
3. It will ask you to create an App-Level Token:
   - Name: "socket-token"
   - Scope: `connections:write`
   - Click **Generate**
4. **Copy the token** (starts with `xapp-...`) → paste in `config.yaml` under `slack.app_token`

### Set Bot Permissions

1. In the left sidebar, click **OAuth & Permissions**
2. Scroll to **Scopes → Bot Token Scopes** and add:
   - `chat:write`
   - `chat:write.public`
3. Scroll up and click **Install to Workspace** → Allow
4. **Copy the Bot User OAuth Token** (starts with `xoxb-...`) → paste in `config.yaml` under `slack.bot_token`

### Enable Interactivity (for buttons & modals)

1. In the left sidebar, click **Interactivity & Shortcuts**
2. Toggle **ON**
3. Since we use Socket Mode, you do NOT need a Request URL — just toggle it on

### Create the Channel

1. In Slack, create a channel (e.g., `#email-replies`)
2. Right-click the channel name → **View channel details**
3. Scroll to the bottom — copy the **Channel ID** (e.g., `C0123456789`)
4. Paste in `config.yaml` under `slack.channel_id`
5. Invite the bot to the channel: type `/invite @Email Aggregator` in the channel

---

## Step 3: Get Your Instantly API Key

1. Log into https://app.instantly.ai
2. Go to **Settings → Integrations → API**
3. Copy your API key
4. Paste it in `config.yaml` under `instantly_api_key`

---

## Step 4: Set Up Google Sheets CRM

### Create the Sheet
1. Go to https://sheets.google.com and create a new spreadsheet
2. Name it "Email CRM" (or whatever you want)
3. Copy the Sheet ID from the URL:
   `https://docs.google.com/spreadsheets/d/`**THIS_PART**`/edit`
4. Paste in `config.yaml` under `google_sheet_id`

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

## Step 5: Set Up Gmail Sending (for Google inboxes)

### Enable Gmail API
1. In Google Cloud Console (same project from Step 4)
2. Search "Gmail API" → Enable it

### Create OAuth2 Credentials
1. Go to **APIs & Services → Credentials**
2. Click **Create Credentials → OAuth Client ID**
3. If prompted, configure the OAuth consent screen:
   - User Type: **External**
   - App name: "Email Aggregator"
   - Add your email as a test user
   - Add ALL your Gmail inbox emails as test users too
4. Application type: **Desktop App**
5. Download the JSON file
6. Save it as `credentials/gmail_oauth_credentials.json`

### First Run Auth
The first time you approve a reply in Slack, the script will open a browser
for each Gmail inbox to authorize sending. Log in with that inbox's Google
account and grant permission. Tokens are saved so you only do this once.

---

## Step 6: Set Up Microsoft Outlook (skip if you only have Google inboxes)

1. Go to https://portal.azure.com → **Azure Active Directory → App registrations**
2. Click **New Registration**
   - Name: "Email Aggregator"
   - Supported accounts: "Accounts in any organizational directory"
3. Note the **Application (client) ID** and **Directory (tenant) ID**
4. Go to **Certificates & secrets → New client secret** → copy the value
5. Go to **API permissions → Add permission → Microsoft Graph → Application permissions**
   - Add: `Mail.Send` and `Mail.ReadWrite`
   - Click **Grant admin consent**
6. Uncomment and fill the `microsoft:` section in `config.yaml`

---

## Step 7: Get Your Anthropic API Key

1. Go to https://console.anthropic.com
2. Create an account and go to **API Keys**
3. Create a new key and copy it
4. Paste it in `config.yaml` under `anthropic_api_key`

**Cost**: ~$0.003 per reply classified + drafted. For 100 replies/month = ~$0.30/month.

---

## Step 8: Configure Your Clients

Edit `config.yaml` — update each client's:
- `name` — how you refer to them
- `tone` — how the AI should write (e.g., "professional and friendly")
- `service_description` — one sentence about what they offer
- `scheduling_link` — their Calendly/Cal.com link
- `inboxes` — email + provider (google/microsoft)

---

## Step 9: Run It

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

### Recommended: run both
```bash
# Terminal 1: continuous reply processing
python main.py --loop

# Terminal 2: daily follow-ups (run once a day)
python main.py --followups
```

---

## How It Works

```
Instantly (campaign replies)
       │
       ▼
  Python script (polls every 5 min)
       │
       ├─→ Claude AI classifies reply
       ├─→ Google Sheet CRM updated
       ├─→ Claude AI generates response
       │
       ▼
  Slack channel (#email-replies)
       │
       ├─ [Approve & Send] → email sent from correct inbox
       ├─ [Edit & Send]    → edit in modal, then sent
       └─ [Skip]           → ignored
```

1. Script polls Instantly for new campaign replies every 5 minutes
2. Each reply is classified (interested / not interested / OOO / bounce / question / meeting)
3. Lead is added/updated in your Google Sheet CRM
4. For actionable replies, Claude generates a response matching the client's tone
5. A Slack notification shows the reply + proposed response with 3 buttons
6. You click **Approve & Send** → email is sent from the original inbox automatically
7. Or click **Edit & Send** → tweak the text in a popup → then it sends
8. Or click **Skip** → nothing happens

All from one Slack channel. No need to log into any inbox.

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

**"No new replies found"**
Check that your Instantly API key is correct and you have active campaigns with replies.

**Slack buttons don't work**
Make sure Socket Mode is ON and Interactivity is ON in your Slack app settings.

**Gmail auth fails**
Make sure you added ALL inbox emails as test users in the OAuth consent screen, and Gmail API is enabled.

**Google Sheets error**
Make sure you shared the sheet with the service account email (in `credentials/service_account.json`).

**Microsoft auth fails**
Make sure admin consent was granted for Mail.Send permission.

**Slack message says "Reply data expired"**
This happens if the script was restarted between posting and clicking the button. Pending replies are stored in memory. For production use, you'd want to persist these — but for 3 clients this is unlikely to be an issue.

---

## File Structure

```
├── config.yaml              ← Your settings (edit this)
├── credentials/
│   ├── service_account.json           ← Google Sheets access
│   └── gmail_oauth_credentials.json   ← Gmail sending auth
├── main.py                  ← Run this
├── instantly_client.py      ← Instantly API
├── sheets_crm.py            ← Google Sheets CRM
├── response_generator.py    ← Claude AI classification + drafts
├── email_sender.py          ← Sends emails via Gmail/Outlook API
├── slack_handler.py         ← Slack notifications + button handling
├── state.json               ← Auto-generated, tracks processed replies
├── requirements.txt
└── setup_guide.md           ← You are here
```
