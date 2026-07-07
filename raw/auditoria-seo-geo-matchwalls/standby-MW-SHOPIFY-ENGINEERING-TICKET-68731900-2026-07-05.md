# STANDBY — Shopify Engineering ticket 68731900

Fecha: 2026-07-05  
Hora de registro: 15:09 Europe/Madrid  
Estado: `STANDBY`  
Modo: seguimiento documental / sin cambios en Shopify

## Resumen

Shopify Support confirmó en chat que el ticket de ingeniería `68731900` queda abierto con dos incidencias separadas:

1. HTML/render cache desactualizado en páginas España/Francia.
2. Errores `500` intermitentes en la home `https://www.matchwalls.com/`.

Shopify indicó que ingeniería hará seguimiento por email y pidió retener cambios por parte de MatchWalls.

Contactos confirmados por Daniel:

- `danibermejo3t@gmail.com`
- `daniel.bermejo@matchwalls.com`

## Incidencia 1: HTML/cache desactualizado España/Francia

Estado: `STANDBY`

Descripción:

- Páginas España/Francia mostraban inconsistencias de render/storefront tras cambios ya guardados.
- El caso ya estaba escalado a ingeniería antes de añadir la incidencia de home.

No ejecutar mientras esté abierto:

- Cambios en contenido de páginas España/Francia.
- Cambios en traducciones LangShop relacionadas.
- Cambios en SEO fields de esas páginas.
- Cambios en schema, enlaces internos o bloques visibles de esas páginas.

## Incidencia 2: home con `500` intermitente

Estado: `RIESGO CRITICO`

URL afectada:

`https://www.matchwalls.com/`

Evidencia aportada a Shopify:

- `edge=MAD`
- `theme=178399019384`
- `pageType=index`
- `server=cloudflare`
- `cache-control: private, no-store` en `500`
- `render_ms` aproximado en `500`: 1195–1579 ms
- `servedBy` diferente entre respuestas `500` y `200`
- Afecta a Chrome y bots: Googlebot, Bingbot, OAI-SearchBot, PerplexityBot
- Última muestra fuerte: 14 `500` de 20 solicitudes

Archivos generados:

- `ticket-shopify-MW-CRAWLERS-HOME-500-SHOPIFY-INFRA-EVIDENCE-013F1B-2026-07-05.md`
- `headers-MW-CRAWLERS-HOME-500-HEADERS-RECHECK-013F1B-2026-07-05.csv`
- `recheck-MW-CRAWLERS-HOME-500-SHOPIFY-INFRA-EVIDENCE-013F1-2026-07-05.csv`

## Congelación operativa

Estado: `VERIFICADO Y CORRECTO`

Hasta respuesta de Shopify ingeniería, no ejecutar cambios en:

- Tema MAIN.
- Tema draft usado para publicación.
- Home.
- Secciones, snippets o archivos Liquid.
- App embeds.
- LangShop.
- Traducciones.
- Páginas España/Francia.
- URLs, handles, redirecciones, canonicals.
- SEO title/meta description.
- Schema en tema.
- `robots.txt`, `llms.txt`, `agents.md`, sitemap.
- Configuración IndexNow.

## Trabajo permitido mientras esperamos

Estado: `VERIFICADO Y CORRECTO`

Se permite continuar con trabajo que no altere Shopify ni el storefront:

1. Documentación y reconciliación de cola maestra.
2. Auditorías con datos exportados o capturas ya disponibles.
3. Bing Webmaster Tools en solo lectura.
4. Google Search Console en solo lectura.
5. Análisis de keywords, páginas citadas y rendimiento.
6. Preparación de contenidos en borrador local, sin subirlos.
7. Preparación de briefs DE/NL/UK/BE en documentos locales.
8. Diseño de panel CEO/CMO en local.
9. Revisión de estrategia de crawlers/IA sin modificar `robots.txt`.

## Trabajo bloqueado temporalmente

Estado: `STANDBY`

No avanzar con:

- Publicaciones de tema.
- Cambios de home.
- Nuevos bloques visibles en páginas públicas.
- Nuevas traducciones o actualizaciones LangShop.
- Cambios SEO en páginas España/Francia.
- Cambios en schema Liquid.
- Cambios de crawling/robots.
- Reenvíos manuales masivos IndexNow derivados de cambios de contenido.

## Plan de respuesta según Shopify

### Si Shopify confirma infraestructura/cache/render worker

Ejecutar:

`MW-SHOPIFY-ENGINEERING-FIX-POSTCHECK-013F4`

Pruebas:

- Home con Chrome, Googlebot, Bingbot, OAI-SearchBot, PerplexityBot.
- Mínimo 20–40 solicitudes controladas.
- Páginas España/Francia afectadas por el ticket anterior.
- `robots.txt`, `sitemap.xml`, `llms.txt`, `agents.md`.
- Revisión de `server-timing`, `servedBy`, `cf-ray`, `x-request-id`.

### Si Shopify pide revisar tema/app

Ejecutar primero solo diagnóstico:

`MW-HOME-RENDER-500-THEME-APP-DIAG-013F2`

Sin cambios. Solo lectura de:

- secciones de home;
- app embeds;
- snippets;
- diferencias con tema anterior;
- dependencias que puedan afectar render.

### Si Shopify pide mantener congelación

Continuar solo con lotes documentales/no Shopify:

- `MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J`
- `MW-MASTER-QUEUE-RECONCILIATION-014A`
- `MW-CEO-CMO-PANEL-SPEC-014B`
- `MW-GEO-DE-NL-UK-BRIEF-DRAFT-015A`

## Próximo lote recomendado ahora

`MW-MASTER-QUEUE-RECONCILIATION-014A`

Motivo:

- No toca Shopify.
- Ordena histórico, adeudo y bloqueos.
- Deja lista la cola de trabajo para retomar rápido cuando ingeniería responda.

Alternativa si Daniel quiere avanzar con medición:

`MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J`

Motivo:

- Solo lectura.
- Aprovecha Bing Webmaster Tools ya verificado.
- Alimenta el panel CEO/CMO sin alterar la web.

