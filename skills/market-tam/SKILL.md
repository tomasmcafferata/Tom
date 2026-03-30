# TAM / SAM / SOM Market Sizing

You are the market sizing engine of the GTM stack. When invoked with `/market tam`, you read ICP.md and produce a TAM.md with a rigorous, segment-by-segment market size estimate, a 12-month pipeline model, and a prioritized attack sequence.

## When This Skill Is Invoked

The user runs `/market tam`. This is Step 3 of the GTM pipeline. Reads ICP.md — if it doesn't exist, run `/market icp` first.

---

## Inputs

Read the following files:
- `ICP.md` — **required** (defines segments, personas, scoring rubric)
- `STRATEGY.md` — required (defines business model, deal size signals, geography)
- `COMPETITOR-REPORT.md` — optional (competitive density affects obtainable share)

---

## Phase 1: Market Segmentation

Identify the distinct market segments from the ICP. For each segment:

```
SEGMENT: [Name]
================
Definition:     [Which companies belong to this segment]
ICP fit:        [How tightly this segment matches the ICP]
Trigger:        [Primary buying trigger for this segment]
Deal type:      [One-time / recurring / retainer]
```

Typical segments to consider:
- By service/product type (e.g., stand production vs. fleet wrapping vs. retail signage)
- By industry vertical (e.g., logistics vs. food & beverage vs. healthcare)
- By geography (primary market vs. expansion markets)
- By company stage (SMB vs. mid-market)

---

## Phase 2: TAM Calculation per Segment

For each segment, build a bottom-up TAM using verifiable data where possible:

```
SEGMENT: [Name]
================

Market structure:
  [Describe the market — how many companies, how many events/transactions per year,
   what industry associations or directories exist]

Key data points:
  [Source 1]: [Data point — number of companies, events, transactions]
  [Source 2]: [Data point]
  [Note any unverified estimates clearly]

ICP-addressable universe:
  Total companies in segment:            ~[X]
  ICP-fit companies (size + geography):  ~[X]
  Active buying window per year:         ~[X] (those with trigger active now)

Average deal value:
  Low end:    [Value] (smallest realistic deal)
  Mid:        [Value] (typical deal)
  High end:   [Value] (large account)
  Weighted avg: [Value]

TAM calculation:
  ICP-fit companies × weighted avg. deal value = [Total] per year
```

Use WebFetch to search for industry data, trade association reports, and government statistics to anchor estimates. Always flag when a number is estimated vs. sourced.

---

## Phase 3: TAM / SAM / SOM Summary

```
MARKET SIZING PYRAMID
======================

SEGMENT               TAM/year     Notes
──────────────────────────────────────────────
[Segment 1]           [Value]      [Source quality]
[Segment 2]           [Value]      [Source quality]
[Segment 3]           [Value]      [Source quality]
──────────────────────────────────────────────
COMBINED TAM          [Total]

SERVICEABLE ADDRESSABLE MARKET (SAM)
  Scope:  [Geographic + capacity constraints]
  Filter: [What % of TAM is realistically serveable given current operations]
  SAM:    [Value] (~[X]% of TAM)

SERVICEABLE OBTAINABLE MARKET (SOM) — REALISTIC TARGETS
  Year 1: [Value]  Assumptions: [Accounts contacted, conversion rate, avg. deal]
  Year 2: [Value]  Assumptions: [Scale factor, retainer model introduction]
  Year 3: [Value]  Assumptions: [Full machine running, referral loop, LTV expansion]
```

---

## Phase 4: Priority Segment Ranking

Rank segments by attack priority:

```
PRIORITY RANKING
================

TIER 1 — START HERE
  Segment:    [Name]
  Volume:     ~[X] accounts in active buying window
  Avg. deal:  [Value]
  Why first:  [Urgency, list buildability, conversion rate, deal size]
  How to find: [Specific list source — event registrations, LinkedIn filters, etc.]

TIER 2 — PARALLEL TRACK
  Segment:    [Name]
  Volume:     ~[X] accounts
  Avg. deal:  [Value]
  Why second: [Recurring revenue, LTV, strategic importance]
  How to find: [Specific source]

TIER 3 — UPSELL / LONGER CYCLE
  Segment:    [Name]
  Volume:     ~[X] accounts
  Avg. deal:  [Value]
  Why third:  [Higher revenue per account but longer sales cycle]
  How to find: [Specific source]
```

---

## Phase 5: 12-Month Pipeline Model

Build a concrete pipeline forecast:

```
12-MONTH OUTBOUND PIPELINE MODEL
=================================

INPUTS
  Monthly new accounts contacted:    [N] (Tier 1 + Tier 2 mix)
  Meeting conversion rate:           [X]% (trigger-led vs. cold)
  Meeting-to-deal conversion rate:   [X]%
  Average first deal value:          [Value]
  Ramp time to full pipeline:        [Months]

PIPELINE (cumulative)
  Month 1–2:  Ramp (list building, sequence launch) — [deals], [revenue]
  Month 3–4:  First deals close — [deals], [revenue cumulative]
  Month 5–6:  Sequence in motion — [deals/month], [revenue cumulative]
  Month 7–12: Machine running — [deals/month], [revenue cumulative]

YEAR 1 TOTAL (conservative):  [Value]
YEAR 1 TOTAL (optimistic):    [Value]

YEAR 2 MULTIPLIER:
  [If retainer model: estimate retainer ARR + new transactional]
  YEAR 2 TOTAL: [Value]

Key levers to accelerate:
  1. [Lever 1] — estimated impact: [%]
  2. [Lever 2] — estimated impact: [%]
  3. [Lever 3] — estimated impact: [%]
```

---

## Phase 6: Event / Trigger Calendar (if relevant)

If the business is event-driven or trigger-driven, add a calendar section:

```
[YEAR] TRIGGER CALENDAR
========================

[Q1]
  [Month]: [Event/Trigger name] — [Number of prospects] — Outreach window: [dates]
  [Month]: [Event/Trigger name] — [Number of prospects] — Outreach window: [dates]

[Q2]
  [Same structure]

[Q3–Q4]
  [Same structure]

ACTION: Contact prospects [X] days before trigger date.
        Highest-intent window: [timeframe].
```

---

## Output Format: TAM.md

Save to `clients/<ClientName>/TAM.md` or `TAM.md` in current directory.

Structure: Executive Summary → Market Segmentation → Segment-by-Segment TAM → TAM/SAM/SOM Summary → Priority Ranking → Pipeline Model → Trigger Calendar → Next Steps

---

## Terminal Output

```
=== MARKET SIZING: TAM/SAM/SOM ===

Company: [name]

Market Segments: [count]
  [Segment 1]: [TAM value]
  [Segment 2]: [TAM value]
  [Segment 3]: [TAM value]

Combined TAM:  [value]/year
SAM:           [value]/year  ([X]% of TAM)
SOM Year 1:    [value]  (conservative)
SOM Year 1:    [value]  (optimistic)

Priority Attack:
  Tier 1: [segment name] — [volume] accounts — avg. deal [value]
  Tier 2: [segment name] — [volume] accounts — avg. deal [value]

12-month pipeline (conservative): [value]

TAM saved to: TAM.md

Next: /market competitors → map competitive landscape
      /market positioning → build differentiation from ICP + TAM + competitors
```

---

## Quality Standards

- **Bottom-up over top-down** — calculate from number of companies × deal value, not from percentage of a global market report
- **Source your numbers** — note when data is from an industry body, government stat, or estimated
- **Flag uncertainty** — "estimated" vs. "verified" on every key number
- **Pipeline model must use real conversion rates** — not optimistic defaults; use benchmarks from the ICP's sales cycle and outreach channel
- **Trigger calendar is required** for event-driven businesses — it's the highest-ROI section

---

## Cross-Skill Integration

- Reads: `ICP.md` (required), `STRATEGY.md` (required), `COMPETITOR-REPORT.md` (optional)
- Outputs feed: `/market abm` (segment and tier definitions), `/market positioning` (market size context)
- After completion, suggest: `/market competitors` if not yet run, then `/market positioning`
