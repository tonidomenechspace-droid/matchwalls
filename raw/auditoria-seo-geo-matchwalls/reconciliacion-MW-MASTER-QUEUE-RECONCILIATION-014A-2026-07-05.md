# Reconciliación de cola maestra — MW-MASTER-QUEUE-RECONCILIATION-014A

Fecha: 2026-07-05  
Hora de cierre: 15:24 Europe/Madrid  
Modo: documental / solo lectura / sin cambios Shopify  
Estado final: `VERIFICADO Y CORRECTO`

## Objetivo

Reconciliar el estado operativo real del programa SEO/GEO/AEO de MatchWalls para poder seguir avanzando mientras Shopify Engineering responde al ticket `68731900`.

Este lote no modifica Shopify, LangShop, tema, URLs, handles, SEO fields, redirecciones, robots, sitemap, schema, IndexNow ni ninguna app.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `registro-cambios-ejecutados.md`
- `standby-MW-SHOPIFY-ENGINEERING-TICKET-68731900-2026-07-05.md`
- `cola-segura-mientras-shopify-engineering-2026-07-05.md`
- `handoff-chatgpt-MW-SEO-GEO-MARKET-STRATEGY-AUDIT-012A-2026-07-01.md`
- `handoff-chatgpt-MW-GEO-LANDINGS-PRIORITY-MAP-012B-2026-07-01.md`
- `handoff-chatgpt-MW-GEO-LANDINGS-BRIEF-COUNTRY-PILLARS-012C-2026-07-02.md`
- `handoff-chatgpt-MW-GEO-LANDINGS-CONTENT-DRAFTS-012D-2026-07-02.md`
- `qa-MW-PUBLISH-TECH-DEBT-010P-2026-06-26.md`
- `diagnostico-MW-INDEXABILITY-CANONICAL-HREFLANG-DIAG-011H-2026-07-01.md`
- `diagnostico-MW-INDEXABILITY-GEO-COLLECTIONS-ROLLING-DIAG-011E2-2026-07-01.md`
- `resultado-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-MANUAL-CODE-012L6B-2026-07-04.md`
- `resultado-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O-2026-07-04.md`
- `diagnostico-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-POST-PURGE-RECHECK-012O7-2026-07-04.md`
- `resultado-MW-COLLECTIONS-ROOT-HUB-I18N-PUBLISH-READINESS-013E13E-2026-07-04.md`
- `resultado-MW-COLLECTIONS-I18N-CARD-TITLES-SAFE-TEXT-UPDATE-013E16-2026-07-05.md`
- `resultado-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E-2026-07-05.md`
- `resultado-MW-SHOPIFY-CLI-INSTALL-AUTH-THEME-PUSH-013E16E2-2026-07-05.md`
- `audit-MW-INDEXNOW-BING-WEBMASTER-SUBMITTED-URLS-AUDIT-013I5-2026-07-05.md`
- `full-export-MW-INDEXNOW-BING-WEBMASTER-SUBMITTED-URLS-FULL-EXPORT-013I5B-2026-07-05.md`
- `decision-MW-INDEXNOW-NOINDEX-HISTORIC-SUBMISSION-DECISION-013I6-2026-07-05.md`
- `review-MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C-REVIEW-2026-07-05.md`
- `diagnostico-MW-CRAWLERS-WAF-CDN-BOT-ALLOWLIST-DIAG-013F-2026-07-05.md`
- `evidence-MW-CRAWLERS-HOME-500-SHOPIFY-INFRA-EVIDENCE-013F1-2026-07-05.md`
- `addendum-MW-CRAWLERS-HOME-500-HEADERS-RECHECK-013F1B-2026-07-05.md`

## Estado real comprobado en este lote

`VERIFICADO PERO MEJORABLE`

Comprobación pública mínima, sin admin y sin mutaciones:

| URL | Resultado | Evidencia |
|---|---:|---|
| `https://www.matchwalls.com/` | `500` | `x-request-id: d3dce9ae-7dbc-4036-8bb3-07c7dc433252-1783257509`; `theme=178399019384`; `pageType=index`; `edge=MAD`; `servedBy=jlj9`; `render;dur=1518`; `cache-control: private, no-store` |
| `https://www.matchwalls.com/sitemap.xml` | `200` | `content-type: application/xml`; `x-request-id: 3afc0b94-d2f5-4276-8906-459649ad0e62-1783257542` |
| `https://www.matchwalls.com/robots.txt` | `200` | `content-type: text/plain`; `theme=178399019384`; `pageType=robots`; `x-request-id: 8e8257c9-c3c2-41da-b144-ff50b537dfee-1783257543` |

Interpretación: la home sigue en `RIESGO CRITICO` por error `500` intermitente/persistente. `robots.txt` y `sitemap.xml` responden correctamente en la comprobación puntual.

## Bloqueo principal vigente

`RIESGO CRITICO`

Shopify Engineering ticket `68731900` está abierto y confirmado por soporte con dos incidencias:

1. HTML/render cache desactualizado en páginas España/Francia.
2. Errores `500` intermitentes en la home.

Hasta respuesta de ingeniería, quedan congelados:

- tema MAIN y draft;
- home;
- secciones, snippets y Liquid;
- app embeds;
- LangShop/traducciones;
- páginas España/Francia;
- URLs, handles, redirecciones y canonicals;
- SEO title/meta description;
- schema en tema;
- `robots.txt`, `llms.txt`, `agents.md`, sitemap;
- configuración IndexNow.

## Estado reconciliado por bloque

### 1. Deuda técnica global 010

Estado: `CORREGIDO Y VERIFICADO`

El tema técnico `178399019384` fue publicado en `MW-PUBLISH-TECH-DEBT-010P` y la matriz pública de 170 URLs pasó correctamente. El tema anterior `178396463480` quedó como reversión disponible.

Matiz importante: el estado técnico 010P no cancela la incidencia posterior de infraestructura Shopify en home. La home ahora está afectada por ticket `68731900`, no por una deuda 010P ya cerrada.

### 2. Indexabilidad 011

Estado general: `VERIFICADO PERO MEJORABLE`

Cerrado o corregido:

- Política de muestras: noindex por defecto para productos muestra confirmados; páginas informativas de muestras indexables; excepciones solo con evidencia.
- Piloto y rolling de muestras noindex ejecutados y verificados.
- Limpieza de prueba `facade-variants/test` ejecutada.
- Black Friday noindex ejecutado para URLs no evergreen; exclusión visual posterior del hub de colecciones ejecutada en `013E16E2`.
- Varias limpiezas/consolidaciones de redirects ejecutadas: cadenas, dead targets, FR chains, home targets, sample dead target y collections dead targets.

Pendiente:

- `MW-INDEXABILITY-CANONICAL-HREFLANG-DIAG-011H`: estado `VERIFICADO PERO MEJORABLE`; requiere seguir con auditoría/corrección quirúrgica posterior.
- Geográficas: no ejecutar noindex masivo; proteger España/Francia estratégicas; decisión humana + datos GSC antes de tocar.
- IT/PT: `STANDBY`, solo limpieza defensiva si aparece error crítico.

### 3. Landings geográficas España/Francia 012

Estado general: `STANDBY`

Hechos verificados:

- Estrategia y borradores país ES/FR existen.
- Se trabajaron contenido, traducciones, SEO meta, schema e interlinking en lotes 012F–012O.
- Schema main manual `012L6B`: `CORREGIDO Y VERIFICADO` según registro.

Bloqueo:

- Storefront/render de páginas España/Francia quedó inconsistente en 012O/012O7.
- Shopify realizó purge, pero el problema no quedó resuelto completamente.
- La incidencia está dentro del ticket `68731900`.

Decisión:

- No tocar más ES/FR, LangShop, schema ni enlaces visibles hasta que Shopify responda.

### 4. Bing Webmaster / Copilot / AI Performance 013E

Estado general: `VERIFICADO PERO MEJORABLE`

Cerrado:

- Bing Webmaster Tools verificado/importado desde Google Search Console.
- Sitemap detectado con estado `Success`, aprox. 7.8K URLs descubiertas.
- AI Performance ya muestra citas y páginas citadas.
- Se exportaron/analizaron páginas citadas por Bing AI.

Pendiente seguro:

- Crear línea base Bing Search Performance: impresiones, clics, CTR, keywords, páginas, países.
- Separar Search Performance de AI Performance.
- Usar datos Bing/Copilot/Yahoo/Edge como capa de medición, no como promesa de ranking.

### 5. Hub `/collections` e i18n de colecciones 013E10–013E16E2

Estado general: `VERIFICADO PERO MEJORABLE`

Cerrado:

- Diagnóstico de `/en/collections/` citado por Bing AI.
- Arquitectura/copy del hub root i18n preparados.
- Títulos visibles seguros de cards corregidos en ES/EN/FR/DE/NL cuando estaban aprobados.
- Black Friday excluido del hub público de colecciones mediante `013E16E2`: `CORREGIDO Y VERIFICADO`.

Pendiente:

- Publicación/reestructura del hub root completo: `REQUIERE DECISION HUMANA`.
- No avanzar en tema/hub mientras home/render esté bajo ingeniería Shopify.

### 6. IndexNow / Bing / Copilot 013F–013I

Estado general: `VERIFICADO PERO MEJORABLE`

Cerrado:

- La vía de archivo root por CDN redirect fue validada y descartada para producción.
- Rollback temporal de esa vía ejecutado.
- App IndexNow StoreSpark Premium instalada/configurada.
- Idiomas prioritarios activados: ES por defecto, EN, FR, DE, NL.
- Bing Webmaster muestra recepción de URLs IndexNow.
- Política definida para URLs históricas `noindex`: no reenviar manualmente, no retirar sin evidencia, monitorizar si aparecen indexadas/citadas.

Pendiente:

- La discrepancia entre app y Bing Webmaster queda en `STANDBY`/monitorización.
- No reenvíos masivos mientras Shopify Engineering investiga.

### 7. Crawlers / IA / robots / llms / agents 013C–013F1B

Estado general: `STANDBY`

Cerrado:

- Política revisada: no cambiar `robots.txt` ahora; visibilidad primero; no añadir allowlists explícitas de IA sin necesidad.
- `robots.txt`, `sitemap.xml`, `llms.txt` y `agents.md` respondían 200 en auditoría 013F.
- En comprobación mínima de 014A, `robots.txt` y `sitemap.xml` siguen respondiendo 200.

Bloqueo:

- Home devuelve `500`; afecta SEO/GEO/AEO porque la home es URL de entidad.
- No tocar archivos de crawler/agent ni robots hasta respuesta Shopify.

### 8. Entidad factual, schema global y contenidos citables

Estado: `INCOMPLETO`

Hay trabajo parcial en landings ES/FR y schema geográfico, pero no existe todavía un cierre global para:

- entidad MatchWalls coherente en ES/EN/FR/DE/NL;
- Organization/WebSite/Product/Offer/Breadcrumb/Article/FAQ/HowTo coherentes en todo el sitio;
- base factual citable global;
- guías comparativas y contenido editorial por intención;
- autores/expertos/políticas visibles alineadas.

No avanzar con implementación hasta que se libere la congelación de Shopify. Sí se pueden preparar borradores locales.

### 9. Panel CEO/CMO

Estado: `INCOMPLETO`

Pendiente diseñar panel mensual con:

- ingresos y conversiones orgánicas;
- clics/impresiones no-brand;
- URLs válidas/indexadas;
- canibalización de muestras;
- CWV;
- errores schema;
- citas Google AI/Gemini/Copilot/ChatGPT/Claude/Perplexity;
- URLs citadas y exactitud;
- menciones/enlaces.

Este bloque es seguro como documento local.

## Cola segura reconciliada

### Siguiente lote recomendado

`MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J`

Estado: `VERIFICADO Y CORRECTO` como siguiente paso seguro.

Motivo:

- No toca Shopify.
- Aprovecha Bing Webmaster ya verificado.
- Alimenta Bing/Copilot/Yahoo/Edge y el futuro panel CEO/CMO.
- Nos da línea base real mientras Shopify Engineering resuelve infraestructura.

### Alternativas seguras si se prefiere preparar estrategia

1. `MW-BING-AI-PERFORMANCE-CITED-URLS-BASELINE-013J1`
   - Clasificar URLs citadas por Bing AI.
   - No corregir todavía.

2. `MW-CEO-CMO-PANEL-SPEC-014B`
   - Diseñar panel mensual.
   - No conectar ni modificar herramientas.

3. `MW-GEO-DE-NL-UK-BRIEF-DRAFT-015A`
   - Preparar briefs locales Alemania, Países Bajos y UK.
   - No crear páginas.

4. `MW-I18N-SEO-META-GLOBAL-AUDIT-014C`
   - Auditoría documental y de datos exportados sobre SEO meta multiidioma.
   - No escribir en Shopify ni LangShop.

## Cola bloqueada hasta respuesta Shopify

`STANDBY`

- `MW-SHOPIFY-ENGINEERING-FIX-POSTCHECK-013F4`
  - Ejecutar solo cuando Shopify confirme acción o cierre.

- `MW-HOME-RENDER-500-THEME-APP-DIAG-013F2`
  - Ejecutar solo si Shopify pide revisar tema/app o si ingeniería descarta infraestructura.

- `MW-GEO-LANDINGS-SPAIN-FRANCE-STOREFRONT-POSTFIX-QA-012P`
  - Ejecutar tras fix Shopify.

- `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-CLOSE-012O8`
  - No ejecutar hasta storefront estable.

- `MW-GEO-LANDINGS-I18N-SEO-META-GLOBAL-REPAIR`
  - No ejecutar hasta que render/cache y home estén estables.

- `MW-CRAWLERS-AI-FILES-LLMS-AGENTS-FACTUAL-DIAG-013C1`
  - Puede ser lectura, pero queda en espera por cercanía a capa pública de crawlers.

- Cualquier publicación de tema, cambio Liquid, LangShop, URL, SEO fields, schema visible, robots, sitemap o IndexNow masivo.

## Cuándo reparar “todo en todos los idiomas”

`REQUIERE DECISION HUMANA`

El momento profesional para reparar SEO meta, contenido visible e i18n global en ES/EN/FR/DE/NL será después de:

1. Shopify confirme resolución o instrucción clara sobre ticket `68731900`.
2. La home pase QA pública estable con Chrome, Googlebot, Bingbot, OAI-SearchBot y PerplexityBot.
3. Las páginas España/Francia afectadas pasen QA pública estable.
4. Se confirme que LangShop/Shopify no están sirviendo HTML antiguo.
5. Se defina lote quirúrgico por tipo de recurso, no todo mezclado.

Antes de eso, lo correcto es preparar mapas, copy y QA, pero no escribir.

## Decisión final 014A

`VERIFICADO Y CORRECTO`

La cola queda reconciliada:

- Avance permitido: medición, análisis, panel, briefs y documentos locales.
- Avance bloqueado: cambios de storefront, tema, home, landings ES/FR, LangShop, schema visible, robots, sitemap e IndexNow masivo.
- Siguiente paso recomendado: `MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J`.

## Evidencias generadas

`VERIFICADO Y CORRECTO`

- `reconciliacion-MW-MASTER-QUEUE-RECONCILIATION-014A-2026-07-05.md`
- `cola-maestra-reconciliada-MW-MASTER-QUEUE-RECONCILIATION-014A-2026-07-05.csv`

