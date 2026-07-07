# MW-BING-WEBMASTER-SEARCH-PERFORMANCE-KEYWORDS-EXPORT-013J2

Fecha: 2026-07-05  
Modo: solo lectura / análisis de CSV / sin cambios en Shopify, Bing, IndexNow ni configuración externa.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `baseline-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J-2026-07-05.md`
- `analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-FULL-EXPORT-013J1-2026-07-05.md`
- `registro-cambios-ejecutados.md`

## Archivo recibido

`VERIFICADO Y CORRECTO`

Daniel aportó el export de Bing Webmaster Tools:

`C:\Users\d.bermejo\OneDrive - Matchwalls\Escritorio\matchwalls.com_KeywordReport_7_5_2026 BBBBBBB.csv`

Columnas detectadas:

- `Keyword`
- `Impressions`
- `Clicks`
- `CTR`
- `Avg. Position`

Esto confirma que el archivo corresponde a `Search Performance > List By > Keywords`.

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

El CSV contiene:

- Keywords exportadas: `88`
- Impresiones en el export de keywords: `131`
- Clics en el export de keywords: `3`
- CTR calculado sobre queries visibles: `2,29%`
- Posición media ponderada por impresión: `6,43`

Importante: este export de keywords no suma las `749` impresiones del overview 013J/013J1. Esto se trata como limitación del desglose disponible en Bing, no como error de MatchWalls. Bing puede agrupar u ocultar parte de las queries por privacidad, volumen o reglas internas.

## Distribución por idioma/señal de mercado

`VERIFICADO PERO MEJORABLE`

| Idioma / señal | Queries | Impresiones | Clics | Estado |
|---|---:|---:|---:|---|
| ES | 64 | 93 | 1 | `VERIFICADO PERO MEJORABLE` |
| EN / mixto | 9 | 16 | 0 | `VERIFICADO PERO MEJORABLE` |
| FR | 2 | 4 | 0 | `VERIFICADO PERO MEJORABLE` |
| PT | 9 | 13 | 1 | `STANDBY` |
| IT | 2 | 2 | 0 | `STANDBY` |
| Marca con typo | 1 | 2 | 1 | `VERIFICADO PERO MEJORABLE` |
| Ruido/corrupción de export | 1 | 1 | 0 | `INCORRECTO` |

No aparecen señales claras DE ni NL en este export de 3 meses. Esto no demuestra ausencia de demanda; solo indica que Bing no las muestra en el desglose disponible.

## Distribución por intención

`VERIFICADO PERO MEJORABLE`

| Intención | Queries | Impresiones | Clics | Lectura |
|---|---:|---:|---:|---|
| Producto / color / patrón / estilo | 48 | 78 | 1 | Núcleo principal de demanda visible |
| Mural personalizado / proyecto | 13 | 17 | 1 | Interés útil para personalización y B2B |
| Geo / local | 8 | 16 | 0 | Señal geográfica, todavía insuficiente para crear páginas nuevas |
| Medición / instalación / mantenimiento | 11 | 11 | 0 | Base para guías citables y calculadoras |
| Consulta genérica o ambigua | 6 | 6 | 0 | Mantener en observación |
| Marca con typo | 1 | 2 | 1 | Monitorización defensiva |
| Ruido técnico/export | 1 | 1 | 0 | No accionar |

## Queries de prioridad alta

`VERIFICADO PERO MEJORABLE`

| Query | Imp. | Clics | Pos. media | Motivo |
|---|---:|---:|---:|---|
| `papel pasillo plus` | 8 | 0 | 3,75 | Mayor volumen visible del export |
| `papel pintado negro` | 6 | 0 | 8,83 | Producto/color prioritario |
| `wall decoration interior salamanca` | 5 | 0 | 6,00 | Señal geo/local EN-mixta |
| `papel pintado de tartán beige` | 4 | 0 | 5,00 | Patrón/color con posición útil |
| `wall decoration interior tarragona` | 4 | 0 | 8,50 | Señal geo; Tarragona está dentro de mercados ES protegidos |
| `papel pintado con diseño geométrico` | 4 | 0 | 8,75 | Categoría/patrón prioritario |
| `machwalls` | 2 | 1 | 1,00 | Typo de marca con clic real |
| `papel pintado mural geométrico` | 1 | 1 | 6,00 | Query con clic real |

La query `onde personaliza um mural logistico` también tuvo 1 clic, pero se clasifica como `STANDBY` por estar en PT/fuera de idiomas prioritarios actuales.

## Riesgos detectados

`VERIFICADO PERO MEJORABLE`

1. El export de keywords no identifica la URL destino de cada query. No se debe modificar contenido sin cruzarlo con `Pages`.
2. Hay señales PT/IT con impresiones y un clic, pero PT/IT están fuera del alcance prioritario definido.
3. Algunas queries contienen typos o formulaciones pobres, por ejemplo `hzabitacion`, `caunto`, `paresd`, `machwalls`. No deben copiarse literalmente en contenido.
4. Hay una fila corrupta del export con secuencias `#TAB#` y `#N#`. No debe accionarse.
5. La señal geo existe, pero no justifica crear páginas geográficas nuevas sin validar con estrategia, GSC y páginas destino.

## Recomendación operativa

`VERIFICADO PERO MEJORABLE`

No tocar Shopify todavía.

El siguiente lote seguro debe ser:

`MW-BING-WEBMASTER-SEARCH-PERFORMANCE-PAGES-EXPORT-013J3`

Objetivo: exportar `Search Performance > List By > Pages` para cruzar oportunidades de keywords con URLs reales antes de decidir cambios editoriales, enlaces internos, schema o indexabilidad.

Después, si procede:

1. `MW-BING-WEBMASTER-SEARCH-PERFORMANCE-COUNTRY-DEVICE-EXPORT-013J4`
2. `MW-BING-SEO-GEO-QUERY-URL-OPPORTUNITY-MAP-013J5`
3. Lotes editoriales específicos, no masivos, para producto/color, medición, mural personalizado y geo.

## Evidencias generadas

`VERIFICADO Y CORRECTO`

- `keywords-classified-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-KEYWORDS-EXPORT-013J2-2026-07-05.csv`
- `keywords-summary-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-KEYWORDS-EXPORT-013J2-2026-07-05.csv`
- `keywords-analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-KEYWORDS-EXPORT-013J2-2026-07-05.md`

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó Shopify, Bing Webmaster Tools, IndexNow, tema, robots, sitemap, URLs, handles, redirecciones, traducciones, SEO fields, schema, páginas, productos, colecciones, menús ni apps.
