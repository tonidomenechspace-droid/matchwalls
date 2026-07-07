# QA MW-TECH-QA-REGRESSION-MATRIX-010Z - 2026-06-25

## Estado final

`VERIFICADO PERO MEJORABLE`

Matriz compacta de regresión de solo lectura sobre el tema auxiliar `178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.

No se modificó Shopify. No se publicó ningún tema. No se modificó MAIN.

## Alcance

- MAIN real comprobado: `gid://shopify/OnlineStoreTheme/178396463480`, rol `MAIN`, prefijo `/t/45`.
- Tema QA comprobado: `gid://shopify/OnlineStoreTheme/178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.
- URLs públicas probadas con `preview_theme_id=178399019384`.
- Idiomas prioritarios probados en uploader: ES, EN, FR, DE, NL.
- Dispositivos: desktop y móvil 390 px; comprobación adicional FR/NL a 375 px.

## Estado real Shopify verificado antes de QA

### MAIN `178396463480`

- Nombre: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- Rol: `MAIN`.
- `processing=false`.
- `processingFailed=false`.
- `snippets/external-selectors.liquid`: MD5 `8a9c233bca52da58ce59fffc3aee8359`, size `10199`.
- `snippets/srolling_bar_menu.liquid`: MD5 `c254cf711a7706dc21ece2f2ad31acea`, size `8581`.
- `snippets/product-customizer.liquid`: MD5 `3878a24a9bb6cb134247ac6aff707a58`, size `49228`.
- `assets/customizer.js`: MD5 `2a26be9d6af37a992526274df431deaa`, size `40768`.
- `assets/theme.css`: MD5 `89f4729809a0eaac75a764e0fc41888e`, size `241968`.
- `sections/collection-logo-list.liquid`: MD5 `44d02156951a46f0147f3ee3de61f38e`, size `6780`.

### QA `178399019384`

- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol: `UNPUBLISHED`.
- `processing=false`.
- `processingFailed=false`.
- `snippets/external-selectors.liquid`: MD5 `95266feda1603e9c9ef028f0dae74c6f`, size `11109`.
- `snippets/srolling_bar_menu.liquid`: MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`, size `8539`.
- `snippets/product-customizer.liquid`: MD5 `d5a74ccb15b645eeb79e8c52f7c5a4ac`, size `49230`.
- `assets/customizer.js`: MD5 `6684ed205824c8ba660bd4c67a5e26fc`, size `40832`.
- `assets/theme.css`: MD5 `b86a0e260263eed6a2586a3e7bca8e05`, size `242427`.
- `sections/collection-logo-list.liquid`: MD5 `e246746230f64c88b529db9aa370f3e2`, size `5937`.

## Resultados correctos

`VERIFICADO Y CORRECTO`

- Home ES desktop: assets `/t/46` = 8, assets `/t/45` = 0, H1 `Papeles pintados para paredes y murales`, canonical `https://www.matchwalls.com/`, hreflang 8, consola 0 errores, fuga CSS visible de home `false`.
- Carrito ES desktop: assets `/t/46` = 7, assets `/t/45` = 0, canonical `https://www.matchwalls.com/cart`, hreflang 8, consola 0 errores.
- Colección `/collections/ofertas`: assets `/t/46` = 7, assets `/t/45` = 0, H1 `Ofertas`, canonical correcto, hreflang 8, consola 0 errores.
- Producto estándar `lineas-noridcas-verde`: H1 `Líneas Nórdicas Verde`, inputs presentes, prueba `420 x 320`, sincronización correcta, evento QA `input_mural_outside` count `2`, último evento `height=320`, consola 0 errores.

## Uploader multidioma desktop

`VERIFICADO Y CORRECTO`

| Idioma | URL final | H1 | Medida probada | Sincronización | Evento QA | Consola | Estado |
|---|---|---|---:|---|---|---:|---|
| ES | `/products/custom-file-uploader?mwqa=010a2d` | `Tu Mural Personalizado` | `415 x 315` | OK | count `2`, `height=315` | 0 | `VERIFICADO Y CORRECTO` |
| EN | `/en/products/custom-file-uploader?mwqa=010a2d` | `Your custom mural` | `416 x 316` | OK | count `2`, `height=316` | 0 | `VERIFICADO Y CORRECTO` |
| FR | `/fr/products/telechargeur-de-fichiers-personnalise?mwqa=010a2d` | `Votre fresque personnalisée` | `417 x 317` | OK | count `2`, `height=317` | 0 | `VERIFICADO Y CORRECTO` |
| DE | `/de/products/benutzerdefinierte-datei-uploader?mwqa=010a2d` | `Ihr individuelles Wandgemälde` | `418 x 318` | OK | count `2`, `height=318` | 0 | `VERIFICADO Y CORRECTO` |
| NL | `/nl/products/aangepaste-bestandsbelaster?mwqa=010a2d` | `Uw aangepaste muurschildering` | `419 x 319` | OK | count `2`, `height=319` | 0 | `VERIFICADO Y CORRECTO` |

## Mobile

### Correcto

- Home ES móvil 390: assets `/t/46`, 0 assets `/t/45`, H1 correcto, canonical correcto, hreflang 8, consola 0 errores, fuga CSS visible de home `false`.
- Uploader FR/NL móvil 390: inputs presentes, sincronización de medidas correcta, evento QA `input_mural_outside` correcto, consola 0 errores.

### Incidencia detectada

`INCORRECTO`

Overflow horizontal en uploader móvil FR/NL:

| URL | Viewport | ScrollWidth | Overflow |
|---|---:|---:|---:|
| `/fr/products/telechargeur-de-fichiers-personnalise?mwqa=010a2d` | 390 | 447 | +57 px |
| `/nl/products/aangepaste-bestandsbelaster?mwqa=010a2d` | 390 | 427 | +37 px |
| `/fr/products/telechargeur-de-fichiers-personnalise?mwqa=010a2d` | 375 | 447 | +72 px |
| `/nl/products/aangepaste-bestandsbelaster?mwqa=010a2d` | 375 | 427 | +52 px |

## Diagnóstico de causa probable

`VERIFICADO PERO MEJORABLE`

La incidencia móvil no corresponde al bloque legal corregido en `MW-TECH-MOBILE-OVERFLOW-LEGAL-FLEX-010C2`.

Elementos implicados:

- Sección: `shopify-section--product-recommendations`.
- ID observado: `shopify-section-template--24951169024376__related-products`.
- Componente: `scroll-carousel`.
- ID observado: `scroll-area-template--24951169024376__related-products`.
- Elemento interno: `REVEAL-ITEMS`.
- Ancho observado en móvil: `1483 px`.
- Archivo leído en Shopify: `sections/related-products.liquid`.
- Checksum actual QA: MD5 `d8822a8c73cee73d61744c0b68b7a375`, size `10705`.
- `assets/theme.css` actual QA: MD5 `b86a0e260263eed6a2586a3e7bca8e05`, size `242427`.

La sección `related-products.liquid` genera un carrusel de productos relacionados con `scroll-carousel`, `class="scroll-area bleed ..."`, `reveal-items selector=".product-list > *"` y `product-list class="product-list"`.

## Conclusión

`VERIFICADO PERO MEJORABLE`

La deuda técnica JavaScript crítica queda estable en esta matriz compacta: sin errores de consola en las URLs probadas, tracking `input_mural_outside` correcto y tema QA cargando assets `/t/46`.

Pero no se recomienda publicar ni pasar a matriz final 170/170 sin tratar antes el overflow móvil de productos relacionados en uploader FR/NL.

## Próximo lote recomendado

`MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3`

Objetivo: corregir de forma acotada el overflow móvil generado por `related-products` / `scroll-carousel` en producto uploader FR/NL, verificando que no rompe el carrusel ni desktop.