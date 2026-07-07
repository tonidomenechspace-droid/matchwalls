# MW-CEO-CMO-PANEL-SPEC-014C

Fecha: 2026-07-05  
Modo: documental / solo lectura / sin cambios externos.  
Estado final: `VERIFICADO Y CORRECTO`

## Objetivo

`VERIFICADO Y CORRECTO`

Definir el panel mensual CEO/CMO para controlar el programa SEO, GEO y AGEO de MatchWalls con rigor ejecutivo:

- medir negocio, demanda orgánica, indexabilidad, citabilidad IA, salud técnica y avance editorial;
- separar datos verificados de métricas aún no accesibles;
- evitar decisiones basadas en impresiones parciales o datos no confirmados;
- mantener una cola accionable para cuando Shopify Engineering resuelva la incidencia de infraestructura.

Este lote no crea un dashboard conectado ni modifica Shopify, Bing, Google, GA4, GSC, IndexNow, LangShop, Cloudflare, tema, URLs, handles, robots, sitemap, schema, contenidos ni traducciones.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `infra-hold-replan-MW-MASTER-QUEUE-INFRA-HOLD-REPLAN-014B-2026-07-05.md`
- `infra-hold-replan-queue-MW-MASTER-QUEUE-INFRA-HOLD-REPLAN-014B-2026-07-05.csv`
- `status-MW-MASTER-QUEUE-INFRA-HOLD-REPLAN-014B-2026-07-05.csv`
- `analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-FULL-EXPORT-013J1-2026-07-05.md`
- `overview-summary-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-FULL-EXPORT-013J1-2026-07-05.csv`
- `keywords-summary-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-KEYWORDS-EXPORT-013J2-2026-07-05.csv`
- `pages-summary-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-PAGES-EXPORT-013J3-2026-07-05.csv`
- `country-device-summary-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-COUNTRY-DEVICE-EXPORT-013J4-2026-07-05.csv`
- `qa-MW-BING-WEBMASTER-SITEMAP-STATUS-QA-013E2-2026-07-04.md`
- `qa-MW-BING-WEBMASTER-AI-PERFORMANCE-EXPORT-QA-013E4-2026-07-04.md`
- `qa-MW-BING-WEBMASTER-AI-PERFORMANCE-PAGES-EXPORT-013E6-2026-07-04.md`
- `audit-MW-INDEXNOW-BING-WEBMASTER-SUBMITTED-URLS-AUDIT-013I5-2026-07-05.csv`
- `full-export-MW-INDEXNOW-BING-WEBMASTER-SUBMITTED-URLS-FULL-EXPORT-013I5B-2026-07-05.md`
- `monitor-MW-INDEXNOW-BING-WEBMASTER-DISCREPANCY-MONITOR-013I5C-2026-07-05.md`
- `review-MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C-REVIEW-2026-07-05.md`
- `public-qa-retry-analysis-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6R-2026-07-05.md`
- `shopify-ticket-update-MW-SHOPIFY-INFRA-500-REQUEST-ID-UPDATE-013J6R1-2026-07-05.md`
- `registro-cambios-ejecutados.md`

## Estado real comprobado

### Bloqueo técnico vigente

`RIESGO CRITICO`

El ticket Shopify Engineering `68731900` sigue abierto. La cola 014B mantiene bloqueado todo lo que dependa de render público estable:

- crawls públicos amplios;
- edición/publicación de tema;
- schema visible en MAIN;
- cambios de landings España/Francia;
- cambios LangShop;
- robots, sitemap, `llms.txt`, `agents.md`;
- envíos IndexNow manuales o masivos;
- QA público completo de las 42 URLs priorizadas.

La especificación del panel se puede completar porque usa datos ya exportados y trabajo documental.

### Datos verificados disponibles

`VERIFICADO Y CORRECTO`

- Bing Search Performance overview: `749` impresiones, `3` clics, CTR calculado `0,40%`, periodo `2026-06-13` a `2026-07-03`.
- Bing Keywords export: `88` queries, `131` impresiones visibles/exportadas, `3` clics, posición media ponderada `6,43`.
- Bing Pages export: `49` URLs, `136` impresiones visibles/exportadas, `3` clics, posición media ponderada `6,19`.
- Bing Country/Device export: `11` países y `2` dispositivos; total overview `749` impresiones y `3` clics.
- Bing Sitemap: `https://www.matchwalls.com/sitemap.xml`, estado `Success`, `0` errores, `0` warnings, `7.8K` URLs descubiertas.
- Bing AI Performance overview: `10` citas, `5` días con citas, `8` cited pages sumadas por día.
- Bing AI Performance Pages: `7` URLs citadas, `10` citas totales.
- IndexNow en Bing: contador visible `13` submitted URLs; tabla/export verificable `3` URLs.
- Robots/crawlers: `robots.txt`, `sitemap.xml`, `llms.txt` y `agents.md` estaban accesibles en la revisión 013C; no se recomienda tocar robots ahora.

### Datos no accesibles o incompletos

`INCOMPLETO` / `NO ACCESIBLE`

- GA4: ingresos orgánicos, conversiones, tasa de conversión, AOV y revenue por país/idioma no verificados en este lote.
- Shopify Analytics: ventas orgánicas y conversiones por canal no verificadas en este lote.
- Google Search Console: impresiones/clics/indexación por URL no verificados en este lote.
- Core Web Vitals con CrUX/GSC real: no verificado en este lote.
- Google AI Overviews, Gemini, ChatGPT, Claude, Perplexity, Comet, Grok, Meta y Ollama: sin panel de citas verificado equivalente a Bing AI Performance.
- Exactitud de las respuestas IA: pendiente de QA manual posterior.

## Diseño recomendado del panel CEO/CMO

`VERIFICADO Y CORRECTO`

Frecuencia: mensual, con corte fijo el primer día laborable del mes.  
Idiomas prioritarios: ES, EN, FR, DE y NL.  
Mercados prioritarios: España, Francia, Alemania, Países Bajos y UK/EN cuando aplique.  
Estados permitidos: los estados obligatorios del proyecto, sin categorías nuevas.

### 1. Resumen ejecutivo

`VERIFICADO Y CORRECTO`

Debe responder en una pantalla:

- ¿sube o baja la demanda orgánica no-brand?
- ¿qué país/idioma aporta oportunidad real?
- ¿qué URLs están siendo citadas por IA?
- ¿hay riesgo técnico que impida publicar o medir?
- ¿qué lote se puede ejecutar sin poner en riesgo la tienda?

Estado actual recomendado para el bloque superior:

- Estado SEO/GEO global: `VERIFICADO PERO MEJORABLE`
- Estado técnico storefront: `RIESGO CRITICO` hasta respuesta Shopify Engineering.
- Estado medición Bing/Copilot: `VERIFICADO Y CORRECTO`
- Estado medición Google/GSC/GA4/CWV: `NO ACCESIBLE`
- Estado contenidos citables ES/EN/FR/DE/NL: `INCOMPLETO`

### 2. Negocio orgánico

`NO ACCESIBLE`

KPIs necesarios:

- ingresos orgánicos;
- pedidos orgánicos;
- tasa de conversión orgánica;
- AOV orgánico;
- ingresos por país/idioma;
- conversión por dispositivo.

Fuente requerida:

- GA4;
- Shopify Analytics;
- atribución interna o UTM si existe.

No se deben inventar estas cifras a partir de Bing. Bing mide demanda/citas, no ventas.

### 3. Demanda orgánica en buscadores

`VERIFICADO PERO MEJORABLE`

KPIs disponibles hoy:

- Bing impressions/clicks/CTR;
- keywords por intención;
- URLs por tipo;
- países;
- dispositivos.

Límites:

- Bing no sustituye Google Search Console.
- Los exports de Keywords y Pages no suman el mismo total que el overview; deben tratarse como detalle visible/exportable, no como totalidad absoluta.
- No se debe extrapolar Google desde Bing.

### 4. GEO / AGEO / citabilidad IA

`VERIFICADO PERO MEJORABLE`

KPIs disponibles hoy:

- Bing AI Performance: `10` citas.
- URLs citadas: `7`.
- Idiomas con citas: ES/default `4`, EN `4`, PT `2`.
- Idiomas prioritarios sin citas en ese export: FR `0`, DE `0`, NL `0`.

Interpretación:

- MatchWalls ya tiene presencia real en Microsoft Copilot/partners.
- Hay que reforzar contenido citable en ES/EN y abrir gap analysis para FR/DE/NL.
- PT aparece citado, pero PT no es prioridad activa; queda `STANDBY` hasta decisión.

No se debe afirmar que schema, IndexNow o contenido nuevo garantizarán citas.

### 5. Indexabilidad y rastreo

`VERIFICADO PERO MEJORABLE`

KPIs del panel:

- sitemap Bing: estado, errores, warnings, URLs descubiertas;
- IndexNow: URLs enviadas, fallos, discrepancias;
- GSC: válidas/indexadas/excluidas, cuando esté accesible;
- noindex por tipo de URL;
- redirecciones, 404 y cadenas críticas;
- robots/crawlers IA.

Estado actual:

- Bing sitemap: `VERIFICADO Y CORRECTO`.
- IndexNow app: instalada y con recepción visible, pero discrepancia `13` vs `3` queda `VERIFICADO PERO MEJORABLE` / `STANDBY`.
- GSC index coverage: `NO ACCESIBLE` en este lote.

### 6. Salud técnica y publicación

`RIESGO CRITICO`

KPIs del panel:

- estado de Shopify Engineering ticket `68731900`;
- número de 500 recientes con `x-request-id`;
- resultado de safety gate post-infra;
- CWV real;
- errores JavaScript críticos;
- mobile overflow;
- estado de tema MAIN vs hotfix.

Estado actual:

- public QA amplio bloqueado;
- 2 eventos HTTP `500` añadidos al ticket en `013J6R1`;
- no publicar ni editar tema hasta postcheck de infraestructura.

### 7. Contenido, entidad y autoridad

`INCOMPLETO`

KPIs del panel:

- páginas citables publicadas por idioma;
- landings geográficas útiles por país;
- FAQs/HowTo/comparativas publicadas;
- entidad factual MatchWalls coherente en ES/EN/FR/DE/NL;
- perfiles oficiales y sameAs validados;
- backlinks/menciones cualitativas.

Estado actual:

- España/Francia avanzadas pero congeladas por infraestructura.
- DE/NL/UK/BE/USA/MX deben seguir como briefs locales antes de Shopify.
- Entidad factual global aún pendiente.

## Estructura visual recomendada

`VERIFICADO Y CORRECTO`

Panel mensual de 6 bloques:

1. Semáforo ejecutivo.
2. Negocio orgánico.
3. Demanda SEO por buscador.
4. Citabilidad IA / GEO.
5. Indexabilidad y salud técnica.
6. Próximos lotes y decisiones.

El panel debe tener una fila de advertencia fija:

> Si existe `RIESGO CRITICO` técnico en storefront, ningún KPI de publicación queda liberado automáticamente.

## Criterios de decisión

`VERIFICADO Y CORRECTO`

- Si Bing impressions suben pero clics no suben: revisar snippets, intención y URLs que rankean.
- Si AI citations suben pero citan URLs débiles: priorizar canonical/indexabilidad/contenido de esas URLs.
- Si FR/DE/NL siguen con 0 citas: abrir gap de contenido factual y guías citables por idioma.
- Si IndexNow muestra fallos: auditar URLs enviadas y excluir noindex/no valiosas.
- Si GSC/GA4 no están accesibles: no cerrar el panel como ejecutivo completo.
- Si Shopify Engineering no ha cerrado el ticket: mantener bloqueado cualquier lote de publicación o crawl amplio.

## Próximo lote recomendado

`REQUIERE DECISION HUMANA`

Opción principal:

`MW-ENTITY-FACTUAL-BRIEF-ES-EN-FR-DE-NL-015A`

Motivo:

- 100% documental.
- Refuerza SEO/GEO/AGEO sin tocar Shopify.
- Prepara la base citable de marca para Google, Bing/Copilot, ChatGPT, Claude, Perplexity, Gemini y otros sistemas.

Opción alternativa:

`MW-BING-SEARCH-PERFORMANCE-CONSOLIDATED-INSIGHTS-013J7`

Motivo:

- Profundiza en oportunidades detectadas por Bing sin publicar.
- Útil para preparar correcciones futuras cuando se desbloquee infraestructura.

## Archivos generados

`VERIFICADO Y CORRECTO`

- `ceo-cmo-panel-spec-MW-CEO-CMO-PANEL-SPEC-014C-2026-07-05.md`
- `ceo-cmo-panel-metrics-MW-CEO-CMO-PANEL-SPEC-014C-2026-07-05.csv`
- `ceo-cmo-panel-data-sources-MW-CEO-CMO-PANEL-SPEC-014C-2026-07-05.csv`
- `status-MW-CEO-CMO-PANEL-SPEC-014C-2026-07-05.csv`

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó Shopify, Bing Webmaster Tools, IndexNow, LangShop, Cloudflare, Google, GA4, Search Console, tema, URLs, handles, redirecciones, contenidos, traducciones, SEO fields, robots, sitemap, schema, productos, páginas, colecciones ni apps.
