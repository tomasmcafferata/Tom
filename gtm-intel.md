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

## Section 7: Best Intent Signals (2026)
*Source: coldiq.com / Michel Lieben*

A three-layer signal map showing where buying signals come from, from most owned (1st party) to most external (3rd party).

### First Party Signals (innermost — highest intent)
| Signal | Tools |
|--------|-------|
| Product Usage | Mixpanel, Amplitude, etc. |
| Meeting Forms | Chili Piper, HubSpot, Calendly |
| Gated Content | Webflow, Docsend, etc. |
| CRM Data | HubSpot, Salesforce, Clay |
| Call Transcripts | Fireflies, Gong, etc. |
| Marketing Sequence | ActiveCampaign, HubSpot, etc. |
| LinkedIn Signals | Clay, PhantomBuster, etc. |
| Website Visitor | RB2B, Instantly, Keyplay, Vento |

### Second Party Signals (middle layer)
| Signal | Tools |
|--------|-------|
| Afinity Signals | Affinity, Salesforce, etc. |
| Ad Engagement | Metadata, LinkedIn Ads, etc. |
| Review Sites | G2, Capterra, Trustpilot |
| Champion Tracking | Clay, Keyplay, etc. |

### Third Party Signals (outermost — broadest reach)
| Signal | Tools |
|--------|-------|
| Web Data | Similarweb, SparkToro, etc. |
| Funding Announcements | Crunchbase, Harmonic, LinkedIn, Elegrow |
| Job Openings Data | Clay, Keyplay, LinkedIn, Elegrow |
| Social Engagement | PhantomBuster, Clay, etc. |
| Person Data | LinkedIn, Clay, Claude |
| Lookalike Search | Ocean.io, Keyplay, etc. |
| Ads Activity | Aritic, SemRush, Ahrefs |
| Custom Scraping | Aritic, PhantomBuster, Clay |
| News | Keyplay, Google Alerts, etc. |
| Search Trends | Semrush, SimilarWeb, Ahrefs |
| Firmographic Data | Clay, Apollo, etc. |
| Technographic Data | BuiltWith, Keyplay, etc. |

---

## Section 8: Marketing Head Toolkit
*Practical AI + automation stack for a Head of Marketing*

| Category | Tool | What It Does |
|----------|------|-------------|
| **Sales Intelligence** | NotebookLM | Analyzes 2,000+ sales calls. Extracts patterns you'd never catch manually. |
| **Workflow Automation** | n8n | Reduces newsletter production from 2 hours → 15 min. Tracks 100+ sources via RSS. |
| **Content Drafting** | Claude | Connected to Drive + Notion. Knows your positioning. |
| **Vibe Coding** | Lovable | Builds sales tools in a day (vs. $5K+ agency quote + 2 months). |
| **Transcription** | Gemini | Best transcriptions on the market. Pulls context from your world. |
| **Engagement Alerts** | Slack Automations | Pings when ICP prospects post. No missed engagement windows. |

---

## Section 9: The One-Person AI Business — $1M Roadmap
*Source: chris-donnelly.co.uk*

**A 6-part roadmap to $1M with 0 employees.**

### 1. Spot the Pain
Find a boring pain point (repetitive, costly, ignored).
- Examples: sorting messy email inboxes, re-entering data into spreadsheets, filling repetitive online forms
- Map out the workflow: INPUTS → STEPS → OUTPUTS

### 2. Start as a Service
Do the job manually as a productised service.
- Prove demand before automation
- Charge from day one

### 3. Business Models
| Model | Description |
|-------|-------------|
| Productised Services | Fixed scope, fixed price |
| Cohorts / Courses | Time-boxed, outcome-driven |
| SaaS / Micro-tools | Automate one sharp workflow |
| Templates / Digital Assets | Recurring passive sales |

### 4. Marketing Engine
- **Listen:** Identify customer pain points using Listen Labs & AI research
- **Create:** Build site & content with Lovable + Searchable
- **Compound:** Drive traffic and earn mentions in ChatGPT & Perplexity using Searchable
- **Personalise:** Tailor experiences with Clay & Mutiny

### 5. Operations OS
**Rule:**
- If it repeats → automate
- If it needs judgement → template

**Key Tools:**
| Tool | Use |
|------|-----|
| Lindy | Inbox, scheduling, CRM |
| Fathom | Call memory |
| Cursor | Internal automations |
| Precision | Cockpit of live KPIs |

### 6. Sales Engine
```
CAPTURE → QUALIFY → NURTURE → CLOSE → EXPAND
```
- AI replies instantly, revives no-shows

**Deck structure (Gamma):** Problem → Proof → Plan → Price

**Offer Maths:**
- $3k/mo × 28 clients = $1M
- $1k product × 84/month = $1M
- $199 SaaS × 420 subs = $1M

---

## Section 10: GTM Engineer Cheat Sheet
*Source: coldiq.com / Michel Lieben*

### Responsibilities — Developing Effective Cold Outbound Strategies
- Understanding the target audience and segmenting it effectively
- Crafting compelling and concise email copy that captures attention and encourages action
- Ensuring emails meet inboxing criteria to minimize bounce rates and avoid spam filters
- Following industry best practices for deliverability and compliance
- Continually optimizing campaigns for lasting performance
- Monitoring campaign analytics to ensure optimal deliverability and engagement
- A/B testing email variations to determine the best approach
- Refreshing email content to avoid recipient fatigue
- Analyzing campaign responses to refine audience targeting
- Generating new strategies based on insights to keep campaigns fresh and compelling

### Sales Org Structure

```
GTM Engineer
├── Email Infrastructure
├── List Building
├── Account Enrichments
├── Contact Enrichments
├── Account & Contact Scoring
└── AI Personalized Copywriting
        ↓
      SDRs
├── Follow up with campaign replies
├── 1:1 manual prospecting top 1000 accounts
└── Inbound-led outbound plays
        ↓
      AEs
├── Demos
└── 1:1 manual prospecting top 200 accounts
```

### Tools Stack

**Data:** Clay, Apollo.io, Prospeo, FullEnrich, LinkedIn, Wiza, Exa, Spify, Openmart

**Deliverability:** Cloudflare, Gmail, Outlook

**AI Models:** ChatGPT, Claude, Gemini, OpenRouter

**Intent Signals:** Vector, CommonRoom, Halbounce, Relevance AI, Claude Code

**Automations:** n8n, Conductor

**Sales Engagement:** Lemlist, Instantly, Smartlead

### Metrics

| Category | KPIs |
|----------|------|
| **Deliverability** | Bounce rate, Unsubscribe rate, Domain reputation |
| **Engagement** | Open rate, CTR rate, Reply rate, Positive reply rate, Lead to positive reply ratio |
| **Outcome** | Meeting booked rate, Show up rate, Pipeline contribution, CAC, LTV/CAC, Revenue generated from campaigns |

### Campaign Playbook — Trigger Ideas

**Standard triggers:**
- G2 reviews, Attended Company Webinar, Attended LinkedIn Event, Engaged with company's posts, Engaged with founders' posts, Founders & CEOs Followers, Following company LinkedIn page, Following a competitor, Using a competitor

**Expansion triggers:**
- Ex-user / champion, Portfolio VC, Fibbler LinkedIn Ads, New team member, Skills-targeting, Role-targeting, Industry-level research, Resources for Individual Contributors

**Problem-aware triggers:**
- Leaving employees, Companies without an employee for the task, Bad reviews targeting, AI-generated ideas, Cold outreach tier 2,3,4, Facebook community page, IG followers

### Skills Required

**Business:** Market analysis, Competitive intelligence, Business strategy, Copywriting, Data-driven decision making, Cross-Functional Alignment

**Technical:** RevOps, CRM Systems, Data analysis, AI Sales tech stack, Data enrichment, A/B Testing, Deliverability optimization, Automation, API & Integration Knowledge

### Reading List (COLDIQ)
- Influence (Cialdini)
- Cold Email Manifesto
- Writing Tools
- Copywriting Secrets
- ColdIQ's Outbound Secrets (e-book)
- To Sell Is Human (Daniel H. Pink)
- Thinking Fast and Slow
- Hacking Growth

### GTM Engineering Pros to Follow
Kenny Damian, Eric Nowoslawski, Kellen Casebeer, Enzo Carasso, Alex Fine, Patrick Spychalski, Jordan Crawford, Brandon Charleson, Josh Whitfield

---

## Section 11: Outbound Playbook 2026
*Source: Reverrr / Guillermo Morcillo*

A structured end-to-end outbound system across 4 phases.

### Phase 1 — Set Up Account
**Tools:** Claude, Gemini, NotebookLM, ChatGPT

1. Initial Audit
2. ICP Definition
3. Value Prop
4. Messaging

### Phase 2 — Intelligence
| Stream | Tools |
|--------|-------|
| Market Research + Lead Enrichment + List Creation | Clay |
| Buying Signals | APIFY, Trigify.io, BuiltWith, TheirStack |

### Phase 3 — Implementation

| Channel | Sub-components |
|---------|---------------|
| **Cold Email** | Technical Setup, Email Sequence |
| **LinkedIn Outreach** | New Connections, Warm Messaging |
| **LinkedIn Content** | LinkedIn Content, Lead Magnets |

### Phase 4 — Sales Process
**Tools:** emlen, Default, Tally

```
Outbound → Meeting Booked → Demo → Trial → Revenue
```

---

*Document in progress — each section added from curated intel images*
