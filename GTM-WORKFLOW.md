# GTM Outbound System — Full Workflow Map

## System Overview

This is a multi-client outbound GTM engine built on 21 Claude Code skills + 5 parallel agents. It takes a client URL or description as input and produces a complete outbound system: strategy foundation, ICP, market sizing, positioning, messaging, email sequences, ABM playbook, and optional ad/landing assets.

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
  audit                           strategy        emails
  quick                              icp             social
  seo                                tam             ads
  funnel                         competitors         copy
  landing                         positioning       launch
  brand                            messaging
  competitors                        abm
```

---

## Track 1: Outbound GTM Stack (Sequential Pipeline)

This is the core revenue engine. Skills run in order — each reads the output of the previous.
Run everything at once with: `/market gtm <url> <client-name>`

```
STRATEGIC LAYER
───────────────
┌──────────────┐
│ /market      │  → STRATEGY.md  (business model, brand voice, growth vectors, buying triggers)
│  strategy    │
└──────┬───────┘
       │
┌──────▼───────┐     ┌──────────┐     ┌──────────────┐
│ /market icp  │────▶│  /market │     │   /market    │
│              │     │   tam    │  ┌─▶│  competitors │
└──────────────┘     └──────────┘  │  └──────┬───────┘
                                   │         │
POSITIONING + MESSAGING LAYER      │         │
──────────────────────────────     │         ▼
                          ┌────────┴──────────────────┐
                          │     /market positioning    │  → POSITIONING.md
                          └────────────────┬──────────┘
                                           │
                          ┌────────────────▼──────────┐
                          │     /market messaging      │  → MESSAGING.md
                          │  [+ internal content scan] │  (iterates existing copy)
                          └────────────────┬──────────┘

EXECUTION LAYER
───────────────
                          ┌────────────────▼──────────┐
                          │       /market abm          │  → ABM.md
                          └────────────────┬──────────┘
                                           │
                          ┌────────────────▼──────────┐
                          │      /market emails        │  → EMAIL-SEQUENCES.md  ← PRIMARY
                          └────────────┬──────────────┘
                                       │
               COMPLEMENTARY (optional, feed from emails)
               ────────────────────────────────────────
                        ┌──────┴──────┐
               ┌────────▼───┐  ┌──────▼──────┐
               │/market ads │  │/market      │
               │            │  │ landing     │
               └────────────┘  └─────────────┘
```

### Step-by-Step with Deliverables

```
     SKILL                READS                               PRODUCES               PURPOSE
──────────────────────────────────────────────────────────────────────────────────────────────────
STRATEGIC LAYER
 1   /market strategy     [website/description]               STRATEGY.md            WHY — business model, brand, growth vectors
 2   /market icp          STRATEGY.md                         ICP.md                 WHO to target
 3   /market tam          ICP.md                              TAM.md                 HOW MANY targets exist
 4   /market competitors  [website]                           COMPETITOR-REPORT.md   WHO you're up against

POSITIONING + MESSAGING LAYER
 5   /market positioning  ICP.md + COMPETITORS + STRATEGY     POSITIONING.md         WHERE you stand vs. market
 6   /market messaging    POSITIONING + ICP + STRATEGY        MESSAGING.md           WHAT to say (iterates existing copy)
                          + [internal content analysis]

EXECUTION LAYER
 7   /market abm          ICP + TAM + MESSAGING + POS.        ABM.md                 HOW to engage specific accounts
 8   /market emails       MESSAGING.md + ABM.md               EMAIL-SEQUENCES.md     EXACT sequences to send  ← PRIMARY

COMPLEMENTARY (optional — feed from emails for alignment)
 9   /market ads          MESSAGING + EMAIL-SEQUENCES         AD-CAMPAIGNS.md        PAID channel copy
10   /market landing      MESSAGING + EMAIL-SEQUENCES         LANDING-CRO.md         WHERE traffic converts
```

### Data Flow Diagram

```
STRATEGY.md ─────┬──────────────────────────────────────────────────────┐
                 │                                                      │
                 ▼                                                      │
             ICP.md ──────┬──────────────────────────────────────────┐  │
                          │                                          │  │
                          ▼                                          │  │
                      TAM.md ────────────────────────────┐           │  │
                          │                             │           │  │
                          │  COMPETITOR-REPORT.md ──┐   │           │  │
                          │                         ▼   │           │  │
                          │               POSITIONING.md─┤           │  │
                          │                         │   │           │  │
                          │                         ▼   │           │  │
                          │                   MESSAGING.md ──────────┴──┘
                          │               (+ content scan)    │
                          │                                   │
                          │                            ABM.md─┘
                          │                               │
                          │                    EMAIL-SEQUENCES.md  ← PRIMARY
                          │                        │         │
                          └──────────────▶  AD-CAMPAIGNS  LANDING-CRO
                                             (optional)   (optional)
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

**One command to run the full outbound GTM stack:**
```
/market gtm <url> <client-name>
```
Creates `clients/<client-name>/`, runs all 10 steps in sequence, saves every deliverable there.

**Or run steps individually:**
```
STRATEGIC LAYER
Step 1:  /market strategy <url>        → clients/<name>/STRATEGY.md
Step 2:  /market icp <url>             → clients/<name>/ICP.md
Step 3:  /market tam <url>             → clients/<name>/TAM.md
Step 4:  /market competitors <url>     → clients/<name>/COMPETITOR-REPORT.md

POSITIONING + MESSAGING
Step 5:  /market positioning <url>     → clients/<name>/POSITIONING.md
Step 6:  /market messaging <url>       → clients/<name>/MESSAGING.md

EXECUTION
Step 7:  /market abm <url>             → clients/<name>/ABM.md
Step 8:  /market emails <url>          → clients/<name>/EMAIL-SEQUENCES.md  ← PRIMARY

COMPLEMENTARY (optional)
Step 9:  /market ads <url>             → clients/<name>/AD-CAMPAIGNS.md
Step 10: /market landing <url>         → clients/<name>/LANDING-CRO.md
```

Optional analysis add-ons (run anytime):
```
         /market audit <url>            → clients/<name>/MARKETING-AUDIT.md
         /market seo <url>              → clients/<name>/SEO-AUDIT.md
         /market brand <url>            → clients/<name>/BRAND-VOICE.md
         /market report <url>           → clients/<name>/MARKETING-REPORT.md
         /market proposal <client>      → clients/<name>/CLIENT-PROPOSAL.md
```

---

## Skill Inventory: 21 Skills + 5 Agents

### Skills Created In-House (GTM-specific)
| Skill | Purpose | GTM Layer |
|-------|---------|-----------|
| market-strategy | Business model, brand voice, growth vectors, buying triggers | Strategic — Step 1 |
| market-icp | ICP builder for outbound | Strategic — Step 2 |
| market-tam | TAM/SAM/SOM sizing | Strategic — Step 3 |
| market-positioning | Competitive positioning | Positioning — Step 5 |
| market-messaging | Messaging architecture (iterates existing content) | Messaging — Step 6 |
| market-abm | Account-Based Marketing playbook | Execution — Step 7 |

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

    STRATEGY.md               ──▶      Pitch deck narrative, brand guidelines, sales brief
    ICP.md                    ──▶      Apollo / Sales Navigator list building
    TAM.md                    ──▶      Account prioritization & quota planning
    COMPETITOR-REPORT.md      ──▶      Battle cards for sales calls
    POSITIONING.md            ──▶      Website copy, pitch deck, sales narrative
    MESSAGING.md              ──▶      Cold email copy, LinkedIn DMs, call scripts
    ABM.md                    ──▶      CRM account tiers, engagement tracking
    EMAIL-SEQUENCES.md        ──▶      Instantly / Smartlead / Lemlist sequences  ← PRIMARY
    AD-CAMPAIGNS.md           ──▶      Google Ads, Meta Ads, LinkedIn Ads (aligned to emails)
    LANDING-CRO.md            ──▶      Webflow / Framer landing page (aligned to emails)
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
1. Run: `/market gtm <url> <ClientName>` — creates the folder and runs all 10 steps automatically
2. Optional: run analysis track for deeper audit
3. Optional: compile into report/proposal

**Cross-client insights:**
- Competitor reports may overlap (same industry)
- Messaging patterns that work for one client inform others
- ICP scoring rubrics can be templated across similar verticals
