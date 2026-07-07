# Ejecución MW-INDEXABILITY-REDIRECTS-COLLECTIONS-MURALES-COLLISION-CLEANUP-011F4

Fecha: 2026-06-28  
Estado global: `CORREGIDO Y VERIFICADO`

## Aprobación

`VERIFICADO Y CORRECTO`

Aprobación exacta recibida:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-COLLECTIONS-MURALES-COLLISION-CLEANUP-011F4`

## Alcance ejecutado

`CORREGIDO Y VERIFICADO`

Se eliminó únicamente la redirección Admin conflictiva:

- ID: `gid://shopify/UrlRedirect/1534386274680`.
- Path: `/collections/murales`.
- Target: `/en/collections/all-matchwallsmurals-murals`.

No se modificaron handles, colecciones, traducciones, productos, canonicals, temas, sitemaps ni otros redirects.

## Respaldo previo

`VERIFICADO Y CORRECTO`

Archivo: `backup-pre-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-MURALES-COLLISION-CLEANUP-011F4-2026-06-28.csv`.

Valor eliminado:

- `/collections/murales` -> `/en/collections/all-matchwallsmurals-murals`.

Colección real conservada:

- `gid://shopify/Collection/439953719523`.
- Handle: `murales`.
- Título: `Todos los Papeles Pintados`.
- Productos: 758.
- Publicaciones: 9.

## Operación ejecutada

`CORREGIDO Y VERIFICADO`

Mutación ejecutada: `urlRedirectDelete`.

Resultado Shopify:

- `deletedUrlRedirectId`: `gid://shopify/UrlRedirect/1534386274680`.
- `userErrors`: `[]`.

## Verificación Admin post

`CORREGIDO Y VERIFICADO`

Archivo: `admin-post-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-MURALES-COLLISION-CLEANUP-011F4-2026-06-28.csv`.

Resultados:

- `urlRedirect(id: gid://shopify/UrlRedirect/1534386274680)` devuelve `null`.
- `urlRedirectsCount(query: "path:/collections/murales")` devuelve `0`, precisión `EXACT`.
- La colección real `murales` sigue existiendo con 758 productos y 9 publicaciones.

Observación fuera de alcance:

- `urlRedirectsCount(query: "target:/en/collections/all-matchwallsmurals-murals")` devuelve `8`, precisión `EXACT`.
- Son redirects legacy hacia el handle EN; no se tocaron en 011F4.

## Verificación pública post

`CORREGIDO Y VERIFICADO`

Archivo: `qa-publico-post-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-MURALES-COLLISION-CLEANUP-011F4-2026-06-28.csv`.

Verificado:

- `/collections/murales` devuelve 200 directo.
- Canonical: `https://www.matchwalls.com/collections/murales`.
- H1: `Todos los Papeles Pintados`.
- Sin meta robots `noindex` visible.
- `/en/collections/all-matchwallsmurals-murals` devuelve 200.
- FR/DE/NL localizados devuelven 200 con canonical propio.

## Decisión de no revertir

`VERIFICADO Y CORRECTO`

No se revierte porque:

- La eliminación fue aceptada por Shopify.
- El path conflictivo ya no existe en redirects Admin.
- La colección real `/collections/murales` responde 200 directo.
- La URL EN localizada sigue respondiendo 200.

## Reversión disponible

`VERIFICADO PERO MEJORABLE`

Valor a recrear si Daniel lo pidiera:

- Path: `/collections/murales`.
- Target: `/en/collections/all-matchwallsmurals-murals`.

Mutación de rollback validada previamente: `urlRedirectCreate`.

Limitación: al tratarse de una ruta que colisiona con una colección real, Shopify podría rechazar recrear el redirect. No se recomienda revertir salvo incidencia real.

## Siguiente paso recomendado

`REQUIERE DECISION HUMANA`

Preparado siguiente lote:

`MW-INDEXABILITY-REDIRECTS-COLLECTIONS-PAPELES-CONSOLIDATION-011F5`

Objetivo: consolidar `/collections/papeles-pintados` para que apunte directamente a `/collections/murales`, ahora que `path:/collections/murales = 0`.
