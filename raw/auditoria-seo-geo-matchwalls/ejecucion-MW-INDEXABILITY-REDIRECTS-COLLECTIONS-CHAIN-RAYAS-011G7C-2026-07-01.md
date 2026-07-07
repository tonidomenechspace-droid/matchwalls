# Ejecucion - MW-INDEXABILITY-REDIRECTS-COLLECTIONS-CHAIN-RAYAS-011G7C

Fecha: 2026-07-01  
Estado final: CORREGIDO Y VERIFICADO

## Autorizacion

Daniel aprobo exactamente:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-COLLECTIONS-CHAIN-RAYAS-011G7C`

## Alcance ejecutado

Escritura Shopify acotada a 1 redirect:

- ID: `gid://shopify/UrlRedirect/408478908643`
- Path: `/collections/rayas-rollos`
- Target anterior: `/collections/papel-pintado-rayas`
- Target nuevo: `/collections/murales-estilo-a-rayas`

No se modificaron colecciones, productos, paginas, tema, traducciones, handles, canonicals, precios ni inventario.

## Precheck

Estado previo verificado en Admin:

- Redirect fuente:
  - `gid://shopify/UrlRedirect/408478908643`
  - `/collections/rayas-rollos` -> `/collections/papel-pintado-rayas`
- Redirect intermedio existente:
  - `gid://shopify/UrlRedirect/417542537443`
  - `/collections/papel-pintado-rayas` -> `/collections/murales-estilo-a-rayas`
- Coleccion destino final:
  - `gid://shopify/Collection/439174496483`
  - handle `murales-estilo-a-rayas`
  - titulo `Papel Pintado Rayas`
  - 87 productos
- No existe coleccion Admin con handle `papel-pintado-rayas`; era un redirect intermedio, no una coleccion canonica.

## Backup

Backup previo creado:

- `backup-pre-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-CHAIN-RAYAS-011G7C-2026-07-01.csv`

## Operacion

Mutacion Admin GraphQL validada contra schema y ejecutada:

- `urlRedirectUpdate`
- Resultado tecnico Shopify: `userErrors: 0`
- Shopify devolvio:
  - path `/collections/rayas-rollos`
  - target `/collections/murales-estilo-a-rayas`

Nota: `userErrors: 0` solo confirma aceptacion tecnica por Shopify. El cierre depende de las verificaciones posteriores.

## Verificaciones posteriores

Admin:

- `gid://shopify/UrlRedirect/408478908643` devuelve:
  - path `/collections/rayas-rollos`
  - target `/collections/murales-estilo-a-rayas`
- Conteo `target:/collections/papel-pintado-rayas`: 0.
- El redirect intermedio `/collections/papel-pintado-rayas -> /collections/murales-estilo-a-rayas` sigue existiendo para trafico directo antiguo y no se modifico.

Storefront:

- `/collections/rayas-rollos` -> 301 -> `/collections/murales-estilo-a-rayas` -> 200.
- `/collections/papel-pintado-rayas` -> 301 -> `/collections/murales-estilo-a-rayas` -> 200.
- `/collections/murales-estilo-a-rayas` -> 200.
- Canonical final: `https://www.matchwalls.com/collections/murales-estilo-a-rayas`.

Sitemap:

- Archivos leidos: 29.
- URLs leidas: 7.274.
- Errores: 0.
- `/collections/rayas-rollos`: 0 apariciones.
- `/collections/papel-pintado-rayas`: 0 apariciones.
- `/collections/murales-estilo-a-rayas`: 1 aparicion.

## Reversion

Solo con aprobacion expresa de Daniel:

- Ejecutar `urlRedirectUpdate` sobre `gid://shopify/UrlRedirect/408478908643`.
- Restaurar target anterior: `/collections/papel-pintado-rayas`.

No se recomienda revertir salvo decision comercial contraria, porque el estado corregido reduce una cadena de redireccion.

## Evidencias

- `backup-pre-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-CHAIN-RAYAS-011G7C-2026-07-01.csv`
- `mutation-results-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-CHAIN-RAYAS-011G7C-2026-07-01.csv`
- `admin-post-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-CHAIN-RAYAS-011G7C-2026-07-01.csv`
- `qa-publico-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-CHAIN-RAYAS-011G7C-2026-07-01.csv`
- `sitemap-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-CHAIN-RAYAS-011G7C-2026-07-01.csv`
