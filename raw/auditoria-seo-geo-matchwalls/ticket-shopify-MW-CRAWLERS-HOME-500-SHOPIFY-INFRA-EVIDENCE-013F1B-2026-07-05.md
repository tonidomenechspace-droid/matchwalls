# Shopify Support ticket draft — Home returns intermittent 500 for crawlers and browser

Subject:

`Intermittent 500 on homepage https://www.matchwalls.com/ — Storefront Rendering / Infrastructure escalation requested with request IDs and headers`

Message:

Hello Shopify Support,

We need help investigating an intermittent `500` error on our storefront homepage:

`https://www.matchwalls.com/`

This is not a content-edit request. Please do not change theme files, published theme, page content, menus, translations, markets, SEO fields, handles, URLs, redirects, apps, `robots.txt`, sitemap or IndexNow configuration.

## Expected behavior

The homepage should consistently return `200 OK` HTML for normal browser requests and legitimate crawler user-agents.

## Actual behavior

The same homepage intermittently returns Shopify's generic `500` error page.

The error response body begins with:

```txt
<!-- The source of truth for this generic error page
```

This does not look like a WAF block, robots issue, captcha, `403`, `401` or `429`. It looks like a storefront render / infrastructure / CDN / shard issue.

## Important context

Other public resources tested correctly:

- `https://www.matchwalls.com/robots.txt`: `200 OK`
- `https://www.matchwalls.com/sitemap.xml`: `200 OK`
- `https://www.matchwalls.com/llms.txt`: `200 OK`
- `https://www.matchwalls.com/agents.md`: `200 OK`
- `https://www.matchwalls.com/pages/papel-pintado-espana`: `200 OK`
- `https://www.matchwalls.com/en/collections/`: `200 OK`

So the issue appears concentrated on the homepage render, not a global robots/crawler block.

## Recheck 1 — status pattern

Date/time: 2026-07-05 around 13:05 Europe/Madrid  
URL: `https://www.matchwalls.com/`

We tested 5 user-agents, 3 requests each:

- Chrome: 3/3 returned `200`
- Googlebot: 2/3 returned `200`, 1/3 returned `500`
- Bingbot: 1/3 returned `200`, 2/3 returned `500`
- OAI-SearchBot: 1/3 returned `200`, 2/3 returned `500`
- PerplexityBot: 0/3 returned `200`, 3/3 returned `500`

Total: 8 failures out of 15 requests.

## Recheck 2 — headers captured

Date/time: 2026-07-05 around 13:12-13:13 Europe/Madrid  
URL: `https://www.matchwalls.com/`

We captured headers from both `200` and `500` responses.

Total:

- 20 requests
- 6 returned `200`
- 14 returned `500`

Common headers / server timing observed on `500` responses:

- `server: cloudflare`
- `content-type: text/html; charset=utf-8`
- `cache-control: private, no-store`
- `edge;desc="MAD"`
- `theme;desc="178399019384"`
- `pageType;desc="index"`
- `servedBy;desc="..."`
- `render;dur=...`

`x-shopify-stage` was not present in the captured responses.

## Examples of 500 responses with headers

Bingbot:

- `x-request-id`: `7d3b7d2d-fec8-45d5-8fe1-de787c4f25ee-1783249963`
- `cf-ray`: `a165efafee8a2183-MAD`
- `servedBy`: `mvhx`
- `render_ms`: `1524`
- `cache-control`: `private, no-store`

Bingbot:

- `x-request-id`: `99ff8a84-70ce-45c7-a6b2-75e4188fe6cc-1783249969`
- `cf-ray`: `a165efd3bc5a2183-MAD`
- `servedBy`: `mp8j`
- `render_ms`: `1579`
- `cache-control`: `private, no-store`

OAI-SearchBot:

- `x-request-id`: `49062a87-3951-46e0-8cc6-f2d4c9cacd1e-1783249972`
- `cf-ray`: `a165efe70cec2183-MAD`
- `servedBy`: `jxcr`
- `render_ms`: `1419`
- `cache-control`: `private, no-store`

OAI-SearchBot:

- `x-request-id`: `deff5efe-ab87-4e0f-bd10-7c9ade430ff5-1783249981`
- `cf-ray`: `a165f01ece612183-MAD`
- `servedBy`: `vs2h`
- `render_ms`: `1539`
- `cache-control`: `private, no-store`

PerplexityBot:

- `x-request-id`: `7269f21e-e073-45e4-8b77-70956861b834-1783249984`
- `cf-ray`: `a165f0323f842183-MAD`
- `servedBy`: `sdsh`
- `render_ms`: `1229`
- `cache-control`: `private, no-store`

Googlebot:

- `x-request-id`: `6e430cb7-655e-4749-968d-4e4f0ea0c95c-1783249998`
- `cf-ray`: `a165f089cc712183-MAD`
- `servedBy`: `jw58`
- `render_ms`: `1195`
- `cache-control`: `private, no-store`

Chrome:

- `x-request-id`: `a639dbfb-c1c6-4c41-bfa7-b5e143324282-1783250006`
- `cf-ray`: `a165f0bbfc662183-MAD`
- `servedBy`: `8p5v`
- `render_ms`: `1471`
- `cache-control`: `private, no-store`

Chrome:

- `x-request-id`: `b56767e7-b84c-4496-93df-52ce2410e934-1783250012`
- `cf-ray`: `a165f0e2f8d12183-MAD`
- `servedBy`: `vs2h`
- `render_ms`: `1429`
- `cache-control`: `private, no-store`

## Examples of 200 responses in the same window

Bingbot:

- `x-request-id`: `88787b17-e25a-47c3-adf1-e2f3a6d94368-1783249959`
- `cf-ray`: `a165ef998cbf2183-MAD`
- `servedBy`: `5m4w`

OAI-SearchBot:

- `x-request-id`: `7a9ba609-a381-4125-8f56-5b138231eb03-1783249975`
- `cf-ray`: `a165effa7e772183-MAD`
- `servedBy`: `r9cv`

Googlebot:

- `x-request-id`: `7a233d64-edd5-4bed-8efc-bf73995d82d4-1783249996`
- `cf-ray`: `a165f07fbcc22183-MAD`
- `servedBy`: `k77s`

Chrome:

- `x-request-id`: `f054d91b-64bc-4ddf-a067-926a2d8571b1-1783250015`
- `cf-ray`: `a165f0f689112183-MAD`
- `servedBy`: `2t67`

## Request

Please escalate this to Storefront Rendering / Infrastructure and investigate the request IDs above.

Questions:

1. Are these `500` responses caused by storefront rendering, an edge/cache shard, an app/theme render dependency, or Shopify infrastructure?
2. Can Shopify confirm why the same URL returns both `200` and `500` in the same short time window, same edge region `MAD`, same theme `178399019384`, and `pageType=index`?
3. Can Shopify inspect the `servedBy` values and `render;dur` timings for failing requests?
4. Is there a safe cache/render purge or infrastructure action Shopify can perform without changing content, theme, URLs, translations, SEO fields or apps?
5. Should we avoid further homepage/theme changes while Shopify investigates?

Attached evidence:

- Recheck status CSV: `recheck-MW-CRAWLERS-HOME-500-SHOPIFY-INFRA-EVIDENCE-013F1-2026-07-05.csv`
- Headers CSV: `headers-MW-CRAWLERS-HOME-500-HEADERS-RECHECK-013F1B-2026-07-05.csv`

Thank you.

