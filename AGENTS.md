# LLM Wiki Operating Guide

This vault is an Obsidian knowledge base maintained with help from Codex. Treat the raw sources as immutable evidence and the wiki as the compiled, maintained knowledge layer.

## Directory Map

- `000-Wiki/raw/` stores source material. Do not edit source files after ingest except to fix filenames or add missing assets requested by the user.
- `000-Wiki/raw/assets/` stores downloaded images and attachments referenced by source files.
- `000-Wiki/wiki/` stores LLM-maintained markdown pages.
- `000-Wiki/wiki/index.md` is the content catalog. Update it whenever pages are added, renamed, or materially changed.
- `000-Wiki/wiki/log.md` is append-only. Add one dated entry for every ingest, query page, lint pass, or structural maintenance pass.
- `000-Wiki/wiki/Sources/` stores one summary page per raw source.
- `000-Wiki/wiki/Entities/` stores people, organizations, projects, products, places, and named objects.
- `000-Wiki/wiki/Concepts/` stores reusable ideas, methods, themes, questions, and terms.
- `000-Wiki/wiki/Analyses/` stores synthesized answers, comparisons, decisions, and research notes created from user questions.
- `000-Wiki/wiki/Synthesis/` stores high-level maps, thesis pages, timelines, and overview pages.
- `000-Wiki/wiki/_templates/` stores page templates.

## Core Rules

1. Preserve provenance. Claims derived from sources should cite source summary pages using Obsidian links, for example `[[000-Wiki/wiki/Sources/example-source|Example Source]]`.
2. Prefer compiled knowledge over repeated retrieval. When a query produces a useful synthesis, ask whether to file it or file it directly if the user requested wiki maintenance.
3. Keep pages small enough to maintain. Split recurring entities and concepts into their own pages when they are referenced from multiple places.
4. Use Obsidian links for internal relationships. Use plain markdown links for external URLs.
5. Surface contradictions instead of hiding them. Add a `Contradictions and tensions` section when sources disagree.
6. Do not invent facts. Mark uncertain inferences explicitly as `Inference:` and keep them separate from source-backed statements.
7. Maintain the index and log in the same change as the wiki updates.

## Page Format

Use YAML frontmatter on generated wiki pages:

```yaml
---
type: source|entity|concept|analysis|synthesis|index|log
status: draft|active|stale
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - "[[000-Wiki/wiki/Sources/source-page]]"
tags:
  - wiki
---
```

Use these sections when they fit:

- `Summary`
- `Key points`
- `Evidence`
- `Related pages`
- `Open questions`
- `Contradictions and tensions`
- `Maintenance notes`

## Ingest Workflow

When the user asks to process a source:

1. Locate the source in `000-Wiki/raw/` or ask the user to add it if it is missing.
2. Read the source completely enough to identify the main claims, entities, concepts, dates, and open questions.
3. Create or update one page in `000-Wiki/wiki/Sources/` using `000-Wiki/wiki/_templates/source-summary.md`.
4. Update relevant pages in `Entities/`, `Concepts/`, `Synthesis/`, or `Analyses/`.
5. Add reciprocal links where useful.
6. Update `000-Wiki/wiki/index.md`.
7. Append a log entry to `000-Wiki/wiki/log.md` with this exact heading pattern:
   `## [YYYY-MM-DD] ingest | Source title`

## Query Workflow

When answering questions against the wiki:

1. Read `000-Wiki/wiki/index.md` first.
2. Search the wiki with `rg` for relevant terms.
3. Read the most relevant pages before answering.
4. Cite wiki pages in the answer.
5. If the answer is reusable, create an `Analyses/` page and log it with:
   `## [YYYY-MM-DD] query | Question or page title`

## Lint Workflow

When asked to health-check the wiki, inspect for:

- Orphan pages with no meaningful inbound links.
- Important repeated terms that lack an entity or concept page.
- Pages missing frontmatter, sources, or update dates.
- Contradictions between old and new claims.
- Stale pages whose source set has changed.
- Index entries that are missing, duplicated, or inaccurate.

Append lint results to `000-Wiki/wiki/log.md` with:
`## [YYYY-MM-DD] lint | Scope`

## Naming

- Use descriptive lowercase-kebab-case filenames for generated pages.
- Keep source summary filenames aligned with the source title when possible.
- Avoid renaming existing pages unless the user asked or the current name is clearly misleading.

## Editing Discipline

- Keep raw files immutable.
- Keep generated wiki updates tightly scoped to the source or question.
- Do not bulk rewrite established pages for style only.
- If a change affects many pages, summarize the affected pages in the log entry.
