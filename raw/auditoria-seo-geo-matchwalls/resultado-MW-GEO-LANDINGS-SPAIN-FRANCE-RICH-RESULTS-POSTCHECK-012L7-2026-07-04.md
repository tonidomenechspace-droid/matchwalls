# Resultado lote MW-GEO-LANDINGS-SPAIN-FRANCE-RICH-RESULTS-POSTCHECK-012L7

Fecha: 2026-07-04  
Estado final: `VERIFICADO Y CORRECTO`

## Alcance

Lote de solo lectura.

Objetivo: comprobar en producción que las landings país España/Francia publicadas en ES, EN, FR, DE y NL exponen structured data estable, parseable, coherente con contenido visible y apto para comprensión por buscadores y sistemas IA.

No se modificó Shopify, LangShop, temas, páginas, handles, URLs, canonicals, hreflang, metadatos, productos, precios, redirecciones ni App Embeds.

## Documentos leídos

- `resultado-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-MANUAL-CODE-012L6B-2026-07-04.md`.
- `qa-publico-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-MANUAL-CODE-012L6B-2026-07-04.csv`.
- `registro-cambios-ejecutados.md`.

## Estado real Shopify comprobado

Consulta Shopify Admin de solo lectura:

- Tema MAIN: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- `processing`: `false`.
- `processingFailed`: `false`.
- `updatedAt`: `2026-07-04T12:23:11Z`.
- `config/settings_data.json`: checksum `d487694e14fe7558034b7d4595075de4`, sin cambios.
- `snippets/geo-landing-schema.liquid`: checksum `9033b2bfa89dc435b9811b3d897e07c1`.
- `snippets/microdata-schema.liquid`: checksum `a3d8e23b4979219149a9c5b5f76723ec`.

Estado: `VERIFICADO Y CORRECTO`.

## Criterio Google actualizado

Fuentes oficiales consultadas:

- Google Search Central indica que el Rich Results Test sirve para comprobar qué rich results puede generar el structured data de una URL.
- Google recomienda Schema Markup Validator para validación genérica de Schema.org, sin validación específica de features de Google.
- Google mantiene `BreadcrumbList` como feature disponible en desktop en regiones e idiomas donde Google Search está disponible.
- Google Search Central documenta que la documentación de FAQ rich result fue retirada en junio de 2026 porque la función ya no aparece en Google Search desde mayo de 2026.

Conclusión: `FAQPage` no debe declararse como candidato real a rich result de Google en 2026. En MatchWalls debe considerarse una capa semántica Schema.org/GEO/AEO, no una promesa de resultado enriquecido FAQ.

## QA pública

URLs verificadas:

- España ES: `https://www.matchwalls.com/pages/papel-pintado-espana`.
- España EN: `https://www.matchwalls.com/en/pages/spain-wallpaper`.
- España FR: `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`.
- España DE: `https://www.matchwalls.com/de/pages/spanien-tapete`.
- España NL: `https://www.matchwalls.com/nl/pages/spanje-behang`.
- Francia ES: `https://www.matchwalls.com/pages/papel-pintado-francia`.
- Francia EN: `https://www.matchwalls.com/en/pages/french-wallpaper`.
- Francia FR: `https://www.matchwalls.com/fr/pages/papier-peint-en-france`.
- Francia DE: `https://www.matchwalls.com/de/pages/franzosische-tapete`.
- Francia NL: `https://www.matchwalls.com/nl/pages/frans-behang`.

Resultado común de las 10 URLs:

- HTTP 200.
- Canonical propio correcto.
- Sin `noindex`.
- Permitidas para Googlebot por `robots.txt`.
- JSON-LD parseable sin errores.
- `WebPage` correcto.
- `FAQPage` correcto.
- Preguntas y respuestas del FAQ presentes en contenido visible.
- `BreadcrumbList` correcto.
- Candidatura Google Breadcrumb rich result: `VERIFICADO Y CORRECTO`.
- Candidatura Google FAQ rich result: no se declara; función retirada por Google en 2026.
- Capa GEO/AEO: `VERIFICADO Y CORRECTO`.

Archivo de evidencia:

- `qa-publico-MW-GEO-LANDINGS-SPAIN-FRANCE-RICH-RESULTS-POSTCHECK-012L7-2026-07-04.csv`.

## QA con user-agent Googlebot

Se comprobó la respuesta pública con user-agent de Googlebot.

Resultado común de las 10 URLs:

- HTTP 200.
- Canonical correcto.
- JSON-LD parseable sin errores.
- Tipos `WebPage`, `FAQPage` y `BreadcrumbList` presentes.

Estado: `VERIFICADO Y CORRECTO`.

Archivo de evidencia:

- `qa-googlebot-MW-GEO-LANDINGS-SPAIN-FRANCE-RICH-RESULTS-POSTCHECK-012L7-2026-07-04.csv`.

## Limitaciones

- No se ejecutó Google Rich Results Test manual interactivo desde Search Console/Rich Results Test porque no existe una API oficial documentada para automatizarlo de forma fiable dentro del flujo.
- La validación realizada confirma HTML público, JSON-LD, canonical, robots, visibilidad de FAQ y consistencia técnica.
- No garantiza ranking, indexación, rich result efectivo, cita en IA ni tráfico.

## Recomendación

Mantener el schema publicado.

Actualizar la terminología futura del programa:

- `BreadcrumbList`: candidato real a rich result de Google.
- `WebPage` + `FAQPage`: capa semántica para comprensión, Schema.org, GEO/AEO y sistemas IA.
- No prometer FAQ rich results en Google.

## Estado final

`VERIFICADO Y CORRECTO`

El lote 012L7 queda cerrado como postcheck de solo lectura.
