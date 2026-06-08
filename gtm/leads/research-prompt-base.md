# Research Agent — Base Prompts (generic, shared across ALL clients & ICPs)

These are the two GPT prompts you paste into Clay. They **never change** between ICPs.
The only thing that changes per ICP is the **brief** (a value, not a prompt) — see
`clients/<client>/research-brief-<icp>.yaml`. That separation is what makes this
replicable: clone the Clay table, swap the brief, done.

This file is the version-controlled source of truth. Clay is just where it runs.

Build order in Clay (one table per ICP):
```
company_name, location, company_domain   (imported from the client Sheet)
        │
        ▼
[ Prompt A → column "dossier" ]   generic company profile (web/scrape + GPT)
        │
        ▼
[ Prompt B → column "icp_lens" ]  dossier + {{icp_brief}} → fit + triggers
        │
        ▼
filter icp_fit ∈ {strong, medium}  →  email waterfall (Clay credits, survivors only)
        │
        ▼
write back to the client Sheet by lead_id
```
> Pair Prompt A with Clay's website-scrape (or a web-enabled GPT) so the model has the
> page text. Use your OpenAI key in the Clay AI column, same as you do today.

---

## Prompt A — column `dossier` (generic profiler — identical in every table)

```
ROL: Sos un agente que analiza empresas y extrae un perfil operativo OBJETIVO a partir
de su presencia pública (sitio web + fuentes públicas).

INPUT:
  company_name:   {{company_name}}
  location:       {{location}}
  company_domain: {{company_domain}}   # puede venir vacío

REGLAS:
- Si no hay dominio, buscalo con company_name + location. La location orienta, no
  descalifica resultados válidos. Si no encontrás uno razonable, dejá company_domain vacío.
- Extraé info OBJETIVA y OPERATIVA. Nada de marketing, premios, reputación ni slogans.
- Si un dato no es explícito, dejá el campo VACÍO. No inventes.
- Registrá las URLs usadas (sources) y un nivel de confianza.

CAMPOS (todos genéricos — describen la empresa, sin importar quién le venda):
  company_domain        dominio oficial
  activity_description  qué produce / transforma / presta, en términos operativos
  industry              sector / industria principal
  offerings_list        productos o servicios concretos
  primary_customer_type tipo de cliente principal si es evidente
  sales_channels        mecanismo comercial principal de venta
  geographic_footprint  HQ + zonas / regiones donde opera
  size_estimate         tamaño estimado: micro / chica / mediana / grande
  size_evidence         qué señal lo sugiere (team page, "somos X", n° de sucursales)
  recent_changes        cambios recientes (aperturas, expansión, rebrand, lanzamientos,
                        mudanzas, contrataciones clave) con fecha si aparece
  digital_presence      LinkedIn de empresa + canales activos

Devolvé SOLO este JSON:
{
  "company_domain": "",
  "activity_description": "",
  "industry": "",
  "offerings_list": "",
  "primary_customer_type": "",
  "sales_channels": "",
  "geographic_footprint": "",
  "size_estimate": "",
  "size_evidence": "",
  "recent_changes": "",
  "digital_presence": "",
  "sources": [],
  "extraction_confidence": ""   // alta | media | baja
}
```

---

## Prompt B — column `icp_lens` (the ICP lens — identical prompt, brief is the variable)

```
ROL: Dado el perfil objetivo de una empresa (dossier) y un brief de ICP, evaluás el FIT
para ESE ICP y cazás los triggers que el brief pide. No re-describas la empresa; interpretá.

INPUT:
  dossier:   {{dossier}}      # el JSON de la columna anterior
  icp_brief: {{icp_brief}}    # el brief del ICP — MISMO para toda la tabla

TAREA:
1) Extraé los `additional_signals` que pide el brief. Si el dossier / fuentes no lo dicen,
   dejá ese campo vacío. No inventes.
2) Buscá los `triggers_to_hunt` del brief. Listá SOLO los que tengan evidencia.
3) Juzgá el fit usando fit_positive / fit_negative del brief:
     strong = varias señales positivas, ninguna negativa fuerte
     medium = señales mixtas o parciales
     weak   = pocas señales / mayormente negativas
     none   = claramente fuera de ICP
4) Justificá en 1-2 frases con evidencia concreta.

Devolvé SOLO este JSON (las claves de icp_signals son las del `additional_signals` del brief):
{
  "icp_signals": { },
  "icp_fit": "",          // strong | medium | weak | none
  "icp_fit_reason": "",
  "triggers_found": []
}
```

> The email waterfall runs only on rows where `icp_fit` is `strong` or `medium`
> (the gate). `weak`/`none` never consume email credits.
