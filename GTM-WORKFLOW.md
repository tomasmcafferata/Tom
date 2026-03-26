# GTM Outbound System — Full Workflow Map

## System Overview

This is a multi-client outbound GTM engine built on 20 Claude Code skills + 5 parallel agents. It takes a client URL or description as input and produces a complete outbound system: ICP, market sizing, positioning, messaging, email sequences, ad campaigns, ABM playbook, and landing page specs.

---

## Architecture

```
                        ┌─────────────────────────────────┐
                        │     /market <command> <url>      │
                        │       Main Orchestrator          │
                        └───────────────┬─────────────────┘
                                        │
               ┌────────────────────────┼────────────────────────┐
               │                        │                        │
    ┌──────────▼──────────┐  ┌──────────▼──────────┐  ┌─────────▼──────────┐
    │   ANALYSIS TRACK    │  │   OUTBOUND GTM TRACK │  │   CONTENT TRACK    │
    │   (Website Audit)   │  │   (Build & Execute)  │  │   (Create Assets)  │
    └──────────┬──────────┘  └──────────┬──────────┘  └─────────┬──────────┘
               │                        │                        │
    ┌──────────┘                        │               ┌────────┘
    │                                   │               │
    ▼                                   ▼               ▼
  audit                              icp             emails
  quick                              tam             social
  seo                                competitors     ads
  funnel                             positioning     copy
  landing                            messaging       launch
  brand                              abm
  competitors
```

---

## Track 1: Outbound GTM Stack (Sequential Pipeline)

This is the core revenue engine. Skills run in order — each reads the output of the previous.

```
┌──────────┐     ┌──────────┐     ┌──────────────┐     ┌──────────────┐
│  /market │     │  /market │     │   /market    │     │   /market    │
│   icp    │────▶│   tam    │  ┌─▶│  positioning │────▶│  messaging   │
│          │     │          │  │  │              │     │              │
└────┬─────┘     └──────────┘  │  └──────────────┘     └──────┬───────┘
     │                         │                              │
     │  ┌──────────────┐       │                    ┌─────────┼──────────┐
     │  │   /market    │       │                    │         │          │
     └─▶│ competitors  │───────┘               ┌────▼───┐ ┌───▼──┐ ┌────▼────┐
        │              │                       │/market │ │/market│ │ /market │
        └──────────────┘                       │  abm   │ │emails │ │  ads    │
                                               └────────┘ └──────┘ └─────────┘
                                                    │
                                               ┌────▼────┐
                                               │ /market │
                                               │ landing │
                                               └─────────┘
```

### Step-by-Step with Deliverables

```
STEP  SKILL              READS                           PRODUCES              PURPOSE
─────────────────────────────────────────────────────────────────────────────────────────
 1    /market icp         [website/description]            ICP.md               WHO to target
 2    /market tam         ICP.md                           TAM.md               HOW MANY targets exist
 3    /market competitors [website]                        COMPETITOR-REPORT.md  WHO you're up against
 4    /market positioning ICP.md + COMPETITOR-REPORT.md    POSITIONING.md        WHERE you stand
 5    /market messaging   POSITIONING.md + ICP.md          MESSAGING.md         WHAT to say
 6    /market abm         ICP + TAM + MESSAGING + POS.    ABM.md               HOW to engage accounts
 7    /market emails      MESSAGING.md + ABM.md            EMAIL-SEQUENCES.md   EXACT sequences to send
 8    /market ads         MESSAGING.md                     AD-CAMPAIGNS.md      PAID channel copy
 9    /market landing     MESSAGING.md                     LANDING-CRO.md       WHERE traffic converts
```

### Data Flow Diagram

```
ICP.md ──────┬───────────────────────────────────────────────────────────┐
             │                                                           │
             ▼                                                           │
         TAM.md ──────────────────────────────────────┐                  │
             │                                        │                  │
             │    COMPETITOR-REPORT.md ────┐           │                  │
             │                            ▼           │                  │
             │                     POSITIONING.md ────┤                  │
             │                            │           │                  │
             │                            ▼           │                  │
             │                      MESSAGING.md ─────┤──────┬───────────┤
             │                            │           │      │           │
             │                            │           ▼      ▼           ▼
             │                            │        ABM.md  ADS.md   LANDING.md
             │                            │           │
             │                            ▼           │
             │                    EMAIL-SEQUENCES.md ◀┘
             │
             └──────────────────────────────────▶ [All downstream skills]
```

---

## Track 2: Website Analysis Stack (Parallel)

These skills analyze an existing website. Can run independently or feed into the GTM stack.

```
                           /market audit <url>
                                  │
                    Launches 5 PARALLEL subagents:
                                  │
          ┌───────────┬───────────┼───────────┬──────────────┐
          ▼           ▼           ▼           ▼              ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
    │ content  │ │conversion│ │competitv.│ │technical │ │ strategy │
    │  agent   │ │  agent   │ │  agent   │ │  agent   │ │  agent   │
    └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘
         │            │            │            │            │
         └────────────┴────────────┴────────────┴────────────┘
                                   │
                                   ▼
                         MARKETING-AUDIT.md
                         (Composite Score 0-100)
```

### Individual Analysis Skills

```
SKILL              PRODUCES              CAN RUN STANDALONE?   FEEDS INTO
──────────────────────────────────────────────────────────────────────────
/market audit      MARKETING-AUDIT.md    Yes                   report, proposal
/market quick      [terminal output]     Yes                   —
/market seo        SEO-AUDIT.md          Yes                   report
/market funnel     FUNNEL-ANALYSIS.md    Yes                   report, emails
/market landing    LANDING-CRO.md        Yes                   report
/market brand      BRAND-VOICE.md        Yes                   copy, messaging
/market competitors COMPETITOR-REPORT.md Yes                   positioning, abm
```

---

## Track 3: Content Generation Stack

These produce client-ready content. Best results when fed by the GTM stack outputs.

```
SKILL              PRODUCES              BEST INPUT                STANDALONE OK?
──────────────────────────────────────────────────────────────────────────────────
/market emails     EMAIL-SEQUENCES.md    MESSAGING.md + ABM.md     Yes (basic)
/market social     SOCIAL-CALENDAR.md    [topic/url]               Yes
/market ads        AD-CAMPAIGNS.md       MESSAGING.md              Yes (basic)
/market copy       COPY-SUGGESTIONS.md   [url] + BRAND-VOICE.md    Yes
/market launch     LAUNCH-PLAYBOOK.md    [product description]     Yes
```

---

## Track 4: Client Reporting & Proposals

Aggregate analysis into client-ready deliverables.

```
SKILL              PRODUCES              READS
─────────────────────────────────────────────────────────────
/market report     MARKETING-REPORT.md   All audit files
/market report-pdf MARKETING-REPORT.pdf  All audit files
/market proposal   CLIENT-PROPOSAL.md    All available files
```

---

## Multi-Client Folder Structure

```
Tom/
├── clients/
│   ├── NDC/                          ← enedece.com.ar
│   │   ├── ICP.md
│   │   ├── TAM.md
│   │   ├── COMPETITOR-REPORT.md
│   │   ├── POSITIONING.md
│   │   ├── MESSAGING.md
│   │   ├── ABM.md
│   │   ├── EMAIL-SEQUENCES.md
│   │   ├── AD-CAMPAIGNS.md
│   │   ├── LANDING-CRO.md
│   │   ├── MARKETING-AUDIT.md        ← optional (analysis track)
│   │   ├── SEO-AUDIT.md              ← optional
│   │   ├── BRAND-VOICE.md            ← optional
│   │   └── MARKETING-REPORT.md       ← optional (compiled report)
│   │
│   ├── [CLIENT-2]/                   ← next client
│   │   ├── ICP.md
│   │   ├── TAM.md
│   │   └── ...
│   │
│   └── [CLIENT-N]/
│       └── ...
│
└── GTM-WORKFLOW.md                   ← this file
```

---

## Full GTM Run: Single Command Reference

To run the complete outbound GTM stack for a new client:

```
Step 1:  /market icp <url>              → saves to clients/<name>/ICP.md
Step 2:  /market tam <url>              → saves to clients/<name>/TAM.md
Step 3:  /market competitors <url>      → saves to clients/<name>/COMPETITOR-REPORT.md
Step 4:  /market positioning <url>      → saves to clients/<name>/POSITIONING.md
Step 5:  /market messaging <url>        → saves to clients/<name>/MESSAGING.md
Step 6:  /market abm <url>             → saves to clients/<name>/ABM.md
Step 7:  /market emails <url>           → saves to clients/<name>/EMAIL-SEQUENCES.md
Step 8:  /market ads <url>             → saves to clients/<name>/AD-CAMPAIGNS.md
Step 9:  /market landing <url>          → saves to clients/<name>/LANDING-CRO.md
```

Optional analysis add-ons (run before or after):
```
         /market audit <url>            → clients/<name>/MARKETING-AUDIT.md
         /market seo <url>              → clients/<name>/SEO-AUDIT.md
         /market brand <url>            → clients/<name>/BRAND-VOICE.md
         /market report <url>           → clients/<name>/MARKETING-REPORT.md
         /market proposal <client>      → clients/<name>/CLIENT-PROPOSAL.md
```

---

## Skill Inventory: 20 Skills + 5 Agents

### Skills Created In-House (GTM-specific)
| Skill | Created | Purpose |
|-------|---------|---------|
| market-icp | This session | ICP builder for outbound |
| market-tam | This session | TAM/SAM/SOM sizing |
| market-positioning | This session | Competitive positioning |
| market-messaging | This session | Full messaging architecture |
| market-abm | This session | Account-Based Marketing |

### Skills from Marketing Toolkit (GitHub)
| Skill | Source | Purpose |
|-------|--------|---------|
| market (orchestrator) | Repo | Routes all /market commands |
| market-audit | Repo | Full parallel website audit |
| market-brand | Repo | Brand voice analysis |
| market-competitors | Repo | Competitive intelligence |
| market-copy | Repo | Copywriting analysis |
| market-emails | Repo | Email sequence generation |
| market-funnel | Repo | Sales funnel analysis |
| market-landing | Repo | Landing page CRO |
| market-launch | Repo | Launch playbook |
| market-proposal | Repo | Client proposal generator |
| market-report | Repo | Markdown report |
| market-report-pdf | Repo | PDF report |
| market-seo | Repo | SEO audit |
| market-social | Repo | Social media calendar |
| market-ads | Repo | Ad creative generation |

### Parallel Subagents (used by /market audit)
| Agent | Purpose |
|-------|---------|
| market-content | Content quality analysis |
| market-conversion | CRO analysis |
| market-competitive | Competitive positioning |
| market-technical | Technical SEO |
| market-strategy | Growth strategy |

---

## Connection to Outbound Execution

```
    GTM STACK OUTPUT                    EXECUTION LAYER
    ────────────────                    ───────────────

    ICP.md                    ──▶      Apollo / Sales Navigator list building
    TAM.md                    ──▶      Account prioritization & quota planning
    COMPETITOR-REPORT.md      ──▶      Battle cards for sales calls
    POSITIONING.md            ──▶      Website copy, pitch deck, sales narrative
    MESSAGING.md              ──▶      Cold email copy, LinkedIn DMs, call scripts
    ABM.md                    ──▶      CRM account tiers, engagement tracking
    EMAIL-SEQUENCES.md        ──▶      Instantly / Smartlead / Lemlist sequences
    AD-CAMPAIGNS.md           ──▶      Google Ads, Meta Ads, LinkedIn Ads
    LANDING-CRO.md            ──▶      Webflow / Framer / custom landing page build
```

### Outbound Tech Stack Integration Points

```
DELIVERABLE              →  TOOL                    →  ACTION
─────────────────────────────────────────────────────────────────
ICP.md filter specs      →  Apollo.io               →  Build prospect list
ICP.md filter specs      →  LinkedIn Sales Nav      →  Build account list
TAM.md tier definitions  →  CRM (HubSpot/Pipedrive) →  Create account tiers
ABM.md research cards    →  CRM                     →  Populate account fields
EMAIL-SEQUENCES.md       →  Instantly.ai            →  Load sequences
EMAIL-SEQUENCES.md       →  Smartlead               →  Load sequences
MESSAGING.md LinkedIn    →  LinkedIn (manual)       →  Send connection requests
AD-CAMPAIGNS.md          →  Google/Meta/LinkedIn    →  Launch ad campaigns
LANDING-CRO.md           →  Webflow/Framer          →  Build landing page
```

---

## Running for Multiple Clients

Each client gets their own folder under `clients/`. The workflow is identical per client — only the input URL changes.

**To onboard a new client:**
1. Create folder: `clients/<ClientName>/`
2. Run the 9-step GTM stack (all outputs save to that folder)
3. Optional: run analysis track for deeper audit
4. Optional: compile into report/proposal

**Cross-client insights:**
- Competitor reports may overlap (same industry)
- Messaging patterns that work for one client inform others
- ICP scoring rubrics can be templated across similar verticals
