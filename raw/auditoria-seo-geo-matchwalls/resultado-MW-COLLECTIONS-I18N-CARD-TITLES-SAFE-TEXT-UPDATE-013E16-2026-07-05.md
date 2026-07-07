# Resultado - MW-COLLECTIONS-I18N-CARD-TITLES-SAFE-TEXT-UPDATE-013E16

Fecha: 2026-07-05

## Estado final

`CORREGIDO Y VERIFICADO`

Lote aprobado por Daniel:

`APROBADO LOTE MW-COLLECTIONS-I18N-CARD-TITLES-SAFE-TEXT-UPDATE-013E16`

## Alcance ejecutado

`VERIFICADO Y CORRECTO`

Se actualizaron únicamente títulos visibles traducidos de colecciones incluidos como seguros en el copy map 013E15.

No se modificaron handles, URLs, redirecciones, canonicals, hreflang, robots, sitemaps, tema MAIN, tema draft, Liquid, productos, precios, inventario, imágenes, Black Friday, Bing, IndexNow, GA4, GTM, Search Console ni LangShop de forma manual.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `resultado-MW-COLLECTIONS-I18N-CARD-TITLES-COPY-MAP-013E15-2026-07-05.md`
- `copy-map-MW-COLLECTIONS-I18N-CARD-TITLES-COPY-MAP-013E15-2026-07-05.csv`
- `registro-cambios-ejecutados.md`

## Estado real comprobado antes de escribir

`VERIFICADO Y CORRECTO`

Se verificaron por Shopify Admin GraphQL los IDs reales de colección, el título fuente, el digest actual del campo `title` y el título traducido actual antes de mutar.

Las 10 filas coincidían exactamente con el copy map 013E15:

| Idioma | Resource ID | Anterior | Nuevo |
|---|---|---|---|
| EN | `gid://shopify/Collection/646110085496` | `Basin Wallpaper` | `Cuenca Wallpaper` |
| FR | `gid://shopify/Collection/443626914019` | `Papier Peint Alava` | `Papier Peint Álava` |
| FR | `gid://shopify/Collection/646109659512` | `Papier Peint Almeria` | `Papier Peint Almería` |
| FR | `gid://shopify/Collection/646109725048` | `Papier Peint Avila` | `Papier Peint Ávila` |
| FR | `gid://shopify/Collection/646110314872` | `Papier Peint Jaen` | `Papier Peint Jaén` |
| DE | `gid://shopify/Collection/439174562019` | `Tapete 3D` | `3D-Tapete` |
| NL | `gid://shopify/Collection/439174562019` | `Behang 3D` | `3D-behang` |
| DE | `gid://shopify/Collection/439057613027` | `Tapete Gold` | `Goldene Tapete` |
| DE | `gid://shopify/Collection/439174627555` | `Tapete Japanisch` | `Japanische Tapete` |
| NL | `gid://shopify/Collection/439174365411` | `Geometrische Behangstijlen` | `Geometrisch Behang` |

## Escrituras realizadas

`CORREGIDO Y VERIFICADO`

Se ejecutó `translationsRegister` sobre el campo `title` de cada recurso/idioma, usando el `translatableContentDigest` vigente.

Resultado:

- 10 traducciones registradas.
- `userErrors`: `0` en todas las mutaciones.
- No se tocaron `handle`, `body_html`, `meta_title`, `meta_description` ni ningún campo no incluido.

## Verificación Admin posterior

`CORREGIDO Y VERIFICADO`

Lectura independiente posterior con Shopify Admin GraphQL confirmó los 10 títulos nuevos almacenados con `outdated=false`.

## Verificación pública posterior

`CORREGIDO Y VERIFICADO`

Se verificó en storefront público:

- `https://www.matchwalls.com/en/collections` contiene `Cuenca Wallpaper`.
- `https://www.matchwalls.com/fr/collections` contiene `Papier Peint Álava`, `Papier Peint Almería`, `Papier Peint Ávila`, `Papier Peint Jaén`.
- `https://www.matchwalls.com/de/collections` contiene `3D-Tapete`, `Goldene Tapete`, `Japanische Tapete`.
- `https://www.matchwalls.com/nl/collections` contiene `3D-behang`, `Geometrisch Behang`.

## Incidencias

`VERIFICADO PERO MEJORABLE`

- Se detecta deuda heredada ajena a este lote: algunos `body_html` traducidos de colecciones geográficas y algunos `handle` heredados siguen siendo mejorables. No se tocaron porque están fuera del alcance aprobado.
- Black Friday permanece en `REQUIERE DECISION HUMANA` para un lote separado.

## Reversión

`VERIFICADO Y CORRECTO`

La reversión consiste en registrar de nuevo los títulos anteriores exactos mediante `translationsRegister`, usando el digest vigente del campo `title`.

Valores de reversión:

- EN `gid://shopify/Collection/646110085496`: `Basin Wallpaper`.
- FR `gid://shopify/Collection/443626914019`: `Papier Peint Alava`.
- FR `gid://shopify/Collection/646109659512`: `Papier Peint Almeria`.
- FR `gid://shopify/Collection/646109725048`: `Papier Peint Avila`.
- FR `gid://shopify/Collection/646110314872`: `Papier Peint Jaen`.
- DE `gid://shopify/Collection/439174562019`: `Tapete 3D`.
- NL `gid://shopify/Collection/439174562019`: `Behang 3D`.
- DE `gid://shopify/Collection/439057613027`: `Tapete Gold`.
- DE `gid://shopify/Collection/439174627555`: `Tapete Japanisch`.
- NL `gid://shopify/Collection/439174365411`: `Geometrische Behangstijlen`.

## Evidencias generadas

`VERIFICADO Y CORRECTO`

- `precheck-MW-COLLECTIONS-I18N-CARD-TITLES-SAFE-TEXT-UPDATE-013E16-2026-07-05.csv`
- `mutation-result-MW-COLLECTIONS-I18N-CARD-TITLES-SAFE-TEXT-UPDATE-013E16-2026-07-05.csv`
- `postcheck-public-MW-COLLECTIONS-I18N-CARD-TITLES-SAFE-TEXT-UPDATE-013E16-2026-07-05.csv`
- `resultado-MW-COLLECTIONS-I18N-CARD-TITLES-SAFE-TEXT-UPDATE-013E16-2026-07-05.md`

## Siguiente lote recomendado

`REQUIERE DECISION HUMANA`

`MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-EXCLUDE-DECISION-013E16B`

Objetivo: decidir si Black Friday debe seguir visible en el hub/listado evergreen o excluirse sin borrar colecciones, sin tocar handles y sin crear redirecciones.
