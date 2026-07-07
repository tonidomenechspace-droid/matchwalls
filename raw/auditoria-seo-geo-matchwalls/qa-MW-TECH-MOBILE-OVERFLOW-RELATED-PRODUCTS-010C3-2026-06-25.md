# QA MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3 - 2026-06-25

## Estado

`INCORRECTO` para el candidato. Rollback final: `CORREGIDO Y VERIFICADO`.

## Lote aprobado

`APROBADO LOTE MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3`

## Alcance real ejecutado

- Tema QA: `gid://shopify/OnlineStoreTheme/178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.
- Archivo: `sections/related-products.liquid`.
- MAIN: `gid://shopify/OnlineStoreTheme/178396463480`, rol `MAIN`, prefijo `/t/45`; solo lectura.
- `assets/theme.css`: solo lectura; no modificado.
- No se publicó ningún tema.

## Estado previo verificado

| Recurso | Tema | MD5 | Size | Estado |
|---|---:|---:|---:|---|
| `sections/related-products.liquid` | QA `178399019384` | `d8822a8c73cee73d61744c0b68b7a375` | `10705` | `VERIFICADO Y CORRECTO` |
| `assets/theme.css` | QA `178399019384` | `b86a0e260263eed6a2586a3e7bca8e05` | `242427` | `VERIFICADO Y CORRECTO` |
| `sections/related-products.liquid` | MAIN `178396463480` | `d8822a8c73cee73d61744c0b68b7a375` | `10705` | `VERIFICADO Y CORRECTO` |
| `assets/theme.css` | MAIN `178396463480` | `89f4729809a0eaac75a764e0fc41888e` | `241968` | `VERIFICADO Y CORRECTO` |

## Validación previa local

- Estructura Liquid revisada: un bloque `{% schema %}` y un bloque `<style>`.
- JSON de schema válido.
- Validación local completa de Shopify Theme Check: `NO ACCESIBLE` por dependencia local ausente `@shopify/theme-check-common`.
- Se consultó documentación Shopify Liquid; se mantuvo CSS en `<style>` porque Liquid no se renderiza dentro de `{% stylesheet %}`.

## Candidato aplicado

- MD5 candidato local: `e1637667eebf1ec246786deaa2a45297`.
- Size candidato: `11112`.
- Cambio conceptual: añadir `@media screen and (max-width: 699px)` en `sections/related-products.liquid` para contener `overflow-x` en la sección de productos relacionados.
- Mutación `themeFilesUpsert`: `userErrors=[]`.
- Readback candidato: MD5 `e1637667eebf1ec246786deaa2a45297`, size `11112`.

## Resultado QA del candidato

`INCORRECTO`

| URL | Viewport | Assets QA | Assets MAIN | Overflow | Consola | Resultado |
|---|---:|---:|---:|---:|---|---|
| `/fr/products/telechargeur-de-fichiers-personnalise?mwqa=010c3` | 390 px | 11 | 0 | `+57 px` | 0 errores | No corrige |
| `/nl/products/aangepaste-bestandsbelaster?mwqa=010c3` | 390 px | 11 | 0 | `+37 px` | 0 errores | No corrige |

Conclusión: el cambio no resuelve la causa real del `scrollWidth` en FR/NL.

## Rollback

`CORREGIDO Y VERIFICADO`

- Se ejecutó rollback al archivo original.
- Una primera lectura intermedia devolvió MD5 `ccd037da6ce4b2f41963e823e3845e48`, size `10699`, por una discrepancia en una clase de flecha. Este estado no fue aceptado como final.
- Se repitió la restauración desde el archivo local verificado contra MAIN.
- Readback final QA: MD5 `d8822a8c73cee73d61744c0b68b7a375`, size `10705`, `processing=false`, `processingFailed=false`.
- MAIN final: MD5 `d8822a8c73cee73d61744c0b68b7a375`, size `10705`, `processing=false`, `processingFailed=false`.

## QA pública después del rollback

| URL | Viewport | Assets QA | Assets MAIN | H1 | Canonical | Hreflang | Overflow | Consola |
|---|---:|---:|---:|---|---|---:|---:|---|
| NL uploader | 390 px | 11 | 0 | `Uw aangepaste muurschildering` | correcto | 8 | `+37 px` | 0 errores |
| FR uploader | 390 px | 11 | 0 | `Votre fresque personnalisée` | correcto | 8 | `+57 px` | 0 errores |

## Decisión técnica

- No publicar.
- No promover 010C3.
- No repetir parche CSS sin diagnóstico más fino.
- Siguiente recomendado: `MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-DIAG-010C4`, solo lectura, para identificar el nodo exacto que expande el documento y distinguir si el origen es `scroll-carousel`, `product-card`, controles flotantes, padding/bleed o contenido traducido.