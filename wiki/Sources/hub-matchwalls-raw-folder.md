---
type: source
status: active
created: 2026-07-07
updated: 2026-07-07
sources: []
tags:
  - wiki
  - source
  - hub
  - security
---

# Hub MatchWalls raw folder

## Summary

Source summary for the local folder `raw/hub_matchwalls/`. The folder contains notes about the planned [[wiki/Entities/hub-matchwalls|Hub MatchWalls]], Shopify API/n8n integration, Google/Analytics configuration, social channel configuration, and Shopify collections.

This source folder is intentionally not committed to Git because several files contain credentials, passwords, OAuth client secrets, and account access details.

## Key points

- The hub is framed as an external or strategic control layer connected to [[wiki/Entities/shopify|Shopify]].
- Shopify can be connected by custom app/API and by [[wiki/Entities/n8n|n8n]] credentials.
- The folder includes Google OAuth/Analytics configuration notes.
- The folder includes social channel configuration notes.
- The folder includes a Shopify collections export-like note with collection IDs, names, product counts, and rule conditions.

## Evidence

Local raw files reviewed:

- `raw/hub_matchwalls/prompt para codex.md`
- `raw/hub_matchwalls/conexion de shopify.md`
- `raw/hub_matchwalls/configuracion redes.md`
- `raw/hub_matchwalls/Datos de configuracion hub.md`
- `raw/hub_matchwalls/google analytics.md`
- `raw/hub_matchwalls/colecciones.md`

Sensitive evidence detected:

- Store/admin or account passwords.
- Social account credentials.
- Google OAuth client secrets.
- API/token setup instructions.

## Related pages

- [[wiki/Entities/hub-matchwalls|Hub MatchWalls]]
- [[wiki/Entities/matchwalls|MatchWalls]]
- [[wiki/Entities/shopify|Shopify]]
- [[wiki/Entities/n8n|n8n]]
- [[wiki/Entities/google-analytics|Google Analytics]]
- [[wiki/Concepts/shopify-api|Shopify API]]
- [[wiki/Concepts/business-transferability|Business transferability]]

## Maintenance notes

Do not copy secrets from this source into wiki pages. Keep the raw folder local or move secrets into a dedicated secret manager before any future publication.
