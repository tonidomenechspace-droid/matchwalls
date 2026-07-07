# Análisis del export recibido — MW-BING-WEBMASTER-SEARCH-PERFORMANCE-FULL-EXPORT-013J1

Fecha: 2026-07-05  
Hora de análisis: 16:15 Europe/Madrid  
Modo: solo lectura / análisis CSV  
Estado final: `INCOMPLETO`

## Conclusión ejecutiva

El archivo recibido es válido y confirma la línea base global de Search Performance:

- `3` clics.
- `749` impresiones.
- CTR calculado: `0.40%`.
- Periodo del CSV: `2026-06-13` a `2026-07-03`.

Pero no es el export completo de keywords/páginas. El archivo se llama:

`matchwalls.com_SearchPerformanceOverview_All_7_5_2026.csv`

y solo contiene:

- `Date`
- `Clicks`
- `Impressions`
- `Avg. CTR`

Por tanto, sirve para el baseline temporal, pero no permite analizar las 88 keywords completas, páginas, países ni dispositivos.

## Archivo recibido

`VERIFICADO Y CORRECTO`

Ruta:

`C:\Users\d.bermejo\OneDrive - Matchwalls\Escritorio\matchwalls.com_SearchPerformanceOverview_All_7_5_2026.csv`

Estructura:

| Campo | Estado |
|---|---|
| Filas | `21` |
| Columnas | `Date`, `Clicks`, `Impressions`, `Avg. CTR` |
| Tipo | Overview diario |
| Keywords incluidas | No |
| Páginas incluidas | No |
| Países incluidos | No |
| Dispositivos incluidos | No |

## Validación contra baseline 013J

`VERIFICADO Y CORRECTO`

El CSV coincide con el baseline visible de Bing:

| Métrica | Captura 013J | CSV 013J1 | Estado |
|---|---:|---:|---|
| Clicks | `3` | `3` | `VERIFICADO Y CORRECTO` |
| Impressions | `749` | `749` | `VERIFICADO Y CORRECTO` |
| CTR | `0.4%` | `0.40%` | `VERIFICADO Y CORRECTO` |

Esto confirma que el baseline de pantalla era correcto.

## Evolución diaria

`VERIFICADO PERO MEJORABLE`

Top días por impresiones:

| Fecha | Clicks | Impresiones | CTR |
|---|---:|---:|---:|
| 2026-06-17 | 1 | 66 | 1.52% |
| 2026-06-23 | 1 | 54 | 1.85% |
| 2026-06-18 | 0 | 52 | 0.00% |
| 2026-06-25 | 0 | 46 | 0.00% |
| 2026-06-24 | 0 | 45 | 0.00% |

Los únicos días con clicks son:

- 2026-06-14: 1 click / 27 impresiones.
- 2026-06-17: 1 click / 66 impresiones.
- 2026-06-23: 1 click / 54 impresiones.

## Lectura por bloques de 7 días

`VERIFICADO PERO MEJORABLE`

| Ventana | Impresiones | Clicks | CTR calculado |
|---|---:|---:|---:|
| 2026-06-13 a 2026-06-19 | 236 | 2 | 0.85% |
| 2026-06-20 a 2026-06-26 | 278 | 1 | 0.36% |
| 2026-06-27 a 2026-07-03 | 235 | 0 | 0.00% |

Lectura prudente:

- Las impresiones son relativamente estables.
- El click-through cae a cero en el último bloque.
- No se puede atribuir la caída a una página, query o país porque este CSV no trae ese detalle.

## Riesgos de interpretación

`VERIFICADO PERO MEJORABLE`

No debe concluirse todavía:

- qué keyword genera los clicks;
- qué páginas rankean;
- qué país aporta visibilidad;
- si ES/EN/FR/DE/NL están funcionando proporcionalmente;
- si hay canibalización;
- si las landings geográficas están aportando impresiones;
- si las URLs citadas en AI Performance coinciden con Search Performance.

Para eso falta el export de keywords, páginas, países y dispositivos.

## Estado frente al objetivo 013J1

`INCOMPLETO`

El objetivo era analizar el export completo de Search Performance. El archivo recibido completa solo la parte de overview diario.

Queda pendiente:

- export `Keywords` / `List By Keywords`;
- export `Pages`;
- export `Country`;
- export `Device`.

## Archivos generados

`VERIFICADO Y CORRECTO`

- `analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-FULL-EXPORT-013J1-2026-07-05.md`
- `overview-summary-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-FULL-EXPORT-013J1-2026-07-05.csv`
- `overview-daily-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-FULL-EXPORT-013J1-2026-07-05.csv`

## Próximo paso recomendado

`MW-BING-WEBMASTER-SEARCH-PERFORMANCE-KEYWORDS-EXPORT-013J2`

Acción manual:

1. Bing Webmaster Tools.
2. Search Performance.
3. Bajar a `List By`.
4. Seleccionar `Keywords`.
5. Pulsar `Download all`.
6. Guardar el CSV en Escritorio.
7. Avisar: `GUARDADO 013J2`.

Si Bing permite exportar también `Pages`, `Device` y `Country`, hacerlo después, pero la prioridad quirúrgica es `Keywords`.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó:

- Shopify.
- Bing Webmaster Tools.
- IndexNow.
- Search Performance.
- Tema.
- URLs.
- Handles.
- Traducciones.
- SEO fields.
- Robots.
- Sitemap.
- Apps.
