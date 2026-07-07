# QA MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B - 2026-06-25

## Estado final

`RIESGO CRITICO`

El lote fue aprobado y ejecutado sobre el tema auxiliar `178399019384`, pero falló la prueba funcional crítica. Se inició reversión inmediata; la reversión quedó parcial por rechazo de Shopify al reescribir `snippets/external-selectors.liquid` mediante `themeFilesUpsert`.

No se modificó MAIN. No se publicó ningún tema.

## Aprobación

- Aprobación exacta recibida: `APROBADO LOTE MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B`.
- Tema afectado: `gid://shopify/OnlineStoreTheme/178399019384`.
- Rol del tema: `UNPUBLISHED`.
- Prefijo de preview: `/t/46`.
- MAIN confirmado e intacto: `gid://shopify/OnlineStoreTheme/178396463480`.

## Archivos afectados

### `snippets/external-selectors.liquid`

- MD5 previo verificado: `8a9c233bca52da58ce59fffc3aee8359`.
- Tamaño previo verificado: `10199`.
- MD5 candidato 010A2B: `46dc6dcb927f9e8005d0c3bdcba4751d`.
- Tamaño candidato 010A2B: `11062`.
- Estado final en Shopify: `RIESGO CRITICO`; permanece en MD5 `46dc6dcb927f9e8005d0c3bdcba4751d`.

### `snippets/srolling_bar_menu.liquid`

- MD5 previo verificado en auxiliar: `7d6dfb8df5e4b9ef813eca32aaebc237`.
- Tamaño previo verificado: `8539`.
- MD5 candidato 010A2B: `eec87a2c8dc9790a6c499a72e5323337`.
- Tamaño candidato 010A2B: `6991`.
- Estado final en Shopify: `VERIFICADO Y CORRECTO`; revertido a MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`.

## Cambio ejecutado

`INCORRECTO`

- Se añadió tracking propietario en `snippets/external-selectors.liquid`.
- Se retiró la responsabilidad muerta de `input_mural_outside` de `snippets/srolling_bar_menu.liquid`.
- La mutación `themeFilesUpsert` fue validada contra schema y aceptada sin `userErrors` para los dos archivos.
- La lectura posterior confirmó los checksums del candidato en ambos archivos antes de QA.

## QA pública

`INCORRECTO`

URL probada:

`https://www.matchwalls.com/products/custom-file-uploader?preview_theme_id=178399019384&mwqa=010a2b_run_20260625`

Resultados:

- Assets del tema auxiliar `/t/46`: `VERIFICADO Y CORRECTO`.
- Campos externos e internos presentes: `#external-width`, `#external-height`, `#width`, `#height`.
- Sincronización de medidas tras introducir `405 x 305`: `VERIFICADO Y CORRECTO`.
- Cálculo visual de superficie: `4.05m x 3.05m = 12.35 m²`.
- Errores de consola: `0`.
- `window.dataLayer`: no creado.
- Eventos `input_mural_outside`: `0`.

Conclusión: el cambio no resolvió el tracking dinámico. La prueba crítica falló.

## Reversión

`INCOMPLETO`

- Se revirtió correctamente `snippets/srolling_bar_menu.liquid` a MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`.
- `snippets/external-selectors.liquid` no pudo revertirse mediante dos intentos controlados de `themeFilesUpsert`; Shopify devolvió `El contenido incluye caracteres no válidos`.
- El respaldo local de `external-selectors.liquid` tiene MD5 `8a9c233bca52da58ce59fffc3aee8359`, tamaño `10199` y `BadControlCount = 0`.
- MAIN conserva `external-selectors.liquid` con MD5 `8a9c233bca52da58ce59fffc3aee8359`, tamaño `10199`.

## Estado real final verificado en Shopify

- Tema `178399019384`: `UNPUBLISHED`.
- `snippets/external-selectors.liquid`: MD5 `46dc6dcb927f9e8005d0c3bdcba4751d`, tamaño `11062`, actualizado `2026-06-25T12:10:29Z`.
- `snippets/srolling_bar_menu.liquid`: MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`, tamaño `8539`, actualizado `2026-06-25T12:17:56Z`.

## Decisión requerida

`REQUIERE DECISION HUMANA`

No avanzar sobre este tema auxiliar hasta resolver una de estas dos opciones:

1. Reversión manual en editor Shopify de `snippets/external-selectors.liquid` usando el contenido de MAIN/respaldo local.
2. Nuevo lote técnico acotado para corregir `external-selectors.liquid` desde el candidato actual, sin intentar preservar checksum exacto, con QA pública obligatoria.

## Exclusiones respetadas

- No se modificó MAIN.
- No se publicó ningún tema.
- No se cambiaron URLs, handles, canonicals, hreflang, redirecciones, productos, precios, inventario, traducciones, schema ni apps externas.
---

## Actualización posterior R1 - 2026-06-25

`CORREGIDO Y VERIFICADO` para la reversión pendiente.

El lote `MW-TECH-ROLLBACK-EXTERNAL-SELECTORS-010A2B-R1` restauró `snippets/external-selectors.liquid` en el tema auxiliar `178399019384` al MD5 `8a9c233bca52da58ce59fffc3aee8359`. El riesgo crítico del tema auxiliar queda resuelto.

El tracking dinámico permanece `INCORRECTO` porque `input_mural_outside` sigue en `0`. No usar 010A2B como corrección funcional.