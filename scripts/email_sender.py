"""
Email Sender — sends emails from Gmail or Outlook inboxes.
Used after a reply is approved in Slack.
"""

import os
import json
import base64
from email.mime.text import MIMEText

from google.oauth2.credentials import Credentials as OAuthCredentials
from googleapiclient.discovery import build
import requests


class EmailSender:
    """Sends emails from Google or Microsoft inboxes."""

    GMAIL_SCOPES = [
        "https://www.googleapis.com/auth/gmail.send",
        "https://www.googleapis.com/auth/gmail.compose",
    ]

    def __init__(self, gmail_credentials_path: str = None, microsoft_config: dict = None):
        self.gmail_credentials_path = gmail_credentials_path
        self.microsoft_config = microsoft_config or {}
        self._gmail_services = {}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def send_email(
        self,
        inbox_email: str,
        to_email: str,
        subject: str,
        body: str,
        provider: str = "google",
        thread_id: str = None,
        in_reply_to: str = None,
    ):
        """Send an email from the specified inbox."""
        if provider == "google":
            self._send_gmail(inbox_email, to_email, subject, body, thread_id, in_reply_to)
        elif provider == "microsoft":
            self._send_outlook(inbox_email, to_email, subject, body)
        else:
            raise ValueError(f"Unknown provider: {provider}")

    # ------------------------------------------------------------------
    # Gmail
    # ------------------------------------------------------------------

    def _get_gmail_service(self, inbox_email: str):
        """Get or create Gmail API service for an inbox."""
        if inbox_email in self._gmail_services:
            return self._gmail_services[inbox_email]

        token_file = f"credentials/gmail_token_{inbox_email.replace('@', '_at_')}.json"

        creds = None
        if os.path.exists(token_file):
            creds = OAuthCredentials.from_authorized_user_file(token_file, self.GMAIL_SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                from google.auth.transport.requests import Request
                creds.refresh(Request())
                with open(token_file, "w") as f:
                    f.write(creds.to_json())
            else:
                # Need initial auth — open browser
                from google_auth_oauthlib.flow import InstalledAppFlow
                print(f"\n  [AUTH] Opening browser to authorize Gmail for {inbox_email}")
                print(f"  [AUTH] Log in with {inbox_email}!")
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.gmail_credentials_path, self.GMAIL_SCOPES
                )
                creds = flow.run_local_server(port=0)
                os.makedirs("credentials", exist_ok=True)
                with open(token_file, "w") as f:
                    f.write(creds.to_json())
                print(f"  [OK] Token saved for {inbox_email}")

        service = build("gmail", "v1", credentials=creds)
        self._gmail_services[inbox_email] = service
        return service

    def _send_gmail(self, inbox_email, to_email, subject, body, thread_id=None, in_reply_to=None):
        """Send an email via Gmail API."""
        service = self._get_gmail_service(inbox_email)

        message = MIMEText(body)
        message["to"] = to_email
        message["from"] = inbox_email
        message["subject"] = subject
        if in_reply_to:
            message["In-Reply-To"] = in_reply_to
            message["References"] = in_reply_to

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        send_body = {"raw": raw}
        if thread_id:
            send_body["threadId"] = thread_id

        service.users().messages().send(userId="me", body=send_body).execute()
        print(f"  [SENT] Gmail: {inbox_email} → {to_email}")

    # ------------------------------------------------------------------
    # Microsoft Outlook
    # ------------------------------------------------------------------

    def _get_ms_token(self) -> str:
        """Get Microsoft Graph access token."""
        import msal

        app = msal.ConfidentialClientApplication(
            self.microsoft_config["client_id"],
            authority=f"https://login.microsoftonline.com/{self.microsoft_config['tenant_id']}",
            client_credential=self.microsoft_config["client_secret"],
        )
        result = app.acquire_token_for_client(
            scopes=["https://graph.microsoft.com/.default"]
        )
        if "access_token" in result:
            return result["access_token"]
        raise Exception(f"MS auth failed: {result.get('error_description', result)}")

    def _send_outlook(self, inbox_email, to_email, subject, body):
        """Send an email via Microsoft Graph API."""
        token = self._get_ms_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        mail_data = {
            "message": {
                "subject": subject,
                "body": {"contentType": "Text", "content": body},
                "toRecipients": [{"emailAddress": {"address": to_email}}],
            },
            "saveToSentItems": True,
        }

        url = f"https://graph.microsoft.com/v1.0/users/{inbox_email}/sendMail"
        resp = requests.post(url, headers=headers, json=mail_data, timeout=30)
        resp.raise_for_status()
        print(f"  [SENT] Outlook: {inbox_email} → {to_email}")
