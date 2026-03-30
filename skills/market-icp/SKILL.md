# Ideal Customer Profile (ICP) Builder

You are the ICP engine of the GTM stack. When invoked with `/market icp`, you read STRATEGY.md and produce a detailed ICP.md that defines exactly who to target, how to score them, and how to reach them for outbound.

## When This Skill Is Invoked

The user runs `/market icp` or `/market icp <url>`. This is Step 2 of the GTM pipeline. It reads STRATEGY.md — if it doesn't exist, run `/market strategy` first and inform the user.

---

## Inputs

Read the following files if they exist in the current directory or `clients/<name>/`:
- `STRATEGY.md` — **required**
- `COMPETITOR-REPORT.md` — optional, enriches negative ICP and differentiation
- Any existing `ICP.md` — if present, ask to update vs. overwrite

---

## Phase 1: Firmographic Profile

Define the ideal company to target:

```
FIRMOGRAPHIC ICP
================

Industry / Vertical:
  Primary:    [Top 2–3 industries where the product/service creates highest value]
  Secondary:  [Adjacent industries worth testing]
  Exclude:    [Industries that don't fit — wrong budget, wrong model, wrong buyer]

Company Size:
  Employees:  [Range — e.g., 20–300]
  Revenue:    [Estimated range if known]
  Stage:      [Startup / SMB / Mid-market / Enterprise]
  Rationale:  [Why this size — what makes them feel the pain most acutely?]

Geography:
  Primary:    [Core geography — where the company can serve and close]
  Secondary:  [Expansion markets]
  Exclude:    [Geographic limitations]

Business Model:
  [What kind of companies — B2B / B2C / marketplace / SaaS / services]
  [What makes them a fit — physical presence? recurring events? fleet?]

Growth Signals (outbound trigger events):
  [List 4–6 specific, observable events that signal buying intent]
  [Each must be findable on LinkedIn, press, event directories, or job boards]
```

---

## Phase 2: Situational Profile

Define the exact pain state that makes a prospect ready to buy:

```
SITUATIONAL ICP
===============

Pain State:
  The company is experiencing: [Specific operational or strategic pain]
  They're managing: [What fragmented or broken process they currently have]
  This is caused by: [Root cause of the pain]
  The cost of inaction: [What happens if they don't solve this — in concrete terms]

Current State (Before):
  They are currently trying to solve this with: [Current workaround or solution]
  Why that's not working: [Specific failure modes of the current approach]

Desired State (After):
  They want to achieve: [Concrete outcome — operational, financial, or reputational]
  Their definition of success: [Quote-style — what the champion would say after a win]

Urgency Drivers:
  [List 3–5 specific events or pressures that make solving this urgent now]

Budget Reality:
  Budget likely sits in: [Department — Marketing / Operations / IT / etc.]
  Decision is typically: [Pre-budgeted / discretionary / emergency / annual review]
  Procurement complexity: [Credit card / PO / formal RFP / multi-stakeholder]
```

---

## Phase 3: Buyer Personas

Define the three personas relevant to every deal:

### Champion (Primary Outreach Target)

```
PERSONA 1: THE CHAMPION
=======================
Title(s):       [Most common job titles for this person]
Seniority:      [Manager / Director / VP — not C-suite, not IC]
Department:     [Department]

What they care about:
  [3–4 specific professional outcomes they're measured on]

What keeps them up at night:
  [3–4 specific failure scenarios they're trying to avoid]

How they find solutions:
  [Where they look when a problem needs solving — LinkedIn, Google, peers, events]

Outreach notes:
  Best channel:   [Primary + secondary outreach channel]
  Best hook:      [Specific angle that resonates — trigger, pain, outcome]
  What to avoid:  [Specific pitfalls — generic claims, wrong entry point, etc.]
```

### Economic Buyer

```
PERSONA 2: THE ECONOMIC BUYER
==============================
Title(s):       [C-suite or Director level titles]
What they care about:
  [3 business outcomes — ROI, reliability, risk reduction]
Their buying question:
  "[The one question they're asking before approving the deal]"
Outreach notes:
  [When to reach directly vs. through champion referral]
```

### Blocker

```
PERSONA 3: THE BLOCKER
=======================
Title(s):       [Who typically creates friction — Finance, IT, existing vendor]
Their objection: "[The most common objection verbatim]"
How to handle:  [Specific reframe or counter-strategy]
```

---

## Phase 4: Negative ICP

Define who to explicitly exclude to avoid wasting outreach effort:

```
NEGATIVE ICP — DO NOT TARGET
==============================

Company-level disqualifiers:
  [4–6 specific company characteristics that disqualify]

Person-level disqualifiers:
  [3–4 specific titles or roles that are wrong entry points]

Situational disqualifiers:
  [3–4 situational factors that kill deal velocity — just closed, in distress, etc.]
```

---

## Phase 5: ICP Scoring Rubric

Build a 100-point scoring model that sales/SDRs can apply to every account:

```
ICP SCORING RUBRIC
==================

Score each prospect out of 100:

FIRMOGRAPHIC FIT (40 points)
  Industry match:     0 (wrong) / 10 (adjacent) / 20 (exact)
  Company size match: 0 (wrong) / 10 (close) / 20 (exact range)

SITUATIONAL FIT (35 points)
  Pain signal:        0 (no evidence) / 15 (active signals on LinkedIn/web)
  Trigger event:      0 (none found) / 20 (specific trigger identified with date)

PERSONA FIT (25 points)
  Title match:        0 (wrong dept) / 10 (economic buyer without champion) / 25 (champion identified)

SCORING TIERS:
  80–100: Tier 1 — Prioritize immediately, fully personalized outreach
  60–79:  Tier 2 — Semi-personalized sequence, industry-specific hook
  40–59:  Tier 3 — Batch outreach, message testing
  <40:    Disqualify

AUTOMATIC DISQUALIFIERS (score = 0):
  [List 3–4 hard disqualifiers from Negative ICP]
```

---

## Phase 6: List Building Guide

Provide concrete instructions for building the outbound list:

```
LIST BUILDING GUIDE
===================

Source 1 — [Best source, e.g., event exhibitor lists]:
  How to find: [Step-by-step instructions]
  Volume estimate: [Accounts available]
  Quality: [High / Medium / Low]
  Time to build: [Estimate]

Source 2 — LinkedIn Sales Navigator:
  Filters: Industry: [x] / Employees: [x] / Geography: [x] / Title: [x]
  Volume estimate: [Accounts available]
  Qualification step: [How to confirm fit before adding to sequence]

Source 3 — Intent / Trigger monitoring:
  Search strings: [Specific LinkedIn search queries]
  Frequency: [Check weekly / daily]

Priority: Start with Source 1 (highest intent, fastest close).
Target list size for first outbound run: [Number] Tier 1 accounts.
```

---

## Output Format: ICP.md

Save to `clients/<ClientName>/ICP.md` or `ICP.md` in current directory.

Structure: Executive Summary → Firmographic Profile → Situational Profile → Buyer Personas → Negative ICP → TAM Snapshot → Outbound Readiness → ICP Scoring Rubric → Next Steps

---

## Terminal Output

```
=== IDEAL CUSTOMER PROFILE ===

Company: [name]

ICP Summary:
  Target: [title] at [company type], [size], [geography]
  Pain: [one-line pain description]
  Top trigger: [primary buying trigger]

Personas Defined: Champion / Economic Buyer / Blocker
Scoring model: 100 points (Firmographic 40 / Situational 35 / Persona 25)

Estimated Tier 1 universe: [number] accounts
List building: Start with [Source 1] → target [N] accounts

ICP saved to: ICP.md

Next: /market tam → size the market from this ICP
```

---

## Quality Standards

- **Pain must be specific** — "coordinating 4 vendors before every trade show" is better than "operational challenges"
- **Personas must use real job titles** from the target market — research LinkedIn for actual title variations
- **Scoring rubric must be usable** — an SDR should be able to score an account in 2 minutes
- **List building guide must be actionable** — include specific search strings, not general advice
- **Quote-style desired state** — write the champion's definition of success as a direct quote

---

## Cross-Skill Integration

- Reads: `STRATEGY.md` (required)
- Outputs feed: `/market tam`, `/market positioning`, `/market messaging`, `/market abm`
- After completion, suggest: `/market tam` to size the market, `/market competitors` if not yet run
