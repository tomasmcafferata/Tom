# Diseño Organizacional — triage del material de la cátedra

Carpeta original: `~/Downloads/DO-10788-AD-BLEND2-2026-2T_2026096_1825` (44 archivos, ~470 MB).
Al repo se copiaron 28 (~15 MB). Qué se trajo, qué no y por qué.

## Lo que vale y está acá

| Archivo | Por qué |
|---|---|
| `clase1.pptx` … `clase5.pptx` | Los 5 decks de Delle Donne. Son autosuficientes: teoría, casos y respuestas modelo de los talleres. Cubren 57 de las 68 preguntas del examen. Es la fuente de estudio principal. |
| `programa.doc` | Formato OLE viejo. Trae evaluación, mínimos, política de IA y bibliografía. Ya volcado al Hub. |
| `examen_multiple_choice_preguntas.docx` | **El archivo más valioso de la carpeta.** Las 68 preguntas reales del examen, sin las opciones. |
| `tf_casos_individuales.docx` | El pool de 12 casos del trabajo final (el archivo trae 13, el 13 duplica al 4). |
| `tf_ejemplos_resueltos.docx` | Volkswagen y Haier con las **respuestas modelo de la cátedra**. Revela la estructura exacta de la consigna. |
| `taller_agente_inmobiliario.xlsx` | Planilla del taller de Clase 2. Casi vacía: es para completar en clase. |
| `lecturas/` (15 artículos) | Las 6 ligadas al examen + la teoría núcleo citada en los decks. |

### Las 6 lecturas que el examen exige y los decks no cubren

`culture_is_not_the_culprit.txt` (P22-24) · `por_que_cuesta_tanto_un_incentivo.pdf` (P25-26) · `economics_of_organizational_architecture.pdf` (P38-39) · `zhu_xie_compensation_incentives.pdf` (P40-41) · `microsofts_lost_decade.docx` (P54-56) · `ranking_workers_tech_companies.docx` (P57).

`culture_is_not_the_culprit` está como `.txt` y no como PDF: el original pesa 8,5 MB por las fotos y el texto extraído es idéntico para lo que hace falta.

## Lo que se dejó afuera

| Archivo | Peso | Motivo |
|---|---|---|
| `Managerial Economics and Organizational Architecture.pdf` (Brickley) | 4 MB, ~600 pág. | Bibliografía obligatoria, pero ninguna de las dos evaluaciones la requiere. Queda en Descargas como referencia de consulta puntual. |
| `XVI CONGRESO ADRHA - Entrevista a Marc Effron.f4v` | **422 MB** | Excede el límite de GitHub. Las 5 razones de Effron contra la autoevaluación ya están en el deck de Clase 5 y en el Glosario. |
| `Informe-Mazars-NCG-461-2023.pdf` | 19 MB | Normativa de gobierno corporativo chilena. No aparece en ninguna pregunta ni en ningún deck. |
| `04_Rank and Yank.pdf` (Kwoh, WSJ) | 1,7 MB | **Escaneado sin capa de texto**: `pdftotext` devuelve 3 bytes y no hay OCR instalado. Está en la bibliografía del programa, pero su contenido está cubierto por el deck de Clase 5 y por `ranking_workers_tech_companies.docx`. |
| `Freakonomics Intro y Cap 1 Castellano.pdf` | 5 MB | También escaneado sin texto. Se trajo la versión en inglés, que sí es legible. |
| `Escasez_de_talento_2020 Manpower.pdf` | 7,9 MB | No aparece en ninguna pregunta ni en los decks. |
| `Your Financial Adviser Doesn't… - WSJ.pdf` | 6,4 MB | El caso está resumido en el deck de Clase 2 (slide 7). No justifica 6 MB. |
| `Comportamiento humano y niveles de trabajo en modelo ST-IT` | 2,5 MB | Lectura complementaria de Clase 4, no evaluada. |
| `2021 mercer pago por competencias.pdf`, `La motivación como factor crítico del empleo público.pdf`, `Economía del comportamiento — Thaler.pdf`, `Dificultades en reconocer la propia incompetencia.pdf`, `informe compensaciones ASG.pptx`, `nuevos articulos evaluacion de desempeño.docx`, `Quiénes son los directores que más ganan en EE.UU..docx` | varios | Material de contexto. No aparecen en el banco de preguntas ni son citados como lectura obligatoria en los decks. |

## Notas de extracción

- Los `.pptx` y `.docx` se leen con `zipfile` + regex sobre el XML (no hay `python-pptx` instalado). Script en el scratchpad de la sesión.
- El `programa.doc` es OLE binario: no hay LibreOffice ni antiword en la máquina. Se extrajo con un volcado de strings en cp1252, que resultó limpio.
- Intérprete de Python: `C:\Users\Tomas Cafferata\AppData\Local\Python\bin\python.exe`. `pdftotext` en `C:\Program Files\Git\mingw64\bin\`.
