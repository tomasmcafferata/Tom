# /import-leads

Import leads from a source Google Sheet into a client CRM sheet.

## Usage

```
/import-leads <source_url> <dest_url> --client <NAME> [--batch <name>]
```

- `source_url` — Google Sheet with the leads to import
- `dest_url`   — Client CRM sheet (destination)
- `--client`   — Client prefix for lead IDs (e.g. NDC, AGUPA, TOMAS)
- `--batch`    — Optional. If omitted, use the source sheet's title.

---

## What to do (step by step)

**1. Parse the arguments from `$ARGUMENTS`.**
Extract `source_url`, `dest_url`, `--client`, and `--batch` from the input.
Derive the Google Sheet ID from each URL (the long alphanumeric ID between `/d/` and `/edit`).

**2. Read the source sheet** using the Drive MCP tool (`read_file_content`).
- Get the file title (for `source_batch` if `--batch` not provided) using `get_file_metadata`.
- Identify the column names present in the source.

**3. Read the destination sheet** using the Drive MCP tool (`read_file_content`).
- Extract the column headers from the **Leads** tab (first row).
- This is always read live — never assume or hard-code the columns.

**4. Detect the source format** by comparing the source columns to the signature columns in the format templates at `gtm/scripts/formats/`:
- `linkedin_sales_nav.json` → signature: `profile_url`, `headline`, `location_name`, `current_company`, `current_company_position`
- `clay_enriched.json`      → signature: `email`, `company_size`, `industry`
- If no template matches, treat it as **unknown format** and derive the mapping manually.

**5. Build the mapping.**
- Start from the matched template (or from scratch if unknown).
- For each destination column, decide:
  - **Direct map**: a source column clearly corresponds to it
  - **Default**: a fixed value makes sense (e.g. `status = new`, `enriched = FALSE`)
  - **Blank**: no source data, will be filled in a later enrichment step
- Flag any destination columns that exist in the CRM but have no source data (these will be blank).

**6. Show the mapping table to the user** in this format:

```
SOURCE SHEET:  <title> (<N> rows)
DEST SHEET:    <title> — tab: Leads
FORMAT:        <detected format or "unknown">
LEAD ID PREFIX: <client>-001 ...

COLUMN MAPPING:
  dest_col          <- source_col / "static value" / [blank - later]
  ...

Columns that will be blank (for enrichment later):
  email, company_size, industry, icp_segment, icp_score, icp_tier, track ...
```

Ask: **"Confirmas el mapeo? (s/n) — o indicame qué cambiar."**

**7. On confirmation**, do the following:

a. Write the mapping to a temp file: `gtm/scripts/formats/_current_import.json`
   Format: `{ "column_map": {...}, "defaults": {...} }`

b. Run the import script:
```bash
py -3 gtm/scripts/import_leads.py \
  --source-id  <source_id> \
  --dest-id    <dest_id> \
  --dest-tab   Leads \
  --batch      "<batch_name>" \
  --prefix     <CLIENT> \
  --mapping    gtm/scripts/formats/_current_import.json
```

c. Report the result: how many leads imported, ID range, any errors.

**8. After a successful import**, ask the user:
> "Queres guardar este mapeo como template para futuros imports con este formato? Si sí, dame un nombre (ej: `clay_ndc_v1`)."

If yes, save it to `gtm/scripts/formats/<name>.json` for reuse.

---

## Key rules

- **Always read dest headers live** — never assume the CRM columns.
- **Never overwrite existing leads** — the script appends, always checks existing IDs.
- If the source has duplicate leads (same `profile_url` or `linkedin_url`), warn the user before importing.
- If `--client` is not provided, ask before proceeding.
- If the dest tab is not named `Leads`, show the available tabs and ask which one to use.
