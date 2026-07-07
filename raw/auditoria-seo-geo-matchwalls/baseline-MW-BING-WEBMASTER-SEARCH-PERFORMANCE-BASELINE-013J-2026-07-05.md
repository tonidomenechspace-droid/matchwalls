# Baseline Bing Search Performance — MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J

Fecha: 2026-07-05  
Hora de registro: 15:52 Europe/Madrid  
Modo: solo lectura / medición / sin cambios externos  
Estado final: `VERIFICADO PERO MEJORABLE`

## Objetivo

Crear una línea base inicial de Bing Webmaster Tools > Search Performance para `matchwalls.com/`, separada de AI Performance e IndexNow, mientras Shopify Engineering mantiene abierto el ticket `68731900`.

Este lote no modifica Shopify, Bing Webmaster Tools, IndexNow, tema, páginas, traducciones, URLs, handles, SEO fields, schema, robots, sitemap, `llms.txt`, `agents.md`, redirecciones ni apps.

## Documentos y evidencias revisadas

`VERIFICADO Y CORRECTO`

- `registro-cambios-ejecutados.md`
- `reconciliacion-MW-MASTER-QUEUE-RECONCILIATION-014A-2026-07-05.md`
- `diagnostico-MW-BING-WEBMASTER-AI-PERFORMANCE-DIAG-013E3-2026-07-04.md`
- `manual-check-MW-INDEXNOW-BING-WEBMASTER-RECEPTION-MANUAL-CHECK-013I4B-2026-07-05.md`
- `monitor-MW-INDEXNOW-BING-WEBMASTER-DISCREPANCY-MONITOR-013I5C-2026-07-05.md`
- Capturas aportadas por Daniel de Bing Webmaster Tools > Search Performance, 2026-07-05.

## Estado real de acceso

`VERIFICADO PERO MEJORABLE`

Se intentó comprobar el informe desde el navegador integrado, pero la pestaña disponible redirigió a la pantalla pública de Bing Webmaster Tools con `Sign In`. Por tanto:

- no se pudo descargar desde Codex el CSV completo de Search Performance;
- no se pudo verificar desde sesión activa la tabla completa de 88 keywords;
- sí se registran como evidencia válida las capturas autenticadas aportadas por Daniel.

Además, se buscó un CSV ya descargado en:

- `C:\Users\d.bermejo\OneDrive - Matchwalls\Escritorio`
- `C:\Users\d.bermejo\Downloads`
- `C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls`

Resultado: `INCOMPLETO`; no se localizó un export específico de Bing Search Performance.

## Métricas visibles de Search Performance

`VERIFICADO Y CORRECTO`

Fuente: capturas autenticadas de Bing Webmaster Tools.

| Métrica | Valor visible |
|---|---:|
| Propiedad | `matchwalls.com/` |
| Informe | Search Performance |
| Rango seleccionado | `3 M` |
| Total clicks | `3` |
| Total impressions | `749` |
| Avg. CTR | `0.4%` |
| Keywords visibles | `25` |
| Keywords totales indicadas por Bing | `88` |

`NO ACCESIBLE`: posición media global, URLs/páginas asociadas a cada query, distribución por país, dispositivo y páginas, porque no hay export completo en este lote.

## Keywords visibles registradas

`VERIFICADO PERO MEJORABLE`

Se ha creado la matriz:

- `baseline-keywords-visible-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J-2026-07-05.csv`

Lectura principal:

- Hay presencia real en Bing Search con 749 impresiones en 3 meses.
- El volumen visible es bajo, pero hay posiciones útiles en long-tail.
- Solo una fila visible tiene click: `machwalls`, 1 click, posición 1.00. Los otros 2 clicks del total no son atribuibles con la evidencia visible.
- La mayoría de queries visibles son no-brand y tienen 0 clicks.
- Aparecen señales en ES, EN, FR y PT. PT queda fuera del alcance prioritario salvo autorización expresa.

## Oportunidades detectadas

`VERIFICADO PERO MEJORABLE`

Prioridad alta para próximos análisis, no para escritura inmediata:

1. Medición de pared:
   - `imagen de como es el ancho y el alto de una pared`
   - Conecta con guías de medición e instalación.

2. Patrones y familias:
   - `papel pintado de tartán beige`
   - `papel de tartán amarillo y azul`
   - `papel pintado gingham precio`
   - `papel con cuadros de gingham verde`
   - `papel de pared con patrón de gingham rosa`
   - `papel de pared con puntos de polka rosa`

3. Colores / estilos:
   - `papel pintado negro`
   - `papel pintado lila`
   - `papel de pared estética negra y blanco`
   - `papel pintado geométrico`
   - `papel pintado con diseño geométrico`

4. Geográficas:
   - `wall decoration interior salamanca`
   - `wall decoration interior tarragona`

5. Personalización / FR:
   - `fresque avec photo`

## Riesgos y cautelas

`VERIFICADO PERO MEJORABLE`

- No confundir Search Performance con AI Performance:
  - Search Performance visible: 3 clicks, 749 impresiones, 0.4% CTR.
  - AI Performance 013E3: 10 citations en Microsoft Copilot/partners.

- No confundir IndexNow con indexación:
  - Bing IndexNow muestra 13 submitted URLs, pero eso no significa ranking ni indexación.

- No optimizar literalmente typos o queries dudosas:
  - `machwalls`
  - `panel pared hzabitacion juvenil`

- No actuar sobre PT ahora:
  - `papel de parede lilás`
  - `site para fazer mural`
  - `mural com nome da equipe e foto com tnt e crepon`

- No tocar Shopify ni páginas mientras ticket `68731900` siga abierto:
  - home/render están bajo investigación de infraestructura;
  - cualquier cambio de contenido podría contaminar la lectura del incidente.

## Estado final del lote

`VERIFICADO PERO MEJORABLE`

Baseline inicial creado, pero parcial. Sirve para orientar el panel SEO/GEO/AEO y priorizar futuros análisis, no para ejecutar cambios todavía.

## Archivos generados

`VERIFICADO Y CORRECTO`

- `baseline-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J-2026-07-05.md`
- `baseline-summary-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J-2026-07-05.csv`
- `baseline-keywords-visible-MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J-2026-07-05.csv`

## Próximo paso recomendado

`MW-BING-WEBMASTER-SEARCH-PERFORMANCE-FULL-EXPORT-013J1`

Objetivo:

1. Descargar `Download all` de Bing Webmaster Tools > Search Performance con sesión autenticada.
2. Confirmar rango exacto.
3. Analizar las 88 keywords completas.
4. Separar por keyword, página, país y dispositivo si Bing lo permite.
5. Mapear query → URL → idioma → intención → prioridad.

Este próximo lote sigue siendo solo lectura.
