# GTM System — Development Roadmap

## Visión

Sistema GTM outbound que corre casi solo. Tomás hace direccionamiento estratégico y QA.
El sistema maneja: investigación → lista → campaña → replies → conversión → reporte.

---

## Estado actual del pipeline

```
[INVESTIGACIÓN]  →  [LISTA]  →  [CAMPAÑA]  →  [REPLIES]  →  [CONVERSIÓN]  →  [REPORTE]
  ✅ Cubierto        ❌ Manual   ➕ Instantly   ✅ Cubierto    ❌ Manual        ❌ Manual
```

---

## Módulos a desarrollar

### M1 — Monitoreo de campaña
**Problema:** Instantly corre solo pero es una caja negra. No sabés si algo está mal hasta que ya es tarde.  
**Solución:** Daily digest de métricas via Instantly API → Slack.

**Alcance:**
- [ ] Conectar Instantly API (métricas de campaña: open rate, reply rate, bounce rate)
- [ ] Detectar campañas pausadas o con problemas de deliverability
- [ ] Enviar resumen diario a Slack (por cliente)
- [ ] Alerta inmediata si bounce rate supera umbral configurable

**Entradas:** Instantly API  
**Salidas:** Mensaje Slack con métricas del día  
**Esfuerzo estimado:** Bajo (1-2 días)  
**Prioridad:** Alta

---

### M2 — Weekly digest + reporting automático
**Problema:** El reporte al cliente es manual. No hay visibilidad regular de resultados.  
**Solución:** Cron job semanal que compila métricas y genera reporte por cliente.

**Alcance:**
- [ ] Script que lee el CRM (Google Sheets) + Instantly API
- [ ] Genera resumen semanal: replies recibidos, clasificaciones, emails enviados, meetings
- [ ] Genera resumen mensual compilado (usando `/market report`)
- [ ] Envío automático al cliente (Gmail) o guardado en carpeta del cliente
- [ ] Dashboard de estado por cliente en Google Sheets

**Entradas:** Google Sheets CRM, Instantly API  
**Salidas:** Email al cliente, archivo en `clients/<nombre>/MARKETING-REPORT.md`  
**Esfuerzo estimado:** Medio (2-3 días)  
**Prioridad:** Alta

---

### M3 — Estado operativo del cliente (dashboard)
**Problema:** Sin visibilidad de en qué etapa está cada cliente. Crítico con 3+ clientes.  
**Solución:** Hoja "Status" en Google Sheets con pipeline stage por cliente.

**Pipeline stages:**
```
Onboarding → Strategy Docs → List Building → Campaign Active → Replies → Meeting → Closed
```

**Alcance:**
- [ ] Hoja "Clients" en Google Sheets con columnas: cliente, stage, fecha inicio, próxima acción, responsable
- [ ] Auto-actualización de stage cuando hay eventos (campaña activa, meeting booked, etc.)
- [ ] Vista resumida en Slack (comando `/status` o mensaje diario)

**Entradas:** Eventos del sistema (campaigns, CRM)  
**Salidas:** Hoja Sheets, mensaje Slack  
**Esfuerzo estimado:** Bajo-medio (1-2 días)  
**Prioridad:** Alta

---

### M4 — List building semi-automático
**Problema:** ICP.md → Apollo → Clay → Instantly es 2-3 horas manuales por cliente, cada ciclo.  
**Solución:** Automatizar los puentes entre herramientas. Entrada manual sigue siendo válida.

**Alcance (fase 1 — puentes):**
- [ ] Script que toma CSV exportado de Apollo y lo sube directamente a Instantly via API
- [ ] Integración con Clay webhook para enriquecimiento en cadena antes del upload
- [ ] Deduplicación automática contra leads ya procesados en el CRM

**Alcance (fase 2 — búsqueda automática):**
- [ ] Apollo API: construir query desde criterios del ICP.md (industria, tamaño, cargo)
- [ ] Output directo a pipeline de enriquecimiento

**Entradas:** `clients/<nombre>/ICP.md`, CSV de Apollo, Clay  
**Salidas:** Lista subida a Instantly  
**Esfuerzo estimado:** Fase 1: medio (2-3 días) / Fase 2: alto (1 semana+)  
**Prioridad:** Media (fase 1) / Baja (fase 2)

---

### M5 — Conversión post-reply positivo
**Problema:** Cuando un lead dice "interested" o bookea una reunión, el sistema no hace nada más. Caída libre.  
**Solución:** Flujos automáticos según el evento de conversión.

**Alcance:**
- [ ] Si clasificación = `interested`: auto-draft de propuesta de call + envío a Slack para aprobación
- [ ] Calendly webhook → actualizar CRM a "Meeting Booked" automáticamente
- [ ] Trigger automático de `/market enablement` cuando el status llega a "Meeting Booked"
- [ ] Template de follow-up post-call generado 24hs después del meeting
- [ ] Si clasificación = `question`: respuesta usa contexto del cliente para resolver objeción específica

**Entradas:** Clasificación del reply, Calendly webhook, CRM  
**Salidas:** Drafts en Slack, CRM actualizado, `SALES-ENABLEMENT.md` generado  
**Esfuerzo estimado:** Medio-alto (3-4 días)  
**Prioridad:** Media

---

### M6 — Feedback loop estratégico
**Problema:** El sistema ejecuta pero no aprende. Si el 40% de replies preguntan lo mismo, nadie actualiza el MESSAGING.md.  
**Solución:** Análisis periódico de patrones en replies → sugerencias de mejora.

**Alcance:**
- [ ] Script semanal que analiza clasificaciones del CRM (patrones de objeciones, preguntas frecuentes)
- [ ] Genera sugerencias de mejora para `MESSAGING.md` y `EMAIL-SEQUENCES.md`
- [ ] Envía resumen a Slack: "Esta semana el 35% de replies preguntó por precio. Considerar ajustar secuencia 3."
- [ ] (Opcional) Auto-propone variantes de subject lines basadas en reply rate

**Entradas:** Google Sheets CRM (columna classification + reply snippets)  
**Salidas:** Reporte de patrones en Slack, sugerencias de edición en docs  
**Esfuerzo estimado:** Medio (2-3 días)  
**Prioridad:** Baja-media (valor compuesto a largo plazo)

---

### M7 — Onboarding de nuevo cliente
**Problema:** Añadir un cliente nuevo requiere tocar 4-5 lugares manualmente (config.yaml, Sheets, Slack, Instantly, carpeta de archivos). Propenso a errores.  
**Solución:** Script de onboarding que hace el setup completo desde un solo comando.

**Alcance:**
- [ ] Script `onboard_client.py <nombre> <url> <inbox_email>`
- [ ] Crea carpeta `clients/<nombre>/`
- [ ] Agrega el cliente al `config.yaml` del sistema de respuestas
- [ ] Crea pestaña del cliente en Google Sheets CRM
- [ ] Crea canal Slack o configura notificaciones por cliente
- [ ] Checklist de pasos manuales restantes (Instantly campaign, Gmail OAuth)

**Entradas:** Nombre, URL, inbox email  
**Salidas:** Setup completo + checklist de lo que falta  
**Esfuerzo estimado:** Medio (2-3 días)  
**Prioridad:** Media (escala con número de clientes)

---

### M8 — Infraestructura del sistema de respuestas *(ya identificado)*
**Problema:** El script de respuestas puede caerse silenciosamente. Sin alertas ni logs persistentes.  
**Solución:** Operaciones básicas de sistema.

**Alcance:**
- [ ] Process manager (systemd o supervisor) para reinicio automático
- [ ] Logging a archivo con rotación
- [ ] Heartbeat → alerta Slack si el proceso para
- [ ] Backup de `state.json`
- [ ] Auto-manejo de bounces (sin draft, solo archivar)
- [ ] Auto-manejo de OOO (extraer fecha de retorno, programar follow-up)
- [ ] Update de status post-envío → "Waiting Reply"

**Entradas:** Proceso existente (`main.py`)  
**Salidas:** Sistema más robusto  
**Esfuerzo estimado:** Bajo-medio (1-2 días)  
**Prioridad:** Alta

---

## Secuencia de desarrollo recomendada

```
FASE 1 — Visibilidad y estabilidad (2-3 semanas)
  M8  Infraestructura del sistema de respuestas
  M1  Monitoreo de campaña
  M3  Dashboard de estado del cliente

FASE 2 — Cierre del loop (3-4 semanas)
  M2  Weekly digest + reporting automático
  M5  Conversión post-reply positivo
  M7  Onboarding de nuevo cliente

FASE 3 — Escala y aprendizaje (4-6 semanas)
  M4  List building semi-automático (fase 1: puentes)
  M6  Feedback loop estratégico
  M4  List building automático (fase 2: Apollo API)
```

---

## Dependencias entre módulos

```
M8 (infraestructura)  ──────────────────────────────────────────── base de todo
M1 (monitoreo)        → requiere: Instantly API key configurada
M2 (reporting)        → requiere: M1 + M3 para tener datos completos
M3 (dashboard)        → requiere: CRM funcionando (ya existe)
M4 (list building)    → requiere: M3 para saber cuándo activar
M5 (conversión)       → requiere: M8 (sistema de respuestas estable)
M6 (feedback loop)    → requiere: M2 + datos históricos acumulados
M7 (onboarding)       → requiere: M3 + M8 para saber qué configurar
```

---

## Fuera del alcance (por ahora)

- HubSpot integration (agregar complejidad sin beneficio claro dado el stack actual)
- LinkedIn automation (riesgo de ban, mejor manejarlo manualmente)
- Apollo API para búsqueda automática (M4 fase 2) — esperar a validar la fase 1 primero
