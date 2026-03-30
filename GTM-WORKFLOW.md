# GTM Outbound System — Workflow Map

## Overview

8-step pipeline that takes a client URL and produces a complete outbound GTM stack: strategy foundation, ICP, market sizing, competitive positioning, messaging architecture, ABM playbook, and cold email sequences ready to load in Instantly or Smartlead.

---

## Pipeline

```
STEP    COMMAND                    READS                          PRODUCES
────────────────────────────────────────────────────────────────────────────────────
  1     /market strategy <url>     [website]                      STRATEGY.md
  2     /market icp                STRATEGY.md                    ICP.md
  3     /market tam                ICP.md + STRATEGY.md           TAM.md
  4     /market competitors <url>  [website]                      COMPETITOR-REPORT.md
  5     /market positioning        ICP + COMPETITORS + STRATEGY   POSITIONING.md
  6     /market messaging          POSITIONING + ICP + STRATEGY   MESSAGING.md
  7     /market abm                ICP + TAM + MESSAGING          ABM.md
  8     /market emails             MESSAGING + ABM                EMAIL-SEQUENCES.md ← primary
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

## Adding a New Client

```bash
/market gtm https://newclient.com ClientName
```

Creates `clients/ClientName/`, runs all 8 steps, saves every deliverable.
