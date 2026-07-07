# Ejecucion de lote: MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-CLEANUP-011G3A

Fecha: 2026-06-29  
Estado final: CORREGIDO Y VERIFICADO  
Autorizacion recibida: `APROBADO LOTE MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-CLEANUP-011G3A`

## 1. Alcance ejecutado

Se eliminaron exclusivamente 6 redirecciones de producto que estaban verificadas como redirecciones hacia destinos 404.

No se modificaron:

- Productos.
- Handles.
- Colecciones.
- Paginas.
- Sitemaps.
- Tema Shopify.
- Redirect de muestra en STANDBY.

## 2. Precheck inmediato

Antes de ejecutar:

- Total de redirects Shopify: 620 EXACT.
- Los 6 redirects candidatos existian y coincidian exactamente con la propuesta.
- El redirect excluido `gid://shopify/UrlRedirect/412616229091` seguia existiendo:
  - Path: `/products/muestra-desnudos-blanco-y-negro`
  - Target: `/collections/muestras`
  - Estado: STANDBY.

## 3. Operaciones ejecutadas

Mutacion validada y ejecutada secuencialmente:

`urlRedirectDelete(id: ID!)`

Resultados:

| Orden | ID eliminado | Path | Target anterior | Resultado |
|---|---|---|---|---|
| 1 | `gid://shopify/UrlRedirect/408237834467` | `/products/poster-de-papel-mate-calidad-museo-con-marco-de-madera` | `/products/echoing-corridor-3` | `userErrors: []` |
| 2 | `gid://shopify/UrlRedirect/408370151651` | `/products/endless-horizon-3` | `/products/echoing-corridor` | `userErrors: []` |
| 3 | `gid://shopify/UrlRedirect/408474484963` | `/products/rusted-horizon-marron-copia` | `/products/ember-glow-marron` | `userErrors: []` |
| 4 | `gid://shopify/UrlRedirect/408525930723` | `/products/urban-geometrico` | `/products/urban-geometrico-beige` | `userErrors: []` |
| 5 | `gid://shopify/UrlRedirect/408525996259` | `/products/urban-geometrico-beige-copia` | `/products/urban-geometrico-gris` | `userErrors: []` |
| 6 | `gid://shopify/UrlRedirect/408514429155` | `/products/urban-sketch-beige-copia` | `/products/melodic-flow` | `userErrors: []` |

## 4. Postcheck Admin

Resultado:

- Total de redirects Shopify: 614 EXACT.
- Los 6 IDs eliminados devuelven `null`.
- Los 6 paths eliminados devuelven 0 redirects.
- El redirect de muestra en STANDBY sigue intacto:
  - `gid://shopify/UrlRedirect/412616229091`
  - `/products/muestra-desnudos-blanco-y-negro` -> `/collections/muestras`

Archivo:

- `admin-post-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-CLEANUP-011G3A-2026-06-29.csv`

## 5. Postcheck publico

Resultado:

- Las 6 URLs fuente responden 404 directo.
- Las 6 URLs fuente ya no presentan redireccion.
- Los 6 targets siguen respondiendo 404 directo.
- No se detectaron errores de solicitud.

Archivo:

- `qa-publico-post-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-CLEANUP-011G3A-2026-06-29.csv`

## 6. Postcheck sitemap

Resultado:

- 29 sitemaps hijo revisados.
- 0 coincidencias exactas para las 6 fuentes.
- 0 coincidencias exactas para los 6 targets.

Archivo:

- `qa-sitemap-exact-post-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-CLEANUP-011G3A-2026-06-29.csv`

## 7. Respaldo y reversion

Backup previo:

- `backup-pre-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-CLEANUP-011G3A-2026-06-29.csv`

Metodo de reversion:

- Recrear con `urlRedirectCreate` cada redirect usando el mismo `path` y `target` del backup.
- Shopify asignaria IDs nuevos; la reversion funcional se verificaria por `path` y `target`.

## 8. Incidencias

- Sin incidencias en Shopify.
- Primer intento local de QA publico fallo por libreria HTTP no cargada en PowerShell; se repitio cargando `System.Net.Http` y el QA publico quedo verificado.

## 9. Resultado final

CORREGIDO Y VERIFICADO.

