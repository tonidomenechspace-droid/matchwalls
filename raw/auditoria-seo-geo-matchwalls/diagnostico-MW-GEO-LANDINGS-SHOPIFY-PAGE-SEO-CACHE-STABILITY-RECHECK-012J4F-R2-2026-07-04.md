# Diagnostico R2 - MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-CACHE-STABILITY-RECHECK-012J4F

Fecha/hora: 2026-07-04 03:48:13 +02:00

## Estado final

`VERIFICADO Y CORRECTO`

## Motivo

Repeticion controlada del lote ya cerrado `MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-CACHE-STABILITY-RECHECK-012J4F`, solicitada por Daniel, para confirmar estabilidad posterior de la meta description publica.

No se modifico Shopify.

## Alcance

- Recurso: Shopify Page.
- Page GID: `gid://shopify/Page/687276622200`.
- Handle: `papel-pintado-espana`.
- URL canonica ES: `https://www.matchwalls.com/pages/papel-pintado-espana`.
- Valor obsoleto vigilado: `Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural.`

## Documentos revisados

- `registro-cambios-ejecutados.md`.
- `diagnostico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-CACHE-STABILITY-RECHECK-012J4F-2026-07-04.md`.

## Admin/API recheck

`VERIFICADO Y CORRECTO`

Consulta Admin GraphQL validada contra schema.

- `id`: `gid://shopify/Page/687276622200`.
- `title`: `Papel pintado en España para hogares y proyectos profesionales`.
- `handle`: `papel-pintado-espana`.
- `bodySummary`: `Papel pintado, murales y soluciones a medida en España En MatchWalls diseñamos papel pintado, murales decorativos y soluciones a medida para transf...`.
- `updatedAt`: `2026-07-04T00:07:41Z`.
- `isPublished`: `true`.
- `global.description_tag`: `null`.
- `global.title_tag`: `null`.

## QA publico canonico R2

`VERIFICADO Y CORRECTO`

Primera matriz:

- 18 intentos sobre URL canonica.
- 17 respuestas 200 limpias.
- 0 apariciones del valor obsoleto 012J3.
- 1 error transitorio de red/SSL en Googlebot simulado.

Reintento dirigido:

- 3/3 respuestas 200 para Googlebot simulado.
- 0 apariciones del valor obsoleto 012J3.
- 0 errores.

Resultado efectivo:

- 20 respuestas publicas validas limpias.
- 0 apariciones del valor obsoleto 012J3.
- Chrome EN canoniza/redirige a `/en/pages/spain-wallpaper` y devuelve meta description inglesa, sin valor obsoleto ES.
- Chrome ES, Googlebot simulado, Bingbot simulado, OAI-SearchBot simulado y PerplexityBot simulado devuelven meta description derivada del body actual ES.

## Limitaciones

- User-agents simulados no equivalen a IPs reales verificadas de crawlers.
- `updatedAt` sigue sin cambiar; no se afirma purga CDN demostrada.
- La verificacion se limita a la pagina `papel-pintado-espana`, no a todas las landings/idiomas/mercados.

## Decision

La incidencia de meta description obsoleta sigue estabilizada en la muestra R2.

Estado: `VERIFICADO Y CORRECTO`.

## Siguiente paso

Volver al plan SEO/GEO y no tocar SEO meta nativo/i18n en esta pagina hasta definir una ruta estable.

