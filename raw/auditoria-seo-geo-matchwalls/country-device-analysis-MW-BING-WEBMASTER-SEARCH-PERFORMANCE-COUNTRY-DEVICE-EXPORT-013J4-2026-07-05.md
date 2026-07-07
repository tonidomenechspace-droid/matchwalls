# MW-BING-WEBMASTER-SEARCH-PERFORMANCE-COUNTRY-DEVICE-EXPORT-013J4

Fecha: 2026-07-05  
Modo: solo lectura / análisis de CSV / sin cambios en Shopify, Bing, IndexNow ni configuración externa.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `baseline-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J-2026-07-05.md`
- `keywords-analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-KEYWORDS-EXPORT-013J2-2026-07-05.md`
- `pages-analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-PAGES-EXPORT-013J3-2026-07-05.md`
- `registro-cambios-ejecutados.md`

## Archivos recibidos

`VERIFICADO Y CORRECTO`

Country:

`C:\Users\d.bermejo\OneDrive - Matchwalls\Escritorio\matchwalls.com_CountryReport_7_5_2026 EEEEEEEEEE.csv`

Device:

`C:\Users\d.bermejo\OneDrive - Matchwalls\Escritorio\matchwalls.com_DeviceReport_7_5_2026 DDDDDDD.csv`

## Validación

`VERIFICADO Y CORRECTO`

Ambos exports suman exactamente:

- Impresiones: `749`
- Clics: `3`
- CTR calculado: `0,40%`

Esto coincide con el baseline y overview 013J/013J1. A diferencia de `Keywords` y `Pages`, estos dos exports sí cubren el total visible del informe de Search Performance.

## Country: distribución por país

`VERIFICADO PERO MEJORABLE`

| País / bucket | Impresiones | % impresiones | Clics | Estado |
|---|---:|---:|---:|---|
| `ww` / worldwide o unknown | 456 | 60,88% | 1 | `VERIFICADO PERO MEJORABLE` |
| España (`es`) | 112 | 14,95% | 1 | `VERIFICADO PERO MEJORABLE` |
| Francia (`fr`) | 68 | 9,08% | 0 | `VERIFICADO PERO MEJORABLE` |
| Brasil (`br`) | 40 | 5,34% | 1 | `STANDBY` |
| Estados Unidos (`us`) | 38 | 5,07% | 0 | `VERIFICADO PERO MEJORABLE` |
| Italia (`it`) | 12 | 1,60% | 0 | `STANDBY` |
| Alemania (`de`) | 11 | 1,47% | 0 | `VERIFICADO PERO MEJORABLE` |
| Japón (`jp`) | 7 | 0,93% | 0 | `REQUIERE DECISION HUMANA` |
| Reino Unido (`gb`) | 4 | 0,53% | 0 | `VERIFICADO PERO MEJORABLE` |
| Canadá (`ca`) | 1 | 0,13% | 0 | `VERIFICADO PERO MEJORABLE` |
| China (`cn`) | 0 | 0,00% | 0 | `VERIFICADO Y CORRECTO` |

## Lectura por país

`VERIFICADO PERO MEJORABLE`

1. `ww` concentra el 60,88% de impresiones. Es una señal útil, pero no accionable por país porque Bing lo entrega como bucket agregado o no determinado.
2. España y Francia sí tienen señal directa y están dentro de la estrategia prioritaria.
3. Alemania aparece con señal baja pero real.
4. Reino Unido y Estados Unidos aparecen con señal baja/media, pero se mantienen como mercados futuros o cautelosos; no usar copy genérico ni claims logísticos no verificados.
5. Brasil e Italia tienen datos, incluido 1 clic en Brasil, pero quedan en `STANDBY` porque PT/IT están fuera del alcance prioritario actual.

## Device: distribución por dispositivo

`VERIFICADO PERO MEJORABLE`

| Dispositivo | Impresiones | % impresiones | Clics | CTR | Posición media |
|---|---:|---:|---:|---:|---:|
| Desktop | 713 | 95,19% | 3 | 0,42% | 10,00 |
| Mobile | 36 | 4,81% | 0 | 0,00% | 17,90 |

## Lectura por dispositivo

`VERIFICADO PERO MEJORABLE`

La señal de Bing actual es claramente desktop:

- Desktop concentra el 95,19% de impresiones y el 100% de clics.
- Mobile tiene baja muestra, cero clics y peor posición media.

Esto no significa que mobile no importe. Para SEO/GEO de e-commerce sigue siendo crítico, pero en Bing Search Performance el volumen actual está casi todo en desktop.

## Cruce prudente con 013J2 y 013J3

`VERIFICADO PERO MEJORABLE`

Bing exporta `Keyword`, `Page`, `Country` y `Device` como dimensiones separadas. No existe en estos CSVs una unión directa query → URL → país → dispositivo.

Por tanto:

- Es válido decir que el informe total se concentra en desktop.
- Es válido decir que España y Francia tienen señal directa.
- Es válido decir que las URLs y keywords principales detectadas en 013J2/013J3 pertenecen sobre todo a colecciones ES, producto/color/patrón, geo y medición.
- No es válido afirmar que una keyword concreta viene de un país concreto sin datos adicionales.
- No es válido modificar una URL concreta solo por un país si no se cruza con URL/consulta y revisión pública.

## Riesgos detectados

`VERIFICADO PERO MEJORABLE`

1. `ww` limita la lectura geográfica: demasiada señal queda sin país concreto.
2. Mobile es débil en Bing, pero la muestra es pequeña; no se debe concluir que solo importa desktop.
3. PT/IT tienen datos reales, pero siguen fuera del foco prioritario.
4. Estados Unidos aparece, pero la estrategia había definido que EN-US requiere claims logísticos claros antes de crear landings.
5. Cambiar handles, URLs o landings por estos datos sería prematuro.

## Recomendación operativa

`VERIFICADO PERO MEJORABLE`

No tocar Shopify todavía.

Siguiente lote seguro:

`MW-BING-SEO-GEO-QUERY-URL-OPPORTUNITY-MAP-013J5`

Objetivo: crear un mapa de oportunidad con:

- keywords 013J2;
- páginas 013J3;
- países/dispositivos 013J4;
- estado de prioridad;
- si requiere auditoría URL pública;
- si queda en `STANDBY`;
- si puede alimentar futuros lotes editoriales.

Este mapa debe diferenciar hechos directos de inferencias, para no sobreactuar.

## Evidencias generadas

`VERIFICADO Y CORRECTO`

- `country-classified-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-COUNTRY-DEVICE-EXPORT-013J4-2026-07-05.csv`
- `device-classified-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-COUNTRY-DEVICE-EXPORT-013J4-2026-07-05.csv`
- `country-device-summary-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-COUNTRY-DEVICE-EXPORT-013J4-2026-07-05.csv`
- `country-device-analysis-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-COUNTRY-DEVICE-EXPORT-013J4-2026-07-05.md`

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó Shopify, Bing Webmaster Tools, IndexNow, Search Performance, tema, URLs, handles, traducciones, SEO fields, robots, sitemap, schema, productos, páginas, colecciones ni apps.
