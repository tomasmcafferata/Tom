# GTM Intelligence & Process Foundation

A living document compiling frameworks, systems, and processes for building scalable GTM operations.

---

## Section 1: The Outbound System Behind $14M in Generated Revenue
*Source: Kinetyca.com / Matteo Fois*

Signal-based targeting, built into a system that runs without you.

### Signal Layer — What Triggers the System

| Signal | Tools |
|--------|-------|
| Hiring signals (budget exists, pain is live) | Apollo, Sales Navigator |
| Funding rounds (new spend, new priorities) | Crunchbase, Apollo |
| Tech stack changes (evaluation window open) | BuiltWith, Datanyze |
| LinkedIn activity (pain being expressed publicly) | Sales Navigator, Clay |
| Intent data (actively researching) | Bombora, G2 |
| Company growth (headcount velocity rising) | Apollo, LinkedIn |

### What Most Teams Skip — The Infrastructure Layer

**Score**
- Signal-based tiering: T1 / T2 / T3
- T1 + T2 signals firing at once
- Not all signals carry equal weight

**Route**
- T1 → Multi-channel, immediate
- T2 → LinkedIn first, email follows
- T3 → Nurture queue / monitor only

**CRM Sync**
- Every signal auto-logged
- Zero manual data entry
- Full pipeline visibility from trigger one

> *"Without this layer outbound is just guessing with extra steps."*

### Channel Execution — What Goes Out and When

- **Cold email:** Smartlead, Email Bison — Hook + reference the signal directly. 4 lines max, one ask, no pitch.
- **LinkedIn outbound:** HeyReach, Gojaberry — Signal as connection context. Value before the ask. T1 + T2 only.
- **Multi-channel sequence:** Email → LinkedIn connect → LinkedIn message → Email follow-up → Final touch (Claude, Clay)

### Full System Flow

```
SIGNAL → ENRICH → SCORE → ROUTE → SEQUENCE → CRM SYNC → CONVERT
```

> Score → Route → CRM Sync = the three steps 90% of outbound teams skip entirely

---

## Section 2: 16 AI Workflows & Prompts for RevOps

### Section 2.1 — AI in RevOps: The Basics

**What AI Can Replace, Augment, and Should Stay Human In:**
- **Replace:** Repetitive, data-heavy tasks with clear inputs/outputs (pipeline hygiene checks, call summaries, MEDDIC scoring)
- **Augment:** Tasks where AI does the heavy lifting but a human makes the final call (forecast prediction, deal risk flagging, win/loss patterns)
- **Stay Human:** Judgment calls, relationships, accountability (e.g. final forecast commit, rep coaching conversations, executive alignment)

**Anatomy of a Good RevOps Prompt:**
- Role (tell AI who it is)
- Context (what data, deal, or situation you're feeding it)
- Task (what exactly you want it to do)
- Output format (table, bullets, summary, score)
- Constraints (what to ignore, what to prioritize)

**AI as a Search Engine vs. AI as a Workflow Engine:**
- Search engine mode: reactive, one question, one answer
- Workflow engine mode: proactive, structured input → measured output → action
- Workflow mode is where RevOps gets real ROI

### Section 2.2 — Revenue Intelligence Workflows

| Workflow | Purpose |
|----------|---------|
| Win/Loss Analysis | Identify patterns across won/lost deals |
| Competitive Intelligence | Track competitive win rates and patterns |
| Churn Signal Detection | Flag at-risk accounts proactively |
| ICP & Segmentation Analysis | Score and segment accounts by fit |

**Win/Loss Analysis Workflow (Schedule-Triggered — 1st Monday, 8am):**
1. Get/Lookup Record → Opportunity (Closed-Won, Closed-Lost, last 30d)
2. AI Agent → Win/Loss Analysis
3. Create Report → Summary Report
4. Send Internal Email → 3 recipients

### Section 2.3 — Deal Intelligence Workflows

| Workflow | Purpose |
|----------|---------|
| Deal Risk Assessment | Flag deals at risk before they slip |
| MEDDIC Compliance Check | Ensure qualification completeness |
| Key Objections Surfacing | Identify and prepare for common objections |
| Conversation & Call Intelligence | Extract insights from calls automatically |

**Deal Risk Assessment Workflow (Schedule-Triggered — Monday 9am, Weekly):**
1. Get/Lookup Record → Opportunity (Not Closed-Won, Closed Lost)
2. AI Agent → Assess deal risk
3. AI Agent → Flag deals
4. Send Slack Message → 1 recipient

### Section 2.4 — Pipeline & Forecast Workflows

| Workflow | Purpose |
|----------|---------|
| Coverage Analysis | Assess pipeline coverage vs. targets |
| Pipeline Hygiene Check | Clean stale/inaccurate pipeline data |
| Forecast Prediction | AI-assisted forecast accuracy |
| Scenario Planning | Model different attainment scenarios |

**Coverage Analysis Workflow (Schedule-Triggered — Monday 9am, Weekly):**
1. Get/Lookup Record → Opportunity (Not Closed-Won, Closed-Lost)
2. AI Agent → Pipeline coverage analysis
3. Create Report → Report by team and territory
4. Send Internal Email → 5 recipients

### Section 2.5 — AI Productivity Workflows

| Workflow | Purpose |
|----------|---------|
| AI CRM Updates | Auto-update CRM fields post-call |
| AI Call Summary (MEDDIC) | Structured call notes from recordings |
| AI Call Coaching & Scoring | Score rep performance automatically |
| AI Follow-Up Emails | Draft contextual follow-ups after calls |

**AI CRM Updates Workflow (Record-Triggered — when record is created):**
1. Get/Lookup Record → Recording
2. AI Agent → Update Salesforce MEDDIC fields
3. AI Agent → Update next steps field

---

## Section 3: Email Deliverability Checklist for 2026
*Source: Kinetyca.com / Matteo Fois*

**Setup → Configure → Weekly Loop**

### Step 1 — BUILD (1-time setup)

1. **Pick a provider tier:**
   - Managed: 35/day
   - Standard: 20/day
   - Hypertide: 2/day

2. **Buy domains + inboxes**

3. **Log everything in an Infra Tracker (Google Sheet)**
   - Columns: Domain | Inbox | Provider | Region | Launch Date | Group | Status

### Step 2 — CONFIGURE (essentials)

1. **Inbox settings:**
   - Min gap: 10 min
   - Daily limit: 35 / 20 / 2 (by provider)

2. **Campaign settings:**
   - Trigger delay: 12 min
   - Timezone aligned + region segmented

3. **Tags (required):**
   - launch DD/MM/YYYY
   - US / EU / APAC
   - Group 1–5

### Step 3 — WEEKLY DELIVERABILITY LOOP (run every week)

1. **Reconnect** — Fix disconnected inboxes
2. **Health check** — Smartlead warmup reputation; <85 = at risk
3. **Rotate** — Rotate 1 group on schedule; keep a bench pool ready; Hypertide: 2/day
4. **Rehab (if at risk)** — Bench inbox; drop to 5/day; warmup stays ON; tag: burn relaunch DD/MM/YYYY

**Capacity rule:** Keep ~65–80% sending active (pause rotation if bench gets too big)

### Non-Negotiables
- Warmup stays ON (always)
- Mailboxes are region-locked (US→US, EU→EU, APAC→APAC)
- Rotation is prevention (don't wait for burn)

---

## Section 4: Claude Code — GTM Skills Stack

### Core Outbound Workflow

| Step | Skill | What It Does |
|------|-------|--------------|
| 0 | `//company-context-builder` | Define ICP, product language, win cases; auto-updated from call recordings |
| 1 | `/list-building` | Hypothesis-driven prospecting; lookalikes OR instant search; 200–500 companies |
| 2 | `/market-problems-deep-research` | Industry pain discovery; what leaders are saying; educate before targeting |
| 3 | `/data-points-builder` | Segmentation + personalization signals; podcasts, launches, hiring, messaging |
| 4 | `/table-enrichment` | Extract enrichment layer; structured monitoring + quality control |
| 5 | `/list-building` (refined) | Re-run search using exact datapoints |
| 6 | `/tiering-&-segmentation` | Align segments with problem hypotheses |
| 7 | `//email-generation` | Strict instruction-based composition; Python assembly layer; iterative refinement in-chat |
| 8 | `//copy-feedback` | Simulate cold-reader persona; stress-test message; refine per prospect |
| 9 | `/run-instantly` | Push to Instantly before send |

---

## Section 5: The LLM Stack for Modern GTM Teams in 2026
*Source: Kinetyca.com / Matteo Fois*

### Model Roles

| Model | Best Used For |
|-------|--------------|
| **GPT-4o mini** (via Clay API) | All Clay-related automation and enrichment: lead enrichment from LinkedIn/Apollo, data cleanup and formatting, short prospect summaries, filling personalization variables in templates, quick grammar/phrasing fixes at scale |
| **Claude Opus 4.6** | High-quality, human-sounding writing: cold email sequences (first touch, follow-ups, breakups), reframing messaging for different personas or industries, drafting case studies and customer stories, writing social content with a conversational tone |
| **Gemini 3** | Deep research and strategic thinking: market mapping and niche segmentation, competitor and product analysis, finding relevant events/podcasts/communities, long-form brainstorming for campaigns and positioning |
| **GPT-5.2** | Solving complex, multi-step problems: designing sophisticated GTM workflows and automation logic, multi-factor decision-making, synthesizing insights from mixed data sources, building multi-layered campaign plans with contingencies |

### GTM Flow — Which LLM Where

```
Gemini 3          → GPT-4o mini (Clay)     → Claude 4.6       → GPT-4o mini (Clay)        → GPT-5.2
Research ICP,        Pull and enrich lead      Write persuasive    Deploy campaigns and         Troubleshoot complex
market, competitors, data, clean fields,       outreach            run quick A/B copy tests.    campaign challenges,
and messaging        fill personalization.     sequences.                                       optimize targeting,
angles.                                                                                         plan scaling strategy.
```

---

## Section 6: 8 Skills to Master as a GTM Engineer
*Source: workflows.io / Fivos Aresti*

### 1. Tech Stack Evaluations
Key tools to know: Clay, Apollo, Salesforce, Instantly, Finymail, Discolike, HeyReach, Snowflake, Ocean.io, Bettercontact, Hubspot, Nooks

### 2. TAM Mapping
- Find companies with Store Leads → Source
- Import data from Apify actor → Data
- Discolike export/discover → Data
- Apify Export → Custom table
- Target Account List (final output)

### 3. Workflow Design
Full outbound automation stack:
- OutboundSync → Instantly + HeyReach → Outbound Campaigns → Automatic Contact Creation → Hubspot (move deal stage) → Triggers: Reply / Sign Up → Slack notifications

### 4. Signal Tracking
Signal layers from outer to inner:
- **3rd-Party Signals:** Firmographic data, social signals, people data, search analytics, web data, job openings, review sites, news, technographic data, funding announcements, ad insights, LinkedIn engagement, champion tracking, advertisement activity
- **2nd-Party Signals:** Partner signals, meeting form, gated content, outreach replies, marketing sequences
- **1st-Party Signals:** Product usage, website visitor, CRM data

### 5. Data Enrichment (Clay-style)
| Enrichment | Cost |
|-----------|------|
| Use AI (Artificial Intelligence) | 0.1/row |
| Enrich Company (Companies, People, Jobs) | 1/row |
| Work Email | ~3/row |
| Company Domain | ~1/row |
| Website Traffic (Monthly) | ~3/row |
| Company Latest Funding | ~4/row |
| Website Techstack | ~6/row |
| Company Revenue | ~9/row |

### 6. Automated Outbound
1. ICP Model
2. List Building (Claude)
3. Data Enrichment (Clay)
4. Lead Scoring (Clay)
5. Enroll to Manual Sequences (Claude)
6. Automate Email Campaigns (Instantly)
7. Automate LinkedIn Campaigns (HeyReach)

### 7. Inbound Orchestration
1. Capture & Initial Qualification (Claude, Slack, Webflow)
2. Lead Routing (Chili Piper, Clay, Cal)
3. Approving Leads (Hubspot, Chili Piper, Slack)
4. Deep Enrichment (Clay, Email tools)
5. CRM Sync & Preparation (Slack, Hubspot)
6. Meeting Execution & Intelligence Layer (tools for call intel)

### 8. Awareness Stage Scoring
```
Identified → Aware → Interested → Evaluating → Selecting
```

### Reading List
- Cold Email Manifesto
- $100M Leads
- To Sell Is Human (Daniel H. Pink)
- Gap Selling
- Influence (Cialdini)
- $100M Offers
- Exactly What to Say
- Everybody Writes
- Hacking Growth

---

*Document in progress — each section added from curated intel images*
