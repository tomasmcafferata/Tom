"""
Draft Creator — creates email drafts in Gmail or Outlook for human review.
"""

import base64
from email.mime.text import MIMEText

from google.oauth2.credentials import Credentials as OAuthCredentials
from google.oauth2.service_account import Credentials as SACredentials
from googleapiclient.discovery import build
import requests


# =====================================================================
# GMAIL DRAFT CREATOR
# =====================================================================

class GmailDraftCreator:
    """
    Creates drafts in Gmail using OAuth2 credentials.

    You need OAuth2 credentials (not service account) for Gmail draft creation
    because service accounts can't access regular Gmail accounts unless you
    have Google Workspace with domain-wide delegation.

    For personal Gmail: use OAuth2 token flow (see setup_guide.md).
    For Workspace: use service account + domain-wide delegation.
    """

    SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]

    def __init__(self, credentials_path: str, token_path: str = None):
        """
        credentials_path: path to OAuth2 client credentials JSON
        token_path: path to saved token JSON (auto-generated after first auth)
        """
        self.credentials_path = credentials_path
        self.token_path = token_path or credentials_path.replace(".json", "_token.json")
        self.services = {}  # Cache per inbox email

    def _get_service(self, inbox_email: str):
        """Get or create Gmail API service for an inbox."""
        if inbox_email in self.services:
            return self.services[inbox_email]

        import os
        import json
        from google_auth_oauthlib.flow import InstalledAppFlow

        token_file = f"credentials/gmail_token_{inbox_email.replace('@', '_at_')}.json"

        creds = None
        if os.path.exists(token_file):
            creds = OAuthCredentials.from_authorized_user_file(token_file, self.SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                from google.auth.transport.requests import Request
                creds.refresh(Request())
            else:
                print(f"\n  [AUTH] Opening browser to authorize Gmail for {inbox_email}")
                print(f"  [AUTH] Make sure to log in with {inbox_email}!")
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_path, self.SCOPES
                )
                creds = flow.run_local_server(port=0)

            # Save token for next time
            os.makedirs("credentials", exist_ok=True)
            with open(token_file, "w") as f:
                f.write(creds.to_json())
            print(f"  [OK] Token saved to {token_file}")

        service = build("gmail", "v1", credentials=creds)
        self.services[inbox_email] = service
        return service

    def create_draft(
        self,
        inbox_email: str,
        to_email: str,
        subject: str,
        body: str,
        thread_id: str = None,
        in_reply_to: str = None,
    ) -> str:
        """
        Create a draft in the inbox.
        Returns the draft ID.
        """
        service = self._get_service(inbox_email)

        message = MIMEText(body)
        message["to"] = to_email
        message["from"] = inbox_email
        message["subject"] = subject
        if in_reply_to:
            message["In-Reply-To"] = in_reply_to
            message["References"] = in_reply_to

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        draft_body = {"message": {"raw": raw}}
        if thread_id:
            draft_body["message"]["threadId"] = thread_id

        draft = service.users().drafts().create(
            userId="me", body=draft_body
        ).execute()

        print(f"  [DRAFT] Gmail draft created for {to_email} in {inbox_email}")
        return draft["id"]


# =====================================================================
# MICROSOFT OUTLOOK DRAFT CREATOR
# =====================================================================

class OutlookDraftCreator:
    """
    Creates drafts in Outlook/Microsoft 365 using MSAL.

    Requires an Azure AD app registration with Mail.ReadWrite permission.
    See setup_guide.md for setup instructions.
    """

    GRAPH_URL = "https://graph.microsoft.com/v1.0"

    def __init__(self, client_id: str, tenant_id: str, client_secret: str):
        self.client_id = client_id
        self.tenant_id = tenant_id
        self.client_secret = client_secret
        self._token = None

    def _get_token(self) -> str:
        """Get access token using client credentials flow."""
        import msal

        app = msal.ConfidentialClientApplication(
            self.client_id,
            authority=f"https://login.microsoftonline.com/{self.tenant_id}",
            client_credential=self.client_secret,
        )
        result = app.acquire_token_for_client(
            scopes=["https://graph.microsoft.com/.default"]
        )
        if "access_token" in result:
            return result["access_token"]
        raise Exception(f"Failed to get Microsoft token: {result.get('error_description', result)}")

    def create_draft(
        self,
        inbox_email: str,
        to_email: str,
        subject: str,
        body: str,
        thread_id: str = None,
        in_reply_to: str = None,
    ) -> str:
        """
        Create a draft in the Outlook inbox.
        Returns the draft message ID.
        """
        token = self._get_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        draft_data = {
            "subject": subject,
            "body": {"contentType": "Text", "content": body},
            "toRecipients": [{"emailAddress": {"address": to_email}}],
        }

        # Create draft in the user's mailbox
        url = f"{self.GRAPH_URL}/users/{inbox_email}/messages"
        resp = requests.post(url, headers=headers, json=draft_data, timeout=30)
        resp.raise_for_status()
        msg = resp.json()

        print(f"  [DRAFT] Outlook draft created for {to_email} in {inbox_email}")
        return msg["id"]
