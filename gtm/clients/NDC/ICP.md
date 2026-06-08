# Ideal Customer Profile (ICP)
**Company / Product:** NDC — enedece.com.ar
**Date:** March 26, 2026
**GTM Motion:** Outbound
**Prepared for:** GTM Team

---

## Executive Summary

NDC's ideal customer is a mid-size Argentine company (20–300 employees) that needs to show up professionally in physical spaces — at trade shows, on their vehicle fleet, in retail locations, or at corporate events — and is currently juggling multiple fragmented suppliers to make it happen. The pain is coordination overhead, inconsistent quality, and the stress of tight deadlines across design, production, and installation. NDC wins because they do it all in-house: renders, taller, impresión, logística, and installation under one roof. The primary outreach target is the Marketing Manager or Events Coordinator who carries the operational burden of making this work every year. The market is large, under-served by integrated providers, and highly trigger-driven — the best time to reach them is 60–90 days before a major trade show or store opening.

---

## Segments / Motions

NDC's outbound covers **two motions with two different buyers**. Most of this document describes Segment A (the default). Segment B was discovered when an actual lead list ("Ops ICP Ploteo", ~2,804 leads) turned out to be ops/logistics people, not marketing — so it gets its own persona + screen below.

| Segment | Motion | Primary buyer | Where defined |
|---|---|---|---|
| **A — Events / Stands** | Trade-show stands, event production, signage | Marketing Manager / Events Coordinator | The body of this document |
| **B — Ploteo / Fleet-wrapping** | Vehicle wrapping / fleet branding | Ops / Logistics / Fleet decision-maker, or GM / owner (PyME) | Section **"Segment B"** below |

The pre-screen rules that triage a raw list into persona tiers are encoded per-segment in `clients/NDC/prescreen-rules.yaml` (the executable mirror of the prose here) and run via `gtm/scripts/prescreen.py --client NDC`.

---

## Firmographic Profile

```
FIRMOGRAPHIC ICP
================

Industry / Vertical:
  Primary:    Logistics & transportation (vehicle fleet branding)
              Food & beverage / CPG (trade show presence at Alimentaria, SIAL, etc.)
              Healthcare & pharma (medical congresses, stands at Expofarmacia, etc.)
              Retail chains & franchises (store signage, restyling, new openings)
  Secondary:  Technology / IT companies (tech events, stands)
              Construction & real estate (project signage, showrooms)
              Manufacturing / industrial (sector trade fairs)
  Exclude:    Pure B2C consumer brands with no event or fleet presence
              Micro-businesses under 10 employees (no budget, no repeat volume)
              Government/public sector (slow procurement, low margin)

Company Size:
  Employees:  20–300
  Revenue:    $500K–$15M USD equivalent (ARS)
  Stage:      Established SMB or growing mid-market; NOT pre-revenue

  Rationale:  Small enough that they don't have in-house production capability,
              large enough to have a recurring events/branding budget. Companies
              in this range attend 2–6 trade shows per year and have 5–50 branded
              vehicles. They feel the pain of fragmented suppliers most acutely.

Geography:
  Primary:    Gran Buenos Aires + CABA (fastest turnaround, NDC's home base)
  Secondary:  Rosario, Córdoba, Mendoza (national installation capability)
  Exclude:    International (no cross-border logistics currently)

Business Model:
  B2B companies selling to other businesses or through physical retail channels.
  Companies where physical presence = commercial credibility.

Tech Stack Signals (if relevant):
  Uses:       Companies using event management platforms (Eventbrite, etc.)
              Companies with active LinkedIn company pages posting about events
              Companies advertising trade show participation on social media
  Avoid:      Pure digital-only companies with no physical footprint

Growth Signals (outbound trigger events):
  - Registered or announced participation in a major trade show (Expo Rural,
    ExpoEFI, Alimentaria, Automechanika, FITHEP, Cosméticos & Perfumería, etc.)
  - New store opening, franchise expansion, or office relocation announced
  - Vehicle fleet renewal (job posting for fleet manager, or news of fleet expansion)
  - Company rebranding (new logo, new visual identity announced on LinkedIn/press)
  - New product line launch requiring event presence
  - Hired a new Marketing Manager or Events Coordinator (new person = new vendor review)
  - Recent funding round or acquisition (new budget, new identity needs)
```

---

## Situational Profile

```
SITUATIONAL ICP
===============

Pain State:
  The company is experiencing: Coordination chaos before every major event or campaign.
  They're managing 3–5 separate vendors — a graphic design studio, a printing shop,
  a stand constructor, a transport company, and an installation crew — none of whom
  talk to each other. Someone (usually the Marketing Manager) is the human glue.
  This is caused by: The Argentine market being fragmented — there is no dominant
  integrated visual communications provider for SMBs.
  The cost of inaction: A botched stand at Expo Rural costs the company its one shot
  to impress 10,000 industry buyers. A poorly wrapped fleet sends the wrong signal
  to prospects every day it's on the road. A delayed store opening loses revenue.

Current State (Before):
  They are currently trying to solve this with: A patchwork of local printers,
  freelance designers, and stand rental companies — re-quoted from scratch each time.
  Why that's not working: No single vendor owns the outcome. Delays in one step
  cascade into the rest. Quality is inconsistent across vendors. The Marketing
  Manager spends 40% of their pre-event time on logistics, not strategy.

Desired State (After):
  They want to achieve: One vendor call, one brief, one delivery. Show up at the
  event and everything is already set up, on-brand, on time.
  Their definition of success: "I sent NDC the brief, they handled everything,
  and the stand looked exactly like the render."

Urgency Drivers:
  - Event date is fixed and immovable — urgency is baked in
  - Board/CEO visibility: the stand represents the company at the industry's
    biggest events — failure is highly visible
  - Competitor is also exhibiting at the same show (competitive pressure)
  - New Marketing Manager wants to make an impression in their first big event

Budget Reality:
  Budget likely sits in: Marketing department (events + branding line items)
                         or Commercial/Sales (trade show budget)
  Decision is typically: Pre-budgeted annually for recurring events;
                         discretionary for new initiatives (new fleet wrapping,
                         store restyling)
  Procurement complexity: Usually credit card or PO — no formal RFP process
                          at SMB level. Decision made by Marketing Manager,
                          approved by Commercial Director or CFO.
```

---

## Buyer Personas

### Champion (Primary Outreach Target)

```
PERSONA 1: THE CHAMPION
=======================
Title(s):       Marketing Manager / Responsable de Marketing
                Coordinadora de Eventos / Events & Communications Manager
                Brand Manager / Jefe de Marketing
Seniority:      Manager / Coordinator (not C-suite, not IC)
Department:     Marketing / Communications

What they care about:
  - Executing events flawlessly — their reputation is on the line at every trade show
  - Reducing the coordination overhead that eats their week before every event
  - Consistent brand presentation across all physical touchpoints (stand, fleet,
    signage, merch) — everything matching the brief
  - Having a vendor they can trust to deliver without hand-holding

What keeps them up at night:
  - The stand arrives incomplete the day before the show opens
  - A vendor drops out 3 weeks before the event
  - The CEO walks past the stand and it doesn't look like the render
  - Managing 5 vendors at once for a single event and being blamed when one fails

How they find solutions:
  - Word of mouth from peers in similar roles (most trusted)
  - LinkedIn (actively posts about events, follows industry accounts)
  - Google searches when a vendor fails them ("empresa stands Buenos Aires",
    "ploteo vehicular empresas")
  - Industry event directories and exhibitor lists

Outreach notes:
  - Best channel:  LinkedIn (they're active, posting about events and campaigns)
                   Cold email (professional, responds to specific hooks)
  - Best hook:     Reference a specific upcoming event they're exhibiting at,
                   or a recent event they posted about on LinkedIn.
                   Lead with the pain: "coordinating 4 vendors for one stand"
  - What to avoid: Generic "we do printing" pitches. They get those constantly.
                   Never lead with price. Lead with the outcome and the relief.
```

### Economic Buyer

```
PERSONA 2: THE ECONOMIC BUYER
==============================
Title(s):       Gerente Comercial / Commercial Director
                Director de Marketing / CMO
                CEO / Dueño (at companies under 50 employees)
Seniority:      C-Suite / Director
Department:     Commercial / Marketing / General Management

What they care about:
  - ROI on event spend: did the stand generate leads, meetings, visibility?
  - Brand consistency: does the company look professional vs. competitors?
  - Operational reliability: no surprises, no fires, no excuses

Their buying question:
  "Can I trust this vendor to make us look good at [Expo Name] without
   my team losing sleep over it?"

Outreach notes:
  - Reach via:    Champion referral (preferred) or exec-to-exec LinkedIn
  - Best message: Business outcome framing — "Companies that consolidate their
                  event production under one vendor save 30% of pre-event
                  coordination time and show up more consistently."
```

### Blocker

```
PERSONA 3: THE BLOCKER
=======================
Title(s):       CFO / Contador / Finance Manager
Their objection: "We already have a printer we've worked with for years.
                  Why would we change?"
How to handle:  Acknowledge the relationship, then reframe: NDC is not a
                printer — they're a full production + logistics partner.
                The existing printer can't build a stand, wrap a truck fleet,
                and coordinate on-site installation. That's the gap NDC fills.
                Offer a first project at lower stakes (e.g., banner production
                for an internal event) to demonstrate quality and reliability
                before proposing a full stand engagement.
```

---

## Negative ICP

```
NEGATIVE ICP — DO NOT TARGET
==============================

Company-level disqualifiers:
  - Fewer than 10 employees — no recurring events budget, not worth the CAC
  - Pure digital businesses (tech startups, software companies with no
    physical presence or events strategy)
  - Government agencies and municipalities (slow payment, low margin,
    procurement bureaucracy)
  - Companies that already have in-house production (large corporates
    with internal design + print departments)
  - Companies outside Argentina (no cross-border capability currently)

Person-level disqualifiers:
  - Junior graphic designers or community managers — no budget authority
  - CEOs of 500+ person companies — wrong entry point, need the Marketing Manager
  - Purchasing/procurement managers as first contact — they commoditize
    and drive to cheapest bid; get to Marketing first

Situational disqualifiers:
  - Just completed a major event (no immediate urgency for 6–9 months)
  - Company in financial distress or active layoffs
  - Already locked in a multi-year contract with a competitor
  - Startup pre-revenue or pre-product — no events budget exists yet
```

---

## TAM Snapshot

```
TAM SNAPSHOT
============

Estimated universe of ICP-fit companies:
  Narrow ICP (20–300 employees, exhibiting at trade shows, GBA):  ~3,000–5,000 companies
  Broader ICP (all Argentine B2B companies with events/fleet budget): ~15,000–25,000 companies

How to build the list:
  - LinkedIn Sales Navigator filters:
      Industry: Logistics / Food & Beverage / Healthcare / Retail / Manufacturing
      Company size: 11–200 employees
      Geography: Buenos Aires, Argentina
      Title: "Marketing Manager", "Gerente de Marketing", "Coordinadora de Eventos"
  - Apollo / Clay filters:
      Industries: Transportation, Food Production, Pharmaceutical, Retail
      Employees: 20–300
      Country: Argentina
      Keywords: "eventos", "ferias", "stands", "flota vehicular"
  - Intent triggers (manual):
      Exhibitor lists from: Expo Rural, ExpoEFI, Alimentaria Argentina,
      FITHEP, Automechanika Buenos Aires, Cosméticos & Perfumería
      LinkedIn posts announcing event participation (search: "estaremos en [expo]")
      LinkedIn posts showing new store openings or fleet rebranding

Priority segments to start with:
  1. Logistics & transport companies (GBA, 20–200 employees) — estimated 800–1,200 accounts
     [Highest immediate trigger: fleet wrapping is recurring, high-value, visible ROI]
  2. Food & beverage / CPG brands (exhibiting at Alimentaria/FITHEP) — estimated 400–600 accounts
     [Best proof: these events are large, visible, and companies spend heavily on stands]
  3. Healthcare/pharma companies (medical congress exhibitors) — estimated 200–400 accounts
     [High spend per stand, professional buyer, repeat annually]
```

---

## Outbound Readiness

```
OUTBOUND READINESS
==================

List buildability:          Medium
  Reason: Argentine companies are findable on LinkedIn and Apollo, but
          data quality for SMBs is lower than US/EU markets. Exhibitor
          lists from major trade shows are the highest-quality source
          and require manual research.

Reachability:               Medium–High
  Reason: Marketing Managers in Argentina are active on LinkedIn, especially
          around events. Cold email deliverability is solid. Response rates
          are generally higher than US cold outreach due to lower volume
          of outbound they receive.

Message clarity:            Sharp
  Reason: The pain (fragmented vendors, coordination chaos before events) is
          specific, felt, and easy to articulate in one sentence.

Sales cycle estimate:       2–6 weeks (from first contact to first project)
                            Recurring projects compress to days once trust is established
Typical deal size:          $150,000–$2,000,000+ ARS per project
                            ($500–$6,000 USD equivalent at current rates)
                            Fleet wrapping projects can be $1M–$5M+ ARS for full fleets
Estimated conversion rate:  3–7% cold to meeting (higher with trigger-based outreach)

Biggest outbound challenge:
  Trust barrier — Argentine SMBs are wary of new vendors for high-stakes events.
  Address by: leading with a low-stakes entry offer (banner, back de prensa,
  merchandising for an internal event) before pitching the full stand engagement.
  Let them experience the quality and reliability on a small project first.

Recommended starting sequence:
  Channel 1: LinkedIn — engage with their event-related posts before connecting.
             Then connect with a personalized note referencing their upcoming event.
  Channel 2: Cold email — 4-step sequence over 12 days, trigger-led
             (reference a specific upcoming expo they're exhibiting at)
  Channel 3: LinkedIn DM after connection (day 5 post-connect) — share a
             relevant case study or before/after of a similar company's stand
```

---

## ICP Scoring Rubric

```
ICP SCORING RUBRIC
==================

Score each prospect out of 100:

FIRMOGRAPHIC FIT (40 points)
  Industry match:       0 (wrong vertical) / 10 (adjacent) / 20 (exact — logistics,
                        food & bev, pharma, retail, manufacturing)
  Company size match:   0 (<10 or >500 employees) / 10 (10–20 or 300–500) / 20 (20–300)

SITUATIONAL FIT (35 points)
  Pain signal present:  0 (no evidence of events/fleet/signage activity)
                        15 (active LinkedIn presence posting about events or fleet)
  Trigger event:        0 (no upcoming event found)
                        20 (registered/announced exhibitor at a named trade show
                           within 60–90 days, OR new store opening announced,
                           OR fleet expansion news found)

PERSONA FIT (25 points)
  Title match:          0 (wrong department — HR, IT, Finance)
                        10 (Commercial Director or CEO without dedicated Marketing)
                        25 (Marketing Manager / Events Coordinator / Brand Manager)

SCORING TIERS:
  80–100: Tier 1 — Prioritize immediately, personalize outreach with specific
          event name, show date, and relevant case study
  60–79:  Tier 2 — Include in sequences with industry-specific personalization
  40–59:  Tier 3 — Batch outreach only, test messaging
  <40:    Disqualify — remove from active list

AUTOMATIC DISQUALIFIERS (score = 0 regardless):
  - Fewer than 10 employees
  - Government/public sector entity
  - Pure digital business with no physical presence or events activity
```

---

## Segment B — Ploteo / Fleet-Wrapping (ops buyer)

> **Why this segment exists.** A loaded list (~2,804 leads, batch "Ops ICP Ploteo") does **not** match Segment A's marketing persona — only ~2% of titles are marketing/events; the bulk are operations, general management, and "encargados". For fleet wrapping in an Argentine SMB, the decision-maker is **not** marketing — it's whoever **runs the fleet** (operations/logistics) or **whoever is in charge** (GM/owner in small companies). Marketing enters as a co-buyer for brand consistency, not as the entry point. This section defines that buyer and the rubric to screen this list correctly.

### Buyer Personas (ploteo)

**Primary — runs the fleet**
```
Titles:     Gerente / Director de Operaciones · COO · Jefe/Gerente de Logística
            Jefe/Gerente de Flota · Gerente de Transporte · Gerente de Distribución
            Encargado de Flota / Logística / Transporte (with qualifier)
Seniority:  Manager / Director (operational decision-maker)
Cares:      That the fleet looks professional and consistent, the wrap survives use,
            and the vendor hits deadlines without stalling operations.
```

**Primary alternate — whoever is in charge (small PyME)**
```
Titles:     Gerente General · General Manager · Director General · CEO
            Dueño / Propietario / Titular / Socio / Fundador
Seniority:  C-suite / owner
When:       Companies <50 employees with no dedicated ops manager, where the
            owner/GM makes this kind of purchase.
```

**Secondary — Marketing (co-buyer, not entry)**
```
Titles:     Gerente de Marketing · Marca · Trade Marketing · Comunicación
Role:       Guards brand consistency of the wrap. Influences, rarely signs the ploteo.
            Useful as a second contact, not as first touch for this motion.
```

**Blocker**
```
Titles:     CFO / Contador / Compras
Objection:  "We already have someone who does our cars." / "Why change?"
Handling:   Reframe: NDC integrates design + production + installation + logistics —
            not a loose shop. Low-risk entry offer (1–2 pilot vehicles).
```

### Firmographic Profile (ploteo)
```
Owns or operates a fleet (central signal):
  Primary:    Logistics / transport / distribution · Food & beverage / CPG (delivery)
              Field-service crews · Construction · Wholesalers with delivery
  Secondary:  Retail with distribution fleet · Pharma/health with delivery
  Exclude:    Companies with no vehicles (office/digital only) · <10 employees
              Government/public · Corporates with in-house production · outside Argentina

Company Size:   20–300 employees (enough vehicles to matter, not so large they have an
                in-house shop). Owner/GM decides in the <50 band.

Geography:      Primary: GBA + CABA. Secondary: Rosario, Córdoba, Mendoza, Santa Fe.
                Exclude: outside Argentina (no cross-border).
```

### Trigger events (ploteo)
```
- Fleet renewal or expansion (vehicle purchase, post, or news)
- Rebranding / new visual identity (cars must be re-wrapped)
- New branch / distribution center opening (new vehicles to brand)
- Hiring a "Fleet/Logistics Manager" (new management = vendor review)
- Merger/acquisition (fleet identity unification)
```

### Scoring rubric (ploteo) — what each stage evaluates

> **Design key:** the pre-screen is **free** and can only look at what we already have (title, company, location). Real company fit (does it have a fleet?, industry, size) and triggers **need enrichment** and are scored post-enrichment. We do not spend Clay credits on leads the title already disqualifies.

```
SCORE /100

PERSONA FIT (35)          ← pre-screen evaluates this (title)
  35  Fleet/ops decision-maker (Operations, Logistics, Fleet, Transport,
      Distribution) or GM/Owner in a PyME
  20  GM/Director at a mid-size company, or Commercial with influence
  10  Marketing (co-buyer) or "Encargado" with a relevant qualifier
   0  Wrong dept (HR, IT, Finance-only, junior, cashier, reception)

GEOGRAPHY (10)            ← pre-screen evaluates this (location)
  10  GBA / CABA
   7  Rosario / Córdoba / Mendoza / Santa Fe / rest of Argentina
   0  Outside Argentina  →  DISQUALIFY (no cross-border)

FIRMOGRAPHIC FIT (35)     ← post-enrichment (industry + size)
  20  Industry with own/delivery fleet (logistics, distribution, food&bev, etc.)
  15  Size 20–300 employees

SITUATIONAL / TRIGGER (20) ← post-enrichment / research
  20  Fleet trigger detected (renewal, rebrand, expansion)
   0  No trigger

TIERS:
  80–100  Tier 1 — prioritize, personalize (visible fleet, concrete trigger)
  60–79   Tier 2 — sequence with industry personalization
  40–59   Tier 3 — batch, test messaging
  <40     Disqualify

AUTOMATIC DISQUALIFIERS (score = 0):
  - Outside Argentina
  - <10 employees / government / no fleet
  - Wrong-department person
```

### Pre-screen rules (free, title + location only)

The pre-screen assigns a **persona_tier** to decide **how far to enrich** (Clay cost dial) — it does *not* produce the final score. Plain-language rules below; the **executable encoding** lives in `clients/NDC/prescreen-rules.yaml` (edit there to tune) and runs via `gtm/scripts/prescreen.py --client NDC`.

```
TIER 1 (clear target — enrich YES):
  Ops / logistics / fleet / transport / distribution / supply-chain titles,
  or GM / General Manager / Director General / owner-tier (dueño, socio, fundador, CEO, COO).

TIER 2 (co-buyer / influencer — enrich PROBABLE):
  Commercial / sales / marketing / admin titles,
  or "Encargado de {flota|logística|transporte|operaciones|depósito|distribución|...}".

TIER 3 (ambiguous — ENRICH, then judge):
  Bare "Encargado/a" with no qualifier (~1,639 leads in the current list).
  Cannot be disambiguated on title alone. DECISION: enrich on the first pass — we prefer
  to stay flexible on ambiguous personas and let enrichment (company industry/size) decide,
  rather than drop a potential fleet buyer. Drop later if the company turns out off-ICP.

DISQUALIFY (do not enrich):
  - location present and NOT Argentina
  - wrong-department titles: HR, IT, software/dev (developer, not biz-dev), finance,
    accountant, CFO, treasury, community manager, design, intern, junior, reception,
    cashier, salesperson
  - no title
```

> **Decision (resolved 2026-06-03):** Tier 3 (bare "Encargado", ~1,639 leads) **enters** the first enrichment pass. It is the biggest Clay-cost driver, but the policy is to stay flexible on ambiguous personas and let company enrichment decide. Full enrich pool = Tier 1+2+3 (~2,283 leads).

### Pipeline for this segment
1. Pre-screen applies these rules → tier table + pool (free). ~2,283 kept.
2. Clay research, cheap, on all 2,283: generic `dossier` + `icp_lens` (this segment's
   brief) → industry, fleet signals, triggers, `icp_fit`. See `gtm/leads/ENRICHMENT.md`
   + `clients/NDC/research-brief-ploteo.yaml`.
3. Gate on `icp_fit` (strong/medium) → email waterfall (Clay credits) on survivors only.
4. Campaign ideation by segment over the leads that have an email.

> Cost order: research is cheap (GPT) and runs on everyone; the email is the expensive
> Clay credit and runs last, only on leads the `icp_fit` gate passes. The formal /100
> rubric below is the reference logic; the live gate is the `icp_fit` verdict.

---

## Next Steps

1. **Build Tier 1 list (target: 30–50 accounts):** Pull exhibitor lists from the next 2 major Argentine trade shows (check Expo Rural, ExpoEFI, Alimentaria calendars). Cross-reference with LinkedIn to find the Marketing Manager at each exhibiting company. These are your hottest leads — they have a fixed event deadline and an active budget.

2. **Build Tier 2 list (target: 100–200 accounts):** Use LinkedIn Sales Navigator with filters: Industry = Logistics + Food & Bev + Healthcare, Employees = 20–300, Argentina. Filter for companies with active event/fleet presence on their LinkedIn page.

3. **Run `/market tam`** to size the full addressable market and model 12-month pipeline from these tiers.

4. **Run `/market messaging`** to develop the cold email hook and LinkedIn opener for the Marketing Manager persona — the trigger-led angle ("I saw you're exhibiting at [Expo] in [Month]") is the strongest entry point.

5. **Run `/market competitors`** to map who else is competing for this brief in the Argentine visual communications market and sharpen NDC's differentiation angle.
