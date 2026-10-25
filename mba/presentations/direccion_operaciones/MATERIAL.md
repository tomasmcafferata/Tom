# Dirección de Operaciones — triage del material de la cátedra

Carpeta original: `~/Downloads/Dirección de Operaciones` (12 archivos, ~62 MB, 4 módulos).
Al repo se copiaron 10 (~41 MB). Qué se trajo, qué no y por qué.

## Lo que está acá

| Archivo | Por qué |
|---|---|
| `modulo1_estrategia_operaciones.pdf` | Deck de Romano. Abre el curso: presenta los 5 ejes y Estrategia de Operaciones. |
| `modulo2_agile.pdf` | Deck de Castano Lucero. Mindset ágil, complejidad, State of Agile, MVP, Scrum y otros marcos. |
| `modulo3_gestion_proyectos.pdf` | Deck completo de Gestión de Proyectos. |
| `modulo3_gestion_proyectos_dictado.pdf` | Versión resumida de lo que efectivamente se dicta. Leer primero esta. |
| `modulo3_guia_edt.pdf`, `modulo3_guia_riesgos.pdf` | Guías prácticas cortas para armar EDT y grilla de riesgos. |
| `modulo3_herramienta_trabajo.xlsx` | Plantilla de gestión: control de cambios, interesados y requisitos, actividades y costo, EDT, cronograma, riesgos, comunicaciones, contrataciones. Probable base de un trabajo práctico. |
| `modulo3_ejercicio_camino_critico.xlsx` | Actividades A-N con predecesoras. **Sin resolución.** |
| `modulo4_mejora_procesos.pdf` | Deck de Romano sobre estrategia y mejora de procesos. |
| `bibliografia/scrum_guide_2020.pdf` | 300 KB, ~5.000 palabras, en castellano. Es la fuente canónica de Scrum: barata de leer entera. |

## Lo que se dejó afuera

| Archivo | Peso | Motivo |
|---|---|---|
| `The Agile Samurai` (Rasmusson) | 14 MB, ~59k palabras, inglés | Bibliografía complementaria. Queda en Descargas para consulta puntual. |
| `Guia Practica Agil.pdf` (PMI) | 7 MB, ~48k palabras | Ídem. |

## Lo que falta

- **Programa / cronograma / evaluación**: la carpeta no lo trae.
- **Customer Experience**: el deck de Romano lo anuncia como eje del curso, pero no hay material.

## Notas de extracción

- Texto con `pdftotext -enc UTF-8 -layout` (`C:\Program Files\Git\mingw64\bin\`). Los decks son muy visuales: el texto extraído pierde diagramas.
- Los `.xlsx` se leen con `zipfile` + XML (no hace falta openpyxl para inspeccionar).
