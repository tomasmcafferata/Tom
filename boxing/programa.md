# Programa de Estudio de Boxeo

Sistema de estudio de estilos. 2 sesiones por semana (Mar + Mié, 18:00). 3 semanas por boxeador. La rutina completa de cada bloque llega por email al inicio del bloque — buscala con la etiqueta **rutina** en Gmail.

---

## Calendario

| Bloque | Boxeador | Semana | Fechas | Foco |
|--------|----------|--------|--------|------|
| 1 | Dmitry Bivol | S1 | Mar 15 Abr + Mié 16 Abr | Aprendizaje |
| 1 | Dmitry Bivol | S2 | Mar 22 Abr + Mié 23 Abr | Consolidación |
| 1 | Dmitry Bivol | S3 | Mar 29 Abr + Mié 30 Abr | Aplicación libre |
| 2 | Marvin Hagler | S1 | Mar 6 May + Mié 7 May | Aprendizaje |
| 2 | Marvin Hagler | S2 | Mar 13 May + Mié 14 May | Consolidación |
| 2 | Marvin Hagler | S3 | Mar 20 May + Mié 21 May | Aplicación libre |
| 3 | (próximo) | — | — | — |

---

## Boxeadores en el programa

1. **Dmitry Bivol** — Escuela soviética, paso pendular, jab dominante `→ boxing/boxeadores/bivol/`
2. **Marvin Hagler** — Presión inteligente, stalking, combinación con pausa, cuerpo-cabeza `→ boxing/boxeadores/hagler/`

---

## Cómo funciona el sistema

- Cada bloque arranca con un email el lunes de inicio. Etiquetalo **rutina** en Gmail.
- Las dos sesiones de la semana tienen la misma rutina de 12 rounds — la repetición fija los movimientos.
- Las 3 semanas usan la misma rutina. Lo que cambia es el foco mental de cada semana:
  - **Semana 1 — Aprendizaje:** conocer los movimientos, no importa la limpieza
  - **Semana 2 — Consolidación:** los movimientos empiezan a sentirse propios
  - **Semana 3 — Aplicación libre:** olvidarse de los movimientos, pelear y que aparezcan solos
- Al terminar un boxeador, arranca el siguiente con su propio email.

---

## Cómo se crea un bloque nuevo

Cuatro pasos en orden. No saltear ninguno.

---

### Paso 1 — Investigación profunda (Research Prompt)

Abrir `boxing/research-prompt.md`. Reemplazar `[BOXER NAME]` y `[DIVISION]`. Correr en Claude con deep research activo.

El resultado es un documento de 10 secciones:

| Sección | Contenido | Destino |
|---------|-----------|---------|
| §1 Style matrix | Código (ej. O.V.C) + archetype + hybrid tendencies | Email — encabezado |
| §2 Philosophical core | Principio rector + mental model + comportamiento bajo presión | Email — por qué |
| §3 Physical profile | Atributos y sus consecuencias mecánicas | Referencia — no alimenta downstream |
| §4 Footwork | Patrones de movimiento nombrados + mecánica | **Rutina** |
| §5 Punching mechanics | Cadena cinética + analogía física + signature feature | **Rutina** |
| §6 Offensive system | Combinaciones core con estructura de beat + variaciones | **Rutina** |
| §7 Defensive system | Mecanismo primario + counters + comportamiento bajo presión | **Rutina** |
| §8 What to absorb | Principios universales + espectro de accesibilidad | Email — conceptos clave |
| §9 Sparring cues | Triggers de live work + peleas de referencia | Email — peleas + conceptos |
| §10 Structural gaps | Vulnerabilidades y counter entry points | Referencia — no alimenta downstream |

Guardar como `boxing/boxeadores/<nombre>/advanced-analysis.md`.

---

### Paso 2 — Block Config

Extraer del `advanced-analysis.md` los campos necesarios para generar la rutina y el email. Guardar como `boxing/boxeadores/<nombre>/block-config.md`.

**Estructura del archivo:**

```markdown
# Block Config — [Boxer Name]

## Identity
matrix_code: [e.g. O.V.C]
archetype: [e.g. "Outboxer · Volume · Counter"]
governing_principle: "[Una frase — el principio rector del boxeador]"

## Anchor concepts
<!-- De §8: principios universales accesibles para cualquier boxeador.
     3 a 6 conceptos. Sin restricciones de nivel — el sistema se encarga
     de la progresión a través de las semanas, no de filtrar conceptos. -->

1. [Concepto] — [Descripción técnica en 1–2 oraciones. Fuente: §N]
2. [Concepto] — [Descripción técnica en 1–2 oraciones. Fuente: §N]
3. [Concepto] — [Descripción técnica en 1–2 oraciones. Fuente: §N]

## Week mantras
<!-- Una frase por semana. Captura el foco mental de esa semana,
     no una técnica específica. -->

week_1: "[Frase de aprendizaje]"
week_2: "[Frase de consolidación]"
week_3: "[Frase de aplicación libre]"

## Film references
<!-- 3 peleas. Fuente: §6, §7, §9. Para cada una: qué muestra
     del sistema del boxeador y el search string de YouTube. -->

1. [Boxeador] vs [Rival] ([año])
   focus: [Qué muestra esta pelea — 1 oración]
   youtube: "[Search string exacto]"

2. [Boxeador] vs [Rival] ([año])
   focus: [Qué muestra esta pelea — 1 oración]
   youtube: "[Search string exacto]"

3. [Boxeador] vs [Rival] ([año])
   focus: [Qué muestra esta pelea — 1 oración]
   youtube: "[Search string exacto]"

## Por qué
[Párrafo 1 — específico del boxeador: por qué su sistema es valioso estudiar, qué enseña que otros no enseñan]

[Párrafo 2 — opcional: comportamiento bajo presión, contexto histórico, o aprendizaje clave]

## Rutina source
<!-- Secciones del advanced-analysis que alimentan los 12 rounds.
     Siempre §4, §5, §6, §7. No modificar. -->

sections: [4, 5, 6, 7]
```

**Reglas del block-config:**

- Los anchor concepts vienen de §8 — son los principios universales, no una lista exhaustiva de todo lo que hace el boxeador
- Los mantras de semana no describen técnicas — describen el estado mental con el que se entrena esa semana
- Las peleas de referencia vienen de §6, §7 o §9 — priorizá peleas donde el sistema del boxeador se ve en su forma más pura
- El block-config es el único documento que Claude lee para generar la rutina y el email — el advanced-analysis no se vuelve a consultar después de este paso

---

### Paso 3 — Rutina

Usando el `advanced-analysis.md` (solo §4, §5, §6, §7) y el `block-config.md`, generar la rutina de 12 rounds.

**Formato del archivo `rutina.md`:**

```markdown
# Rutina — [Boxer Name]
Bloque [N] · 12 rounds · 3 min trabajo / 1 min descanso
Sombra o bolsa · La misma rutina las 6 sesiones del bloque

---

## Round 1 — [Nombre]
*[Propósito en una oración]*

**Consigna:** [Qué hacer en este round]
**Técnico:** [Mecánica específica a trabajar]
**Táctico:** [Objetivo táctico del round]
**Estratégico:** [Por qué este round importa para el bloque completo]

---

## Round 2 — [Nombre]
...
```

**Progresión de los 12 rounds — estructura en tres tercios:**

| Tercio | Rounds | Orientación |
|--------|--------|-------------|
| Técnico | 1–4 | Mecánica y movimiento — los fundamentos del análisis traducidos a ejercicios |
| Táctico | 5–8 | Aplicación situacional — combinaciones, setups, respuestas a situaciones de pelea |
| Estratégico | 9–12 | Gestión del fight — defensa activa, tempo, integración, round 12 libre |

El contenido específico de cada round surge libremente del análisis del boxeador (§4–§7). La tabla orienta la progresión, no prescribe el contenido. El nivel asumido es intermedio-avanzado; los conceptos avanzados del análisis entran en todo el bloque, no solo en los rounds del medio.

---

### Paso 4 — Draft de Gmail

Dos sub-pasos separados. El primero genera el HTML localmente; el segundo lo envía a Gmail. Separarlos evita el error de latencia que ocurre cuando Claude genera HTML largo y llama a la API en el mismo paso.

#### Paso 4a — Generar HTML

Correr el script desde la raíz del repo:

```bash
python3 boxing/generate-email-draft.py boxing/boxeadores/<nombre>
```

El script lee `block-config.md` y `rutina.md`, extrae las fechas del calendario de `programa.md`, y escribe `email-draft.html` en la carpeta del boxeador. Revisar el archivo antes de continuar.

#### Paso 4b — Crear borrador en Gmail

Correr el script desde la raíz del repo:

```bash
python3 boxing/send-to-gmail.py boxing/boxeadores/<nombre>
```

El script lee `email-draft.html`, llama a la API de Gmail directamente vía HTTP, y crea el borrador. Si la llamada falla, el HTML ya está guardado — solo reintentar este sub-paso.

**Asunto:** `🥊 Programa [Boxeador] — 3 semanas | 6 sesiones`

**Estructura del email — qué sección del análisis alimenta cada parte:**

| Parte del email | Fuente |
|-----------------|--------|
| Por qué estudiamos a [Boxeador] | block-config: sección `## Por qué` |
| Conceptos clave del bloque | block-config: `anchor_concepts` |
| Cómo funciona la rutina | Texto fijo del sistema |
| Calendario del bloque | Fechas del calendario principal |
| Peleas recomendadas | block-config: `film_references` |
| Los 12 rounds | `rutina.md` completa |

**Estilos base HTML** (inline styles, compatibles con Gmail):

- Fuente: `font-family: Georgia, serif; color: #1a1a1a;`
- Contenedor: `max-width: 600px; margin: 0 auto; padding: 32px 24px;`
- Separador: `<hr style="border: none; border-top: 1px solid #d0d0d0; margin: 28px 0;">`
- Título principal `<h1>`: `font-size: 26px; font-weight: bold; margin: 0 0 4px 0;`
- Subtítulo: `font-size: 14px; color: #666; margin: 0 0 32px 0;`
- Encabezado de sección `<h2>`: `font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.08em; color: #888; margin: 0 0 16px 0;`
- Párrafo `<p>`: `font-size: 15px; line-height: 1.65; margin: 0 0 14px 0;`
- Título de concepto / round `<h3>`: `font-size: 15px; font-weight: bold; margin: 20px 0 6px 0;`
- Label de fila `<strong>`: `font-size: 14px;`
- Texto de fila `<span>`: `font-size: 14px; color: #333;`
- Mantra de semana: `font-style: italic; color: #555; margin: 4px 0 0 0;`
- Footer: `font-size: 12px; color: #aaa; text-align: center; margin-top: 40px;`

**Estructura HTML del email:**

```html
<div style="font-family: Georgia, serif; color: #1a1a1a; max-width: 600px; margin: 0 auto; padding: 32px 24px;">

  <h1 style="font-size: 26px; font-weight: bold; margin: 0 0 4px 0;">🥊 Programa [Boxeador]</h1>
  <p style="font-size: 14px; color: #666; margin: 0 0 32px 0;">3 semanas · 6 sesiones · Martes y Miércoles 18:00</p>

  <hr style="border: none; border-top: 1px solid #d0d0d0; margin: 28px 0;">

  <h2 style="font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.08em; color: #888; margin: 0 0 16px 0;">Por qué estudiamos a [Boxeador]</h2>
  <p style="font-size: 15px; line-height: 1.65; margin: 0 0 14px 0;">[Párrafo 1 — del governing_principle + §2]</p>
  <p style="font-size: 15px; line-height: 1.65; margin: 0;">[Párrafo 2]</p>

  <hr style="border: none; border-top: 1px solid #d0d0d0; margin: 28px 0;">

  <h2 style="font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.08em; color: #888; margin: 0 0 16px 0;">Conceptos clave del bloque</h2>

  <h3 style="font-size: 15px; font-weight: bold; margin: 20px 0 6px 0;">1. [Concepto]</h3>
  <p style="font-size: 15px; line-height: 1.65; margin: 0 0 14px 0;">[Descripción técnica]</p>
  <!-- Repetir por cada anchor concept -->

  <hr style="border: none; border-top: 1px solid #d0d0d0; margin: 28px 0;">

  <h2 style="font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.08em; color: #888; margin: 0 0 16px 0;">Cómo funciona la rutina</h2>
  <p style="font-size: 15px; line-height: 1.65; margin: 0;">12 rounds, 3 min trabajo / 1 min descanso. Sombra o bolsa. La misma rutina las 6 sesiones del bloque — lo que cambia es cómo la vivís cada semana.</p>

  <hr style="border: none; border-top: 1px solid #d0d0d0; margin: 28px 0;">

  <h2 style="font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.08em; color: #888; margin: 0 0 16px 0;">Calendario del bloque</h2>

  <h3 style="font-size: 15px; font-weight: bold; margin: 20px 0 2px 0;">Semana 1 — Aprendizaje</h3>
  <p style="font-size: 14px; color: #555; margin: 0 0 4px 0;">Mar [fecha] + Mié [fecha], 18:00</p>
  <p style="font-size: 14px; font-style: italic; color: #555; margin: 0 0 20px 0;">[week_1 mantra]</p>

  <h3 style="font-size: 15px; font-weight: bold; margin: 0 0 2px 0;">Semana 2 — Consolidación</h3>
  <p style="font-size: 14px; color: #555; margin: 0 0 4px 0;">Mar [fecha] + Mié [fecha], 18:00</p>
  <p style="font-size: 14px; font-style: italic; color: #555; margin: 0 0 20px 0;">[week_2 mantra]</p>

  <h3 style="font-size: 15px; font-weight: bold; margin: 0 0 2px 0;">Semana 3 — Aplicación libre</h3>
  <p style="font-size: 14px; color: #555; margin: 0 0 4px 0;">Mar [fecha] + Mié [fecha], 18:00</p>
  <p style="font-size: 14px; font-style: italic; color: #555; margin: 0;">[week_3 mantra]</p>

  <hr style="border: none; border-top: 1px solid #d0d0d0; margin: 28px 0;">

  <h2 style="font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.08em; color: #888; margin: 0 0 16px 0;">Peleas recomendadas</h2>

  <h3 style="font-size: 15px; font-weight: bold; margin: 20px 0 6px 0;">1. [Boxeador] vs [Rival] — [año]</h3>
  <p style="font-size: 15px; line-height: 1.65; margin: 0 0 6px 0;">[focus]</p>
  <p style="font-size: 14px; color: #555; margin: 0 0 16px 0;">🔍 <em>Buscar en YouTube: [youtube search string]</em></p>
  <!-- Repetir para peleas 2 y 3 -->

  <hr style="border: none; border-top: 1px solid #d0d0d0; margin: 28px 0;">

  <h2 style="font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.08em; color: #888; margin: 0 0 16px 0;">Los 12 Rounds</h2>
  <p style="font-size: 14px; color: #555; margin: 0 0 24px 0;">3 min trabajo / 1 min descanso · Sombra o bolsa · La misma rutina las 6 sesiones del bloque</p>

  <h3 style="font-size: 15px; font-weight: bold; margin: 24px 0 8px 0;">Round 1 — [Nombre]</h3>
  <p style="font-size: 14px; line-height: 1.6; margin: 0 0 4px 0;"><strong>Consigna:</strong> <span style="color: #333;">[qué hacer]</span></p>
  <p style="font-size: 14px; line-height: 1.6; margin: 0 0 4px 0;"><strong>Técnico:</strong> <span style="color: #333;">[mecánica específica]</span></p>
  <p style="font-size: 14px; line-height: 1.6; margin: 0 0 4px 0;"><strong>Táctico:</strong> <span style="color: #333;">[objetivo táctico]</span></p>
  <p style="font-size: 14px; line-height: 1.6; margin: 0 0 20px 0;"><strong>Estratégico:</strong> <span style="color: #333;">[objetivo del bloque]</span></p>
  <!-- Repetir rounds 2–12 -->

  <hr style="border: none; border-top: 1px solid #d0d0d0; margin: 28px 0;">

  <p style="font-size: 12px; color: #aaa; text-align: center; margin: 0;">Sistema de estudio de boxeo · Bloque [N] · tomasmcafferata/tom</p>

</div>
```
