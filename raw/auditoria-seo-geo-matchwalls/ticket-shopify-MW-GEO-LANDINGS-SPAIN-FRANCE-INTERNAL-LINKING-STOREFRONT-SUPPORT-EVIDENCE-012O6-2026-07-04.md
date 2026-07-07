# Shopify Support ticket draft

Subject: Storefront intermittently serves stale Page body HTML across locales despite Admin updatedAt/digests — purge/render cache investigation requested

Hello Shopify Support,

We need help investigating an intermittent storefront rendering issue on two Online Store pages.

## Expected vs actual

Expected:

After updating two published Shopify Pages, all public locale URLs should consistently render the current `body_html`, including a new cross-country internal linking block between the Spain and France pages.

Actual:

Shopify Admin GraphQL confirms the current page body and translations are correct, but public storefront requests intermittently return older HTML that does not include the new block. The issue varies by locale, user-agent and request/shard, while the same published theme is reported in headers.

## Important constraints

Please do not change handles, URLs, page titles, body HTML, translations, markets, theme files, published theme, SEO fields, redirects, menus, products or collections.

We only need the technical source of the stale/inconsistent storefront rendering and, if appropriate, a safe purge/flush of the relevant storefront/render/cache variants.

## Affected resources

Spain page:

- GID: `gid://shopify/Page/687276622200`
- Base handle: `papel-pintado-espana`
- Admin `updatedAt`: `2026-07-04T14:38:21Z`
- `body_html` digest: `746c832dbeacf56abf7095b8edb5774803e1243046aec5e55ae20ee10fc2f7a8`

Public URLs:

- `https://www.matchwalls.com/pages/papel-pintado-espana`
- `https://www.matchwalls.com/en/pages/spain-wallpaper`
- `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`
- `https://www.matchwalls.com/de/pages/spanien-tapete`
- `https://www.matchwalls.com/nl/pages/spanje-behang`

France page:

- GID: `gid://shopify/Page/687276654968`
- Base handle: `papel-pintado-francia`
- Admin `updatedAt`: `2026-07-04T14:39:03Z`
- `body_html` digest: `1e4ecb69b20f08101ebc238004b89f63143aab91f16e4b6083ebe158847e623d`

Public URLs:

- `https://www.matchwalls.com/pages/papel-pintado-francia`
- `https://www.matchwalls.com/en/pages/french-wallpaper`
- `https://www.matchwalls.com/fr/pages/papier-peint-en-france`
- `https://www.matchwalls.com/de/pages/franzosische-tapete`
- `https://www.matchwalls.com/nl/pages/frans-behang`

## Admin state confirmed

Shopify Admin GraphQL confirms:

- Both pages are published.
- The new cross-country linking block exists in the Spanish base `body`.
- EN, FR, DE and NL `body_html` translations contain the equivalent block.
- Translations are `outdated:false`.
- Handles and titles are intact.

## Storefront QA evidence

QA matrix 1:

- 80 public requests.
- 10 locale URLs.
- User-agents: browser Chrome, Googlebot, Bingbot and generic AI-search QA user-agent.
- PASS: 11.
- FAIL: 69.
- `noindex`: 0.
- Canonical mismatches: 0.
- Most responses report `theme;desc="178399019384"` and `pageType;desc="page"`.
- `cf-cache-status` is `DYNAMIC`.

QA recheck:

- 40 public requests.
- PASS: 6.
- FAIL: 34.
- Relevant failing responses are HTTP 200.
- No `noindex`.
- Canonicals OK.
- Theme in headers: `178399019384`.
- `cf-cache-status`: `DYNAMIC`.

## Current failing request examples

Spain ES, browser:

- URL: `https://www.matchwalls.com/pages/papel-pintado-espana`
- Expected body link: `href="/pages/papel-pintado-francia"`
- Result: link missing
- Status: 200
- `x-request-id`: `7fea94a5-0d7a-4817-89aa-26300d73679d-1783177654`
- `servedBy`: `jhkr`
- `theme`: `178399019384`
- `content-language`: `es-ES`
- `cf-cache-status`: `DYNAMIC`

Spain EN, Googlebot:

- URL: `https://www.matchwalls.com/en/pages/spain-wallpaper`
- Expected body link: `href="/en/pages/french-wallpaper"`
- Result: link missing
- Status: 200
- `x-request-id`: `edd4b1f6-b3d3-436e-b5a9-def365e5fd88-1783177658`
- `servedBy`: `7lh9`
- `theme`: `178399019384`
- `content-language`: `en-ES`
- `cf-cache-status`: `DYNAMIC`

France ES, browser:

- URL: `https://www.matchwalls.com/pages/papel-pintado-francia`
- Expected body link: `href="/pages/papel-pintado-espana"`
- Result: link missing
- Status: 200
- `x-request-id`: `816649a6-85b9-40bc-a8b6-7317c9ad1d7e-1783177666`
- `servedBy`: `ww4c`
- `theme`: `178399019384`
- `content-language`: `es-ES`
- `cf-cache-status`: `DYNAMIC`

France FR, Googlebot:

- URL: `https://www.matchwalls.com/fr/pages/papier-peint-en-france`
- Expected body link: `href="/fr/pages/papier-peint-en-espagne"`
- Result: link missing
- Status: 200
- `x-request-id`: `35dd691c-a833-4b4e-b83e-9dcd18361142-1783177672`
- `servedBy`: `8492`
- `theme`: `178399019384`
- `content-language`: `fr-ES`
- `cf-cache-status`: `DYNAMIC`

## Current passing request examples

The inconsistency is important because some requests do render the new body correctly:

Spain DE, browser:

- URL: `https://www.matchwalls.com/de/pages/spanien-tapete`
- Expected body link found: `href="/de/pages/franzosische-tapete"`
- Status: 200
- `x-request-id`: `462c1375-4875-4985-a471-b1ac2a96abb6-1783177662`
- `servedBy`: `r9cv`
- `theme`: `178399019384`
- `content-language`: `de-ES`
- `cf-cache-status`: `DYNAMIC`

France FR, browser:

- URL: `https://www.matchwalls.com/fr/pages/papier-peint-en-france`
- Expected body link found: `href="/fr/pages/papier-peint-en-espagne"`
- Status: 200
- `x-request-id`: `cecb72d8-7cb6-48ce-a26c-009bb31f4683-1783177671`
- `servedBy`: `nxlw`
- `theme`: `178399019384`
- `content-language`: `fr-ES`
- `cf-cache-status`: `DYNAMIC`

## Steps already attempted

1. Normal page body update: Admin correct, storefront not stable.
2. Same-value update/purge attempt: accepted, but did not produce stable storefront rendering.
3. Invisible whitespace bump to force a real `updatedAt`: Admin updated correctly, translations re-registered, but storefront still not stable.
4. Matrix rechecks with multiple user-agents and locales: issue persists.

## Questions for Shopify

1. Can Shopify confirm whether the above request IDs are serving stale rendered HTML for these Page resources?
2. Are Online Store Page body renders cached by locale, user-agent, edge or renderer shard in a way that could explain this mismatch?
3. Can Shopify safely purge/flush storefront rendered HTML/cache variants for:
   - `gid://shopify/Page/687276622200`
   - `gid://shopify/Page/687276654968`
   - all locale URLs listed above?
4. Is there any known interaction between translated page body content and storefront render cache that could cause `outdated:false` Admin translations to render inconsistently?

Attached evidence:

- QA CSV with 80 requests.
- Recheck CSV with 40 requests.
- Admin-confirmed GIDs, `updatedAt` values and `body_html` digests.

Thank you.

