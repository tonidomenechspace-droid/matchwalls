# Shopify Support ticket draft — Home returns intermittent 500 for crawlers and browser

Subject:

`Intermittent 500 on homepage https://www.matchwalls.com/ for browser and crawler user-agents — Storefront Rendering / Infrastructure escalation requested`

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

## Latest recheck

Date/time: 2026-07-05 around 13:05 Europe/Madrid  
URL: `https://www.matchwalls.com/`

We tested 5 user-agents, 3 requests each:

- Chrome: 3/3 returned `200`
- Googlebot: 2/3 returned `200`, 1/3 returned `500`
- Bingbot: 1/3 returned `200`, 2/3 returned `500`
- OAI-SearchBot: 1/3 returned `200`, 2/3 returned `500`
- PerplexityBot: 0/3 returned `200`, 3/3 returned `500`

Total: 8 failures out of 15 requests.

## Request IDs for 500 responses

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

## Request IDs for successful 200 responses in the same window

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

## Context

Other public resources tested correctly:

- `https://www.matchwalls.com/robots.txt`: `200 OK`
- `https://www.matchwalls.com/sitemap.xml`: `200 OK`
- `https://www.matchwalls.com/llms.txt`: `200 OK`
- `https://www.matchwalls.com/agents.md`: `200 OK`
- `https://www.matchwalls.com/pages/papel-pintado-espana`: `200 OK`
- `https://www.matchwalls.com/en/collections/`: `200 OK`

So the issue appears concentrated on the homepage render, not a global robots/crawler block.

## Request

Please escalate this to Storefront Rendering / Infrastructure and investigate the request IDs above.

Questions:

1. Are these `500` responses caused by a storefront rendering shard, edge cache, app/theme render dependency, or Shopify infrastructure?
2. Can Shopify confirm why the same URL returns both `200` and `500` in the same short time window?
3. Is there a safe cache/render purge or infrastructure action Shopify can perform without changing content, theme, URLs, translations, SEO fields or apps?
4. Should we avoid further homepage/theme changes while Shopify investigates?

Thank you.

