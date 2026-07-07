# Ejecucion de lote: MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A

Fecha: 2026-06-29  
Estado final: CORREGIDO Y VERIFICADO  
Autorizacion recibida: `APROBADO LOTE MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A`

## 1. Alcance ejecutado

Se actualizaron exclusivamente 12 redirects FR que antes hacian cadena `301 -> 301 -> 200`.

No se modificaron:

- Handles.
- Colecciones.
- Productos.
- Paginas.
- Sitemaps.
- Canonicals.
- Tema Shopify.
- Redirects EN.
- Redirects AR.
- El redirect FR que termina en 404.

## 2. Precheck

Antes de ejecutar:

- Total redirects Shopify: 614 EXACT.
- Los 12 IDs existian.
- Los 12 `path` y `target` actuales coincidian con el backup previo.
- El redirect FR 404 excluido seguia intacto:
  - `gid://shopify/UrlRedirect/417581367523`
  - `/fr/collections/painted-papers-baller-matchwallswallpapers`
  - `/fr/collections/mural-murals-matchwallsmurals`

## 3. Operacion ejecutada

Mutacion validada contra schema Shopify:

`urlRedirectUpdate(id: ID!, urlRedirect: UrlRedirectInput!)`

Ejecucion secuencial, un redirect cada vez.

Resultado:

- 12/12 updates ejecutados.
- 12/12 con `userErrors: []`.
- 0 errores Shopify.

Archivo:

- `mutation-results-MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A-2026-06-29.csv`

## 4. Postcheck Admin

Resultado:

- Total redirects Shopify: 614 EXACT.
- 12/12 IDs siguen existiendo.
- 12/12 targets coinciden con el destino propuesto.
- El redirect FR 404 excluido sigue intacto.

Archivo:

- `admin-post-MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A-2026-06-29.csv`

## 5. Postcheck publico

Resultado:

- 12/12 fuentes responden `301 -> 200`.
- 0/12 fuentes mantienen cadena multiple.
- 0/12 fuentes terminan en 404.
- 12/12 targets nuevos responden 200.
- 0 errores de solicitud.

Archivo:

- `qa-publico-post-MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A-2026-06-29.csv`

## 6. Postcheck sitemap

Resultado:

- 12 fuentes: 0 coincidencias exactas en sitemap.
- 12 targets antiguos: 0 coincidencias exactas en sitemap.
- 12 targets nuevos: 0 coincidencias exactas en sitemap.

Archivo:

- `qa-sitemap-post-MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A-2026-06-29.csv`

## 7. Reversion disponible

Backup previo:

- `backup-pre-MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A-2026-06-29.csv`

Metodo de reversion:

- Ejecutar `urlRedirectUpdate` por cada ID.
- Mantener el mismo `path`.
- Restaurar el `target` anterior desde el backup.

## 8. Incidencias

- Sin incidencias Shopify.
- Sin errores publicos en el QA post.
- Nota: algunos handles finales FR siguen siendo linguisticamente mejorables; no se han cambiado en este lote porque el alcance era solo consolidar cadenas.

## 9. Resultado final

CORREGIDO Y VERIFICADO.

