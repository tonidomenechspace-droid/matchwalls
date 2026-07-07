# MW-CRAWLERS-WAF-CLOUDFLARE-429-SUPPORT-EVIDENCE-013J6B

Fecha: 2026-07-05  
Modo: solo lectura / documentación de evidencia.  
Estado final: `VERIFICADO PERO MEJORABLE`

## Objetivo

`VERIFICADO Y CORRECTO`

Preparar un paquete claro de evidencia sobre respuestas `429` de Cloudflare detectadas durante el QA público de URLs priorizadas por Bing en el lote `MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6`.

Este lote no modifica Shopify, Bing Webmaster Tools, IndexNow, LangShop, Cloudflare, tema, URLs, handles, contenidos ni configuraciones.

## Hechos verificados

`VERIFICADO Y CORRECTO`

Fuente primaria local:

- `public-qa-analysis-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.md`
- `public-url-qa-final-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.csv`
- `crawler-access-risk-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.csv`
- `summary-final-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.csv`

Resultados del QA 013J6:

| Métrica | Resultado | Estado |
|---|---:|---|
| URLs priorizadas comprobadas | 42 | `VERIFICADO Y CORRECTO` |
| Browser-like `200` | 6 | `VERIFICADO Y CORRECTO` |
| Browser-like `429` | 36 | `INCOMPLETO` |
| Bingbot-like `429` | 42 | `INCOMPLETO` |
| Mini recheck lento tras cooldown | 3/3 `429` | `INCOMPLETO` |
| Servidor observado en Bingbot-like | `cloudflare` en 42/42 | `VERIFICADO Y CORRECTO` |
| `x-request-id` Shopify en respuestas `429` | No presente | `VERIFICADO Y CORRECTO` |

## Interpretación rigurosa

`VERIFICADO PERO MEJORABLE`

Lo que sí se puede afirmar:

- El entorno de QA recibió `429` de Cloudflare.
- El bloqueo impidió validar 36 de 42 URLs a nivel HTML.
- El user-agent Bingbot-like recibió `429` en 42 de 42 URLs.
- En las respuestas `429` no aparecieron `x-request-id` de Shopify ni headers de render Shopify, por lo que el bloqueo parece producirse antes de una respuesta HTML normal de Shopify.

Lo que no se puede afirmar sin evidencia adicional:

- No se puede afirmar que Bingbot real esté bloqueado.
- No se puede afirmar que las URLs con `429` estén mal a nivel SEO/editorial.
- No se puede afirmar que sea un fallo de Shopify Liquid o de contenido.
- No se debe mezclar automáticamente con el ticket Shopify `68731900`, que trata render/cache/500.

## URLs verificadas correctamente antes del bloqueo

`VERIFICADO Y CORRECTO`

Estas 6 URLs respondieron `200` con navegador normal y pasaron checks básicos de página:

1. `https://www.matchwalls.com/collections/murales-estilo-geometrico`
2. `https://www.matchwalls.com/collections/murales-mas-vendidos-mural`
3. `https://www.matchwalls.com/collections/murales-para-el-pasillo`
4. `https://www.matchwalls.com/collections/papeles-pintados-color-blanco-y-negro`
5. `https://www.matchwalls.com/collections/papeles-pintados-color-negro`
6. `https://www.matchwalls.com/products/gingham-charm-rosa`

## Muestra de URLs afectadas por `429` browser-like

`INCOMPLETO`

Ejemplos de URLs no juzgables por `429`:

1. `https://www.matchwalls.com/pages/medidas-paredes`
2. `https://www.matchwalls.com/products/gingham-charm-verde`
3. `https://www.matchwalls.com/collections/papeles-pintados-color-verde`
4. `https://www.matchwalls.com/en/collections/salamanca-wallpaper`
5. `https://www.matchwalls.com/en/collections/tarragona-wallpaper`
6. `https://www.matchwalls.com/collections/murales-para-habitaciones-de-adolescentes`
7. `https://www.matchwalls.com/collections/comprar-papel-pintado-paris`
8. `https://www.matchwalls.com/products/marejada-azul`
9. `https://www.matchwalls.com/collections/papeles-pintados-color-lila`
10. `https://www.matchwalls.com/collections/murales-estilo-paisajes`

La lista completa está en:

- `public-url-qa-final-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.csv`
- `crawler-access-risk-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.csv`

## Recomendación operativa

`REQUIERE DECISION HUMANA`

No continuar con crawls automatizados amplios hasta aclarar el origen del `429`.

Ruta segura:

1. Documentar el caso como posible regla WAF/rate-limit/bot-score/CDN.
2. Pedir confirmación a soporte técnico competente:
   - Si Shopify/Cloudflare aplica rate-limit o bot protection a user-agents crawler-like.
   - Si existe forma segura de permitir QA controlado sin afectar seguridad.
   - Si deben validarse bots por IP oficial antes de permitir user-agents.
3. Repetir QA con una cadencia más conservadora solo cuando la capa WAF/CDN esté aclarada.

## Siguiente lote recomendado

`REQUIERE DECISION HUMANA`

Opción A, si Daniel quiere consultar soporte:

`MW-CRAWLERS-WAF-CLOUDFLARE-429-SUPPORT-SUBMISSION-013J6C`

Opción B, si Daniel prefiere esperar:

`MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6R`

solo cuando el acceso público/crawler esté estable.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó Shopify, Bing Webmaster Tools, IndexNow, LangShop, Cloudflare, tema, URLs, handles, redirecciones, contenidos, traducciones, SEO fields, robots, sitemap, schema, productos, páginas, colecciones ni apps.
