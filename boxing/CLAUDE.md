# CLAUDE.md — Boxing Training System

## Contexto del proyecto
Sistema de entrenamiento de boxeo basado en absorción de estilos de boxeadores elite.
El atleta es un boxeador amateur en desarrollo, categoría +75 kg, con competencia próxima.

**Siempre leer `BOXING_BRAIN.md` antes de generar cualquier programa o responder sobre el estado del entrenamiento.**

---

## Archivos clave

| Archivo | Propósito |
|---------|-----------|
| `BOXING_BRAIN.md` | Memoria estratégica del atleta. Fuente de verdad del proyecto. |
| `boxeadores/{nombre}/` | Perfil del boxeador modelo + historial de programas generados |
| `programa.md` | Programa de la semana activa (se sobreescribe cada semana) |
| `generate-email-draft.py` | Genera borrador del programa para revisión |
| `send-to-gmail.py` | Envía el programa aprobado por email |

---

## Cuándo actualizar BOXING_BRAIN.md

Claude Code actualiza el archivo **directamente y sin pedir confirmación** en estos casos:

### Actualización automática (silenciosa)
- Al generar un nuevo programa semanal → actualizar `## 1. ESTADO ACTUAL`
  - Incrementar semana del ciclo
  - Actualizar foco de la semana
  - Actualizar "próxima acción"
  - Actualizar fecha de última actualización

### Actualización por instrucción explícita del atleta
Cuando el atleta dice algo como:
- *"terminé la semana"* / *"cerramos el ciclo de Bivol"* → actualizar `## 5. TRACKING`
- *"cambió la fecha de la competencia"* → actualizar `## 3. PERIODIZACIÓN` y `## 1. ESTADO ACTUAL`
- *"arranco precompetencia"* / *"nueva fase"* → actualizar fase en `## 1` y `## 3`
- *"actualizá mi perfil"* + descripción → actualizar `## 2. PERFIL DEL ATLETA`
- *"el próximo boxeador es X"* → agregar entrada en `## 4. BIBLIOTECA` y actualizar `## 1`
- *"anotá en el tracking"* + observación → agregar nota en `## 5. TRACKING`

### No modificar sin instrucción explícita
- `## 6. STRENGTH & CONDITIONING`
- `## 7. NUTRICIÓN`
- Historial de boxeadores completados en `## 4`

---

## Cómo generar un programa semanal

1. Leer `BOXING_BRAIN.md` — fase actual, semana del ciclo, foco, anti-patterns del atleta
2. Leer el perfil del boxeador activo en `boxeadores/{nombre}/`
3. Generar `programa.md` cruzando: estilo del boxeador × perfil del atleta × fase del ciclo
4. El programa debe estar personalizado al perfil actual del atleta según `## 2. PERFIL DEL ATLETA` en `BOXING_BRAIN.md` — fortalezas, áreas críticas y anti-patterns vigentes al momento de generación
5. Actualizar `## 1. ESTADO ACTUAL` en `BOXING_BRAIN.md`
6. Ejecutar `generate-email-draft.py` para preparar el borrador

---

## Principios del entrenador virtual

- Los programas no son genéricos. Siempre reflejan la realidad actual del atleta.
- "Absorber un estilo" = extraer principios transferibles, no copiar mecánicamente.
- El perfil del atleta en `BOXING_BRAIN.md` es dinámico — leerlo siempre, no asumir nada de memoria.
- Menos es más: un programa claro y ejecutable vale más que uno exhaustivo.
