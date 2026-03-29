# GTM Outbound System

This repository is a multi-client outbound GTM engine. It contains the full skill stack, scripts, and client work.

## How to use

Run the full GTM pipeline for a new client:
```
/market gtm <url> <ClientName>
```

Or run steps individually:
```
/market strategy <url>     → clients/<name>/STRATEGY.md
/market icp                → clients/<name>/ICP.md
/market tam                → clients/<name>/TAM.md
/market competitors <url>  → clients/<name>/COMPETITOR-REPORT.md
/market positioning        → clients/<name>/POSITIONING.md
/market messaging          → clients/<name>/MESSAGING.md
/market abm                → clients/<name>/ABM.md
/market emails             → clients/<name>/EMAIL-SEQUENCES.md
```

## Structure

```
.claude/commands/   ← all GTM skills (loaded automatically by Claude Code)
.claude/agents/     ← parallel subagents for /market audit
clients/            ← one folder per client
  NDC/              ← enedece.com.ar (active)
scripts/            ← Python execution layer
GTM-WORKFLOW.md     ← full system reference map
config.yaml         ← API keys and configuration (use .env for secrets)
```

## Active clients

- **NDC** (`clients/NDC/`) — enedece.com.ar — outbound GTM, Argentine market
