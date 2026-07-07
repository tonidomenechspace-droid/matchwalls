---
type: analysis
status: active
created: 2026-07-07
updated: 2026-07-07
sources:
  - "[[wiki/Analyses/shopify-seo-geo-developer-handoff-2026-07-07]]"
  - "[[wiki/Analyses/matchwalls-audit-status-objectives-2026-07-07]]"
tags:
  - wiki
  - obsidian
  - knowledge-graph
  - audit
  - matchwalls
---

# Obsidian knowledge graph quality

## Summary

La boveda esta funcionando bien como primera capa de memoria auditada para [[wiki/Entities/matchwalls|MatchWalls]]: ya hay indice, log, sintesis inicial, informes utiles y una primera capa de fuentes, entidades y conceptos para entender el estado [[wiki/Concepts/seo|SEO]]/[[wiki/Concepts/geo|GEO]] de [[wiki/Entities/shopify|Shopify]].

Todavia no es un grafo exhaustivo de todo el corpus, pero ya no esta limitado a relaciones entre informes. La primera capa conecta fuentes criticas, entidades de negocio/plataforma y conceptos tecnicos.

Diagnostico actualizado:

- Como repositorio compartido y memoria de auditoria: `BIEN`.
- Como wiki Obsidian navegable por relaciones: `MEJORADO TRAS LA PRIMERA CAPA DE GRAFO`.
- Como base para tomar decisiones tecnicas sin releer todos los raw: `UTIL`.
- Como sistema automatico de etiquetas/relaciones de todo el corpus: `TODAVIA NO`.

## Evidence

Comprobacion local realizada el 2026-07-07:

| Evidencia | Resultado |
|---|---:|
| Archivos actuales bajo `wiki/` | 31 |
| Paginas generadas principales con frontmatter YAML | Si |
| Wikilinks detectados en `wiki/` | 240 |
| Wikilinks rotos detectados | 0 |
| `wiki/index.md` enlaza la sintesis y los analisis | Si |
| `wiki/log.md` registra consultas y lint passes | Si |
| Paginas en `wiki/Sources/` | 8 |
| Paginas en `wiki/Entities/` | 6 |
| Paginas en `wiki/Concepts/` | 10 |
| Raw files modificados durante las pasadas recientes | No |

Archivos iniciales de la capa wiki:

- [[wiki/index|Wiki Index]]
- [[wiki/log|Wiki Log]]
- [[wiki/Synthesis/raw-inventory-initial-pass|Raw inventory initial pass]]
- [[wiki/Analyses/shopify-seo-geo-developer-handoff-2026-07-07|Shopify SEO/GEO developer handoff]]
- [[wiki/Analyses/matchwalls-audit-status-objectives-2026-07-07|MatchWalls audit status and completed objectives]]
- [[wiki/Analyses/obsidian-knowledge-graph-quality-2026-07-07|Obsidian knowledge graph quality]]
- `wiki/_templates/source-summary.md`

Nodos de grafo creados en la primera capa:

- Fuentes: [[wiki/Sources/shopify-seo-geo-staging-readme|Shopify SEO-GEO staging README]], [[wiki/Sources/operational-plan-2026-07-04|Operational plan 2026-07-04]], [[wiki/Sources/infra-hold-replan-014b|Infrastructure hold replan 014B]], [[wiki/Sources/ceo-cmo-panel-spec-014c|CEO CMO panel spec 014C]], [[wiki/Sources/shopify-cli-theme-push-013e16e2|Shopify CLI theme push 013E16E2]], [[wiki/Sources/indexnow-readiness-013f|IndexNow readiness 013F]], [[wiki/Sources/entity-factual-brief-015a|Entity factual brief 015A]], [[wiki/Sources/entity-source-validation-015b|Entity source validation 015B]].
- Entidades: [[wiki/Entities/matchwalls|MatchWalls]], [[wiki/Entities/shopify|Shopify]], [[wiki/Entities/shopify-engineering-ticket-68731900|Shopify Engineering ticket 68731900]], [[wiki/Entities/bing|Bing]], [[wiki/Entities/langshop|LangShop]], [[wiki/Entities/indexnow|IndexNow]].
- Conceptos: [[wiki/Concepts/seo|SEO]], [[wiki/Concepts/geo|GEO]], [[wiki/Concepts/aeo|AEO]], [[wiki/Concepts/schema|Schema]], [[wiki/Concepts/indexability|Indexability]], [[wiki/Concepts/crawl|Crawl]], [[wiki/Concepts/canonical|Canonical]], [[wiki/Concepts/hreflang|Hreflang]], [[wiki/Concepts/entity-facts|Entity facts]], [[wiki/Concepts/shopify-liquid|Shopify Liquid]].

## What is being done well

### 1. La informacion ya no esta solo en raw

Antes, el conocimiento estaba disperso en reportes, CSV, auditorias y resultados de lotes. Ahora existe una capa compilada en `wiki/Analyses/` que permite entender el estado sin leer todo el corpus.

Valor: acelera onboarding, evita repetir analisis y reduce el riesgo de interpretar mal los lotes.

### 2. Hay trazabilidad de mantenimiento

`wiki/log.md` registra:

- creacion de estructura inicial;
- informe tecnico de handoff;
- reporte ejecutivo de objetivos;
- ejecucion de `AGENTS.md` como lint pass.

Valor: tu y Dani podeis ver que se hizo, cuando y con que objetivo.

### 3. El indice empieza a funcionar como puerta de entrada

`wiki/index.md` enlaza las paginas principales. Esto es correcto para Obsidian porque convierte la boveda en algo navegable desde un punto central.

Valor: reduce friccion para que un socio no tecnico encuentre el estado vigente.

### 4. Los informes ya usan frontmatter y tags

Los analisis incluyen propiedades como:

- `type: analysis`
- `status: active`
- `created`
- `updated`
- `sources`
- `tags`

Valor: permite futuras vistas, filtros, bases de Obsidian o consultas por tipo/estado/tag.

## What is not yet being done well

### 1. Las paginas de fuentes todavia son una primera capa

El `AGENTS.md` pide preservar procedencia mediante paginas en `wiki/Sources/`. Ya existe una primera seleccion de fuentes criticas, pero no se ha ingerido todo el corpus.

Impacto: la trazabilidad mejoro, pero para auditoria fuerte falta crear mas source summaries de los raw restantes.

### 2. Faltan entidades secundarias

Ya existen entidades principales. Quedan entidades secundarias por decidir, como `Dani`, `Daniel`, `Google Search Console`, `GA4`, `Copilot`, `Cloudflare`, `Shopify CLI` y colecciones/productos criticos si pasan a ser recurrentes.

Impacto: el grafo ya muestra relaciones centrales, pero aun no todo el ecosistema operativo.

### 3. Faltan conceptos secundarios

Ya existen conceptos principales. Quedan conceptos secundarios como `AGEO`, `SEM`, `crawl budget`, `robots.txt`, `sitemap`, `llms.txt`, `agents.md`, `FAQPage`, `BreadcrumbList`, `WebPage`, `sameAs` y `Search Performance`.

Impacto: la busqueda semantica interna mejora, pero todavia puede especializarse.

### 4. Las relaciones aun pueden profundizarse

Hay 240 wikilinks detectados en `wiki/` y 0 enlaces rotos. Ya hay red util entre fuentes, entidades, conceptos y analisis, pero todavia faltan enlaces reciprocos mas finos por cada lote raw.

Impacto: Obsidian ya aporta valor como mapa visual inicial, pero no como mapa exhaustivo de todo el corpus.

### 5. `AGENTS.md` no genera por si solo

`AGENTS.md` es una guia operativa, no un motor automatico. Para que genere etiquetas y relaciones, hay que ejecutar pasadas concretas:

- ingest de fuentes;
- extraccion de entidades;
- extraccion de conceptos;
- creacion de enlaces reciprocos;
- lint de orfandad y enlaces.

## Current added value

Lo que ya aporta ahora:

- Memoria compartida entre tu y Dani.
- Registro de decisiones y bloqueos.
- Separacion entre cambios aplicados, preparados y bloqueados.
- Reduccion de dependencia de chats largos de Codex.
- Punto de entrada para que un desarrollador entienda MatchWalls sin leer todo `raw/`.
- Base para reportar objetivos cumplidos y estado actual.

## Additional value still available

Lo que puede aportar si se completa el grafo:

- Mapa visual de plataformas, tickets, lotes, riesgos y decisiones.
- Paginas de entidad para saber rapidamente que se sabe de `MatchWalls`, `Shopify`, `Bing`, `LangShop`, `IndexNow`.
- Paginas de concepto para que SEO/GEO/AEO no sean terminos sueltos sino criterios reutilizables.
- Paginas de fuente para auditar cada claim.
- Vistas filtrables por `status`, `type`, `tags`, area tecnica o prioridad.
- Mejor coordinacion con Dani: cada lote puede enlazar a sus fuentes, entidades afectadas, riesgos y siguiente accion.

## Recommended next pass

La siguiente pasada recomendable es ampliar la primera capa de relaciones:

1. Ingerir mas fuentes raw por prioridad, empezando por reportes de lotes `012`, `013`, `014` y `015`.
2. Crear entidades secundarias solo cuando tengan recurrencia real.
3. Crear conceptos secundarios para `AGEO`, `SEM`, `robots.txt`, `sitemap`, `llms.txt`, `agents.md`, `FAQPage`, `BreadcrumbList` y `WebPage`.
4. Enlazar cada source summary a los lotes, entidades y conceptos afectados.
5. Ejecutar lint de orfandad y links tras cada tanda.

## Decision

El trabajo se estaba haciendo bien como base inicial, pero todavia no como sistema completo de etiquetas y relaciones Obsidian. Tras la primera capa de grafo, ya existen `Sources`, `Entities` y `Concepts` para las piezas centrales de [[wiki/Entities/matchwalls|MatchWalls]], [[wiki/Entities/shopify|Shopify]], [[wiki/Entities/bing|Bing]], [[wiki/Entities/indexnow|IndexNow]], [[wiki/Entities/langshop|LangShop]], [[wiki/Concepts/seo|SEO]], [[wiki/Concepts/geo|GEO]] y [[wiki/Concepts/aeo|AEO]].

La prioridad ahora es ampliar el ingest de fuentes y crear enlaces reciprocos mas profundos a medida que se procesen mas raw.
