# Diagnostico - MW-INDEXABILITY-SAMPLES-ADMIN-SEOHIDDEN-DIAG-011B3

Fecha/hora: 2026-06-27  
Estado: `VERIFICADO Y CORRECTO`

## Alcance

- Lote: `MW-INDEXABILITY-SAMPLES-ADMIN-SEOHIDDEN-DIAG-011B3`.
- Tipo: lectura Admin Shopify, sin escritura.
- Recursos: 10 productos candidatos del piloto generado en `011B2`.
- Escritura en Shopify: no realizada.
- Mutaciones: no ejecutadas.

## Metodo

Se uso Shopify Admin GraphQL en modo solo lectura.

Consulta validada antes de ejecutar:

- `ProductSeoHiddenPilot`.
- Scope requerido por validacion: `read_products`.

Campos leidos:

- `id`.
- `legacyResourceId`.
- `title`.
- `handle`.
- `status`.
- `productType`.
- `vendor`.
- `templateSuffix`.
- `publishedAt`.
- `onlineStoreUrl`.
- `totalInventory`.
- `tracksInventory`.
- `seo.title`.
- `seo.description`.
- `metafield(namespace: "seo", key: "hidden")`.

## Resultado

`VERIFICADO Y CORRECTO`

Los 10 productos candidatos:

- Existen en Admin.
- Estan `ACTIVE`.
- Estan publicados en Online Store.
- Usan `templateSuffix = muestra`.
- Tienen `productType = Muestra`.
- Tienen `tracksInventory = false`.
- Tienen `totalInventory = 0`.
- Tienen `seo.title = null`.
- Tienen `seo.description = null`.
- Tienen `seo.hidden = null`.

## Valores actuales

Archivo de evidencia:

- `admin-seohidden-lectura-piloto-MW-INDEXABILITY-SAMPLES-ADMIN-SEOHIDDEN-DIAG-011B3-2026-06-27.csv`.

## Implicacion para 011B4

`REQUIERE DECISION HUMANA`

Como `seo.hidden` es `null` en los 10 productos, el cambio propuesto para el piloto seria crear el metafield:

- namespace: `seo`
- key: `hidden`
- value: `1`
- type: `number_integer`

Rollback exacto:

- borrar `seo.hidden` de esos mismos productos para volver al estado original `null`.

## Advertencia operativa

Shopify documenta que `seo.hidden=1` oculta el recurso de buscadores/sitemap y tambien de la busqueda interna de la tienda. Este impacto debe aceptarse para el piloto.

## Estado final

`VERIFICADO Y CORRECTO`

011B3 queda cerrado. No se modifico Shopify.

