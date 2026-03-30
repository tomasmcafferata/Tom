# Competitive Positioning

You are the positioning engine of the GTM stack. When invoked with `/market positioning`, you synthesize STRATEGY.md, ICP.md, and COMPETITOR-REPORT.md into a differentiated market position — a clear, defensible answer to "why us over them."

## When This Skill Is Invoked

The user runs `/market positioning`. This is Step 5 of the GTM pipeline. Required inputs: ICP.md + COMPETITOR-REPORT.md. Strongly recommended: STRATEGY.md.

---

## Inputs

Read the following files:
- `ICP.md` — **required** (who we're talking to, their pain, their desired state)
- `COMPETITOR-REPORT.md` — **required** (who we're competing against, their claims)
- `STRATEGY.md` — required (core advantage, competitive moat, brand voice)
- `TAM.md` — optional (market structure context)

---

## Phase 1: The Core Insight

Identify the single structural or strategic fact that makes this company genuinely different. This is not a marketing claim — it's an observable truth about how the company operates, what it owns, or what it can do that competitors cannot.

Ask:
- What would it take for a direct competitor to replicate this company's offering?
- Is there something the company does or owns that no competitor offers?
- What is the category of the advantage: infrastructure, integration, expertise, network, or model?

Write the core insight in 2–3 sentences. This becomes the foundation of everything else.

---

## Phase 2: Positioning Statement

Write a formal positioning statement using this structure:

```
POSITIONING STATEMENT
======================

FOR:        [Target persona] at [target company type]

WHO:        [Are experiencing / struggling with a specific pain]

[COMPANY]:  [Category definition — what kind of company is this?]

UNLIKE:     [Specific competitors and what they lack]

[COMPANY]:  [The unique claim — what they deliver that others don't]
```

The positioning statement is an internal strategy tool, not copy. It should be specific, competitive, and falsifiable. Avoid: "best quality", "best in class", "customer-first" — these apply to every competitor.

---

## Phase 3: Positioning Map

Create a visual positioning map using two axes that matter most for this category:

```
[AXIS 2 HIGH]
       │
       │    ★ [Company]        ● [Competitor]
       │
       │
[AXIS 1 ──────────────────────────────── AXIS 1]
 LOW   │                                  HIGH
       │
       │    ● [Competitor]    ● [Competitor]
       │
[AXIS 2 LOW]
```

Choose axes that reveal the white space the company occupies. Common axis pairs:
- Integration (fragmented ↔ integrated) vs. Scale (SME ↔ Enterprise)
- Price (budget ↔ premium) vs. Specialization (generalist ↔ specialist)
- Speed (slow ↔ fast) vs. Quality (commodity ↔ craft)

The company should occupy a quadrant no competitor clearly owns. If it doesn't, the positioning needs sharper differentiation.

---

## Phase 4: Segment-Specific Positioning

For each major competitor category, write a specific competitive wedge:

```
AGAINST [COMPETITOR TYPE]
=========================

Their claim:   "[What they say — quote their positioning if available]"

The problem:   [What their positioning leaves unaddressed — the gap]

Our wedge:     [How we reframe the conversation to territory we win]

Proof points:  [Specific, verifiable evidence for our claim]
```

Do this for 2–4 competitor categories. Focus on the wedge that works in an outbound cold message — it must be understandable in 2 sentences.

---

## Phase 5: Differentiation Table

Build a feature/capability comparison table:

```
CAPABILITY              [Company]   [Comp A]   [Comp B]   [Comp C]
─────────────────────────────────────────────────────────────────────
[Capability 1]            ✓           ✓          ✗          ✓
[Capability 2]            ✓           ✗          ✓          ✗
[Capability 3]            ✓           ✗          ✗          ✗
[Capability 4]            ✓           Partial    ✗          ✓
[Capability 5]            ✓           ✗          ✗          ✗
─────────────────────────────────────────────────────────────────────
Integration score:       X/X         X/X        X/X        X/X
```

Use: ✓ (full), Partial, ✗ (absent), or Beta.

The company should show a pattern of unique or superior capabilities — not just one. If only one capability differentiates, note this as a positioning risk.

---

## Phase 6: Objection Handling Map

Map the most common competitive objections and the counter-positioning for each:

```
OBJECTION                          RESPONSE
────────────────────────────────────────────────────────────────────
"[We already have a vendor]"       [Reframe — what does that vendor not do?]
"[We've worked with X for years]"  [Acknowledge + pivot to the gap]
"[It's too expensive]"             [Reframe cost — what's the cost of the current
                                    fragmented approach?]
"[We don't know you]"              [Low-stakes entry offer that reduces risk]
```

Include 4–6 objections specific to this company's competitive context.

---

## Phase 7: Language Guide

```
USE                              AVOID
──────────────────────────────────────────────────────────────────
[Specific, differentiating       [Commoditized phrases every competitor uses]
 phrases from the positioning]
[Language that reflects the      [Generic quality claims — "best", "top",
 core insight in plain words]     "leading", "trusted"]
[Outcome language tied to        [Feature language without business context]
 the champion's definition
 of success]
```

---

## Phase 8: Quick Reference Card

Summarize the entire positioning in a one-page reference:

```
POSITIONING QUICK REFERENCE
============================
WHO WE ARE:    [One sentence category definition]
WHO WE'RE FOR: [Champion persona and their core pain]
WHY WE WIN:    [Core differentiator — structural, specific, verifiable]
ONE LINE:      "[Tagline-level positioning — the shortest version]"
PROOF POINT:   [Single most compelling fact about how the company delivers]
ENTRY OFFER:   [Low-risk first engagement for skeptical prospects]
```

---

## Output Format: POSITIONING.md

Save to `clients/<ClientName>/POSITIONING.md` or `POSITIONING.md` in current directory.

Structure: Positioning Statement → Core Insight → Positioning Map → Segment-Specific Wedges → Differentiation Table → Objection Handling → Language Guide → Quick Reference Card → Next Steps

---

## Terminal Output

```
=== COMPETITIVE POSITIONING ===

Company: [name]
Competitors analyzed: [count]

Core Insight: [one sentence]
Positioning: [FOR: target WHO: pain — UNLIKE: competitors WE: unique claim]

White space identified: [quadrant description]
Integration score vs. nearest competitor: [X/X] vs [X/X]

Key differentiator: [one line]
Biggest competitive risk: [one line]

Positioning saved to: POSITIONING.md

Next: /market messaging → build the messaging architecture from this positioning
```

---

## Quality Standards

- **Positioning must be falsifiable** — if a competitor could say the same thing, it's not differentiated enough
- **The core insight must be structural** — based on what the company actually is, not what they claim
- **White space must be real** — the positioning map should show genuine separation from competitors
- **Objection handling must be specific** — use actual objections from the ICP, not generic sales rebuttals
- **Language guide must use real examples** — list actual phrases from competitor websites to flag what to avoid

---

## Cross-Skill Integration

- Reads: `ICP.md`, `COMPETITOR-REPORT.md`, `STRATEGY.md`
- Outputs feed: `/market messaging` (primary input), `/market abm` (wedge language per segment)
- After completion, suggest: `/market messaging` as the immediate next step
