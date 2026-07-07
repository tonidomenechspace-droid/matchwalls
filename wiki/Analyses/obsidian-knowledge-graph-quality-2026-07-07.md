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

La boveda esta funcionando bien como primera capa de memoria auditada para MatchWalls: ya hay indice, log, sintesis inicial y dos informes utiles para entender el estado SEO/GEO de Shopify.

Pero todavia no esta funcionando plenamente como grafo Obsidian de etiquetas y relaciones. La razon es concreta: faltan paginas de fuentes, entidades y conceptos. Ahora mismo la relacion principal es entre informes, no entre los objetos de negocio del proyecto.

Diagnostico corto:

- Como repositorio compartido y memoria de auditoria: `BIEN`.
- Como wiki Obsidian navegable por relaciones: `INCOMPLETO`.
- Como base para tomar decisiones tecnicas sin releer todos los raw: `UTIL`.
- Como sistema automatico de etiquetas/relaciones de todo el corpus: `TODAVIA NO`.

## Evidence

Comprobacion local realizada el 2026-07-07:

| Evidencia | Resultado |
|---|---:|
| Archivos actuales bajo `wiki/` | 6 |
| Paginas generadas principales con frontmatter YAML | Si |
| Wikilinks detectados en `wiki/` | 19 |
| `wiki/index.md` enlaza la sintesis y los analisis | Si |
| `wiki/log.md` registra consultas y lint passes | Si |
| Carpeta `wiki/Sources/` | No existe |
| Carpeta `wiki/Entities/` | No existe |
| Carpeta `wiki/Concepts/` | No existe |
| Raw files modificados durante las pasadas recientes | No |

Archivos actuales:

- [[wiki/index|Wiki Index]]
- [[wiki/log|Wiki Log]]
- [[wiki/Synthesis/raw-inventory-initial-pass|Raw inventory initial pass]]
- [[wiki/Analyses/shopify-seo-geo-developer-handoff-2026-07-07|Shopify SEO/GEO developer handoff]]
- [[wiki/Analyses/matchwalls-audit-status-objectives-2026-07-07|MatchWalls audit status and completed objectives]]
- `wiki/_templates/source-summary.md`

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

### 1. Faltan paginas de fuentes

El `AGENTS.md` pide preservar procedencia mediante paginas en `wiki/Sources/`, pero esa carpeta aun no existe.

Impacto: los informes citan raw paths y otras paginas wiki, pero todavia no existe una pagina resumen por fuente. Para auditoria fuerte, esto es insuficiente.

### 2. Faltan entidades

No existe `wiki/Entities/`. Terminos como `MatchWalls`, `Shopify`, `Bing`, `LangShop`, `IndexNow`, `Dani`, `Daniel`, `Shopify Engineering ticket 68731900` deberian tener paginas propias si se repiten.

Impacto: el grafo Obsidian no puede mostrar relaciones reales entre actores, plataformas, tickets y decisiones.

### 3. Faltan conceptos

No existe `wiki/Concepts/`. Conceptos como `SEO`, `GEO`, `AEO`, `AGEO`, `IndexNow`, `schema`, `crawl`, `canonical`, `hreflang`, `entity facts` deberian estar normalizados.

Impacto: se pierde valor de busqueda semantica interna y reutilizacion de conocimiento.

### 4. Las relaciones aun son pocas

Hay 19 wikilinks detectados en `wiki/`, pero la mayoria conectan indice, log e informes. No hay todavia red rica de relaciones entre entidades, conceptos, fuentes y decisiones.

Impacto: Obsidian aun no aporta todo su valor como mapa visual del proyecto.

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

La siguiente pasada recomendable no es escribir otro informe largo, sino crear la primera capa de relaciones:

1. Crear `wiki/Sources/` con 5-10 paginas resumen de los raw mas importantes.
2. Crear `wiki/Entities/` para `MatchWalls`, `Shopify`, `Bing`, `LangShop`, `IndexNow` y `Shopify Engineering ticket 68731900`.
3. Crear `wiki/Concepts/` para `SEO`, `GEO`, `AEO`, `schema`, `IndexNow`, `crawl budget`, `canonical`, `hreflang`.
4. Enlazar los dos informes existentes a esas paginas.
5. Actualizar `wiki/index.md` y `wiki/log.md`.

## Decision

El trabajo se esta haciendo bien como base inicial, pero todavia no como sistema completo de etiquetas y relaciones Obsidian. La evidencia principal es que ya existen informes enlazados, frontmatter e indice/log, pero aun no existen `Sources`, `Entities` ni `Concepts`.

La prioridad ahora es convertir los nombres repetidos y fuentes criticas en paginas propias.
