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
   - Lunes = Liderazgo y Gestión de Equipos de Alto Rendimiento (en curso)
   - Miércoles = IFE — Información Financiera de la Empresa (en curso)
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

### IFE — Información Financiera de la Empresa (en curso — Miércoles)
- Hub Doc: `8cm37vq-10953`
  - Página Índice: `8cm37vq-10933`
  - Página Glosario: `8cm37vq-10973`
  - Página Progreso: `8cm37vq-10993`
  - Páginas de clase: se agregan en `mba/courses/ife.yaml` → hub_pages → clase_N

### Liderazgo y Gestión de Equipos (en curso — Lunes)
- Hub Doc: `8cm37vq-10973`
  - Página Índice: `8cm37vq-10953`
  - Página Glosario: `8cm37vq-11013`
  - Página Progreso: `8cm37vq-11033`
  - Páginas de clase: se agregan en `mba/courses/liderazgo.yaml` → hub_pages → clase_N

---

## Calendario Google
- Lunes: Liderazgo y Gestión de Equipos (en curso)
- Miércoles: IFE — Información Financiera de la Empresa (en curso)
- Economía y Negocios: completada (era presencial — viaje ida y vuelta = tiempo de podcast)
- Gestión de Personas: completada (era virtual)
- Bloques de estudio: 2 sesiones de 1 hora cada una, creadas después de recibir la respuesta de NotebookLM

## NotebookLM (plan gratuito — suficiente)
- Un notebook por curso (4 en total: Economía, Gestión, IFE, Liderazgo)
- Subir todos los PDFs de bibliografía al notebook correspondiente (setup único)
- **IFE**: subir Fowler Newton — Análisis de estados contables + Fowler Newton — Contabilidad con inflación
- **Liderazgo**: subir papers de Clase 5 (Blanchard Cap.6 + Heifetz Cap.5 + Bass + Goldsmith). Los casos Harvard se leen directo, no subirlos.
- El sistema genera un **deep-dive prompt** que el usuario pega en NotebookLM Q&A → devuelve explicación técnica con profundidad del libro → usuario pega la respuesta acá → Claude crea la página de clase unificada, actualiza el Glosario y crea los bloques de Calendar
- Durante "estudiar": el usuario hace las queries que Claude genera → pega las respuestas acá
