# Ejecución MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1

Fecha: 2026-06-29  
Estado final: `CORREGIDO Y VERIFICADO`  
Tipo: eliminación acotada de redirects Admin obsoletos

## Aprobación y alcance

`CORREGIDO Y VERIFICADO`

Aprobación exacta recibida:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1`

Alcance ejecutado:

- Eliminación de 14 objetos `UrlRedirect` en Shopify Admin.
- No se modificaron colecciones.
- No se modificaron handles.
- No se modificaron productos.
- No se modificaron páginas.
- No se modificó sitemap manualmente.
- No se modificaron canonicals.
- No se modificó tema Shopify.
- No se modificó contenido visible.

## Respaldo previo

`VERIFICADO Y CORRECTO`

Archivo:

- `backup-pre-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`

Contiene los IDs, paths y targets originales necesarios para reversión.

## Precheck Admin

`VERIFICADO Y CORRECTO`

Antes de ejecutar:

- Los 14 redirects existían con los IDs esperados.
- Total redirects Admin: 634.
- Precisión: `EXACT`.

## Operación ejecutada

`CORREGIDO Y VERIFICADO`

Mutación ejecutada secuencialmente, una vez por ID:

```graphql
mutation DeleteOneUrlRedirect011G1($id: ID!) {
  urlRedirectDelete(id: $id) {
    deletedUrlRedirectId
    userErrors {
      field
      message
    }
  }
}
```

Resultado:

- 14/14 redirects eliminados.
- 14/14 con `userErrors: []`.

Archivo:

- `mutation-results-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`

IDs eliminados:

- `gid://shopify/UrlRedirect/417542766819`
- `gid://shopify/UrlRedirect/417542799587`
- `gid://shopify/UrlRedirect/417542832355`
- `gid://shopify/UrlRedirect/417542865123`
- `gid://shopify/UrlRedirect/417542897891`
- `gid://shopify/UrlRedirect/417542930659`
- `gid://shopify/UrlRedirect/417542963427`
- `gid://shopify/UrlRedirect/417542996195`
- `gid://shopify/UrlRedirect/417543028963`
- `gid://shopify/UrlRedirect/417543061731`
- `gid://shopify/UrlRedirect/417543094499`
- `gid://shopify/UrlRedirect/417543127267`
- `gid://shopify/UrlRedirect/417543160035`
- `gid://shopify/UrlRedirect/417543192803`

## Postcheck Admin

`CORREGIDO Y VERIFICADO`

Archivo:

- `admin-post-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`

Resultado:

- 14/14 IDs eliminados devuelven `null`.
- 14/14 paths fuente tienen `urlRedirectsCount = 0`, precisión `EXACT`.
- Total redirects Admin: 620.
- Precisión: `EXACT`.

## Postcheck público

`CORREGIDO Y VERIFICADO`

Archivo:

- `qa-publico-post-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`

Resultado para las 14 fuentes `/collections/papeles-pintados-color-*`:

- 14/14 devuelven `200`.
- 14/14 cargan con `0` saltos.
- 14/14 mantienen canonical propio.
- 14/14 tienen H1 visible.
- 14/14 sin `noindex` visible en meta robots ni `X-Robots-Tag`.

Resultado para los 14 targets antiguos:

- 14/14 siguen devolviendo `404`.
- Esto es esperado: el lote eliminó redirects Admin inertes, no creó nuevos destinos.

## Postcheck sitemap

`CORREGIDO Y VERIFICADO`

Archivos:

- `qa-sitemap-exact-post-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`
- `qa-sitemap-es-exact-post-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`

Resultado limpio en sitemap de colecciones ES:

- 14/14 fuentes siguen en sitemap ES exacto.
- 14/14 targets antiguos no están en sitemap ES exacto.

Nota:

- Una comprobación amplia inicial encontró timeout en un sitemap de colecciones IT no relacionado con este lote. Se reejecutó la verificación acotada al sitemap de colecciones ES y quedó correcta.

## Efecto conseguido

`CORREGIDO Y VERIFICADO`

Se han retirado 14 redirects Admin obsoletos/inertes que apuntaban a targets `404`, sin afectar las colecciones públicas reales.

Antes:

- Existían redirects Admin para paths de colecciones ES reales.
- Las fuentes cargaban `200`, pero los targets configurados en Admin eran `404`.

Después:

- No quedan redirects Admin para esos 14 paths.
- Las 14 colecciones públicas siguen cargando `200` directo.
- Los targets antiguos `404` no aparecen en sitemap ES.

## Reversión disponible

`VERIFICADO Y CORRECTO`

Si fuera necesario revertir:

- Usar `urlRedirectCreate` con los valores del backup:
  - `path`
  - `target`

Mutación validada en la propuesta:

```graphql
mutation RestoreOneUrlRedirect011G1($path: String!, $target: String!) {
  urlRedirectCreate(urlRedirect: {path: $path, target: $target}) {
    urlRedirect {
      id
      path
      target
    }
    userErrors {
      field
      message
    }
  }
}
```

Los IDs nuevos no serían necesariamente iguales a los eliminados.

## Archivos de evidencia

- `propuesta-lote-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.md`
- `backup-pre-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`
- `mutation-results-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`
- `admin-post-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`
- `qa-publico-post-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`
- `qa-sitemap-exact-post-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`
- `qa-sitemap-es-exact-post-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`

## Siguiente paso recomendado

`REQUIERE DECISION HUMANA`

Continuar con el siguiente bloque de redirects, pero no mezclarlo con esta ejecución ya cerrada.

Prioridad sugerida:

`MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3`

Motivo: ya hay 7 fuentes verificadas que redirigen a `404`, y requiere decidir si se eliminan o se repuntan a sustitutos reales.
