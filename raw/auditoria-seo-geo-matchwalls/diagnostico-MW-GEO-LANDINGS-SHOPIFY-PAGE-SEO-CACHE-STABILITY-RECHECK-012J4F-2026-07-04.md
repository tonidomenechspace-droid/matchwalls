# Diagnostico - MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-CACHE-STABILITY-RECHECK-012J4F

Fecha/hora: 2026-07-04 03:39:44 +02:00

## Estado final

`VERIFICADO Y CORRECTO`

## Alcance

Lote de solo lectura para comprobar estabilidad publica de `page_description` despues de:

- rollback de 012J3;
- soporte Shopify;
- intento UI 012J4E bloqueado;
- same-value update 012J4E2 aceptado sin cambio de `updatedAt`;
- QA publica limpia inicial de 012J4E2.

Recurso:

- Shopify Page: `gid://shopify/Page/687276622200`.
- Handle: `papel-pintado-espana`.
- URL canonica ES: `https://www.matchwalls.com/pages/papel-pintado-espana`.

No se modifico Shopify.

## Documentos leidos

- `registro-cambios-ejecutados.md`.
- `ejecucion-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SAME-VALUE-UPDATE-CACHE-PURGE-012J4E2-2026-07-04.md`.
- `qa-publico-canonical-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SAME-VALUE-UPDATE-CACHE-PURGE-012J4E2-2026-07-04.csv`.

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

No hay cambio inesperado en Admin/API.

## QA publico canonico

`VERIFICADO Y CORRECTO`

Se ejecuto una matriz publica sobre:

`https://www.matchwalls.com/pages/papel-pintado-espana`

Perfiles:

- Chrome ES simulado.
- Chrome EN simulado.
- Googlebot simulado.
- Bingbot simulado.
- OAI-SearchBot simulado.
- PerplexityBot simulado.

Primera ronda:

- 30 intentos.
- 27 respuestas 200 limpias.
- 0 apariciones del valor obsoleto 012J3.
- 3 errores transitorios de red/timeout en muestras aisladas.

Reintento de perfiles con errores:

- 6/6 respuestas 200.
- 0 errores.
- 0 apariciones del valor obsoleto 012J3.

Resultado efectivo:

- No se reproduce la contaminacion 012J3.
- Chrome ES, Googlebot simulado, Bingbot simulado, OAI-SearchBot simulado y PerplexityBot simulado devuelven meta description derivada del body actual ES.
- Chrome EN redirige/canoniza a la URL EN `/en/pages/spain-wallpaper` y devuelve meta description inglesa; no contiene el valor obsoleto ES.

## Valor obsoleto vigilado

`Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural.`

Resultado:

- No aparece en la muestra final.

## Limitaciones

- Los user-agents son simulados; no equivalen a IPs reales verificadas de Google, Bing, OpenAI, Perplexity u otros crawlers.
- `updatedAt` sigue sin cambiar desde `2026-07-04T00:07:41Z`; por tanto, no se afirma que 012J4E2 haya forzado una purga CDN.
- Lo que sí queda verificado es que el HTML publico actual, en la muestra ejecutada, ya no devuelve el valor obsoleto.

## Decision

La incidencia publica de valor SEO obsoleto 012J3 queda estabilizada en la muestra actual.

Estado: `VERIFICADO Y CORRECTO`.

## Siguiente paso recomendado

Volver al plan SEO/GEO:

1. Mantener este caso en observacion pasiva.
2. No tocar de nuevo metadescripciones nativas multidioma hasta definir una ruta estable para SEO meta i18n.
3. Continuar con landings geograficas y auditoria SEO/GEO segun cola maestra.

Si reaparece el valor 012J3 en un futuro:

- Reabrir con evidencia nueva.
- Enviar a Shopify/LangShop la comparativa Admin/API limpio vs HTML contaminado.
- Solicitar purga backend real.

