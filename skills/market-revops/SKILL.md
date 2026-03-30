# Revenue Operations Setup

You are the RevOps engine of the GTM outbound stack. When invoked with `/market revops`, you design the operational infrastructure that connects outbound marketing to sales: lead lifecycle stages, scoring model, CRM setup, pipeline configuration, and handoff processes. The output is a ready-to-implement RevOps blueprint.

## When This Skill Is Invoked

The user runs `/market revops`. This is an optional deliverable skill — run after the core GTM pipeline (Steps 1-8) when the client needs to operationalize the outbound system in a CRM. Required inputs: ICP.md + ABM.md.

---

## Inputs

Read the following files from `clients/<ClientName>/`:
- `ICP.md` — **required** (account tiers, scoring rubric, buyer personas)
- `ABM.md` — **required** (account tiers, sequence assignments, metrics targets)
- `MESSAGING.md` — optional (sequence names for pipeline stage mapping)
- `STRATEGY.md` — optional (business model, deal size, sales cycle length)

Ask the user:
1. Current CRM (HubSpot / Pipedrive / Salesforce / none / other)
2. GTM motion: founder-led sales, SDR team, or hybrid
3. Average deal size and estimated sales cycle length
4. Current biggest operational pain (leads getting lost, no follow-up, no visibility)

---

## Phase 1: Lead Lifecycle Definition

Define every stage a lead passes through from first contact to closed deal:

```
LEAD LIFECYCLE STAGES
======================

STAGE               DEFINITION                          ENTRY CRITERIA              EXIT CRITERIA
────────────────────────────────────────────────────────────────────────────────────────────────────
Prospect            In list, not yet contacted          Added to sequence           Email 1 sent
Contacted           Sequence active                     Email 1 sent                Reply received OR
                                                                                    sequence complete
Engaged             Replied (any reply)                 Reply received              Meeting booked OR
                                                                                    disqualified
Meeting Booked      Discovery call scheduled            Calendar invite sent        Meeting held
Discovery Done      Call completed, notes taken         Meeting held                Qualified OR
                                                                                    disqualified
Proposal Sent       Formal quote or proposal delivered  Proposal/quote sent         Decision received
Negotiation         Active back-and-forth on terms      Prospect requested changes  Won OR lost
Closed Won          Deal signed / first invoice sent    PO or agreement received    —
Closed Lost         Deal explicitly lost                Prospect said no            —
Nurture             Not ready now, re-engage later      No urgency, future trigger  Trigger appears →
                                                                                    re-enter at Prospect

DISQUALIFIED:       Negative ICP, wrong persona, no budget, competitor locked in
UNRESPONSIVE:       Completed full sequence, zero engagement — move to Nurture, not Lost
```

---

## Phase 2: Lead Scoring Model

Translate the ICP scoring rubric (from ICP.md) into CRM-ready point values:

```
LEAD SCORING MODEL
==================

FIRMOGRAPHIC FIT (40 points max)
  Industry match
    Exact primary vertical:          20 pts
    Adjacent/secondary vertical:     10 pts
    Wrong vertical:                   0 pts

  Company size match
    Exact ICP range:                 20 pts
    Close but slightly off:          10 pts
    Outside range:                    0 pts

SITUATIONAL FIT (35 points max)
  Pain signal present (LinkedIn/web activity showing events/fleet/signage):
    Strong signal (posted about trigger):  15 pts
    Weak signal (industry presence):        8 pts
    No signal:                              0 pts

  Trigger event identified:
    Active trigger with date:          20 pts
    Trigger likely but unconfirmed:    10 pts
    No trigger found:                   0 pts

PERSONA FIT (25 points max)
  Title match:
    Champion (Marketing Manager / Events Coord.):  25 pts
    Economic buyer without champion identified:     10 pts
    Wrong department:                               0 pts

SCORE TIERS:
  80-100:  Tier 1 — Personalized outreach, immediate priority
  60-79:   Tier 2 — Semi-personalized sequence
  40-59:   Tier 3 — Batch outreach
  <40:     Disqualify — do not contact

AUTOMATIC DISQUALIFIERS (override score → 0):
  - Fewer than 10 employees
  - Government/public sector
  - Pure digital business (no physical presence)
  - Already closed/lost in past 6 months
```

---

## Phase 3: CRM Configuration

Provide setup instructions for the client's CRM:

### HubSpot (Free/Starter)

```
HUBSPOT SETUP
=============

PIPELINE: "Outbound GTM"
  Stages: [map from lifecycle stages above]
  Required fields at each stage: [list what must be filled to advance]

CONTACT PROPERTIES TO ADD:
  ICP Score (number, 0-100)
  ICP Tier (dropdown: T1 / T2 / T3 / Disqualified)
  Trigger Type (dropdown: Feria / Flota / Apertura / Rebrand / Nuevo MKT / Nurture)
  Trigger Detail (text: e.g., "Expo Rural Julio 2026")
  Trigger Date (date)
  Sequence Assigned (dropdown: [list from ABM.md])
  Sequence Step (number)
  Last Contact Date (date — auto-populated by email integration)
  Meeting Booked (date)

COMPANY PROPERTIES TO ADD:
  LinkedIn URL (URL)
  ICP Score (number)
  ICP Tier (dropdown)
  Active Trigger (yes/no)
  Fleet Size (number) — if fleet segment
  Events Per Year (number) — if events segment

VIEWS TO CREATE:
  "Tier 1 — Ready to Contact": ICP Tier = T1, Stage = Prospect
  "Active Sequences": Stage = Contacted, Last Contact = last 14 days
  "Meetings This Week": Stage = Meeting Booked, date = this week
  "Nurture — Next Trigger": Stage = Nurture, Trigger Date = next 90 days
  "Stuck — No Movement": Stage = Discovery Done, no activity in 7 days

AUTOMATIONS TO SET UP:
  → When email replied: move to "Engaged"
  → When meeting booked: move to "Meeting Booked", notify owner
  → When sequence complete, no reply: move to "Nurture"
  → When trigger date is 90 days out: re-activate from Nurture to Prospect
```

### Pipedrive

```
PIPEDRIVE SETUP
===============

PIPELINE: "Outbound GTM"
  Stages: [same stage names as above]

CUSTOM FIELDS (Deals):
  ICP Score, ICP Tier, Trigger Type, Trigger Detail, Trigger Date, Sequence Assigned

FILTERS:
  "Hot Accounts": ICP Score > 80, Stage = Prospect
  "Meetings This Week": Stage = Meeting Booked, Close Date = this week
  "Nurture Pool": Stage = Nurture

ACTIVITIES:
  Create activity templates for each sequence step:
  "Email 1 — FERIAS-T1", "LinkedIn Connect", "Email 2 — Social Proof", etc.
```

---

## Phase 4: Handoff Processes

Define how leads move between stages and between people:

```
HANDOFF PROCESSES
=================

SEQUENCE → MEETING BOOKED
  Trigger: Prospect replies with interest or books directly
  Action:  Remove from sequence in Instantly immediately
           Move to "Engaged" in CRM
           Assign to [founder / AE] within [X] hours
  SLA:     Reply within 4 hours during business hours
  Template: [First reply template — warm, specific, confirms meeting]

MEETING BOOKED → DISCOVERY DONE
  Trigger: Meeting held
  Action:  Fill discovery notes in CRM (template below)
           Score: qualified / unqualified / nurture
           If qualified: move to "Proposal Sent" within [X] days
  Required fields: Pain stated, trigger confirmed, decision maker identified,
                   budget signal, timeline, next step agreed

DISCOVERY NOTES TEMPLATE:
  Pain: [What they said in their words]
  Trigger: [Specific event — name, date]
  Current solution: [What they're using now]
  Decision process: [Who else is involved]
  Budget signal: [Pre-approved / discretionary / needs CFO approval]
  Timeline: [When they need to decide]
  Entry offer response: [Interested / needs more info / not ready]
  Next step: [Specific action + date]

CLOSED LOST → NURTURE
  Trigger: Prospect says no / not now
  Action:  Tag reason (price / timing / competitor / wrong fit)
           Set follow-up date based on trigger calendar:
           If "not now — next feria": set reminder for 90 days before next event
           If "wrong timing": set reminder for 6 months
           If "competitor locked in": set reminder for 12 months
```

---

## Phase 5: Metrics Dashboard

Define the weekly metrics to track:

```
REVOPS METRICS DASHBOARD
==========================

WEEKLY ACTIVITY METRICS
  New Tier 1 accounts added:          _____  (target: [N]/week)
  Emails sent:                        _____  (target: [N]/week)
  LinkedIn connections sent:          _____  (target: [N]/week)
  Replies received:                   _____
  Meetings booked:                    _____

CONVERSION METRICS (review monthly)
  Prospect → Engaged rate:            _____%  (target: >[X]%)
  Engaged → Meeting rate:             _____%  (target: >[X]%)
  Meeting → Proposal rate:            _____%  (target: >[X]%)
  Proposal → Won rate:                _____%  (target: >[X]%)
  Full funnel: Prospect → Won:        _____%

PIPELINE HEALTH
  Active Tier 1 accounts:             _____
  Meetings held this month:           _____
  Open proposals:                     _____  total value: $______
  Deals closed this month:            _____  revenue: $______
  Nurture pool size:                  _____  (leads to re-activate)

SEQUENCE PERFORMANCE (review weekly in Instantly)
  Best performing sequence:           [name] — [reply rate]%
  Worst performing sequence:          [name] — [reply rate]%
  Subject line A/B winner this week:  [subject]

SPEED METRICS
  Average time to first reply:        [hours] (target: <4h business hours)
  Average sequence → meeting days:    [days]
  Average meeting → proposal days:    [days]
  Average proposal → close days:      [days]
```

---

## Output Format: REVOPS.md

Save to `clients/<ClientName>/REVOPS.md`.

Structure: Lead Lifecycle Stages → Scoring Model → CRM Configuration → Handoff Processes → Metrics Dashboard → Implementation Checklist

---

## Terminal Output

```
=== REVENUE OPERATIONS BLUEPRINT ===

Client: [name]
CRM: [platform]

Lifecycle stages defined: [count]
Scoring model: [N] factors, [N] point tiers
Pipeline: [N] stages configured

Handoff SLAs:
  Sequence → Meeting reply: [X] hours
  Meeting → Proposal: [X] days
  Proposal → Decision: [X] days

Key automations: [count] defined
Dashboard metrics: [count] KPIs

RevOps blueprint saved to: REVOPS.md

Implementation checklist:
  [ ] CRM pipeline created
  [ ] Custom fields added
  [ ] Views/filters configured
  [ ] Automations set up
  [ ] Instantly integrated with CRM
  [ ] Team trained on handoff process
```

---

## Cross-Skill Integration

- Reads: `ICP.md`, `ABM.md`, `MESSAGING.md`, `STRATEGY.md`
- Operationalizes: the account tiers and sequence structure from `ABM.md` into CRM stages
- Run after: `market-abm` and `market-emails` (need sequences defined before building CRM around them)
- Complements: `market-enablement` (enablement covers the meeting; revops covers everything around it)
