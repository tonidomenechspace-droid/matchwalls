# QA final - MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B

Fecha/hora cierre: 2026-06-27 01:10:36 +02:00  
Estado final: `CORREGIDO Y VERIFICADO`

## Alcance ejecutado

- 1 producto anomalo confirmado como muestra por titulo, handle, plantilla y URLs.
- Product GID: `gid://shopify/Product/8554043474147`.
- Legacy ID: `8554043474147`.
- Campo modificado: metafield `seo.hidden`.
- Valor anterior: `null`.
- Valor nuevo: `1`.
- Tipo: `number_integer`.

No se tocaron:

- Producto principal `https://www.matchwalls.com/products/abstract-curves-negro`.
- `productType`.
- Handles.
- Canonicals.
- Redirecciones.
- Tema Shopify.
- Precios.
- Inventario.
- Variantes.
- Apps.

## Resultado Admin

- Shopify acepto la mutacion `SetSeoHiddenSampleAnomaly` con `userErrors=[]`.
- Lectura posterior Admin:
  - `seo.hidden.value=1`.
  - `seo.hidden.type=number_integer`.
  - `productType=Mural` permanece sin cambios.
  - `templateSuffix=muestra` permanece sin cambios.

## Resultado storefront

- 7/7 URLs de muestra responden HTTP 200.
- 7/7 URLs de muestra tienen meta robots `noindex,nofollow`.
- 7/7 URLs de muestra tienen canonical self.
- 7/7 URLs de muestra tienen H1 presente.
- Producto principal inferido responde HTTP 200, no tiene `noindex`, mantiene canonical self y H1.

## Resultado sitemap

- 7/7 URLs de muestra ausentes de product sitemaps.
- Producto principal `https://www.matchwalls.com/products/abstract-curves-negro` sigue presente en product sitemap.

## Evidencias generadas

- `admin-seohidden-post-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`
- `qa-publico-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`
- `qa-sitemap-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`
- `qa-sitemap-products-checked-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`

## Incidencias

- Sin incidencias abiertas.
- Queda deuda separada: el producto conserva `productType=Mural`. No se corrigio en este lote por alcance aprobado.
- Queda deuda linguistica separada: URL NL usa `sample` en ingles. No se corrigio en este lote por alcance aprobado.

## Rollback

Rollback exacto disponible:

- Ejecutar `metafieldsDelete`.
- ownerId: `gid://shopify/Product/8554043474147`.
- namespace: `seo`.
- key: `hidden`.
- Estado esperado tras rollback: `seo.hidden=null`.

## Siguiente recomendado

Continuar con indexabilidad restante:

- Clasificacion de 7.932 URLs.
- Muestras ya resueltas: 541/541 URLs de producto muestra localizadas retiradas de sitemap/noindex tras `011B4`, `011B5` y `011B5B`.
- Siguiente bloque probable: colecciones geograficas repetitivas, URLs de prueba/sin valor y redirecciones.
