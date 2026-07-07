# Ejecucion - MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-SAFE-CLEANUP-011G7B1

Fecha: 2026-07-01  
Estado final: CORREGIDO Y VERIFICADO

## Autorizacion

Daniel aprobo exactamente:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-SAFE-CLEANUP-011G7B1`

## Alcance ejecutado

Escritura Shopify acotada a 5 redirects:

1. Actualizado:
   - ID: `gid://shopify/UrlRedirect/405254897891`
   - Path: `/collections/kids`
   - Target anterior: `/collections/kids-rollos`
   - Target nuevo: `/collections/kids-murales`
2. Eliminados:
   - `gid://shopify/UrlRedirect/408478843107` - `/collections/patrones-grandes-rollos` -> `/collections/papel-pintado-estampado-grande`
   - `gid://shopify/UrlRedirect/408478974179` - `/collections/semi-lisos-rollos` -> `/collections/semi-lisos-papel-pintado`
   - `gid://shopify/UrlRedirect/408479006947` - `/collections/moderno-rollos` -> `/collections/moderno-papel-pintado`
   - `gid://shopify/UrlRedirect/408719425763` - `/collections/lienzos-artista` -> `/collections/lienzos-abstractos`

No se modificaron colecciones, productos, paginas, tema, traducciones, handles, canonicals, precios ni inventario.

## Precheck

- Los 5 redirects existian y coincidian exactamente con el diagnostico 011G7B.
- La coleccion `/collections/kids-murales` existe en Admin:
  - ID: `gid://shopify/Collection/436916191459`
  - Titulo: `Papeles Pintados Para Habitaciones Infantiles`
  - Productos: 294

## Backup

Backup previo creado:

- `backup-pre-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-SAFE-CLEANUP-011G7B1-2026-07-01.csv`

## Operacion

Mutacion Admin GraphQL validada contra schema y ejecutada:

- `urlRedirectUpdate`: 1/1 correcto.
- `urlRedirectDelete`: 4/4 correctos.
- Resultado tecnico Shopify: `userErrors: 0` en las 5 operaciones.

Nota: `userErrors: 0` solo confirma aceptacion tecnica por Shopify. El cierre depende de las verificaciones posteriores.

## Verificaciones posteriores

Admin:

- `gid://shopify/UrlRedirect/405254897891` devuelve:
  - path `/collections/kids`
  - target `/collections/kids-murales`
- Los 4 IDs eliminados devuelven `null`.
- Conteo de redirects hacia los 4 targets muertos eliminados: 0.
- Existe otro redirect previo hacia `/collections/kids-murales`:
  - `gid://shopify/UrlRedirect/417318404323`
  - `/collections/papeles-pintados-infantiles` -> `/collections/kids-murales`
  - No se modifico porque queda fuera del alcance aprobado.

Storefront:

- `/collections/kids` -> 301 -> `/collections/kids-murales` -> 200.
- `/collections/kids-murales` -> 200, canonical `https://www.matchwalls.com/collections/kids-murales`.
- Las 4 fuentes eliminadas devuelven 404 directo:
  - `/collections/patrones-grandes-rollos`
  - `/collections/semi-lisos-rollos`
  - `/collections/moderno-rollos`
  - `/collections/lienzos-artista`
- Los 4 antiguos targets muertos siguen en 404, pero ya no reciben esos redirects.

Sitemap:

- Archivos leidos: 29.
- URLs leidas: 7.274.
- Errores: 0 en lectura repetida.
- `/collections/kids-murales`: 1 aparicion.
- Todas las fuentes antiguas y targets muertos comprobados: 0 apariciones.

Incidencias:

- Primera lectura de sitemap tuvo 1 fallo transitorio y 7.262 URLs leidas. Se repitio con detalle: 29 archivos, 7.274 URLs y 0 errores. No se considera incidencia activa del lote.

## Reversion

Solo con aprobacion expresa de Daniel:

- Revertir `/collections/kids` con `urlRedirectUpdate` al target anterior `/collections/kids-rollos`.
- Recrear los 4 redirects eliminados con `urlRedirectCreate` usando los valores del backup.

No se recomienda revertir salvo decision comercial contraria, porque los targets anteriores devuelven 404.

## Evidencias

- `backup-pre-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-SAFE-CLEANUP-011G7B1-2026-07-01.csv`
- `mutation-results-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-SAFE-CLEANUP-011G7B1-2026-07-01.csv`
- `admin-post-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-SAFE-CLEANUP-011G7B1-2026-07-01.csv`
- `qa-publico-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-SAFE-CLEANUP-011G7B1-2026-07-01.csv`
- `sitemap-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-SAFE-CLEANUP-011G7B1-2026-07-01.csv`
