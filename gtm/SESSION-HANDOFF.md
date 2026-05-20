# GTM System — Session Handoff
**Fecha:** 2026-05-20  
**Objetivo de la sesión:** Mapear el sistema GTM completo y arrancar M4 (lead pipeline)

---

## Contexto del sistema

Sistema GTM outbound freelance multi-cliente. Tomás opera como estratega + QA. El sistema debería correr casi solo.

**Stack activo:**
- LinkedIn Sales Navigator + LinkedHelper (export de listas)
- Clay (enriquecimiento: email + account intel)
- Instantly (envío de campañas outbound)
- Sistema de email-response (Python, ya construido): pollea Instantly → clasifica replies → genera drafts → Slack approval → envía emails
- Google Sheets (CRM de replies, ahora también Lead DB)
- Slack (notificaciones, aprobaciones)

**Clientes activos:** NDC (enedece.com.ar), Agupá, Tomas (propio)

---

## Estado del pipeline completo

```
[INVESTIGACIÓN]  →  [LISTA]  →  [CAMPAÑA]  →  [REPLIES]  →  [CONVERSIÓN]  →  [REPORTE]
  ✅ Cubierto        🔧 En build  ➕ Instantly   ✅ Cubierto    ❌ Pendiente     ❌ Pendiente
```

---

## Qué se construyó esta sesión

### 1. ROADMAP.md (`gtm/ROADMAP.md`)
8 módulos priorizados con alcance, esfuerzo y dependencias.

### 2. Google Sheet — NDC Lead Database
**URL:** https://docs.google.com/spreadsheets/d/1IE_KZpTBSzYE6i9_fCRcDptgpDjLh4ZXqBQOOW1jmQY  
**Ubicación en Drive:** Carpeta "Cold" (tomascafferata19@gmail.com)

Tres tabs configuradas via Apps Script:
- **Leads** — 29 columnas, dropdowns en status/track/segment/tier, color coding por status
- **Campaigns** — historial de campañas lanzadas
- **Pipeline** — fórmulas automáticas: conteo por status, segmento, tier, capacidad calculada

### 3. Módulo `gtm/leads/`
- `setup_sheet.gs` — Apps Script que creó la estructura del sheet
- `setup_sheet.py` — versión Python (requiere service account, para uso local)
- `config.yaml` — configuración del módulo (sheet ID, capacidad de inboxes)
- `requirements.txt`

---

## Decisiones de arquitectura tomadas

**Lead Database:**
- Google Sheets (no SQLite, no Airtable) — ya en el stack, Claude puede leer/escribir
- Un sheet por cliente (no un master sheet multi-cliente)
- Una tab Leads con columna `icp_segment` (no tabs separadas por segmento)

**Dos tracks de leads:**
- `trigger` — listas de expositores de ferias, prioridad alta, secuencia personalizada por evento
- `base` — Sales Navigator via LinkedHelper, batch recurrente

**Flujo de importación en dos pasos:**
1. LinkedHelper CSV (sin email) → deduplica → agrega leads con status `new`
2. Clay CSV (con email + intel) → actualiza columnas de enrichment → status `enriched`

La deduplicación en el paso 1 evita pagar Clay por leads que ya están en la DB.

**Claude Code como mediador (decisión clave):**
No Python scripts corriendo localmente para operaciones de leads. En cambio:
- Tomás le pasa el CSV a Claude en la sesión
- Claude lee, deduplica, formatea y escribe en Sheets
- Claude genera digests leyendo directamente los sheets
- Requiere un Apps Script web app como endpoint de escritura (setup único, en browser)

---

## Ciclo operativo recurrente (diseñado, no implementado aún)

```
CADA 2-3 SEMANAS (base leads):
  LinkedHelper exporta CSV → Tomás se lo pasa a Claude
  Claude deduplica y agrega leads 'new' al sheet
  Claude exporta lista para Clay
  Clay enriquece (manual en web UI)
  Clay output → Tomás se lo pasa a Claude
  Claude actualiza enrichment → status 'enriched'
  Claude planea próximo batch (por tier y segmento)
  Tomás aprueba → Claude sube a Instantly

CUANDO HAY FERIA PRÓXIMA (trigger leads):
  Lista de expositores → Claude importa, prioriza, genera campaña personalizada

DIARIO (automático):
  Sync de resultados Instantly → actualiza statuses en sheet
  Replies fluyen al sistema de email-response (ya construido)
```

---

## Modelo de datos del lead (29 columnas)

```
IDENTIDAD:     lead_id, email, first_name, last_name, title, company,
               company_size, industry, location, linkedin_url

ORIGEN:        source_type, source_batch, import_date

ENRICHMENT:    enriched, enrichment_date, email_confidence, company_intel

SEGMENTACIÓN:  track, icp_segment, icp_score, icp_tier

LIFECYCLE:     status, current_campaign, last_contact_date,
               campaign_count, cooling_until

RESULTADO:     reply_classification, do_not_contact, notes
```

**Status values:** new → enriched → queued → active → cooling → replied/interested/meeting_booked/converted  
**Terminales:** not_interested, unsubscribed, bounced, do_not_contact

**Capacidad NDC:** 4 inboxes × 30/día × 21 días / 4 pasos = **630 leads/ciclo**  
**Cooldown:** 90 días antes de re-engagement

---

## Preguntas abiertas — resolver en próxima sesión

### 1. ¿Dónde corre `main.py`? (CRÍTICO)
El sistema de email-response necesita estar siempre encendido. ¿Laptop, servidor, VPS?
Esto determina M8 (infraestructura) y si los cron jobs son viables.

### 2. ¿Cómo es el output de Clay?
¿Qué columnas devuelve? ¿CSV o export desde la UI de Clay?
Necesario para construir el import de enrichment.

### 3. ¿Qué columnas tiene el CSV de LinkedHelper?
Necesario para construir el import. Usuario no tenía uno disponible en esta sesión.

### 4. Apps Script web app como endpoint de escritura
Para que Claude pueda escribir en Sheets sin credenciales locales.
Pendiente de construir e instalar (5 minutos en browser).

---

## Módulos priorizados (del ROADMAP.md)

```
FASE 1 — Visibilidad y estabilidad
  M8  Infraestructura email-response (bloqueado hasta saber dónde corre)
  M1  Monitoreo de campaña — Instantly → Slack
  M3  Dashboard de estado del cliente

FASE 2 — Cierre del loop
  M2  Weekly digest + reporting
  M5  Conversión post-reply positivo
  M7  Onboarding nuevo cliente

FASE 3 — Escala
  M4  List building (en progreso — sheet creado, import pendiente)
  M6  Feedback loop estratégico
```

---

## Archivos clave

```
gtm/
├── ROADMAP.md                          ← plan completo del sistema
├── GTM-WORKFLOW.md                     ← pipeline de investigación (8 pasos)
├── SESSION-HANDOFF.md                  ← este archivo
├── clients/NDC/                        ← docs estratégicos (ICP, TAM, etc.)
├── leads/
│   ├── config.yaml                     ← sheet ID + capacidad
│   ├── setup_sheet.gs                  ← Apps Script (ya ejecutado)
│   └── setup_sheet.py                  ← versión Python (para referencia)
└── skills/email-response/
    ├── main.py                         ← sistema de replies (ya funciona)
    ├── config.yaml
    └── ...
```
