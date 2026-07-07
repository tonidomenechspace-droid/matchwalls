# QA MW-TECH-MOBILE-OVERFLOW-VARIANT-SWATCH-DIAG-010C4 - 2026-06-26

## Estado

`VERIFICADO Y CORRECTO` como diagnóstico de causa.

La incidencia visual queda `INCOMPLETO` hasta ejecutar un lote de corrección posterior. No se ha modificado Shopify.

## Alcance

- Lote indicado por Daniel: `MW-TECH-MOBILE-OVERFLOW-VARIANT-SWATCH-DIAG-010C4`.
- Tipo: diagnóstico de solo lectura.
- Tema QA auditado: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre tema QA: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol: `UNPUBLISHED`.
- Prefijo público QA: `/t/46`.
- MAIN no modificado.
- No se publicaron temas.
- No se modificaron productos, precios, variantes, inventario, handles, canonicals, hreflang, redirecciones, GA4, GTM, Merchant Center ni apps.

## Estado Shopify verificado

Consulta Admin GraphQL de solo lectura:

| Recurso | Estado |
|---|---|
| Tema QA `178399019384` | `UNPUBLISHED`, `/t/46`, `processing=false`, `processingFailed=false` |
| `snippets/variant-picker.liquid` QA | MD5 `48ef3d83e49275ccea7f044c1b56d2d8`, size `14811`, updated `2026-06-18T18:30:47Z` |
| `snippets/option-value.liquid` QA | MD5 `f2fd22527bc9b48182911c0c54f23399`, size `17066`, updated `2026-06-18T18:30:46Z` |
| `assets/theme.css` QA | MD5 `b86a0e260263eed6a2586a3e7bca8e05`, size `242427`, updated `2026-06-25T10:01:20Z` |

## URLs medidas

Las mediciones se hicieron en storefront QA con assets `/t/46` y sin assets `/t/45`.

| Idioma | URL | Viewport | H1 | Assets `/t/46` | Assets `/t/45` |
|---|---|---:|---|---:|---:|
| FR | `/fr/products/telechargeur-de-fichiers-personnalise?preview_theme_id=178399019384&mwqa=010c4-fr-390` | 390 | `Votre Fresque Personnalisée` | 11 | 0 |
| FR | `/fr/products/telechargeur-de-fichiers-personnalise?preview_theme_id=178399019384&mwqa=010c4-fr-375` | 375 | `Votre Fresque Personnalisée` | 11 | 0 |
| NL | `/nl/products/aangepaste-bestandsbelaster?preview_theme_id=178399019384&mwqa=010c4-nl-390` | 390 | `Uw Aangepaste Muurschildering` | 11 | 0 |
| NL | `/nl/products/aangepaste-bestandsbelaster?preview_theme_id=178399019384&mwqa=010c4-nl-375` | 375 | `Uw Aangepaste Muurschildering` | 11 | 0 |

## Resultado de overflow

| Idioma | Viewport | `docClientWidth` | `docScrollWidth` | Overflow vs `innerWidth` | `main#main` scroll | Resultado |
|---|---:|---:|---:|---:|---:|---|
| FR | 390 | 375 | 447 | `+57 px` | 447 | `INCORRECTO` visual pendiente |
| FR | 375 | 360 | 447 | `+72 px` | 447 | `INCORRECTO` visual pendiente |
| NL | 390 | 375 | 427 | `+37 px` | 427 | `INCORRECTO` visual pendiente |
| NL | 375 | 360 | 427 | `+52 px` | 427 | `INCORRECTO` visual pendiente |

## Aislamiento del origen

El lote 010C3 apuntó a `related-products`, pero la medición 010C4 demuestra que no es el origen del ancho de documento.

| Nodo | FR 390 `client/scroll/own` | FR 375 `client/scroll/own` | NL 390 `client/scroll/own` | NL 375 `client/scroll/own` | Interpretación |
|---|---:|---:|---:|---:|---|
| `main#main` | `375 / 447 / 72` | `360 / 447 / 87` | `375 / 427 / 52` | `360 / 427 / 67` | El overflow nace dentro de `main` |
| `.product-info` / `safe-sticky.product-info` | `335 / 427 / 92` | `320 / 427 / 107` | `335 / 407 / 72` | `320 / 407 / 87` | Contenedor afectado |
| `.product-info__variant-picker` | `335 / 427 / 92` | `320 / 427 / 107` | `335 / 407 / 72` | `320 / 407 / 87` | Origen acotado |
| `variant-picker#div-to-duplicate` | `335 / 427 / 92` | `320 / 427 / 107` | `335 / 407 / 72` | `320 / 407 / 87` | Origen acotado |
| `.variant-picker__option-values.wrap.gap-2` | `335 / 427 / 92` | `320 / 427 / 107` | `335 / 407 / 72` | `320 / 407 / 87` | Origen directo |
| `.shopify-section--product-recommendations` | `375 / 375 / 0` | `360 / 360 / 0` | `375 / 375 / 0` | `360 / 360 / 0` | No ensancha el documento |
| `related-products scroll-carousel` | `375 / 1523 / 1148` | `360 / 1469 / 1109` | `375 / 1523 / 1148` | `360 / 1469 / 1109` | Scroll interno correcto, no causa raíz |
| `ul.mobile-menu` | scroll interno | scroll interno | scroll interno | scroll interno | Scroll interno de menú, no causa raíz principal |

## Causa exacta

La causa queda acotada al pseudo-elemento de tooltip de los swatches:

- Selector fuente: `.block-swatch[data-tooltip]::after`.
- Origen en tema QA: `snippets/variant-picker.liquid`.
- Regla detectada en CSS inline del snippet:
  - `content: attr(data-tooltip)`.
  - `position: absolute`.
  - `left: 50%`.
  - `transform: translateX(-50%)`.
  - `white-space: nowrap`.
  - `opacity: 0`.
  - `visibility: hidden`.
- Aunque el tooltip está invisible, su caja absoluta con texto largo cuenta para el `scrollWidth` del contenedor móvil.

Evidencia NL 375:

| Swatch | Ancho visible | `scrollWidth` | Exceso | `::after` |
|---|---:|---:|---:|---|
| `NIET GEWEVEN` | 74 px | 188 px | +114 px | tooltip `Wandstaart - 50 cm brede strips - 0,20 inch breed`, ancho aprox. 302 px |
| `VINYL` | 60 px | 181 px | +121 px | tooltip ancho aprox. 302 px |
| `SCHIL & STOK` | 68 px | 212 px | +144 px | tooltip `50 cm brede strips - 0,20 inch zelf -adhesieve wandbreedte`, ancho aprox. 357 px |
| `METALLICS` | 60 px | 181 px | +121 px | tooltip ancho aprox. 302 px |

Evidencia FR:

| Swatch | Viewport | Ancho visible | `scrollWidth` | Exceso |
|---|---:|---:|---:|---:|
| `NON TISSÉ` | 390/375 | 60 px | 201 px | +141 px |
| `VINYLE` | 390/375 | 60 px | 201 px | +141 px |
| `PELER ET BÂTON` | 390/375 | 81 px | 235 px | +154 px |
| `MÉTALLIQUE` | 390/375 | 62 px | 202 px | +140 px |

## Conclusión

`MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3` queda confirmado como candidato de causa incorrecta para esta incidencia.

La causa real del overflow FR/NL del uploader móvil está en el tooltip `::after` de los swatches de variantes/materiales, renderizado desde `snippets/variant-picker.liquid`.

## Próximo lote recomendado

`MW-TECH-MOBILE-OVERFLOW-SWATCH-TOOLTIP-010C5`

Objetivo: en el tema QA `178399019384`, ocultar o neutralizar en móvil el pseudo-tooltip `::after` de `.block-swatch[data-tooltip]`, preservando desktop y sin tocar productos, variantes, precios, inventario ni relacionados.

## Riesgo estimado del siguiente lote

`VERIFICADO PERO MEJORABLE`

- Bajo riesgo si se acota a `max-width: 699px`.
- Efecto previsto: desaparece el tooltip hover de swatches en móvil, donde el hover no es una interacción fiable.
- Desktop debe mantenerse intacto.
- Debe validarse ES/EN/FR/DE/NL, uploader y producto estándar.

## Pruebas requeridas para 010C5

- FR uploader móvil 390 y 375: overflow `0`.
- NL uploader móvil 390 y 375: overflow `0`.
- ES/EN/DE uploader móvil 390: sin nuevo overflow.
- Producto estándar móvil ES/FR/NL: sin nuevo overflow.
- Desktop 1440 ES/FR/NL: tooltip hover y layout sin regresión.
- Related products: carrusel móvil sigue desplazable internamente.
- Tracking y flujo del uploader sin regresión.
