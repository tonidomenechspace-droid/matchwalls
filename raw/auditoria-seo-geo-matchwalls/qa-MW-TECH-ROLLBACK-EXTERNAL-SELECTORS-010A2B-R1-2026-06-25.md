# QA MW-TECH-ROLLBACK-EXTERNAL-SELECTORS-010A2B-R1 - 2026-06-25

## Estado final

`CORREGIDO Y VERIFICADO`

Rollback ejecutado y verificado sobre el tema auxiliar `178399019384`. El archivo `snippets/external-selectors.liquid` volvió al checksum previo correcto.

No se modificó MAIN. No se publicó ningún tema.

## Aprobación

- Aprobación exacta recibida: `APROBADO LOTE MW-TECH-ROLLBACK-EXTERNAL-SELECTORS-010A2B-R1`.
- Tema afectado: `gid://shopify/OnlineStoreTheme/178399019384`.
- Rol del tema: `UNPUBLISHED`.
- Prefijo de preview: `/t/46`.
- MAIN confirmado previamente: `gid://shopify/OnlineStoreTheme/178396463480`, sin modificación.

## Recurso restaurado

`snippets/external-selectors.liquid`

- Estado antes del rollback R1: MD5 `46dc6dcb927f9e8005d0c3bdcba4751d`, tamaño `11062`.
- Estado objetivo: MD5 `8a9c233bca52da58ce59fffc3aee8359`, tamaño `10199`.
- Estado final verificado en Shopify: MD5 `8a9c233bca52da58ce59fffc3aee8359`, tamaño `10199`, actualizado `2026-06-25T13:07:38Z`.

## Contexto

El lote `MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B` falló QA porque el evento `input_mural_outside` siguió en `0`. La reversión automática por `themeFilesUpsert` falló dos veces para `external-selectors.liquid` por rechazo de contenido. En R1 se realizó la reversión desde el editor Shopify y se verificó por checksum real.

## Método de ejecución

- Editor Shopify del tema auxiliar abierto con `key=snippets/external-selectors.liquid`.
- Contenido restaurado desde respaldo local con MD5 `8a9c233bca52da58ce59fffc3aee8359`.
- Antes de guardar, se verificó en el editor que ya no aparecía la función experimental `pushInputMuralOutsideEvent` añadida en el candidato de `external-selectors.liquid`.
- Guardado mediante editor Shopify.
- Lectura posterior con Admin GraphQL validada contra schema.

## Estado real final en Shopify

- Tema `178399019384`: `UNPUBLISHED`, `processing=false`, `processingFailed=false`.
- `snippets/external-selectors.liquid`: `VERIFICADO Y CORRECTO`, MD5 `8a9c233bca52da58ce59fffc3aee8359`, size `10199`.
- `snippets/srolling_bar_menu.liquid`: `VERIFICADO Y CORRECTO`, MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`, size `8539`.

## QA público de rollback

`VERIFICADO Y CORRECTO`

Preview probado en producto `custom-file-uploader` con tema auxiliar `/t/46`.

Resultados:

- Assets `/t/46`: `VERIFICADO Y CORRECTO`.
- Campos externos: `#external-width` y `#external-height` presentes.
- Campos internos: `#width` y `#height` presentes.
- Prueba `407 x 307`: campos internos sincronizados a `407 x 307`.
- Superficie visible: `4.07m x 3.07m = 12.49 m²`.
- Funciones experimentales del candidato 010A2B en `external-selectors.liquid`: `pushExternalWidthTracking` y `pushExternalHeightTracking` ausentes.
- `window.dataLayer`: no creado; `input_mural_outside`: `0`.

Nota: este rollback restaura estabilidad, pero no corrige el tracking dinámico. El bug de tracking sigue `INCORRECTO` y requiere nuevo diagnóstico/lote si se decide continuar.

## Exclusiones respetadas

- No se modificó MAIN.
- No se publicó ningún tema.
- No se cambiaron URLs, handles, canonicals, hreflang, redirecciones, productos, precios, inventario, traducciones, schema ni apps externas.