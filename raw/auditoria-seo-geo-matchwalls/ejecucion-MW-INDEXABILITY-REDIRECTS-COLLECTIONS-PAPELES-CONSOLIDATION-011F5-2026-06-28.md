# Ejecución MW-INDEXABILITY-REDIRECTS-COLLECTIONS-PAPELES-CONSOLIDATION-011F5

Fecha: 2026-06-28  
Estado global: `CORREGIDO Y VERIFICADO`

## Aprobación

`VERIFICADO Y CORRECTO`

Aprobación exacta recibida:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-COLLECTIONS-PAPELES-CONSOLIDATION-011F5`

## Alcance ejecutado

`CORREGIDO Y VERIFICADO`

Se actualizó únicamente 1 redirección Shopify Admin:

- ID: `gid://shopify/UrlRedirect/410027000035`.
- Path: `/collections/papeles-pintados`.
- Target anterior: `/collections/papeles-pintados-old`.
- Target nuevo: `/collections/murales`.

No se eliminaron redirecciones. No se cambiaron handles, colecciones, traducciones, productos, canonicals, temas, sitemaps ni contenido visible.

## Dependencia verificada

`CORREGIDO Y VERIFICADO`

Antes de ejecutar:

- `path:/collections/murales = 0`, precisión `EXACT`.
- Colección real `murales` intacta:
  - `gid://shopify/Collection/439953719523`.
  - 758 productos.
  - 9 publicaciones.
  - `seo.hidden = null`.

## Respaldo previo

`VERIFICADO Y CORRECTO`

Archivo: `backup-pre-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-PAPELES-CONSOLIDATION-011F5-2026-06-28.csv`.

Valor original para reversión:

- `gid://shopify/UrlRedirect/410027000035`: `/collections/papeles-pintados` -> `/collections/papeles-pintados-old`.

Recurso conservado:

- `gid://shopify/UrlRedirect/417318207715`: `/collections/papeles-pintados-old` -> `/collections/murales`.

## Operación ejecutada

`CORREGIDO Y VERIFICADO`

Mutación ejecutada: `urlRedirectUpdate`.

Input:

- ID: `gid://shopify/UrlRedirect/410027000035`.
- Path: `/collections/papeles-pintados`.
- Target: `/collections/murales`.

Resultado Shopify:

- `userErrors = []`.
- Readback Admin confirma target nuevo.

## Verificación Admin post

`CORREGIDO Y VERIFICADO`

Archivo: `admin-post-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-PAPELES-CONSOLIDATION-011F5-2026-06-28.csv`.

Resultados:

- `/collections/papeles-pintados` -> `/collections/murales`.
- `/collections/papeles-pintados-old` -> `/collections/murales`.
- `path:/collections/murales = 0`, precisión `EXACT`.
- Colección `murales` intacta.

## Verificación pública post

`CORREGIDO Y VERIFICADO`

Archivo: `qa-publico-post-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-PAPELES-CONSOLIDATION-011F5-2026-06-28.csv`.

Verificado por HTTP:

- `/collections/papeles-pintados` devuelve 301 -> `/collections/murales` -> 200.
- `/collections/papeles-pintados-old` devuelve 301 -> `/collections/murales` -> 200.
- `/collections/murales` devuelve 200 directo.
- `/collections/murales-mvp` devuelve 301 -> `/collections/murales` -> 200.
- `/collections/%20papeles-pintados` devuelve 301 -> `/collections/murales` -> 200.
- Canonical final: `https://www.matchwalls.com/collections/murales`.
- H1 final: `Todos los Papeles Pintados`.
- Sin meta robots `noindex` visible.

## Efecto conseguido

`CORREGIDO Y VERIFICADO`

La cadena principal:

`/collections/papeles-pintados` -> `/collections/papeles-pintados-old` -> `/collections/murales`

queda consolidada a:

`/collections/papeles-pintados` -> `/collections/murales`

El recurso intermedio se conserva para enlaces históricos directos:

`/collections/papeles-pintados-old` -> `/collections/murales`.

## Reversión disponible

`VERIFICADO Y CORRECTO`

Si fuera necesario revertir:

- Ejecutar `urlRedirectUpdate` sobre `gid://shopify/UrlRedirect/410027000035`.
- Restaurar target: `/collections/papeles-pintados-old`.

No se recomienda revertir salvo incidencia pública real.

## Siguiente paso recomendado

`REQUIERE DECISION HUMANA`

Diagnóstico propuesto:

`MW-INDEXABILITY-REDIRECTS-COLLECTIONS-LEGACY-DEPENDENTS-DIAG-011F6`

Objetivo: decidir si mantener, consolidar o documentar como legacy los redirects restantes:

- `/collections/murales-mvp` -> `/collections/murales`.
- `/collections/%20papeles-pintados` -> `/collections/murales`.
- 8 redirects legacy hacia `/en/collections/all-matchwallsmurals-murals`.
