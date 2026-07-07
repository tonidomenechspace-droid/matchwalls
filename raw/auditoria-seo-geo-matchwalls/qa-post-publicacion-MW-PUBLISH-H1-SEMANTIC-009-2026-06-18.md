# QA post-publicación — MW-PUBLISH-H1-SEMANTIC-009

Fecha de cierre: 18 de junio de 2026, 19:42 CEST.

Estado final: `CORREGIDO Y VERIFICADO`.

## Publicación

`VERIFICADO Y CORRECTO`

- Tema publicado: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- ID: `gid://shopify/OnlineStoreTheme/178396463480`.
- Rol posterior: `MAIN`.
- Prefijo servido: `/t/45`.
- `processing: false`; `processingFailed: false`.
- Tema anterior conservado: `gid://shopify/OnlineStoreTheme/178383749496`.
- Rol del tema anterior: `UNPUBLISHED`.
- No fue necesaria la reversión.

## Resultado de las 170 comprobaciones

`CORREGIDO Y VERIFICADO`

- Escritorio: 85/85 correctas.
- Móvil, viewport `390 × 844`: 85/85 correctas.
- Cobertura: 17 páginas × ES/EN/FR/DE/NL × escritorio/móvil.
- En 170/170:
  - tema servido `/t/45`;
  - un único H1 no vacío;
  - canonical self;
  - hreflang ES/EN/FR/DE/NL;
  - `html lang` correcto;
  - ausencia de `noindex` accidental;
  - contenido principal no vacío;
  - ausencia de página 404 o error Shopify.

Matriz: `matriz-post-publicacion-MW-PUBLISH-H1-SEMANTIC-009-2026-06-18.csv`.

## Smoke test global

`VERIFICADO Y CORRECTO`

Home, producto, colección y carrito se comprobaron en escritorio y móvil:

- todos sirvieron `/t/45`;
- contenido visible no vacío;
- sin página 404;
- home, producto y colección conservaron H1 visible;
- el carrito no muestra H1, condición fuera del alcance del lote y no atribuida
  a la publicación H1.

Dos cargas iniciales de escritorio agotaron el tiempo de navegación; la
repetición posterior de home y producto fue correcta. No se contabilizaron como
válidas hasta completar la lectura pública.

## Incidencias preexistentes

`VERIFICADO PERO MEJORABLE`

### Overflow móvil

- FR: 17/17 páginas, `scrollWidth 408` frente a `clientWidth 375`.
- NL: 17/17 páginas, normalmente `381/375`; `onze-producten`, `405/375`.
- Total: 34/85 contextos móviles.
- Coincide con el patrón documentado antes de publicar; no es una regresión del
  lote 009.

### Consola JavaScript

- `Cannot read properties of null (reading 'addEventListener')` en las páginas
  revisadas y rutas globales.
- `SyntaxError: Unexpected token ','` en `Nuestros productos` y sus versiones
  ES/EN/FR/DE/NL.
- `this.convertToInches is not a function` en el customizador de producto.
- `customizer.js` no figuraba entre las diferencias MAIN/candidato del preflight;
  el error del customizador no es atribuible al lote H1.
- El error `addEventListener` y el `SyntaxError` ya se habían reproducido en el
  MAIN anterior durante el QA aislado. Se trasladan a los sublotes técnicos.

## Límite de temas

`VERIFICADO PERO MEJORABLE`

Shopify muestra `Theme limit reached`: existen 20 temas. No se eliminó ninguno.
Antes de crear otro tema auxiliar se requiere auditar los 20 temas y presentar
un lote de limpieza con IDs, respaldo y aprobación exacta.

## Acciones no realizadas

- No se editaron archivos durante la publicación.
- No se cambiaron contenido, traducciones, handles, canonicals, hreflang,
  redirecciones, productos, colecciones, precios, inventario, variantes,
  imágenes, App Embeds ni LangShop.
- No se eliminó ningún tema.

## Resultado

El lote `MW-PUBLISH-H1-SEMANTIC-009` queda `CORREGIDO Y VERIFICADO`. La deuda
técnica observada queda fuera de este lote y requiere propuestas separadas.
