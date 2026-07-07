# QA MW-TECH-MOBILE-OVERFLOW-SWATCH-TOOLTIP-010C5 - 2026-06-26

## Estado

`CORREGIDO Y VERIFICADO`

## Aprobación y alcance

- Aprobación exacta recibida: `APROBADO LOTE MW-TECH-MOBILE-OVERFLOW-SWATCH-TOOLTIP-010C5`.
- Tema afectado: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre tema: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol: `UNPUBLISHED`.
- Prefijo QA: `/t/46`.
- Archivo modificado: `snippets/variant-picker.liquid`.
- MAIN verificado y no modificado: `gid://shopify/OnlineStoreTheme/178396463480`, rol `MAIN`, prefijo `/t/45`.
- No se publicó ningún tema.
- No se modificaron productos, precios, variantes, inventario, handles, redirecciones, canonicals, hreflang, GA4, GTM, Merchant Center ni apps.

## Motivo

El diagnóstico `MW-TECH-MOBILE-OVERFLOW-VARIANT-SWATCH-DIAG-010C4` demostró que el overflow móvil FR/NL no procedía de `related-products`, sino del pseudo-elemento:

`.block-swatch[data-tooltip]::after`

El tooltip se renderizaba desde `snippets/variant-picker.liquid` con `content: attr(data-tooltip)`, `position:absolute` y `white-space: nowrap`. Aunque estaba invisible por `opacity:0` y `visibility:hidden`, su caja seguía computando en el `scrollWidth` móvil.

## Valores originales

| Archivo | Tema | MD5 original | Size original | Estado |
|---|---|---:|---:|---|
| `snippets/variant-picker.liquid` | QA `178399019384` | `48ef3d83e49275ccea7f044c1b56d2d8` | `14811` | `VERIFICADO Y CORRECTO` |
| `snippets/variant-picker.liquid` | MAIN `178396463480` | `48ef3d83e49275ccea7f044c1b56d2d8` | `14811` | `VERIFICADO Y CORRECTO` |
| `assets/theme.css` | QA `178399019384` | `b86a0e260263eed6a2586a3e7bca8e05` | `242427` | Solo lectura |
| `sections/related-products.liquid` | QA `178399019384` | `d8822a8c73cee73d61744c0b68b7a375` | `10705` | Solo lectura |

## Cambio aplicado

En `snippets/variant-picker.liquid`, dentro del bloque `<style>` existente, se añadió una regla móvil acotada:

```css
@media screen and (max-width: 699px) {
  .product-info__variant-picker .block-swatch[data-tooltip]::after {
    content: none;
    display: none;
  }
}
```

La regla afecta únicamente al pseudo-tooltip de los swatches dentro de `.product-info__variant-picker` en móvil.

No se modificó el HTML visible, ni precios, ni variantes, ni lógica Liquid de selección.

## Ejecución Shopify

- Mutación usada: `themeFilesUpsert`.
- Tipo de cuerpo: `BASE64`.
- Resultado: `userErrors=[]`.
- Archivo actualizado: `snippets/variant-picker.liquid`.
- Readback Shopify:
  - MD5 nuevo: `44af7568d1ddeb65f5fabe7b782c7a05`.
  - Size nuevo: `14968`.
  - `processing=false`.
  - `processingFailed=false`.

## Validación técnica

`VERIFICADO PERO MEJORABLE`

- La operación GraphQL fue validada contra schema Admin antes de ejecutar.
- La búsqueda Shopify Liquid devolvió referencia general sobre estilos en snippets.
- El validador local `shopify-liquid/scripts/validate.mjs` no pudo completarse por dependencia ausente del runtime: `@shopify/theme-check-common`. No se clasifica como error del código, sino como limitación de herramienta local.
- Shopify aceptó el archivo con `userErrors=[]`.
- Readback confirmó MD5 y tamaño esperados.
- QA público confirmó que el CSS se aplica y corrige la causa.

## QA público crítico

Todas las pruebas se ejecutaron contra el tema QA `/t/46`; assets MAIN `/t/45` = 0.

| Idioma | Viewport | H1 | `docClientWidth` | `docScrollWidth` | Overflow | Assets `/t/46` | Resultado |
|---|---:|---|---:|---:|---:|---:|---|
| FR | 390 | `Votre Fresque Personnalisée` | 375 | 375 | 0 | 11 | `CORREGIDO Y VERIFICADO` |
| FR | 375 | `Votre Fresque Personnalisée` | 360 | 360 | 0 | 11 | `CORREGIDO Y VERIFICADO` |
| NL | 390 | `Uw Aangepaste Muurschildering` | 375 | 375 | 0 | 11 | `CORREGIDO Y VERIFICADO` |
| NL | 375 | `Uw Aangepaste Muurschildering` | 360 | 360 | 0 | 11 | `CORREGIDO Y VERIFICADO` |

## QA de nodos causales

| Nodo | FR 390 | FR 375 | NL 390 | NL 375 | Resultado |
|---|---:|---:|---:|---:|---|
| `main#main` ownScroll | 0 | 0 | 0 | 0 | `CORREGIDO Y VERIFICADO` |
| `.product-info__variant-picker` ownScroll | 0 | 0 | 0 | 0 | `CORREGIDO Y VERIFICADO` |
| `variant-picker#div-to-duplicate` ownScroll | 0 | 0 | 0 | 0 | `CORREGIDO Y VERIFICADO` |
| `.variant-picker__option-values` ownScroll | 0 | 0 | 0 | 0 | `CORREGIDO Y VERIFICADO` |
| `.shopify-section--product-recommendations` ownScroll | 0 | 0 | 0 | 0 | `VERIFICADO Y CORRECTO` |

El carrusel de relacionados mantiene scroll interno:

- FR 390: `relatedCarousel clientWidth=375`, `scrollWidth=1523`, `overflow-x:auto`.
- FR 375: `relatedCarousel clientWidth=360`, `scrollWidth=1469`, `overflow-x:auto`.
- NL 390: `relatedCarousel clientWidth=375`, `scrollWidth=1523`, `overflow-x:auto`.
- NL 375: `relatedCarousel clientWidth=360`, `scrollWidth=1469`, `overflow-x:auto`.

## QA del pseudo-tooltip

En móvil, el pseudo-elemento queda neutralizado:

| Idioma | Viewport | Swatch | `::after content` | `::after display` |
|---|---:|---|---|---|
| FR | 390/375 | `NON TISSÉ` | `none` | `none` |
| FR | 390/375 | `PELER ET BÂTON` | `none` | `none` |
| NL | 390/375 | `NIET GEWEVEN` | `none` | `none` |
| NL | 390/375 | `SCHIL & STOK` | `none` | `none` |

## Controles ES/EN/DE móvil

| Idioma | URL | Viewport | H1 | `docScrollWidth` | Overflow | Assets `/t/46` | Resultado |
|---|---|---:|---|---:|---:|---:|---|
| ES | `/products/custom-file-uploader` | 390 | `Tu Mural Personalizado` | 375 | 0 | 11 | `CORREGIDO Y VERIFICADO` |
| EN | `/en/products/custom-file-uploader` | 390 | `Your Custom Mural` | 375 | 0 | 11 | `CORREGIDO Y VERIFICADO` |
| DE | `/de/products/benutzerdefinierte-datei-uploader` | 390 | `Ihr Individuelles Wandgemälde` | 375 | 0 | 11 | `CORREGIDO Y VERIFICADO` |

## Control desktop

| Idioma | Viewport | `docScrollWidth` | Overflow | Tooltip desktop |
|---|---:|---:|---:|---|
| FR | 1440 | 1425 | 0 | `::after display=block`, contenido conservado |
| NL | 1440 | 1425 | 0 | `::after display=block`, contenido conservado |

## Consola

`VERIFICADO Y CORRECTO`

- Errores capturados en QA durante la verificación: 0.

## Incidencias y limitaciones

- El tooltip hover de swatches queda desactivado en móvil dentro de `.product-info__variant-picker`. Se considera aceptable porque hover no es una interacción fiable en móvil y era la causa del overflow.
- Desktop conserva el tooltip.
- No se ha ejecutado una matriz completa de 170 pruebas en este cierre; las pruebas realizadas cubren la incidencia crítica y controles de idioma/desktop relacionados.

## Reversión

Restaurar `snippets/variant-picker.liquid` del tema QA `178399019384` al MD5 original `48ef3d83e49275ccea7f044c1b56d2d8`, size `14811`.

Fuente de rollback verificada:

- MAIN `gid://shopify/OnlineStoreTheme/178396463480`.
- Archivo `snippets/variant-picker.liquid`.
- MD5 `48ef3d83e49275ccea7f044c1b56d2d8`.
- Size `14811`.

Método: `themeFilesUpsert` con el contenido original o copia controlada desde MAIN al tema QA.

## Estado final

`CORREGIDO Y VERIFICADO`

El overflow móvil del uploader FR/NL detectado tras 010C3 queda corregido en el tema QA `178399019384`. No publicar todavía sin la matriz de regresión/paso de publicación correspondiente.
