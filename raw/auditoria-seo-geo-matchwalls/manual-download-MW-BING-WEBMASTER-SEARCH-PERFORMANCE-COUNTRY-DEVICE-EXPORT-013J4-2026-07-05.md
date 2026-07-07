# MW-BING-WEBMASTER-SEARCH-PERFORMANCE-COUNTRY-DEVICE-EXPORT-013J4

Fecha: 2026-07-05  
Modo: solo lectura / preparación de export / sin cambios en Shopify, Bing, IndexNow ni configuración externa.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `baseline-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J-2026-07-05.md`
- `keywords-analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-KEYWORDS-EXPORT-013J2-2026-07-05.md`
- `pages-analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-PAGES-EXPORT-013J3-2026-07-05.md`
- `registro-cambios-ejecutados.md`

## Estado real comprobado

`INCOMPLETO`

Se revisaron:

- `C:\Users\d.bermejo\OneDrive - Matchwalls\Escritorio`
- `C:\Users\d.bermejo\Downloads`

Archivos recientes detectados:

- `matchwalls.com_PageTrafficReport_7_5_2026 CCCCCCCCCC.csv`
- `matchwalls.com_KeywordReport_7_5_2026 BBBBBBB.csv`
- `matchwalls.com_SearchPerformanceOverview_All_7_5_2026.csv`
- `matchwalls.com_IndexNowSubmittedUrls_7_5_2026 AAAAAAAA.csv`
- `matchwalls.com_AIPageStatsReport_7_4_2026 ORO.csv`
- `matchwalls.com_AIPerformanceOverviewStats_7_4_2026 (1).csv`

No se encontró ningún CSV de `Country` ni de `Device`.

## Objetivo del lote

`REQUIERE DECISION HUMANA`

Descargar dos exports separados desde Bing Webmaster Tools:

1. `Search Performance > List By > Country > Download all`
2. `Search Performance > List By > Device > Download all`

Ambos deben usar el mismo rango que los lotes anteriores: `3 M`.

## Pasos exactos para Daniel

`REQUIERE DECISION HUMANA`

### Export Country

1. En Bing Webmaster Tools, entrar en `matchwalls.com/`.
2. Ir a `Search Performance`.
3. Mantener rango `3 M`.
4. Bajar hasta la tabla `List By`.
5. Pulsar `Country`.
6. Verificar que la tabla muestra países, no URLs ni keywords.
7. Pulsar `Download all`.
8. Guardar el CSV en el Escritorio.

### Export Device

1. En la misma pantalla `Search Performance`.
2. En `List By`, pulsar `Device`.
3. Verificar que la tabla muestra dispositivos, por ejemplo desktop/mobile/tablet.
4. Pulsar `Download all`.
5. Guardar el CSV en el Escritorio.

Cuando estén ambos, avisar:

`GUARDADO 013J4`

## Qué NO descargar

`VERIFICADO Y CORRECTO`

No sirve para este lote:

- `SearchPerformanceOverview`
- `KeywordReport`
- `PageTrafficReport`
- `IndexNowSubmittedUrls`
- `AIPageStatsReport`

## Riesgo detectado

`VERIFICADO PERO MEJORABLE`

El riesgo principal es tomar decisiones de contenido sobre URLs y keywords sin conocer país/dispositivo. Este lote queda bloqueado hasta recibir ambos CSVs.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó Shopify, Bing Webmaster Tools, IndexNow, Search Performance, tema, URLs, handles, traducciones, SEO fields, robots, sitemap, schema, productos, páginas, colecciones ni apps.
