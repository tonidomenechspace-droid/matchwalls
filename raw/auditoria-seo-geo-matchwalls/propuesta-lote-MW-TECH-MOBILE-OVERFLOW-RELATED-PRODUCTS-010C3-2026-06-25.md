# Propuesta lote MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3 - 2026-06-25

## Estado

`REQUIERE DECISION HUMANA`

No ejecutado. Pendiente de aprobación exacta.

## Aprobación necesaria

Para ejecutar este lote, Daniel debe responder exactamente:

`APROBADO LOTE MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3`

## Motivo

La regresión compacta `MW-TECH-QA-REGRESSION-MATRIX-010Z` detectó overflow horizontal móvil en el producto uploader FR/NL:

| URL | Viewport | ScrollWidth | Overflow |
|---|---:|---:|---:|
| `/fr/products/telechargeur-de-fichiers-personnalise?mwqa=010a2d` | 390 | 447 | +57 px |
| `/nl/products/aangepaste-bestandsbelaster?mwqa=010a2d` | 390 | 427 | +37 px |
| `/fr/products/telechargeur-de-fichiers-personnalise?mwqa=010a2d` | 375 | 447 | +72 px |
| `/nl/products/aangepaste-bestandsbelaster?mwqa=010a2d` | 375 | 427 | +52 px |

La causa probable está acotada a la sección de productos relacionados:

- `shopify-section--product-recommendations`.
- `scroll-carousel`.
- `scroll-area-template--24951169024376__related-products`.
- `REVEAL-ITEMS` interno con ancho observado `1483 px`.

## Alcance exacto

Tema afectado:

- `gid://shopify/OnlineStoreTheme/178399019384`.
- Rol: `UNPUBLISHED`.
- Prefijo: `/t/46`.

Archivo principal candidato:

- `sections/related-products.liquid`.
- MD5 actual: `d8822a8c73cee73d61744c0b68b7a375`.
- Size actual: `10705`.
- `updatedAt`: `2026-06-18T18:30:51Z`.

Archivo alternativo solo si se justifica en ejecución:

- `assets/theme.css`.
- MD5 actual: `b86a0e260263eed6a2586a3e7bca8e05`.
- Size actual: `242427`.
- `updatedAt`: `2026-06-25T10:01:20Z`.

Exclusiones:

- No modificar MAIN.
- No publicar tema.
- No modificar productos, precios, variantes, inventario, handles, canonicals, hreflang, redirecciones, GA4, GTM, Merchant Center ni apps.

## Valores actuales

En `sections/related-products.liquid`, la sección define CSS embebido por `section.id` y genera:

- `<scroll-carousel class="scroll-area bleed ...">`
- `<reveal-items selector=".product-list > *">`
- `<product-list class="product-list">`

En móvil, el carrusel conserva contenido interno más ancho que el viewport y termina generando anchura de documento en las URLs FR/NL del uploader.

## Valor propuesto

Añadir una regla móvil acotada al `section.id` de `related-products` para contener el overflow horizontal de la sección sin tocar desktop ni el cálculo de productos.

Candidato conceptual a validar durante ejecución:

```liquid
@media screen and (max-width: 699px) {
  #shopify-section-{{ section.id }} {
    overflow-x: hidden;
  }

  #shopify-section-{{ section.id }} .section-stack,
  #shopify-section-{{ section.id }} .floating-controls-container {
    min-width: 0;
  }

  #shopify-section-{{ section.id }} .scroll-area.bleed {
    max-width: 100vw;
    overflow-x: auto;
    overflow-y: hidden;
  }
}
```

La forma final debe validarse sobre la web antes de guardar si se detecta que el carrusel pierde usabilidad.

## Riesgos

- Puede afectar todos los bloques `related-products` en páginas de producto móvil, no solo el uploader.
- Puede modificar el comportamiento visual del carrusel móvil si la regla es demasiado restrictiva.
- Puede ocultar controles laterales si dependen del overflow visible.
- No debe impactar desktop si se mantiene el `max-width: 699px`.

## Reversión

Restaurar `sections/related-products.liquid` a MD5 `d8822a8c73cee73d61744c0b68b7a375`, size `10705`.

Si finalmente se tocara `assets/theme.css`, restaurar a MD5 `b86a0e260263eed6a2586a3e7bca8e05`, size `242427`.

## Pruebas posteriores obligatorias

- Readback Shopify: rol `UNPUBLISHED`, `processing=false`, `processingFailed=false`.
- FR uploader móvil 390 y 375: overflow 0.
- NL uploader móvil 390 y 375: overflow 0.
- Verificar que el carrusel de productos relacionados sigue siendo desplazable en móvil.
- Producto estándar móvil ES: sin overflow nuevo.
- Home móvil ES: sin overflow nuevo.
- Uploader ES/EN/FR/DE/NL desktop: tracking `input_mural_outside` sigue correcto.
- Producto estándar ES desktop: tracking correcto.
- Consola: 0 errores en URLs centinela.
- Assets `/t/46`; no `/t/45`.
## Resultado de ejecución - 2026-06-25

`INCORRECTO` para el candidato. Rollback final: `CORREGIDO Y VERIFICADO`.

- Lote aprobado exactamente: `APROBADO LOTE MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3`.
- Candidato aplicado en QA `178399019384`: MD5 `e1637667eebf1ec246786deaa2a45297`, size `11112`; `themeFilesUpsert` con `userErrors=[]`.
- QA crítica fallida: FR móvil 390 mantuvo overflow `+57 px`; NL móvil 390 mantuvo overflow `+37 px`; assets `/t/46`, sin assets `/t/45`, consola sin errores.
- Se ejecutó rollback. La primera lectura intermedia detectó MD5 `ccd037da6ce4b2f41963e823e3845e48`; no se aceptó como estado final.
- Restauración final verificada: QA `sections/related-products.liquid` MD5 `d8822a8c73cee73d61744c0b68b7a375`, size `10705`, igual que MAIN.
- `assets/theme.css` no fue modificado.
- MAIN no fue modificado.
- Estado final: no publicar, no promover 010C3, abrir diagnóstico fino `MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-DIAG-010C4` antes de proponer otro cambio.