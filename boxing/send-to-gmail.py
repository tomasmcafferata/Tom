#!/usr/bin/env python3
"""
Sends email-draft.html to Gmail as a draft, calling the MCP HTTP API directly.
Claude never needs to hold the HTML in context.

Usage:
  python3 boxing/send-to-gmail.py boxing/boxeadores/<boxer>
"""
import glob
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

GMAIL_SERVER_ID = "36ac7041-b374-48e1-82ca-8314f34987d6"
TO = "tomascafferata19@gmail.com"


def get_oauth_token():
    # Try session ingress token file first (most reliable in subprocesses)
    token_file = os.environ.get(
        "CLAUDE_SESSION_INGRESS_TOKEN_FILE",
        "/home/claude/.claude/remote/.session_ingress_token",
    )
    p = Path(token_file)
    if p.exists():
        return p.read_text().strip()
    raise RuntimeError(f"Cannot find OAuth token (checked {token_file})")


def get_mcp_config():
    matches = glob.glob("/tmp/mcp-config-cse_*.json")
    if not matches:
        raise RuntimeError("No MCP config found in /tmp/")
    with open(matches[0]) as f:
        return json.load(f)


def create_draft(token, mcp_cfg, subject, body):
    server_cfg = mcp_cfg["mcpServers"][GMAIL_SERVER_ID]
    url = server_cfg["url"]
    extra_headers = server_cfg.get("headers", {})

    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "gmail_create_draft",
            "arguments": {
                "to": TO,
                "subject": subject,
                "body": body,
                "contentType": "text/html",
            },
        },
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json, text/event-stream")
    for k, v in extra_headers.items():
        req.add_header(k, v)

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        body_err = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code}: {body_err[:400]}")

    # Handle SSE format: lines starting with "data: "
    if raw.startswith("data:") or "\ndata:" in raw:
        lines = [l[6:] for l in raw.splitlines() if l.startswith("data:")]
        raw = "\n".join(lines)

    return json.loads(raw)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 boxing/send-to-gmail.py <boxer_dir>", file=sys.stderr)
        sys.exit(1)

    html_path = Path(sys.argv[1]) / "email-draft.html"
    if not html_path.exists():
        print(f"Error: {html_path} not found — run generate-email-draft.py first", file=sys.stderr)
        sys.exit(1)

    html = html_path.read_text(encoding="utf-8")

    # Extract boxer name from the first <h1>
    m = re.search(r"Programa (.+?)</h1>", html)
    boxer = m.group(1) if m else "Boxeador"
    subject = f"🥊 Programa {boxer} — 3 semanas | 6 sesiones"

    print(f"To:      {TO}")
    print(f"Subject: {subject}")
    print(f"Body:    {len(html):,} chars")
    print("Calling Gmail API...")

    token = get_oauth_token()
    cfg = get_mcp_config()
    result = create_draft(token, cfg, subject, html)

    # Print a clean summary
    content = result.get("result", result)
    if isinstance(content, dict):
        draft_id = content.get("draftId") or content.get("id", "")
        if draft_id:
            print(f"✓  Draft created — ID: {draft_id}")
        else:
            print("✓  Response:", json.dumps(content, indent=2)[:300])
    elif isinstance(content, list):
        # MCP result may be a list of content blocks
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                print("✓ ", block.get("text", "")[:300])
    else:
        print("✓  Result:", str(result)[:300])


if __name__ == "__main__":
    main()
