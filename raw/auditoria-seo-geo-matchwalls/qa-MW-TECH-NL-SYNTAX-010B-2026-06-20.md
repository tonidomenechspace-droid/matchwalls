# QA — MW-TECH-NL-SYNTAX-010B

Fecha de cierre: 2026-06-20 11:29:21 +02:00.

Estado: `CORREGIDO Y VERIFICADO`.

## Ejecución almacenada

- Tema auxiliar `178399019384`, `/t/46`, `UNPUBLISHED`.
- Archivo: `snippets/ultimate-datalayer.liquid`.
- MD5 anterior: `449db7505f61b2f81c835cc32669c37c`; 57168 bytes.
- MD5 final: `792a7f2c37022db342e1d7a82a8d3679`; 57177 bytes.
- Dos condiciones `if` y una `unless` cambiadas de coincidencia parcial a
  `request.page_type == 'product'`.
- Lectura posterior: tres condiciones estrictas, cero condiciones amplias y
  cero `userErrors`.
- MAIN `178396463480` y reversión `178383749496` permanecen con el MD5 original.

## QA específica

`CORREGIDO Y VERIFICADO`

- Páginas «Nuestros productos» ES/EN/FR/DE/NL × escritorio/móvil: 10/10.
- Producto Floral Symphony ES/EN/FR/DE/NL × escritorio/móvil: 10/10.
- Total: 20/20.
- `SyntaxError: Unexpected token ','`: 0.
- `variant_id: ,`: 0.
- En producto: `variant_id` numérico, Product/Offer, formulario de compra,
  canonical propio, cinco hreflang y H1 único.
- La primera carga del producto EN mostró un fallo transitorio de descarga; la
  repetición aislada fue correcta y la prueba móvil también fue correcta.

## Regresión completa

`CORREGIDO Y VERIFICADO`

- Matriz base: 85 URLs verificadas de ES/EN/FR/DE/NL.
- Escritorio: 85/85.
- Móvil: 85/85.
- Total: 170/170.
- Criterios: H1 exacto y único, canonical propio, cinco hreflang prioritarios,
  idioma HTML, ausencia de `noindex`, contenido, recursos `/t/46` y ausencia de
  errores críticos de consola.
- Errores `SyntaxError`, `addEventListener`, `convertToInches`, `variant_id` o
  `Ultimate_Shopify_DataLayer`: 0.

## Deudas separadas

### Tracking dinámico

`INCORRECTO`

- El evento `view_item` no aparece en `window.dataLayer` ni en el auxiliar ni
  en MAIN para el mismo producto.
- No existe diferencia atribuible a 010B.
- Permanece dentro de la deuda de tracking 010A2, que fue revertida al fallar su
  prueba crítica.

### Desbordamiento móvil FR/NL

`VERIFICADO PERO MEJORABLE`

- Escritorio: 0/85 URLs con overflow.
- Móvil: 34/85, exactamente 17 FR y 17 NL.
- Coincide con la línea base previa y no aumentó con 010B.
- Se mantiene para `MW-TECH-MOBILE-OVERFLOW-FR-NL-010C`.

### Validador Liquid empaquetado

`NO ACCESIBLE`

- No pudo ejecutarse por la dependencia ausente
  `@shopify/theme-check-common`.
- Esta limitación no se ocultó ni se interpretó como validación superada.
- El código fue contrastado con la referencia oficial de `request.page_type`,
  aceptado por Shopify, leído de nuevo y validado mediante 190 renders reales.

## Reversión

Restaurar las tres condiciones originales y confirmar MD5
`449db7505f61b2f81c835cc32669c37c`, o descartar el tema auxiliar. No se ha
publicado ni modificado MAIN.
