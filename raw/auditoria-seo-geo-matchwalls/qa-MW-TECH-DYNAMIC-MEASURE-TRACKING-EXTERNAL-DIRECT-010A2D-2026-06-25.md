# QA MW-TECH-DYNAMIC-MEASURE-TRACKING-EXTERNAL-DIRECT-010A2D - 2026-06-25

## Estado final

`CORREGIDO Y VERIFICADO`

Lote ejecutado sobre el tema auxiliar `178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.

No se modifico MAIN. No se publico ningun tema.

## Aprobacion

Aprobacion exacta recibida:

`APROBADO LOTE MW-TECH-DYNAMIC-MEASURE-TRACKING-EXTERNAL-DIRECT-010A2D`

## Alcance ejecutado

Archivo modificado:

- `snippets/external-selectors.liquid`.

Exclusiones respetadas:

- No se modifico `snippets/srolling_bar_menu.liquid`.
- No se modifico MAIN `178396463480`.
- No se publicaron temas.
- No se modificaron productos, precios, variantes, inventario, GTM, GA4, URLs, handles, canonicals, hreflang ni redirecciones.

## Estado previo

Tema auxiliar:

- ID: `gid://shopify/OnlineStoreTheme/178399019384`.
- Rol: `UNPUBLISHED`.
- `processing=false`.
- `processingFailed=false`.

Archivo previo:

- `snippets/external-selectors.liquid`.
- MD5 previo: `8a9c233bca52da58ce59fffc3aee8359`.
- Bytes previos: `10199`.

## Cambio ejecutado

En `snippets/external-selectors.liquid`:

- Se añadio `pushInputMuralOutsideEvent(dimension, value)` junto al flujo funcional de los campos de medida.
- Se añadio `updateMeasureTrackingQa(payload)` solo activa cuando la URL contiene `mwqa=010a2d`, para permitir QA publica verificable en DOM.
- Se invoco `pushInputMuralOutsideEvent('width', externalWidthInput.value)` dentro del listener ya existente de anchura.
- Se invoco `pushInputMuralOutsideEvent('height', externalHeightInput.value)` dentro del listener ya existente de altura.
- No se modifico calculo de superficie, unidades, precio, personalizador ni `localStorage`.

Validaciones previas:

- Busqueda Shopify Liquid ejecutada sobre `theme snippet javascript`.
- Parser JS local: `VERIFICADO Y CORRECTO`.
- Validador Shopify Liquid local: `NO ACCESIBLE` por dependencia local ausente `@shopify/theme-check-common`; no fue un error del codigo candidato.
- Mutacion `themeFilesUpsert` validada contra schema antes de ejecutarse.

## Resultado almacenado

`VERIFICADO Y CORRECTO`

Respuesta de `themeFilesUpsert`:

- `userErrors`: `[]`.
- Archivo: `snippets/external-selectors.liquid`.
- MD5 nuevo: `95266feda1603e9c9ef028f0dae74c6f`.
- Bytes: `11109`.
- `updatedAt`: `2026-06-25T13:48:06Z`.

Lectura posterior independiente:

- Tema auxiliar: `UNPUBLISHED`.
- `processing=false`.
- `processingFailed=false`.
- MD5 almacenado: `95266feda1603e9c9ef028f0dae74c6f`.
- Contenido con `updateMeasureTrackingQa`, `pushInputMuralOutsideEvent`, llamada de anchura y llamada de altura presentes.

## QA publica critica - ES

URL:

- `https://www.matchwalls.com/products/custom-file-uploader?preview_theme_id=178399019384&mwqa=010a2d`.

Resultado:

- Assets `/t/46`: `VERIFICADO Y CORRECTO`.
- `#external-width`: 1.
- `#external-height`: 1.
- `#width`: 1.
- `#height`: 1.
- Prueba `421 x 321`: inputs internos sincronizados.
- Superficie: `4.21m x 3.21m = 13.51 m²`.
- Señal QA: `data-mw010a2d-count=2`.
- Ultimo evento: `event=input_mural_outside`, `dimension=height`, `value=321`.
- Errores de consola: 0.

Prueba secuencial:

- Antes: count `2`.
- Anchura `422`: count `3`, `dimension=width`, `value=422`, superficie `4.22m x 3.21m = 13.55 m²`.
- Altura `322`: count `4`, `dimension=height`, `value=322`, superficie `4.22m x 3.22m = 13.59 m²`.
- Errores de consola: 0.

Nota tecnica:

- La lectura directa de `window.dataLayer` desde el navegador de QA permanece opaca por el contexto seguro del navegador.
- La señal DOM `data-mw010a2d-*` confirma que el codigo del tema empuja el evento en el contexto real; los payloads aparecen enriquecidos con `gtm.uniqueEventId`, señal coherente con procesamiento de GTM.

## Mini-QA multidioma en URL critica

Producto: `custom-file-uploader`.

| Idioma | URL final | Assets `/t/46` | Campos | Prueba | Evento QA | Consola | Estado |
|---|---|---|---|---|---|---|---|
| ES | `/products/custom-file-uploader?mwqa=010a2d` | Si | 4/4 | `412 x 312` | count `2`, `height=312` | 0 errores | `VERIFICADO Y CORRECTO` |
| EN | `/en/products/custom-file-uploader?mwqa=010a2d` | Si | 4/4 | `412 x 312` | count `2`, `height=312` | 0 errores | `VERIFICADO Y CORRECTO` |
| FR | `/fr/products/telechargeur-de-fichiers-personnalise?mwqa=010a2d` | Si | 4/4 | `412 x 312` | count `2`, `height=312` | 0 errores | `VERIFICADO Y CORRECTO` |
| DE | `/de/products/benutzerdefinierte-datei-uploader?mwqa=010a2d` | Si | 4/4 | altura `313` en reintento | count `1`, `height=313` | 0 errores | `VERIFICADO Y CORRECTO` |
| NL | `/nl/products/aangepaste-bestandsbelaster?mwqa=010a2d` | Si | 4/4 | `412 x 312` | count `2`, `height=312` | 0 errores | `VERIFICADO Y CORRECTO` |

## QA producto estandar

Producto centinela:

- `lineas-noridcas-verde`.

Resultado:

- URL QA: `https://www.matchwalls.com/products/lineas-noridcas-verde?preview_theme_id=178399019384&mwqa=010a2d`.
- URL final: `https://www.matchwalls.com/products/lineas-noridcas-verde?mwqa=010a2d`.
- Assets `/t/46`: `VERIFICADO Y CORRECTO`.
- H1: `Líneas Nórdicas Verde`.
- Campos `#external-width` y `#external-height`: presentes.
- Anchura `403`: evento QA `dimension=width`, `value=403`.
- Superficie observada: `4.03m x 3.22m = 12.98 m²`.
- Consola: 0 errores.

Limitacion:

- El navegador de QA fallo al intentar reescribir altura en este producto estandar por re-render del control (`Focused input target no longer matches the resolved locator`).
- La altura se verifico correctamente en la URL critica y en DE reintentado.

Estado producto estandar: `VERIFICADO PERO MEJORABLE`.

## Reversion disponible

Si hubiera que revertir este sublote:

- Restaurar `snippets/external-selectors.liquid` al MD5 `8a9c233bca52da58ce59fffc3aee8359`, bytes `10199`.
- Confirmar por GraphQL.
- No publicar.

## Estado final

`CORREGIDO Y VERIFICADO`

El tracking dinamico `input_mural_outside` queda corregido y verificado en el tema auxiliar `178399019384`. Sigue pendiente cualquier decision de publicacion y la matriz completa antes de publicar.