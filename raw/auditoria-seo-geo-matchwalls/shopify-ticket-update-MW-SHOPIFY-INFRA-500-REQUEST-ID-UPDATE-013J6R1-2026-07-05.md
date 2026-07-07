# MW-SHOPIFY-INFRA-500-REQUEST-ID-UPDATE-013J6R1

Fecha: 2026-07-05  
Ticket Shopify relacionado: `68731900`  
Modo: solo lectura / preparación de actualización para soporte.  
Estado final: `VERIFICADO Y CORRECTO`

## Objetivo

`VERIFICADO Y CORRECTO`

Preparar una actualización breve para el ticket Shopify `68731900` con nuevos errores `500` detectados durante el safety gate del lote `MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6R`.

No se realizaron nuevas pruebas contra la web en este lote.

## Evidencia usada

`VERIFICADO Y CORRECTO`

- `public-qa-retry-analysis-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6R-2026-07-05.md`
- `safety-gate-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6R-2026-07-05.csv`
- `status-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6R-2026-07-05.csv`

## Nuevos eventos `500`

`RIESGO CRITICO`

| URL | HTTP | Elapsed ms | Server | CF-Ray | Shopify x-request-id |
|---|---:|---:|---|---|---|
| `https://www.matchwalls.com/products/gingham-charm-verde` | 500 | 3266 | cloudflare | `a1677b84fa654bd6-MAD` | `085d24e5-299a-4e8c-bd90-f0ba737e13bb-1783266176` |
| `https://www.matchwalls.com/en/collections/salamanca-wallpaper` | 500 | 3294 | cloudflare | `a1677c42ca9cf91f-MAD` | `84b5fb4a-fca0-48bb-80b9-1ee7399344c6-1783266207` |

## Mensaje sugerido para Shopify Support / Engineering

```text
Hi Shopify Support,

Please add this update to engineering ticket 68731900.

We performed a very small safety-gate recheck today before resuming any broader SEO QA. We did not run a full crawl. The previous Cloudflare 429 behavior did not appear in this small sample, but 2 out of 5 public URLs returned HTTP 500.

New 500 evidence:

1. URL: https://www.matchwalls.com/products/gingham-charm-verde
   HTTP status: 500
   Elapsed: 3266 ms
   Server: cloudflare
   CF-Ray: a1677b84fa654bd6-MAD
   Shopify x-request-id: 085d24e5-299a-4e8c-bd90-f0ba737e13bb-1783266176

2. URL: https://www.matchwalls.com/en/collections/salamanca-wallpaper
   HTTP status: 500
   Elapsed: 3294 ms
   Server: cloudflare
   CF-Ray: a1677c42ca9cf91f-MAD
   Shopify x-request-id: 84b5fb4a-fca0-48bb-80b9-1ee7399344c6-1783266207

Context:

- This was a browser-like request, not a Bingbot-like request.
- The affected edge/PoP appears to be MAD in both failures.
- We stopped the QA immediately after detecting these 500s to avoid adding noise while engineering investigates.
- We have not changed content, page handles, URLs, translations, markets, theme files, SEO fields, redirects, robots, sitemap, schema, apps, or IndexNow settings.

Please confirm whether these request IDs match the same storefront rendering / infrastructure issue already escalated under ticket 68731900, and whether we should continue holding all page/theme/translation changes and avoid further public QA crawls until engineering completes the investigation.

Thank you.
```

## Recomendación operativa

`REQUIERE DECISION HUMANA`

Enviar el mensaje anterior como respuesta al ticket Shopify `68731900`.

Mientras no exista respuesta de ingeniería:

- No continuar crawls públicos amplios.
- No tocar tema, traducciones, SEO fields, schema, landings o URLs para intentar resolverlo.
- Mantener los lotes de cambio en Shopify en espera si dependen de QA público estable.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó Shopify, Bing Webmaster Tools, IndexNow, LangShop, Cloudflare, tema, URLs, handles, redirecciones, contenidos, traducciones, SEO fields, robots, sitemap, schema, productos, páginas, colecciones ni apps.
