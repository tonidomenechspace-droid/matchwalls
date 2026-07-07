# QA MW-BING-WEBMASTER-AI-PERFORMANCE-EXPORT-QA-013E4 — 2026-07-04

## Estado

`VERIFICADO PERO MEJORABLE`

CSV descargado desde Bing Webmaster Tools / AI Performance. No se ha modificado Shopify, Bing, IndexNow, sitemap, DNS, CDN, tema, páginas, robots, URLs, handles ni SEO fields.

## Archivo analizado

`VERIFICADO Y CORRECTO`

- Archivo: `C:\Users\d.bermejo\OneDrive - Matchwalls\Escritorio\matchwalls.com_AIPerformanceOverviewStats_7_4_2026 (1).csv`
- Tamaño: 695 bytes.
- Columnas:
  - `Date`
  - `Citations`
  - `Cited Pages`
- Tipo de exportación: overview diario, no detalle por URL ni consulta.

## Resumen de datos

`VERIFICADO Y CORRECTO`

- Filas: `20`.
- Total citations: `10`.
- Días con citas: `5`.
- Suma diaria de `Cited Pages`: `8`.
- Día con más citas: `6/17/2026`, con `3` citas y `3` páginas citadas.

## Días con actividad

`VERIFICADO Y CORRECTO`

| Fecha | Citations | Cited Pages |
|---|---:|---:|
| 6/17/2026 | 3 | 3 |
| 6/23/2026 | 2 | 1 |
| 6/24/2026 | 1 | 1 |
| 6/25/2026 | 2 | 1 |
| 6/30/2026 | 2 | 2 |

## Interpretación

`VERIFICADO PERO MEJORABLE`

MatchWalls tiene señales reales de citación en AI Performance de Bing para Microsoft Copilot y partners. La actividad no es continua, pero existe.

Este CSV confirma volumen temporal agregado, no identifica:

- URL exacta citada;
- consulta / grounding query;
- idioma;
- país;
- exactitud de la respuesta;
- si la página citada es estratégica o accidental.

## Limitación crítica

`INCOMPLETO`

El archivo no permite clasificar URLs citadas. Para poder convertir esto en mejora SEO/GEO/AGEO accionable hace falta obtener el detalle de:

- pestaña `Pages`, si tiene datos/exportación;
- pestaña `Grounding Queries`, si tiene datos/exportación;
- cualquier CSV de detalle disponible en Bing.

En la captura previa de `Grounding Queries`, la tabla mostraba `No data available` y `0 rows`, por lo que el detalle de consultas no estaba disponible en ese momento.

## Recomendación

`VERIFICADO PERO MEJORABLE`

1. Registrar este CSV como primera línea base CEO/CMO para Microsoft Copilot/partners.
2. Intentar revisar/exportar `Pages` en AI Performance:
   - si hay filas: clasificar URLs;
   - si no hay filas: registrar que Bing solo aporta overview agregado por ahora.
3. No modificar contenido ni IndexNow a partir de este dato todavía.

## Siguiente lote recomendado

`MW-BING-WEBMASTER-AI-PERFORMANCE-PAGES-QA-013E5`

Objetivo: abrir pestaña `Pages` dentro de AI Performance y comprobar si existen URLs citadas. Solo lectura.

## Estado final

`VERIFICADO PERO MEJORABLE`

Tenemos la primera métrica real de Copilot/AI para MatchWalls: `10` citas en el periodo exportado. Aún no tenemos el detalle de URLs ni consultas, así que no se debe inferir qué contenido está funcionando hasta revisar la pestaña `Pages`.
