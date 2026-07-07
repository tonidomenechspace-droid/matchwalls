---
type: analysis
status: active
created: 2026-07-07
updated: 2026-07-07
sources:
  - "[[wiki/Synthesis/raw-inventory-initial-pass]]"
tags:
  - wiki
  - shopify
  - seo
  - geo
  - handoff
---

# Shopify SEO/GEO developer handoff

## Summary

El repositorio contiene una auditoria operativa de [[wiki/Entities/matchwalls|MatchWalls]] centrada en [[wiki/Concepts/seo|SEO]], [[wiki/Concepts/geo|GEO]], [[wiki/Concepts/aeo|AEO]]/AGEO, [[wiki/Entities/bing|Bing]]/Copilot, [[wiki/Concepts/crawl|crawlers]], [[wiki/Concepts/schema|schema]], contenido multidioma y cambios controlados en [[wiki/Entities/shopify|Shopify]]. No es solo un repositorio de codigo: es una bitacora de lotes ejecutados con evidencias, respaldos, matrices CSV y decisiones de bloqueo.

El estado actual no es "todo aplicado". La lectura correcta es:

- Hay cambios tecnicos y editoriales ya preparados o validados.
- Hay al menos un cambio confirmado aplicado en el tema live: exclusion de la coleccion evergreen Black Friday del hub publico `/collections`.
- Las landings de Espana y Francia y parte del trabajo visible de SEO/GEO estan bloqueadas por una incidencia de cache/render/sincronizacion publica en Shopify.
- El sistema esta en modo prudente: no hacer publicaciones amplias, crawls masivos, schema visible, cambios de tema, traducciones o IndexNow hasta resolver o acotar la incidencia con Shopify Engineering.

Inference: tu socio esta usando Codex como operador de paquetes de trabajo, no como un generador libre de codigo. Cada paquete tiene identificador `MW-...`, alcance aprobado, estado, evidencia, QA, backups y siguiente decision.

## Evidence base

Archivos raw principales revisados para este handoff:

- [[wiki/Sources/shopify-seo-geo-staging-readme|Shopify SEO-GEO staging README]]
- [[wiki/Sources/operational-plan-2026-07-04|Operational plan 2026-07-04]]
- [[wiki/Sources/infra-hold-replan-014b|Infrastructure hold replan 014B]]
- `raw/auditoria-seo-geo-matchwalls/cola-segura-mientras-shopify-engineering-2026-07-05.md`
- [[wiki/Sources/ceo-cmo-panel-spec-014c|CEO CMO panel spec 014C]]
- `raw/auditoria-seo-geo-matchwalls/resultado-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E-2026-07-05.md`
- [[wiki/Sources/shopify-cli-theme-push-013e16e2|Shopify CLI theme push 013E16E2]]
- [[wiki/Sources/indexnow-readiness-013f|IndexNow readiness 013F]]
- [[wiki/Sources/entity-factual-brief-015a|Entity factual brief 015A]]
- [[wiki/Sources/entity-source-validation-015b|Entity source validation 015B]]

## What is in the repository

El material se divide en tres capas:

- `raw/`: evidencia, reportes, exports, backups, trabajos preparados y auditorias. Debe tratarse como fuente de verdad historica, no como zona de edicion libre.
- `wiki/`: capa compilada para entender el proyecto. Este informe vive aqui.
- Configuracion local de Obsidian/Git: hay cambios locales en `.obsidian` no relacionados con este handoff.

La carpeta mas importante para el proyecto Shopify es `raw/auditoria-seo-geo-matchwalls/`. Ahi estan los lotes ejecutados, resultados, CSV de QA, propuestas, backups y matrices.

## Operating model used by Codex

El sistema funciona por lotes con nombres como:

- `MW-GEO-LANDINGS-...`
- `MW-COLLECTIONS-...`
- `MW-INDEXNOW-...`
- `MW-ENTITY-FACTUAL-...`
- `MW-MASTER-QUEUE-...`

Cada lote suele tener objetivo exacto, estado final, documentos leidos, evidencia generada, QA publico o Admin, backup si toca tema Shopify y decision de siguiente paso.

Regla critica: los documentos vigentes insisten en no escribir en Shopify sin aprobacion exacta del tipo `APROBADO LOTE [NOMBRE]`.

## Current live Shopify state

Tema live identificado en los reportes:

- Store: `matchwalls.myshopify.com`
- Tema MAIN/live: `gid://shopify/OnlineStoreTheme/178399019384`
- Nombre MAIN: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`

Tema staging mencionado:

- `SEO-GEO staging - 2026-06-15`
- ID: `gid://shopify/OnlineStoreTheme/178383585656`

Tema QA aislado mencionado en varios lotes:

- `178396463480`
- Relacionado con `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA`

Cambio live confirmado:

- Archivo: `sections/main-list-collections.liquid`
- Lote aplicado: `MW-SHOPIFY-CLI-INSTALL-AUTH-THEME-PUSH-013E16E2`
- Resultado: `CORREGIDO Y VERIFICADO`
- Efecto: exclusion visual por ID estable de la coleccion Black Friday evergreen del hub publico de colecciones.
- QA publico: `/collections`, `/en/collections`, `/fr/collections`, `/de/collections`, `/nl/collections` devuelven 200, tema `178399019384`, 47 tarjetas y 0 Black Friday.

El lote anterior `013E16E` habia quedado `INCOMPLETO`; el lote posterior `013E16E2` lo cerro con Shopify CLI y `--only "sections/main-list-collections.liquid"`.

## SEO/GEO work already done or prepared

### Page content and H1

El staging SEO/GEO tenia como objetivo que las paginas usaran `page.content` como contenido editorial visible y que `sections/main-page.liquid` generase un unico H1. La intencion es dejar de depender de bloques antiguos repetidos o claims no validados.

### Spain and France landings

Los documentos vigentes indican:

- `012E`: revision de contenido verificada.
- `012F`: contenido de paginas mejorado.
- `012H`: traducciones EN/FR/DE/NL trabajadas en LangShop.
- `012J4F`: meta/cache resuelto tras purga o tecnica de same-value.
- `012L6B`: schema `WebPage`, `FAQPage` y `BreadcrumbList` aplicado en MAIN.
- `012L7`: schema validado publicamente.
- `012M`: linking interno verificado pero mejorable.
- `012N`: copy map preparado.
- `012O`: bloque de linking interno incompleto porque Admin y storefront publico no sincronizan de forma fiable.

Interpretacion para desarrollo: no asumir que lo que esta en Admin se refleja siempre en publico. El bloqueo actual nace precisamente de esa discrepancia.

### Collections hub

Se trabajo el hub `/collections` en varios idiomas. El cambio live confirmado elimina Black Friday evergreen del listado publico sin tocar handles, URLs, traducciones, mercados, productos, colecciones ni SEO fields.

### Bing, Copilot and AI visibility

Hay una base de datos verificada para Bing:

- Bing Search Performance: 749 impresiones, 3 clicks, CTR 0.40%, periodo 2026-06-13 a 2026-07-03.
- Bing keywords export: 88 queries, 131 impresiones exportadas/visibles, 3 clicks, posicion media ponderada 6.43.
- Bing pages export: 49 URLs, 136 impresiones exportadas/visibles, 3 clicks, posicion media ponderada 6.19.
- Bing sitemap: `https://www.matchwalls.com/sitemap.xml`, estado `Success`, 0 errores, 0 warnings, 7.8K URLs descubiertas.
- Bing AI Performance: 10 citas, 5 dias con citas, 7 URLs citadas.

No hay evidencia suficiente en estos archivos de GA4, Shopify Analytics, GSC, CrUX/CWV real o paneles IA fuera de Bing.

### Entity factual layer

Los lotes `015A` y `015B` crean una base factual prudente para MatchWalls:

- Se puede describir MatchWalls como tienda online especializada en papel pintado, murales decorativos y soluciones murales a medida.
- Idiomas prioritarios: ES, EN, FR, DE, NL.
- Publicos seguros: hogares y proyectos profesionales.
- Temas seguros: muestras, medicion de paredes, personalizacion, estilos, estancias, colores y materiales.

Pero siguen bloqueados para schema/copy publico:

- razon social;
- CIF/NIF/VAT;
- direccion legal;
- telefono/email estructurado;
- `sameAs`;
- founding date o claim "desde 1961";
- Barcelona como sede;
- fabricacion propia;
- certificaciones;
- sostenibilidad;
- Trustpilot/reviews;
- garantias, plazos, devoluciones o envio gratis.

## Main blocker

El bloqueo principal es [[wiki/Entities/shopify-engineering-ticket-68731900|Shopify Engineering ticket 68731900]].

Problema documentado: inconsistencia entre Admin y storefront publico en landings geograficas, especialmente el caso `012O`. Los QA registran muchas respuestas FAIL aunque no aparecen `noindex`, las canonicals son correctas y el tema publico es el esperado.

Datos relevantes:

- `012O5`: 80 requests, 11 PASS, 69 FAIL.
- `012O6`: 40 requests, 6 PASS, 34 FAIL.
- `012O5B`: 80 requests, 14 PASS, 66 FAIL.
- Tema publico en esas comprobaciones: `178399019384`.
- `cf-cache-status: DYNAMIC`.

Decision vigente:

- No avanzar contenido visible de paises hasta resolver la discrepancia.
- No hacer rollback ahora porque Admin esta correcto y el storefront publico sigue mostrando contenido antiguo valido.
- No seguir escribiendo contenido a ciegas.
- Continuar o responder a Shopify/LangShop support y revalidar cuando confirmen purga/flush o causa.

## Infrastructure and crawler risk

El replan `014B` marco una pausa tecnica por incidencias detectadas en pruebas:

- `013J6`: 42 URLs prioritarias; 6 con 200, 36 incompletas por 429; entorno QA recibio 429 en 42/42 con user-agent tipo Bingbot.
- `013J6R`: safety gate de 5 URLs; 3/5 con 200, 2/5 con 500, 0/5 con 429.

URLs con 500 documentadas:

- `https://www.matchwalls.com/products/gingham-charm-verde`
- `https://www.matchwalls.com/en/collections/salamanca-wallpaper`

Regla vigente hasta respuesta de Shopify Engineering:

- No broad public crawls.
- No theme publishes.
- No Liquid/snippets/schema/app embeds/home/layout.
- No edits a paginas Espana/Francia, LangShop, traducciones, SEO fields visibles, handles, URLs, canonicals, redirects, robots, sitemap, `llms.txt`, `agents.md`.
- No IndexNow masivo/manual.
- No interpretar los 500 como fallo editorial SEO sin confirmacion tecnica.

## IndexNow status

[[wiki/Entities/indexnow|IndexNow]] no esta implementado.

Estado publico revisado el 2026-07-05:

- `robots.txt`: 200.
- `sitemap.xml`: 200.
- `agents.md`: 200.
- `llms.txt`: 200.
- `indexnow.txt`: 404.

Bloqueo tecnico: falta una key verificable alojada de forma correcta para cubrir `www.matchwalls.com`.

Decision recomendada en los reportes:

- No generar key real todavia.
- No enviar URLs.
- Preguntar a Shopify si Online Store puede servir un TXT arbitrario `/{indexnow-key}.txt` en raiz.
- Si Shopify no puede, comparar app IndexNow vs Edge/CDN/worker vs posponer.

## What your partner is doing with Codex

Tu socio ha usado Codex para construir una cadena de trabajo semiauditada:

- define paquetes pequenos con nombres estables;
- pide aprobacion antes de escrituras;
- hace diagnosticos documentales y tecnicos;
- genera backups antes de tocar Liquid;
- contrasta Admin API, storefront publico, Bing Webmaster y CSVs;
- crea reportes de resultado por lote;
- mantiene una cola de tareas bloqueadas, seguras y preparables.

El enfoque es conservador. No intenta arreglarlo todo en una sola tanda. La prioridad es no publicar claims no verificados y no empeorar el estado SEO mientras Shopify tiene una incidencia abierta.

La parte que como desarrollador debes vigilar: hay muchos documentos y estados parciales. Un archivo `resultado-*` posterior puede corregir el estado de uno anterior. Ejemplo claro: `013E16E` decia que Black Friday seguia incompleto; `013E16E2` lo cerro como corregido y verificado.

## Developer entry plan

1. Tomar como fuente inicial este informe y los raw listados en `Evidence base`.
2. Revisar primero el estado de Shopify Engineering ticket `68731900`.
3. No hacer cambios visibles en tema, LangShop, schema, robots, sitemap, `llms.txt`, `agents.md` ni IndexNow hasta resolver el bloqueo o aprobar un lote acotado.
4. Si necesitas tocar tema, trabajar con una rama/directorio local completo y hacer diffs contra el tema live `178399019384`.
5. Para cualquier Liquid live, exigir backup del asset remoto antes de escribir y postcheck publico multiidioma despues.
6. Separar trabajo documental seguro de trabajo publicable:
   - seguro: briefs, mapas de schema, copy drafts, matrices de URLs, QA checklist.
   - bloqueado: publicaciones MAIN, schema visible, landings pais, traducciones, crawls amplios, IndexNow.
7. Si se reabre la ejecucion tecnica, empezar por un postcheck de baja intensidad, no por un crawl masivo.

## Immediate safe tasks

Estas tareas no deberian tocar Shopify:

- Consolidar una matriz unica de lotes con columnas: lote, estado, archivo resultado, afecta Shopify, afecta MAIN, reversible, siguiente decision.
- Preparar brief tecnico para Shopify Engineering con `x-request-id`, URLs 500 y resumen del caso `012O`.
- Preparar propuesta de schema minimo para entidad con solo `name`, `url` y descripcion prudente.
- Revisar la cola Bing/AI para priorizar 5-10 URLs, sin enviar IndexNow.
- Crear checklist post-infra para cuando Shopify responda.

## Blocked or high-risk tasks

No ejecutar sin decision explicita:

- Publicar tema o snippets en MAIN.
- Modificar `sections/main-page.liquid`, `snippets/microdata-schema.liquid`, layout, app embeds o home.
- Editar paginas Espana/Francia o traducciones LangShop.
- Cambiar SEO fields visibles, handles, canonicals, redirects o URLs.
- Tocar `robots.txt`, `sitemap.xml`, `llms.txt`, `agents.md`.
- Implementar IndexNow o enviar URLs.
- Hacer crawls publicos amplios.
- Publicar claims corporativos no validados.

## SEM note

En los documentos revisados el trabajo real aparece como SEO/GEO/AEO/AGEO, Bing/Copilot, crawlers, schema, contenido, indexabilidad y entidad. No he visto evidencia de gestion SEM entendida como campanas de pago, ads, presupuestos, conversion tracking o paid search. Si existen campanas SEM, probablemente estan fuera de los raw revisados o aun no se han incorporado a la auditoria.

## Open questions

- Cual es el estado actual del ticket Shopify `68731900`.
- Si Shopify confirmo causa o resolucion de la inconsistencia `012O`.
- Si Daniel ya aporto los datos oficiales pendientes de entidad.
- Si hay acceso real a GSC, GA4, Shopify Analytics y Search Console fuera de Bing.
- Si se quiere mantener Shopify CLI como via operativa autorizada para cambios quirurgicos en MAIN.
- Si existe infraestructura externa capaz de servir `/{indexnow-key}.txt` sin riesgo DNS/CDN.

## Maintenance notes

Este informe es una lectura de estado para entrada de desarrollador. No sustituye un ingest completo de todos los raw ni una auditoria actual contra Shopify live. Antes de ejecutar cambios, hay que verificar el estado actual real de Shopify, porque los reportes revisados llegan hasta el 2026-07-06 y el estado externo puede haber cambiado.
