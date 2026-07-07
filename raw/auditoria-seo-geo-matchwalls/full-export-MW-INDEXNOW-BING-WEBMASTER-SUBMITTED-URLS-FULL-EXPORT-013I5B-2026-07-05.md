# MW-INDEXNOW-BING-WEBMASTER-SUBMITTED-URLS-FULL-EXPORT-013I5B

Fecha: 2026-07-05  
Hora de registro: 12:16 Europe/Madrid  
Modo: solo lectura  
Estado final: `INCOMPLETO`

## Objetivo

Intentar obtener la lista completa de URLs enviadas por IndexNow en Bing Webmaster Tools, porque el panel de Bing indicaba `Submitted URLs: 13`, mientras que el CSV recibido en el lote `013I5` contenía solo `3` filas.

## Documentos y registros revisados

`VERIFICADO Y CORRECTO`

- `registro-cambios-ejecutados.md`
- `audit-MW-INDEXNOW-BING-WEBMASTER-SUBMITTED-URLS-AUDIT-013I5-2026-07-05.md`
- `audit-MW-INDEXNOW-BING-WEBMASTER-SUBMITTED-URLS-AUDIT-013I5-2026-07-05.csv`
- Evidencia manual de Bing Webmaster Tools aportada por Daniel el 2026-07-05.

## Estado real observado en Bing Webmaster Tools

`VERIFICADO PERO MEJORABLE`

Propiedad observada:

- `matchwalls.com/`

Panel IndexNow:

- Métrica visible: `Submitted URLs`
- Valor visible: `13`

Tabla visible:

- Sección: `Submitted Urls list(shows latest 1000 urls)`
- Filas visibles: `3 rows`
- Botón `Export`: visible.
- Botón `View complete report`: visible en la parte superior del bloque IndexNow.
- No se observan filtros visibles para ampliar de 3 a 13 filas en la tabla mostrada.

URLs visibles en la tabla:

1. `https://www.matchwalls.com/`
   - Submitted: `Today at 10:02`
   - Source: `Self`
   - Details: `View`
2. `https://www.matchwalls.com/products/custom-file-uploader`
   - Submitted: `15 Jun 2026 at 22:52`
   - Source: `Shopify`
   - Details: `View`
3. `https://www.matchwalls.com/products/bambuze-negro`
   - Submitted: `15 Jun 2026 at 14:49`
   - Source: `Shopify`
   - Details: `View`

## Resultado del lote

`INCOMPLETO`

Bing muestra una métrica agregada de `13` submitted URLs, pero la tabla accesible en la pantalla y el CSV previamente exportado solo permiten verificar `3` URLs. No hay evidencia suficiente para listar o auditar las 10 URLs restantes sin inventar datos.

## Interpretación técnica

`VERIFICADO PERO MEJORABLE`

La integración de IndexNow está funcionando a nivel de recepción porque Bing muestra actividad y la home enviada aparece como `Self`. Sin embargo, el informe de Bing no expone todos los elementos que suma en el contador agregado.

Posibles explicaciones no verificadas:

- Bing puede contar envíos históricos no mostrados en la tabla actual.
- Bing puede agrupar eventos no exportables en la vista visible.
- La interfaz puede limitar los datos mostrados pese a indicar `latest 1000 urls`.
- El informe puede estar mezclando métricas agregadas recientes con filas detalladas disponibles.

Estas hipótesis quedan como inferencias, no como hechos confirmados.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó:

- Shopify.
- Bing Webmaster Tools.
- IndexNow.
- App IndexNow.
- Sitemap.
- Robots.
- URLs.
- Handles.
- Configuración de idiomas.
- Envíos manuales.

No se pulsaron acciones de riesgo ni se enviaron nuevas URLs.

## Decisión operativa

`REQUIERE DECISION HUMANA`

No conviene bloquear el plan por esta discrepancia si:

- las 3 URLs visibles ya están auditadas;
- la app no muestra fallos;
- Bing registra recepción;
- no se va a hacer una whitelist manual de URLs.

Conviene monitorizar de nuevo tras 24-72 horas o cuando la app genere nuevos eventos reales de productos, colecciones, páginas o blogs.

## Próximo lote recomendado

`MW-INDEXNOW-BING-WEBMASTER-DISCREPANCY-MONITOR-013I5C`

Objetivo: revisar de nuevo Bing Webmaster Tools después de propagación y nuevos eventos reales, sin tocar Shopify ni enviar URLs manualmente.

Alternativa si se quiere avanzar sin esperar:

`MW-INDEXNOW-NOINDEX-HISTORIC-SUBMISSION-DECISION-013I6`

Objetivo: decidir cómo tratar la URL histórica `custom-file-uploader` enviada por Shopify pese a tener `noindex,nofollow`, sin hacer cambios si no hay impacto real.

