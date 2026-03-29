"""
Slack Handler — sends reply notifications to a Slack channel with
Approve / Edit / Skip buttons. Listens for button clicks via Socket Mode
(no public URL needed). On approval, sends the email from the correct inbox.
"""

import json
import threading

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


class SlackHandler:
    def __init__(self, bot_token: str, app_token: str, channel_id: str, email_sender):
        """
        bot_token: Slack Bot User OAuth Token (xoxb-...)
        app_token: Slack App-Level Token (xapp-...) for Socket Mode
        channel_id: Slack channel ID to post notifications to
        email_sender: EmailSender instance for sending approved replies
        """
        self.channel_id = channel_id
        self.email_sender = email_sender
        self.pending = {}  # message_ts -> reply data

        self.app = App(token=bot_token)
        self.socket_handler = SocketModeHandler(self.app, app_token)

        # Register button handlers
        self.app.action("approve_reply")(self._handle_approve)
        self.app.action("edit_reply")(self._handle_edit)
        self.app.action("skip_reply")(self._handle_skip)
        self.app.view("edit_modal_submit")(self._handle_edit_submit)

    def start(self):
        """Start listening for Slack interactions in a background thread."""
        thread = threading.Thread(target=self.socket_handler.start, daemon=True)
        thread.start()
        print("  [OK] Slack bot connected (Socket Mode)")

    def notify_new_reply(self, reply_data: dict):
        """
        Post a notification to the Slack channel with the reply + proposed response.

        reply_data keys:
            lead_email, lead_name, company, client_name, campaign,
            inbox_email, classification, reply_body, proposed_response,
            subject, thread_id, message_id, provider
        """
        lead = reply_data.get("lead_email", "unknown")
        name = reply_data.get("lead_name", "")
        company = reply_data.get("company", "")
        client = reply_data.get("client_name", "")
        inbox = reply_data.get("inbox_email", "")
        classification = reply_data.get("classification", "")
        reply_body = reply_data.get("reply_body", "")[:800]
        proposed = reply_data.get("proposed_response", "")

        # Header line
        if company:
            header = f"*{name or lead}* ({company}) → {inbox}"
        else:
            header = f"*{name or lead}* → {inbox}"

        # Classification emoji
        emoji_map = {
            "interested": ":fire:",
            "question": ":question:",
            "meeting": ":calendar:",
            "not_interested": ":no_entry_sign:",
            "ooo": ":palm_tree:",
            "bounce": ":warning:",
        }
        emoji = emoji_map.get(classification, ":email:")

        blocks = [
            {
                "type": "header",
                "text": {"type": "plain_text", "text": f"{client} — New Reply"}
            },
            {
                "type": "context",
                "elements": [
                    {"type": "mrkdwn", "text": f"{emoji} *{classification.upper()}* | Campaign: {reply_data.get('campaign', 'N/A')}"}
                ]
            },
            {"type": "divider"},
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"{header}\n\n*Their message:*\n>{reply_body}"}
            },
            {"type": "divider"},
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*Proposed response:*\n```{proposed}```"}
            },
        ]

        # Only show action buttons if there's a proposed response
        if proposed:
            blocks.append({
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Approve & Send"},
                        "style": "primary",
                        "action_id": "approve_reply",
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Edit & Send"},
                        "action_id": "edit_reply",
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Skip"},
                        "style": "danger",
                        "action_id": "skip_reply",
                    },
                ]
            })

        result = self.app.client.chat_postMessage(
            channel=self.channel_id,
            blocks=blocks,
            text=f"New reply from {lead} ({client})",  # fallback for notifications
        )

        # Store pending reply data keyed by message timestamp
        ts = result["ts"]
        self.pending[ts] = reply_data
        print(f"  [SLACK] Notification posted for {lead}")
        return ts

    # ------------------------------------------------------------------
    # Button handlers
    # ------------------------------------------------------------------

    def _handle_approve(self, ack, body):
        """User clicked Approve & Send — send the email as-is."""
        ack()
        ts = body["message"]["ts"]
        reply_data = self.pending.get(ts)

        if not reply_data:
            self._update_message(body, ":warning: Reply data expired. Please handle manually.")
            return

        try:
            self.email_sender.send_email(
                inbox_email=reply_data["inbox_email"],
                to_email=reply_data["lead_email"],
                subject=reply_data.get("subject", ""),
                body=reply_data["proposed_response"],
                provider=reply_data.get("provider", "google"),
                thread_id=reply_data.get("thread_id"),
                in_reply_to=reply_data.get("message_id"),
            )
            self._update_message(body, f":white_check_mark: *Sent* to {reply_data['lead_email']}")
            del self.pending[ts]
        except Exception as e:
            self._update_message(body, f":x: *Failed to send:* {str(e)[:200]}")

    def _handle_edit(self, ack, body):
        """User clicked Edit — open a modal with the proposed text."""
        ack()
        ts = body["message"]["ts"]
        reply_data = self.pending.get(ts)

        if not reply_data:
            return

        self.app.client.views_open(
            trigger_id=body["trigger_id"],
            view={
                "type": "modal",
                "callback_id": "edit_modal_submit",
                "private_metadata": ts,  # link back to the message
                "title": {"type": "plain_text", "text": "Edit Response"},
                "submit": {"type": "plain_text", "text": "Send"},
                "close": {"type": "plain_text", "text": "Cancel"},
                "blocks": [
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": f"*To:* {reply_data['lead_email']}\n*From:* {reply_data['inbox_email']}"}
                    },
                    {
                        "type": "input",
                        "block_id": "response_block",
                        "label": {"type": "plain_text", "text": "Response"},
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "response_text",
                            "multiline": True,
                            "initial_value": reply_data.get("proposed_response", ""),
                        }
                    }
                ]
            }
        )

    def _handle_edit_submit(self, ack, view):
        """User submitted the edited response from the modal."""
        ack()
        ts = view["private_metadata"]
        reply_data = self.pending.get(ts)

        if not reply_data:
            return

        edited_text = view["state"]["values"]["response_block"]["response_text"]["value"]

        try:
            self.email_sender.send_email(
                inbox_email=reply_data["inbox_email"],
                to_email=reply_data["lead_email"],
                subject=reply_data.get("subject", ""),
                body=edited_text,
                provider=reply_data.get("provider", "google"),
                thread_id=reply_data.get("thread_id"),
                in_reply_to=reply_data.get("message_id"),
            )
            # Update the original Slack message
            self.app.client.chat_update(
                channel=self.channel_id,
                ts=ts,
                blocks=[{
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f":white_check_mark: *Sent (edited)* to {reply_data['lead_email']}"}
                }],
                text=f"Sent to {reply_data['lead_email']}",
            )
            del self.pending[ts]
        except Exception as e:
            self.app.client.chat_postMessage(
                channel=self.channel_id,
                text=f":x: Failed to send edited reply to {reply_data['lead_email']}: {str(e)[:200]}",
            )

    def _handle_skip(self, ack, body):
        """User clicked Skip — mark as skipped."""
        ack()
        ts = body["message"]["ts"]
        reply_data = self.pending.get(ts)
        lead = reply_data["lead_email"] if reply_data else "unknown"
        self._update_message(body, f":fast_forward: *Skipped* — {lead}")
        if ts in self.pending:
            del self.pending[ts]

    def _update_message(self, body, new_text: str):
        """Replace the original message with a status update."""
        self.app.client.chat_update(
            channel=body["channel"]["id"],
            ts=body["message"]["ts"],
            blocks=[{"type": "section", "text": {"type": "mrkdwn", "text": new_text}}],
            text=new_text,
        )
