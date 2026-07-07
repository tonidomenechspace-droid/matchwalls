---
type: synthesis
status: active
created: 2026-07-07
updated: 2026-07-07
sources: []
tags:
  - wiki
  - raw-inventory
---

# Raw Inventory Initial Pass

## Summary

This first pass establishes the wiki structure and records a coarse inventory of the raw source layer. It is not a full ingest. The raw layer currently contains Shopify theme exports, SEO/GEO audit evidence, staging files, and temporary work folders.

## Raw folder inventory

| Folder | File count | Notes |
| --- | ---: | --- |
| `raw/auditoria-seo-geo-matchwalls/` | 894 | Main audit corpus with markdown notes, CSV exports, screenshots, diagnostics, backups, and operational evidence. |
| `raw/auditoria-seo-geo-matchwallslangshop-export-navigation-raw-2026-06-17/` | 4 | Navigation export source set. The folder name likely needs review because it appears concatenated. |
| `raw/shopify-staging/` | 4 | Small staging source set. |
| `raw/theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E/` | 308 | Extracted Shopify theme work tree. |
| `raw/tmp-matchwalls-010a2b/` | 8 | Temporary theme work artifacts. |
| `raw/tmp-matchwalls-010a2d/` | 5 | Temporary theme work artifacts. |
| `raw/tmp-matchwalls-010c2/` | 4 | Temporary CSS/theme work artifacts. |
| `raw/tmp-matchwalls-010c3/` | 3 | Temporary related-products work artifacts. |

## File type inventory

| Extension | Count | Notes |
| --- | ---: | --- |
| `.csv` | 473 | Audit exports and operational tables. |
| `.md` | 312 | Human-readable audit notes, decisions, handoffs, reports, and logs. |
| `.liquid` | 180 | Shopify theme sections/snippets/templates. |
| `.json` | 150 | Theme configuration, diagnostics, exports, and structured evidence. |
| `.txt` | 49 | URL lists and raw text evidence. |
| `.png` | 23 | Screenshots and visual evidence. |
| `.py` | 10 | Utility and audit scripts. |
| `.js` | 9 | Theme or validation scripts. |
| `.css` | 8 | Theme CSS snapshots and temporary CSS outputs. |
| Other | 8 | `.before`, `.svg`, `.cjs`, fonts, `.zip`, `.tmp`, `.evidence`, `.xml`, `.html`. |

## Maintenance notes

- `wiki/index.md`, `wiki/log.md`, `wiki/_templates/source-summary.md`, and this synthesis page were created in this pass.
- The wiki is ready for scoped ingestion into `wiki/Sources/`, `wiki/Entities/`, `wiki/Concepts/`, and `wiki/Analyses/`.
- Recommended next source family for ingest: the markdown decision and audit files in `raw/auditoria-seo-geo-matchwalls/`, because they are already human-readable and likely contain the highest-level project knowledge.
- The root ZIP `matchwalls_matchwalls-shopify_2026-07-06_1043.zip` is excluded because the extracted content is already represented under `raw/`.

## Open questions

- Should temporary folders under `raw/tmp-matchwalls-*` remain as immutable evidence, or should they be summarized and then archived outside the primary source corpus?
- Should the concatenated folder name `raw/auditoria-seo-geo-matchwallslangshop-export-navigation-raw-2026-06-17/` be renamed for clarity?
- Which source family should be ingested first: SEO/GEO decisions, Shopify theme work, or ChatGPT handoffs?
