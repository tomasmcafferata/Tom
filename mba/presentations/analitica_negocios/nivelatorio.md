> **Curso de Nivelación en Métodos Cuantitativos** · Ing. Carlos Arana · UCEMA MADE
> Página autocontenida: teoría de los 7 módulos, fórmulas, funciones de Excel, los ejemplos del profe y la guía de ejercicios completa con datos y resolución verificada.
> Curso autogestionado: slides + videoclases + guía de ejercicios con clave de corrección.

## Para qué sirve

Es el piso común de estadística descriptiva y probabilidad que dan por sabido las dos materias cuantitativas del programa: **Métodos Cuantitativos para la Toma de Decisiones** e **Introducción a la Ciencia de Datos**.

Toda la analítica de negocios después se apoya en tres ideas de este curso:

1. **Resumir datos** sin engañarse (media vs mediana, dispersión, outliers).
2. **Medir relaciones** entre variables (correlación, y que correlación no es causalidad).
3. **Cuantificar incertidumbre** (probabilidad condicional, binomial, normal).

⚠️ **Condiciones de aprobación:** la carpeta no trae ni formato de examen ni fecha. Confirmar en el campus si hay evaluación y cuánto pesa.

## Mapa del curso

| Módulo | Tema | Pregunta que responde | Videoclases |
| --- | --- | --- | --- |
| 1 | Intro a la estadística descriptiva | ¿Qué tipo de dato tengo? | [Video](https://youtu.be/BQv8zskfghs) |
| 2 | Expresión gráfica | ¿Cómo se distribuyen mis datos? | [Video](https://youtu.be/sLbuv7ae0_I) |
| 3 | Posición, dispersión y medidas robustas | ¿Cuál es el valor típico y cuánto varía? | [Parte 1](https://youtu.be/wb2Z1i4l67I) · [Parte 2](https://youtu.be/61Vj2qexEYk) |
| 4 | Análisis bivariado y correlación | ¿Dos variables se mueven juntas? | [Video](https://youtu.be/z40O-SR0VOE) |
| 5 | Teoría de la probabilidad | ¿Qué tan probable es un evento, y cómo cambia con información nueva? | [P1](https://youtu.be/mdeFgLtX6QE) · [P2](https://youtu.be/4ctxZhpaIK8) · [P3](https://youtu.be/WbXI7C_TrS8) · [P4](https://youtu.be/Po-mvaA7kYw) · [P5](https://youtu.be/QDPcy8Z5iGo) |
| 6 | Variable aleatoria discreta y binomial | ¿Cuántos éxitos espero en n intentos? | [Parte 1](https://youtu.be/IJk4VrcM8OA) · [Parte 2](https://youtu.be/qLhkhJSu8Aw) |
| 7 | Variable aleatoria continua y normal | ¿Qué probabilidad hay de caer en un rango? | [Parte 1](https://youtu.be/3o23-aoNerE) · [Parte 2](https://youtu.be/AHdH0IzQEPQ) |

**Bloque I (Módulos 1 a 4):** estadística descriptiva. Mirar datos que ya tenés.
**Bloque II (Módulos 5 a 7):** probabilidad. Razonar sobre lo que todavía no pasó.

## Plan de estudio sugerido (4 sesiones)

| Sesión | Contenido | Tiempo |
| --- | --- | --- |
| 1 | Módulos 1 y 2 + ejercicios | ~1 h |
| 2 | Módulos 3 y 4 + ejercicios (con Excel abierto) | ~1 h 30 |
| 3 | Módulo 5 + ejercicios | ~1 h 30 |
| 4 | Módulos 6 y 7 + ejercicios + "Resumen de una hoja" | ~1 h 30 |

Método: leer la teoría del módulo acá, ver el video solo si algo no cierra, resolver los ejercicios **tapando la resolución**, y recién después comparar.

* * *

# BLOQUE I · ESTADÍSTICA DESCRIPTIVA

# Módulo 1 · Introducción a la estadística descriptiva

## Conceptos

**Estadística:** ciencia que recoge, organiza, presenta, analiza e interpreta datos para tomar mejores decisiones.
**Estadística descriptiva:** los métodos para organizar, resumir y presentar datos de manera informativa (tablas, gráficos, números).

| Término | Qué es |
| --- | --- |
| Dato | Valor o característica que se observa, cuenta o mide |
| Variable | Característica que puede tomar distintos valores |
| Población (universo) | Conjunto completo de personas u objetos con características comunes |
| Muestra | Subconjunto de la población que efectivamente se observa |

## Tipos de variables (la clasificación del profe)

```
Variable
├── Continua (C): surge de MEDIR, cualquier valor en un rango
└── Discreta (D): surge de CONTAR o de categorizar
     ├── Nominal (DN): categorías sin orden        → sexo, color, forma de pago, sí/no
     ├── Ordinal (DO): categorías con orden natural → nivel educativo, $ / $$ / $$$
     └── Cardinal (DC): número entero, sin valores intermedios → cantidad de hijos, de llamadas
```

**Por momento de obtención:**

*   **Sección transversal:** datos del mismo momento (ej.: ratio P/E de 27 acciones hoy).
*   **Sección longitudinal / serie de tiempo:** datos a lo largo de varios períodos (ej.: ventas mensuales de centros de compras 2018-2019, INDEC).

⚠️ **Trampas de clasificación (según el criterio del profe):**

*   **Montos de dinero = Continua (C).** Factura, alquiler, consumo de electricidad.
*   **Una variable sí/no es Nominal (DN)**, aunque tenga dos valores (¿tiene cocina?, ¿tiene luz?).
*   **Una escala de precios $ a $$$$ es Ordinal (DO)**, aunque use símbolos.
*   **Promedios son Continuos** aunque la variable original sea un conteo (duración promedio de llamadas = C).

### Ejemplo del profe · empresa de telefonía

| Variable | Tipo |
| --- | --- |
| Número de teléfonos celulares en el hogar | DC |
| Duración total (en minutos) de las llamadas al mes | DC |
| Monto de la factura por llamadas nacionales | C |
| Duración promedio de las llamadas de larga distancia | C |
| Monto de la factura por larga distancia | C |
| Número de llamadas a celular el último mes | DC |
| Monto de la factura por llamadas a celular | C |
| Tipo de servicio de internet ("Int50", "Int100+Tel", "Int200+Tel") | DO |
| Forma de pago (efectivo, transferencia, tarjeta, PagoFácil) | DN |

## Guía · Módulo 1

### Ejercicio 1 · Hoteles

Muestra de 9 hoteles. Precio de habitación doble de $ (más bajo) a $$$$ (más alto). Score general: cuanto más alto, más satisfacción.

| Hotel | Precio | Nro. de hab. | Score gral. |
| --- | --- | --- | --- |
| Hotel Lafayette | $$ | 18 | 83,6 |
| Sofitel Hotel | $$$$ | 45 | 73,7 |
| Hotel Continental | $$ | 166 | 86,3 |
| Axsur Design Hotel | $ | 120 | 85,5 |
| Palace Luzern | $$ | 54 | 77,8 |
| Oalladium Business Hotel | $$ | 10 | 76,9 |
| Hotel Sacher | $$$ | 47 | 76,8 |
| Balfer Hotel | $$$ | 22 | 90,6 |
| Palacio Hotel | $ | 326 | 80,9 |

a. ¿Cuántas variables hay? b. Clasificarlas.

**Resolución:** a. **3** (el nombre del hotel identifica la unidad, no es variable de análisis). b. Precio **DO** · Nro. de habitaciones **DC** · Score **C**.

### Ejercicio 2 · Datos INDEC para una constructora

Clasificar: a. tipo de vivienda (particular/colectiva) · b. número de dormitorios · c. si cuenta con cocina · d. número de ocupantes · e. material de paredes y techo · f. material de pisos · g. si cuenta con energía eléctrica · h. consumo mensual promedio de electricidad · i. monto del alquiler.

**Resolución:** a **DN** · b **DC** · c **DN** · d **DC** · e **DN** · f **DN** · g **DN** · h **C** · i **C**.

> Nota: una versión de la clave pone "i. DC". Es inconsistente con el propio criterio del profe (montos de dinero = C). Va **C**.

* * *

# Módulo 2 · Expresión gráfica de la información cuantitativa

## Conceptos

**Distribución de frecuencias:** tabla con todos los valores posibles de una variable y cuántas veces aparece cada uno.

| Columna | Símbolo | Cálculo |
| --- | --- | --- |
| Frecuencia absoluta | fa | Conteo de cada valor |
| Frecuencia relativa | fr | `fr = fa / n` (suma 1, o 100%) |
| Frecuencia acumulada | Fa | Suma de fa hasta ese valor |

**Histograma:** gráfico de barras contiguas de una distribución de frecuencias. Eje horizontal: valores o intervalos de la variable. **Eje vertical: la frecuencia** (cuántas observaciones caen en cada barra).

⚠️ **La trampa del histograma:** el eje vertical **no** es el valor de la variable. Si el histograma es de "cosechadoras vendidas por cliente", la altura de la barra es **cantidad de clientes**, no cantidad de cosechadoras.

### Ejemplo del profe · gaseosas por semana (20 jóvenes)

Datos: 5, 2, 2, 4, 5, 1, 1, 4, 2, 1, 3, 5, 1, 0, 5, 0, 3, 2, 3, 4.

| Nro. de refrescos | fa | fr |
| --- | --- | --- |
| 0 | 2 | 10% |
| 1 | 4 | 20% |
| 2 | 4 | 20% |
| 3 | 3 | 15% |
| 4 | 3 | 15% |
| 5 | 4 | 20% |
| **Total** | **20** | **100%** |

### Ejemplo del profe · libros comprados en el año (32 personas)

Histograma: 0 libros → 1 · 1 → 4 · 2 → 5 · 3 → 10 · 4 → 8 · 5 → 3 · 6 → 0 · 7 → 1.

*   ¿Cuántos compraron 3 o menos? 1 + 4 + 5 + 10 = **20**
*   ¿Qué % compró más de 4? (3 + 0 + 1) / 32 = **12,5%**

⚠️ **"Más de 4" no incluye el 4. "3 o menos" sí incluye el 3.** Leer los bordes es la mitad del ejercicio.

## Guía · Módulo 2

### Ejercicio 1 · Llamadas por día

| Llamadas/día | Frecuencia |
| --- | --- |
| 1 - 4 | 16 |
| 5 - 8 | 11 |
| 9 - 12 | 5 |
| 13 - 16 | 3 |
| 17 - 20 | 1 |

a. ¿Cuántas personas respondieron? b. Tabla de frecuencias relativas. c. ¿Cuántas hacen menos de 9 llamadas? d. ¿Qué proporción y qué porcentaje hace 13 o más?

**Resolución:**

*   a. 16 + 11 + 5 + 3 + 1 = **36**
*   b. 1-4: 16/36 = **0,44** · 5-8: **0,31** · 9-12: **0,14** · 13-16: **0,08** · 17-20: **0,03**
*   c. 16 + 11 = **27**
*   d. (3 + 1)/36 = **0,11** → **11%**. Proporción y porcentaje son lo mismo en distinta escala.

### Ejercicio 2 · Cosechadoras por punto de venta

Histograma (cantidad de cosechadoras vendidas a cada cliente): 0 → 1 · 1 → 4 · 2 → 5 · 3 → 10 · 4 → 8 · 5 → 3 · 6 → 0 · 7 → 1.

a. ¿De qué tipo es? b. ¿El eje de frecuencias representa cosechadoras vendidas? c. ¿A cuántos clientes relevó? d. ¿Qué proporción compró exactamente 5?

**Resolución:** a. De **frecuencias absolutas** (el eje llega a 10, son conteos, no proporciones). b. **No**: representa **cantidad de clientes**. c. Suma de barras = **32**. d. 3/32 = **0,094**.

### Ejercicio 3 · Carrera elegida (63 ingresantes)

Datos crudos (63): Sociología, Adm. de Empresas, Adm. de Empresas, Abogacía, Sociología, Economía, Abogacía, Economía, Sociología, Contador Público, Adm. de Empresas, Psicología, Adm. de Empresas, Economía, Psicología, Ingeniería, Cs. Exactas, Ingeniería, Cs. Sociales, Psicología, Adm. de Empresas, Ingeniería, Ingeniería, Psicología, Abogacía, Psicología, Adm. de Empresas, Economía, Ingeniería, Artes, Cs. Sociales, Cs. Sociales, Ingeniería, Adm. de Empresas, Adm. de Empresas, Adm. de Empresas, Cs. Sociales, Abogacía, Ingeniería, Psicología, Adm. de Empresas, Artes, Psicología, Artes, Artes, Cs. Exactas, Sociología, Abogacía, Economía, Sistemas, Cs. Sociales, Ingeniería, Ingeniería, Cs. Sociales, Ingeniería, Artes, Ingeniería, Sistemas, Adm. de Empresas, Abogacía, Adm. de Empresas, Cs. Sociales, Adm. de Empresas.

a. Tablas de frecuencia absoluta y relativa. b. Carrera más elegida y su %. c. % que elige una de las dos más elegidas.

**Resolución:**

| Carrera | fa | fr |
| --- | --- | --- |
| Adm. de Empresas | 13 | 0,206 |
| Ingeniería | 11 | 0,175 |
| Cs. Sociales | 7 | 0,111 |
| Psicología | 7 | 0,111 |
| Abogacía | 6 | 0,095 |
| Artes | 5 | 0,079 |
| Economía | 5 | 0,079 |
| Sociología | 4 | 0,063 |
| Cs. Exactas | 2 | 0,032 |
| Sistemas | 2 | 0,032 |
| Contador Público | 1 | 0,016 |
| **Total** | **63** | **1** |

*   b. **Adm. de Empresas, 20,6%** (13/63).
*   c. (13 + 11)/63 = **38,1%**.

> Nota: la clave dice 20,31%, que es 13/64. Error de la clave: con 63 datos da **20,63%**.

* * *

# Módulo 3 · Medidas de posición central, dispersión y medidas robustas

## Medidas de posición central

| Medida | Qué es | Fórmula / regla | Excel |
| --- | --- | --- | --- |
| Media | Promedio | `x̄ = Σxᵢ / n` (muestral) · `μ` (poblacional) | `=PROMEDIO()` |
| Mediana | Valor central de los datos ordenados | n impar: el del medio · n par: promedio de los dos del medio | `=MEDIANA()` |
| Moda | Valor que más se repite | El de mayor frecuencia (puede haber varias o ninguna) | `=MODA()` |

**La media es sensible a valores extremos. La mediana no: es una medida ROBUSTA.**

Ejemplo del profe:

*   Muestra 1: 3, 4, 6, 3, 5, 5 → x̄ = 26/6 = **4,33**
*   Muestra 2: 3, 6, 4, 5, 7, **56** → x̄ = 81/6 = **13,5** (un solo dato arrastra la media lejos de donde están los otros cinco)
*   Mediana de la muestra 2: ordenada 3, 4, **5, 6**, 7, 56 → (5 + 6)/2 = **5,5** (no se inmuta)
*   Moda de 1, −5, 13, 4, −8, −4, 5, 6, 1, 11, 5, −5, −6, −5 → **−5** (aparece 3 veces)

**Regla de negocio:** con datos asimétricos o con outliers (salarios, precios, ventas con picos), la mediana describe mejor "el caso típico".

## Asimetría

| Forma | Dónde se concentran los datos | Orden de las medidas |
| --- | --- | --- |
| Simétrica | En el centro | Media = Mediana = Moda |
| Asimétrica a la derecha (positiva) | A la izquierda, con cola larga a la derecha | Moda < Mediana < Media |
| Asimétrica a la izquierda (negativa) | A la derecha, con cola larga a la izquierda | Media < Mediana < Moda |

**Truco mental:** la media siempre "se va hacia la cola". El nombre de la asimetría es el lado de la cola, no el de la montaña.

## Medidas de dispersión

Dos proveedores con el mismo promedio de días de entrega (10) pueden ser muy distintos: el Proveedor 1 entrega siempre entre 9 y 11 días, el Proveedor 2 entre 7 y 15. **La media sola no alcanza: hace falta medir la variabilidad.**

| Medida | Fórmula (muestral) | Excel | Unidades |
| --- | --- | --- | --- |
| Desvío respecto de la media | `(xᵢ − x̄)` | | Las de la variable |
| Varianza muestral | `s² = Σ(xᵢ − x̄)² / (n − 1)` | `=VAR.S()` | Al cuadrado |
| Desvío estándar muestral | `s = √s²` | `=DESVEST.M()` | Las de la variable |

*   **Por qué al cuadrado:** si sumás los desvíos tal cual, los positivos y negativos se cancelan y siempre da 0. Elevando al cuadrado todos suman.
*   **Por qué la raíz:** para volver a las unidades originales ($, días) y poder interpretar.
*   **Por qué n − 1:** es la versión muestral (la del curso). Con la población entera se divide por N y se usa σ.

### Ejemplo del profe · salarios iniciales de 12 egresados de Administración

Datos: 3450, 3550, 3650, 3480, 3355, 3310, 3490, 3730, 3540, 3925, 3520, 3480.

*   x̄ = **3540**
*   Σ(xᵢ − x̄)² = 301.850
*   s² = 301.850 / 11 = **27.440,91**
*   s = √27.440,91 = **165,65**

## Percentiles y cuartiles

**Percentil p:** valor tal que al menos el p% de las observaciones son menores o iguales.

**Método del profe (3 pasos):**

1. Ordenar los datos de menor a mayor.
2. Calcular el índice `i = (p / 100) · n`.
3. Si **i es entero** → percentil = promedio de las posiciones i e i+1. Si **i no es entero** → percentil = el valor en la posición del primer entero mayor que i.

**Cuartiles:** Q1 = percentil 25 · Q2 = percentil 50 = mediana · Q3 = percentil 75.

Ejemplo con los salarios ordenados: 3310, 3355, 3450, 3480, 3480, 3490, 3520, 3540, 3550, 3650, 3730, 3925.

| Medida | i | Resultado |
| --- | --- | --- |
| P85 | 0,85 · 12 = 10,2 → posición 11 | **3730** |
| Q1 | 0,25 · 12 = 3 (entero) → posiciones 3 y 4 | (3450 + 3480)/2 = **3465** |
| Q2 | 0,50 · 12 = 6 → posiciones 6 y 7 | (3490 + 3520)/2 = **3505** |
| Q3 | 0,75 · 12 = 9 → posiciones 9 y 10 | (3550 + 3650)/2 = **3600** |

⚠️ **Excel no usa este método.** `=CUARTIL.INC()` y `=PERCENTIL.INC()` interpolan distinto y dan otros números (Q1 = 3472,5 en este ejemplo). Si piden el percentil "a mano", usar la regla del profe.

**Complemento útil (no está en las slides):** rango intercuartílico `RIC = Q3 − Q1`. Regla estándar de outlier: todo dato fuera de `[Q1 − 1,5·RIC ; Q3 + 1,5·RIC]`.

## Guía · Módulo 3

### Ejercicio 1 · Precios de las 30 acciones del Dow Jones

Datos ($/acción): General Motors 20 · AT&T 25 · Pfizer 25 · Disney 25 · Intel 25 · Microsoft 25 · Alcoa 29 · Hewlett-Packard 32 · Verizon 32 · Merck 33 · General Electric 35 · McDonald's 35 · Honeywell 37 · DuPont 40 · JPMorgan Chase 40 · Coca-Cola 41 · Home Depot 42 · Wal-Mart 45 · Citigroup 49 · American Express 53 · United Technologies 56 · Procter & Gamble 59 · ExxonMobil 61 · Caterpillar 62 · Johnson & Johnson 62 · Boeing 69 · AIG 70 · Altria Group 76 · 3M 78 · IBM 83.

a. Media, mediana y moda. b. Varianza y desvío estándar muestrales.

**Resolución:**

*   Media = 1364 / 30 = **45,47**
*   Mediana: n = 30 par → posiciones 15 y 16 = (40 + 41)/2 = **40,5**
*   Moda = **25** (se repite 5 veces)
*   s² = **331,77** · s = **18,21**

Lectura: media > mediana → asimetría positiva (algunas acciones caras tiran el promedio para arriba).

### Ejercicio 2 · Entrada "Campo VIP" de las 20 mejores giras (U$S)

Bruce Springsteen 122,30 · Dave Matthews Band 44,11 · Aerosmith/KISS 69,52 · Shania Twain 61,80 · Fleetwood Mac 78,34 · Radiohead 39,50 · Cher 64,47 · Counting Crows 36,48 · Timberlake/Aguilera 74,43 · Maná 46,48 · Toby Keith 37,76 · James Taylor 44,93 · Alabama 40,83 · Harper/Johnson 33,70 · 50 Cent 38,89 · Steely Dan 36,38 · Red Hot Chili Peppers 56,82 · R.E.M. 46,16 · American Idols Live 39,11 · Mariah Carey 56,08.

1. Media y mediana. 2. Varianza y desvío. 3. ¿Springsteen es outlier? 4. ¿Qué medida de centralidad usarías?

**Resolución:**

1. Media = **53,40** · Mediana = (44,93 + 46,16)/2 = **45,55** (la clave redondea 45,5)
2. s² = **448,23** · s = **21,17**
3. **Sí.** Está notablemente alejado del resto. Con números: está a 3,25 desvíos de la media, y supera el límite superior del RIC (Q3 + 1,5·RIC ≈ 99,3).
4. **Mediana.** Hay un outlier y la distribución es asimétrica: la media (53,4) queda por encima de 12 de las 20 entradas.

### Ejercicio 3 · Ventas de sidra (miles de unidades)

4,5 · 4 · 3 · 6 · 5 · 3 · 3 · 6 · 7 · 23 · 6,5 · 5 · 8 · 1,5 · 8 · 8,5 · 3 · 2,5 · 2,5 · 3 · 8 · 23,5 · 5,5 · 3

1. Media, mediana y moda. 2. Si son ventas mensuales con estacionalidad marcada, ¿hay outliers?

**Resolución:**

1. Media = 153 / 24 = **6,375** · Mediana = **5** · Moda = **3** (aparece 6 veces)
2. **No.** El 23 y el 23,5 serían las ventas de diciembre (fiestas). Un valor extremo que tiene explicación de negocio **no es un error a descartar**: es información.

⚠️ **Lección del ejercicio:** la estadística detecta valores raros, pero el que decide si son outliers es el contexto. Compararlo con el Ejercicio 2, donde el valor extremo sí se trata como outlier.

* * *

# Módulo 4 · Análisis bivariado y correlación

## Conceptos

**Tabla de pares de valores:** cada observación clasificada según dos variables a la vez (x, y).
**Gráfico de dispersión:** cada punto es un par (x, y). Es lo primero que hay que mirar: muestra dirección, forma y fuerza de la relación.

| Medida | Fórmula | Qué dice | Qué NO dice | Excel |
| --- | --- | --- | --- | --- |
| Covarianza muestral | `sxy = Σ(xᵢ − x̄)(yᵢ − ȳ) / (n − 1)` | **Dirección** de la relación lineal (signo) | La fuerza: depende de las unidades, no tiene escala | `=COVARIANZA.M()` |
| Coeficiente de correlación de Pearson | `r = sxy / (sx · sy)` | **Dirección y fuerza**. Siempre entre −1 y +1 | Causalidad | `=COEF.DE.CORREL()` o `=PEARSON()` |
| Coeficiente de determinación | `R² = r²` | % de la variabilidad de y asociada linealmente a x | Causalidad | `=COEFICIENTE.R2()` |

> El coeficiente de determinación está en el programa del curso pero no aparece en las slides. Se agrega acá porque es lo que viene en Métodos Cuantitativos.

**Por qué funciona la covarianza:** si cuando x está arriba de su media y también está arriba de la suya, el producto `(xᵢ − x̄)(yᵢ − ȳ)` es positivo. Si cuando una sube la otra baja, el producto es negativo. Sumando todos, el signo que domina revela la dirección.

**Por qué hace falta r:** una covarianza de 210.244 no dice si la relación es fuerte o débil (cambia si medís en gramos o kilos). Dividir por los desvíos la estandariza a [−1, +1].

## Interpretación de r (escala del profe)

| r | Lectura |
| --- | --- |
| −1 | Correlación perfecta inversa |
| −1 a −0,5 | Fuerte inversa |
| −0,5 a 0 | Débil / muy débil inversa |
| 0 | No existe relación **lineal** |
| 0 a 0,5 | Débil / muy débil directa |
| 0,5 a 1 | Fuerte directa |
| +1 | Correlación perfecta directa |

*   **r > 0:** relación directa (x sube, y sube).
*   **r < 0:** relación inversa (x sube, y baja).
*   **r ≈ 0:** no hay relación lineal (puede haber una relación no lineal).

⚠️ **Correlación no es causalidad.** Que publicidad y envíos correlacionen 0,89 no prueba que la publicidad cause las ventas: las marcas que más venden también son las que más presupuesto tienen para publicitar. En analítica de negocios esta es la trampa número uno.

### Ejemplo del profe · importador de libros (precio vs peso, 15 libros)

| Precio ($) | 1390 | 745 | 565 | 1445 | 2550 | 800 | 1450 | 1095 | 825 | 990 | 800 | 2100 | 1095 | 940 | 1345 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peso (gr) | 725 | 272 | 520 | 760 | 1874 | 200 | 650 | 738 | 344 | 505 | 430 | 1210 | 487 | 457 | 802 |

1. x̄ = 18.135/15 = **1209** · ȳ = 9974/15 = **664,93**
2. sxy = 2.943.419 / 14 = **210.244** → positiva: relación directa
3. sx = 535,56 · sy = 418
4. r = 210.244 / (535,56 × 418) = **0,94** → directa y fuerte

Uso de negocio: si el precio anticipa el peso, el importador puede estimar el costo de flete de un lote antes de despacharlo.

## Guía · Módulo 4

### Ejercicio 1 · DJIA vs S&P 500 (variación % diaria, 9 días)

| DJIA | 0,20 | 0,82 | −0,99 | 0,04 | −0,24 | 1,01 | 0,30 | 0,55 | −0,25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S&P 500 | 0,24 | 0,19 | −0,91 | 0,08 | −0,33 | 0,87 | 0,36 | 0,83 | −0,16 |

a. Coeficiente de correlación muestral. b. ¿Hace falta mirar ambos índices para tener una idea del mercado diario?

**Resolución:** a. r = **0,91** · b. **No.** La correlación es muy alta: con uno de los dos alcanza para saber hacia dónde fue el mercado ese día.

### Ejercicio 2 · Publicidad vs envíos de las 10 principales cervezas

| Marca | Publicidad (U$S M) | Envíos (M bbl) |
| --- | --- | --- |
| Budweiser | 120,0 | 36,3 |
| Bud Light | 68,7 | 20,7 |
| Miller Lite | 100,1 | 15,9 |
| Coors Light | 76,6 | 13,2 |
| Busch | 8,7 | 8,1 |
| Natural Light | 0,1 | 7,1 |
| Miller Genuine Draft | 21,5 | 5,6 |
| Miller High Life | 1,4 | 4,4 |
| Busch Light | 5,3 | 4,3 |
| Milwaukee's Best | 1,7 | 4,3 |

a. Coeficiente de correlación. b. ¿Positiva o negativa?

**Resolución:** a. r = **0,885** (la clave trunca a 0,88) · b. **Positiva.** Extra: R² = 0,78 → el 78% de la variabilidad de los envíos se asocia linealmente con la publicidad.

* * *

# BLOQUE II · PROBABILIDAD

# Módulo 5 · Teoría de la probabilidad

## Conceptos base

| Término | Qué es | Ejemplo |
| --- | --- | --- |
| Experimento | Proceso de observación que genera resultados | Llamar a un cliente para ofrecerle un producto |
| Espacio muestral (S) | Todos los resultados posibles | {Compró, No compró, Le interesa} |
| Evento | Subconjunto de resultados del espacio muestral | "La suma de dos dados es 3" = {(1,2), (2,1)} |
| Probabilidad | Medida del grado de incertidumbre de un resultado | P(cara) = 0,5 |

**Requisitos de toda asignación de probabilidades:**

1. `0 ≤ P(Eᵢ) ≤ 1` para cada resultado.
2. `Σ P(Eᵢ) = 1`: las probabilidades de todos los resultados suman 1.

**Probabilidad de un evento** = suma de las probabilidades de los resultados que lo componen.

## Tres métodos para asignar probabilidades

| Método | Cuándo se usa | Cálculo | Ejemplo |
| --- | --- | --- | --- |
| Clásico | Todos los resultados son igualmente probables | `P = 1 / n` | Dado: 1/6 |
| Frecuencia relativa | Hay datos históricos | `P = veces que ocurrió / total de observaciones` | 600 de 1500 estudiantes eligen Negocios → 0,40 |
| Subjetivo | No hay datos ni simetría; se usa juicio experto | Grado de confianza del decisor | "Hay 70% de chances de cerrar el deal" |

### Ejemplo del profe · dos dados

*   Espacio muestral: 36 pares, (1,1) a (6,6), cada uno con probabilidad 1/36.
*   Suma = 3 → {(1,2), (2,1)} → 2/36 = **1/18**
*   Suma = 7 → {(1,6), (6,1), (2,5), (5,2), (3,4), (4,3)} → 6/36 = **1/6**
*   Suma = 2 → {(1,1)} → **1/36**. No son igual de probables.

## Operaciones entre eventos

| Operación | Notación | Significado | Regla |
| --- | --- | --- | --- |
| Complemento | Aᶜ | Todo lo que no es A | `P(A) + P(Aᶜ) = 1` |
| Intersección | A ∩ B | A **y** B a la vez | Ley de multiplicación |
| Unión | A ∪ B | A **o** B (o ambos) | Ley de adición |

Ejemplo intersección: dado, A = par {2, 4, 6}, B = múltiplo de 3 {3, 6} → A ∩ B = **{6}**.

## Ley de la adición

`P(A ∪ B) = P(A) + P(B) − P(A ∩ B)`

**Por qué se resta la intersección:** al sumar P(A) y P(B), la zona común se contó dos veces.

*   **Eventos mutuamente excluyentes** (no tienen resultados en común, A ∩ B = ∅): `P(A ∪ B) = P(A) + P(B)`.

Ejemplo del profe: P(elige M) = 0,6 · P(elige F) = 0,55 · P(ambos) = 0,35 → P(M o F) = 0,6 + 0,55 − 0,35 = **0,8**.

## Probabilidad condicional

`P(A | B) = P(A ∩ B) / P(B)`

"Probabilidad de A **sabiendo que** ya ocurrió B". **B pasa a ser el nuevo espacio muestral**: dejás de mirar todo el universo y mirás solo dentro de B.

### Ejemplo del profe · capacitación y premio (400 vendedores)

**Tabla de contingencia (conteos):**

| | Hizo capacitación (C) | No hizo (NC) | Total |
| --- | --- | --- | --- |
| Recibió premio (P) | 38 | 48 | 86 |
| No recibió (NP) | 82 | 232 | 314 |
| **Total** | **120** | **280** | **400** |

**Tabla de probabilidad conjunta (cada celda / 400):**

| | C | NC | Marginal |
| --- | --- | --- | --- |
| P | 0,095 | 0,120 | **0,215** |
| NP | 0,205 | 0,580 | **0,785** |
| **Marginal** | **0,30** | **0,70** | **1** |

*   **Probabilidad conjunta** (el centro de la tabla): P(C ∩ P) = 0,095 → "hizo la capacitación **y** ganó premio".
*   **Probabilidad marginal** (los bordes): P(P) = 0,095 + 0,12 = **0,215** → "ganó premio", sin importar lo demás.
*   **Probabilidad condicional:**
    *   P(P | C) = 0,095 / 0,30 = **0,32**
    *   P(P | NC) = 0,12 / 0,70 = **0,17**

Lectura: entre los que se capacitaron, el 32% gana premio. Entre los que no, el 17%. La capacitación está **asociada** a ganar premio (que la cause es otra discusión: quizás se anotan los más motivados).

⚠️ **La trampa más frecuente del módulo:** confundir conjunta con condicional.

*   "Probabilidad de que un vendedor **haya hecho la capacitación y** gane premio" → conjunta → 0,095.
*   "Probabilidad de que un vendedor **que hizo la capacitación** gane premio" → condicional → 0,32.

La frase "de los que…", "si…", "dado que…", "entre los…" siempre indica condicional.

## Independencia

A y B son **independientes** si saber que ocurrió uno no cambia la probabilidad del otro:

`P(A | B) = P(A)` · o equivalente · `P(B | A) = P(B)`

Si no se cumple, son **dependientes**. En el ejemplo: P(P | C) = 0,32 ≠ P(P) = 0,215 → **dependientes**.

⚠️ **Mutuamente excluyentes ≠ independientes.** Son casi opuestos: si A y B son mutuamente excluyentes y ocurre A, sabés con certeza que B no ocurrió. Eso es la máxima dependencia posible.

## Ley de la multiplicación

Sale de despejar la condicional:

`P(A ∩ B) = P(B) · P(A | B) = P(A) · P(B | A)`

**Para eventos independientes:** `P(A ∩ B) = P(A) · P(B)`

## Probabilidad total y Teorema de Bayes

Cuando el espacio se divide en grupos B₁, B₂, …, Bₙ que no se superponen y cubren todo (Σ P(Bᵢ) = 1):

**Probabilidad total:** `P(A) = Σ P(Bᵢ) · P(A | Bᵢ)`

**Bayes:** `P(Bⱼ | A) = P(Bⱼ) · P(A | Bⱼ) / Σ P(Bᵢ) · P(A | Bᵢ)`

**En criollo:** Bayes "da vuelta" la condicional. Conocés P(síntoma | causa) y querés P(causa | síntoma). Es la base de todo modelo que actualiza una creencia con evidencia nueva (scoring de leads, detección de fraude, diagnóstico).

**Método del árbol:**

1. Primer nivel: los grupos con sus probabilidades P(Bᵢ).
2. Segundo nivel: la condicional P(A | Bᵢ) de cada rama.
3. Multiplicar a lo largo de cada rama → conjunta P(Bᵢ ∩ A).
4. Sumar las ramas que terminan en A → probabilidad total P(A).
5. Rama que te interesa / total → Bayes.

### Ejemplo del profe · aseguradora (marca de auto y póliza tipo R)

Nissan 20% · Volkswagen 14% · Otras 66%. P(R | Nissan) = 0,73 · P(R | VW) = 0,09 · P(R | Otras) = 0,18.

| Rama | P(marca) | P(R ∣ marca) | P(marca ∩ R) |
| --- | --- | --- | --- |
| Nissan | 0,20 | 0,73 | 0,1460 |
| Volkswagen | 0,14 | 0,09 | 0,0126 |
| Otras | 0,66 | 0,18 | 0,1188 |
| **P(R) total** | | | **0,2774** |

a. P(R) = **0,2774**
b. P(VW | R) = 0,0126 / 0,2774 = **0,0454**

⚠️ **Error en la slide del profe:** la slide pone 0,1460 en el numerador y llega a 0,5263. Ese número es **P(Nissan | R)**, no P(VW | R). La respuesta correcta a la pregunta planteada es **0,0454 (4,5%)**. Tiene sentido: VW casi no contrata pólizas R (9%), así que entre los autos con póliza R hay muy pocos VW.

## Guía · Módulo 5

### Ejercicio 1 · Viajeros de un sitio de turismo

En los últimos 12 meses: 45,8% viajó por trabajo, 54% por turismo y 25% por trabajo y turismo.

a. P(trabajo o turismo). b. P(ni trabajo ni turismo).

**Resolución:**

*   a. Ley de adición: 0,458 + 0,54 − 0,25 = **0,748 ≈ 0,75**
*   b. Complemento: 1 − 0,748 = **0,252 ≈ 0,25**

> El enunciado dice "25% por razones de trabajo y personales". Es un error de tipeo: se refiere a trabajo y turismo (si no, el ejercicio no se puede resolver).

### Ejercicio 2 · Ocupación y género (EE.UU., millones de personas de 25 a 64 años)

| Ocupación | Hombres | Mujeres |
| --- | --- | --- |
| Directivo/Profesional | 19.079 | 19.021 |
| Enseñanza/Ventas/Administrativo | 11.079 | 19.315 |
| Servicio | 4.977 | 7.947 |
| Producción con precisión | 11.682 | 1.138 |
| Operadores/Obrero | 10.576 | 3.482 |
| Agricultura/Ganadería/Silvicultura/Pesca | 1.838 | 514 |

a. Tabla de probabilidad conjunta. b. P(directivo/profesional | mujer). c. P(producción con precisión | hombre). d. ¿La ocupación es independiente del género?

**Resolución:**

a. Total = 110.648. Cada celda / 110.648:

| Ocupación | Hombres | Mujeres | Marginal |
| --- | --- | --- | --- |
| Directivo/Profesional | 0,172 | 0,172 | 0,344 |
| Enseñanza/Ventas/Adm. | 0,100 | 0,175 | 0,275 |
| Servicio | 0,045 | 0,072 | 0,117 |
| Producción con precisión | 0,106 | 0,010 | 0,116 |
| Operadores/Obrero | 0,096 | 0,031 | 0,127 |
| Agro/Pesca | 0,017 | 0,005 | 0,021 |
| **Marginal** | **0,535** | **0,465** | **1** |

b. P(Dir | M) = 0,172 / 0,465 = **0,37**
c. P(Prod | H) = 0,106 / 0,535 = **0,197**
d. **No son independientes.** Para que lo fueran, P(ocupación | género) debería ser igual a P(ocupación) en todas las filas. Ejemplo claro: P(Producción | H) = 0,197 vs P(Producción) = 0,116 vs P(Producción | M) = 0,022. La única fila donde se acercan es Directivo/Profesional (0,32 hombres, 0,37 mujeres, 0,34 total), que es lo que la clave quiere decir con "sólo en Dir/Prof".

> ⚠️ Hay una versión de la clave que da b = 0,17 y c = 0,11. Son las **conjuntas** ("mujer y directiva"), no las condicionales que pide el enunciado ("una trabajadora mujer"). Van **0,37 y 0,197**.

### Ejercicio 3 · Seguro médico por edad

| Edad | Con seguro (SÍ) | Sin seguro (NO) |
| --- | --- | --- |
| 18 a 34 | 750 | 170 |
| 35 o más | 950 | 130 |

a. Tabla de probabilidad conjunta. b. P(sin seguro). c. P(sin seguro | 18-34). d. P(sin seguro | 35+). e. P(18-34 | sin seguro).

**Resolución:**

a. Total = 2000:

| Edad | SÍ | NO | Marginal |
| --- | --- | --- | --- |
| 18 a 34 | 0,375 | 0,085 | 0,46 |
| 35 o más | 0,475 | 0,065 | 0,54 |
| **Marginal** | **0,85** | **0,15** | **1** |

*   b. P(NO) = **0,15**
*   c. P(NO | 18-34) = 0,085 / 0,46 = **0,1848**
*   d. P(NO | 35+) = 0,065 / 0,54 = **0,12**
*   e. P(18-34 | NO) = 0,085 / 0,15 = **0,567**

Comparar c y e: **P(NO | joven) = 18% pero P(joven | NO) = 57%**. Misma celda, distinto denominador. Es exactamente la diferencia que Bayes formaliza.

* * *

# Módulo 6 · Variables aleatorias discretas y distribución binomial

## Conceptos

**Variable aleatoria:** descripción numérica del resultado de un experimento. Convierte resultados en números para poder operar.

| Experimento | Variable aleatoria X | Valores posibles |
| --- | --- | --- |
| Lanzar una moneda 4 veces | Número de caras | 0, 1, 2, 3, 4 |
| Control de calidad de 10 celulares | Celulares con defecto | 0, 1, …, 10 |
| Concierto en el Gran Rex | Número de asistentes | 0, 1, …, 3300 |

**Discreta:** toma valores contables (conteos). **Continua:** toma cualquier valor en un intervalo (Módulo 7).

**Distribución de probabilidad:** describe cómo se reparten las probabilidades entre los valores de X. Propiedades: `0 ≤ P(xᵢ) ≤ 1` y `Σ P(xᵢ) = 1`. Se presenta en forma tabular, gráfica (barras) o como función.

Ejemplo dado: P(X = x) = 1/6 para x = 1…6 → P(par) = 3/6 = **0,5** · P(X < 3) = P(1) + P(2) = **0,333**.

## Media (valor esperado) y varianza

| Medida | Fórmula | Lectura |
| --- | --- | --- |
| Valor esperado | `μ = E(X) = Σ xᵢ · P(xᵢ)` | Promedio de largo plazo si el experimento se repitiera muchas veces |
| Varianza | `σ² = Σ P(xᵢ) · (xᵢ − μ)²` | Dispersión alrededor de μ |
| Desvío estándar | `σ = √σ²` | En unidades de X |

**Diferencia con el Módulo 3:** allá se promediaban datos observados (cada dato pesa 1/n). Acá cada valor se pondera por **su probabilidad**.

⚠️ **E(X) no tiene por qué ser un valor posible.** "Se esperan 1,5 autos vendidos por día" es correcto aunque nunca se vendan 1,5 autos.

### Ejemplo del profe · autos vendidos por día (concesionaria)

| x | P(x) | x · P(x) | (x − μ)² | P(x) · (x − μ)² |
| --- | --- | --- | --- | --- |
| 0 | 0,18 | 0 | 2,25 | 0,405 |
| 1 | 0,39 | 0,39 | 0,25 | 0,0975 |
| 2 | 0,24 | 0,48 | 0,25 | 0,06 |
| 3 | 0,14 | 0,42 | 2,25 | 0,315 |
| 4 | 0,04 | 0,16 | 6,25 | 0,25 |
| 5 | 0,01 | 0,05 | 12,25 | 0,1225 |
| **Σ** | **1** | **μ = 1,5** | | **σ² = 1,25** |

σ = √1,25 = **1,12** autos.

## Distribución binomial

Cuenta la **cantidad de éxitos en n ensayos**. Sirve para todo lo que es "de n casos, ¿cuántos cumplen?": clientes que compran, piezas defectuosas, leads que responden.

**Las 4 condiciones de un experimento binomial (verificarlas siempre):**

1. **n ensayos idénticos.**
2. **Dos resultados** posibles por ensayo: éxito o fracaso.
3. **p constante**: la probabilidad de éxito no cambia de un ensayo a otro.
4. **Ensayos independientes**: uno no afecta a los otros.

**Función binomial:**

`P(X = x) = C(n, x) · pˣ · (1 − p)ⁿ⁻ˣ` · con `C(n, x) = n! / [x! · (n − x)!]`

| Término | Qué es |
| --- | --- |
| n | Número de ensayos |
| x | Número de éxitos buscado |
| p | Probabilidad de éxito en cada ensayo |
| C(n, x) | De cuántas formas distintas se pueden ubicar los x éxitos entre los n ensayos |
| pˣ · (1 − p)ⁿ⁻ˣ | Probabilidad de **una** secuencia concreta con x éxitos |

**Lógica:** la probabilidad de una secuencia puntual (ej.: compra, compra, no compra) es 0,3 · 0,3 · 0,7. Pero hay varias secuencias con 2 compras; C(3, 2) = 3 las cuenta.

**Media y varianza de la binomial (complemento):** `E(X) = n · p` · `Var(X) = n · p · (1 − p)`.

### Ejemplo del profe · 3 clientes, P(compra) = 0,30

| x | Cálculo | P(x) |
| --- | --- | --- |
| 0 | 1 · 0,3⁰ · 0,7³ | 0,343 |
| 1 | 3 · 0,3¹ · 0,7² | 0,441 |
| 2 | 3 · 0,3² · 0,7¹ | **0,189** |
| 3 | 1 · 0,3³ · 0,7⁰ | 0,027 |
| **Σ** | | **1** |

## Binomial en Excel

`=DISTR.BINOM.N(núm_éxito; ensayos; prob_éxito; acumulado)` (en versiones viejas: `DISTR.BINOM`, mismos argumentos)

*   `acumulado = FALSO` → P(X = x) (probabilidad puntual)
*   `acumulado = VERDADERO` → P(X ≤ x) (acumula **desde 0 hasta x inclusive**)

**Traducción de frases a Excel (la parte que más se equivoca):**

| Frase | Probabilidad | Excel |
| --- | --- | --- |
| "exactamente 3" | P(X = 3) | `DISTR.BINOM.N(3; n; p; FALSO)` |
| "a lo sumo 3" / "no más de 3" | P(X ≤ 3) | `DISTR.BINOM.N(3; n; p; VERDADERO)` |
| "menos de 3" | P(X ≤ 2) | `DISTR.BINOM.N(2; n; p; VERDADERO)` |
| "más de 3" | 1 − P(X ≤ 3) | `1 − DISTR.BINOM.N(3; n; p; VERDADERO)` |
| "3 o más" / "al menos 3" | 1 − P(X ≤ 2) | `1 − DISTR.BINOM.N(2; n; p; VERDADERO)` |
| "ninguno" | P(X = 0) | `DISTR.BINOM.N(0; n; p; FALSO)` |

⚠️ **En la discreta, "menos de 3" y "a lo sumo 3" son distintos** (el 3 entra o no entra). En la continua (Módulo 7) da igual.

### Ejemplo del profe · n = 5, p = 0,4

Distribución: P(0) = 0,0778 · P(1) = 0,2592 · P(2) = 0,3456 · P(3) = 0,2304 · P(4) = 0,0768 · P(5) = 0,0102.

*   a. P(X = 1) = `DISTR.BINOM(1;5;0,4;FALSO)` = **0,2592**
*   b. P(X < 2) = P(0) + P(1) = `DISTR.BINOM(1;5;0,4;VERDADERO)` = **0,3370**
*   c. P(X > 2) = P(3) + P(4) + P(5) = 1 − P(X ≤ 2) = `1-DISTR.BINOM(2;5;0,4;VERDADERO)` = **0,3174**

## Guía · Módulo 6

### Ejercicio 1 · Pagos por choques de una aseguradora

| Pago ($) | 0 | 500 | 1000 | 3000 | 5000 | 8000 | 10000 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Probabilidad | 0,85 | 0,04 | 0,04 | 0,03 | 0,02 | 0,01 | 0,01 |

a. Con el pago esperado, ¿qué prima permite cubrir los gastos? b. P(pagar entre 3000 y 8000).

**Resolución:**

*   a. E(X) = 0 + 500·0,04 + 1000·0,04 + 3000·0,03 + 5000·0,02 + 8000·0,01 + 10000·0,01 = 20 + 40 + 90 + 100 + 80 + 100 = **$430**. Esa es la prima de equilibrio (sin ganancia ni gastos administrativos).
*   b. P(3000) + P(5000) + P(8000) = 0,03 + 0,02 + 0,01 = **0,06**

Esto es literalmente cómo se tarifa un seguro: prima = pérdida esperada + margen.

### Ejercicio 2 · Demanda mensual de un producto

| Demanda (unidades) | 300 | 400 | 500 | 600 |
| --- | --- | --- | --- | --- |
| Probabilidad | 0,20 | 0,30 | 0,35 | 0,15 |

a. Si la orden mensual se basa en la demanda esperada, ¿cuánto se ordena? b. Si cada unidad vendida deja $70 y cada unidad ordenada cuesta $50, ¿resultado del mes si se ordena lo de (a) y la demanda real fue 300?

**Resolución:**

*   a. E(D) = 300·0,2 + 400·0,3 + 500·0,35 + 600·0,15 = 60 + 120 + 175 + 90 = **445 unidades**
*   b. Ingreso: 300 × 70 = 21.000 · Costo: 445 × 50 = 22.250 → **−$1.250**

Lección: decidir por el valor esperado no protege del mes malo. Sobra stock en 2 de cada 10 meses.

### Ejercicio 3 · Piezas defectuosas (p = 0,03, n = 2)

a. P(ninguna defectuosa). b. P(exactamente una). c. P(las dos).

**Resolución:**

*   a. 0,97² = **0,9409 ≈ 0,94**
*   b. 2 · 0,03 · 0,97 = **0,0582**
*   c. 0,03² = **0,0009**

Control: 0,9409 + 0,0582 + 0,0009 = 1.

### Ejercicio 4 · Estudiantes con saldo de tarjeta > $7000 (p = 0,09, n = 10)

a. P(exactamente 2). b. P(ninguno). c. P(3 o más).

**Resolución:**

*   a. C(10,2) · 0,09² · 0,91⁸ = 45 · 0,0081 · 0,4702 = **0,1714** → `DISTR.BINOM.N(2;10;0,09;FALSO)`
*   b. 0,91¹⁰ = **0,3894 ≈ 0,39** → `DISTR.BINOM.N(0;10;0,09;FALSO)`
*   c. 1 − P(X ≤ 2) = 1 − (0,3894 + 0,3851 + 0,1714) = **0,054** → `1-DISTR.BINOM.N(2;10;0,09;VERDADERO)`

### Ejercicio 5 · Trabajadores que usan transporte público (p = 0,30, n = 10)

a. P(exactamente 3). b. P(no más de 3).

**Resolución:**

*   a. C(10,3) · 0,3³ · 0,7⁷ = 120 · 0,027 · 0,0824 = **0,2668**
*   b. P(X ≤ 3) = 0,0282 + 0,1211 + 0,2335 + 0,2668 = **0,6496** → `DISTR.BINOM.N(3;10;0,3;VERDADERO)`

* * *

# Módulo 7 · Variable aleatoria continua y distribución normal

## Conceptos

**Variable aleatoria continua:** representa mediciones y puede tomar cualquier valor dentro de un intervalo (tiempo, peso, precio, ingreso).

Si hacés un histograma con intervalos cada vez más angostos (de 15 minutos a 1 minuto), las barras se afinan y el contorno se vuelve una **curva suave**. Esa curva es la función de densidad.

**Función de densidad de probabilidad f(x):** la probabilidad de que X caiga en un intervalo [a, b] es **el área bajo la curva** entre a y b. El área total bajo la curva es 1.

⚠️ **Consecuencias que se preguntan:**

*   **P(X = un valor exacto) = 0.** Un punto no tiene área. Solo tiene sentido preguntar por intervalos.
*   Por eso en la continua **P(X < a) = P(X ≤ a)**. "Al menos", "más de", "inclusive" dan lo mismo en los bordes.
*   **f(x) no es una probabilidad.** Es una altura; la probabilidad es el área.

## Distribución normal (campana de Gauss)

`f(x) = [1 / (σ√2π)] · e^(−(x − μ)² / 2σ²)` (no hace falta calcularla a mano: se usa Excel)

**Características:**

1. **Dos parámetros:** la media μ (dónde está el centro) y el desvío σ (qué tan ancha es).
2. **Media = mediana = moda.**
3. **Simétrica** respecto de μ: tan probable caer a cierta distancia por debajo como por encima.
4. **σ determina la forma:** σ chico → campana alta y angosta · σ grande → baja y ancha.

Muchas variables reales se comportan así: alturas, pesos, errores de medición, llenado de una máquina.

## Regla empírica (68-95-99,7)

| Intervalo | Probabilidad adentro | En cada cola |
| --- | --- | --- |
| μ ± 1σ | **0,68** | 0,16 |
| μ ± 2σ | **0,95** | 0,025 |
| μ ± 3σ | **0,997** | 0,0015 |

**Cómo usar las colas:** como la curva es simétrica, lo que queda afuera se reparte mitad y mitad. Fuera de μ ± 1σ queda 0,32 → **0,16 de cada lado**.

### Ejemplo del profe · horas por mes en una red social (μ = 10, σ = 3)

| Pregunta | Razonamiento | Respuesta |
| --- | --- | --- |
| P(entre 4 y 16 hs) | 4 y 16 = μ ± 2σ | **0,95** |
| ¿Entre qué valores está casi garantizado (0,997)? | μ ± 3σ | **1 y 19 hs** |
| ¿Qué valor supera solo el 2,5%? | Cola derecha de μ + 2σ | **16 hs** |
| P(menos de 7 hs) | 7 = μ − 1σ → cola izquierda | **0,16** (no tan improbable) |
| P(más de 19 hs) | 19 = μ + 3σ → cola derecha | **0,0015** (extremadamente improbable) |

> Fe de erratas del profe: en el video la última respuesta figura como 0,015. La correcta es 0,0015.

## Normal en Excel

`=DISTR.NORM.N(x; media; desv_estándar; VERDADERO)` (en versiones viejas: `DISTR.NORM`) → devuelve **P(X < x)**

⚠️ **Excel siempre acumula a izquierda.** Da el área desde −∞ hasta x.

| Pregunta | Fórmula |
| --- | --- |
| P(X < a) | `DISTR.NORM.N(a; μ; σ; VERDADERO)` |
| P(X > a) | `1 − DISTR.NORM.N(a; μ; σ; VERDADERO)` |
| P(a < X < b) | `DISTR.NORM.N(b; μ; σ; VERDADERO) − DISTR.NORM.N(a; μ; σ; VERDADERO)` |
| ¿Qué valor deja un área p a su izquierda? | `INV.NORM(p; μ; σ)` (complemento) |

**El último argumento va siempre VERDADERO.** Con FALSO devuelve la altura de la curva, que no es una probabilidad.

**Estandarización (complemento, por si no hay Excel):** `z = (x − μ) / σ` = a cuántos desvíos de la media está x. Toda normal se convierte en la normal estándar (μ = 0, σ = 1), y z se busca en la tabla. Ejemplo: x = 12,25 con μ = 10 y σ = 3 → z = 0,75.

### Ejemplo del profe · red social (μ = 10, σ = 3)

*   P(X < 12,25) = `DISTR.NORM(12,25;10;3;VERDADERO)` = **0,77**
*   P(X > 6) = `1 - DISTR.NORM(6;10;3;VERDADERO)` = **0,91**

## Guía · Módulo 7

### Ejercicio 1 · Precio de acciones del S&P 500 (μ = $30, σ = $8,20)

a. P(precio de por lo menos $40). b. P(precio no mayor a $20).

**Resolución:**

*   a. P(X ≥ 40) = `1 - DISTR.NORM.N(40;30;8,2;VERDADERO)` = **0,111** (z = 1,22)
*   b. P(X ≤ 20) = `DISTR.NORM.N(20;30;8,2;VERDADERO)` = **0,111** (z = −1,22)

Dan igual por simetría: 20 y 40 están a la misma distancia de 30. Si ves eso, te ahorrás la segunda cuenta.

### Ejercicio 2 · Ingreso per cápita (μ = $1500, σ = $500)

a. P(ingreso > $2000). b. P(entre $750 y $1500).

**Resolución:**

*   a. 2000 = μ + 1σ → cola derecha de la regla empírica = **0,16**. Excel: `1-DISTR.NORM.N(2000;1500;500;VERDADERO)` = 0,1587.
*   b. `DISTR.NORM.N(1500;…) − DISTR.NORM.N(750;…)` = 0,5 − 0,0668 = **0,433**. Atajo: P(X < μ) = 0,5 siempre.

### Ejercicio 3 · Máquina de llenado de agua mineral

La cantidad vertida sigue una normal con media 500 ml y **varianza 25** ml².

a. ¿Qué % de botellas se llena con entre 490 y 507 ml? b. ¿Por qué entre 490 y 510 ml está el 95%?

**Resolución:**

*   **Primero: σ = √25 = 5 ml.** Dan la varianza, no el desvío.
*   a. `DISTR.NORM.N(507;500;5;VERDADERO) − DISTR.NORM.N(490;500;5;VERDADERO)` = 0,9192 − 0,0228 = **0,8965 ≈ 90%**
*   b. Porque 490 y 510 son **μ ± 2σ** (500 ± 2·5), y ahí cae el 95% por la regla empírica.

> ⚠️ **Las dos versiones de la guía se contradicen.** La guía por módulo tiene clave a = 0,26 y pregunta por "450 y 550 ml". Eso sale de usar σ = 25, es decir, tratar la varianza como si fuera el desvío. La guía unificada usa σ = 5, pregunta por 490-510 y da 0,89. Lo correcto con el enunciado es **σ = 5 → 0,8965**. Es justamente la trampa que el ejercicio quiere probar.

### Ejercicio 4 · Horas conectado a internet en el trabajo (μ = 77 hs, σ = 20 hs)

a. P(menos de 50 hs). b. % que pasó más de 100 hs.

**Resolución:**

*   a. `DISTR.NORM.N(50;77;20;VERDADERO)` = **0,0885** (z = −1,35)
*   b. `1-DISTR.NORM.N(100;77;20;VERDADERO)` = **0,1251 → 12,5%** (z = 1,15)

* * *

# Fe de erratas del material

Errores encontrados al verificar cada número con Python. En todos los casos la versión correcta es la que figura arriba.

| Dónde | Qué dice | Qué es correcto | Por qué |
| --- | --- | --- | --- |
| Slides M5 · Bayes aseguradora | P(VW ∣ R) = 0,1460/0,2774 = 0,5263 | **0,0126/0,2774 = 0,0454** | Usa la rama de Nissan en el numerador |
| Guía M7 Ej. 3 (versión por módulo) | a = 0,26 · "entre 450 y 550 ml" | **σ = 5 → 0,8965 · entre 490 y 510** | Toma la varianza (25) como desvío |
| Clave M5 Ej. 2 (versión unificada) | b = 0,17 · c = 0,11 | **b = 0,37 · c = 0,197** | Da conjuntas; el enunciado pide condicionales |
| Clave M2 Ej. 3 b | 20,31% | **20,63%** | Divide por 64 en lugar de 63 |
| Clave M1 Ej. 2 i (versión por módulo) | Monto de alquiler = DC | **C** | Contradice el criterio "montos = continua" |
| Enunciado M5 Ej. 1 | "trabajo y personales" | **trabajo y turismo** | Tipeo |
| Slides M5 · capacitación | "1200 vendedores" | **400** | La tabla suma 400 |
| Slides M6 · concesionaria | 57 días sin ventas → P(0) = 0,18 | Con 57 los días suman 303 | La tabla de probabilidades (0,18) es la que vale |

* * *

# Resumen de una hoja

## Fórmulas

| Tema | Fórmula |
| --- | --- |
| Frecuencia relativa | `fr = fa / n` |
| Media | `x̄ = Σxᵢ / n` |
| Varianza muestral | `s² = Σ(xᵢ − x̄)² / (n − 1)` |
| Desvío estándar | `s = √s²` |
| Índice de percentil | `i = (p/100) · n` → entero: promedio de i e i+1 · no entero: siguiente posición |
| Covarianza muestral | `sxy = Σ(xᵢ − x̄)(yᵢ − ȳ) / (n − 1)` |
| Correlación de Pearson | `r = sxy / (sx · sy)` |
| Determinación | `R² = r²` |
| Complemento | `P(Aᶜ) = 1 − P(A)` |
| Adición | `P(A ∪ B) = P(A) + P(B) − P(A ∩ B)` |
| Condicional | `P(A ∣ B) = P(A ∩ B) / P(B)` |
| Multiplicación | `P(A ∩ B) = P(B) · P(A ∣ B)` |
| Independencia | `P(A ∣ B) = P(A)` ⇔ `P(A ∩ B) = P(A) · P(B)` |
| Probabilidad total | `P(A) = Σ P(Bᵢ) · P(A ∣ Bᵢ)` |
| Bayes | `P(Bⱼ ∣ A) = P(Bⱼ) · P(A ∣ Bⱼ) / P(A)` |
| Valor esperado | `E(X) = Σ xᵢ · P(xᵢ)` |
| Varianza de v.a. | `σ² = Σ P(xᵢ) · (xᵢ − μ)²` |
| Binomial | `P(X = x) = C(n,x) · pˣ · (1−p)ⁿ⁻ˣ` · `E(X) = np` |
| Estandarización | `z = (x − μ) / σ` |
| Regla empírica | μ±1σ: 68% · μ±2σ: 95% · μ±3σ: 99,7% |

## Excel

| Qué | Función |
| --- | --- |
| Media · Mediana · Moda | `PROMEDIO` · `MEDIANA` · `MODA` |
| Varianza · Desvío (muestrales) | `VAR.S` · `DESVEST.M` |
| Covarianza muestral | `COVARIANZA.M` |
| Correlación | `COEF.DE.CORREL` o `PEARSON` |
| R² | `COEFICIENTE.R2` |
| Binomial | `DISTR.BINOM.N(x; n; p; FALSO = puntual / VERDADERO = acumulada ≤ x)` |
| Normal | `DISTR.NORM.N(x; μ; σ; VERDADERO)` → P(X < x) |
| Normal inversa | `INV.NORM(prob; μ; σ)` |

## Checklist de trampas

| # | Trampa | Regla |
| --- | --- | --- |
| 1 | Montos de dinero | Continua, no cardinal |
| 2 | Eje vertical del histograma | Es la frecuencia, no el valor de la variable |
| 3 | Media con outliers | Usar mediana |
| 4 | Outlier con explicación de negocio | No se descarta (sidra en diciembre) |
| 5 | Varianza muestral | Dividir por n − 1 |
| 6 | Percentil a mano | Regla del profe, no `PERCENTIL.INC` |
| 7 | Covarianza grande = relación fuerte | Falso: la fuerza la da r |
| 8 | Correlación alta | No implica causalidad |
| 9 | "Y" vs "dado que" | Conjunta vs condicional |
| 10 | Excluyentes vs independientes | Excluyentes con P > 0 son dependientes |
| 11 | Bayes | Numerador = la rama que te preguntan |
| 12 | "Menos de 3" en la binomial | P(X ≤ 2) |
| 13 | "3 o más" en la binomial | 1 − P(X ≤ 2) |
| 14 | Excel normal | Acumula a izquierda: P(X > a) = 1 − … |
| 15 | Dan la varianza en la normal | Sacar la raíz antes de usar σ |
| 16 | Continua | P(X = a) = 0, así que < y ≤ dan igual |
