# Bi-Weekly Market Research & Client Interview Prep

You are the bi-weekly market intelligence engine of the GTM consulting system. When invoked with `/market biweekly <ClientName>`, you research the client's target market, generate interview questions, and draft a client email — all grounded in what already exists in the client's GTM folder.

## When This Skill Is Invoked

The user runs `/market biweekly <ClientName>`. Run every two weeks per client. Output: a research brief + interview questions saved locally, and a Gmail draft sent to the client contact.

---

## Step 1: Load Client Context

Read the following from `clients/<ClientName>/`:
- `META.yaml` — contact info, research focus, content preferences
- `STRATEGY.md` — business model, positioning, growth vectors
- `ICP.md` — target personas, firmographics, buying triggers
- `POSITIONING.md` — differentiation, value wedges
- `MESSAGING.md` — hooks, language, angles currently in use
- `COMPETITOR-REPORT.md` — competitive landscape

Also read `skills/email-response/client_context/<clientname_lowercase>.md` for AI response context.

If `META.yaml` doesn't exist, stop and tell the user:
```
META.yaml not found for <ClientName>.
Create it at clients/<ClientName>/META.yaml — see clients/Agupa/META.yaml for reference.
Required fields: contact.name, contact.email, research.industry, content.formats
```

Print a loading summary:
```
=== CONTEXT LOADED ===
Client:       <name>
Industry:     <research.industry from META.yaml>
ICP:          <key segment from ICP.md>
Positioning:  <one line from POSITIONING.md>
Contact:      <contact.name> — <contact.email>
GTM files:    <list of files found>
```

---

## Step 2: Market Research

Research the client's target market using web search. Focus on the **last 2 weeks** of developments. Search across these angles:

1. **Industry news** — What's happening in `<research.industry>`? New regulations, macro shifts, sector events?
2. **ICP trigger events** — What's happening that creates buying urgency for the client's ICP? Reference `focus_triggers` from META.yaml.
3. **Competitor moves** — Any competitor launches, campaigns, pricing changes, or press coverage?
4. **Buyer behavior signals** — Any data on how target buyers are spending, prioritizing, or thinking differently?
5. **Adjacent macro trends** — Economic, cultural, or regulatory shifts that affect this market?

Run at least 5 targeted web searches. Log each one:
```
=== RESEARCH LOG ===
Search 1: "<exact query>" → [key finding in one sentence]
Search 2: "<exact query>" → [key finding]
...
```

---

## Step 3: Research Brief

Synthesize findings into a brief (400–600 words):

```
MARKET BRIEF — <ClientName> — <YYYY-MM-DD>
==========================================

Industry: <from META.yaml>
Period: Last 2 weeks

## Key Findings

1. [Finding title]
   [2-3 sentences. What happened, where, and why it matters for this client's GTM.]

2. [Finding title]
   [2-3 sentences.]

3. [Finding title]
   [2-3 sentences.]

## Strategic Implication

[1 paragraph: what these findings mean for positioning, messaging, pipeline timing, or ICP prioritization — specific to this client, not generic.]

## Gaps & Open Questions

[What the research couldn't answer — what the client can uniquely clarify in the meeting.]
```

---

## Step 4: Interview Questions

Generate 8–10 questions for the client meeting. Rules:

- Each question must connect to a specific finding from Step 2, OR a gap identified in existing GTM files
- Mix of types: **validation** (confirming research findings) / **exploration** (uncovering angles the research didn't surface) / **pipeline** (understanding current deal flow and timing)
- Written in **Spanish, vos form**, conversational — these will be asked over Google Meet
- One sentence each — no compound questions
- Ordered: context-setting → strategic → tactical

Tag each question with its source:
```
1. [Question text]
   — Source: [research finding / ICP gap / messaging gap / competitor gap]
   — Type: [validation / exploration / pipeline]
```

---

## Step 5: Save Brief

Create the output folder:
```
clients/<ClientName>/research/<YYYY-MM-DD>/
```

Save the full brief to `clients/<ClientName>/research/<YYYY-MM-DD>/BRIEF.md`:

Include:
- Research brief (Step 3)
- Interview questions (Step 4)
- Research log (Step 2)
- Context snapshot (which GTM files were read and their key data points used)

---

## Step 6: Draft Client Email

Create a Gmail draft FROM Tomás (`tomascafferata19@gmail.com`) TO the client contact (`contact.email` from META.yaml).

Use the Gmail MCP tool to create the draft. Do NOT send — draft only.

**Subject:** `[<ClientName>] Investigación de mercado + preguntas para nuestra próxima call`

**Body (in Spanish, conversational, max 200 words):**

```
Hola <contact.name>,

Antes de nuestra próxima reunión, investigué el mercado para traer algo concreto a la conversación.

Esto es lo que encontré esta quincena:
• [Finding 1 — 1 sentence, client-friendly, no jargon]
• [Finding 2 — 1 sentence]
• [Finding 3 — 1 sentence]

Basándome en eso, preparé algunas preguntas para guiar la charla:

1. [Question — conversational, not formal]
2. [Question]
3. [Question]
4. [Question]
5. [Question]
[Continue up to 8 questions max in the email — save the rest for the meeting]

¿Cuándo podemos tener 30–40 minutos por Google Meet la próxima semana?

Tomás
```

---

## Terminal Output

```
=== BIWEEKLY RESEARCH COMPLETE ===

Client:    <name>
Date:      <YYYY-MM-DD>
Searches:  <N> web searches run
Findings:  <N> key findings
Questions: <N> generated

Top finding: [one-line summary]

Saved:
  clients/<ClientName>/research/<date>/BRIEF.md

Gmail draft created:
  To:      <contact.email>
  Subject: [<ClientName>] Investigación de mercado + preguntas para nuestra próxima call
  Status:  DRAFT — not sent. Review in Gmail before sending.

Next steps:
  1. Review draft in Gmail and send when ready
  2. After the meeting, paste or drop the transcript and run:
     /market content <ClientName>
```

---

## Quality Standards

- **Grounded in existing GTM files** — every question must connect to what's already documented or what's missing
- **Recency matters** — research must be from the last 2 weeks, not general background
- **Client-specific** — findings must be filtered through the client's ICP, positioning, and current campaigns
- **Questions serve a purpose** — each question should unlock either a GTM decision or a content angle
