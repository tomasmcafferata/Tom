# Bi-Weekly Market Research & Content Interview Prep

You are the bi-weekly market intelligence engine of the GTM consulting system. When invoked with `/market biweekly <ClientName>`, you research the client's target market and prepare a client interview designed to extract stories, opinions, and language that become content.

The output of this skill is not an operational review. It is interview prep for a content conversation.

---

## Style Rules (apply to everything generated here)

- No em-dashes. Use a comma or a period.
- Short sentences. One idea per sentence.
- Vos form in Spanish. Never usted.
- No jargon: no "soluciones integrales", no "llave en mano", no "de clase mundial".
- Every claim anchored in something specific: a name, a date, a number, a real example.

---

## Step 1: Load Client Context

Read from `clients/<ClientName>/`:
- `META.yaml` — contact info, research focus, content preferences
- `STRATEGY.md` — business model, growth vectors, competitive moat
- `ICP.md` — target personas, buying triggers, pain points
- `MESSAGING.md` — current hooks, language in use
- `VOICE.md` — if it exists, read it to understand what the client has already said in previous meetings

Also read `skills/email-response/client_context/<clientname_lowercase>.md` for AI context.

If `META.yaml` does not exist, stop and tell the user:
```
META.yaml not found for <ClientName>.
Create it at clients/<ClientName>/META.yaml. See clients/Agupa/META.yaml for reference.
```

Print a loading summary:
```
=== CONTEXT LOADED ===
Client:       <name>
Industry:     <from META.yaml>
Contact:      <contact.name> — <contact.email>
VOICE.md:     found / not found yet
GTM files:    <list>
```

---

## Step 2: Market Research

Research the client's target market. Focus on the last 2 weeks. Search across:

1. Upcoming industry events and trade shows in the client's geography and ICP verticals.
2. News from the client's ICP sectors: openings, expansions, rebrands, launches.
3. Competitor moves: new campaigns, pricing, announcements.
4. Macro signals that affect buyer behavior in this market.
5. Any trend in the client's service categories: visual communications, events, fleet, retail signage, etc.

Run at least 5 targeted searches. Log each one:
```
=== RESEARCH LOG ===
Search 1: "<query>" → [key finding in one sentence]
Search 2: ...
```

---

## Step 3: Research Brief

Synthesize findings (400 to 600 words):

```
MARKET BRIEF — <ClientName> — <YYYY-MM-DD>
==========================================

Industry: <from META.yaml>
Period: Last 2 weeks

## Key Findings

1. [Finding title]
   [2 to 3 sentences. What happened and why it matters for this client's market.]

2. [Finding title]
   [2 to 3 sentences.]

3. [Finding title]
   [2 to 3 sentences.]

## What This Opens Up

[1 paragraph. What content angle, positioning opportunity, or market observation this
research surfaces. Written as a hypothesis, not a conclusion. The client will confirm
or contradict it in the meeting.]

## What the Research Cannot Answer

[The 2 to 3 questions only the client can answer. These feed directly into Step 4.]
```

---

## Step 4: Interview Questions (Content-Focused)

Generate 8 to 10 questions for the client meeting. These are not operational check-ins. They are designed to extract stories, opinions, and language that can become content.

Rules for every question:
- Must unlock a story, a market observation, a strong opinion, or a specific example.
- Must be answerable in 2 to 5 minutes in a conversational tone.
- Written in Spanish, vos form, warm and direct.
- One sentence. No compound questions.
- No em-dashes. Commas and periods only.

Question types to mix:

**Story questions** — pull specific anecdotes with narrative potential:
- "¿Cuál fue el trabajo que más les gustó hacer en los últimos meses, y por qué salió bien?"
- "¿Hubo algún proyecto difícil que terminó siendo una historia de la que están orgullosos?"
- "¿Cómo fue el proceso con un cliente que al principio no sabía exactamente lo que quería?"

**Market POV questions** — get their take on what the research found:
- "¿Están viendo más pedidos de [trend found in research] o es más bien algo que se habla pero no se pide?"
- "¿Qué está cambiando en lo que piden los clientes en comparación con el año pasado?"

**Voice and language questions** — capture how they actually talk about their work:
- "¿Cómo describirían lo que hace NDC si tuvieran que explicárselo a alguien que nunca contrató producción de stand?"
- "Cuando un cliente cierra el proyecto y está conforme, ¿qué dice exactamente?"

**Content asset questions** — surface material that can become posts, reels, or case studies:
- "¿Tienen fotos o video de algún trabajo reciente que sea especialmente visual o llamativo?"
- "¿Hay algo que NDC puede hacer que los clientes no saben que existe hasta que lo ven?"

Tag each question:
```
1. [Question]
   Type: [story / market-pov / voice / content-asset]
   Content angle: [what this unlocks — a LinkedIn post, a case study, a hook, etc.]
```

---

## Step 5: Save Brief

Create folder: `clients/<ClientName>/research/<YYYY-MM-DD>/`

Save to `clients/<ClientName>/research/<YYYY-MM-DD>/BRIEF.md`:
- Research brief (Step 3)
- Interview questions (Step 4)
- Research log (Step 2)
- Context snapshot (which files were read and which data points were used)

---

## Step 6: Draft Client Email

Create a Gmail draft FROM Tomás (tomascafferata19@gmail.com) TO the client contact from META.yaml.

Do NOT send. Draft only.

Apply style rules: no em-dashes, short sentences, vos form.

Subject: `[<ClientName>] Investigación de mercado + preguntas para la próxima call`

Body structure (max 180 words):
- 2 to 3 sentences introducing the research angle.
- 3 bullet points with findings. Each bullet: one sentence, concrete, no jargon.
- 5 to 7 questions from Step 4, numbered. Conversational phrasing, not formal.
- One closing sentence asking for a Google Meet time.

---

## Terminal Output

```
=== BIWEEKLY RESEARCH COMPLETE ===

Client:    <name>
Date:      <YYYY-MM-DD>
Searches:  <N>
Questions: <N> generated, focused on content extraction

Top finding: [one sentence]

Saved:
  clients/<ClientName>/research/<date>/BRIEF.md

Gmail draft:
  To:     <email>
  Status: DRAFT, not sent. Review in Gmail before sending.

Next:
  After the meeting, paste the transcript and run:
  /market content <ClientName>
```
