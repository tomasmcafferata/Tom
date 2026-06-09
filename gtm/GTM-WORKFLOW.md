# GTM Outbound System — Workflow Map

## Overview

Two phases. **(1) Strategy build** — an 8-step pipeline that takes a client URL and produces a complete outbound GTM stack: strategy foundation, ICP, market sizing, competitive positioning, messaging architecture, ABM playbook, and cold email sequences. **(2) Execution** — the operational layer that runs real campaigns off that stack: a lead list → enriched, scored, personalized, sent, and reply-tracked. See **Execution Pipeline** below.

---

## Pipeline

```
STEP    COMMAND                    READS                          PRODUCES
────────────────────────────────────────────────────────────────────────────────────
  0     /market research <url>     [website + online sources]     CUSTOMER-RESEARCH.md  ← optional but recommended
  1     /market strategy <url>     [website]                      STRATEGY.md
  2     /market icp                STRATEGY.md                    ICP.md
  3     /market tam                ICP.md + STRATEGY.md           TAM.md
  4     /market competitors <url>  [website]                      COMPETITOR-REPORT.md
  5     /market positioning        ICP + COMPETITORS + STRATEGY   POSITIONING.md
  6     /market messaging          POSITIONING + ICP + STRATEGY   MESSAGING.md
  7     /market abm                ICP + TAM + MESSAGING          ABM.md
  8     /market emails             MESSAGING + ABM                EMAIL-SEQUENCES.md    ← primary
─────   ──────────────────────────────────────────────────────────────────────────────
        /market enablement         POSITIONING + MESSAGING + ICP  SALES-ENABLEMENT.md   ← after meetings booked
        /market revops             ICP + ABM                      REVOPS.md             ← CRM + pipeline setup
        /market report             all files                      MARKETING-REPORT.md
        /market proposal           all files                      CLIENT-PROPOSAL.md
```

Run everything at once:
```
/market gtm <url> <ClientName>
```

---

## Data Flow

```
STRATEGY.md ──────────────────────────────────────────────────────┐
                │                                                  │
                ▼                                                  │
            ICP.md ───────────────────────────────────────────┐   │
                │                                             │   │
                ▼                                             │   │
            TAM.md ─────────────────────────────────┐        │   │
                                                     │        │   │
            COMPETITOR-REPORT.md ──┐                 │        │   │
                                   ▼                 │        │   │
                          POSITIONING.md ────────────┤        │   │
                                   │                 │        │   │
                                   ▼                 │        │   │
                            MESSAGING.md ────────────┴────────┘   │
                           (+ content scan)    │                   │
                                               ▼                   │
                                           ABM.md ─────────────────┘
                                               │
                                    EMAIL-SEQUENCES.md  ← primary deliverable
```

---

## Skills

All skills live in `skills/`. The orchestrator loads them on demand.

```
skills/
├── market-strategy/SKILL.md      Step 1 — business model, brand voice, growth vectors, triggers
├── market-icp/SKILL.md           Step 2 — who to target, scoring rubric, list building
├── market-tam/SKILL.md           Step 3 — TAM/SAM/SOM, segment sizing, pipeline model
├── market-competitors/SKILL.md   Step 4 — competitive intelligence, positioning gaps
├── market-positioning/SKILL.md   Step 5 — differentiation, competitive wedges
├── market-messaging/SKILL.md     Step 6 — hooks per trigger, persona angles, follow-up logic
├── market-abm/SKILL.md           Step 7 — account tiers, research card, engagement playbooks
├── market-emails/SKILL.md        Step 8 — cold email sequences, subject lines, LinkedIn track
├── market-competitive/SKILL.md   Support — deep competitive research (used within competitors step)
├── market-report/SKILL.md        Deliverable — compiled marketing report
└── market-proposal/SKILL.md      Deliverable — client proposal
```

---

## Client Folder Structure

```
clients/
└── <ClientName>/
    ├── STRATEGY.md
    ├── ICP.md
    ├── TAM.md
    ├── COMPETITOR-REPORT.md
    ├── POSITIONING.md
    ├── MESSAGING.md
    ├── ABM.md
    └── EMAIL-SEQUENCES.md     ← primary deliverable
```

---

## Deliverables → Execution

```
ICP.md              →  Apollo / LinkedIn Sales Navigator list building
TAM.md              →  Account prioritization, quota planning
ABM.md              →  CRM account tiers, research cards, engagement playbooks
EMAIL-SEQUENCES.md  →  Instantly / Smartlead / Lemlist sequences  ← PRIMARY
MESSAGING.md        →  LinkedIn DMs, call scripts, LinkedIn connection notes
```

---

## Execution Pipeline (leads → campaigns → replies)

The strategy stack is the *blueprint*. This is the *operational layer* that runs campaigns
off it. Pattern throughout: **a generic engine + a per-client/ICP config**, so it replicates
across clients and across ICPs within a client.

```
STAGE                  WHERE                          CONFIG / ARTIFACT
──────────────────────────────────────────────────────────────────────────────────────────
import leads           scripts/import_leads.py        scripts/formats/*.json  → Lead Sheet
pre-screen persona     scripts/prescreen.py           clients/<c>/prescreen-rules.yaml  (free: title+geo)
enrich · research      Clay (native Sheet sync)       leads/research-prompt-base.md
                                                      + clients/<c>/research-brief-<icp>.yaml
gate                   Clay icp_fit (strong/medium)   only survivors continue
enrich · email         Clay waterfall (credits)       survivors only — costliest, last
campaign ideation      /market campaigns (skill)      ICP + POSITIONING → idea menu (Google Doc)
personalize copy       Clay                           leads/personalization-prompt-base.md + campaign brief
build send list        scripts/build_instantly_csv.py column-agnostic → Instantly CSV
send                   Instantly (manual upload)      approval gate = you
reply loop             skills/email-response          Reply CRM + Slack one-click approval
reconcile replies      scripts/sync_replies.py        → outbound Leads status / do_not_contact
verify enrichment      scripts/enrich_status.py       read-only coverage report
recipe + contract      leads/ENRICHMENT.md            Clay setup + write-back columns
```

**Division of labor**
- **Clay** = facts *and* words at volume (research, triggers, email-finding, per-lead copy). Prompts/briefs are versioned in the repo and pasted into Clay.
- **Repo scripts** = deterministic logic (pre-screen, CSV build, reply sync) + dumb mappers. No copy generation in the repo.
- **Skills** = the creative/human steps (campaign ideation; reply handling).

**Two CRMs, bridged.** Outbound **Lead CRM** (one Google Sheet, the lead lifecycle) + inbound **Reply CRM** (the email-response sheet). `sync_replies.py` copies reply outcomes onto the outbound leads so future sends skip repliers.

**Scoring sandwich (cost order).** Free pre-screen → cheap research on all → gate on `icp_fit` → expensive email on survivors only.

---

## Adding a New Client

```bash
/market gtm https://newclient.com ClientName
```

Creates `clients/ClientName/`, runs all 8 steps, saves every deliverable.
