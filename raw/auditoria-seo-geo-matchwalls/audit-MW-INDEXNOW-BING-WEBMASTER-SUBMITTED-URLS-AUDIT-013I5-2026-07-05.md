# MW-INDEXNOW-BING-WEBMASTER-SUBMITTED-URLS-AUDIT-013I5

Fecha: 2026-07-05  
Modo: solo lectura.  
Estado final: `VERIFICADO PERO MEJORABLE`.

## Objetivo

Auditar las URLs exportadas desde Bing Webmaster Tools > IndexNow para comprobar si son canónicas, valiosas y coherentes con la política de indexación de MatchWalls.

## Archivo recibido

`VERIFICADO Y CORRECTO`

Archivo aportado por Daniel:

- `C:\Users\d.bermejo\OneDrive - Matchwalls\Escritorio\matchwalls.com_IndexNowSubmittedUrls_7_5_2026 AAAAAAAA.csv`

Contenido real del CSV:

- 3 filas de URLs.

Nota crítica: Bing Webmaster Tools mostraba `Submitted URLs: 13`, pero el CSV exportado contiene solo 3 filas. Por tanto, esta auditoría cubre el 100% del archivo recibido, no el 100% del total indicado por Bing.

## URLs auditadas

### 1. `https://www.matchwalls.com/`

`CORREGIDO Y VERIFICADO`

- Source CSV: `none` / en pantalla Bing aparecía como `Self`.
- Submitted: `07/05/2026T01:02:00-07:00`.
- HTTP: `200`.
- Canonical: `https://www.matchwalls.com/`.
- Robots meta: no se detecta `noindex`.
- Title: `MatchWalls - Papeles pintados que transforman tus espacios`.

Conclusión: URL canónica, indexable y valiosa. Correcta para IndexNow.

### 2. `https://www.matchwalls.com/products/custom-file-uploader`

`VERIFICADO PERO MEJORABLE`

- Source CSV: `shopify`.
- Submitted: `06/15/2026T13:52:00-07:00`.
- HTTP: `200`.
- Canonical: `https://www.matchwalls.com/products/custom-file-uploader`.
- Robots meta: `noindex,nofollow`.
- Title: `Papel pintado y mural personalizado | MatchWalls`.

Conclusión: URL histórica enviada por Shopify, pero actualmente marcada como `noindex,nofollow`. No debe enviarse manualmente ni formar parte de una whitelist IndexNow futura. No requiere acción urgente si no está indexada, porque el `noindex` actual ya comunica exclusión a buscadores.

### 3. `https://www.matchwalls.com/products/bambuze-negro`

`VERIFICADO Y CORRECTO`

- Source CSV: `shopify`.
- Submitted: `06/15/2026T05:49:00-07:00`.
- HTTP: `200`.
- Canonical: `https://www.matchwalls.com/products/bambuze-negro`.
- Robots meta: no se detecta `noindex`.
- Title: `Papel Pintado Bambúze Negro`.

Conclusión: producto canónico e indexable. A priori válido para IndexNow.

## Clasificación general

`VERIFICADO PERO MEJORABLE`

De las 3 URLs exportadas:

- Correctas / indexables: 2
  - `https://www.matchwalls.com/`
  - `https://www.matchwalls.com/products/bambuze-negro`
- No apta para envío futuro manual: 1
  - `https://www.matchwalls.com/products/custom-file-uploader`

## Discrepancia pendiente

`INCOMPLETO`

Bing muestra `13` submitted URLs, pero el CSV recibido contiene `3`. Faltan 10 URLs por auditar.

Posibles causas:

- export limitado a filas visibles;
- filtro activo;
- paginación;
- descarga parcial;
- comportamiento de Bing Webmaster Tools.

## Recomendación

`REQUIERE DECISION HUMANA`

No usar Manual submissions todavía.

Siguiente paso recomendado:

`MW-INDEXNOW-BING-WEBMASTER-SUBMITTED-URLS-FULL-EXPORT-013I5B`

Objetivo:

1. conseguir la lista completa de las 13 URLs;
2. confirmar si hay paginación/filtros;
3. auditar las 10 URLs restantes;
4. decidir si hay que excluir, ignorar histórico o tomar alguna acción sobre URLs noindex.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó Bing, Shopify, IndexNow, app, URLs, settings ni sitemap. No se enviaron URLs manualmente.
