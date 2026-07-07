# QA del tema no publicado SEO schema hotfix - 2026-06-15

Fecha de cierre: 15 de junio de 2026

## Decisión

**Aprobado por Daniel para publicación manual.** El hotfix funcional está corregido y verificado. La conexión disponible bloquea por seguridad la publicación automática de temas, por lo que queda pendiente únicamente la acción manual desde Shopify.

## Alcance ejecutado

- Tema modificado: `SEO schema hotfix - 2026-06-15`.
- ID: `gid://shopify/OnlineStoreTheme/178383749496`.
- Rol comprobado después del cambio: `UNPUBLISHED`.
- Tema MAIN: no modificado.
- Único archivo funcional actualizado: `snippets/microdata-schema.liquid`.
- Checksum local y Shopify coincidente: `58417e4825aa3d4570a6646f292aaedc`.

## Checklist con evidencias

| Comprobación | Resultado | Evidencia |
|---|---|---|
| Diferencia exacta frente a MAIN | Aprobado con observaciones | El archivo funcional diferente es `snippets/microdata-schema.liquid`. Las fuentes `.liquid` de los assets compilados coinciden con MAIN. |
| GTIN falsos | Aprobado | Producto ES y EN: 4 ofertas, 4 SKU, 0 `gtin` y 0 `mpn` cuando los barcodes coinciden con IDs internos. |
| Product y Offer | Aprobado | Product conserva SKU superior, peso `QuantitativeValue`, `ImageObject`, 4 Offer, precios, moneda, disponibilidad, URL y SKU por oferta. |
| AggregateRating corporativo fijo | Aprobado | Home conserva BreadcrumbList, WebSite y Organization, sin AggregateRating no demostrable. |
| Breadcrumb de artículo | Aprobado | El tercer elemento usa el título real del artículo. |
| Rich Results Test | Aprobado | Google detecta 3 elementos válidos: fragmento de producto, ficha de comerciante y breadcrumb; sin errores críticos. |
| Home | Aprobado | JSON-LD parseable, BreadcrumbList + WebSite + Organization, H1 presente, sin desbordamiento de escritorio. |
| Producto ES | Aprobado | H1 único, JSON-LD parseable, Product + BreadcrumbList, 4 ofertas y 0 GTIN/MPN falsos. |
| Producto EN | Aprobado | `lang=en`, H1 correcto, Product + BreadcrumbList, 4 ofertas y 0 GTIN/MPN falsos. |
| Artículo | Aprobado con observación | BlogPosting y BreadcrumbList parseables; se conservan campos existentes. El autor vacío es un problema previo no incluido en este hotfix. |
| Carrito | Aprobado con observación | Renderiza en escritorio y móvil sin errores JSON-LD. Sigue sin H1, problema previo no causado por el hotfix. |
| Formularios | Aprobado con observaciones | `formulario-particulares` renderiza y conserva formulario. La página `/pages/contact` mantiene dos H1 y los problemas previos de contenido. |
| Móvil y escritorio | Aprobado con observación | Home, carrito y formulario sin desbordamiento. Producto presenta 52 px de desbordamiento a 390 px, también ajeno al schema. |
| App Embeds | Aprobado | `config/settings_data.json` coincide con MAIN: `a1192f2f698d277e0f69f7156a61a90c`. |
| Otros cambios inesperados | Observación pendiente | Permanece `snippets/microdata-schema-original.liquid`, copia exacta del schema MAIN y sin referencias. Shopify bloqueó su borrado desde la conexión. |

## Diferencias conocidas respecto a MAIN

- `snippets/microdata-schema.liquid`: diferencia intencionada y validada.
- `snippets/microdata-schema-original.liquid`: archivo auxiliar sin uso; copia exacta de MAIN.
- `assets/country-flags.css`, `assets/sections.js` y `assets/theme.js`: compilados distintos generados por Shopify; sus fuentes `.liquid` coinciden con MAIN.
- Configuración, App Embeds, layout y plantillas representativas comprobadas: coinciden con MAIN.

## Contenido exacto del hotfix funcional

1. Omite GTIN y MPN si el barcode coincide con el ID interno de la variante.
2. Conserva GTIN o MPN cuando exista un barcode comercial distinto del ID interno.
3. Retira solo el AggregateRating corporativo fijo y no justificable.
4. Corrige solo el nombre del tercer breadcrumb de artículos.
5. Conserva el resto del schema MAIN.

## Pendientes antes de publicar

1. Publicar manualmente únicamente `SEO schema hotfix - 2026-06-15`.
2. Conservar temporalmente el archivo auxiliar sin uso, según aprobación de Daniel.
3. No publicar `SEO-GEO staging - 2026-06-15`.

## Aprobación recibida

- Daniel aprobó la publicación del hotfix el 15 de junio de 2026.
- Daniel aprobó conservar temporalmente `snippets/microdata-schema-original.liquid`.
- Comprobación inmediatamente anterior a publicación: tema `UNPUBLISHED`, `processing: false`, `processingFailed: false` y checksum funcional `58417e4825aa3d4570a6646f292aaedc`.

## Verificación ampliada ES, EN, DE, FR y NL

El hotfix de schema se comprobó públicamente en una ficha de producto localizada de cada idioma prioritario.

| Idioma | Product y Breadcrumb | Ofertas / SKU | GTIN/MPN falsos | Resultado |
|---|---|---:|---:|---|
| ES | Válidos y localizados | 4 / 4 | 0 / 0 | Aprobado |
| EN | Válidos y localizados | 4 / 4 | 0 / 0 | Aprobado |
| DE | Válidos y localizados | 4 / 4 | 0 / 0 | Aprobado |
| FR | Válidos y localizados | 4 / 4 | 0 / 0 | Aprobado |
| NL | Válidos y localizados | 4 / 4 | 0 / 0 | Aprobado |

Las cinco homes conservan canonical propio, ocho hreflang, BreadcrumbList, WebSite y Organization, sin AggregateRating corporativo fijo y sin errores JSON-LD. Los cinco artículos localizados conservan BlogPosting y muestran el título real del artículo como tercer breadcrumb.

Esta aprobación se limita al hotfix. No significa que todo el contenido internacional esté corregido.

## Errores internacionales que permanecen fuera del hotfix

- Home NL: H1 defectuoso `Matchwalls: Papeadra Papel -specialisten` y title en español.
- Home DE: H1 poco natural `Bemalten Papiere für Wände und Wandgemälde`.
- Producto DE: siguen visibles `Offenes Auto`, `3 mit Klarna in 3 Amtszeiten bezahlen` y `Haben Sie Ihre eigenen Designs? Wir werden wahr!`.
- Producto NL: siguen visibles `Open auto`, `Betaal in 3 termen met Klarna`, `Spaties` y `Heeft u uw eigen ontwerpen? We komen uit!`.
- Atención al cliente EN y DE: conservan el segundo H1 español `Atención al cliente — MatchWalls`.
- Artículos ES, EN, DE, FR y NL: el schema de autor sigue vacío.
- Títulos editoriales de artículos DE y NL contienen traducciones automáticas deficientes.
