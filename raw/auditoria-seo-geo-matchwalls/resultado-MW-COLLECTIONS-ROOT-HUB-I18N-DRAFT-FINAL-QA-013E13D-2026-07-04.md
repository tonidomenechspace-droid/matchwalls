# Resultado MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-FINAL-QA-013E13D

Fecha: 2026-07-04  
Estado final: `VERIFICADO PERO MEJORABLE`

## Alcance aprobado

`APROBADO LOTE MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-FINAL-QA-013E13D`

Lote de solo lectura para QA final del tema draft `178396463480` antes de cualquier decisión sobre MAIN.

No se ejecutaron escrituras en Shopify. No se tocó MAIN, LangShop, páginas, productos, colecciones, handles, URLs, redirecciones, canonicals, hreflang, robots, sitemaps, Bing, IndexNow, precios, inventario ni publicación.

## Estado real Shopify

`VERIFICADO Y CORRECTO`

- Draft: `gid://shopify/OnlineStoreTheme/178396463480`.
- Rol draft: `UNPUBLISHED`.
- Archivo evaluado: `sections/main-list-collections.liquid`.
- Checksum draft: `910b00ca49c28be5258ac2a17f1731d5`.
- MAIN: `gid://shopify/OnlineStoreTheme/178399019384`.
- Rol MAIN: `MAIN`.
- Checksum MAIN del mismo archivo: `70c8ead00d939f15528f6f11e5bfb540`.
- MAIN no fue modificado.

## QA desktop y mobile

`CORREGIDO Y VERIFICADO`

Se verificaron 10 combinaciones:

- Desktop: ES, EN, FR, DE y NL.
- Mobile: ES, EN, FR, DE y NL.

Resultado del bloque nuevo:

- 10/10 con bloque `.mw-collections-root` presente y visible.
- 10/10 con H1 correcto y único.
- 10/10 con 6 enlaces rápidos.
- 10/10 con 3 FAQs.
- 10/10 sin `translation missing`, sin claves Liquid visibles y sin URLs antiguas del producto custom uploader dentro del bloque.
- 10/10 con CTA de mural personalizado apuntando a páginas informativas indexables.
- 10/10 con canonical visible coherente.
- 10/10 con 8 alternates hreflang visibles.
- 10/10 con JSON-LD parseable; tipo detectado: `BreadcrumbList`.
- 10/10 con 48 `collection-card` en el listado completo de colecciones.

## Overflow

`VERIFICADO PERO MEJORABLE`

- El bloque nuevo no genera overflow horizontal: `root_overflow_px=0` en 10/10 combinaciones.
- La página completa muestra overflow heredado en:
  - FR mobile: `page_overflow_px=33`.
  - NL mobile: `page_overflow_px=7`.
- Este comportamiento ya era consistente con deuda previa de FR/NL móvil y no se atribuye al bloque nuevo.

## Deuda heredada detectada en listado de colecciones

`VERIFICADO PERO MEJORABLE`

El listado completo mantiene 48 tarjetas en todos los idiomas, pero se detectan textos heredados mejorables fuera del bloque nuevo:

- FR: ejemplos como `Nouveaux mortels` y `Le plus vendu`.
- DE: ejemplos como `Bestverkauf` y `Versicherte Eleganz`.
- NL: ejemplos como `Best verkopen` y `Nieuwe matchwalls`.
- EN/FR/DE/NL mantienen handles heredados con `matchwallsmurals` en algunas colecciones.

Esto no invalida el bloque 013E13C/013E13D, pero confirma que la arquitectura y traducción de colecciones sigue pendiente en un lote separado.

## Incidencia Shopify 012O

`VERIFICADO PERO MEJORABLE`

El QA 013E13D se ha realizado en preview autenticado y no depende de una publicación MAIN. La incidencia 012O de caché/render de storefront sigue pendiente de ingeniería Shopify y debe considerarse antes de cualquier promoción a MAIN.

## Evidencias

`VERIFICADO Y CORRECTO`

- `admin-read-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-FINAL-QA-013E13D-2026-07-04.csv`.
- `qa-final-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-FINAL-QA-013E13D-2026-07-04.csv`.
- `qa-collection-list-inherited-debt-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-FINAL-QA-013E13D-2026-07-04.csv`.

## Recomendación

`REQUIERE DECISION HUMANA`

No se recomienda promocionar a MAIN todavía hasta:

1. Recibir o agotar razonablemente la respuesta de ingeniería Shopify sobre 012O.
2. Decidir si se acepta publicar el hub con la deuda heredada de nombres de colecciones FR/DE/NL documentada, o si se abre antes un lote específico de corrección de colecciones.

Siguiente lote seguro recomendado:

`MW-COLLECTIONS-ROOT-HUB-I18N-PUBLISH-READINESS-013E13E`

Objetivo: propuesta de decisión de publicación, no ejecución, comparando beneficio/riesgo y definiendo exactamente si se espera a Shopify 012O o si se prepara una promoción quirúrgica posterior.
