# Auditoría de datos estructurados

## Hechos verificados

| Tipo | Cobertura observada | Evaluación |
|---|---:|---|
| Product / Offer / Brand | 116 páginas válidas | Presente en productos; validar cobertura completa y consistencia de precio/disponibilidad. |
| AggregateRating | 7 páginas, las homes localizadas | Riesgo alto: no se observó `Review` schema. Debe comprobarse que la puntuación representa reseñas visibles, actuales y elegibles. |
| Review | 0 páginas | No presente en la muestra. No debe añadirse solo para justificar AggregateRating sin reseñas reales visibles. |
| BreadcrumbList | 564 páginas | Cobertura amplia. |
| WebSite / SearchAction | 7 homes | Correcto como base. |
| Organization | 40 páginas | Presente en homes/artículos; consolidar identidad, `sameAs`, logo y contacto. |
| BlogPosting | 33 artículos | Presente; revisar autor, fechas, imágenes y entidad editora. |
| FAQPage | 14 páginas | Presente; mantener sincronizado con contenido visible. |

## Hallazgo prioritario: AggregateRating

`AggregateRating` aparece en las siete homes localizadas, no en los productos observados. Esto puede ser válido únicamente si representa una entidad elegible y la valoración es visible y verificable en la propia página conforme a las políticas del buscador. La ausencia de `Review` no invalida automáticamente el agregado, pero aumenta la necesidad de revisar su procedencia, entidad evaluada, recuento, valor y contenido visible.

**Acción recomendada:** validar cada home con Rich Results Test y Schema Markup Validator; documentar fuente, fecha y método; retirar o corregir el marcado si no coincide con la experiencia visible. No realizar cambios sin autorización.

## Modelo recomendado

- Producto: `Product` + `Offer` coherente con variante/precio/disponibilidad visibles; SKU y GTIN/MPN cuando existan.
- Muestra: decidir si es producto independiente. Si no debe posicionar, evitar que compita con el producto principal.
- Organización: una entidad estable con `sameAs`, datos de contacto, política de envíos/devoluciones y país.
- Artículos/guías: `Article`/`BlogPosting` con autor experto, fecha de publicación/modificación y fuentes.
- FAQ: solo preguntas y respuestas visibles; evitar marcado repetido sin valor.

## Actualización verificada en Shopify

### GTIN falsos

El tema principal interpreta como GTIN cualquier barcode numérico de longitud compatible. En una muestra de 50 productos activos y 65 variantes, los 65 barcodes coinciden exactamente con el ID interno de la variante Shopify. Por tanto, esos valores no son identificadores comerciales verificables y no deben publicarse como GTIN.

**Acción segura preparada:** el tema no publicado `SEO schema hotfix - 2026-06-15` conserva SKU y Offer, pero omite GTIN cuando `barcode == variant.id`.

### AggregateRating y breadcrumbs

- El hotfix elimina el AggregateRating fijo de Organization porque no se ha demostrado su fuente ni elegibilidad.
- El hotfix corrige el tercer elemento del breadcrumb de artículos para que represente el artículo y no repita el blog.
- Las pruebas en home, producto y artículo no mostraron errores de parseo JSON-LD.

### Estado de despliegue

El hotfix funcional está corregido y verificado en el tema no publicado. El checksum del archivo aplicado coincide con la versión local validada. Google Rich Results Test detectó tres elementos válidos sin errores críticos. No se ha publicado.

Permanece una copia auxiliar sin uso, `snippets/microdata-schema-original.liquid`, porque Shopify bloqueó su borrado desde la conexión. Los assets compilados distintos conservan fuentes `.liquid` idénticas a MAIN. La evidencia completa está en `qa-hotfix-schema-2026-06-15.md`.
## Actualizacion 16 de junio de 2026

Daniel confirmo la publicacion manual del tema `SEO schema hotfix - 2026-06-15`.

Estado verificado tras publicacion:

- El hotfix es ahora el tema `MAIN`: `gid://shopify/OnlineStoreTheme/178383749496`.
- `SEO-GEO staging - 2026-06-15` permanece `UNPUBLISHED`.
- `snippets/microdata-schema.liquid` conserva checksum `58417e4825aa3d4570a6646f292aaedc`.
- `snippets/microdata-schema-original.liquid` permanece como copia auxiliar conservada.
- 35 URLs revisadas en escritorio y 35 en movil cargan `/cdn/shop/t/43/`.
- Errores JSON-LD: 0.
- `AggregateRating` corporativo fijo detectado: 0.
- GTIN/MPN falsos detectados: 0.
- Productos probados con `Product` y 4 `Offer` completos: 10/10 en escritorio y 10/10 en movil.

Estado del hotfix publicado: `CORREGIDO Y VERIFICADO`.

Limitacion: siguen pendientes la validacion completa de todo el catalogo, la auditoria Merchant Center/Search Console y las mejoras de Organization, FAQ, Article y Product schema no incluidas en este hotfix.

Evidencia: `qa-post-publicacion-hotfix-2026-06-16-MW-PUBLISH-HOTFIX-001.md`.
