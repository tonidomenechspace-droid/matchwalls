# Diagnóstico — MW-TECH-JS-ADD-EVENT-LISTENER-010A

Fecha: 2026-06-18.

Estado: `INCORRECTO`.

## Hallazgo reproducido

La consola pública registra de forma global:

`TypeError: Cannot read properties of null (reading 'addEventListener')`

Se reprodujo en home, producto, colección y carrito del MAIN `/t/45`. La QA de
170 pruebas del lote 009 ya lo había observado en los cinco idiomas
prioritarios. La repetición actual volvió a confirmarlo en ES, DE y NL. Las
cargas directas EN y FR quedaron incompletas durante esta repetición y no se
usan como nueva evidencia; se conserva la evidencia válida de la QA anterior.

## Origen exacto

- MAIN: `gid://shopify/OnlineStoreTheme/178396463480`.
- Archivo: `snippets/srolling_bar_menu.liquid`.
- MD5 actual en Shopify: `c254cf711a7706dc21ece2f2ad31acea`.
- Copia local: 8.581 bytes y el mismo MD5.
- Inclusión global: `sections/header.liquid`, línea local 381.
- Selectores: líneas locales 243–244.
- Listeners sin comprobación nula: líneas locales 283–284.

El encabezado carga globalmente el snippet. Este busca `#external-width` y
`#external-height`, elementos propios del personalizador que no existen en la
mayoría de páginas. Después llama directamente a `addEventListener` sobre
valores `null`, provocando la excepción.

## Clasificación

`VERIFICADO Y CORRECTO`

- Causa técnica identificada por consola, HTML renderizado y archivo real de
  Shopify.
- La copia local coincide exactamente con el archivo remoto por MD5.

`VERIFICADO PERO MEJORABLE`

- El mismo recorrido detecta otro error independiente en `customizer.js`:
  `this.convertToInches is not a function`. Queda fuera de 010A para evitar
  mezclar causas y tendrá su propio diagnóstico/lote.

## Corrección mínima recomendada

Registrar cada listener únicamente si existe su campo. Con ambos campos
presentes, el comportamiento y los eventos de `dataLayer` se mantienen. Si no
existen, el código deja de lanzar la excepción.

No se recomienda ocultar el error de forma global ni modificar librerías de
terceros.

