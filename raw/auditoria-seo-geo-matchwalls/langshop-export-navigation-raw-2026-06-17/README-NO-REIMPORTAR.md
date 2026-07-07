# LangShop navigation export raw - 2026-06-17

Estado: VERIFICADO PERO MEJORABLE

Estos CSV son respaldo/evidencia del estado exportado desde LangShop Navigation.
No son una fuente aprobada para reimportacion directa.

Archivos incluidos:

- navigation_export_es_de.csv
- navigation_export_es_en.csv
- navigation_export_es_fr.csv
- navigation_export_es_nl.csv

Verificacion local:

- Los 4 CSV existen en esta carpeta.
- Cada CSV tiene cabecera `location,source,target`.
- Cada CSV contiene 189 filas.
- Cada CSV conserva 1 fila historica con `Tarjeta regalo`.
- No se detectaron filas con `Black Friday`.
- No se detectaron filas con `Envios internacionales` / `International shipping`.

Criterio de uso:

- Usar solo como respaldo, auditoria y comparacion.
- No importar en LangShop sin un lote aprobado.
- Antes de cualquier importacion, cruzar contra el estado publico actual de Shopify/matchwalls.com.
- La fuente de verdad editorial es el contenido optimizado y verificado en Shopify/storefront, no este export bruto.

Shopify/LangShop:

- No se modifico Shopify.
- No se modifico LangShop.
- No se ejecuto ninguna mutacion.
