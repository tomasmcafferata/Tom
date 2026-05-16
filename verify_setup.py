#!/usr/bin/env python3
"""
Pre-flight check — run this before main.py to verify everything is configured.
Usage: python verify_setup.py
"""

import os
import sys
import json


def check(label, ok, detail=""):
    status = "OK" if ok else "FAIL"
    print(f"  [{status}] {label}")
    if detail and not ok:
        print(f"         → {detail}")
    return ok


def main():
    print("\n" + "=" * 55)
    print("  EMAIL RESPONSE AGGREGATOR — PRE-FLIGHT CHECK")
    print("=" * 55 + "\n")

    all_ok = True

    # 1. .env file
    print("1. Environment variables (.env)")
    if not os.path.exists(".env"):
        check(".env file", False, "Create a .env file with your secrets. See setup_guide.md.")
        print("\n  Cannot continue without .env. Exiting.\n")
        sys.exit(1)

    with open(".env") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip())

    required_vars = [
        "INSTANTLY_API_KEY",
        "ANTHROPIC_API_KEY",
        "SLACK_BOT_TOKEN",
        "SLACK_APP_TOKEN",
        "SLACK_CHANNEL_ID",
        "GOOGLE_SHEET_ID",
    ]
    for var in required_vars:
        val = os.environ.get(var, "")
        all_ok &= check(var, bool(val), f"Missing in .env")

    # MS credentials (optional but needed for Agupá)
    ms_vars = ["MS_AGUPA_CLIENT_ID", "MS_AGUPA_TENANT_ID", "MS_AGUPA_CLIENT_SECRET"]
    for var in ms_vars:
        val = os.environ.get(var, "")
        check(var, bool(val), "Missing — Agupá Microsoft emails won't work")

    # 2. Credential files
    print("\n2. Credential files")
    for f in ["credentials/service_account.json", "credentials/gmail_oauth_credentials.json"]:
        exists = os.path.exists(f)
        all_ok &= check(f, exists, "Download from Google Cloud Console. See setup_guide.md.")
        if exists:
            with open(f) as fh:
                try:
                    json.load(fh)
                except json.JSONDecodeError:
                    all_ok &= check(f"  {f} valid JSON", False, "File is not valid JSON")

    # 3. Config
    print("\n3. Config file")
    try:
        import yaml
        with open("config.yaml") as f:
            config = yaml.safe_load(f)
        check("config.yaml loads", True)
        clients = config.get("clients", [])
        check(f"  {len(clients)} clients configured", len(clients) > 0)
        for c in clients:
            ctx = c.get("context_file", "")
            if ctx:
                has_content = os.path.exists(ctx) and os.path.getsize(ctx) > 100
                check(f"  {c['name']} context ({ctx})", has_content,
                      "Empty template — AI responses will be generic")
    except Exception as e:
        all_ok &= check("config.yaml", False, str(e))

    # 4. Python dependencies
    print("\n4. Python dependencies")
    deps = {
        "yaml": "pyyaml",
        "anthropic": "anthropic",
        "slack_bolt": "slack-bolt",
        "slack_sdk": "slack-sdk",
        "gspread": "gspread",
        "google.oauth2": "google-auth",
        "requests": "requests",
        "msal": "msal",
    }
    for module, pip_name in deps.items():
        try:
            __import__(module)
            check(module, True)
        except ImportError:
            all_ok &= check(module, False, f"pip install {pip_name}")

    # 5. API connectivity
    print("\n5. API connectivity")
    import requests as req

    # Instantly
    try:
        r = req.get("https://api.instantly.ai/api/v2/campaigns",
                     headers={"Authorization": f"Bearer {os.environ.get('INSTANTLY_API_KEY', '')}"},
                     params={"limit": 1}, timeout=10)
        if r.status_code == 200:
            data = r.json()
            items = data.get("items", data.get("data", []))
            check(f"Instantly API — {len(items)} campaigns found", True)
        elif r.status_code == 401:
            all_ok &= check("Instantly API", False, "401 Unauthorized — regenerate your API key in Instantly")
        else:
            all_ok &= check("Instantly API", False, f"{r.status_code}: {r.text[:100]}")
    except Exception as e:
        all_ok &= check("Instantly API", False, str(e)[:100])

    # Slack
    try:
        r = req.post("https://slack.com/api/auth.test",
                      headers={"Authorization": f"Bearer {os.environ.get('SLACK_BOT_TOKEN', '')}"},
                      timeout=10)
        data = r.json()
        if data.get("ok"):
            check(f"Slack API — bot: {data.get('user', '?')}", True)
        else:
            all_ok &= check("Slack API", False, data.get("error", "Unknown error"))
    except Exception as e:
        all_ok &= check("Slack API", False, str(e)[:100])

    # Google Sheets
    try:
        from sheets_crm import SheetsCRM
        crm = SheetsCRM(os.environ.get("GOOGLE_SHEET_ID", ""),
                         config.get("google_credentials_path", "credentials/service_account.json"))
        check("Google Sheets API", True)
    except Exception as e:
        all_ok &= check("Google Sheets API", False, str(e)[:100])

    # Anthropic
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))
        msg = client.messages.create(model="claude-sonnet-4-6", max_tokens=10,
                                      messages=[{"role": "user", "content": "Say OK"}])
        check("Anthropic API", True)
    except Exception as e:
        all_ok &= check("Anthropic API", False, str(e)[:100])

    # Summary
    print("\n" + "=" * 55)
    if all_ok:
        print("  ALL CHECKS PASSED — run: python main.py")
    else:
        print("  SOME CHECKS FAILED — fix the issues above first")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()
