# Propuesta MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C — 2026-07-04

## Estado

`REQUIERE DECISION HUMANA`

Este documento es una propuesta de politica. No se ha modificado Shopify, LangShop, `robots.txt`, tema, paginas, SEO fields, handles, URLs, mercados ni sitemaps.

## Punto de partida verificado en 013B

`VERIFICADO PERO MEJORABLE`

- `robots.txt` responde `200`.
- `sitemap.xml` responde `200`.
- `agents.md` responde `200` y esta incluido en `sitemap_agentic_discovery.xml`.
- `/.well-known/ucp` responde `200`.
- Los grupos reales de robots actuales son:
  - `User-agent: *`
  - `User-agent: adsbot-google`
- El grupo `User-agent: *` permite contenido publico y bloquea rutas privadas/trampa como carrito, checkout, account, recommendations, filtros, sort y `/cdn/wpm/*.js`.
- No hay reglas explicitas por crawler IA.
- Por tanto, los bots IA y buscadores que respetan robots quedan permitidos por herencia para contenido publico.

## Principio tecnico importante

`VERIFICADO Y CORRECTO`

No conviene anadir grupos explicitos tipo:

```txt
User-agent: OAI-SearchBot
Allow: /
```

si no se duplican tambien los bloqueos privados del grupo `*`.

Motivo: muchos crawlers aplican el grupo mas especifico. Si creamos un grupo especifico con solo `Allow: /`, ese bot podria dejar de heredar los `Disallow` actuales de carrito, checkout, filtros o endpoints internos.

Por eso, la politica mas segura no es "anadir todos los bots permitidos", sino:

1. mantener el grupo `*` como politica publica general;
2. anadir solo reglas especificas cuando queramos restringir algun bot concreto;
3. si se anaden grupos explicitos de permiso, duplicar los bloqueos privados actuales.

## Objetivo de la politica

Maximizar elegibilidad de MatchWalls para:

- Google Search, Google AI Overviews y AI Mode;
- Bing, Edge, Copilot y Yahoo via Bing;
- ChatGPT Search;
- Claude Search;
- Perplexity y Comet;
- Applebot, Safari, Siri y Spotlight;
- Meta AI si sus crawlers oficiales son confirmados;
- Grok/xAI solo cuando exista fuente primaria o evidencia real de logs.

No se garantizan rankings, indexacion, trafico ni citas IA.

## Politica propuesta por capas

### Capa 1 — buscadores esenciales

`VERIFICADO Y CORRECTO`

Mantener permitido el rastreo publico para:

- `Googlebot`
- `Googlebot-Image`
- `Googlebot-Video`
- `Storebot-Google`
- `bingbot`
- `msnbot`
- `Slurp` / Yahoo via Bing donde aplique
- `Applebot`

Accion propuesta: no cambiar robots. El grupo `*` ya permite contenido publico y conserva bloqueos privados.

### Capa 2 — IA de busqueda, citacion o fetch iniciado por usuario

`VERIFICADO PERO MEJORABLE`

Mantener permitido el acceso publico para:

- `OAI-SearchBot`
- `ChatGPT-User`
- `Claude-SearchBot`
- `Claude-User`
- `PerplexityBot`
- `Perplexity-User`
- `Applebot`

Accion propuesta: no cambiar robots todavia. El grupo `*` ya permite el acceso publico y mantiene los bloqueos privados.

Razon: estos bots o fetchers estan mas cerca de busqueda, citacion, respuestas con enlaces o recuperacion iniciada por usuario. Bloquearlos iria contra el objetivo de aumentar elegibilidad GEO/AGEO.

### Capa 3 — entrenamiento, foundation models o controles extendidos

`REQUIERE DECISION HUMANA`

Bots/controles a decidir separadamente:

- `GPTBot`
- `ClaudeBot`
- `Google-Extended`
- `Applebot-Extended`
- posibles bots Meta de entrenamiento si se verifican oficialmente.

Decision recomendada para MatchWalls ahora:

`OPCION A — VISIBILIDAD PRIMERO`

Mantenerlos permitidos por ahora, porque el objetivo declarado es maximizar descubrimiento, comprension y presencia en sistemas IA. Registrar que esta es una decision consciente y revisarla si aparecen:

- problemas de carga;
- abuso de crawling;
- riesgos legales/comerciales;
- decision de marca de no participar en entrenamiento;
- evidencia de que algun bot afecta negativamente a rendimiento o costes.

Opcion alternativa:

`OPCION B — CITACION SI, ENTRENAMIENTO NO`

Permitir bots de busqueda/citacion y bloquear entrenamiento. Esta opcion reduce exposicion a entrenamiento, pero puede limitar ciertos usos de contenido en sistemas IA fuera de buscadores clasicos.

Ejemplo de bloque futuro si Daniel decide entrenamiento NO:

```txt
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Applebot-Extended
Disallow: /
```

No ejecutar sin aprobacion exacta.

### Capa 4 — Meta AI

`DECLARADO PERO NO VERIFICADO`

Meta indica que ciertos crawlers pueden ayudar a citar y enlazar contenido en respuestas de Meta AI, pero en 013B no se pudo verificar completamente la fuente oficial desde el entorno de trabajo.

Accion propuesta:

- No anadir reglas Meta todavia.
- Verificar fuente oficial y/o logs reales antes de decidir.
- Si se confirma `Meta-WebIndexer` como bot de citacion, permitirlo.
- Decidir por separado cualquier bot de entrenamiento o agente externo de Meta.

### Capa 5 — Grok / xAI

`NO ACCESIBLE`

No se ha verificado una fuente primaria fiable de user-agents oficiales de Grok/xAI.

Accion propuesta:

- No inventar reglas `Grok`, `GrokBot`, `xAI` ni similares.
- Mantener acceso por `User-agent: *` mientras no haya evidencia.
- Reabrir decision si xAI publica documentacion oficial o si aparecen logs verificables.

## Bing / Copilot / Yahoo

`VERIFICADO PERO MEJORABLE`

Politica propuesta:

- Mantener `bingbot` permitido.
- No anadir `NOARCHIVE` ni `NOCACHE` globales.
- Evitar `NOARCHIVE` en paginas comerciales/citables porque Microsoft indica que puede impedir inclusion/citacion en Bing Chat/Copilot answers.
- Usar Bing Webmaster Tools como via principal para Bing, Edge, Copilot y Yahoo.
- Disenar IndexNow en lote separado.

Lote siguiente recomendado:

`MW-INDEXNOW-BING-COPILOT-DESIGN-013D`

## Google / Gemini

`VERIFICADO PERO MEJORABLE`

Politica propuesta:

- Mantener `Googlebot` permitido.
- No bloquear `Googlebot` para intentar controlar AI Overviews/AI Mode: Google indica que esas funciones se apoyan en los requisitos normales de Search.
- Decidir `Google-Extended` separadamente. Si se bloquea, no afecta a inclusion en Google Search, pero si puede afectar a Gemini/Vertex fuera de Search segun documentacion de Google.

Recomendacion actual: no bloquear `Google-Extended` hasta que Daniel tome decision especifica de entrenamiento/grounding fuera de Search.

## OpenAI / ChatGPT

`VERIFICADO PERO MEJORABLE`

Politica propuesta:

- Mantener permitido `OAI-SearchBot`.
- Mantener permitido `ChatGPT-User`.
- Decidir `GPTBot` separadamente.

Recomendacion actual: no bloquear `GPTBot` todavia si el objetivo prioritario es maxima elegibilidad IA. Revisar cuando exista politica de propiedad intelectual/entrenamiento formal.

## Claude / Anthropic

`VERIFICADO PERO MEJORABLE`

Politica propuesta:

- Mantener permitido `Claude-SearchBot`.
- Mantener permitido `Claude-User`.
- Decidir `ClaudeBot` separadamente.

Recomendacion actual: no bloquear `ClaudeBot` hasta decision expresa de entrenamiento.

## Perplexity / Comet

`VERIFICADO PERO MEJORABLE`

Politica propuesta:

- Mantener permitido `PerplexityBot`.
- Mantener permitido `Perplexity-User`.
- Auditar WAF/CDN si existe, porque Perplexity recomienda permitir por user-agent e IP oficial.

No hacer reglas WAF sin acceso real.

## Apple / Safari / Siri / Spotlight

`VERIFICADO PERO MEJORABLE`

Politica propuesta:

- Mantener permitido `Applebot`.
- Decidir `Applebot-Extended` separadamente.

Recomendacion actual: no bloquear `Applebot-Extended` todavia si el objetivo es maxima elegibilidad en Apple Intelligence/Siri/Search, salvo decision de entrenamiento NO.

## Propuesta ejecutiva recomendada

`REQUIERE DECISION HUMANA`

Recomendacion de Codex para MatchWalls ahora:

1. No modificar `robots.txt` todavia.
2. Declarar internamente politica `VISIBILIDAD PRIMERO`.
3. Mantener permitidos por ahora bots de busqueda, citacion, usuario y entrenamiento.
4. No anadir grupos explicitos de permiso para bots IA, para no romper los `Disallow` privados.
5. No bloquear training bots hasta decision humana especifica.
6. Avanzar antes con Bing Webmaster Tools e IndexNow.
7. Crear monitor mensual de logs/citas/impresiones antes de endurecer restricciones.

## Si Daniel quiere bloquear entrenamiento

`REQUIERE APROBACION EXACTA`

Se prepararia un lote separado:

`MW-CRAWLERS-AI-TRAINING-OPT-OUT-ROBOTS-PROPOSAL-013C2`

Alcance de propuesta:

- bloquear `GPTBot`;
- bloquear `ClaudeBot`;
- bloquear `Google-Extended`;
- bloquear `Applebot-Extended`;
- revisar Meta training bots solo tras fuente oficial.

No recomendado como primer movimiento si el objetivo principal es crecer en visibilidad IA.

## Lotes siguientes

1. `MW-INDEXNOW-BING-COPILOT-DESIGN-013D`
   - Solo diseno.
   - Definir clave, ubicacion, URLs elegibles, trigger de altas/cambios/bajas y pruebas.

2. `MW-BING-WEBMASTER-VERIFICATION-DIAG-013E`
   - Solo lectura/manual.
   - Verificar si MatchWalls esta dado de alta en Bing Webmaster Tools.

3. `MW-CRAWLERS-WAF-CDN-BOT-ALLOWLIST-DIAG-013F`
   - Solo lectura si hay acceso.
   - Verificar si CDN/WAF bloquea bots oficiales por IP/UA.

4. `MW-CRAWLERS-AI-POLICY-ROBOTS-IMPLEMENTATION-013G`
   - Solo si Daniel aprueba una politica exacta.
   - Escritura controlada en `robots.txt.liquid` o mecanismo equivalente de Shopify.

## Fuentes base

- OpenAI crawlers: https://developers.openai.com/api/docs/bots
- Anthropic crawlers: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- Perplexity crawlers: https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- Google AI features: https://developers.google.com/search/docs/appearance/ai-features
- Google crawlers / Google-Extended: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers
- Applebot / Applebot-Extended: https://support.apple.com/en-us/119829
- Bing content controls: https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat
- IndexNow: https://www.indexnow.org/documentation
- Yahoo/Bing submission: https://help.yahoo.com/kb/SLN2217.html

## Estado final de 013C

`VERIFICADO Y CORRECTO`

La propuesta queda preparada. No hay escritura ejecutada. La decision recomendada es no tocar robots todavia y avanzar con IndexNow/Bing Webmaster antes de cualquier restriccion de entrenamiento.
