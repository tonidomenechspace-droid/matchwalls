---
type: entity
status: active
created: 2026-07-07
updated: 2026-07-07
sources:
  - "[[wiki/Sources/hub-matchwalls-raw-folder]]"
tags:
  - wiki
  - entity
  - hub
  - matchwalls
---

# Hub MatchWalls

## Summary

Hub MatchWalls is the proposed strategic control layer for [[wiki/Entities/matchwalls|MatchWalls]]. It is intended to connect operational systems such as [[wiki/Entities/shopify|Shopify]], [[wiki/Entities/google-analytics|Google Analytics]], social channels, reporting, automation, and potentially [[wiki/Entities/n8n|n8n]] workflows.

## Key points

- The hub should be presented as a layer of control, data, automation, reporting, and process governance.
- [[wiki/Entities/shopify|Shopify]] remains the transactional ecommerce platform.
- The hub can increase [[wiki/Concepts/business-transferability|business transferability]] if it documents and centralizes processes, integrations, and reusable data.
- The current raw notes include sensitive credentials and must be sanitized before sharing.

## Open questions

- Which parts of the hub already exist versus which are planned.
- Which integrations are production, test, or only documented ideas.
- Which credentials need rotation because they appeared in local raw notes.
- Whether n8n will be the execution layer, the orchestration layer, or only an integration option.

## Related pages

- [[wiki/Entities/matchwalls|MatchWalls]]
- [[wiki/Entities/shopify|Shopify]]
- [[wiki/Entities/n8n|n8n]]
- [[wiki/Entities/google-analytics|Google Analytics]]
- [[wiki/Concepts/shopify-api|Shopify API]]
- [[wiki/Concepts/business-transferability|Business transferability]]
