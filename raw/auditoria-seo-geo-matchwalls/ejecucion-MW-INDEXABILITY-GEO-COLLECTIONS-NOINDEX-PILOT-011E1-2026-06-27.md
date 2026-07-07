# Ejecución MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1

Fecha: 2026-06-27  
Estado final: `CORREGIDO Y VERIFICADO`

## Aprobación

`APROBADO LOTE MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1`

## Alcance ejecutado

Aplicado `seo.hidden=1` a 6 colecciones geográficas no estratégicas:

- `gid://shopify/Collection/443626914019` — `comprar-papel-pintado-alava`.
- `gid://shopify/Collection/646109593976` — `comprar-papel-pintado-albacete`.
- `gid://shopify/Collection/646109626744` — `comprar-papel-pintado-alicante`.
- `gid://shopify/Collection/646109659512` — `comprar-papel-pintado-almeria`.
- `gid://shopify/Collection/646109757816` — `comprar-papel-pintado-badajoz`.
- `gid://shopify/Collection/646109856120` — `comprar-papel-pintado-burgos`.

No se modificaron handles, redirecciones, productos, precios, inventario, contenido visible, tema, navegación, canonicals manuales ni traducciones.

## Respaldo previo

`VERIFICADO Y CORRECTO`

- Archivo: `backup-pre-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- Valor previo común: `seo.hidden = null`.
- `productsCount = 73` en 6/6.
- `resourcePublicationsCount = 9` en 6/6.

## Operación ejecutada

`CORREGIDO Y VERIFICADO`

- Mutación Admin GraphQL validada: `metafieldsSet`.
- Namespace: `seo`.
- Key: `hidden`.
- Type: `number_integer`.
- Value: `1`.
- Resultado Shopify: `userErrors: []`.

Metafields creados:

- `gid://shopify/Metafield/198966948921720` — Álava.
- `gid://shopify/Metafield/198966948954488` — Albacete.
- `gid://shopify/Metafield/198966948987256` — Alicante.
- `gid://shopify/Metafield/198966949020024` — Almería.
- `gid://shopify/Metafield/198966949052792` — Badajoz.
- `gid://shopify/Metafield/198966949085560` — Burgos.

## Verificación Admin

`CORREGIDO Y VERIFICADO`

- Archivo: `admin-post-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- 6/6 colecciones verificadas con:
  - `seo.hidden = 1`;
  - type `number_integer`;
  - updatedAt `2026-06-27T09:45:49Z`.

## Verificación pública

`CORREGIDO Y VERIFICADO`

- Archivo: `qa-publico-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- 36/36 URLs localizadas responden 200.
- 36/36 URLs tienen meta robots `noindex,nofollow`.
- Las páginas siguen accesibles directamente, sin eliminación ni redirección.

Distribución verificada:

- ES: 6.
- EN: 6.
- FR: 5.
- DE: 5.
- NL: 6.
- PT: 6.
- IT: 2.

## Verificación sitemap

`CORREGIDO Y VERIFICADO`

- Archivo: `qa-sitemap-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- 36/36 URLs afectadas ausentes de los sitemaps localizados.
- Cada sitemap de colecciones revisado pasa de 106 a 100 URLs.

Estado geo restante:

- Archivo: `qa-sitemap-geo-restante-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- Geográficas candidatas todavía presentes en sitemap: 310.
- Distribución restante:
  - ES 52.
  - EN 50.
  - FR 51.
  - DE 36.
  - NL 46.
  - PT 49.
  - IT 26.

## Método de reversión

`VERIFICADO Y CORRECTO`

Eliminar los 6 metafields `seo.hidden` creados en este lote:

- `gid://shopify/Metafield/198966948921720`.
- `gid://shopify/Metafield/198966948954488`.
- `gid://shopify/Metafield/198966948987256`.
- `gid://shopify/Metafield/198966949020024`.
- `gid://shopify/Metafield/198966949052792`.
- `gid://shopify/Metafield/198966949085560`.

Tras reversión:

1. Verificar Admin: `seo.hidden = null`.
2. Verificar público: sin robots `noindex`.
3. Verificar sitemap tras regeneración/caché.

## Evidencias

- `diagnostico-MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E-2026-06-27.md`.
- `propuesta-lote-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.md`.
- `backup-pre-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- `admin-post-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- `qa-publico-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- `qa-sitemap-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- `qa-summary-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.txt`.
- `qa-sitemap-geo-restante-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.

