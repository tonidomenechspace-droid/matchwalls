# Diagnostico — MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B

Fecha: 2026-06-25.

Estado: `REQUIERE DECISION HUMANA`.

## 1. Documentos leidos

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `cola-maestra-lotes-publicacion-seo-geo-2026-06-18.csv`.
- `lista-maestra-errores-cambios-evoluciones-mejoras.md`.
- `propuesta-lote-MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2-2026-06-18.md`.
- `qa-MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2-2026-06-18.md`.
- Archivos locales comparativos:
  - `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E/snippets/external-selectors.liquid`.
  - `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E/snippets/srolling_bar_menu.liquid`.

## 2. Estado historico contrastado

`MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2` fue ejecutado y revertido el 2026-06-18.

Resultado historico verificado en registros:

- Lote `010A2`: `INCORRECTO`.
- Se modifico solo `snippets/srolling_bar_menu.liquid`.
- Checksum experimental: `fc76e23f024cbda9ba30f40aec5c2c1e`.
- Prueba critica: 0 eventos `input_mural_outside` en anchura y altura.
- Reversion completada a `7d6dfb8df5e4b9ef813eca32aaebc237`.

## 3. Estado real Shopify comprobado

Consulta Admin GraphQL validada contra esquema antes de ejecutarse.

Tema MAIN actual:

- ID: `gid://shopify/OnlineStoreTheme/178396463480`.
- Nombre: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- Rol: `MAIN`.
- Prefijo: `/t/45`.
- `processing`: `false`.
- `processingFailed`: `false`.

Tema auxiliar:

- ID: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol: `UNPUBLISHED`.
- Prefijo: `/t/46`.
- `processing`: `false`.
- `processingFailed`: `false`.

Tema rollback:

- ID: `gid://shopify/OnlineStoreTheme/178383749496`.
- Nombre: `SEO schema hotfix - 2026-06-15`.
- Rol: `UNPUBLISHED`.
- Prefijo: `/t/43`.
- `processing`: `false`.
- `processingFailed`: `false`.

## 4. Checksums remotos

| Tema | Archivo | MD5 | Bytes | Estado |
|---|---|---:|---:|---|
| MAIN `178396463480` | `snippets/external-selectors.liquid` | `8a9c233bca52da58ce59fffc3aee8359` | 10199 | `VERIFICADO Y CORRECTO` |
| MAIN `178396463480` | `snippets/srolling_bar_menu.liquid` | `c254cf711a7706dc21ece2f2ad31acea` | 8581 | `VERIFICADO PERO MEJORABLE` |
| Auxiliar `178399019384` | `snippets/external-selectors.liquid` | `8a9c233bca52da58ce59fffc3aee8359` | 10199 | `VERIFICADO PERO MEJORABLE` |
| Auxiliar `178399019384` | `snippets/srolling_bar_menu.liquid` | `7d6dfb8df5e4b9ef813eca32aaebc237` | 8539 | `VERIFICADO PERO MEJORABLE` |
| Rollback `178383749496` | `snippets/external-selectors.liquid` | `8a9c233bca52da58ce59fffc3aee8359` | 10199 | `VERIFICADO Y CORRECTO` |
| Rollback `178383749496` | `snippets/srolling_bar_menu.liquid` | `c254cf711a7706dc21ece2f2ad31acea` | 8581 | `VERIFICADO Y CORRECTO` |

## 5. Prueba publica en preview auxiliar

URL probada:

- `https://www.matchwalls.com/products/custom-file-uploader?preview_theme_id=178399019384&mwqa=010a2b_diag_20260625`.

Verificacion:

- Assets del tema auxiliar `/t/46`: `VERIFICADO Y CORRECTO`.
- `#external-width`: 1 elemento.
- `#external-height`: 1 elemento.
- `#width`: 1 elemento.
- `#height`: 1 elemento.
- `html lang`: `es`.
- Titulo: `Papel pintado y mural personalizado | MatchWalls`.

Prueba de cambio:

- Anchura externa: `402`.
- Altura externa: `302`.
- Anchura interna despues del cambio: `402`.
- Altura interna despues del cambio: `302`.
- Superficie calculada: `4.02m x 3.02m = 12.14 m²`.
- `window.dataLayer`: no creado.
- Eventos `input_mural_outside`: 0.
- Errores de consola: 0.

Estado: `INCORRECTO`.

## 6. Hallazgo tecnico

El HTML renderizado del preview contiene:

- 1 script con la cadena `input_mural_outside`, procedente del header.
- 1 script con los listeners reales de `externalWidthInput` y `externalHeightInput`, procedente de `external-selectors.liquid`.

El snippet `external-selectors.liquid` es el que recibe los eventos reales de los campos, porque al modificar anchura/altura actualiza:

- los inputs internos;
- la superficie calculada;
- el estado del personalizador.

El tracking de `input_mural_outside` sigue viviendo en `snippets/srolling_bar_menu.liquid`, que es un snippet global del header y no es el propietario funcional de los campos de medida.

## 7. Diagnostico final

`INCORRECTO`

La deuda de tracking dinamico sigue pendiente. El sublote `010A2` fallo porque intento resolver el evento desde `srolling_bar_menu.liquid`. La evidencia actual indica que el punto correcto de intervencion es `snippets/external-selectors.liquid`, donde ya existen los listeners fiables de anchura y altura.

## 8. Acciones realizadas

- Lectura de registros.
- Lectura Shopify Admin GraphQL validada.
- Prueba funcional en preview del auxiliar.
- Inspeccion de scripts renderizados.
- Ninguna mutacion Shopify.
- Ninguna publicacion.
- Ningun cambio en MAIN.

## 9. Siguiente paso recomendado

Crear y aprobar el sublote:

`MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B`

Objetivo:

- mover el evento `input_mural_outside` al snippet propietario de los campos;
- limpiar el tracking muerto del header para evitar dobles eventos;
- mantener `collection_submenu_click` intacto;
- ejecutar prueba critica antes de cualquier matriz completa.
