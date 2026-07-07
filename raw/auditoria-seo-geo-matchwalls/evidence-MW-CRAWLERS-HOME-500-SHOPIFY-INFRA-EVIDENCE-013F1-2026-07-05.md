# MW-CRAWLERS-HOME-500-SHOPIFY-INFRA-EVIDENCE-013F1

Fecha: 2026-07-05  
Hora de registro: 13:06 Europe/Madrid  
Modo: solo lectura  
Estado final: `RIESGO CRITICO`

## Objetivo

Preparar un paquete de evidencia para Shopify Support / Storefront Rendering / Infrastructure sobre errores `500` intermitentes en:

`https://www.matchwalls.com/`

Este lote no modifica Shopify, tema, apps, `robots.txt`, Bing, IndexNow, CDN, WAF, URLs, handles, traducciones ni contenido.

## Contexto previo

`VERIFICADO Y CORRECTO`

El lote `MW-CRAWLERS-WAF-CDN-BOT-ALLOWLIST-DIAG-013F` detectó:

- No hay bloqueo global de bots en `robots.txt`.
- `robots.txt`, `sitemap.xml`, `llms.txt` y `agents.md` responden `200 OK`.
- Páginas internas probadas responden `200 OK`.
- La home devuelve `500` intermitente con página genérica Shopify.

## Revalidación 013F1

`RIESGO CRITICO`

Se realizó una revalidación breve de la home con 5 user-agents y 3 solicitudes por user-agent.

URL probada:

`https://www.matchwalls.com/`

Resultado agregado:

- Total solicitudes: 15
- Respuestas `200`: 7
- Respuestas `500`: 8
- Tasa de fallo observada: 53,3%

Desglose:

- Chrome: 3/3 `200`
- Googlebot: 2/3 `200`, 1/3 `500`
- Bingbot: 1/3 `200`, 2/3 `500`
- OAI-SearchBot: 1/3 `200`, 2/3 `500`
- PerplexityBot: 0/3 `200`, 3/3 `500`

Marcador de error recibido:

```txt
<!-- The source of truth for this generic error page
```

Este marcador corresponde a una página genérica de error Shopify, no a un bloqueo WAF clásico.

## Request IDs 500 actuales

`VERIFICADO Y CORRECTO`

Googlebot:

- `ebb41ee4-197e-4aff-9230-d8bdd8ca874f-1783249527`

Bingbot:

- `95bd8cb7-761c-4d67-ba46-d1a8b78c2d3e-1783249530`
- `4a63db8c-172c-4253-b811-1026c7a645e6-1783249536`

OAI-SearchBot:

- `a6d938cf-d633-4d50-9be3-38879ed25ee0-1783249539`
- `e54d0359-802e-4565-8bc3-36d43bc3a770-1783249544`

PerplexityBot:

- `74dab310-8c62-4b9b-93c0-f3e4b4133edd-1783249547`
- `8d6d52f6-256c-4d7a-9344-f024c27e75d8-1783249550`
- `9e22d769-158d-492d-b083-bf74c9acd833-1783249553`

## Request IDs 200 actuales

`VERIFICADO Y CORRECTO`

Chrome:

- `b91fa507-af3a-40c6-bf17-3f3343c2f14a-1783249512`
- `0374624f-17b6-4455-8f25-5b892be35242-1783249515`
- `e9be145f-171e-4d9b-a31b-d166e3b43df2-1783249518`

Googlebot:

- `8850e77f-ffc5-42b4-9f31-bcb11a4f146c-1783249521`
- `a4d8ff6c-2d09-4656-8461-3784e805eb16-1783249524`

Bingbot:

- `11805d23-40d3-4740-a4ce-a2c9367a4466-1783249533`

OAI-SearchBot:

- `83e9cb44-05d5-4a20-9e7c-a662cadbc043-1783249542`

## Interpretación técnica

`RIESGO CRITICO`

El patrón observado no encaja con:

- bloqueo por `robots.txt`;
- bloqueo WAF clásico;
- captcha;
- `403`;
- `401`;
- `429`;
- falta de sitemap;
- problema específico de IndexNow.

El patrón sí encaja con error intermitente de renderizado/infraestructura/caché/shard de Shopify Storefront en la home.

La home falla con bots y también había fallado previamente con navegador normal, por lo que no debe tratarse como una política de bots sino como estabilidad de storefront.

## Impacto SEO/GEO/AEO

`RIESGO CRITICO`

La home es recurso central para:

- descubrimiento de marca;
- rastreo inicial;
- autoridad de entidad MatchWalls;
- Bing/Copilot;
- Google;
- ChatGPT Search;
- Perplexity/Comet;
- Claude Search;
- Applebot.

Un `500` intermitente en home puede degradar rastreo, indexación, confianza, recrawl y citabilidad, aunque las páginas internas funcionen.

## Petición recomendada a Shopify

`VERIFICADO Y CORRECTO`

Solicitar escalación a:

- Storefront Rendering
- Infrastructure
- CDN/edge cache/rendering team

Pedir que investiguen los request IDs indicados, especialmente la diferencia entre respuestas `200` y `500` para la misma URL y mismo periodo.

## Qué NO debe cambiarse

`VERIFICADO Y CORRECTO`

Pedir expresamente que no se modifiquen:

- theme files;
- published theme;
- page content;
- menus;
- translations;
- markets;
- SEO fields;
- handles;
- URLs;
- redirects;
- apps;
- `robots.txt`;
- sitemap;
- IndexNow.

## Archivos del paquete

`VERIFICADO Y CORRECTO`

- `evidence-MW-CRAWLERS-HOME-500-SHOPIFY-INFRA-EVIDENCE-013F1-2026-07-05.md`
- `recheck-MW-CRAWLERS-HOME-500-SHOPIFY-INFRA-EVIDENCE-013F1-2026-07-05.csv`
- `ticket-shopify-MW-CRAWLERS-HOME-500-SHOPIFY-INFRA-EVIDENCE-013F1-2026-07-05.md`

## Próximo lote recomendado

`MW-HOME-RENDER-500-THEME-APP-DIAG-013F2`

Objetivo: diagnóstico de solo lectura de la home en Shopify/theme/apps para identificar si una sección, app embed, snippet o dependencia podría estar relacionada con el `500`.

Si Shopify confirma que el problema es infraestructura pura, mantener `013F2` en standby.

