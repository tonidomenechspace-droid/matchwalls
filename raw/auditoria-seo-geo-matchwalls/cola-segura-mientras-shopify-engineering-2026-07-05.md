# Cola segura mientras Shopify Engineering responde

Fecha: 2026-07-05  
Estado: `STANDBY` operativo sobre Shopify / avance documental permitido

## Regla principal

No ejecutar cambios que puedan alterar el storefront, el render de home, las páginas España/Francia, traducciones, SEO visible, schema o tema hasta que Shopify responda al ticket `68731900`.

## Lotes recomendados, en orden

### 1. `MW-MASTER-QUEUE-RECONCILIATION-014A`

Estado: `VERIFICADO Y CORRECTO` como siguiente paso seguro.

Objetivo:

- Revisar cola maestra.
- Separar ejecutado, verificado, standby y pendiente.
- Marcar bloqueos por ticket Shopify.
- Evitar repetir trabajos o tocar áreas congeladas.

Impacto Shopify: ninguno.

### 2. `MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J`

Estado: `VERIFICADO Y CORRECTO` como lote seguro si hay capturas/exportaciones.

Objetivo:

- Registrar línea base Bing: impresiones, clics, CTR, keywords, páginas y países.
- Separar datos Search Performance de AI Performance.
- Documentar oportunidad Bing/Copilot/Yahoo/Edge.

Impacto Shopify: ninguno.

### 3. `MW-BING-AI-PERFORMANCE-CITED-URLS-BASELINE-013J1`

Estado: `VERIFICADO Y CORRECTO` como lote seguro si se trabaja con CSV/export.

Objetivo:

- Auditar URLs citadas por Bing AI Performance.
- Clasificar si son canónicas, indexables, antiguas, no prioritarias o fuera de idioma prioritario.
- No cambiar nada todavía.

Impacto Shopify: ninguno.

### 4. `MW-CEO-CMO-PANEL-SPEC-014B`

Estado: `VERIFICADO Y CORRECTO` como lote documental.

Objetivo:

- Diseñar el panel mensual CEO/CMO.
- Definir métricas por país/idioma: orgánico, no-brand, indexación, IA, CWV, schema, menciones.

Impacto Shopify: ninguno.

### 5. `MW-GEO-DE-NL-UK-BRIEF-DRAFT-015A`

Estado: `VERIFICADO Y CORRECTO` como borrador local.

Objetivo:

- Preparar briefs y estructura de contenido para Alemania, Países Bajos y UK.
- No crear páginas ni traducir en Shopify.

Impacto Shopify: ninguno.

## Lotes en standby hasta respuesta Shopify

### `MW-HOME-RENDER-500-THEME-APP-DIAG-013F2`

Estado: `STANDBY`

Motivo:

- Puede ser útil si Shopify pide revisar tema/app.
- Mejor esperar primero la lectura de ingeniería para no contaminar diagnóstico.

### `MW-GEO-LANDINGS-SPAIN-FRANCE-*`

Estado: `STANDBY`

Motivo:

- Relacionado con el ticket de HTML/cache desactualizado.
- No tocar España/Francia hasta respuesta.

### `MW-GEO-LANDINGS-I18N-*`

Estado: `STANDBY`

Motivo:

- LangShop/traducciones pueden disparar nuevos renders/cachés.
- Shopify pidió retener cambios.

### `MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-*`

Estado: `STANDBY`

Motivo:

- Implica tema/schema visible.
- Congelado hasta respuesta.

### `MW-CRAWLERS-AI-FILES-LLMS-AGENTS-FACTUAL-DIAG-013C1`

Estado: `STANDBY`

Motivo:

- Diagnóstico sería seguro, pero puede relacionarse con archivos públicos de agente.
- Prioridad menor hasta cerrar incidencia de home.

## Decisión recomendada

Avanzar ahora con:

`MW-MASTER-QUEUE-RECONCILIATION-014A`

Después, si queda tiempo y sin respuesta de Shopify:

`MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J`

