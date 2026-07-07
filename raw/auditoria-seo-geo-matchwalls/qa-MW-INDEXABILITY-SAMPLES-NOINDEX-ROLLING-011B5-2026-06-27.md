# QA final - MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5

Fecha/hora cierre: 2026-06-27 00:59:45 +02:00
Estado final: `CORREGIDO Y VERIFICADO`

## Alcance ejecutado

- 75 productos muestra limpios.
- 473 URLs localizadas asociadas.
- Ejecucion en 3 bloques de 25 productos.
- Producto anomalo excluido: `gid://shopify/Product/8554043474147` / `muestra-abstract-curves-negro`.
- No se tocaron handles, canonicals, redirecciones, tema, precios, inventario, variantes, apps ni Search Console/Bing/GA4/GTM/Merchant Center.

## Resultado por bloque

| Bloque | Productos Admin | URLs publicas | URLs publicas OK | URLs sitemap | Ausentes sitemap OK |
|---|---:|---:|---:|---:|---:|
| 011B5-01 | 25 | 173 | 173 | 173 | 173 |
| 011B5-02 | 25 | 144 | 144 | 144 | 144 |
| 011B5-03 | 25 | 156 | 156 | 156 | 156 |

## Resultado consolidado

- Admin final: 75/75 con `seo.hidden=1` y `type=number_integer`.
- Storefront: 473/473 URLs con HTTP 200, `noindex,nofollow`, canonical self y H1 presente.
- Sitemaps de producto: 473/473 URLs ausentes.
- Product sitemaps revisados: 7.

## Incidencias

- Primera pasada del bloque 2 detecto 1 URL IT sin meta robots por respuesta transitoria/cach?: `https://www.matchwalls.com/it/products/armony-rosa-stripe-sample`.
- Reintento aislado: 4/4 correcto con `noindex,nofollow`, canonical self y H1.
- Re-QA completa del bloque 2: 144/144 correcto. No queda incidencia abierta.

## Evidencias generadas

- `admin-seohidden-post-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`
- `qa-publico-localizado-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`
- `qa-sitemap-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`
- `qa-sitemap-products-checked-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`
- `qa-publico-localizado-bloque-01-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`
- `qa-publico-localizado-bloque-02-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`
- `qa-publico-localizado-bloque-03-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`
- `qa-sitemap-bloque-01-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`
- `qa-sitemap-bloque-02-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`
- `qa-sitemap-bloque-03-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`

## Rollback

Para revertir, ejecutar `metafieldsDelete` por cada Product GID afectado: namespace `seo`, key `hidden`. Estado esperado tras rollback: `seo.hidden=null`.

## Siguiente recomendado

- Tratar la anomalia excluida en lote separado: `MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B`.
- Despues continuar con la clasificacion de URLs restantes: colecciones geograficas, pruebas/URLs sin valor y redirecciones.
