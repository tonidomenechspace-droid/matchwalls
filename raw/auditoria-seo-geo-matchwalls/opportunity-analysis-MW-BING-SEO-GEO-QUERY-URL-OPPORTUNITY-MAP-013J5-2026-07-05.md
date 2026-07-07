# MW-BING-SEO-GEO-QUERY-URL-OPPORTUNITY-MAP-013J5

Fecha: 2026-07-05  
Modo: solo lectura / análisis cruzado de CSV / sin cambios en Shopify, Bing, IndexNow ni configuración externa.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `keywords-analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-KEYWORDS-EXPORT-013J2-2026-07-05.md`
- `pages-analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-PAGES-EXPORT-013J3-2026-07-05.md`
- `country-device-analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-COUNTRY-DEVICE-EXPORT-013J4-2026-07-05.md`
- `registro-cambios-ejecutados.md`

## Insumos validados

`VERIFICADO Y CORRECTO`

| Fuente | Filas | Impresiones | Clics | Cobertura |
|---|---:|---:|---:|---|
| Keywords 013J2 | 88 | 131 | 3 | Desglose parcial por query |
| Pages 013J3 | 49 | 136 | 3 | Desglose parcial por URL |
| Country 013J4 | 11 | 749 | 3 | Coincide con overview |
| Device 013J4 | 2 | 749 | 3 | Coincide con overview |

## Regla metodológica crítica

`VERIFICADO Y CORRECTO`

Bing exporta `Keyword`, `Page`, `Country` y `Device` como dimensiones separadas. Los CSV disponibles no contienen una unión directa:

`keyword → URL → país → dispositivo`

Por tanto:

- Se pueden agrupar oportunidades por intención y cluster.
- Se pueden usar país/dispositivo como contexto global.
- No se puede afirmar que una keyword concreta llegó a una URL concreta desde un país o dispositivo concreto.
- No se autoriza ninguna escritura en Shopify con esta información sin QA público posterior.

## Mapa de oportunidades

`VERIFICADO PERO MEJORABLE`

| ID | Cluster | Prioridad | Estado | Evidencia directa | Próximo paso |
|---|---|---|---|---|---|
| `BING-GEO-OPP-001` | ES colecciones producto/color/patrón/espacio | ALTA | `VERIFICADO PERO MEJORABLE` | 47 keywords / 16 páginas / 136 señales combinadas / 3 clics | QA público de URLs prioritarias |
| `BING-GEO-OPP-002` | Geo/local existente ES/EN/FR | MEDIA | `VERIFICADO PERO MEJORABLE` | 8 keywords / 8 páginas / 33 señales / 0 clics | QA geo read-only, sin crear páginas nuevas |
| `BING-GEO-OPP-003` | Medición/instalación y contenido citable | MEDIA | `VERIFICADO PERO MEJORABLE` | 11 keywords / 2 páginas / 19 señales / 0 clics | QA de contenido informacional |
| `BING-GEO-OPP-004` | Mural personalizado / proyecto | MEDIA | `VERIFICADO PERO MEJORABLE` | 5 keywords / 2 páginas prioritarias / 11 señales / 0 clics | QA páginas de personalización prioritarias |
| `BING-GEO-OPP-005` | Productos individuales visibles | MEDIA | `VERIFICADO PERO MEJORABLE` | 14 productos / 27 impresiones / 0 clics | QA de producto/schema/canonical |
| `BING-GEO-OPP-006` | Marca typo `machwalls` | BAJA | `VERIFICADO PERO MEJORABLE` | 1 keyword / 2 impresiones / 1 clic | Monitorizar, no crear página |
| `BING-GEO-OPP-007` | Mobile débil en Bing | MEDIA | `VERIFICADO PERO MEJORABLE` | Device: mobile 36 impresiones / 0 clics | Monitor técnico, sin tocar tema ahora |
| `BING-GEO-OPP-008` | PT/IT/BR señales fuera de prioridad | STANDBY | `STANDBY` | 11 keywords / 7 páginas / 34 señales / 2 clics | No accionar sin autorización Fase 2 |
| `BING-GEO-OPP-009` | Legacy `matchwallsmurals/matchwallsmurais` | STANDBY | `STANDBY` | 2 páginas / 2 impresiones / 0 clics | No tocar por instrucción permanente |
| `BING-GEO-OPP-010` | USA/UK/DE mercados estratégicos incipientes | BAJA | `VERIFICADO PERO MEJORABLE` | Country: US 38, DE 11, GB 4 impresiones | Monitorizar, sin landings nuevas |

## Cola prioritaria de QA URL

`VERIFICADO PERO MEJORABLE`

Primero deben revisarse estas URLs públicas, sin editar:

1. `https://www.matchwalls.com/collections/murales-estilo-geometrico`
2. `https://www.matchwalls.com/collections/murales-mas-vendidos-mural`
3. `https://www.matchwalls.com/collections/murales-para-el-pasillo`
4. `https://www.matchwalls.com/collections/papeles-pintados-color-blanco-y-negro`
5. `https://www.matchwalls.com/collections/papeles-pintados-color-negro`
6. `https://www.matchwalls.com/products/gingham-charm-rosa`
7. `https://www.matchwalls.com/pages/medidas-paredes`
8. `https://www.matchwalls.com/products/gingham-charm-verde`
9. `https://www.matchwalls.com/collections/papeles-pintados-color-verde`
10. `https://www.matchwalls.com/en/collections/salamanca-wallpaper`
11. `https://www.matchwalls.com/en/collections/tarragona-wallpaper`

Checks obligatorios por URL:

- HTTP status.
- Indexabilidad.
- Title/meta description.
- H1/H2.
- Canonical.
- Hreflang.
- JSON-LD/schema.
- Enlaces internos.
- Render desktop/mobile.
- Señales de cache/infra si aparecen respuestas anómalas.

## Contexto país/dispositivo

`VERIFICADO PERO MEJORABLE`

País:

- `ww`: 456 impresiones / 1 clic. Es bucket agregado, no accionable por país.
- España: 112 impresiones / 1 clic.
- Francia: 68 impresiones / 0 clics.
- Estados Unidos: 38 impresiones / 0 clics.
- Alemania: 11 impresiones / 0 clics.
- Reino Unido: 4 impresiones / 0 clics.
- Brasil: 40 impresiones / 1 clic, pero `STANDBY`.
- Italia: 12 impresiones / 0 clics, `STANDBY`.

Dispositivo:

- Desktop: 713 impresiones / 3 clics.
- Mobile: 36 impresiones / 0 clics.

Lectura: Bing está dando casi toda la visibilidad actual en desktop, pero esto no elimina la necesidad de mantener mobile perfecto para SEO general, Google, usuarios y sistemas IA.

## Decisiones y límites

`VERIFICADO Y CORRECTO`

No se autoriza todavía:

- Cambiar handles.
- Cambiar URLs.
- Cambiar canonicals.
- Cambiar redirecciones.
- Crear landings nuevas.
- Editar contenido de colecciones, productos o páginas.
- Editar LangShop.
- Tocar tema/Liquid/CSS.
- Cambiar noindex/index.
- Accionar PT/IT.
- Accionar legacy `matchwallsmurals`.

## Próximo lote seguro recomendado

`MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6`

Objetivo: revisar públicamente las URLs prioritarias del mapa, empezando por las colecciones ES con mayor señal y clic real, sin modificar Shopify.

## Evidencias generadas

`VERIFICADO Y CORRECTO`

- `opportunity-map-MW-BING-SEO-GEO-QUERY-URL-OPPORTUNITY-MAP-013J5-2026-07-05.csv`
- `priority-url-qa-queue-MW-BING-SEO-GEO-QUERY-URL-OPPORTUNITY-MAP-013J5-2026-07-05.csv`
- `opportunity-summary-MW-BING-SEO-GEO-QUERY-URL-OPPORTUNITY-MAP-013J5-2026-07-05.csv`
- `opportunity-analysis-MW-BING-SEO-GEO-QUERY-URL-OPPORTUNITY-MAP-013J5-2026-07-05.md`

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó Shopify, Bing Webmaster Tools, IndexNow, Search Performance, tema, URLs, handles, traducciones, SEO fields, robots, sitemap, schema, productos, páginas, colecciones ni apps.
