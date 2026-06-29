# Finanzas Corporativas — Curso de Nivelación (Resumen)
> MBA · Prof. Lic. Joel Vaisman (MBA, MFin, FMVA®)
> Doc de referencia. Curso autogestionado (videos + guía resuelta + autoevaluaciones). No entra en el flujo de ClickUp/NotebookLM/Calendar.

---

## 1. Para qué sirve este curso

Es el **piso común** antes de cursar Finanzas Corporativas: que todos sepan **valuar flujos de fondos** (valor tiempo del dinero). Todo lo que viene después de la materia —valuación de empresas, decisiones de inversión, costo de capital— se apoya en esto. Si esto no está sólido, lo demás no cierra.

---

## 2. Condiciones de aprobación (lo que importa)

| Ítem | Detalle |
|---|---|
| **Examen** | Final virtual, 20 preguntas choice / V-F, **40 minutos** |
| **Formato** | Secuencial: si no contestás una, **no podés volver atrás** |
| **Cuándo** | En un día **fuera** de la cursada del MBA |
| **Recuperatorio** | 2 días después si desaprobás o no rendís (si rendís jue/vie → lunes). Sin excepciones por viajes/superposición |
| **Nota** | Aprobás con **4 o más**. Pondera **15%** de la nota final de Finanzas Corporativas |
| **Si no aprobás** | Hay que **retomar el nivelatorio** antes de poder cursar la materia |
| **Consultas** | Foro del curso (canal oficial con el instructor) |

> ⚠️ El formato secuencial sin retroceso premia tener la mecánica automatizada. No es un examen para "pensarlo en el momento": hay que llegar con las fórmulas y los criterios resueltos de antemano.

---

## 3. Convenciones de cálculo (decisivas para no errar)

- **Base por defecto: 30/365** (salvo que el enunciado aclare otra, ej. 30/360).
- **Régimen por defecto: compuesto** (salvo aclaración).
- **Retorno y Costo Financiero son TASAS**, no importes de dinero.
- **TNA con subíndice** (TNA30, TNA60, TNA90) = tasa **nominal** anual cuyo **plazo de capitalización** es ese subíndice en días. Ej.: TNA90 = nominal anual que capitaliza cada 90 días. Hay que pasarla a **tasa efectiva del período** antes de operar.

---

## 4. Mapa de conceptos (4 unidades)

### Unidad 1 — Operaciones esenciales y tasas
- **Capitalización** (llevar al futuro): `VF = VP · (1 + i)^n`
- **Descuento** (traer al presente): `VP = VF / (1 + i)^n`
  - Aplicaciones: descuento de un **CPD** (cheque de pago diferido), de un proyecto de inversión.
- **TNA** (Tasa Nominal Anual) y cómo se "subindica" según el plazo de capitalización.
- **Tasa nominal vs. tasa efectiva**: la nominal es de referencia; la efectiva es la que realmente capitaliza. `i_efectiva_período = TNA · (días_período / base)`.
- **Bases** para tasas efectivas (30/365, 30/360, etc.).
- **Retorno y Costo Financiero** como tasas; **CFT** (Costo Financiero Total) = incluye intereses + impuestos (IVA) + gastos.
- **Ecuación de Fisher** — separa tasa nominal, tasa real e inflación:
  `(1 + i_nominal) = (1 + r_real) · (1 + inflación)` → `r_real = (1+i_nom)/(1+π) − 1`

### Unidad 2 — Régimen Simple y Régimen Compuesto
- **Simple**: el interés se calcula siempre sobre el capital inicial (`VF = VP·(1 + i·n)`).
- **Compuesto**: el interés se capitaliza (interés sobre interés) — el del curso por defecto.
- **Cambio de frecuencia de capitalización**: cómo encontrar la **tasa efectiva equivalente** para otra periodicidad (ej. pasar de capitalizar cada 30 días a cada 90, manteniendo el mismo resultado anual): `(1 + i₁)^(días/d₁) = (1 + i₂)^(días/d₂)`.

### Unidad 3 — Valuación de Rentas
- **Renta / anualidad**: corriente de pagos en el tiempo.
- **Rentas constantes (finitas)**: pagos iguales. VA de anualidad inmediata vs. **diferida** (primer pago en t>1). Incluye el **sistema francés** (préstamo con cuota constante).
  `VA = C · [1 − (1+i)^(−n)] / i`
- **Rentas variables**: pagos que crecen a una tasa `g`.
- **Rentas perpetuas (perpetuidades)**:
  - Constante: `VA = C / i`
  - Creciente (Gordon): `VA = C / (i − g)`  (requiere `i > g`)

### Unidad 4 — Criterios de Decisión de Inversión
- **VAN** (Valor Actual Neto): `VAN = −I₀ + Σ FFₜ / (1+k)^t`
  - **VAN > 0 → genera valor → conviene.** VAN < 0 → destruye valor.
- **TIR** (Tasa Interna de Retorno): la tasa `k` que hace `VAN = 0`.
  - **TIR > tasa exigida → conviene.**
  - Entre proyectos **mutuamente excluyentes**: si ambos superan la tasa exigida, se elige el de **mayor TIR**.

---

## 5. Guía de ejercicios — índice rápido (con respuestas)

| # | Tema | Resultado |
|---|---|---|
| 1 | Interés de cupón de bono (8% nominal semestral, base 30/360, VR $500) | $20 |
| 2 | Plazo fijo TNA 25% a 40 días sobre $2.000.000 | $2.054.794,52 |
| 3 | CFT de crédito 90 días (TNA90 50% + IVA 21% s/intereses) | CFT90 = 14,918% |
| 4 | Valor de contado de mercadería (2 cheques, descuento al 60% nom.) | $857.565,99 |
| 5 | Tasa nominal equivalente p/ renovar cada 90 días (desde TNA30 40%) | TNA90 = 41,33% |
| 6 | Tasas efectivas equivalentes (60/120/180/365 días desde TNA45 20%) | — (cálculo) |
| 7 | Cuenta con tramos a distintas tasas + retiro parcial | — (cálculo) |
| 8 | **Retorno real** de acción (Fisher, IPC 2% mensual) | — (cálculo) |
| 9 | Valor Nominal de cheque a descontar (TNA60 45%, 180 días) | $1.238.738,42 |
| 10 | VA de renta constante (5 pagos mensuales de $6.000, i=2%) | VA = $28.280,76 |
| 11 | Cuota sistema francés ($1.000.000, 24 cuotas, 40% nom.) | C = $60.892,18 |
| 12 | VA de renta diferida trimestral (ojo frecuencia de capitalización) | $483.138,18 |
| 13 | Precio de perpetuidad constante ($10.000 anual, 12%) | $83.333,33 |
| 14 | Precio de perpetuidad creciente (g = 3%) | $111.111,11 |
| 15 | VAN y TIR de proyecto (4 flujos, tasa 25%) | VAN $55.008 / TIR 30,56% → conviene |
| 16 | VAN con perpetuidad desde año 4 (tasa 35%) | VAN ($229.492) → destruye valor |
| 17 | VAN con perpetuidad creciente desde año 3 (g=1%, tasa 20%) | VAN $76.206,14 |
| 18 | Elección entre A y B por **TIR** (excluyentes, exigencia 25%) | TIR A 25,31% / TIR B 54,77% → elegir B |

> Cada ejercicio está resuelto en un video de la playlist. Los ejercicios 6, 7 y 8 no traen respuesta en la guía: son buenos candidatos para practicar la mecánica completa.

---

## 6. Playlist (videos por tema)

Acceso: webcampus o `Playlist del curso de nivelación.pdf` (links de YouTube). Estructura:
- **Intro** → Operaciones esenciales y tasas (capitalización, descuento, TNA, bases, retorno/costo, Fisher) → Régimen simple vs. compuesto + cambio de frecuencia → Valuación de rentas (constantes, variables, perpetuas) → Criterios VAN y TIR.

---

## 7. Cómo estudiarlo (sugerido)

1. Mirar los videos de cada unidad en orden y rehacer **a mano** el ejercicio asociado antes de ver la resolución.
2. Armar una **hoja de fórmulas** (capitalización/descuento, equivalencia de tasas, anualidad, perpetuidad, VAN, TIR) — es lo que te salva en el examen secuencial.
3. Hacer las autoevaluaciones choice/V-F de cada unidad para entrenar el formato del final.
4. Dudas → foro del curso.
