# LangShop Support ticket draft

Subject: Translated Shopify Page body appears correct in Admin/LangShop state but storefront intermittently renders older HTML — translation cache/flush check requested

Hello LangShop Support,

We need help investigating an intermittent storefront rendering issue affecting translated Shopify Pages.

## Expected vs actual

Expected:

Two Shopify Pages were updated with a cross-country internal linking block. The base Spanish body and EN, FR, DE and NL translations contain the new block and Shopify Admin reports translations as `outdated:false`.

Actual:

Public storefront requests intermittently render older HTML without the translated block. Some locale/user-agent requests show the new block and others do not. This suggests a possible translation/render cache mismatch or app-side cache, although we cannot confirm the exact source without LangShop support.

## Important constraints

Please do not change handles, URLs, page titles, body HTML, translations, markets, theme files, published theme, SEO fields, redirects, menus, products or collections.

We only need confirmation of whether LangShop stores/caches page `body_html` translations outside Shopify translations, and whether a safe backend cache flush/sync can be performed for the affected page GIDs/locales.

## Affected resources

Spain page:

- Shopify GID: `gid://shopify/Page/687276622200`
- Base handle: `papel-pintado-espana`
- Admin `updatedAt`: `2026-07-04T14:38:21Z`
- Shopify `body_html` digest: `746c832dbeacf56abf7095b8edb5774803e1243046aec5e55ae20ee10fc2f7a8`

Locale URLs:

- ES: `https://www.matchwalls.com/pages/papel-pintado-espana`
- EN: `https://www.matchwalls.com/en/pages/spain-wallpaper`
- FR: `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`
- DE: `https://www.matchwalls.com/de/pages/spanien-tapete`
- NL: `https://www.matchwalls.com/nl/pages/spanje-behang`

France page:

- Shopify GID: `gid://shopify/Page/687276654968`
- Base handle: `papel-pintado-francia`
- Admin `updatedAt`: `2026-07-04T14:39:03Z`
- Shopify `body_html` digest: `1e4ecb69b20f08101ebc238004b89f63143aab91f16e4b6083ebe158847e623d`

Locale URLs:

- ES: `https://www.matchwalls.com/pages/papel-pintado-francia`
- EN: `https://www.matchwalls.com/en/pages/french-wallpaper`
- FR: `https://www.matchwalls.com/fr/pages/papier-peint-en-france`
- DE: `https://www.matchwalls.com/de/pages/franzosische-tapete`
- NL: `https://www.matchwalls.com/nl/pages/frans-behang`

## Admin translation state confirmed

Shopify Admin GraphQL confirms:

- The base Spanish body contains the new block.
- EN, FR, DE and NL `body_html` translations contain the equivalent block.
- Translation records are `outdated:false`.
- Handles and titles remain intact.

## Storefront QA evidence

QA matrix:

- 80 public requests.
- 10 locale URLs.
- User-agents: browser Chrome, Googlebot, Bingbot and generic AI-search QA user-agent.
- PASS: 11.
- FAIL: 69.
- `noindex`: 0.
- Canonical mismatches: 0.
- Most responses report the expected published theme `178399019384`.
- `cf-cache-status`: `DYNAMIC`.

Current recheck:

- 40 public requests.
- PASS: 6.
- FAIL: 34.
- Relevant failing responses are HTTP 200.
- No `noindex`.
- Canonicals OK.
- Theme in headers: `178399019384`.

## Examples of missing translated links

Spain EN:

- URL: `https://www.matchwalls.com/en/pages/spain-wallpaper`
- Expected body link: `href="/en/pages/french-wallpaper"`
- Result: missing in public HTML for Googlebot request.
- `x-request-id`: `edd4b1f6-b3d3-436e-b5a9-def365e5fd88-1783177658`
- `servedBy`: `7lh9`
- `content-language`: `en-ES`

Spain FR:

- URL: `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`
- Expected body link: `href="/fr/pages/papier-peint-en-france"`
- Result: missing in public HTML for Bingbot request.
- `x-request-id`: `e7025196-795e-4189-8b8b-42a333cd3cb0-1783177660`
- `servedBy`: `9gtz`
- `content-language`: `fr-ES`

France FR:

- URL: `https://www.matchwalls.com/fr/pages/papier-peint-en-france`
- Expected body link: `href="/fr/pages/papier-peint-en-espagne"`
- Result: missing in public HTML for Googlebot request.
- `x-request-id`: `35dd691c-a833-4b4e-b83e-9dcd18361142-1783177672`
- `servedBy`: `8492`
- `content-language`: `fr-ES`

France NL:

- URL: `https://www.matchwalls.com/nl/pages/frans-behang`
- Expected body link: `href="/nl/pages/spanje-behang"`
- Result: missing in public HTML for browser request.
- `x-request-id`: `98d8f723-8d7f-4d98-9a74-beaf8f8637df-1783177676`
- `servedBy`: `kzpw`
- `content-language`: `nl-ES`

## Examples where the new translated block does appear

Spain DE:

- URL: `https://www.matchwalls.com/de/pages/spanien-tapete`
- Expected body link found: `href="/de/pages/franzosische-tapete"`
- `x-request-id`: `462c1375-4875-4985-a471-b1ac2a96abb6-1783177662`
- `servedBy`: `r9cv`
- `content-language`: `de-ES`

France FR:

- URL: `https://www.matchwalls.com/fr/pages/papier-peint-en-france`
- Expected body link found: `href="/fr/pages/papier-peint-en-espagne"`
- `x-request-id`: `cecb72d8-7cb6-48ce-a26c-009bb31f4683-1783177671`
- `servedBy`: `nxlw`
- `content-language`: `fr-ES`

## Questions for LangShop

1. Does LangShop keep an app-side cache or storage layer for translated Shopify Page `body_html` values outside Shopify's translation records?
2. Can LangShop confirm whether the affected Page GIDs and locales are fully synced in LangShop backend?
3. Can LangShop safely flush/rebuild translated page body cache for:
   - `gid://shopify/Page/687276622200`
   - `gid://shopify/Page/687276654968`
   - locales EN, FR, DE and NL?
4. Could LangShop be serving different translated HTML variants depending on locale, user-agent, market or storefront render context?
5. Is there a recommended safe sync/publish/cache-refresh action that does not modify handles, URLs, body text or translations?

Attached evidence:

- QA CSV with 80 requests.
- Recheck CSV with 40 requests.
- Admin-confirmed GIDs, `updatedAt` values and `body_html` digests.

Thank you.

