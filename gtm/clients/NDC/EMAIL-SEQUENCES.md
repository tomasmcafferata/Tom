# Email Sequences — Outbound GTM
**Company / Product:** NDC Communication Group — enedece.com.ar
**Date:** March 27, 2026
**GTM Motion:** Outbound — Español rioplatense (Argentina)
**Tool:** Instantly.ai (o Smartlead)
**Inputs:** MESSAGING.md, ABM.md, POSITIONING.md, ICP.md

---

## Configuración General de Sequences

```
CONFIGURACIÓN TÉCNICA
======================
Sending account:    Dominio alternativo calentado (ej: info@ndc-comunicacion.com.ar)
                    NUNCA usar el dominio principal enedece.com.ar para outbound
Warmup:             Mínimo 3 semanas antes de lanzar (Instantly warmup automático)
Volumen inicial:    20–30 emails/día/bandeja (escalar a 50–80 en semana 3+)
Tracking:           Apertura y clicks activados
Reply detection:    Activado — sacar de secuencia al responder
Zona horaria:       America/Argentina/Buenos_Aires
Horario de envío:   Martes–Jueves, 9:00–11:00 ARS
Days between steps: Ver cada secuencia
```

---

## SECUENCIA 1: FERIAS-T1 — Expositor Confirmado

**Trigger:** La empresa aparece como expositor en una feria específica
**Persona:** Gerente / Responsable de Marketing / Coordinadora de Eventos
**Duración:** 12 días, 4 pasos
**Objetivo:** Conseguir reunión / llamada antes del cierre de producción

---

### Email 1 — Día 1

```
Subject: {{first_name}}, el stand de {{company}} para {{feria_nombre}}

---

{{first_name}}, vi que {{company}} va a estar en {{feria_nombre}} en {{feria_mes}}.

¿Ya tienen un proveedor para el stand completo — render, producción e instalación?

En NDC hacemos todo en casa: diseño, impresión, construcción y montaje.
Sin terceros. El stand sale como el render porque el mismo equipo lo diseña,
lo imprime y lo instala el día del evento.

¿Vale la pena charlar 15 minutos esta semana?

Saludos,
[NOMBRE]
NDC Communication Group
📞 11 5263-3258
enedece.com.ar

---
[VARIABLES]
{{first_name}}      = nombre del contacto
{{company}}         = nombre de la empresa
{{feria_nombre}}    = ej. "Expo Rural", "ExpoEFI", "Alimentaria"
{{feria_mes}}       = ej. "julio", "agosto"
```

---

### Email 2 — Día 4 (si no responde)

```
Subject: Re: {{first_name}}, el stand de {{company}} para {{feria_nombre}}

---

{{first_name}}, por si no llegó mi email anterior.

Trabajo con responsables de marketing de empresas como {{company}} que exponen en
{{feria_nombre}} y prefieren tener un solo proveedor para todo: diseño, producción,
impresión, logística e instalación.

La diferencia que más valoran nuestros clientes: como no tercerizamos nada,
el stand sale exactamente como el render que aprobaron — sin sorpresas el día del montaje.

¿Tienen un momento esta semana para una llamada rápida?

[NOMBRE]
NDC Communication Group
📞 11 5263-3258
```

*Nota Instantly: Si disponés de foto de un stand producido para una industria similar, adjuntarla aquí como imagen inline o link a galería NDC.*

---

### Email 3 — Día 7 (urgencia de plazos)

```
Subject: {{feria_nombre}}: los tiempos de producción se están por apretar

---

{{first_name}},

Una cosa práctica: para {{feria_nombre}}, los tiempos de producción cómodos
cierran aproximadamente {{fecha_limite_produccion}}.

Si todavía están evaluando opciones para el stand, esta semana puedo armarte
una propuesta con números reales para que tengas algo concreto antes de decidir.

¿Me pasás algunos datos del stand que están pensando? (metros cuadrados aproximados,
si necesitan impresión gráfica, si requieren montaje y desmontaje)

[NOMBRE]
NDC Communication Group
📞 11 5263-3258

---
[VARIABLES]
{{fecha_limite_produccion}} = fecha aproximada = 5–6 semanas antes de la feria
```

---

### Email 4 — Día 12 (cierre suave)

```
Subject: Última consulta sobre {{feria_nombre}}, {{first_name}}

---

{{first_name}}, última vez que te escribo por {{feria_nombre}}.

Si ya lo tienen cubierto con otro proveedor, perfecto — guardá NDC para la próxima
temporada de ferias.

Si todavía están evaluando, puedo tener una propuesta lista en 48 horas.
Solo necesito saber: metros cuadrados del stand, nombre de la feria y fecha.

[NOMBRE]
NDC Communication Group
📞 11 5263-3258
enedece.com.ar
```

---

## SECUENCIA 2: FERIAS-T2 — Industria Activa, Sin Trigger Específico

**Trigger:** Empresa del verticales correcto (alimentos, farma, logística, retail, automotriz), sin feria específica identificada todavía
**Persona:** Gerente / Responsable de Marketing
**Duración:** 21 días, 3 pasos
**Objetivo:** Generar radar activo — que respondan cuando llegue el trigger

---

### Email 1 — Día 1

```
Subject: Stands para empresas de {{industria}} — NDC

---

{{first_name}},

Trabajo con empresas de {{industria}} en Argentina que exponen en ferias
como {{feria_industria_ejemplo}} y necesitan un proveedor que se encargue
de todo: diseño, producción, impresión e instalación del stand.

En NDC lo hacemos en casa — sin terceros — para que el stand llegue al evento
exactamente como el render, y vos puedas llegar al evento sin haber perdido
una semana coordinando proveedores.

¿Esto les es relevante para alguna feria de los próximos meses?

[NOMBRE]
NDC Communication Group
📞 11 5263-3258
enedece.com.ar

---
[VARIABLES]
{{industria}}               = ej. "la industria alimentaria", "logística y transporte",
                              "el sector farmacéutico", "retail"
{{feria_industria_ejemplo}} = ej. "Alimentaria", "Expo Logística", "Expofarmacia", "Retail Day"
```

---

### Email 2 — Día 10

```
Subject: {{company}}: stands, flota y locales — todo en un solo proveedor

---

{{first_name}}, por si no llegó mi email anterior.

Una cosa que diferencia a NDC de otras empresas de comunicación visual:
no solo hacemos stands para ferias.

El mismo equipo se encarga de ploteo vehicular, cartelería y restyling de locales.
Muchas empresas de {{industria}} nos contactan para la feria y terminan
trabajando con nosotros para su flota y sus sucursales también.

¿Tienen alguna feria o evento en el horizonte para el que valga la pena charlar?

[NOMBRE]
NDC
```

---

### Email 3 — Día 21

```
Subject: ¿Ferias 2026 de {{company}}?

---

{{first_name}}, última vez que te escribo.

¿Tienen alguna feria o evento en la agenda para el segundo semestre 2026
donde podamos ser útiles?

Si me decís que no están planeando nada, te borro de mi lista.
Si hay algo en el horizonte, con gusto armamos una propuesta.

[NOMBRE]
NDC
📞 11 5263-3258
```

---

## SECUENCIA 3: FLOTA-LOGISTICA — Empresa de Transporte / Logística

**Trigger:** Empresa de logística/transporte/distribución con flota visible, 20–300 empleados
**Persona:** Gerente de Marketing / Gerente Comercial / CEO (en empresas chicas)
**Duración:** 21 días, 4 pasos
**Objetivo:** Propuesta de contrato de ploteo de flota

---

### Email 1 — Día 1

```
Subject: La flota de {{company}} — imagen en todos los vehículos

---

{{first_name}},

Para empresas de {{tipo_empresa}} como {{company}}, cada vehículo en la calle
es un punto de contacto con clientes y prospectos.

En NDC nos encargamos del ploteo vehicular completo para flotas corporativas:
diseño, impresión en plotters de gran formato, y aplicación en los vehículos —
para que todos los camiones y camionetas salgan iguales y representen bien
la imagen de la empresa.

¿Tienen el ploteo de la flota resuelto, o están evaluando opciones?

[NOMBRE]
NDC Communication Group
📞 11 5263-3258
enedece.com.ar

---
[VARIABLES]
{{tipo_empresa}} = ej. "logística", "transporte", "distribución"
```

---

### Email 2 — Día 7

```
Subject: Re: flota {{company}} — proceso completo

---

{{first_name}}, por si no llegó mi email.

Lo que diferencia a NDC en ploteo vehicular es el proceso integrado:
el mismo equipo que diseña la identidad visual de la flota la imprime
en nuestra planta propia y la aplica sobre los vehículos.

No tercerizamos ninguna etapa — eso significa que todos los vehículos
quedan exactamente iguales, con los colores del manual de marca.

¿Cuántos vehículos tiene actualmente la flota de {{company}}?
Con ese dato puedo mandarte un presupuesto orientativo.

[NOMBRE]
NDC
📞 11 5263-3258
```

---

### Email 3 — Día 14 (oferta de entrada)

```
Subject: Piloto de ploteo para {{company}} — 3 vehículos

---

{{first_name}},

Una propuesta concreta: hacemos un piloto con 3 vehículos de la flota de {{company}}
para que puedan ver la calidad del trabajo antes de comprometer toda la flota.

Diseño, impresión y aplicación — en nuestra planta en Florida, Buenos Aires.

¿Tiene sentido coordinar una visita al taller para ver los equipos y hablar
de lo que necesitan?

[NOMBRE]
NDC
📞 11 5263-3258
enedece.com.ar
```

---

### Email 4 — Día 21

```
Subject: Última consulta sobre la flota de {{company}}

---

{{first_name}}, última vez que te escribo sobre esto.

Si el ploteo de la flota ya está resuelto con otro proveedor, no hay problema —
guardá NDC para cuando renueven.

Si están evaluando opciones o van a incorporar vehículos nuevos próximamente,
estamos disponibles para una reunión rápida.

[NOMBRE]
NDC
📞 11 5263-3258
```

---

## SECUENCIA 4: RESTYLING — Nueva Apertura / Renovación de Imagen

**Trigger:** Anuncio de nueva apertura de local, nueva sucursal, o rebrand en LinkedIn/prensa
**Persona:** Gerente de Marketing / Director Comercial
**Duración:** 14 días, 3 pasos
**Objetivo:** Propuesta de cartelería + restyling

---

### Email 1 — Día 1

```
Subject: Nueva apertura de {{company}} — cartelería e imagen

---

{{first_name}},

Vi el anuncio de la nueva apertura de {{company}} en {{ubicacion}}.
Felicitaciones — siempre es una buena señal.

Cuando se abre un local nuevo o se renueva imagen, lo más difícil suele ser
coordinar diseño, producción de cartelería, corpóreos, señalética e instalación
— todo en tiempo y forma antes de la apertura.

En NDC lo hacemos en casa: diseño, impresión y colocación, para una sola sucursal
o para un rollout de toda la cadena.

¿Tienen ya resuelto el proveedor para la señalética e imagen del nuevo local?

[NOMBRE]
NDC Communication Group
📞 11 5263-3258
enedece.com.ar

---
[VARIABLES]
{{ubicacion}} = ej. "Palermo", "Rosario", "el centro"
```

---

### Email 2 — Día 7

```
Subject: Re: apertura {{company}} — propuesta de cartelería

---

{{first_name}}, por si no llegó mi mensaje anterior.

Trabajamos con cadenas y marcas en Buenos Aires en la producción de imagen
para nuevas aperturas: marquesinas, corpóreos, señalética interior, vinilos
y toda la gráfica del local.

Si están pensando en más aperturas o en renovar la imagen de sucursales existentes,
el hecho de tener todo en un solo proveedor simplifica mucho la coordinación
y garantiza consistencia de marca en todos los locales.

¿Vale la pena una llamada de 15 minutos para ver si hay fit?

[NOMBRE]
NDC
📞 11 5263-3258
```

---

### Email 3 — Día 14

```
Subject: {{company}} — última consulta

---

{{first_name}}, última vez que te escribo.

Si ya tienen resuelto el proveedor de imagen y cartelería, perfecto.

Si están por abrir más sucursales o renovar imagen y quieren explorar opciones,
estaré disponible para una reunión esta semana o la próxima.

[NOMBRE]
NDC
📞 11 5263-3258
enedece.com.ar
```

---

## SECUENCIA 5: NUEVO-MKT — Nuevo Responsable de Marketing

**Trigger:** LinkedIn muestra que el contacto lleva menos de 6 meses en el cargo
**Persona:** Nuevo Gerente / Responsable de Marketing
**Duración:** 14 días, 3 pasos
**Objetivo:** Posicionar a NDC como el proveedor de referencia desde el inicio

---

### Email 1 — Día 1

```
Subject: {{first_name}}, proveedores de comunicación visual para {{company}}

---

{{first_name}}, vi que arrancaste hace poco como {{cargo}} en {{company}}.
Felicitaciones por el nuevo rol.

Una de las primeras cosas que los responsables de marketing definen es el
proveedor para la comunicación visual física: stands para ferias, ploteo
de flota, cartelería y eventos corporativos.

En NDC hacemos todo eso en casa — sin terceros — para que tengas un solo
interlocutor para toda la comunicación visual de {{company}}.

¿Tiene sentido charlar 15 minutos para que te cuente cómo trabajamos?

[NOMBRE]
NDC Communication Group
📞 11 5263-3258
enedece.com.ar

---
[VARIABLES]
{{cargo}} = ej. "Gerente de Marketing", "Responsable de Eventos"
```

---

### Email 2 — Día 7

```
Subject: Re: NDC para {{company}} — stands, flota y más

---

{{first_name}}, por si no llegó mi email.

En resumen lo que hacemos en NDC:
✓ Stands completos para ferias y exposiciones (diseño, producción, instalación)
✓ Ploteo vehicular para flotas corporativas
✓ Cartelería y restyling de locales y oficinas
✓ Producción de eventos corporativos

Todo en casa, sin terceros.

Si tienen alguna feria, evento o proyecto de imagen en los próximos meses,
vale la pena que lo hablemos antes de que empiece la producción.

¿Cuándo te queda bien una llamada de 15 minutos?

[NOMBRE]
NDC
📞 11 5263-3258
```

---

### Email 3 — Día 14

```
Subject: Último mensaje, {{first_name}}

---

{{first_name}}, entiendo que los primeros meses en un nuevo rol son intensos.

Cuando tengas un momento — y antes de la próxima feria o evento de {{company}} —
con gusto te cuento cómo trabajamos.

Solo respondé este email con "me interesa" y coordinamos.

[NOMBRE]
NDC
📞 11 5263-3258
```

---

## SECUENCIA 6: NURTURE — Post-Evento / No-Respuesta

**Trigger:** Contacto que no respondió a secuencia activa, o primer contacto post-evento
**Persona:** Cualquiera del ICP
**Duración:** 30 días, 2 pasos
**Objetivo:** Mantener radar, convertir en temporada siguiente

---

### Email 1 — Día 1

```
Subject: ¿Cómo les fue en {{feria_nombre}}, {{first_name}}?

---

{{first_name}}, ¿cómo les fue en {{feria_nombre}}?

Espero que el stand haya salido bien y que el evento haya valido la pena.

Para la próxima temporada de ferias, si quieren probar con un solo proveedor
para todo — diseño, producción, instalación — nos encantaría ser esa opción.

¿Cuándo empiezan a planificar los eventos del segundo semestre?

[NOMBRE]
NDC Communication Group
📞 11 5263-3258
```

---

### Email 2 — Día 30

```
Subject: {{company}}: próximas ferias 2026

---

{{first_name}}, ya estamos en la temporada de planificación para el segundo
semestre de ferias.

Si {{company}} va a exponer en algún evento entre julio y diciembre,
es buen momento para hablar antes de que los calendarios se llenen.

¿Tienen algo en agenda?

[NOMBRE]
NDC
📞 11 5263-3258
enedece.com.ar
```

---

## Configuración en Instantly — Resumen de Sequences

```
NOMBRE EN INSTANTLY         TRIGGER             STEPS   DÍAS    VOLUMEN
─────────────────────────────────────────────────────────────────────────
NDC-FERIAS-T1               Expositor activo    4       12      Tier 1 — manual
NDC-FERIAS-T2               Industria activa    3       21      Tier 2 — automatizado
NDC-FLOTA-LOGISTICA         Empresa transporte  4       21      Tier 2 — automatizado
NDC-RESTYLING               Nueva apertura      3       14      Tier 1 — semi-manual
NDC-NUEVO-MKT               Nuevo en cargo      3       14      Tier 1 — semi-manual
NDC-NURTURE                 Post-evento/no resp 2       30      Todos — automatizado
```

---

## Variables Globales a Definir en Instantly

```
{{first_name}}              Nombre del contacto (siempre)
{{company}}                 Nombre de la empresa
{{cargo}}                   Cargo del contacto
{{feria_nombre}}            Nombre de la feria específica
{{feria_mes}}               Mes de la feria
{{feria_industria_ejemplo}} Ejemplo de feria para la industria del prospecto
{{industria}}               Industria del prospecto (en español)
{{tipo_empresa}}            Tipo de empresa (logística, transporte, etc.)
{{ubicacion}}               Ciudad o zona de la nueva apertura
{{fecha_limite_produccion}} Fecha límite de producción (calcular por feria)
```

---

## Reglas de Operación

```
LO QUE SIEMPRE HAY QUE HACER:
  ✓ Personalizar {{feria_nombre}} y {{feria_mes}} para Tier 1 — nunca mandar genérico
  ✓ Sacar a los que responden de la secuencia inmediatamente
  ✓ Responder manualmente en máximo 2 horas a cualquier respuesta positiva
  ✓ Revisar replies diariamente
  ✓ Trackear en CRM: apertura, respuesta, reunión, propuesta, cierre

LO QUE NUNCA HAY QUE HACER:
  ✗ Mandar desde el dominio principal enedece.com.ar
  ✗ Arrancar sin warmup de al menos 3 semanas
  ✗ Mandar más de 50 emails/día en las primeras 2 semanas
  ✗ Usar "llave en mano" en ningún email
  ✗ Hablar de precio en el email de apertura
  ✗ Copiar y pegar sin revisar los campos de personalización
```

---

## A/B Tests Recomendados (mes 2+)

```
TEST 1 — Subject line con nombre de feria vs. sin nombre:
  A: "{{first_name}}, el stand de {{company}} para Alimentaria"
  B: "Stand completo para ferias — NDC"

TEST 2 — CTA: pregunta abierta vs. oferta de meeting:
  A: "¿Vale la pena charlar 15 minutos esta semana?"
  B: "¿Tenés tiempo el jueves a las 10 para una llamada rápida?"

TEST 3 — Longitud del email:
  A: 3 oraciones (versión actual)
  B: 5 oraciones con caso de éxito incluido

TEST 4 — Firma con número de teléfono vs. sin teléfono:
  A: Firma completa con 📞
  B: Solo nombre + NDC + link a web

Medir: tasa de apertura, tasa de respuesta, respuestas positivas.
Correr cada test con mínimo 100 envíos antes de declarar ganador.
```
