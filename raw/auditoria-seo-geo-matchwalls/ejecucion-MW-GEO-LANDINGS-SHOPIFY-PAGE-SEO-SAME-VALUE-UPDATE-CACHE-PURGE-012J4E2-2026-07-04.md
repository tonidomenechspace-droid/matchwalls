# Ejecucion - MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SAME-VALUE-UPDATE-CACHE-PURGE-012J4E2

Fecha/hora: 2026-07-04 03:32:34 +02:00

## Estado final

`VERIFICADO PERO MEJORABLE`

## Aprobacion

Daniel aprobo exactamente:

`APROBADO LOTE MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SAME-VALUE-UPDATE-CACHE-PURGE-012J4E2`

## Alcance

- Recurso: Shopify Page.
- Page GID: `gid://shopify/Page/687276622200`.
- Handle: `papel-pintado-espana`.
- URL publica: `https://www.matchwalls.com/pages/papel-pintado-espana`.
- Accion: mutacion `pageUpdate` validada con valores actuales iguales.
- Exclusiones: no modificar handle, URL, traducciones, LangShop, tema, Liquid, mercados ni metadatos SEO.

## Precheck Admin/API

`VERIFICADO Y CORRECTO`

- `title`: `Papel pintado en España para hogares y proyectos profesionales`.
- `handle`: `papel-pintado-espana`.
- `updatedAt`: `2026-07-04T00:07:41Z`.
- `isPublished`: `true`.
- `templateSuffix`: cadena vacia.
- `global.description_tag`: `null`.
- `global.title_tag`: `null`.
- `bodySummary`: `Papel pintado, murales y soluciones a medida en España En MatchWalls diseñamos papel pintado, murales decorativos y soluciones a medida para transf...`.

## Escritura ejecutada

`VERIFICADO PERO MEJORABLE`

Se ejecuto una mutacion `pageUpdate` validada contra schema con:

- `title`: mismo valor actual.
- `body`: mismo HTML actual leido por API.
- `isPublished`: `true`, mismo valor actual.

No se envio:

- `handle`.
- `redirectNewHandle`.
- `templateSuffix`.
- metadatos SEO.
- traducciones.
- mercado.
- tema.

Resultado Shopify:

- `userErrors`: `[]`.
- `title`: conservado.
- `handle`: conservado.
- `isPublished`: conservado.
- `global.description_tag`: `null`.
- `global.title_tag`: `null`.
- `updatedAt`: se mantuvo en `2026-07-04T00:07:41Z`.

Interpretacion:

- Shopify acepto la mutacion sin errores.
- Sin embargo, al no cambiar `updatedAt`, Shopify parece haber tratado la mutacion como un no-op real.
- Por tanto, no se puede afirmar con evidencia que esta mutacion haya generado una nueva señal de purga CDN.

## Postcheck Admin/API

`VERIFICADO Y CORRECTO`

- Titulo conservado.
- Handle conservado.
- Body HTML conservado.
- `global.description_tag`: `null`.
- `global.title_tag`: `null`.
- `updatedAt`: sin cambio.

## Postcheck publico

`VERIFICADO Y CORRECTO`

Se realizaron 24 comprobaciones HTML:

- 12 con URL QA: `https://www.matchwalls.com/pages/papel-pintado-espana?mwqa=012j4e2`.
- 12 con URL canonica exacta: `https://www.matchwalls.com/pages/papel-pintado-espana`.

Perfiles comprobados en 3 rondas:

- Chrome ES simulado.
- Googlebot simulado.
- Bingbot simulado.
- OAI-SearchBot simulado.

Resultado:

- 24/24 devuelven status 200.
- 24/24 no contienen el valor obsoleto 012J3.
- 24/24 devuelven meta description derivada del body actual:
  `Papel pintado, murales y soluciones a medida en España En MatchWalls diseñamos papel pintado, murales decorativos y soluciones a medida para transformar paredes...`

## Limitaciones

- User-agents simulados no equivalen a IPs reales verificadas de crawlers.
- `updatedAt` no cambio; por tanto, no se puede probar que hubiese purga CDN causada por 012J4E2.
- El resultado publico actual esta limpio en la muestra ejecutada, pero conviene recheck posterior tras propagacion natural.

## Reversion

No requiere reversion de contenido porque los valores finales coinciden con los valores previos.

Si se detectara cualquier diferencia inesperada en el futuro:

- Restaurar el `body` desde el HTML exacto registrado en el precheck de este lote.
- Confirmar `title`, `handle`, `isPublished`, `global.description_tag` y `global.title_tag` contra los valores de precheck.

## Evidencias

- `qa-publico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SAME-VALUE-UPDATE-CACHE-PURGE-012J4E2-2026-07-04.csv`.
- `qa-publico-canonical-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SAME-VALUE-UPDATE-CACHE-PURGE-012J4E2-2026-07-04.csv`.
- `admin-post-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SAME-VALUE-UPDATE-CACHE-PURGE-012J4E2-2026-07-04.csv`.
- `matriz-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SAME-VALUE-UPDATE-CACHE-PURGE-012J4E2-2026-07-04.csv`.

## Siguiente paso seguro

`MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-CACHE-STABILITY-RECHECK-012J4F`

Alcance recomendado:

- Repetir comprobacion publica sobre URL canonica exacta tras un intervalo.
- Mantener user-agents Chrome, Googlebot, Bingbot y OAI-SearchBot simulados.
- Si sigue limpio, cerrar incidencia como comportamiento publico estabilizado.
- Si reaparece valor 012J3, reenviar evidencia a Shopify/LangShop solicitando purga real desde backend.

