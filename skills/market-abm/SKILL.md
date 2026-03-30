# Account-Based Marketing Playbook

You are the ABM engine of the GTM stack. When invoked with `/market abm`, you produce a complete account-based marketing playbook: account tiers, list-building instructions, research card template, engagement playbooks by trigger type, weekly metrics, and the tool stack to run it all.

## When This Skill Is Invoked

The user runs `/market abm`. This is Step 7 of the GTM pipeline. Required inputs: ICP.md + MESSAGING.md. Reads TAM.md for segment prioritization.

---

## Inputs

Read the following files:
- `ICP.md` — **required** (account scoring rubric, firmographic/situational criteria, triggers)
- `MESSAGING.md` — **required** (hooks per trigger, follow-up sequence logic, sequence names)
- `TAM.md` — required (segment prioritization, volume estimates, list sources)
- `POSITIONING.md` — optional (competitive wedges for account-specific messaging)

---

## Core ABM Philosophy

State the guiding principle for this company's outbound model based on the inputs:

```
ABM PHILOSOPHY
==============

Model:        [Trigger-driven / Segment-driven / Named account / Volume-based]
Why:          [1–2 sentences explaining why this model fits this business]
Core insight: [The single observation that makes outreach 2–3x more effective
               for this company — e.g., "A prospect 90 days before a fixed event
               is 10x more likely to respond than the same prospect 6 months out"]
```

---

## Phase 1: Account Tiers

Define 3 tiers with clear, specific criteria drawn from the ICP scoring rubric:

```
TIER 1 — IMMEDIATE ATTACK
==========================
Criteria:     ICP score [X]–100 (per ICP.md rubric)
              + Active trigger identified (within [timeframe])
Volume:       [N] active accounts at any given time
Outreach:     Fully personalized per account — trigger name, event date,
              company-specific detail
Sequence:     [Sequence name from MESSAGING.md] — [N] steps over [N] days
Goal:         Meeting / discovery call within [N] weeks
Owner:        [SDR / founder / sales rep — specify]

Typical Tier 1 account:
  - [Characteristic 1 — specific firmographic]
  - [Characteristic 2 — specific trigger signal]
  - [Characteristic 3 — persona identified on LinkedIn]

TIER 2 — ACTIVE CULTIVATION
============================
Criteria:     ICP score [X]–[X]
              Industry fit confirmed, no active trigger yet
Volume:       [N] accounts in sequence at any given time
Outreach:     Semi-personalized — industry-specific pain, no trigger reference
Sequence:     [Sequence name] — [N] steps over [N] days, slower cadence
Goal:         Radar position — response when trigger appears
Owner:        Automated sequence in [Instantly / Smartlead / Lemlist]

TIER 3 — NURTURE / TEST
========================
Criteria:     ICP score [X]–[X]
              Adjacent industry or incomplete data
Volume:       Unlimited — batch processing
Outreach:     Generic by segment (ferias / fleet / retail / etc.)
Sequence:     [N] steps over [N] days
Goal:         Message testing, surface hidden Tier 2 accounts
Owner:        Fully automated
```

---

## Phase 2: List Building Instructions

For each source from TAM.md, write step-by-step instructions:

### Source 1: [Highest-quality trigger source — e.g., event exhibitor lists]

```
STEP-BY-STEP:
  1. [Go to X website / directory / database]
  2. [Navigate to: section name]
  3. [Download / collect: what to get]
  4. [Cross-reference with: LinkedIn / Apollo / Clay]
  5. [Filter: criteria to apply]
  6. [Find contact: how to find the champion persona at each company]
  7. [Score: apply ICP rubric from ICP.md]
  8. [Add to: Tier 1 list in CRM/sheet]

Volume estimate: ~[N] accounts per [period]
Time to build: ~[X] hours for first [N] accounts
```

### Source 2: LinkedIn Sales Navigator

```
SAVED SEARCH FILTERS:
  Industry:      [Filter values]
  Company size:  [Filter values]
  Geography:     [Filter values]
  Title:         [Filter values]
  Keywords:      [Filter values]

POST-FILTER QUALIFICATION:
  Check:  [What to verify before adding to sequence]
  Remove: [Disqualifiers to catch that the filter misses]

Volume estimate: ~[N] ICP-fit accounts
```

### Source 3: Trigger monitoring (ongoing, weekly)

```
WEEKLY SEARCH STRINGS (run in LinkedIn + Google):
  "[Search string 1]"
  "[Search string 2]"
  "[Search string 3]"

  → Each match = potential Tier 1 account
  → Process: identify champion → score → add to Tier 1 Research Card queue

ALERTS TO SET UP:
  Google Alerts: [Alert strings for company announcements, events, rebrands]
  LinkedIn notifications: [Industry groups, event hashtags to follow]
```

---

## Phase 3: Research Card Template

Provide the complete research card for qualifying and tracking each account:

```
RESEARCH CARD — [TIER] ACCOUNT
================================

BASIC DATA
  Company:          _______________
  Website:          _______________
  LinkedIn:         _______________
  Employees:        _______________
  Industry:         _______________

TRIGGER
  Type:             [ ] [Trigger 1]  [ ] [Trigger 2]  [ ] [Trigger 3]  [ ] [Trigger 4]
  Detail:           _______________
  Date / deadline:  _______________
  Source found:     _______________

CHAMPION CONTACT
  Name:             _______________
  Title:            _______________
  LinkedIn:         _______________
  Email:            _______________
  Time in role:     _______________
  Active on LinkedIn: [ ] Yes  [ ] No
  Last post topic:  _______________

ICP SCORE
  Firmographic:     ___/[X]
  Situational:      ___/[X]
  Persona:          ___/[X]
  TOTAL:            ___/100
  Tier:             [ ] T1  [ ] T2  [ ] T3

SEQUENCE ASSIGNED
  Sequence name:    _______________
  Start date:       _______________
  Channel:          [ ] Email  [ ] LinkedIn  [ ] Both

PERSONALIZATION NOTES
  Specific hook:    _______________
  Event/trigger ref: _______________
  Company-specific detail: _______________

STATUS
  [ ] Researching
  [ ] Ready for outreach
  [ ] Step 1 sent — date: ___
  [ ] Step 2 sent — date: ___
  [ ] Step 3 sent — date: ___
  [ ] Step 4 sent — date: ___
  [ ] Response received — type: _______________
  [ ] Meeting booked — date: ___
  [ ] Proposal sent
  [ ] Won / Lost / Deferred — outcome: _______________
```

---

## Phase 4: Engagement Playbooks by Account Type

Write a day-by-day engagement playbook for each trigger type:

```
PLAYBOOK: [Account type — e.g., "Trade Show Exhibitor"]
==========================================================

DAY 0   RESEARCH
          [What to verify / find before first contact]
          [Go/no-go check: what disqualifies this account]

DAY 1   [CHANNEL 1 — e.g., Email Step 1]
          Sequence: [name]
          Angle: [hook from MESSAGING.md]
          + [CHANNEL 2 — e.g., LinkedIn connection request]
            Note: [copy from MESSAGING.md LinkedIn library]

DAY [X] [Follow-up step] — [angle]
DAY [X] [Follow-up step] — [angle]
DAY [X] [Final step] — soft close

DAY [X+N] NURTURE — post-trigger follow-up

RULES:
  - Remove from sequence immediately if they respond
  - Move to NURTURE if no response after [N] steps
  - [Any other sequence-specific rules]
```

Create playbooks for each major trigger type (minimum 2–3 playbooks).

---

## Phase 5: KPIs and Weekly Metrics

Define the metrics to track and the targets to hit:

```
WEEKLY METRICS DASHBOARD
==========================

ACTIVITY
  New Tier 1 accounts added this week:        _____ (target: [N])
  Emails sent (total):                        _____ (target: [N])
  LinkedIn connections sent:                  _____ (target: [N])

RESPONSE RATES
  Email open rate (target: >[X]%):            _____%
  Email reply rate (target: >[X]%):           _____%
  LinkedIn acceptance rate (target: >[X]%):   _____%
  Positive responses (interest):              _____

PIPELINE
  Meetings booked this week:                  _____
  Meetings held:                              _____
  Proposals sent:                             _____
  Deals closed this month:                    _____
  Revenue generated:                          _____

BENCHMARK — MONTH 1–2 (no social proof):
  Reply rate:    [X]%
  Meetings / 50 accounts:  [N]–[N]
  Deals / 10 meetings:     [N]–[N]

BENCHMARK — MONTH 3+ (with case studies):
  Reply rate:    [X]% (estimated lift: [X]%)
  Meetings / 50 accounts:  [N]–[N]
```

---

## Phase 6: Tech Stack

Recommend the minimum tool stack to run this ABM system:

```
TOOL STACK
===========

TOOL              PURPOSE                    PRIORITY   NOTES
───────────────────────────────────────────────────────────────────
[Tool 1]          [Outbound sequences]       Must       [Configuration note]
[Tool 2]          [List building/enrichment] Must       [Alternative if budget]
[Tool 3]          [CRM]                      Must       [When to upgrade]
[Tool 4]          [LinkedIn outreach]        High       [Compliance note if relevant]
[Tool 5]          [Intent / monitoring]      Medium     [Optional]

MINIMUM TO LAUNCH:
  1. [Step 1 — e.g., set up sending domain + warmup]
  2. [Step 2 — e.g., build first 30 research cards]
  3. [Step 3 — e.g., load first sequence]
  Launch timeline: [N] days from decision to first email sent
```

---

## Phase 7: Immediate Action Plan

Close with a specific "this week" action list based on the current date and trigger calendar from TAM.md:

```
THIS WEEK — IMMEDIATE ACTIONS
==============================

Most urgent trigger:  [Trigger name] — [days until window closes]

Action 1 (today):     [Specific task — e.g., "Pull ExpoX exhibitor list from [url]"]
Action 2 (today):     [Specific task]
Action 3 (this week): [Specific task]
Action 4 (this week): [Specific task — e.g., "Build first 30 Research Cards"]
Action 5 (this week): [Specific task — e.g., "Configure Instantly domain warmup"]

Decision needed from client: [What must the client provide — e.g., case study photos]
Timeline: First emails can go out: [estimated date]
```

---

## Output Format: ABM.md

Save to `clients/<ClientName>/ABM.md` or `ABM.md` in current directory.

Structure: ABM Philosophy → Account Tiers → List Building Instructions → Research Card Template → Engagement Playbooks → Metrics Dashboard → Tech Stack → Immediate Actions → Next Steps

---

## Terminal Output

```
=== ACCOUNT-BASED MARKETING PLAYBOOK ===

Company: [name]

ABM Model: [type]
Account tiers: Tier 1 (~[N] active) / Tier 2 (~[N] in sequence) / Tier 3 (batch)

Engagement playbooks: [count]
List sources: [count]

Most urgent trigger: [name] — [timeframe]
Recommended first list: [source name] — ~[N] Tier 1 accounts available

Tech stack: [tool 1], [tool 2], [tool 3]
Time to first email: ~[N] days

ABM playbook saved to: ABM.md

Next: /market emails → generate ready-to-load sequences for Instantly/Smartlead
```

---

## Quality Standards

- **Playbooks must be day-by-day** — not vague "contact them multiple times"
- **Research card must be fillable by a non-technical person** — checkboxes, clear labels
- **Metrics must have targets** — not just "track this", but "target: >8% reply rate"
- **Immediate actions must be specific and dated** — "pull the exhibitor list from [url]" not "build a list"
- **Tech stack must include free alternatives** — not everyone has a $500/month tool budget

---

## Cross-Skill Integration

- Reads: `ICP.md`, `MESSAGING.md`, `TAM.md`, `POSITIONING.md`
- Outputs feed: `/market emails` (sequence names + trigger types to build for)
- After completion, suggest: `/market emails` as the immediate next step — sequences can load into Instantly same day
