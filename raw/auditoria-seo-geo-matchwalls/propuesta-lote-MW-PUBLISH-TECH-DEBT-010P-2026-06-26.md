# Propuesta de lote - MW-PUBLISH-TECH-DEBT-010P

Fecha: 2026-06-26 23:22:27 +02:00

## Estado

`REQUIERE DECISION HUMANA`

Esta propuesta no ejecuta ninguna publicación. Para publicar se requiere aprobación exacta:

`APROBADO LOTE MW-PUBLISH-TECH-DEBT-010P`

## Objetivo

Publicar el tema técnico QA `178399019384`, que contiene la deuda técnica corregida y verificada en los sublotes 010A-010C5, y conservar el MAIN actual `178396463480` como reversión inmediata.

## Recursos afectados

### Tema actual publicado

- ID histórico verificado: `gid://shopify/OnlineStoreTheme/178396463480`.
- Rol verificado en 010Z2: `MAIN`.
- Prefijo público verificado en 010Z3 live: `/t/45`.
- Función propuesta tras publicación: tema de rollback/reversión.

### Tema candidato a publicar

- ID histórico verificado: `gid://shopify/OnlineStoreTheme/178399019384`.
- Rol verificado en 010Z2: `UNPUBLISHED`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Prefijo preview verificado en 010Z3: `/t/46`.
- Función propuesta tras publicación: nuevo `MAIN`.

## Limitación previa obligatoria

En 010Z3, Shopify CLI/Admin API fue `NO ACCESIBLE`; el comando `shopify` no estaba disponible en PATH.

Por tanto, antes de pulsar publicar debe hacerse un preflight visual/read-only en Shopify Admin:

1. Confirmar que `178399019384` sigue existiendo.
2. Confirmar que `178399019384` sigue siendo el tema QA esperado.
3. Confirmar que `178399019384` no está ya publicado.
4. Confirmar que `178396463480` sigue siendo el MAIN actual o identificar el MAIN real si ha cambiado.
5. Confirmar que existe rollback publicable.
6. Confirmar que no hay banners de error, `processing`, tema corrupto o cambios inesperados.

Si cualquiera de estos puntos no coincide, no publicar y detener el lote.

## Cambios incluidos al publicar el tema QA

La publicación no cambia archivos individuales: cambia el rol del tema completo. Los cambios técnicos relevantes ya verificados dentro del tema QA son:

| Archivo | QA verificado | MAIN/rollback verificado | Motivo |
| --- | --- | --- | --- |
| `snippets/srolling_bar_menu.liquid` | MD5 `7d6dfb8df5e4b9ef813eca32aaebc237` | MD5 `c254cf711a7706dc21ece2f2ad31acea` | Guardia `addEventListener`; evita error JS global |
| `snippets/external-selectors.liquid` | MD5 `95266feda1603e9c9ef028f0dae74c6f` | MD5 `8a9c233bca52da58ce59fffc3aee8359` | Tracking dinámico de medidas |
| `snippets/product-customizer.liquid` | MD5 `d5a74ccb15b645eeb79e8c52f7c5a4ac` | MD5 `3878a24a9bb6cb134247ac6aff707a58` | Guards de file input y modal |
| `assets/customizer.js` | MD5 `6684ed205824c8ba660bd4c67a5e26fc` | MD5 `2a26be9d6af37a992526274df431deaa` | Protección `convertToInches` |
| `assets/theme.css` | MD5 `b86a0e260263eed6a2586a3e7bca8e05` | MD5 `89f4729809a0eaac75a764e0fc41888e` | Correcciones overflow móvil |
| `sections/collection-logo-list.liquid` | MD5 `e246746230f64c88b529db9aa370f3e2` | MD5 `44d02156951a46f0147f3ee3de61f38e` | CSS de home no rastreable como texto |
| `snippets/variant-picker.liquid` | MD5 `44af7568d1ddeb65f5fabe7b782c7a05` | MD5 `48ef3d83e49275ccea7f044c1b56d2d8` | Neutralización de tooltip móvil que causaba overflow |
| `sections/related-products.liquid` | MD5 `d8822a8c73cee73d61744c0b68b7a375` | MD5 `d8822a8c73cee73d61744c0b68b7a375` | Sin cambio final; 010C3 fue revertido |

## Evidencia disponible

- `MW-TECH-QA-FULL-REGRESSION-010Z3`: `VERIFICADO Y CORRECTO`.
- Matriz principal: 170/170.
- Anexo técnico: 13/13.
- Tema QA preview `/t/46`: 170/170.
- Assets MAIN `/t/45` dentro de QA: 0/170.
- H1 esperado y único: 170/170.
- Canonical propio: 170/170.
- Hreflang prioritario ES/EN/FR/DE/NL: 170/170.
- `html lang`: 170/170.
- Sin `noindex`: 170/170.
- Contenido no vacío: 170/170.
- Overflow real: 0/170.
- Consola: 0 errores críticos.
- Tracking `input_mural_outside`: `CORREGIDO Y VERIFICADO`.
- Home CSS visible/rastreable como texto: corregido en QA.
- FR/NL mobile 375 y 390: overflow corregido en QA.

Documentos:

- `qa-MW-TECH-QA-FULL-REGRESSION-010Z3-2026-06-26.md`.
- `matriz-MW-TECH-QA-FULL-REGRESSION-010Z3-2026-06-26.csv`.
- `matriz-tecnica-MW-TECH-QA-FULL-REGRESSION-010Z3-2026-06-26.csv`.

## Valores propuestos

Antes:

- `178396463480`: `MAIN`.
- `178399019384`: `UNPUBLISHED`.

Después:

- `178399019384`: `MAIN`.
- `178396463480`: tema no publicado conservado como reversión.

## Riesgos

`Alto`, porque publicar un tema afecta toda la tienda.

Riesgos específicos:

- App embeds o configuración de tema no visibles por Admin API en este turno.
- Shopify puede mostrar un MAIN real distinto si alguien publicó otro tema después de 010Z3.
- El preview QA está verificado, pero la publicación cambia el contexto público de todo el sitio.
- Checkout real, pago, subida real de archivo y datos externos no fueron probados en 010Z3.
- La publicación corrige deuda técnica, pero no resuelve indexabilidad, política de muestras, colecciones geográficas, redirecciones, CWV, Bing/Copilot ni entidad/schema global.

## Método exacto de ejecución

1. Abrir Shopify Admin > Online Store > Themes.
2. Confirmar tema actual `MAIN`.
3. Confirmar tema candidato `178399019384`.
4. Confirmar rollback `178396463480`.
5. Publicar `178399019384`.
6. No tocar archivos, apps, productos, precios, menús, URLs ni configuración adicional.
7. Si Shopify muestra aviso inesperado o tema distinto, cancelar.

## Método exacto de reversión

Si tras publicar aparece fallo crítico:

1. Volver a Shopify Admin > Online Store > Themes.
2. Publicar de nuevo `178396463480`.
3. Confirmar que live vuelve a `/t/45`.
4. Repetir pruebas centinela.

No se requiere restaurar archivos manualmente si el rollback theme permanece intacto.

## Pruebas posteriores obligatorias

Inmediatas tras publicar:

1. Confirmar live carga el nuevo tema publicado.
2. Home ES desktop/mobile.
3. 17 páginas × 5 idiomas × desktop/mobile = 170 pruebas.
4. Uploader ES/EN/FR/DE/NL.
5. FR/NL mobile 375 y 390.
6. Producto estándar con swatches.
7. Tracking `input_mural_outside`.
8. Home CSS no visible como texto.
9. Consola sin errores críticos.
10. Canonical, hreflang, `html lang`, H1, noindex y overflow.

## Criterio de salida

`CORREGIDO Y VERIFICADO` solo si:

- Publicación completada sin error.
- Nuevo live carga el tema esperado.
- 170/170 post-publicación correctas.
- Anexo técnico post-publicación correcto.
- Registro de cambios actualizado.

## Decisión requerida

Para ejecutar, Daniel debe responder exactamente:

`APROBADO LOTE MW-PUBLISH-TECH-DEBT-010P`

Sin esa frase exacta, no se ejecuta publicación.
