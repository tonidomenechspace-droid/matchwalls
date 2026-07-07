# Ejecucion - MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-CLEANUP-011G4B2

Fecha: 2026-07-01  
Estado final: CORREGIDO Y VERIFICADO

## Autorizacion

Daniel aprobo exactamente:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-CLEANUP-011G4B2`

## Alcance ejecutado

Escritura Shopify acotada a 1 redirect FR:

- ID: `gid://shopify/UrlRedirect/417581367523`
- Path: `/fr/collections/painted-papers-baller-matchwallswallpapers`
- Target anterior: `/fr/collections/mural-murals-matchwallsmurals`
- Accion: eliminar redirect.

No se modificaron colecciones, productos, paginas, tema, traducciones, handles, canonicals, precios ni inventario. Tampoco se repunto a `/fr/collections/salles-de-bain-peintes`.

## Precheck

Estado previo verificado:

- Admin:
  - El redirect existia.
  - `pathCount`: 1.
  - `targetCount` hacia `/fr/collections/mural-murals-matchwallsmurals`: 1.
  - Redirects FR: 23.
- Publico:
  - `/fr/collections/painted-papers-baller-matchwallswallpapers` -> 301 -> `/fr/collections/mural-murals-matchwallsmurals` -> 404.
  - `/fr/collections/mural-murals-matchwallsmurals` -> 404.
  - `/fr/collections/salles-de-bain-peintes` -> 200, candidata viva pero no usada por falta de equivalencia fiable.

## Backup

Backup previo creado:

- `backup-pre-MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-CLEANUP-011G4B2-2026-07-01.csv`

## Operacion

Mutacion Admin GraphQL validada contra schema y ejecutada:

- `urlRedirectDelete`
- Resultado tecnico Shopify:
  - `deletedUrlRedirectId`: `gid://shopify/UrlRedirect/417581367523`
  - `userErrors: 0`

Nota: `userErrors: 0` solo confirma aceptacion tecnica por Shopify. El cierre depende de las verificaciones posteriores.

## Verificaciones posteriores

Admin:

- El ID eliminado devuelve `null`.
- `pathCount` para `/fr/collections/painted-papers-baller-matchwallswallpapers`: 0.
- `targetCount` hacia `/fr/collections/mural-murals-matchwallsmurals`: 0.
- Redirects FR: 22.

Storefront:

- `/fr/collections/painted-papers-baller-matchwallswallpapers` -> 404 directo.
- `/fr/collections/mural-murals-matchwallsmurals` -> 404.
- `/fr/collections/salles-de-bain-peintes` -> 200 y canonical propio; no se modifico.

Sitemap:

- Archivos leidos: 29.
- URLs leidas: 7.274.
- Errores: 0.
- Fuente eliminada: 0 apariciones.
- Target muerto: 0 apariciones.
- Candidata no usada `/fr/collections/salles-de-bain-peintes`: 1 aparicion.

## Reversion

Solo con aprobacion expresa de Daniel:

- Recrear el redirect con `urlRedirectCreate`:
  - path `/fr/collections/painted-papers-baller-matchwallswallpapers`
  - target `/fr/collections/mural-murals-matchwallsmurals`

No se recomienda revertir salvo decision comercial contraria, porque el target anterior devuelve 404.

## Evidencias

- `backup-pre-MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-CLEANUP-011G4B2-2026-07-01.csv`
- `mutation-results-MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-CLEANUP-011G4B2-2026-07-01.csv`
- `admin-post-MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-CLEANUP-011G4B2-2026-07-01.csv`
- `qa-publico-MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-CLEANUP-011G4B2-2026-07-01.csv`
- `sitemap-MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-CLEANUP-011G4B2-2026-07-01.csv`
