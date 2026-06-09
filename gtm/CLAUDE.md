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
.claude/commands/market.md  ← single orchestrator slash command
skills/                     ← all GTM sub-skills (loaded by orchestrator)
  market-strategy/SKILL.md
  market-icp/SKILL.md
  market-tam/SKILL.md
  market-competitors/SKILL.md
  market-competitive/SKILL.md
  market-positioning/SKILL.md
  market-messaging/SKILL.md
  market-abm/SKILL.md
  market-emails/SKILL.md
  market-report/SKILL.md
  market-proposal/SKILL.md
clients/                    ← one folder per client
  NDC/                      ← enedece.com.ar (active)
scripts/                    ← Python execution layer
GTM-WORKFLOW.md             ← full system reference map
config.yaml                 ← API keys and configuration (use .env for secrets)
```

## Execution layer (leads → campaigns → replies)

Beyond the strategy stack above, the repo runs campaigns off a lead list. Generic engine +
per-client config throughout. Full map + cost order: `GTM-WORKFLOW.md`.

```
leads/
  config.yaml                     Lead Sheet id + capacity / cooldown model
  research-prompt-base.md         generic Clay research prompt (paste into Clay)
  personalization-prompt-base.md  generic Clay copy prompt (paste into Clay)
  ENRICHMENT.md                   Clay recipe + write-back contract
scripts/
  import_leads.py                 load a list (formats/*.json) → Lead Sheet
  prescreen.py                    free persona triage (title+geo) → tiers  (clients/<c>/prescreen-rules.yaml)
  enrich_status.py                read-only enrichment coverage report
  build_instantly_csv.py          qualified cohort → Instantly import CSV (column-agnostic)
  sync_replies.py                 reply outcomes → outbound CRM (skip repliers)
skills/
  campaign-ideation/SKILL.md      /market campaigns → breadth idea menu (Google Doc)
  email-response/                 inbound replies → Slack one-click approval
```

Per-client config lives in `clients/<c>/`: `prescreen-rules.yaml`, `research-brief-<icp>.yaml`,
and the ICP/POSITIONING docs (offers folded into POSITIONING.md).

**Division of labor:** Clay generates facts + per-lead copy (prompts versioned here, pasted in);
scripts do deterministic logic (no copy gen); skills do the creative/human steps. Two CRMs
(outbound Lead + inbound Reply) bridged by `sync_replies.py`.

---

## Active clients

- **NDC** (`clients/NDC/`) — enedece.com.ar — outbound GTM, Argentine market. Active ICP
  segments: **events/stands** (marketing buyer) and **ploteo/fleet** (ops/GM buyer — see
  ICP.md "Segment B").
