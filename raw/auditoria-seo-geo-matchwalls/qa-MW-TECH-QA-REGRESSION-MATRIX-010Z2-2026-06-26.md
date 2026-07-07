# QA - MW-TECH-QA-REGRESSION-MATRIX-010Z2

Fecha: 2026-06-26 21:10:31 +02:00

## Estado

`VERIFICADO Y CORRECTO` dentro del alcance compacto de regresión 010Z2.

No equivale a la matriz completa de 170 pruebas ni autoriza publicación. Es una verificación quirúrgica posterior a los lotes 010A-010C5 para confirmar que las correcciones recientes no rompen páginas críticas antes de continuar.

## Alcance

Tipo de lote: diagnóstico y QA de solo lectura.

No se modificó Shopify. No se publicó, duplicó, renombró ni eliminó ningún tema. No se cambiaron productos, precios, variantes, inventario, handles, redirecciones, canonicals, hreflang, GA4, GTM, Merchant Center ni apps.

## Estado real comprobado

- MAIN: `gid://shopify/OnlineStoreTheme/178396463480`, rol `MAIN`, prefijo de assets `/t/45`.
- QA: `gid://shopify/OnlineStoreTheme/178399019384`, rol `UNPUBLISHED`, prefijo de assets `/t/46`.
- Tema QA: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- `processing=false`, `processingFailed=false` en MAIN y QA.
- En las URLs públicas probadas de QA se cargaron assets `/t/46` y no se detectaron assets `/t/45`.

## Archivos clave confirmados antes de la regresión

QA `178399019384`:

- `assets/customizer.js`: MD5 `6684ed205824c8ba660bd4c67a5e26fc`, size `40832`.
- `assets/theme.css`: MD5 `b86a0e260263eed6a2586a3e7bca8e05`, size `242427`.
- `sections/collection-logo-list.liquid`: MD5 `e246746230f64c88b529db9aa370f3e2`, size `5937`.
- `sections/related-products.liquid`: MD5 `d8822a8c73cee73d61744c0b68b7a375`, size `10705`.
- `snippets/external-selectors.liquid`: MD5 `95266feda1603e9c9ef028f0dae74c6f`, size `11109`.
- `snippets/product-customizer.liquid`: MD5 `d5a74ccb15b645eeb79e8c52f7c5a4ac`, size `49230`.
- `snippets/srolling_bar_menu.liquid`: MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`, size `8539`.
- `snippets/variant-picker.liquid`: MD5 `44af7568d1ddeb65f5fabe7b782c7a05`, size `14968`.

MAIN `178396463480` conservado como referencia de rollback:

- `snippets/variant-picker.liquid`: MD5 `48ef3d83e49275ccea7f044c1b56d2d8`, size `14811`.
- `sections/related-products.liquid`: MD5 `d8822a8c73cee73d61744c0b68b7a375`, size `10705`.

## Matriz compacta ejecutada

Todas las URLs se probaron en preview del tema QA `178399019384`.

| Prueba | Viewport | H1 / señal principal | Canonical | hreflang | Assets QA | Assets MAIN | Overflow real | Consola |
| --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| Home ES | 390x900 | `Papeles pintados para paredes y murales` | `/` | 8 | 7 | 0 | 0 | 0 |
| Home ES | 1440x1000 | `Papeles pintados para paredes y murales` | `/` | 8 | 7 | 0 | 0 | 0 |
| Cart ES | 390x900 | sin H1 detectado | `/cart` | 8 | 7 | 0 | 0 | 0 |
| Colección ofertas ES | 390x900 | `Ofertas` | `/collections/ofertas` | 8 | 7 | 0 | 0 | 0 |
| Producto estándar ES | 390x900 | `Líneas Nórdicas Verde` | `/products/lineas-noridcas-verde` | 8 | 11 | 0 | 0 | 0 |
| Uploader ES | 390x900 | `Tu Mural Personalizado` | `/products/custom-file-uploader` | 8 | 11 | 0 | 0 | 0 |
| Uploader EN | 390x900 | `Your custom mural` | `/en/products/custom-file-uploader` | 8 | 11 | 0 | 0 | 0 |
| Uploader FR | 390x900 | `Votre fresque personnalisée` | `/fr/products/telechargeur-de-fichiers-personnalise` | 8 | 11 | 0 | 0 | 0 |
| Uploader FR | 375x900 | `Votre fresque personnalisée` | `/fr/products/telechargeur-de-fichiers-personnalise` | 8 | 11 | 0 | 0 | 0 |
| Uploader DE | 390x900 | `Ihr individuelles Wandgemälde` | `/de/products/benutzerdefinierte-datei-uploader` | 8 | 11 | 0 | 0 | 0 |
| Uploader NL | 390x900 | `Uw aangepaste muurschildering` | `/nl/products/aangepaste-bestandsbelaster` | 8 | 11 | 0 | 0 | 0 |
| Uploader NL | 375x900 | `Uw aangepaste muurschildering` | `/nl/products/aangepaste-bestandsbelaster` | 8 | 11 | 0 | 0 | 0 |
| Uploader FR desktop | 1440x1000 | `Votre fresque personnalisée` | `/fr/products/telechargeur-de-fichiers-personnalise` | 8 | 11 | 0 | 0 | 0 |
| Uploader NL desktop | 1440x1000 | `Uw aangepaste muurschildering` | `/nl/products/aangepaste-bestandsbelaster` | 8 | 11 | 0 | 0 | 0 |

Nota técnica: el navegador interno reportó `clientWidth` 15 px menor que `innerWidth` por la barra vertical del entorno de prueba. Se tomó como overflow real el exceso frente a `window.innerWidth`; resultado `0` en todas las pruebas.

## Verificaciones específicas por deuda técnica

### 010A / 010A3 / 010A4 - guards JavaScript

Estado: `VERIFICADO Y CORRECTO` en la regresión pública medida.

- No se capturaron errores de consola en home, cart, colección, producto estándar ni uploader multilingüe.
- El uploader mantuvo inputs externos e internos disponibles donde aplica.
- No se reprodujo error público asociado a `addEventListener` sobre elementos ausentes.

### 010A2D - tracking directo de medidas

Estado: `CORREGIDO Y VERIFICADO`.

Prueba controlada en QA:

- URL: `/products/custom-file-uploader?preview_theme_id=178399019384&mwqa=010a2d`.
- Viewport: `390x900`.
- Inputs encontrados: `#external-width=1`, `#external-height=1`.
- Tras introducir `421` y `221`:
  - `#external-width=421`.
  - `#external-height=221`.
  - `#width=421`.
  - `#height=221`.
  - Marcador QA `data-mw010a2d-count=2`.
  - Último evento registrado: `{"event":"input_mural_outside","dimension":"height","value":"221","gtm.uniqueEventId":15}`.
- Consola: 0 errores.

Lectura directa de `window.dataLayer` desde el entorno de inspección: `NO ACCESIBLE`. El marcador QA incorporado en el propio código sí confirmó la ejecución del evento.

### 010B - SyntaxError neerlandés

Estado: `VERIFICADO Y CORRECTO` en NL uploader.

- NL mobile 390 y 375: 0 errores de consola.
- NL desktop 1440: 0 errores de consola.
- H1 NL visible: `Uw aangepaste muurschildering`.

### 010C2 / 010C5 - overflow móvil FR/NL

Estado: `CORREGIDO Y VERIFICADO`.

- FR mobile 390: overflow real `0`.
- FR mobile 375: overflow real `0`.
- NL mobile 390: overflow real `0`.
- NL mobile 375: overflow real `0`.
- En mobile, `.product-info__variant-picker .block-swatch[data-tooltip]::after` queda con `display:none` y `content:none`.
- En desktop FR/NL, el tooltip de swatches se conserva con `display:block`.

### 010C3 - related products

Estado: `VERIFICADO Y CORRECTO` en la regresión actual.

- No se detectó overflow real de documento en producto estándar ni uploader.
- `sections/related-products.liquid` no cambió en QA respecto a MAIN: MD5 `d8822a8c73cee73d61744c0b68b7a375`.
- La hipótesis de related-products como causa raíz queda descartada por 010C4 y 010Z2.

### 010D - CSS rastreable en home

Estado: `CORREGIDO Y VERIFICADO` en home QA ES.

- Home mobile y desktop: `cssLeak=false`.
- H1 home visible: `Papeles pintados para paredes y murales`.
- Canonical home correcto: `https://www.matchwalls.com/`.
- 8 alternates hreflang detectados.

## Observaciones no bloqueantes

- Cart ES no mostró H1 en esta medición. Estado: `VERIFICADO PERO MEJORABLE`. No se trata como bloqueo para este lote porque el carrito no es una URL prioritaria de captación orgánica, pero puede revisarse en accesibilidad/UX.
- Los elementos de `announcement-bar__item` aparecen con posiciones negativas por el marquee/carrusel de anuncios. Estado: `VERIFICADO Y CORRECTO` para overflow, porque no generan anchura horizontal real.
- Algunas traducciones visibles en tooltips FR/NL siguen siendo mejorables editorialmente, pero no forman parte del lote técnico 010Z2.

## Cobertura no ejecutada

Estado: `INCOMPLETO` respecto a una regresión total.

No se ejecutaron las 170 pruebas completas. No se verificaron checkout real, subida de archivo con fichero real, pago, creación de pedido, apps externas con datos reales, Search Console, GA4, GTM, Merchant Center, Bing Webmaster Tools ni CrUX.

## Conclusión

`VERIFICADO Y CORRECTO` para seguir trabajando sobre QA `178399019384`.

No hay evidencia en esta matriz compacta de regresión crítica introducida por 010A-010C5. El siguiente paso recomendado es cerrar la deuda técnica restante con lotes pequeños o pasar al bloque de indexabilidad, manteniendo el mismo protocolo de aprobación.
