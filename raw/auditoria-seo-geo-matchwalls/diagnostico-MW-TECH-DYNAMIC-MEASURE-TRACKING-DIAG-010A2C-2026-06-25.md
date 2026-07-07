# Diagnostico - MW-TECH-DYNAMIC-MEASURE-TRACKING-DIAG-010A2C

Fecha: 2026-06-25.

Estado: `REQUIERE DECISION HUMANA`.

## 1. Documentos leidos

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `qa-MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2-2026-06-18.md`.
- `propuesta-lote-MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2-2026-06-18.md`.
- `diagnostico-MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B-2026-06-25.md`.
- `propuesta-lote-MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B-2026-06-25.md`.
- `qa-MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B-2026-06-25.md`.
- `qa-MW-TECH-ROLLBACK-EXTERNAL-SELECTORS-010A2B-R1-2026-06-25.md`.
- `cola-maestra-lotes-publicacion-seo-geo-2026-06-18.csv`.
- `lista-maestra-errores-cambios-evoluciones-mejoras.md`.

## 2. Estado real Shopify comprobado

Consulta Admin GraphQL de solo lectura validada contra schema antes de ejecutarse.

Tema MAIN:

- ID: `gid://shopify/OnlineStoreTheme/178396463480`.
- Nombre: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- Rol: `MAIN`.
- Prefijo: `/t/45`.
- `processing=false`.
- `processingFailed=false`.

Tema auxiliar:

- ID: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol: `UNPUBLISHED`.
- Prefijo: `/t/46`.
- `processing=false`.
- `processingFailed=false`.

Archivos relevantes verificados:

| Tema | Archivo | MD5 | Bytes | Estado |
|---|---|---:|---:|---|
| MAIN `178396463480` | `snippets/external-selectors.liquid` | `8a9c233bca52da58ce59fffc3aee8359` | 10199 | `VERIFICADO Y CORRECTO` |
| Auxiliar `178399019384` | `snippets/external-selectors.liquid` | `8a9c233bca52da58ce59fffc3aee8359` | 10199 | `VERIFICADO Y CORRECTO` |
| MAIN `178396463480` | `snippets/srolling_bar_menu.liquid` | `c254cf711a7706dc21ece2f2ad31acea` | 8581 | `VERIFICADO PERO MEJORABLE` |
| Auxiliar `178399019384` | `snippets/srolling_bar_menu.liquid` | `7d6dfb8df5e4b9ef813eca32aaebc237` | 8539 | `VERIFICADO PERO MEJORABLE` |
| MAIN `178396463480` | `assets/customizer.js` | `2a26be9d6af37a992526274df431deaa` | 40768 | `VERIFICADO PERO MEJORABLE` |
| Auxiliar `178399019384` | `assets/customizer.js` | `6684ed205824c8ba660bd4c67a5e26fc` | 40832 | `VERIFICADO PERO MEJORABLE` |
| MAIN `178396463480` | `snippets/product-customizer.liquid` | `3878a24a9bb6cb134247ac6aff707a58` | 49228 | `VERIFICADO PERO MEJORABLE` |
| Auxiliar `178399019384` | `snippets/product-customizer.liquid` | `d5a74ccb15b645eeb79e8c52f7c5a4ac` | 49230 | `VERIFICADO PERO MEJORABLE` |

Conclusiones de estado:

- El rollback R1 esta confirmado: `external-selectors.liquid` del auxiliar vuelve a coincidir con MAIN.
- El tema auxiliar esta estable y sigue `UNPUBLISHED`.
- MAIN no fue modificado en este diagnostico.
- Shopify no fue modificado en este diagnostico.

## 3. Evidencia de codigo

`snippets/external-selectors.liquid` es el propietario funcional de los campos de medida:

- Lineas 66-67: obtiene `#external-width` y `#external-height`.
- Lineas 147-159: listeners reales de `externalWidthInput` y `externalHeightInput`.
- Esos listeners sincronizan inputs internos, actualizan el personalizador, recalculan superficie y guardan en `localStorage`.
- No empujan `input_mural_outside`.

`snippets/srolling_bar_menu.liquid` en auxiliar contiene el tracking historico:

- Lineas 243-244: obtiene `#external-width` y `#external-height`.
- Lineas 255-263: define `pushInputMuralOutsideEvent`.
- Lineas 273-287: registra listeners si existen los campos.

Historial contrastado:

- `010A2` intento resolverlo desde `srolling_bar_menu.liquid` con listener delegado y fallo con 0 eventos.
- `010A2B` intento mover la responsabilidad a `external-selectors.liquid` con helper/debounce y limpieza del header; fallo con 0 eventos y fue revertido por R1.

## 4. QA publica 010A2C

URL probada:

- `https://www.matchwalls.com/products/custom-file-uploader?preview_theme_id=178399019384&mwqa=010a2c_diag_20260625`.

Resultado de preview:

- URL final en navegador: `https://www.matchwalls.com/products/custom-file-uploader?mwqa=010a2c_diag_20260625`.
- Assets del tema auxiliar `/t/46`: `VERIFICADO Y CORRECTO`.
- Titulo: `Papel pintado y mural personalizado | MatchWalls`.
- `html lang`: `es`.
- `#external-width`: 1.
- `#external-height`: 1.
- `#width`: 1.
- `#height`: 1.

Prueba funcional:

- Anchura externa: `401`.
- Altura externa: `301`.
- Anchura interna: `401`.
- Altura interna: `301`.
- Superficie visible: `4.01m x 3.01m = 12.07 m²`.
- Superficie en customizer: `4.01m x 3.01m = 12.07 m²`.
- Errores de consola: 0.

Tracking observado por el navegador:

- `window.dataLayer`: no creado.
- Eventos `input_mural_outside`: 0.
- Script renderizado con `input_mural_outside`: presente en script inline indice 98.
- Script renderizado de `external-selectors.liquid`: presente en script inline indice 103.
- `pushExternalWidthTracking`: ausente tras rollback R1.

## 5. Limitacion tecnica de verificacion

Se intento una comprobacion puente para leer el `window.dataLayer` real de la pagina sin depender del contexto de lectura del navegador.

Resultado:

- `document.createElement` no esta disponible en el `evaluate` seguro del navegador.
- La URL `javascript:` fue bloqueada por politica de seguridad del navegador.

Estado de esta comprobacion:

`NO ACCESIBLE`.

Por rigor, esta prueba puente no se usa como evidencia positiva ni negativa. La evidencia valida de 010A2C queda limitada a la QA publica soportada por el navegador, la inspeccion del HTML renderizado, los checksums remotos y el historial de QA.

## 6. Diagnostico

Estado del tracking dinamico:

`INCORRECTO`.

Hechos verificados:

- El tema auxiliar esta estable y no publicado.
- `external-selectors.liquid` esta restaurado y coincide con MAIN.
- Los campos de medida funcionan: actualizan inputs internos y superficie.
- El evento `input_mural_outside` sigue sin observarse en QA soportada.
- No hay errores de consola en la prueba `401 x 301`.
- El candidato `010A2B` no debe reutilizarse tal cual.

Inferencia tecnica:

- `srolling_bar_menu.liquid` no es un punto fiable para este tracking.
- `external-selectors.liquid` sigue siendo el punto funcional correcto, pero el enfoque `010A2B` con helper/debounce no demostro el evento.
- Antes de una nueva correccion permanente conviene usar una verificacion que exponga el resultado en DOM o en una senal QA visible desde el navegador, para no depender solo de lectura directa de `window.dataLayer`.

## 7. Siguiente paso recomendado

Crear un lote nuevo, no reutilizar `010A2B`:

`MW-TECH-DYNAMIC-MEASURE-TRACKING-EXTERNAL-DIRECT-010A2D`

Objetivo:

- Intervenir solo `snippets/external-selectors.liquid` en el tema auxiliar.
- Empujar `input_mural_outside` directamente dentro de los listeners ya funcionales de `externalWidthInput` y `externalHeightInput`.
- Evitar helper/debounce nuevo en esta iteracion.
- Incluir una senal QA temporal limitada por parametro `mwqa` para verificar en DOM que el evento se genera en el contexto real de la pagina.
- No tocar MAIN.
- No publicar.
- No limpiar todavia `srolling_bar_menu.liquid` hasta ver si hay duplicado real. Si hay duplicado, revertir y separar limpieza en sublote propio.

## 8. Acciones realizadas

- Lectura de registros.
- Lectura Shopify Admin GraphQL validada.
- Inspeccion de codigo local con checksum contrastado.
- QA publica sobre preview del tema auxiliar.
- Ninguna mutacion Shopify.
- Ninguna publicacion.
- Ningun cambio en MAIN.