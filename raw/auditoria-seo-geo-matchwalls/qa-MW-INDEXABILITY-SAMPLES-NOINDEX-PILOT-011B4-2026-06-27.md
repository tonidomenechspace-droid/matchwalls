# QA - MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4

Fecha/hora: 2026-06-27 00:36:39 +02:00  
Estado: `CORREGIDO Y VERIFICADO`

## Alcance ejecutado

Se aplico `seo.hidden=1` a 10 productos muestra piloto aprobados.

No se modificaron:

- Handles.
- Canonicals.
- Redirecciones.
- Paginas informativas de muestras.
- Colecciones.
- Tema Shopify.
- Precios.
- Inventario.
- Variantes.
- Apps.
- Search Console, Bing, GA4, GTM, Merchant Center.

## Mutacion ejecutada

`metafieldsSet`

Valores aplicados:

- namespace: `seo`
- key: `hidden`
- value: `1`
- type: `number_integer`

Resultado Shopify:

- Metafields devueltos: 10/10.
- `userErrors`: 0.

## Verificacion Admin posterior

`VERIFICADO Y CORRECTO`

- 10/10 productos tienen `seo.hidden.value = 1`.
- 10/10 productos tienen `seo.hidden.type = number_integer`.
- 10/10 productos siguen `ACTIVE`.
- 10/10 productos siguen publicados.
- 10/10 productos conservan `templateSuffix = muestra`.

Evidencia:

- `admin-seohidden-post-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-2026-06-27.csv`.

## Verificacion publica ES

`VERIFICADO Y CORRECTO`

10 URLs ES revisadas:

- 10/10 status 200.
- 10/10 acceso directo operativo.
- 10/10 `meta robots = noindex,nofollow`.
- 10/10 canonical self.
- 10/10 H1 presente.

Evidencia:

- `qa-publico-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-2026-06-27.csv`.

## Verificacion publica localizada

`VERIFICADO Y CORRECTO`

61 URLs localizadas asociadas a los 10 IDs revisadas:

- 61/61 status 200.
- 61/61 `noindex,nofollow`.
- 61/61 canonical self.
- 61/61 H1 presente.

Evidencia:

- `qa-publico-localizado-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-2026-06-27.csv`.

## Verificacion sitemap inmediata

`VERIFICADO Y CORRECTO`

Sitemap root:

- `https://www.matchwalls.com/sitemap.xml`: 200.
- Product sitemaps revisados: 7.

Resultado:

- 0/10 URLs ES piloto presentes en product sitemaps inmediatamente despues del cambio.

Evidencia:

- `qa-sitemap-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-2026-06-27.csv`.

## Rollback disponible

`VERIFICADO Y CORRECTO`

Estado original:

- `seo.hidden = null` en 10/10.

Rollback:

- Ejecutar `metafieldsDelete` para namespace `seo`, key `hidden`, en los 10 Product GID.
- Esto devuelve el estado original `null`.

Rollback validado previamente contra esquema GraphQL:

- `RollbackSeoHiddenForSamplePilot`.

## Incidencias

Sin incidencias criticas.

Nota: `0 userErrors` no garantiza desindexacion en Google/Bing. Solo confirma aceptacion de Shopify. La desindexacion real depende de rastreo posterior de buscadores.

## Estado final

`CORREGIDO Y VERIFICADO`

El piloto 011B4 queda ejecutado y verificado en Admin, storefront publico ES, storefront localizado y sitemap inmediato.

