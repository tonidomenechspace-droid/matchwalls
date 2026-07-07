# MW-BING-WEBMASTER-SEARCH-PERFORMANCE-PAGES-EXPORT-013J3

Fecha: 2026-07-05  
Modo: solo lectura / análisis de CSV / sin cambios en Shopify, Bing, IndexNow ni configuración externa.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `baseline-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J-2026-07-05.md`
- `analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-FULL-EXPORT-013J1-2026-07-05.md`
- `keywords-analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-KEYWORDS-EXPORT-013J2-2026-07-05.md`
- `registro-cambios-ejecutados.md`

## Archivo recibido

`VERIFICADO Y CORRECTO`

Daniel aportó el export de Bing Webmaster Tools:

`C:\Users\d.bermejo\OneDrive - Matchwalls\Escritorio\matchwalls.com_PageTrafficReport_7_5_2026 CCCCCCCCCC.csv`

Columnas detectadas:

- `Page`
- `Impressions`
- `Clicks`
- `CTR`
- `Avg. Position`

Esto confirma que el archivo corresponde a `Search Performance > List By > Pages`.

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

El CSV contiene:

- Páginas exportadas: `49`
- Impresiones en el export de páginas: `136`
- Clics en el export de páginas: `3`
- CTR calculado sobre páginas visibles: `2,21%`
- Posición media ponderada por impresión: `6,19`

Importante: igual que en el export de keywords 013J2, este desglose por páginas no suma las `749` impresiones del overview 013J/013J1. Se interpreta como desglose parcial disponible por Bing, no como error de MatchWalls.

## Distribución por idioma/señal de URL

`VERIFICADO PERO MEJORABLE`

| Idioma / señal URL | URLs | Impresiones | Clics | Estado |
|---|---:|---:|---:|---|
| ES | 32 | 98 | 2 | `VERIFICADO PERO MEJORABLE` |
| PT | 4 | 15 | 1 | `STANDBY` |
| EN | 7 | 14 | 0 | `VERIFICADO PERO MEJORABLE` |
| FR | 3 | 5 | 0 | `VERIFICADO PERO MEJORABLE` con excepciones legacy |
| IT | 2 | 3 | 0 | `STANDBY` |
| DE | 1 | 1 | 0 | `VERIFICADO PERO MEJORABLE` |

No aparecen URLs NL en este export de 3 meses. Esto no demuestra ausencia de demanda NL; solo indica que Bing no muestra URLs NL en el desglose disponible.

## Distribución por tipo de página

`VERIFICADO PERO MEJORABLE`

| Tipo | URLs | Impresiones | Clics | Lectura |
|---|---:|---:|---:|---|
| Colecciones | 28 | 83 | 2 | Principal fuente visible de Bing |
| Productos | 15 | 28 | 0 | Visibilidad de producto, sin clics todavía |
| Páginas | 5 | 23 | 1 | Guías/personalización con señal útil |
| Blog | 1 | 2 | 0 | Señal baja |

## Distribución por cluster

`VERIFICADO PERO MEJORABLE`

| Cluster | URLs | Impresiones | Clics | Lectura |
|---|---:|---:|---:|---|
| Colección producto/color/patrón/espacio | 17 | 62 | 2 | Núcleo visible de oportunidad |
| Producto | 15 | 28 | 0 | Necesita revisión de producto/canonical/merchant antes de accionar |
| Geo/local | 8 | 17 | 0 | Señal geo, pero sin clics y sin justificar expansión masiva |
| Mural personalizado / informacional | 4 | 17 | 1 | Hay interés, pero parte está en PT/IT |
| Medición/instalación | 2 | 8 | 0 | Útil para guías citables |
| Legacy `matchwallsmurals` | 2 | 2 | 0 | `STANDBY` por instrucción permanente |
| Otro | 1 | 2 | 0 | Baja muestra |

## URLs prioritarias detectadas

`VERIFICADO PERO MEJORABLE`

| URL | Imp. | Clics | Pos. media | Estado | Motivo |
|---|---:|---:|---:|---|---|
| `https://www.matchwalls.com/collections/murales-para-el-pasillo` | 11 | 0 | 4,09 | `VERIFICADO PERO MEJORABLE` | Mayor visibilidad ES del export |
| `https://www.matchwalls.com/collections/murales-estilo-geometrico` | 10 | 1 | 6,90 | `VERIFICADO PERO MEJORABLE` | Clic real + cluster patrón/estilo |
| `https://www.matchwalls.com/collections/papeles-pintados-color-blanco-y-negro` | 10 | 0 | 5,60 | `VERIFICADO PERO MEJORABLE` | Color/patrón con visibilidad |
| `https://www.matchwalls.com/collections/murales-mas-vendidos-mural` | 2 | 1 | 1,00 | `VERIFICADO PERO MEJORABLE` | Clic real y posición alta |

La URL `https://www.matchwalls.com/pt/pages/crie-seu-proprio-mural` tuvo 11 impresiones y 1 clic, pero se mantiene en `STANDBY` porque PT está fuera de los idiomas prioritarios actuales.

## URLs y señales en standby

`STANDBY`

- `https://www.matchwalls.com/pt/pages/crie-seu-proprio-mural`
- `https://www.matchwalls.com/it/pages/crea-il-tuo-murale`
- `https://www.matchwalls.com/pt/collections/lilas-pintou-papeis-matchwallswallpapers`
- `https://www.matchwalls.com/it/products/beige-murale-serenita-tropicale`
- `https://www.matchwalls.com/pt/collections/peel-stick-auto-adesivo-papel-de-parede`
- `https://www.matchwalls.com/pt/collections/estrutura-de-murais-matchwallsmurais`
- `https://www.matchwalls.com/fr/collections/peintures-murales-botaniques-matchwallsmurals`

Las URLs relacionadas con `matchwallsmurals/matchwallsmurais` no deben modificarse hasta decisión expresa.

## Observaciones SEO/GEO

`VERIFICADO PERO MEJORABLE`

1. Bing ya está mostrando MatchWalls en páginas comerciales ES de colecciones y productos.
2. Las señales más claras coinciden con los clusters detectados en keywords: pasillo, geométrico, negro/blanco, gingham/tartán y medición.
3. Hay URLs geo EN para Salamanca, Tarragona, Málaga, La Rioja y Castellón. Deben revisarse contra la estrategia de landings geográficas antes de intervenir.
4. Hay una URL DE con posible typo visible en el handle: `peel-stick-self-adhasive-tapete`. No se propone cambio; solo queda señalada para auditoría futura, porque cambiar handles requiere mapa 301 y aprobación específica.
5. PT/IT tienen datos reales, pero siguen fuera de alcance prioritario salvo autorización expresa.

## Recomendación operativa

`VERIFICADO PERO MEJORABLE`

No tocar Shopify todavía.

Siguiente lote seguro recomendado:

`MW-BING-WEBMASTER-SEARCH-PERFORMANCE-COUNTRY-DEVICE-EXPORT-013J4`

Objetivo: obtener `Country` y `Device` para saber si estas impresiones vienen de mercados realmente prioritarios y si hay riesgo mobile/desktop.

Después:

`MW-BING-SEO-GEO-QUERY-URL-OPPORTUNITY-MAP-013J5`

Objetivo: cruzar keywords 013J2 + pages 013J3 + país/dispositivo 013J4 para priorizar cambios editoriales o técnicos con evidencia.

## Evidencias generadas

`VERIFICADO Y CORRECTO`

- `pages-classified-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-PAGES-EXPORT-013J3-2026-07-05.csv`
- `pages-summary-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-PAGES-EXPORT-013J3-2026-07-05.csv`
- `pages-analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-PAGES-EXPORT-013J3-2026-07-05.md`

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó Shopify, Bing Webmaster Tools, IndexNow, Search Performance, tema, URLs, handles, traducciones, SEO fields, robots, sitemap, schema, productos, páginas, colecciones ni apps.
