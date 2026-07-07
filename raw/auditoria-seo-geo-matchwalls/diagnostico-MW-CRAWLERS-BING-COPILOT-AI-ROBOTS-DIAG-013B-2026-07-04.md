# Diagn?stico MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B ? 2026-07-04

## Alcance

Diagn?stico de solo lectura para comprobar la elegibilidad t?cnica b?sica de MatchWalls ante buscadores, navegadores/capas de b?squeda e IA/GEO/AGEO. No se ha modificado Shopify, LangShop, tema, p?ginas, robots.txt, sitemaps, SEO fields, handles, URLs ni mercados.

## Documentos le?dos

- `addendum-plan-operativo-vigente-2026-07-04.md`.
- `programa-ejecucion-seo-geo.md`.
- `lista-maestra-errores-cambios-evoluciones-mejoras.md`.
- `robots-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.txt` como evidencia hist?rica.
- Registro de cambios reciente, con bloqueo `012O` escalado a Shopify Engineering/TMS.

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

- `https://www.matchwalls.com/robots.txt`: `200`, guardado en `C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\robots-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.txt`.
- `https://www.matchwalls.com/sitemap.xml`: `200`.
- `https://www.matchwalls.com/agents.md`: `200` y aparece en `sitemap_agentic_discovery.xml`.
- `https://www.matchwalls.com/.well-known/ucp`: `200`.
- `https://www.matchwalls.com/indexnow.txt`: `404`; no prueba ausencia total de IndexNow porque la key puede tener otro nombre, pero no hay key p?blica en ruta obvia.
- `https://www.matchwalls.com/llms.txt`: `NO ACCESIBLE` en este intento por timeout; no se usa como evidencia.
- Sitemaps detectados: `29`.
- URLs en sitemaps p?blicos contadas: `7274`.
- Idiomas/mercados en sitemap: base ES, EN, FR, DE, NL, adem?s de IT y PT publicados aunque fuera de prioridad activa.

## Robots.txt actual

`VERIFICADO PERO MEJORABLE`

El `robots.txt` solo declara estos grupos:

- `User-agent: *`
- `User-agent: adsbot-google`

No hay reglas expl?citas para `OAI-SearchBot`, `ChatGPT-User`, `GPTBot`, `Claude-SearchBot`, `ClaudeBot`, `PerplexityBot`, `Perplexity-User`, `Applebot`, `Applebot-Extended`, `Google-Extended`, `Meta-WebIndexer`, `FacebookBot`, `Grok` o `xAI`.

La consecuencia pr?ctica es que los crawlers principales quedan permitidos por herencia del grupo `*` para contenido p?blico, y se bloquean rutas transaccionales/trampas como carrito, checkout, filtros, sort, recomendaciones y scripts internos.

## Matriz resumida de permisos

`VERIFICADO PERO MEJORABLE`

- Googlebot/Bingbot/Applebot/OAI-SearchBot/Claude-SearchBot/PerplexityBot: contenido p?blico permitido.
- ChatGPT-User/Perplexity-User/Claude-User: contenido p?blico permitido por robots, aunque algunos fetchers de usuario tienen comportamiento especial seg?n su documentaci?n.
- GPTBot/ClaudeBot/Google-Extended/Applebot-Extended: permitidos impl?citamente; esto equivale a no separar todav?a b?squeda/citaci?n frente a entrenamiento/uso de modelos.
- Cart/checkout/account/recommendations/filtros/sort/traps: bloqueados correctamente por regla m?s espec?fica.

La matriz completa est? en `C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\robots-matrix-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.csv`.

## Bing, Edge, Copilot, Yahoo e IndexNow

`VERIFICADO PERO MEJORABLE`

- Bingbot est? permitido para contenido p?blico.
- El sitemap est? referenciado desde robots.txt.
- Yahoo debe tratarse operativamente v?a Bing Webmaster Tools, salvo que existan datos propios separados.
- Bing Webmaster Tools no est? verificado en este lote: `NO ACCESIBLE`.
- IndexNow no est? verificado: no se encontr? key en `/indexnow.txt`; requiere diagn?stico espec?fico antes de implementar.
- Bing/Microsoft indica que `NOARCHIVE` puede excluir contenido de Bing Chat/Copilot answers, y `NOCACHE` limita el uso a URL/t?tulo/snippet. Por tanto, antes de a?adir controles Bing hay que decidir si priorizamos citaci?n o restricci?n.

## Google, Chrome y Gemini

`VERIFICADO PERO MEJORABLE`

- Googlebot est? permitido para contenido p?blico.
- Google-Extended est? permitido impl?citamente por `User-agent:*`; no hay decisi?n expl?cita sobre uso en Gemini/Vertex fuera de Search.
- Google confirma que AI Overviews/AI Mode no requieren schema o archivos especiales para IA: requieren indexabilidad, contenido textual visible, enlaces internos, experiencia de p?gina y structured data coherente.

## ChatGPT / OpenAI

`VERIFICADO PERO MEJORABLE`

- `OAI-SearchBot` y `ChatGPT-User` est?n permitidos por herencia del grupo `*`.
- `GPTBot` tambi?n est? permitido por herencia, por lo que no existe separaci?n expl?cita entre elegibilidad de b?squeda/citaci?n y entrenamiento.
- Recomendaci?n: en el siguiente lote, proponer pol?tica expl?cita que permita search/user fetch y deje a Daniel decidir entrenamiento.

## Claude / Anthropic

`VERIFICADO PERO MEJORABLE`

- `Claude-SearchBot`, `Claude-User` y `ClaudeBot` quedan permitidos por herencia.
- Anthropic documenta que bloquear `Claude-SearchBot` puede reducir visibilidad/precisi?n en resultados de b?squeda de Claude.
- Recomendaci?n: permitir expl?citamente `Claude-SearchBot`/`Claude-User`; decidir por separado `ClaudeBot`.

## Perplexity / Comet

`VERIFICADO PERO MEJORABLE`

- `PerplexityBot` y `Perplexity-User` quedan permitidos por herencia.
- Perplexity recomienda permitir sus IP oficiales si hay WAF/CDN; esta parte no est? verificada porque no tenemos acceso a WAF/CDN en este lote.

## Apple / Safari / Siri / Spotlight

`VERIFICADO PERO MEJORABLE`

- `Applebot` y `Applebot-Extended` quedan permitidos por herencia.
- Apple permite separar descubrimiento (`Applebot`) de uso para foundation models (`Applebot-Extended`). No hay decisi?n expl?cita en MatchWalls.

## Meta AI y Grok/xAI

- Meta AI: `DECLARADO PERO NO VERIFICADO`. `Meta-WebIndexer`/`FacebookBot` quedar?an permitidos por `*`, pero la fuente oficial no se pudo leer completa en este lote.
- Grok/xAI: `NO ACCESIBLE`. No se ha verificado una fuente primaria fiable de user-agents xAI/Grok; no se deben inventar reglas.

## Riesgos detectados

`REQUIERE DECISION HUMANA`

1. La pol?tica IA actual es demasiado impl?cita: permite casi todo lo p?blico, incluido entrenamiento, sin decisi?n expl?cita.
2. No hay evidencia de IndexNow activo.
3. Bing Webmaster Tools/Yahoo/Copilot no est?n verificados con acceso real.
4. WAF/CDN no est? auditado; las pruebas p?blicas intensivas pueden generar `429`, por lo que no se debe hacer crawling agresivo.
5. IT/PT siguen en sitemap aunque fuera de prioridad activa; no es necesariamente error, pero debe recordarse en cada lote multiling?e.
6. El bloqueo `012O` sigue abierto con Shopify Engineering/TMS; no se debe mezclar con cambios de crawlers.

## Recomendaci?n de siguiente lote

`MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C`

Solo propuesta, sin escritura. Objetivo:

- Mantener permitido: Googlebot, Bingbot, Applebot, OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User.
- Decidir expl?citamente entrenamiento/model training: GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, Meta-WebIndexer/FacebookBot si procede.
- Definir si se crea `llms.txt` o si se mantiene fuera por no ser est?ndar requerido.
- Definir IndexNow en lote separado: `MW-INDEXNOW-BING-COPILOT-DESIGN-013D`.

## Archivos generados

- Robots: `C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\robots-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.txt`
- Matriz robots: `C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\robots-matrix-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.csv`
- Sitemaps: `C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\sitemap-summary-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.csv`
- Controles meta intento: `C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\meta-controls-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.csv`
- Matriz pol?tica: `C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\policy-matrix-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.csv`
- Datos JSON: `C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\diagnostico-data-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.json`

## Fuentes oficiales consultadas

- OpenAI crawlers: https://developers.openai.com/api/docs/bots
- Anthropic crawlers: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- Perplexity crawlers: https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- Google AI features: https://developers.google.com/search/docs/appearance/ai-features
- Google crawlers / Google-Extended: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers
- Applebot / Applebot-Extended: https://support.apple.com/en-us/119829
- Bing content controls for Bing Chat/Copilot: https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat
- IndexNow documentation: https://www.indexnow.org/documentation
- Yahoo Search submission / Bing dependency: https://help.yahoo.com/kb/SLN2217.html

## Estado final

`VERIFICADO PERO MEJORABLE`

MatchWalls es rastreable para buscadores y crawlers IA principales en contenido p?blico. No hay bloqueo cr?tico en robots.txt para Google/Bing/ChatGPT/Claude/Perplexity/Apple. El adeudo real es estrat?gico y operativo: formalizar pol?tica por bot, verificar Bing Webmaster/IndexNow/WAF y decidir entrenamiento vs citaci?n.
