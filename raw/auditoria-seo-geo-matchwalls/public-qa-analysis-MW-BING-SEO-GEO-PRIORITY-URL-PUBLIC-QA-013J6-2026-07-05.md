# MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6

Fecha: 2026-07-05  
Modo: solo lectura / QA público de URLs priorizadas desde Bing Search Performance.  
Estado final: `INCOMPLETO`

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `opportunity-analysis-MW-BING-SEO-GEO-QUERY-URL-OPPORTUNITY-MAP-013J5-2026-07-05.md`
- `priority-url-qa-queue-MW-BING-SEO-GEO-QUERY-URL-OPPORTUNITY-MAP-013J5-2026-07-05.csv`
- `opportunity-map-MW-BING-SEO-GEO-QUERY-URL-OPPORTUNITY-MAP-013J5-2026-07-05.csv`
- `registro-cambios-ejecutados.md`

## Alcance ejecutado

`VERIFICADO Y CORRECTO`

Se intentó comprobar la cola completa de 42 URLs priorizadas en 013J5.

Checks previstos:

- HTTP status.
- URL final y redirecciones.
- Title.
- Meta description.
- Canonical.
- Robots meta / X-Robots-Tag.
- H1.
- Hreflang.
- `html lang`.
- Tipos JSON-LD visibles.
- Respuesta crawler-like con user-agent Bingbot.

No se modificó Shopify, Bing Webmaster Tools, IndexNow, LangShop, tema, contenido, handles, redirecciones, SEO fields, schema ni configuración externa.

## Resultado principal

`INCOMPLETO`

La comprobación no puede considerarse completa porque Cloudflare devolvió `429` durante el QA desde este entorno.

Resumen:

| Bloque | Resultado | Estado |
|---|---:|---|
| URLs en cola 013J5 | 42 | `VERIFICADO Y CORRECTO` |
| URLs con QA browser-like completo | 6 | `VERIFICADO Y CORRECTO` |
| URLs no juzgables por `429` browser-like | 36 | `INCOMPLETO` |
| URLs Bingbot-like con `429` | 42 | `INCOMPLETO` |
| Mini recheck lento tras cooldown | 3/3 `429` | `INCOMPLETO` |

Interpretación rigurosa:

- El `429` impide completar el QA público automatizado.
- El `429` no demuestra por sí solo que las páginas estén mal a nivel SEO/editorial.
- El `429` sí es una señal de riesgo para auditoría crawler/WAF/CDN, especialmente porque el user-agent Bingbot-like quedó bloqueado desde este entorno.
- No se puede afirmar que Bing real esté bloqueado: Bing Webmaster Tools ya muestra impresiones y URLs recibidas por IndexNow.
- Antes de ejecutar más crawling masivo o proponer cambios de contenido, conviene aclarar el comportamiento WAF/CDN.

## URLs verificadas correctamente a nivel página

`VERIFICADO Y CORRECTO`

Las primeras 6 URLs respondieron `200` con navegador normal y pasaron los checks básicos de página:

1. `https://www.matchwalls.com/collections/murales-estilo-geometrico`
2. `https://www.matchwalls.com/collections/murales-mas-vendidos-mural`
3. `https://www.matchwalls.com/collections/murales-para-el-pasillo`
4. `https://www.matchwalls.com/collections/papeles-pintados-color-blanco-y-negro`
5. `https://www.matchwalls.com/collections/papeles-pintados-color-negro`
6. `https://www.matchwalls.com/products/gingham-charm-rosa`

Comprobado en esas 6 URLs:

- HTTP `200`.
- Canonical presente y coherente con URL final/original.
- Meta description presente.
- H1 presente.
- Hreflang presente, 8 alternates detectados.
- Sin `noindex` detectado.
- JSON-LD visible:
  - Colecciones: `BreadcrumbList` / `ListItem`.
  - Producto Gingham Charm Rosa: `Product`, `ImageObject`, `QuantitativeValue`, `Brand`, `Offer`, `BreadcrumbList`, `ListItem`.

Nota técnica: el extractor local mezcló el `<title>` principal con títulos internos de iconos SVG de métodos de pago. La matriz final corrige este artefacto y no lo clasifica como fallo SEO sin una comprobación independiente.

## URLs no juzgables todavía

`INCOMPLETO`

Las 36 URLs restantes devolvieron `429` desde Cloudflare en la pasada browser-like. Como no hubo HTML útil, no se puede validar title, meta, canonical, H1, hreflang ni schema en esas URLs.

No se deben marcar como `INCORRECTO` a nivel página hasta que exista una respuesta `200` verificable.

## Respuesta crawler-like

`INCOMPLETO`

La pasada con user-agent Bingbot-like devolvió `429` en las 42 URLs.

Datos observados:

- Servidor indicado: `cloudflare`.
- Sin `x-request-id` de Shopify en las respuestas `429`.
- Sin render headers de Shopify.

Interpretación:

- El bloqueo ocurre antes de llegar claramente al render Shopify.
- Puede ser protección de Cloudflare, rate limit, WAF, bot score o una combinación.
- No se puede concluir que Bingbot real esté bloqueado sin validación de IP oficial / logs / soporte.
- Sí conviene documentarlo porque afecta a la capacidad de QA SEO/GEO/AEO.

## Riesgos detectados

`REQUIERE DECISION HUMANA`

1. Riesgo de accesibilidad crawler/WAF en auditoría desde entorno externo.
2. Riesgo de falsos negativos si se siguen lanzando crawls automatizados mientras persiste `429`.
3. Riesgo de mezclar este problema con el ticket Shopify `68731900`, que trata render/cache/500; este 013J6 apunta más a capa Cloudflare/rate-limit antes de Shopify.

## Archivos generados

`VERIFICADO Y CORRECTO`

- `public-url-qa-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.csv`
- `crawler-response-qa-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.csv`
- `public-url-qa-final-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.csv`
- `crawler-access-risk-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.csv`
- `summary-final-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.csv`

## Siguiente lote seguro recomendado

`REQUIERE DECISION HUMANA`

`MW-CRAWLERS-WAF-CLOUDFLARE-429-SUPPORT-EVIDENCE-013J6B`

Objetivo:

- Preparar evidencia clara del `429` Cloudflare.
- Separarlo del ticket Shopify `68731900`.
- Decidir si se consulta a Shopify/Cloudflare/app o si se espera antes de reintentar QA crawler.

Después, cuando el acceso esté estable:

`MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6R`

para repetir la QA pública de las 36 URLs pendientes.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó Shopify, Bing Webmaster Tools, IndexNow, LangShop, tema, URLs, handles, redirecciones, contenidos, traducciones, SEO fields, robots, sitemap, schema, productos, páginas, colecciones ni apps.
