# Ejecucion - MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-REPOINT-PAGE-011G7A1

Fecha: 2026-07-01  
Estado final: CORREGIDO Y VERIFICADO

## Autorizacion

Daniel aprobo exactamente:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-REPOINT-PAGE-011G7A1`

## Alcance ejecutado

Escritura Shopify acotada a 1 redirect:

- ID: `gid://shopify/UrlRedirect/412616229091`
- Path origen: `/products/muestra-desnudos-blanco-y-negro`
- Target anterior: `/collections/muestras`
- Target nuevo: `/pages/muestras`

No se modificaron productos, paginas, colecciones, tema, traducciones, handles, canonicals ni inventario.

## Precheck

- Redirect existente verificado en Admin.
- Pagina destino verificada:
  - ID: `gid://shopify/Page/106299195619`
  - Handle: `muestras`
  - Titulo: `Solicita muestras de papel pintado`
  - Publicada: `true`
- Producto origen verificado:
  - ID: `gid://shopify/Product/8561719247075`
  - Handle: `muestra-desnudos-blanco-y-negro`
  - Estado: `DRAFT`
  - `onlineStoreUrl`: `null`
  - Tipo: `Muestra`

## Backup

Backup previo creado:

- `backup-pre-MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-REPOINT-PAGE-011G7A1-2026-07-01.csv`

## Operacion

Mutacion Admin GraphQL validada contra schema y ejecutada:

- `urlRedirectUpdate`
- Resultado: `userErrors: 0`
- Shopify devolvio:
  - path `/products/muestra-desnudos-blanco-y-negro`
  - target `/pages/muestras`

Nota: `userErrors: 0` solo confirma aceptacion tecnica por Shopify. La correccion se considera cerrada por las verificaciones posteriores.

## Verificaciones posteriores

Admin:

- Redirect target actual: `/pages/muestras`.
- Conteo `path:/products/muestra-desnudos-blanco-y-negro`: 1.
- Conteo `target:/collections/muestras`: 0.
- Conteo `target:/pages/muestras`: 1.

Storefront:

- `/products/muestra-desnudos-blanco-y-negro` -> 301 -> `/pages/muestras` -> 200.
- `/products/muestra-desnudos-blanco-y-negro?mwqa=011g7a1` -> 301 -> `/pages/muestras?mwqa=011g7a1` -> 200.
- `/pages/muestras` -> 200, canonical `https://www.matchwalls.com/pages/muestras`.
- `/collections/muestras` sigue en 404, pero ya no es target activo del redirect corregido.

Sitemap:

- Archivos leidos: 29.
- URLs leidas: 7.274.
- Errores: 0.
- `/products/muestra-desnudos-blanco-y-negro`: 0 apariciones.
- `/pages/muestras`: 1 aparicion.
- `/collections/muestras`: 0 apariciones.

## Reversion

Si Daniel aprueba una reversion especifica, ejecutar `urlRedirectUpdate` sobre el mismo ID:

- ID: `gid://shopify/UrlRedirect/412616229091`
- Path: `/products/muestra-desnudos-blanco-y-negro`
- Target: `/collections/muestras`

No se recomienda revertir salvo que haya una decision comercial contraria, porque el target anterior devuelve 404.

## Evidencias

- `backup-pre-MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-REPOINT-PAGE-011G7A1-2026-07-01.csv`
- `mutation-results-MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-REPOINT-PAGE-011G7A1-2026-07-01.csv`
- `qa-publico-MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-REPOINT-PAGE-011G7A1-2026-07-01.csv`
- `sitemap-MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-REPOINT-PAGE-011G7A1-2026-07-01.csv`
