# Clase 5 — AO: Medición de desempeño

> Fuente: ClickUp hub 8cm37vq-11079, page 8cm37vq-11999

> Precargada desde el deck. Se refina cuando se peguen las notas de clase.

## Pregunta central de la clase

¿Cómo medir el desempeño de los empleados de manera que los incentivos estén alineados con los objetivos de la firma?

**El dilema central: medición objetiva vs. medición subjetiva — el trade-off entre costo de medición e incentivos eficientes.**

La compensación por performance usa como **input** el output de la evaluación del desempeño: los dos sistemas están íntimamente relacionados. Las empresas suelen tener mediciones objetivas y subjetivas a la vez.

## Bloque 1 — Fundamentos

### Las dos razones de ser de la evaluación

|  | 1\. Información para el empleado | 2\. Premios y castigos |
| ---| ---| --- |
| Para qué | Proveerle información útil sobre cómo mejorar su productividad | Determinar recompensas y sanciones |
| Incentivo a distorsionar | Ninguno: no afecta su compensación | Fuerte: le conviene distorsionarla a su favor |

**Esta clase se concentra en la segunda.** La evaluación puede ser individual o de sub-unidades de la firma.

### La realidad de la evaluación (HBR, 2020 — "How to Actually Encourage Employee Accountability")

| Dato | % |
| ---| --- |
| Empleados que sienten que su desempeño se administra de manera que los motiva | 14% |
| Recibe comentarios menos de una vez al año | 26% |
| Siente que las métricas de desempeño están bajo su control | 21% |
| Siente que el gerente es responsable de las metas establecidas | 40% |
| No percibe objetividad en la forma en que su gerente lo evalúa | 70% |
| No siente que está desarrollando su potencial en el trabajo | 69% |

### Tendencias: de dónde a dónde

Evaluador único → varios evaluadores · Competencias duras → duras + blandas · Rol pasivo del evaluado → rol activo · Proceso simple → proceso complejo · Diseño aleatorio → diseño sistémico · Tiempo escaso → tiempo considerable · Retroalimentación escasa → retroalimentación importante · Seguimiento nulo → seguimiento alto.

### Taller de apertura: la cocina y las expectativas

Limpiás la cocina entera —platos, lavavajillas, heladera, superficies con desinfectante, basura al garaje, barrer, acomodar mesa y sillas, cambiar el agua de las flores— y tu pareja responde: _"Bien. Cumpliste las expectativas."_

**Lo que dispara:** si el estándar no se explicita antes, el esfuerzo extra no se reconoce ni se repite. La evaluación sin criterios definidos ex ante destruye el incentivo que pretendía crear, y el evaluado no puede saber qué se valora ni cómo alinearse.

## Bloque 2 — Los cuatro criterios de eficacia del sistema de evaluación

(Shields, J. _Managing Employee Performance and Reward_, Cambridge University Press.)

**1\. VALIDEZ — ¿realmente estamos midiendo las cosas correctas para este rol?**
Criterios por los cuales se define el "desempeño" en términos de los estándares deseados, y precisión con que las medidas reflejan o predicen el desempeño real. Un sistema es válido si estándares y medidas son directamente relevantes para lo que requiere ese trabajo, posición o rol.

**2\. FIABILIDAD — ¿produce el instrumento los mismos resultados en condiciones equivalentes?**
Alta fiabilidad = produce repetidamente las mismas puntuaciones a lo largo del tiempo para un mismo nivel de rendimiento, **y** las mismas puntuaciones cuando lo administran diferentes evaluadores.

**3\. COSTOS — ¿vale la pena la inversión en precisión?**
El tiempo y los gastos de buscar instrumentos cada vez más fiables. Los altos costos de medición pueden reducir los beneficios netos de vincular la paga al rendimiento. **El aumento de la compensación de incentivos debe ir acompañado del aumento en la precisión con que se mide el esfuerzo.**

**4\. EQUIDAD ("justicia organizacional") — ¿los empleados perciben el sistema como justo?**
Se centra en la justicia percibida por los evaluados, no solo en la objetividad técnica del instrumento. Un sistema técnicamente válido pero percibido como injusto genera desmotivación y resistencia: **la legitimidad del proceso es tan importante como la precisión del resultado.**

## Bloque 3 — El modelo de Holmström (1979)

### Las variables

| Símbolo | Qué representa | Observable |
| ---| ---| --- |
| Q | Output producido por el empleado | Sí |
| e | Esfuerzo realizado por el empleado | No |
| μ | Variable aleatoria: factores impredecibles que influyen en el output | No |
| α | Productividad marginal del empleado | Estimable |
| W | Parte fija de la compensación | Sí |
| β | Sensibilidad del pago a la performance | Sí |

```
Cantidad producida:        Q = α·e + μ
Función de compensación:   W(Q) = W + β·Q
Desarrollada:              W(Q) = W + β·α·e + β·μ
```

### Las nueve hipótesis del modelo

1. Un solo período.
2. Q es observable y es la **única** medida objetiva de performance. El principal conoce Q, pero no los valores reales de e ni de μ.
3. α puede estimarse.
4. e y μ no son observables.
5. No hay otra medida de performance que Q.
6. El empleado no puede hacer trampa con la medida de performance.
7. No hay otra tarea asignada al empleado que producir Q.
8. Cualquier contrato mutuamente beneficioso es posible (mercado laboral desregulado).
9. El empleado trabaja solo: no hay producción en grupo.

### Las consecuencias

**El contrato de incentivos impone riesgo al empleado.** El pago se convierte en función de μ, una variable que el empleado no controla. Como es averso al riesgo, la firma debe compensarlo con una **compensación diferencial por riesgo**: le sale más caro.

**El sueldo fijo elimina el incentivo al esfuerzo.** Si β = 0, la compensación es independiente de Q y el empleado tiene incentivo a reducir el esfuerzo. Como ni e ni μ son observables, **puede culpar a un μ negativo para justificar un Q pequeño**, y el principal no puede refutarlo.

**Conclusión: siempre existe trade-off** entre compensaciones incentivadoras y el costo de una distribución ineficiente del riesgo. El contrato óptimo combina una parte fija W y una parte variable β·Q.

### La precisión de la medición

Cuanto más **ruido** hay en la medición (mayor varianza de μ), más difícil es distinguir si un Q alto se debe al esfuerzo o a factores externos favorables. Si la medición es imprecisa, el empleado carga con mucho riesgo que no controla; para compensarlo la firma debe pagarle más **o reducir β**.

**La solución:** reducir la varianza de μ mejorando la precisión del instrumento. Cuando se mide con más precisión, una mayor proporción de la variación en Q se explica por el esfuerzo real y menos por el azar. Entonces el empleado asume menos riesgo, la compensación diferencial se reduce y el incentivo transmite mejor la señal correcta.

**El orden importa: primero se mejora la medición, después se sube β.**

### El contrato óptimo y el efecto trinquete

El empleador debe hallar el β óptimo y la W. Para eso necesita conocer α, y hay dos métodos:

*   **Estudios de movimiento y tiempo** — costosos, sujetos a cambios de condiciones, y con riesgo de que los empleados ajusten la producción a la baja para que la cuota baje y luego superarla fácilmente.
*   **Performance pasada — y el efecto trinquete (ratchet)** — usar el desempeño real del año como base del siguiente. El empleado sabe que si supera la meta, la meta del año siguiente aumenta, así que **tiene incentivo racional a moderar el esfuerzo**.

### Taller: maestros y exámenes estandarizados

Se paga al maestro según el aprendizaje de sus alumnos, y la única medida disponible es un examen estandarizado anual. **Hay muchísimo ruido:** la familia del alumno, su contexto socioeconómico, si ese día estaba enfermo, si el examen cubrió los temas que el maestro enseñó.

El maestro asume riesgo que no controla. Si se aumenta el bono sin mejorar la medición, soporta más riesgo y los incentivos son caros y distorsionados. Si se mejoran los instrumentos —evaluaciones más frecuentes, múltiples dimensiones, control por contexto socioeconómico— la medición captura mejor el aporte real del maestro, y **ahí** tiene sentido aumentar el componente variable.

En la plenaria se asumen los roles de: autoridades del gobierno y del colegio, sindicatos de maestros, padres, y maestros.

### Barzel (1982) — los costos de medición

> "Las personas intercambiarán bienes solo si perciben que lo que obtienen es más valioso que lo que dan. Para formar tales percepciones, los atributos de los artículos comercializados deben medirse. Determinar el peso de una naranja puede ser preciso y de bajo costo. Sin embargo, **lo que se pesa es rara vez lo que se valora**: el sabor y la cantidad de jugo son una sorpresa para el comprador."

*   Casi todo es observable, incluso el esfuerzo, a algún costo.
*   Los altos costos de medición pueden reducir los beneficios netos de vincular la paga al rendimiento.
*   Cuanto mayor el pago de incentivos, más riesgo asume el empleado y más debe gastar la empresa en sistemas de medición para cuantificar los factores aleatorios.
*   Si observar y medir la producción es caro, se buscan **variables proxy** (ej.: maestros evaluados por pruebas estandarizadas).
*   Medidas mal diseñadas fomentan el oportunismo: el engaño y el problema de horizonte.

## Bloque 4 — Stack ranking

### Qué es

Sistema que fuerza a clasificar a todos los empleados en una curva de distribución predefinida. Popularizado por GE (Jack Welch) y usado por Microsoft hasta 2013. También llamado _rank and yank_ o _vitality curve_.

| Ventajas | Desventajas |
| ---| --- |
| Diferencia claramente el desempeño | Destruye el trabajo en equipo y la cooperación |
| Evita la compresión de calificaciones (todos "buenos") | Genera competencia destructiva entre pares |
| Obliga a conversaciones difíciles sobre desempeño | Obliga a despedir buenos empleados en equipos excelentes |
| Identifica y retiene el talento superior | El sesgo del evaluador queda amplificado por el sistema |

### ¿Medición del desempeño o sistema de incentivos?

| Medición del desempeño | Sistema de incentivos |
| ---| --- |
| Observa y cuantifica lo que el empleado hizo | Usa esa información para moldear el comportamiento futuro |
| Produce información sobre el desempeño | Vincula la compensación al desempeño medido |
| Su validez depende de qué tan bien captura lo que la firma valora | Crea un juego estratégico: el empleado optimiza lo que se mide |
| Puede existir sin consecuencias sobre la compensación (función informativa) |  |

**La respuesta:** el stack ranking es fundamentalmente **un sistema de incentivos disfrazado de medición**, y lo hace en modo **relativo**: lo que importa no es tu desempeño absoluto sino superar a tus colegas. Eso convierte la evaluación en un **juego de suma cero** —lo que uno gana en ranking, otro lo pierde— y destruye la cooperación independientemente de cuán buena sea la medición subyacente.

### El experimento de las gallinas (Muir, Purdue, 1996)

William Muir midió productividad de gallinas (fácil de medir: contar huevos).

|  | Jaula A — Súper Gallinas | Jaula B — Mejor Grupo |
| ---| ---| --- |
| Selección | Las gallinas más productoras individualmente | El mejor grupo (podía contener gallinas poco productivas individualmente) |
| Resultado | Se picotearon hasta matarse; quedaron 3 malheridas y casi sin plumas | No se agredían |
| Mortalidad | 89% | Baja |
| Productividad | ↓↓↓ | +160% en el mismo período |

**El argumento del memo a Bezos (Evonomics):** así como los criadores eligen a las súper gallinas individualmente y el resultado es que se destruyen entre sí, las empresas hacen exactamente lo mismo con el stack ranking. Seleccionar solo por desempeño individual maximiza la competencia interna y destruye la cooperación que hace productivo al grupo.

### El experimento mental de Eichenwald (Vanity Fair, 2012)

Imaginá que Microsoft hubiera contratado a Steve Jobs, Mark Zuckerberg, Larry Page, Larry Ellison y Jeff Bezos en el mismo equipo, antes de que se hicieran famosos. Bajo stack ranking, **dos de ellos habrían sido calificados por debajo del promedio y uno habría sido considerado desastroso**. Eso no es un sistema de evaluación del desempeño: es fabricar el fracaso.

Entre 2000 y 2010 Microsoft se estancó mientras sus competidores crecían. Lo eliminó en noviembre de 2013, y su resurgimiento como empresa de nube e innovación siguió poco después.

### Selección adversa: a quién atrae y a quién expulsa

| Atrae y retiene | Expulsa |
| ---| --- |
| Alta tolerancia a la competencia interna, baja aversión al riesgo relativo | Empleados cooperativos y orientados al equipo |
| Habilidades políticas: saben quedar bien en el ranking sin producir más | Los mejores de equipos de alto desempeño, penalizados por la distribución forzada |
| Priorizan el logro personal sobre el del equipo (las "súper gallinas") | Alta aversión al riesgo relativo: prefieren que el esfuerzo se premie en términos absolutos |
| Dispuestos a retener información y sabotear colegas si mejora su posición | Quienes valoran estabilidad y colaboración como condición para trabajar bien |

### Cuándo tiene sentido y cuándo no

**La clave es el grado de interdependencia entre tareas: a mayor interdependencia, mayor el daño.**

| Puede tener sentido | No tiene sentido |
| ---| --- |
| Tareas puramente individuales y medibles: ventas puerta a puerta, trading, trabajo a destajo | Trabajo en equipo e interdependiente: software, investigación, consultoría, salud |
| Procesos de selección inicial: filtrar talento en cohortes grandes y homogéneas | Organizaciones que requieren innovación (compartir información es condición necesaria) |
| Organizaciones con exceso de personal, donde el objetivo real es reducir dotación con criterio aparentemente objetivo | Equipos de alto desempeño homogéneo: la distribución forzada obliga a calificar mal a personas excelentes (Microsoft es el caso paradigmático) |

**Condición necesaria en todos los casos:** output individual observable, baja interdependencia, y que lo que se mide sea lo que la firma realmente valora.

**Cuatro estrategias donde es recomendable:** liderazgo en costos con trabajo estandarizado; selección y filtro en etapas de entrada (up-or-out, que selecciona quién continúa, no gestiona el desempeño de los consolidados); reducción estructural de dotación (administración de la salida, no gestión del desempeño); y mercados de talento escaso con diferencias de impacto extremas (trading, fondos de alto rendimiento, donde la diferencia entre el percentil 90 y el 95 tiene impacto económico real y medible).

### Por qué funcionó en GE

Jack Welch, CEO 1981–2001, implementó la _Vitality Curve_: 20% top, 70% medio, 10% inferior.

1. **Conglomerado diversificado con unidades independientes.** Aviación, energía, finanzas, electrodomésticos: cada unidad era esencialmente autónoma. La interdependencia entre personas de distintas unidades era baja, así que el ranking individual no destruía una cooperación que no era el motor del valor.
2. **Escala y burocracia heredada.** En 1981 GE tenía 400.000 empleados y una cultura fuertemente burocrática. El stack ranking fue un instrumento de transformación cultural: forzó conversaciones sobre desempeño que la organización evitaba.
3. **Output medible en múltiples niveles jerárquicos.** Métricas financieras claras por unidad, división y gerente; el desempeño de los líderes era observable en ingresos, márgenes y retornos. **Lo que se medía se aproximaba bien a lo que la firma valoraba.**

Resultado: GE multiplicó su capitalización bursátil 40 veces entre 1981 y 2001. Post-Welch, tardó décadas en resolver los problemas culturales que dejó.

### El retorno del stack ranking (Fast Company, 2023)

GE lo abandonó porque sus propios líderes de RRHH encontraron que fallaba en capturar el potencial futuro, dañaba la moral y no mejoraba el desempeño. Sin embargo, empresas de Amazon a Meta lo están reviviendo; Corvisio estima que ~30% de las Fortune 500 rankea empleados.

**Las razones del regreso:** (a) la transformación digital permite recolectar mucha más data sobre trabajadores —"el stack ranking es un subproducto de la transformación digital, pero no es necesariamente útil ni preciso"—, (b) la tecnología lo vuelve invisible para el trabajador, porque ocurre a puertas cerradas y no se le comunica dónde quedó, (c) el estilo de liderazgo "radicalmente honesto" de ejecutivos como Musk, y (d) la razón de fondo: **las empresas invierten en stack ranking porque quieren justificar despidos.** "El stack ranking nos permite despedir gente y seguir sintiéndonos una buena empresa."

### Del experimento a las organizaciones

*   **Deportes profesionales (estudio 2014):** en fútbol y básquetbol el talento beneficia a los equipos, pero solo hasta cierto punto. Cuando demasiadas estrellas juegan en el mismo equipo, el rendimiento individual y colectivo disminuye significativamente porque la cooperación se deteriora.
*   **Universidad de Duke, departamento de inglés:** a principios de los 90 contrató a todas las superestrellas literarias disponibles para crear "el mejor departamento del mundo". Resultado: disputas personales, divergencias metodológicas y graves deficiencias curriculares.

> "Cuando seleccionamos el talento priorizando el logro individual sobre el logro del equipo, rara vez obtenemos los resultados que esperamos. Cuando las personas pugnan por dominar, nadie puede concentrarse en la tarea que beneficia al conjunto." — Albert-László Barabási

## Bloque 5 — Evaluación subjetiva

### Por qué se usa

Porque es muy caro medir objetivamente y con precisión todo el output que la firma valora del empleado.

**1\. Sistemas de calificaciones por escalas** — típicamente escala de 5 puntos en múltiples factores: logra objetivos · propone y logra altos niveles de performance · buena comunicación · enfatiza el trabajo en grupo · mantiene conocimientos actualizados · identifica y resuelve problemas · evalúa objetivamente a subordinados · asegura igualdad de oportunidades.

**2\. Sistemas basados en objetivos** — se establecen metas más objetivas para evaluar aspectos subjetivos. Ej.: "realizar tres reuniones mensuales con sus pares" para medir _trabajo en equipo_.

### Los cuatro problemas

**A. Sesgo del evaluador a favor del evaluado.** Es más fácil para los dueños argumentar injustificadamente que el desempeño no fue tan bueno; los supervisores pueden tener incentivos para no dar calificaciones imparciales.

**B. Imposición de distribución a priori.** Para evitar calificaciones infladas, algunas firmas imponen una distribución predefinida. Eso genera su propio problema: buenos empleados reciben calificaciones bajas por pertenecer a equipos de alto rendimiento.

**C. Responsabilizar a los supervisores es difícil de implementar.** Las parcialidades disminuyen si se los hace responsables de la performance futura de quienes progresan gracias a sus evaluaciones, pero en la práctica es muy difícil.

**D. Asimetrías de información sobre el proceso.** El empleado puede no saber cómo es evaluado ni qué peso tiene cada criterio, lo que reduce su capacidad de alinear su comportamiento con los objetivos de la firma.

### ¿Qué medimos realmente? La evidencia

**Mount, Scullen & Goff (Journal of Applied Psychology, 2000)** — estudio con 4.492 gerentes evaluados por jefes, pares y subordinados:

*   **62%** de la variación en las calificaciones se explica por las peculiaridades de percepción de cada evaluador.
*   **21%** se explica por el desempeño real.
*   → **Las calificaciones revelan más sobre el evaluador que sobre el evaluado.**

**Ben Waber (Humanyze) y Chamorro-Premuzic, HBR 2022** — las medidas confiables, precisas y libres de sesgo del desempeño laboral son notoriamente difíciles de alcanzar; autoevaluaciones y calificaciones de supervisión se superponen en apenas un **4%**. La verdadera meritocracia es imposible y el desempeño nunca será completamente mensurable, pero las organizaciones pueden volverse más basadas en el mérito si identifican KPIs concretos y usan los datos correctos para medirlos.

**Implicancia:** si el sistema de evaluación no es válido ni confiable, los incentivos diseñados sobre él serán igualmente distorsionados. **La inversión en sistemas de medición precisos es condición necesaria de la eficiencia organizacional.**

### La autoevaluación

| Dato | Valor |
| ---| --- |
| Autoevaluadores que se clasifican en el 25% superior | 85% |
| Superposición típica entre autoevaluación y calificación del supervisor | 4% (correlación 0,22) |
| Proporción de la autoevaluación no relacionada con la opinión del superior | 96% |

**Las cinco razones de Marc Effron para cuestionarla:**
1. Los empleados creen erróneamente que sus aportes influirán en el resultado de la revisión.
2. Es una revisión, no un debate ni una negociación.
3. Es increíblemente sesgada: los hombres extrovertidos tienen ventaja natural.
4. Los empleados son los observadores **menos precisos** de su propio desempeño.
5. Permite a algunos gerentes no prestarle atención a su gente.

## Bloque 6 — El sistema de Deloitte

### El problema (65.000 empleados)

1. El 58% de los gerentes cree que el enfoque actual de gestión del desempeño no impulsa ni el compromiso ni el alto desempeño.
2. Se fijan objetivos a principios de año y al terminar un proyecto el gerente califica el cumplimiento.
3. Las evaluaciones se consolidan en una calificación de fin de año a través de largas **reuniones de consenso** donde grupos de consejeros discuten sobre cientos de personas.
4. Formularios, reuniones y calificaciones consumían cerca de **2 millones de horas por año** (promedio de 4 días por empleado).

### Los tres objetivos del nuevo sistema

*   **a) Reconocer el desempeño** — a través de la compensación variable, vinculando resultados concretos a la remuneración.
*   **b) Ver el desempeño claramente** — reducir el sesgo del evaluador y agilizar el proceso evaluación-calificación-reunión-calificación final.
*   **c) Mejorar el rendimiento** — retroalimentación accionable y continua, no solo una calificación anual.

**La solución al sesgo:** en lugar de preguntar a más personas su opinión, se pregunta solo al líder inmediato, **pero sobre sus propias acciones futuras respecto de esa persona**. Se cambia el objeto de la pregunta, no la cantidad de evaluadores.

### Las cuatro preguntas (escala 1–5, al final de cada proyecto)

1. Dado lo que conozco del desempeño de esta persona, **si fuera mi dinero**, le otorgaría el mayor aumento de compensación y bonificación posibles.
2. Dado lo que conozco del desempeño de esta persona, **siempre la querría en mi equipo**.
3. Esta persona **corre el riesgo de tener un bajo rendimiento**.
4. Esta persona **está lista para un ascenso hoy**.

## Bloque 7 — Alternativas al stack ranking

No existe una solución única: el sistema óptimo depende del tipo de tarea, la observabilidad del output y el grado de interdependencia.

1. **Evaluación por objetivos absolutos (MBO)** — cada empleado se evalúa contra sus propias metas, no contra sus colegas. Elimina el juego de suma cero. Requiere metas bien calibradas para evitar el efecto trinquete.
2. **Incentivos grupales + evaluación subjetiva calibrada** — parte del bono atado al desempeño del equipo o la unidad; el supervisor evalúa subjetivamente la contribución individual pero rinde cuentas por esas evaluaciones. Reduce la competencia interna.
3. **Sistema de Deloitte — evaluación continua por proyecto** — cuatro preguntas prospectivas al terminar cada proyecto, sin reunión de consenso. Reduce el sesgo y provee retroalimentación en tiempo real.
4. **Compensación de largo plazo (acciones, vesting)** — alinea al empleado con el resultado de la firma en el tiempo, no con su ranking semestral. Reduce el oportunismo de corto plazo.

## Bloque 8 — Evaluación de divisiones y precios de transferencia

**El problema de la interdependencia:** las unidades de una corporación son interdependientes, y muchas veces **el output de una unidad es el input de otra**. Eso hace difícil medir el desempeño de cada una por separado.

**El precio de transferencia** es la variable clave. No solo determina cómo se divide la torta: **también afecta su tamaño**, porque cambia las decisiones de producción y compra de ambas unidades.

**El precio óptimo de transferencia de un bien es su costo de oportunidad**: el valor del bien en su mejor uso alternativo.

Las alternativas en discusión: ¿lo determina la unidad que vende? ¿la que compra? ¿se negocia? ¿precio de mercado, costo marginal o costo total? Es en general un problema complejo en las compañías.

## Taller de cierre — Cadena de restaurantes Vanderschmidt

Jan Vanderschmidt fundó una cadena de restaurantes europea muy exitosa y murió inesperadamente a los 55. Era el único dueño y muy autoritario: tomaba todas las decisiones importantes —desde el menú hasta la provisión de comida y el tipo de publicidad—, pagaba salario fijo a los empleados y los monitoreaba continuamente. Su hijo Joop pasó su juventud manejando BMWs y trabajó muy poco con su padre, pero es inteligente y decidió sucederlo como CEO.

**Hacia dónde va el análisis:** la arquitectura de Jan era internamente consistente —autoridad centralizada + monitoreo directo continuo + salario fijo—, y funcionaba porque el conocimiento específico y la capacidad de monitoreo estaban ambos en la misma persona. Joop no tiene ni el conocimiento del negocio ni la capacidad de monitorear como su padre: si mantiene la centralización, decide mal; si descentraliza sin tocar los otros dos pilares, tendrá gerentes con autoridad, salario fijo y sin monitoreo, es decir, la peor combinación posible. La recomendación es mover los tres pilares juntos: descentralizar decisiones operativas hacia los gerentes de local, construir un sistema de medición por local (que ahora es indispensable porque reemplaza al monitoreo personal) y pasar a compensación variable atada a esas métricas. El taller es el cierre integrador de toda la materia.

## Preguntas de examen que salen de esta clase

Del banco de 68: preguntas **58 a 68** (evaluación para premios y castigos, modelo de Holmström y la variable μ, efecto trinquete, Deloitte, abandono del stack ranking en Microsoft, validez, evaluación subjetiva, β = 0, autoevaluación, GE bajo Welch, equidad). Todas se contestan con el deck.
