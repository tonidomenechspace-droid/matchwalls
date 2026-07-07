# QA — MW-TECH-MOBILE-OVERFLOW-LEGAL-FLEX-010C2

Fecha: 2026-06-25.

Estado final: `CORREGIDO Y VERIFICADO`.

## Alcance ejecutado

- Aprobación exacta recibida: `APROBADO LOTE MW-TECH-MOBILE-OVERFLOW-LEGAL-FLEX-010C2`.
- Tema afectado: auxiliar `178399019384`, `/t/46`, `UNPUBLISHED`.
- Archivo afectado: `assets/theme.css`.
- MAIN `178396463480` no fue modificado ni publicado.
- Tema de reversión `178383749496` no fue modificado.
- No se modificaron URLs, handles, textos, traducciones, productos, precios, apps ni tracking.

## Verificación de archivo

`CORREGIDO Y VERIFICADO`

- MD5 auxiliar antes: `05810cc93feb785cc81aed10513a297a`.
- Tamaño auxiliar antes: `241969` bytes.
- MD5 auxiliar después: `b86a0e260263eed6a2586a3e7bca8e05`.
- Tamaño auxiliar después: `242427` bytes.
- Bloque 010C2 exacto presente: 1 aparición.
- Bloque fallido 010C `.custom-legal__item:last-child`: 0 apariciones.
- MAIN conserva MD5 `89f4729809a0eaac75a764e0fc41888e`.
- Reversión conserva MD5 `89f4729809a0eaac75a764e0fc41888e`.
- MAIN y reversión no contienen el bloque exacto 010C2.

## QA centinela

`CORREGIDO Y VERIFICADO`

Viewport 390 px:

- FR `https://www.matchwalls.com/fr/pages/tout-sur-nos-peintures-murales`: `clientWidth 375`, `scrollWidth 375`, overflow `0 px`.
- NL `https://www.matchwalls.com/nl/pages/onze-producten`: `clientWidth 375`, `scrollWidth 375`, overflow `0 px`.
- ES control `https://www.matchwalls.com/pages/papel-pintado-murales`: `clientWidth 375`, `scrollWidth 375`, overflow `0 px`.

Se verificó también:

- `.custom-legal__list`: `display:flex`, `flex-wrap:wrap`, `column-gap:24px`, `row-gap:8px`, `scrollWidth 335`.
- `.custom-legal__item`: `margin-right:0px`, `overflow-wrap:anywhere`.
- En NL productos: `.shopify-section--multi-column .section-header > div` con `min-width:0px` y `.collection-header` con `overflow-wrap:anywhere`.
- H1 exacto, canonical propio, hreflang prioritarios, `html lang` correcto, sin `noindex`, recursos `/t/46` y errores críticos: 0.

## QA ampliada

`CORREGIDO Y VERIFICADO`

- FR/NL a 390 px: 34/34 correctas; overflow máximo `0 px`.
- FR/NL a 375 px: 34/34 correctas; overflow máximo `0 px`.
- Controles ES/EN/DE a 375 px: 51/51 correctas; overflow máximo `0 px`.
- Matriz móvil total a 375 px: 85/85 correctas; overflow máximo `0 px`.
- Matriz desktop a 1440 px: 85/85 correctas; overflow máximo `0 px`.
- Total estándar verificado: 170/170.

Criterios comprobados en matriz:

- H1 único y exacto.
- Canonical propio.
- Hreflang prioritarios ES/EN/FR/DE/NL.
- `html lang` correcto.
- Sin `noindex`.
- Contenido visible suficiente.
- Recursos `/t/46` presentes.
- Sin errores críticos filtrados de consola para `SyntaxError`, `Unexpected token`, `convertToInches`, `addEventListener`, `variant_id` ni `Ultimate_Shopify_DataLayer`.

## Limitaciones

`NO ACCESIBLE`

- No se ejecutó Theme Check local; el criterio de salida de este lote se basó en checksum Shopify, CSS servido y QA pública de preview.
- El lote está verificado en tema auxiliar. No equivale a publicación en MAIN.

## Reversión

`VERIFICADO Y CORRECTO`

- Reversión exacta: retirar únicamente el bloque 010C2 añadido en `assets/theme.css`.
- Objetivo de reversión del auxiliar: volver al MD5 `05810cc93feb785cc81aed10513a297a`.
- Alternativa extrema: descartar el tema auxiliar `178399019384`.

## Estado final

`CORREGIDO Y VERIFICADO`

010C2 corrige el overflow móvil FR/NL verificado en el tema auxiliar `/t/46`, sin tocar MAIN ni publicar.
