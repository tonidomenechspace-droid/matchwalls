# Resultado - MW-COLLECTIONS-I18N-CARD-TITLES-COPY-MAP-013E15

Fecha: 2026-07-05

## Estado final

`VERIFICADO PERO MEJORABLE`

Lote aprobado por Daniel:

`APROBADO LOTE MW-COLLECTIONS-I18N-CARD-TITLES-COPY-MAP-013E15`

## Alcance ejecutado

`VERIFICADO Y CORRECTO`

Se preparó el mapa exacto de cambios propuestos para títulos visibles de tarjetas de colecciones en ES, EN, FR, DE y NL, partiendo del diagnóstico 013E14.

Este lote fue documental y de planificación. No se modificó Shopify.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `resultado-MW-COLLECTIONS-I18N-CARD-TITLES-DIAG-013E14-2026-07-05.md`
- `qa-visible-issues-MW-COLLECTIONS-I18N-CARD-TITLES-DIAG-013E14-2026-07-05.csv`
- `qa-standby-handles-MW-COLLECTIONS-I18N-CARD-TITLES-DIAG-013E14-2026-07-05.csv`
- `registro-cambios-ejecutados.md`

## Estado real comprobado

`VERIFICADO Y CORRECTO`

- Draft `178396463480`: `UNPUBLISHED`, `processing=false`, `processingFailed=false`.
- Draft `sections/main-list-collections.liquid`: checksum `910b00ca49c28be5258ac2a17f1731d5`, size `20882`, updatedAt `2026-07-04T21:29:00Z`.
- MAIN `178399019384`: `MAIN`, `processing=false`, `processingFailed=false`.
- MAIN `sections/main-list-collections.liquid`: checksum `70c8ead00d939f15528f6f11e5bfb540`, size `4934`, updatedAt `2026-06-18T18:30:51Z`.

No se detectó cambio de tema durante este lote.

## Escrituras realizadas

`VERIFICADO Y CORRECTO`

No se realizaron escrituras en Shopify, LangShop, tema MAIN, tema draft, páginas, productos, colecciones, handles, URLs, redirecciones, robots, sitemaps, Bing, IndexNow, precios, inventario ni feeds.

## Copy map propuesto

`VERIFICADO PERO MEJORABLE`

### Correcciones seguras de texto visible, sin handles

| Idioma | Actual | Propuesto | Estado | Prioridad |
|---|---|---|---|---|
| EN | Basin Wallpaper | Cuenca Wallpaper | `INCORRECTO` | Alta |
| FR | Papier Peint Alava | Papier Peint Álava | `VERIFICADO PERO MEJORABLE` | Media |
| FR | Papier Peint Almeria | Papier Peint Almería | `VERIFICADO PERO MEJORABLE` | Media |
| FR | Papier Peint Avila | Papier Peint Ávila | `VERIFICADO PERO MEJORABLE` | Media |
| FR | Papier Peint Jaen | Papier Peint Jaén | `VERIFICADO PERO MEJORABLE` | Media |
| DE | Tapete 3D | 3D-Tapete | `VERIFICADO PERO MEJORABLE` | Media |
| DE | Tapete Gold | Goldene Tapete | `VERIFICADO PERO MEJORABLE` | Media |
| DE | Tapete Japanisch | Japanische Tapete | `VERIFICADO PERO MEJORABLE` | Media |
| NL | Behang 3D | 3D-behang | `VERIFICADO PERO MEJORABLE` | Media |
| NL | Geometrische Behangstijlen | Geometrisch Behang | `VERIFICADO PERO MEJORABLE` | Media |

### Black Friday

`REQUIERE DECISION HUMANA`

No se propone renombrar Black Friday.

Se propone excluirlo del hub/listado evergreen en un lote separado, manteniendo URLs y handles en `STANDBY`, porque 011D/011D1 ya lo trató como campaña obsoleta/noindex.

URLs detectadas:

- ES: `/collections/papel-pintado-black-friday`
- EN: `/en/collections/wallpapers-black-friday`
- FR: `/fr/collections/papiers-peints-black-friday`
- DE: `/de/collections/schwarzer-freitag-wallpaper`
- NL: `/nl/collections/black-friday-wallpaper`

## Handles

`STANDBY`

No se propone tocar handles en 013E15.

Los handles heredados con patrones como `matchwallsmurals`, `matchwallsmurs`, `matchwallswallpapers`, `matchwallswalpapers`, `matchalls` o fragmentos ingleses en FR/DE/NL permanecen fuera del alcance. Su modificación requeriría mapa 301, validación de canonicals/hreflang y aprobación específica.

## Riesgos detectados

`VERIFICADO PERO MEJORABLE`

- Actualizar títulos visibles sin cambiar handles puede dejar una discrepancia temporal entre tarjeta y URL. Se acepta como mejora textual reversible si Daniel aprueba un lote de escritura posterior.
- Black Friday visible en un hub evergreen crea una señal editorial confusa para SEO/GEO/AEO.
- Los cambios de títulos mediante LangShop/Shopify Translate deben verificarse públicamente en ES, EN, FR, DE y NL tras cualquier escritura.

## Reversión futura

`VERIFICADO Y CORRECTO`

Si se aprueba un lote de escritura de títulos, la reversión será restaurar el título visible anterior exacto de cada fila afectada.

Para Black Friday, si se aprueba excluir del hub/listado, la reversión será restaurar su inclusión visual en el hub/listado evergreen.

## Evidencias generadas

`VERIFICADO Y CORRECTO`

- `copy-map-MW-COLLECTIONS-I18N-CARD-TITLES-COPY-MAP-013E15-2026-07-05.csv`
- `admin-read-MW-COLLECTIONS-I18N-CARD-TITLES-COPY-MAP-013E15-2026-07-05.csv`
- `black-friday-policy-MW-COLLECTIONS-I18N-CARD-TITLES-COPY-MAP-013E15-2026-07-05.md`
- `resultado-MW-COLLECTIONS-I18N-CARD-TITLES-COPY-MAP-013E15-2026-07-05.md`

## Siguiente lote seguro recomendado

`REQUIERE DECISION HUMANA`

Para corregir solo textos visibles, sin handles ni Black Friday:

`MW-COLLECTIONS-I18N-CARD-TITLES-SAFE-TEXT-UPDATE-013E16`

Alcance recomendado:

- Actualizar únicamente las 10 correcciones lingüísticas seguras del copy map.
- No cambiar handles.
- No cambiar URLs.
- No tocar Black Friday.
- No tocar redirecciones.
- Verificar ES, EN, FR, DE y NL en storefront.

Para Black Friday:

`MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-EXCLUDE-DECISION-013E16B`

Alcance recomendado:

- Decidir si se excluye Black Friday del hub/listado evergreen.
- No borrar colecciones.
- No cambiar handles ni URLs.
- No crear redirecciones.

