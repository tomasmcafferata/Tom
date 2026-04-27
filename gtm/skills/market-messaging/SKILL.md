# Messaging Architecture

You are the messaging engine of the GTM stack. When invoked with `/market messaging`, you build a complete, ready-to-use messaging system: value propositions by segment, hooks by trigger, persona-specific angles, follow-up sequences, call scripts, LinkedIn library, and objection handling. The output is a copywriting reference that feeds directly into email sequences, LinkedIn outreach, and sales scripts.

## When This Skill Is Invoked

The user runs `/market messaging`. This is Step 6 of the GTM pipeline. Required inputs: POSITIONING.md + ICP.md. Reads existing content from the company's website to iterate on real copy.

---

## Inputs

Read the following files:
- `POSITIONING.md` — **required** (core differentiator, language guide, wedges per segment)
- `ICP.md` — **required** (buyer personas, pain points, buying triggers, desired state)
- `STRATEGY.md` — required (brand voice, tone, language to use/avoid)
- `COMPETITOR-REPORT.md` — optional (competitive context for objection handling)

Additionally, if the company URL is available, fetch the current website copy to:
- Identify existing messages worth keeping
- Flag commoditized language to replace
- Find real customer language to mirror

---

## Core Messaging Principles

Before writing any copy, establish the rules of the voice:

```
MESSAGING RULES
===============

COPY QUALITY STANDARDS (from conversion copywriting)
  Clarity over cleverness — if it sounds smart but unclear, rewrite it plainly.
  Benefits over features — "el stand llega armado" > "instalación incluida".
  Specificity over vagueness — "coordinás 4 proveedores" > "proceso complejo".
  Customer language over vendor language — use the words buyers use, not yours.
  Active voice — "NDC produce e instala" > "la producción e instalación es realizada".
  Cut qualifiers — eliminate "casi", "bastante", "muy" — they weaken every claim.
  Show outcomes, don't state them — "el stand se veía exactamente como el render"
    > "entregamos calidad garantizada".

OUTBOUND RULES
  1. Never open with the company. Open with the prospect's pain or world.
  2. Never use generic quality claims without anchoring to a specific outcome.
  3. Flag and eliminate commoditized phrases — replace with differentiating language.
  4. Every message has one goal: get a response. Not sell. Not explain. Get a reply.
  5. Tone: [direct / warm / peer-to-peer] — match to the ICP's communication style.
  6. Formality: [vos/tú/usted — or English equivalent] — match to target market norms.
  7. Each follow-up adds new value. Never "just checking in."

PSYCHOLOGY PRINCIPLES TO APPLY
  Social proof:   People do what peers do — use client types, not just claims.
  Specificity:    Specific numbers are more believable than round numbers.
                  "4 proveedores" > "varios proveedores".
  Loss aversion:  "El stand que llega incompleto el día antes" >
                  "mejores resultados en tu próximo evento".
  Trigger timing: A message arriving at the right moment (trigger) is 10x more
                  effective than the same message at the wrong moment.
  Reciprocity:    Lead with value (observation, insight, relevant info) before the ask.
```

---

## Phase 1: Value Propositions by Segment

Write a single crisp value proposition for each ICP segment and trigger type:

```
SEGMENT: [Name]
  One-liner: "[Specific outcome for this segment in one sentence]"
  Why it works: [What pain/desire it addresses, why the language lands]

[Repeat for each segment from ICP.md]

MASTER VALUE PROPOSITION (cross-segment):
  "[The shortest version that works across all segments]"
```

Each value proposition must:
- Start with a recognizable customer reality (not a company claim)
- Contain the structural differentiator
- Be under 25 words for the one-liner

---

## Phase 2: Hooks by Buying Trigger

For each buying trigger from ICP.md, write a specific hook:

```
TRIGGER: [Name — e.g., "Trade show registration confirmed"]
=============================================================

Context:    [When to use — what signal was observed and where]

Subject line options:
  A: "[Option A — specific, lower curiosity]"
  B: "[Option B — curiosity-driven]"
  C: "[Option C — direct question]"

Email opening (3 sentences max):
  "[Sentence 1: reference the trigger — shows you did your homework]
   [Sentence 2: state the pain this trigger activates]
   [Sentence 3: bridge to the value prop or CTA]"

LinkedIn connection note (max 300 characters):
  "[Short personalized note referencing the trigger]"

LinkedIn DM (post-connection):
  "[3–5 sentence message — trigger reference + pain + value prop + soft CTA]"
```

Produce hooks for every trigger identified in ICP.md (minimum 3–5 triggers).

---

## Phase 3: Persona-Specific Messaging

For each buyer persona from ICP.md:

```
PERSONA: [Name — Champion / Economic Buyer / etc.]
===================================================

Their world:       [2–3 sentences describing their daily reality]
What hurts:        [3–4 specific pain points — quote-style, their words]
What they want:    [The outcome they're reaching for — quote-style]

Primary message:   "[The hook that lands hardest for this persona]"
Secondary message: "[Backup angle if primary doesn't resonate]"

What to avoid:     [Specific pitfalls for this persona]
```

---

## Phase 4: Follow-Up Sequence Logic

Write the logic and copy for a 4-step follow-up sequence:

```
FOLLOW-UP RULES
===============
- Each step must add value (insight, social proof, urgency, or practical info)
- Never repeat the same angle twice
- Never use "just following up" or "circling back"
- Step 4 is always a clean break — leave the door open, don't chase

STEP 1 (Day 1) — Primary hook:
  Angle: [Trigger + pain + value prop + soft CTA]
  Goal:  Response or meeting request

STEP 2 (Day 3–4) — Social proof or case study angle:
  Angle: [Reference a relevant result or before/after for a similar company]
  Goal:  Build credibility, re-engage

STEP 3 (Day 7–8) — Practical urgency:
  Angle: [A real deadline, production window, or timeline constraint]
  Goal:  Create movement without artificial pressure

STEP 4 (Day 12–14) — Soft close / breakup:
  Angle: "[Last message — acknowledge the timing may be wrong, leave door open]"
  Goal:  Final attempt + clean exit that makes re-engagement easy later

NURTURE (Day 30+) — Post-event or seasonal:
  Angle: [Check-in after the trigger event has passed — plant for next cycle]
  Goal:  Keep warm for next buying window
```

Write the full copy for each step, not just the angle.

---

## Phase 5: Call Scripts

### Cold open (30 seconds)

```
"[Greeting + name + company + one-line intro]
 [Reference to trigger or observed signal]
 [One-sentence value prop]
 [Permission question — 'Do you have 3 minutes, or should I call back tomorrow?']"
```

### Objection handling scripts

For each major objection from POSITIONING.md, write a word-for-word response:

```
OBJECTION: "[Exact phrasing of the objection]"
RESPONSE:
  "[Acknowledge + bridge + reframe in 2–4 sentences]
   Closing question: '[Question that advances the conversation]'"
```

---

## Phase 6: LinkedIn Message Library

Build a reusable library organized by scenario:

```
CONNECTION NOTES (max 300 characters each)
  Trigger A — [scenario]: "[copy]"
  Trigger B — [scenario]: "[copy]"
  Trigger C — [scenario]: "[copy]"
  Generic (no trigger): "[copy]"

DMs POST-CONNECTION
  DM 1 — [scenario]: "[full copy]"
  DM 2 — follow-up if no reply: "[full copy]"
  DM 3 — soft close: "[full copy]"
```

---

## Phase 7: Segment Naming for Sequences

Define the sequence names to use in Instantly/Smartlead/Lemlist:

```
SEQUENCE NAMING
===============
SEGMENT          TRIGGER              TONE          HOOK
──────────────────────────────────────────────────────────────
[SEG-1]          [Trigger type]       [Tone]        "[Hook one-liner]"
[SEG-2]          [Trigger type]       [Tone]        "[Hook one-liner]"
[SEG-3]          [Trigger type]       [Tone]        "[Hook one-liner]"
NURTURE          Post-event           [Tone]        "[Hook one-liner]"
```

---

## Output Format: MESSAGING.md

Save to `clients/<ClientName>/MESSAGING.md` or `MESSAGING.md` in current directory.

Structure: Core Principles → Value Props by Segment → Hooks by Trigger → Persona Messaging → Follow-Up Sequence Logic + Copy → Call Scripts → LinkedIn Library → Sequence Naming → Next Steps

---

## Terminal Output

```
=== MESSAGING ARCHITECTURE ===

Company: [name]

Value propositions: [count] (by segment)
Trigger hooks: [count] (by trigger type)
Personas covered: [count]
Follow-up steps: [count]
LinkedIn messages: [count]

Primary hook: "[best performing hook based on trigger analysis]"
Recommended first sequence: [sequence name]

Messaging saved to: MESSAGING.md

Next: /market abm → build account list and engagement playbook
      /market emails → generate ready-to-load email sequences
```

---

## Quality Standards

- **Every hook must reference a specific trigger** — generic "I'd love to connect" copy is not acceptable
- **Follow-ups must have fresh angles** — no recycling of step 1 copy with different subject lines
- **Call scripts must be natural** — read them aloud; if they sound robotic, rewrite
- **LinkedIn notes must fit in 300 characters** — count and enforce this limit
- **Value props must be tested against the ICP pain** — does this message address something the champion actually worries about?
- **Quote the ICP's language** — use words and phrases from the persona descriptions, not marketing language

---

## Cross-Skill Integration

- Reads: `POSITIONING.md`, `ICP.md`, `STRATEGY.md`
- Optionally scans: company website copy (via WebFetch) to iterate existing language
- Outputs feed: `/market abm` (hooks per account tier), `/market emails` (primary input for sequence copy)
- After completion, suggest: `/market abm` for account-level playbook, `/market emails` for ready-to-send sequences
