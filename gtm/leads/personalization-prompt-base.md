# Personalization Prompt — Base (the "words", pasted into Clay)

The GPT column in Clay that writes the per-lead **personalization line** (level B) — or,
extended, the full body (level C). Decided: Clay generates the words; this file is the
**version-controlled source of truth** you paste in. Same split as the research agent: the
base prompt never changes; the per-**campaign** brief is the variable.

How it's used in Clay:
1. Enrichment columns already exist in the table (`activity_description`, `triggers_found`,
   `icp_signals`, `company_intel`).
2. The client picked a campaign from the ideation menu → paste that idea's
   **angle + offer + hook + proof + language** into the `campaign_brief` variable.
3. The GPT column writes `ai_first_line` per lead. The CSV builder carries it to Instantly
   as the `{{ai_first_line}}` custom variable.

---

## Prompt B — column `ai_first_line` (the personalized opener — identical prompt, brief is the variable)

```
ROL: Escribís la PRIMERA LÍNEA personalizada de un cold email B2B — la que un colega
inteligente escribiría tras notar algo real de la empresa, no un vendedor.

INPUT:
  first_name:      {{first_name}}
  company:         {{company}}
  activity:        {{activity_description}}
  triggers_found:  {{triggers_found}}
  icp_signals:     {{icp_signals}}
  company_intel:   {{company_intel}}
  campaign_brief:  {{campaign_brief}}   # ángulo + oferta + hook + prueba + lenguaje a usar/evitar

REGLAS:
- 1–2 oraciones. Abrí con el mundo del prospecto o el trigger — NUNCA con tu nombre, tu
  empresa, ni "Espero que estés bien".
- Específico: si sacás el dato de la empresa/trigger, la línea NO debería seguir teniendo
  sentido (test de despersonalización).
- Usá SOLO datos presentes en el input. Si no hay un dato concreto, caé a una línea de
  nivel industria (sin inventar) y marcá personalization_level = "low".
- "vos". Sin jerga de ventas ("soluciones integrales", "líderes", "sinergia"). Sin superlativos.
- Respetá el lenguaje a evitar del brief. NO pitchees en la primera línea: preparás el terreno.
- La línea conecta con el ángulo del campaign_brief, sin cerrarlo.

Devolvé SOLO este JSON:
{
  "ai_first_line": "",
  "personalization_level": "",   // high = usó trigger/dato puntual · low = línea de industria
  "personalization_basis": ""    // qué dato concreto usaste — para verificar que no alucinó
}
```

---

## Level C (full body) — extension, same pattern

For small, high-fit cohorts only. One prompt per sequence step writes the whole email from
`campaign_brief` + the step's framework + the lead facts. The base rules above still apply
(máx 5 oraciones, un solo CTA, follow-ups con ángulo nuevo — ver `skills/market-emails`
REGLAS DE ORO). Output a body column per step (`ai_body_step1`…). The CSV builder carries
these through as variables the same way — it does not care how the columns were filled.

---

## Verify

Spot-check `ai_first_line` against `personalization_basis` and `company_intel`: ¿la línea es
verdadera y está apoyada en un dato real? `personalization_level = low` marca los leads que
deberían ir a un trato más template (o salir de una campaña de alta personalización).
