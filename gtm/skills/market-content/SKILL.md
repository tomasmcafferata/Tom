# Post-Meeting Content Generation

You are the content generation engine of the GTM bi-weekly cycle. When invoked with `/market content <ClientName>`, you combine the pre-meeting research brief with the client meeting transcript to generate content and flag GTM updates.

## When This Skill Is Invoked

After the bi-weekly Google Meet. The user runs `/market content <ClientName>` and provides the transcript — either pasted directly in the session or as a file path.

---

## Step 1: Load Inputs

1. Find the most recent research brief: `clients/<ClientName>/research/*/BRIEF.md` (sort by date, take the latest)
2. Read `clients/<ClientName>/META.yaml` for content format preferences and language
3. Read the existing GTM files that may need updating: `MESSAGING.md`, `ICP.md`, `POSITIONING.md`
4. Load the transcript:
   - If the user pasted text in the session: use it directly
   - If the user provided a file path: read the file

If no BRIEF.md exists, stop:
```
No research brief found for <ClientName>.
Run /market biweekly <ClientName> first to generate the pre-meeting research.
```

If no transcript was provided, ask:
```
No transcript found. Paste it directly in the chat or provide a file path:
  clients/<ClientName>/research/<date>/TRANSCRIPT.md
```

Print what you loaded:
```
=== INPUTS LOADED ===
Client:         <name>
Brief:          clients/<ClientName>/research/<date>/BRIEF.md
Transcript:     [pasted / file: <path>]
Content formats: <from META.yaml or defaults>
Language:       <from META.yaml>
```

---

## Step 2: Extract Client Insights from Transcript

Analyze the transcript systematically:

```
TRANSCRIPT ANALYSIS
===================

Confirmed findings (from research brief):
  ✓ [Finding from brief] — confirmed / partially confirmed / contradicted
     Evidence: "[quote or paraphrase from transcript]"

New information (not in the brief):
  + [Insight 1] — [GTM implication]
  + [Insight 2] — [GTM implication]

Pain points mentioned by client:
  "[Direct quote or paraphrase]" — [Theme: ICP pain / competitive gap / timing issue]

Client's own language (phrases to reuse):
  "[Exact phrase used]" — [Where to use: messaging / email hooks / positioning]

Opportunities identified:
  [Opportunity] — [Evidence from transcript]

Unresolved questions or contradictions:
  [What the conversation raised but didn't answer]
```

---

## Step 3: Generate Content

Generate each format listed in `META.yaml content.formats`. Defaults if not specified:
- LinkedIn post
- Refined messaging hooks
- Updated GTM insight

---

### LinkedIn Post

- 150–250 words
- Written as **Tomás' POV** — GTM consultant sharing a market insight
- Hook: a sharp observation from the research or the conversation (not "I had a call with...")
- Body: what this means for GTM strategy in this space
- No confidential client details — generalize the insight to the market level
- End with a soft question or provocation to drive comments
- Language: per META.yaml (default: Spanish)

Format:
```
[Hook — 1 punchy line]

[Body — 3-5 short paragraphs or bullets]

[Closing question or take]

#hashtag1 #hashtag2 #hashtag3
```

---

### Refined Messaging Hooks

Based on: [research finding] + [language extracted from transcript]

Generate 2–3 variants for a new outbound email opening:

```
Variant 1:
  Subject:      [Subject line]
  Opening line: [First sentence of the email]
  Why it works: [1 sentence — which insight or buyer language it leverages]

Variant 2:
  Subject:      ...
  Opening line: ...
  Why it works: ...

Variant 3:
  ...
```

These should be ready to test against current sequences in the client's `EMAIL-SEQUENCES.md`.

---

### Updated GTM Insight (always generated)

Flag specific changes warranted to existing GTM files based on what was learned:

```
GTM UPDATE FLAGS
================

[File: MESSAGING.md]
  Section: [section name]
  Current: "[current content summary]"
  Suggested: "[updated content]"
  Reason: [transcript evidence]

[File: ICP.md]
  Section: [section name]
  Current: "[current content]"
  Suggested: "[update]"
  Reason: [transcript evidence]

[No changes needed to POSITIONING.md — findings confirm current positioning]
```

If changes are significant, suggest running the relevant pipeline step:
```
→ Apply with: /market messaging   (to regenerate full MESSAGING.md)
→ Apply with: /market icp         (to update ICP with new evidence)
```

---

## Step 4: Save Output

Save the full output to `clients/<ClientName>/research/<date>/CONTENT.md`:
- Transcript analysis (Step 2)
- All generated content pieces (Step 3)
- GTM update flags

Use the same `<date>` folder as the brief (the one loaded in Step 1).

If the transcript was pasted (not a file), also save it to:
`clients/<ClientName>/research/<date>/TRANSCRIPT.md`

---

## Terminal Output

```
=== CONTENT GENERATION COMPLETE ===

Client:      <name>
Brief date:  <date>

Transcript analysis:
  Confirmed findings: <N>
  New insights: <N>
  Client language captured: <N> phrases

Content generated:
  ✓ LinkedIn post (<N> words)
  ✓ Messaging hooks (<N> variants)
  ✓ GTM update flags: <N> changes across <N> files

Saved:
  clients/<ClientName>/research/<date>/CONTENT.md
  clients/<ClientName>/research/<date>/TRANSCRIPT.md  (if applicable)

Next steps:
  • Review LinkedIn post → publish when ready
  • Test messaging hooks in current Instantly sequence
  • Apply GTM updates with the commands listed above
  • Schedule next bi-weekly: /market biweekly <ClientName>
```

---

## Quality Standards

- **Quote the client** — use their exact words when they describe pains, wins, or priorities
- **Research + transcript together** — every content piece should synthesize both, not just one
- **Specificity over generality** — "HR leads in Argentine agro companies are prioritizing X" beats "companies are prioritizing culture"
- **Actionable GTM flags** — every suggested update must include evidence from the transcript
