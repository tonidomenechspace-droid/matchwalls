# Diagnostico MW-INDEXABILITY-REDIRECTS-FR-CHAINS-DIAG-011G4

Fecha: 2026-06-29  
Tipo: diagnostico de solo lectura  
Estado final: VERIFICADO PERO MEJORABLE  

## 1. Alcance

Diagnostico acotado de redirects de idioma tras la limpieza 011G3A:

- FR prioritario: alcance principal.
- EN: contexto, por estar en el bloque anterior.
- AR: contexto y STANDBY, fuera de idiomas prioritarios actuales.

No se modifico Shopify. No se cambiaron redirects, handles, colecciones, productos, paginas, canonicals, sitemaps, tema ni contenido visible.

## 2. Estado Admin Shopify comprobado

Consulta GraphQL de lectura validada contra schema antes de ejecutarse.

Resultado actual:

- Total redirects Shopify: 614 EXACT.
- `/fr/*`: 23 redirects.
- `/en/*`: 2 redirects.
- `/ar/*`: 4 redirects.

Archivo:

- `admin-fr-en-ar-MW-INDEXABILITY-REDIRECTS-FR-CHAINS-DIAG-011G4-2026-06-29.csv`

## 3. Verificacion publica

Archivo:

- `qa-publico-fr-en-ar-MW-INDEXABILITY-REDIRECTS-FR-CHAINS-DIAG-011G4-2026-06-29.csv`

Resumen:

| Idioma | Redirects revisados | Cadenas de mas de 1 salto | Fuentes que terminan en 404 | Targets que terminan en 404 | Estado |
|---|---:|---:|---:|---:|---|
| FR | 23 | 12 | 1 | 1 | VERIFICADO PERO MEJORABLE / INCORRECTO |
| EN | 2 | 0 | 0 | 0 | VERIFICADO Y CORRECTO |
| AR | 4 | 1 | 1 | 1 | STANDBY |

## 4. Sitemap exacto

Archivo:

- `qa-sitemap-fr-MW-INDEXABILITY-REDIRECTS-FR-CHAINS-DIAG-011G4-2026-06-29.csv`

Resultado FR:

- 23 fuentes FR: 0 coincidencias exactas en sitemap.
- 23 targets actuales FR: 0 coincidencias exactas en sitemap.
- 16 destinos finales FR unicos: 0 coincidencias exactas en sitemap.

Interpretacion:

- No hay exposicion directa detectada en sitemap para este bloque.
- El problema principal no es sitemap, sino calidad tecnica de redirects: cadenas y un destino muerto.

## 5. Clasificacion

Archivo:

- `clasificacion-MW-INDEXABILITY-REDIRECTS-FR-CHAINS-DIAG-011G4-2026-06-29.csv`

Resultado:

- FR: 12 redirects `VERIFICADO PERO MEJORABLE` por cadena `301 -> 301 -> 200`.
- FR: 1 redirect `INCORRECTO` por terminar en `404`.
- FR: 10 redirects `VERIFICADO Y CORRECTO` por ser `301 -> 200`.
- EN: 2 redirects `VERIFICADO Y CORRECTO`.
- AR: 4 redirects `STANDBY`.

## 6. Candidatos a consolidacion FR

Los 12 redirects FR con cadena multiple pueden consolidarse actualizando el target al destino final 200 ya verificado.

No implica:

- Cambiar handles.
- Renombrar colecciones.
- Modificar contenido FR.
- Cambiar sitemaps.
- Crear o eliminar redirects.

Siguiente propuesta preparada:

`MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A`

## 7. Caso FR incorrecto excluido

Redirect FR que termina en 404:

- ID: `gid://shopify/UrlRedirect/417581367523`
- Path: `/fr/collections/painted-papers-baller-matchwallswallpapers`
- Target actual: `/fr/collections/mural-murals-matchwallsmurals`
- Resultado publico: `301 -> 404`

Estado: INCORRECTO.

No se propone corregirlo automaticamente porque no se ha verificado una coleccion FR equivalente real. Requiere un lote de decision separado:

`MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-DECISION-011G4B`

## 8. EN y AR

EN:

- 2/2 redirects verificados como `301 -> 200`.
- Estado: VERIFICADO Y CORRECTO.
- Sin accion recomendada ahora.

AR:

- 1 redirect termina en 404.
- 1 redirect tiene cadena multiple y cruce hacia EN.
- AR no esta dentro de idiomas prioritarios actuales.
- Estado: STANDBY.
- No tocar sin politica internacional o aprobacion expresa.

## 9. Conclusion

Estado final: VERIFICADO PERO MEJORABLE.

El siguiente paso recomendado es proponer la consolidacion quirurgica de los 12 redirects FR con cadena multiple:

`MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A`

