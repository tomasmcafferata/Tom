# Enrichment Stage — Clay Recipe & Contract

Generic, replicable recipe for the enrichment stage. Enrichment runs in **Clay**; the repo
is the version-controlled **library** of what you paste into Clay:
- `gtm/leads/research-prompt-base.md` — the two generic GPT prompts (never change).
- `clients/<client>/research-brief-<icp>.yaml` — the per-ICP brief (the only thing that changes).
- this file — how to build, gate, write back, clone, and verify.

Client-agnostic. Only the Sheet ID, the cloned Clay table, and the brief differ per ICP.

---

## Cost model (why the order is what it is)

- **Cheap — web research with GPT (your OpenAI key in Clay):** domain, activity, industry,
  size estimate, geography, recent changes, AND the ICP-specific signals + triggers.
  Anything publicly findable. Runs on the **whole pool**.
- **Expensive — Clay credits:** verified **email**. The AI can't do this. Runs **last, on
  survivors only**.

So: research + fit first (cheap, all), email last (expensive, the few that pass the gate).

```
prescreen (free)          → 2,283 kept
   │
Clay: dossier + icp_lens  → fit + triggers          [cheap, all 2,283]
   │
filter icp_fit ∈ {strong, medium}                   [the gate]
   │
Clay: email waterfall     → email + confidence       [Clay credits, survivors only]
   │
write back to Sheet by lead_id → campaigns
```

---

## The generic / brief split (what makes it replicable)

Two Clay AI columns. **Neither prompt changes between ICPs** — only the brief value does.

| Column | Prompt (from research-prompt-base.md) | Per-ICP? |
|---|---|---|
| `dossier` | Prompt A — generic company profile | No — identical everywhere |
| `icp_lens` | Prompt B — reads `dossier` + `{{icp_brief}}` → fit + triggers | Prompt no; only the `icp_brief` value |

The `icp_brief` is a value (a table variable holding the YAML brief text), not part of the
prompt. Clone the table, paste another brief, and the agent hunts different signals with
zero prompt edits.

---

## Build the Clay table (one per ICP)

1. **Source** = the client's Lead Database, filtered to this ICP's pool
   (for NDC-ploteo: `status != disqualified`, ~2,283 rows). Import `lead_id`, `company`
   (→ company_name), `location`, `company_domain`.
2. **Column `dossier`**: AI column with **Prompt A**. Pair with Clay's website scrape (or a
   web-enabled GPT) so the model has the page text. Use your OpenAI key.
3. **Column `icp_lens`**: AI column with **Prompt B**. Inputs: the `dossier` column +
   the `icp_brief` variable (paste `clients/NDC/research-brief-ploteo.yaml`).
4. **Gate**: filter the table to `icp_fit` is `strong` OR `medium`.
5. **Email waterfall** (on the filtered view only): Findymail → Prospeo → Dropcontact
   (tune to your plan). This is where Clay credits get spent — on the survivors.
6. **Write back** to the Sheet, matched on `lead_id` (see contract below).

---

## Write-back contract (Clay → Sheet)

All target columns already exist in the Leads schema — no schema change.

| Clay output | Sheet column |
|---|---|
| `dossier.company_domain` | `company_domain` |
| `dossier.industry` | `industry` |
| `dossier.size_estimate` | `company_size` (note: estimate, not verified) |
| compact `dossier` + `triggers_found` + `icp_fit_reason` | `company_intel` (the field campaigns read) |
| ICP name, e.g. `"ploteo"` | `icp_segment` |
| `icp_lens.icp_fit` (strong/medium/weak/none) | `icp_tier` |
| email waterfall result | `email`, `email_confidence` |
| set on success | `enriched = TRUE` |

`icp_score` stays blank — the gate is the `icp_fit` verdict, not a numeric score.

---

## Verify (read-only gate before campaigns)

```
py -3 gtm/scripts/enrich_status.py --client NDC
```
Watch `With email (enriched)` and `Ready to score` climb as Clay writes back. Then
spot-check 10–15 rows in the Sheet: does `company_intel` read true (no hallucination —
cross-check against `sources`), and does `icp_fit` look right for the `industry`/`activity`?

---

## Clone for a new ICP / client

Nothing in the prompts changes. To add an ICP (e.g. NDC-eventos, Agupá-muebles):
1. Write `clients/<client>/research-brief-<icp>.yaml` (copy ploteo, edit signals/triggers/fit).
2. Duplicate the Clay table, point its source at that ICP's pool, paste the new brief into
   the `icp_brief` variable.
3. Run. Same two prompts, new lens.
