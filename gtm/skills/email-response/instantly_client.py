"""
Instantly API client — fetches campaign replies from your Instantly account.
"""

import time
import requests


class InstantlyClient:
    BASE_URL = "https://api.instantly.ai/api/v1"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def _get(self, endpoint: str, params: dict = None) -> dict:
        params = params or {}
        params["api_key"] = self.api_key
        resp = requests.get(f"{self.BASE_URL}{endpoint}", params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()

    def get_campaigns(self) -> list:
        """Get all campaigns."""
        result = self._get("/campaign/list", {"limit": 100, "skip": 0})
        return result if isinstance(result, list) else result.get("data", [])

    def get_campaign_replies(self, campaign_id: str) -> list:
        """Get replies for a specific campaign."""
        result = self._get(f"/unibox/emails", {
            "campaign_id": campaign_id,
            "email_type": "received",
            "limit": 50,
        })
        return result if isinstance(result, list) else result.get("data", [])

    def get_all_replies(self, since_timestamp: float = None) -> list:
        """
        Get all replies across all campaigns.
        Returns list of dicts with: lead_email, subject, body, timestamp,
        campaign_id, from_address (the inbox that received it).
        """
        campaigns = self.get_campaigns()
        all_replies = []

        for campaign in campaigns:
            cid = campaign.get("id", "")
            try:
                replies = self.get_campaign_replies(cid)
            except Exception as e:
                print(f"  [WARN] Failed to fetch replies for campaign {cid}: {e}")
                continue

            for reply in replies:
                ts = reply.get("timestamp", 0)
                # Skip old replies if a since_timestamp is provided
                if since_timestamp and ts <= since_timestamp:
                    continue

                all_replies.append({
                    "lead_email": reply.get("from_address_email", reply.get("from", "")),
                    "lead_name": reply.get("from_address_name", ""),
                    "subject": reply.get("subject", ""),
                    "body": reply.get("body", reply.get("text", "")),
                    "timestamp": ts,
                    "campaign_id": cid,
                    "campaign_name": campaign.get("name", ""),
                    "to_inbox": reply.get("to_address_email", reply.get("to", "")),
                    "message_id": reply.get("id", reply.get("message_id", "")),
                    "thread_id": reply.get("thread_id", ""),
                })

            # Be nice to the API
            time.sleep(0.5)

        return sorted(all_replies, key=lambda r: r.get("timestamp", 0))

    def get_lead_thread(self, campaign_id: str, lead_email: str) -> list:
        """Get the full email thread for a lead in a campaign."""
        try:
            result = self._get(f"/unibox/emails", {
                "campaign_id": campaign_id,
                "email": lead_email,
                "limit": 20,
            })
            emails = result if isinstance(result, list) else result.get("data", [])
            return sorted(emails, key=lambda e: e.get("timestamp", 0))
        except Exception as e:
            print(f"  [WARN] Failed to fetch thread for {lead_email}: {e}")
            return []
