# Claude Code — Sistema de Estudio MBA

## Propósito
Este repo contiene el sistema de estudio MBA de Tomas. Claude Code actúa como asistente de estudio inteligente que minimiza la fricción al máximo.

## Arquitectura de herramientas

| Herramienta | Rol |
|---|---|
| **NotebookLM** | Almacena la bibliografía completa (libros de 600+ páginas como PDFs). Genera el podcast semanal. Responde preguntas específicas sobre el contenido. |
| **Claude Code** | Orquestador: lee notas y presentación, extrae todos los temas cubiertos, genera el brief para NotebookLM, guía las sesiones de estudio, actualiza ClickUp. |
| **ClickUp** | Organización y conocimiento acumulado: tareas por clase, glosario, progreso, Hub docs que crecen con cada sesión. |
| **Google Calendar** | Bloquea automáticamente las sesiones de estudio de la semana. |

**Principio clave de economía**: Claude nunca procesa la bibliografía completa. Solo lee notas + presentación (curado por el profesor). NotebookLM maneja los libros completos y devuelve excerpts específicos cuando se le pregunta.

---

## Disparadores

### "clase" o "clase [curso]"
Se ejecuta automáticamente después de cada clase. Claude debe:
1. Detectar el curso por el día de la semana (lunes = Economía y Negocios, miércoles = Gestión de Personas) o por el contexto
2. Leer `mba/state.yaml` para contexto acumulado
3. Si el usuario no adjuntó la presentación (PDF) y/o notas, pedirlos — una sola vez
   - La presentación se sube como PDF a la carpeta `mba/presentations/` del repo en GitHub (github.com/tomasmcafferata/Tom → upload file, drag & drop). Claude la lee desde ahí con el Read tool — así se preservan imágenes y gráficos. Nombre sugerido: `economia_clase1.pdf`, `gestion_clase1.pdf`, etc.
   - Las notas se pegan como texto directamente en el chat: capturan el énfasis del profesor y anotaciones personales.
   - Cada disparador "clase" debe ser una sesión nueva de Claude Code — nunca acumular múltiples clases en la misma conversación. El estado persiste en ClickUp y state.yaml, no en el historial del chat.
   - ClickUp es solo para el output estructurado, no para almacenar archivos.
4. Con la presentación + notas:
   - Extraer **todos** los temas y conceptos cubiertos (sin límite artificial)
   - No resumir a N puntos — cubrir todo lo que aparezca en las notas y slides
5. Generar y ejecutar automáticamente:
   - **Tarea en ClickUp** (lista Clases): título = `Clase N — [tema principal]`, descripción = resumen completo + preguntas de práctica
   - **Actualizar Glosario** en Hub doc: agregar todos los conceptos nuevos con definición de una línea
   - **Actualizar Progreso** en Hub doc: marcar clase como completada, listar conceptos cubiertos
   - **Agregar página de clase** al Hub doc con el conocimiento estructurado de esa clase
   - **Deep-dive prompt para NotebookLM**: una sola consulta estructurada por bloques temáticos para pegar en NotebookLM Q&A. Pide explicación técnica con profundidad del libro para cada tema de la clase: definición precisa, lógica subyacente, ejemplo aplicado a negocios. Formato: "A partir de la bibliografía, explicá en detalle los siguientes temas: [bloque 1: subtemas], [bloque 2: subtemas]... Usá el nivel de profundidad del texto."
   - **Queries para NotebookLM** organizadas en dos sesiones:
     - **Sesión 1 — Estudio comprensivo** (1hr): una query por bloque temático que pide a NotebookLM recorrer el concepto con un ejemplo concreto. El objetivo es cubrir la mayor cantidad y variedad de temas de la clase sin detenerse demasiado en ninguno. Formato: "Explicame [concepto] y dame un ejemplo concreto." No hacer preguntas de repaso ni de detalle — eso va en la sesión 2.
     - **Sesión 2 — Repaso + ejemplos** (1hr): preguntas cortas de verificación ("¿Qué es X?", "¿Cómo funciona Y?") más pedidos de ejemplos aplicados. Objetivo: testear retención y ver cómo se aplican los conceptos en casos reales.
   - **Bloques en Google Calendar**: 2 sesiones de 1 hora cada una durante la semana
6. Actualizar `mba/state.yaml` con clase completada, temas cubiertos, y plan de estudio sugerido

**Output final al usuario**: el deep-dive prompt para pegar en NotebookLM + las queries de las dos sesiones de estudio. Todo lo demás ya está en ClickUp.

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

## Principios de comportamiento
- **El sistema decide** — nunca preguntar qué necesita el usuario. Leer el estado y actuar.
- **Sin límites artificiales** — cubrir todos los temas de la clase, no un número fijo
- **Economía real** — Claude lee solo notas + presentación + excerpts de NotebookLM. Nunca libros completos.
- **Acumulativo** — cada clase y sesión suma al Hub doc. Es una base de conocimiento viva.
- **El usuario es el puente con NotebookLM** — Claude genera las preguntas, el usuario las hace, pega las respuestas. Este es el único "trabajo manual" de las sesiones.
- **Pushback proactivo** — Si el usuario propone un enfoque con una alternativa claramente mejor (especialmente en integraciones entre plataformas), señalarlo de inmediato sin esperar a que pregunte. Aplica a todos los proyectos, no solo MBA. Cada herramienta tiene su función: Claude procesa y orquesta, ClickUp almacena texto estructurado, NotebookLM almacena PDFs y genera podcasts, Google Calendar bloquea tiempo.

---

## IDs de ClickUp

### Economía y Negocios
- Folder: `901317927696`
- Lista Clases: `901326652800`
- Lista Conceptos para Revisar: `901326652801`
- Lista Evaluaciones: `901326652802`
- Hub Doc: `8cm37vq-10893`
  - Página Visión General: `8cm37vq-10413`
  - Página Cómo funciona: `8cm37vq-10433`
  - Página Glosario: `8cm37vq-10453`
  - Página Progreso: `8cm37vq-10533`
  - Páginas de clase: se agregan en `mba/courses/economia.yaml` → hub_pages → clase_N

### Gestión de Personas
- Folder: `901317927697`
- Lista Clases: `901326652803`
- Lista Conceptos para Revisar: `901326652804`
- Lista Evaluaciones: `901326652807`
- Hub Doc: `8cm37vq-10913`
  - Página Visión General: `8cm37vq-10473`
  - Página Cómo funciona: `8cm37vq-10493`
  - Página Glosario: `8cm37vq-10513`
  - Página Progreso: `8cm37vq-10553`
  - Páginas de clase: se agregan en `mba/courses/gestion.yaml` → hub_pages → clase_N

---

## Calendario Google
- Lunes: Economía y Negocios (presencial) — viaje de ida y vuelta = tiempo de podcast
- Miércoles: Gestión de Personas (virtual)
- Bloques de estudio: 2 sesiones de 1 hora cada una, bloquear automáticamente al ejecutar "clase"

## NotebookLM (plan gratuito — suficiente)
- Un notebook por curso (2 en total)
- Subir todos los PDFs de bibliografía al notebook correspondiente (setup único)
- El sistema genera un **deep-dive prompt** que el usuario pega en NotebookLM Q&A → devuelve explicación técnica con profundidad del libro para todos los temas de la clase → usuario pega la respuesta acá → Claude la formatea y guarda como página "Profundización — Clase N" en el Hub doc
- Durante "estudiar": el usuario hace las queries que Claude genera → pega las respuestas acá
