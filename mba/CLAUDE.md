# Claude Code — Sistema de Estudio MBA

## Propósito
Este repo contiene el sistema de estudio MBA de Tomas. Claude Code actúa como asistente de estudio inteligente que minimiza la fricción al máximo.

## Arquitectura de herramientas

| Herramienta | Rol |
|---|---|
| **NotebookLM** | Almacena la bibliografía completa (libros de 600+ páginas como PDFs). Genera el podcast semanal. Responde preguntas específicas sobre el contenido. |
| **Claude Code** | Orquestador: lee notas y presentación, extrae todos los temas cubiertos, genera el brief para NotebookLM, guía las sesiones de estudio, actualiza ClickUp. |
| **ClickUp** | Conocimiento acumulado: glosario, progreso, páginas de clase unificadas. Hub docs que crecen con cada sesión. |
| **Google Calendar** | Bloquea automáticamente las sesiones de estudio de la semana. |

**Principio clave de economía**: Claude nunca procesa la bibliografía completa. Solo lee notas + presentación (curado por el profesor). NotebookLM maneja los libros completos y devuelve excerpts específicos cuando se le pregunta.

---

## Disparadores

### "clase" o "clase [curso]"
Se ejecuta automáticamente después de cada clase. Claude debe:
1. Detectar el curso por el día de la semana o por el contexto:
   - Lunes = Sistemas de Información (en curso — Clase 3 es la excepción: jueves 20/08)
   - Finanzas Corporativas (completada — ya no genera clases nuevas)
   - Información Gerencial y Control de Gestión — IGyCG (completada — ya no genera clases nuevas)
   - Liderazgo y Gestión de Equipos (completada — ya no genera clases nuevas)
   - IFE — Información Financiera de la Empresa (completada — ya no genera clases nuevas)
   - Economía y Negocios (completada — ya no genera clases nuevas)
   - Gestión de Personas (completada — ya no genera clases nuevas)
2. Leer `mba/state.yaml` para contexto acumulado
3. Si el usuario no adjuntó la presentación (PDF) y/o notas, pedirlos — una sola vez
   - El PDF debe estar en la carpeta local `mba/presentations/[curso]/` antes de iniciar la sesión (ej: `mba/presentations/ife/clase3.pdf`, `mba/presentations/liderazgo/clase2.pdf`). Claude lo lee directamente con el Read tool — así se preservan imágenes y gráficos. Nombre sugerido: `clase1.pdf`, `clase2.pdf`, etc.
   - Las notas se pegan como texto directamente en el chat: capturan el énfasis del profesor y anotaciones personales.
   - Cada disparador "clase" debe ser una sesión nueva de Claude Code — nunca acumular múltiples clases en la misma conversación. El estado persiste en ClickUp y state.yaml, no en el historial del chat.
4. Con la presentación + notas:
   - Extraer **todos** los temas y conceptos cubiertos (sin límite artificial)
   - No resumir a N puntos — cubrir todo lo que aparezca en las notas y slides
5. Ejecutar inmediatamente (solo estas dos cosas):
   - **Actualizar Progreso** en Hub doc: marcar clase como completada, listar conceptos cubiertos
   - **Actualizar `mba/state.yaml`** con clase completada y temas cubiertos
6. Generar y mostrar al usuario:
   - **Deep-dive prompt para NotebookLM**: una sola consulta estructurada por bloques temáticos. Pide explicación técnica con profundidad del libro para cada tema: definición precisa, lógica subyacente, ejemplo aplicado. Formato: "A partir de la bibliografía, explicá en detalle los siguientes temas: [bloque 1: subtemas], [bloque 2: subtemas]... Usá el nivel de profundidad del texto."
   - **Queries para NotebookLM** organizadas en dos sesiones:
     - **Sesión 1 — Estudio comprensivo** (1hr): una query por bloque temático que pide recorrer el concepto con un ejemplo concreto. Cubrir la mayor cantidad de temas sin detenerse en ninguno. Formato: "Explicame [concepto] y dame un ejemplo concreto." No incluir preguntas de repaso ni de detalle.
     - **Sesión 2 — Repaso + ejemplos** (1hr): preguntas cortas de verificación ("¿Qué es X?", "¿Cómo funciona Y?") más pedidos de ejemplos aplicados. Objetivo: testear retención y aplicación.

**Luego esperar** a que el usuario pegue la respuesta de NotebookLM. NO ejecutar nada más hasta entonces.

7. **SOLO cuando el usuario pega la respuesta de NotebookLM**, ejecutar todo lo siguiente en paralelo:
   - **Página de clase** en Hub doc: una sola página unificada que combina el conocimiento de la presentación + la profundización de NotebookLM por bloque temático. Título: `Clase N — [tema principal]`. Guardar page_id en `mba/courses/[curso].yaml` → hub_pages → clase_N
   - **Actualizar Glosario** en Hub doc: agregar todos los conceptos nuevos con definición de una línea, enriquecida con la explicación de NotebookLM
   - **Bloques en Google Calendar**: 2 sesiones de 1 hora cada una durante la semana
   - **Commit y push** de los archivos actualizados

---

### "estudiar" o "sesión"
Inicia una sesión de estudio guiada. Claude debe:
1. Leer `mba/state.yaml` → decidir qué estudiar (prioridad: énfasis del profesor + tiempo desde última revisión + proximidad de evaluaciones)
2. Presentar sin preguntar: "Hoy estudiamos [tema] de [curso] porque [razón]. Vamos a tardar ~[tiempo]."
3. Para cada sub-tema:
   a. Explicar el concepto con lo que ya se sabe (de las notas de clase)
   b. Dar al usuario **1-2 preguntas específicas para hacerle a NotebookLM** sobre ese tema
   c. Usuario pega la respuesta de NotebookLM
   d. Claude sintetiza, agrega contexto, plantea preguntas de reflexión
4. Al terminar (usuario dice "listo", "siguiente", o similar):
   - Actualizar la página del Hub doc correspondiente con el conocimiento nuevo
   - Marcar tópicos como estudiados en `mba/state.yaml`
   - Si quedan temas: "Próxima sesión: [tema]."

---

### "repaso" o "revisar"
Sesión rápida (15-30 min). Claude debe:
1. Tomar los conceptos más urgentes de `mba/state.yaml`
2. Modo flashcard: hacer preguntas, el usuario responde, Claude da feedback
3. Actualizar estado según desempeño

---

### "ejercicios" o "ejercicios [curso]"
Modo práctica para **materias cuantitativas** (ej. Finanzas Corporativas). **On-command, nunca automático.** Claude debe:
1. Tomar la guía de ejercicios del curso (`mba/presentations/[curso]/ejercicios_*.pdf`)
2. Presentar **un ejercicio por vez**, sin mostrar la respuesta
3. El usuario resuelve; Claude verifica planteo y resultado contra el `.xlsx` de resolución (`ejercicios_*_resolucion.xlsx`), que es la clave de corrección
4. Si hay error, explicar el paso que falló y la fórmula correcta (página **Formulario** del Hub)
5. Trackear en `mba/state.yaml` qué tipos de ejercicio ya domina el usuario

---

### "caso" o "caso [curso]"
Modo **case cracker** para casos de negocio (Harvard u otros). **On-command.** Los casos se leen directo con el Read tool (nunca van a NotebookLM). Claude debe:

1. Identificar curso y caso:
   - El PDF del caso debe estar en `mba/casos/[curso]/` (ej: `mba/casos/control_gestion/caso_nexo.pdf`)
   - Leer `mba/state.yaml` → `topics_covered` del curso: esos son los frameworks con los que se analiza el caso
2. Preguntar el **modo** — una sola vez:
   - **rápido** (~20 min): preparación para discusión en clase. Claude presenta cada paso ya resuelto y hace 1-2 preguntas de verificación por paso.
   - **completo** (1-2 hs): entregable o examen. Walkthrough socrático completo — el usuario responde primero en cada paso, Claude corrige y complementa. Nunca dar la respuesta antes de que el usuario lo intente.
3. Recorrer los **6 pasos del cracker**, en orden:
   1. **Snapshot** — protagonista, decisión a tomar, deadline, stakeholders clave. Una línea por ítem.
   2. **Problema central** — distinguir síntomas de problema raíz. Formularlo como una sola pregunta de decisión.
   3. **Análisis con frameworks del curso** — aplicar SOLO frameworks ya vistos en clase (de `topics_covered`). Nombrar explícitamente cada framework usado. Si un framework obvio todavía no se vio en clase, mencionarlo como "próximamente" pero no usarlo.
   4. **Evidencia cuantitativa** — exhibits, tablas y números del caso. En materias cuantitativas (Finanzas, IGyCG) este paso es el central: plantear los cálculos y que el usuario los resuelva (mismo espíritu que el trigger "ejercicios").
   5. **Alternativas** — 2-3 opciones reales (no strawmen), con criterios de decisión explícitos antes de evaluarlas.
   6. **Recomendación** — decisión única, plan de acción concreto y 2-3 riesgos con mitigación. Sin "depende".
4. Al terminar:
   - Guardar el write-up en `mba/casos/[curso]/[caso].md` siguiendo `mba/casos/TEMPLATE.md`
   - Actualizar `mba/state.yaml` → agregar el caso bajo `cases_analyzed` del curso (nombre, fecha, frameworks aplicados, modo)
   - Commit y push

**Principio del modo completo**: Claude es tribunal, no autor. El write-up final debe reflejar el razonamiento del usuario, corregido — no el de Claude.

---

### "cierre" o "materia terminada"
Se ejecuta al finalizar una materia completa. Claude debe:
1. Leer el hub doc de la materia indicada (`mba/courses/[curso].yaml` → `hub_doc_id`)
2. Listar todas las páginas del doc con `clickup_list_document_pages`
3. Leer el contenido de todas las páginas relevantes en paralelo (todas las clases + glosario)
4. Actualizar la **primera página del doc** (el Índice) con todo el contenido mergeado en una sola página:
   - **Info general** del curso: profesor, modalidad, horario, bibliografía, estado "Completada"
   - **Índice** con tabla de clases y fechas
   - **Todas las clases** en orden, completas, una tras otra (con sus preguntas de práctica)
   - **Glosario** completo al final
5. Informar al usuario qué páginas debe eliminar manualmente en ClickUp (click derecho → Delete):
   - Visión General / Información General
   - Cómo funciona el sistema
   - Progreso del Curso
   - Cada página individual de clase
   - Página individual de Glosario
   - Cualquier otra página redundante
6. Actualizar `mba/courses/[curso].yaml`:
   - Agregar `status: completada`
   - Agregar `unified_page_id: [id de la primera página del doc]`
7. Commit y push de los archivos actualizados

**Nota:** La API de ClickUp no permite eliminar páginas — esa acción siempre la hace el usuario manualmente.

---

## Principios de comportamiento
- **El sistema decide** — nunca preguntar qué necesita el usuario. Leer el estado y actuar.
- **Sin límites artificiales** — cubrir todos los temas de la clase, no un número fijo
- **Economía real** — Claude lee solo notas + presentación + excerpts de NotebookLM. Nunca libros completos.
- **Acumulativo** — cada clase y sesión suma al Hub doc. Es una base de conocimiento viva.
- **Una sola página por clase** — nunca crear páginas separadas de "profundización". Todo va en la página de clase unificada.
- **El usuario es el puente con NotebookLM** — Claude genera las preguntas, el usuario las hace, pega las respuestas. Este es el único "trabajo manual" de las sesiones.
- **Pushback proactivo** — Si el usuario propone un enfoque con una alternativa claramente mejor (especialmente en integraciones entre plataformas), señalarlo de inmediato sin esperar a que pregunte. Aplica a todos los proyectos, no solo MBA. Cada herramienta tiene su función: Claude procesa y orquesta, ClickUp almacena texto estructurado, NotebookLM almacena PDFs y genera podcasts, Google Calendar bloquea tiempo.

---

## IDs de ClickUp

### Economía y Negocios (completada)
- Hub Doc: `8cm37vq-10893`
  - Página Glosario: `8cm37vq-10453`
  - Página Progreso: `8cm37vq-10533`
  - Páginas de clase: se agregan en `mba/courses/economia.yaml` → hub_pages → clase_N

### Gestión de Personas (completada)
- Hub Doc: `8cm37vq-10913`
  - Página Glosario: `8cm37vq-10513`
  - Página Progreso: `8cm37vq-10553`
  - Páginas de clase: se agregan en `mba/courses/gestion.yaml` → hub_pages → clase_N

### IFE — Información Financiera de la Empresa (completada)
- Hub Doc: `8cm37vq-10953`
  - Página Índice: `8cm37vq-10933`
  - Página Glosario: `8cm37vq-10973`
  - Página Progreso: `8cm37vq-10993`
  - Páginas de clase: se agregan en `mba/courses/ife.yaml` → hub_pages → clase_N

### Liderazgo y Gestión de Equipos (completada)
- Hub Doc: `8cm37vq-10973`
  - Página Índice: `8cm37vq-10953`
  - Página Glosario: `8cm37vq-11013`
  - Página Progreso: `8cm37vq-11033`
  - Páginas de clase: se agregan en `mba/courses/liderazgo.yaml` → hub_pages → clase_N

### Información Gerencial y Control de Gestión — IGyCG (completada)
- Hub Doc: `8cm37vq-11019`
  - Páginas: ver `mba/courses/control_gestion.yaml` → hub_pages
- Pendiente: correr el trigger **"cierre"** para unificar el doc.

### Finanzas Corporativas (completada)
- Hub Doc: `8cm37vq-11039`
  - Página Índice: `8cm37vq-11479`
  - Página Formulario: `8cm37vq-11519`  (reemplaza al Glosario)
  - Página Progreso: `8cm37vq-11499`
  - Páginas de clase: se agregan en `mba/courses/finanzas.yaml` → hub_pages → clase_N
- **Materia cuantitativa**: sin NotebookLM (Claude lee los PDFs directo), Glosario = Formulario, modo ejercicios on-command.
- Pendiente: correr el trigger **"cierre"** para unificar el doc.

### Sistemas de Información (en curso — Lunes)
- Hub Doc: `8cm37vq-11059`
  - Página Índice: `8cm37vq-11659`
  - Página Progreso: `8cm37vq-11679`
  - Página Glosario: `8cm37vq-11699`
  - Página TP Final: `8cm37vq-11799`
  - Páginas de clase: ver `mba/courses/sistemas.yaml` → hub_pages
- **Materia conceptual dirigida por decks**: sin NotebookLM. Los decks de Parola son autocontenidos y opinados (frameworks propios + casos) — Claude los lee directo desde `mba/presentations/sistemas/`. Laudon queda como referencia de consulta puntual.
- Clases 1-4 **precargadas** desde los decks; se refinan cuando el usuario pegue las notas.
- **Ojo con el calendario**: Clase 3 es **jueves 20/08** (no lunes). Quiz individual el **24/08**. Documento del TP vence el **27/08**.
- `programa.pdf` de la carpeta del curso es la versión **2025** (otros profesores, otras ponderaciones) — desactualizado. El cronograma y el deck mandan.

---

## Calendario Google
- Lunes: Sistemas de Información (en curso) — **sin bloques automáticos de Calendar** (no usa NotebookLM)
- Finanzas / IGyCG / Liderazgo / IFE / Economía / Gestión de Personas: completadas
- Bloques de estudio (materias con NotebookLM): 2 sesiones de 1 hora, creadas después de recibir la respuesta de NotebookLM

## NotebookLM (plan gratuito — suficiente)
- Un notebook por curso (Economía, Gestión, IFE, Liderazgo)
- **Finanzas Corporativas NO usa NotebookLM** — es cuantitativa; Claude lee los PDFs de teoría (cortos y curados) directamente, clase a clase. El estudio se basa en resolver ejercicios, no en excerpts (ver trigger "ejercicios").
- **Sistemas de Información NO usa NotebookLM** — los decks del profesor son autocontenidos y opinados (frameworks propios y casos), y son lo que evalúa el quiz. Laudon (17ª ed., 81MB, en inglés) se cita solo puntualmente: no justifica el setup.
- Subir todos los PDFs de bibliografía al notebook correspondiente (setup único)
- **IFE**: subir Fowler Newton — Análisis de estados contables + Fowler Newton — Contabilidad con inflación
- **Liderazgo**: subir papers de Clase 5 (Blanchard Cap.6 + Heifetz Cap.5 + Bass + Goldsmith). Los casos Harvard se leen directo, no subirlos.
- El sistema genera un **deep-dive prompt** que el usuario pega en NotebookLM Q&A → devuelve explicación técnica con profundidad del libro → usuario pega la respuesta acá → Claude crea la página de clase unificada, actualiza el Glosario y crea los bloques de Calendar
- Durante "estudiar": el usuario hace las queries que Claude genera → pega las respuestas acá
