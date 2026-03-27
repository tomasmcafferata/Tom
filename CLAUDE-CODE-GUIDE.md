# Claude Code — Guía de trabajo

Referencia práctica para entender cómo funciona Claude Code y cómo mantenemos organizado este repositorio.

---

## Conceptos fundamentales

### El proyecto

Un **proyecto** en Claude Code = un **repositorio de GitHub**. Cuando abrís Claude Code en una carpeta con git, ese directorio es tu proyecto. Este repositorio se llama `tomasmcafferata/tom`.

Si quisieras trabajar con otro proyecto, simplemente abrirías Claude Code en otro directorio (otro repositorio). Cada repositorio tiene su propio historial, branches, y archivos completamente independientes.

### Las branches

Las branches **no son proyectos separados** — son versiones paralelas del mismo código. Permiten trabajar en algo nuevo sin tocar la rama principal (`master`).

**El patrón `claude/<nombre>-<hash>`** es generado automáticamente por Claude Code. Cada sesión/tarea abre su propia rama para no modificar `master` directamente.

Las branches **sí pueden derivarse unas de otras**: si una rama se crea a partir de otra (en lugar de desde `master`), hereda todos sus commits. Es una relación de origen, no de jerarquía.

### Context window vs branch

| | Branch | Context Window |
|---|---|---|
| **Qué es** | Versión del código en git | Memoria de la conversación activa |
| **Persiste** | Sí — para siempre en git | No — desaparece al cerrar la sesión |
| **Contiene** | Archivos, commits, historial | El chat y los archivos leídos en esa sesión |
| **Cómo Claude retoma el trabajo** | Leyendo el historial de commits | No puede — la conversación se perdió |

La branch es el **código**. El context window es la **memoria de trabajo** de Claude en una sesión. Por eso Claude trabaja en branches con nombre único: así puede retomar el hilo aunque no recuerde la conversación anterior.

---

## Sistema de mantenimiento del workspace

### Ciclo de vida de una branch

```
[Sesión Claude] → crea claude/<tarea>-<hash>
      ↓
  trabajo terminado
      ↓
  merge a master
      ↓
  eliminar la branch (ya no aporta nada)
```

### Reglas de higiene

1. **Merge rápido**: cuando una tarea está terminada y aprobada, mergear a `master` en esa misma sesión o en la siguiente.
2. **Eliminar post-merge**: una branch mergeada no tiene utilidad — el historial queda en `master`. Borrarla.
3. **Nombrar descriptivamente**: el nombre automático de Claude (`claude/<tarea>`) ya es suficiente. No renombrar.
4. **Una tarea, una branch**: no acumular cambios de distintos temas en la misma branch.
5. **Ramas sin commits valiosos → eliminar**: si una sesión se cerró sin producir nada útil, borrar la branch.

### Revisión periódica

Cada vez que empezás una sesión nueva, revisar rápidamente las branches abiertas:
- ¿Tiene commits únicos vs `master`? → conservar y planificar merge
- ¿Está al mismo nivel que `master`? → ya mergeada, eliminar
- ¿Tiene 1 commit menor o fue una sesión descartada? → evaluar si vale o eliminar

---

## Estado actual del repo (referencia — actualizar al limpiar)

| Branch | Estado | Acción |
|--------|--------|--------|
| `master` | Base principal | Mantener |
| `claude/email-response-aggregator-hAElt` | Idéntica a master (ya mergeada) | Eliminar |
| `claude/add-install-script-XwwYR` | +4 commits de GTM/ICP sobre master | Merge o evaluar |
| `claude/continue-ndc-gtm-4TWbY` | +10 commits NDC GTM completo | Merge o evaluar |
| `claude/enedece-gtm-sequence-BdK6C` | +1 commit secuencia GTM | Merge o evaluar |
| `claude/market-icp-enedece-xXCic` | +1 commit ICP calificación | Evaluar si es redundante |
