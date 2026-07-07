# Plan de publicación por oleadas SEO, GEO/LLMO y calidad web

Fecha de control: 18 de junio de 2026.

Estado global: `INCOMPLETO`.

## Objetivo

Convertir la auditoría en publicaciones pequeñas, reversibles y verificables
hasta desplegar la web optimizada sin mezclar tema, contenido, indexación,
inventario y arquitectura en un mismo lote.

MatchWalls debe convertirse en una fuente comercial, técnica y factual que
pueda rastrearse, comprenderse y citarse. No se garantizan rankings, indexación,
tráfico ni citas de sistemas IA.

## Punto de partida verificado

`VERIFICADO Y CORRECTO`

- MAIN: `178383749496`, `SEO schema hotfix - 2026-06-15`.
- Candidato H1: `178396463480`, todavía `UNPUBLISHED`.
- Ambos sin fallo de procesamiento.
- Los 17 checksums coinciden con el control aislado.
- Las 170 comprobaciones son evidencia histórica del lote del 18/06; deben
  repetirse tras publicar.

Fuentes externas Bing/Google/bots: `NO ACCESIBLE` en esta sesión. Las
afirmaciones aportadas quedan `DECLARADO PERO NO VERIFICADO` hasta revalidar
sus fuentes oficiales.

## Gobierno documental

- `registro-cambios-ejecutados.md`: solo acciones y verificaciones ocurridas.
- `programa-ejecucion-seo-geo.md`: estrategia y estado global.
- `cola-maestra-lotes-publicacion-seo-geo-2026-06-18.csv`: orden, dependencias,
  riesgo, aprobación y criterio de salida.
- Propuesta de lote: valores actuales/propuestos, evidencia, respaldo,
  reversión y QA.
- Matriz de lote: recurso, ID, URL, idioma y resultado.

## Reglas de avance

1. Antes de cada escritura se presentará el lote y la frase exacta de aprobación.
2. Solo `APROBADO LOTE [NOMBRE]` autoriza ese lote concreto.
3. Un fallo crítico activa reversión; no se improvisa en MAIN.
4. ES/EN/FR/DE/NL forman una unidad cuando el cambio sea internacional.
5. IT y PT-PT quedan fuera salvo autorización expresa.
6. Los handles relacionados con `matchwallsmurals` siguen en `STANDBY`.

## Oleada 0 — Publicación controlada

`MW-PUBLISH-H1-SEMANTIC-009` — `CORREGIDO Y VERIFICADO`.

Publicar únicamente `178396463480`, conservar `178383749496` como reversión y
repetir inmediatamente las 170 pruebas. No incluye ninguna otra corrección.

## Oleada 1 — Estabilización técnica

Después de cerrar o revertir el 009:

- `MW-THEME-LIBRARY-CLEANUP-009B`: `CORREGIDO Y VERIFICADO`; una plaza
  liberada con respaldo ZIP verificado.

- `MW-TECH-JS-ADD-EVENT-LISTENER-010A`: `VERIFICADO PERO MEJORABLE`; los
  guards 010A3/010A4 y 010A5 están `CORREGIDO Y VERIFICADO`, pero 010A2 fue
  revertido y el tracking dinámico continúa separado.
- `MW-TECH-NL-SYNTAX-010B`: `CORREGIDO Y VERIFICADO`; ejecutado únicamente en
  el tema auxiliar, con 20/20 pruebas específicas y 170/170 de regresión.
- `MW-TECH-MOBILE-OVERFLOW-FR-NL-010C`: `INCOMPLETO`; dos causas CSS
  verificadas, candidato de un archivo preparado y pendiente de aprobación.
- `MW-TECH-HOME-CRAWLABLE-CSS-010D`.
- `MW-MEASURE-CWV-FIELD-010E`.

Cada corrección tendrá tema auxiliar, comparación con MAIN y QA de home,
producto, colección, carrito, formularios, escritorio y móvil.

## Oleada 2 — Indexación y arquitectura

- `MW-INDEX-INVENTORY-011A`: clasificar las 7.932 URLs.
- `MW-INDEX-SAMPLES-POLICY-011B`: política para 541+ muestras y mapa
  producto principal ↔ muestra.
- `MW-INDEX-GEO-COLLECTIONS-011C`: decidir las 58 colecciones geográficas con
  datos de tráfico, conversión, unicidad y destino equivalente.
- `MW-INDEX-LOW-VALUE-011D`: pruebas, Black Friday y URLs sin valor.
- `MW-INDEX-REDIRECTS-HREFLANG-011E`: 635 redirecciones, cadenas, 404,
  canonicals y hreflang.

No se cambiarán handles sin mapa 301 uno-a-uno aprobado.

## Oleada 3 — Medición, buscadores prioritarios y crawlers IA

- `MW-ACCESS-MEASUREMENT-012A`: GSC, GA4, Merchant Center, CrUX y medición
  de Google/Gemini.
- `MW-BING-WEBMASTER-012B`: acceso y cobertura real para Bing, Edge y
  Copilot; seguimiento diferenciado de Yahoo.
- `MW-INDEXNOW-DESIGN-012C`: altas, cambios y bajas solo de URLs canónicas y
  valiosas.
- `MW-AI-CRAWLERS-POLICY-012D`: auditar robots, CDN y WAF; separar búsqueda de
  entrenamiento; validar user-agent e IP oficiales para ChatGPT, Claude,
  Perplexity/Comet y Grok cuando exista documentación verificable.
- `MW-YANDEX-WEBMASTER-012E`: `STANDBY`, fuera del alcance activo por decisión
  de Daniel el 18/06/2026.

Antes de proponer cambios se revalidarán las fuentes oficiales aportadas de
Bing, IndexNow, Google, OpenAI, Anthropic, Perplexity y xAI. Yahoo y Comet se
medirán como superficies diferenciadas sin inventar mecanismos de rastreo.

## Oleada 4 — Entidad factual y schema

- `MW-ENTITY-EVIDENCE-013A`: hechos y evidencias aprobadas.
- `MW-ENTITY-CONTENT-I18N-013B`: base factual ES/EN/FR/DE/NL.
- `MW-SCHEMA-ENTITY-013C`: Organization, WebSite, Product, Offer, Breadcrumb y
  Article alineados con contenido visible; `sameAs` solo oficial.

FAQPage, HowTo, LocalBusiness y Service solo se usarán cuando sean aplicables y
elegibles. El schema no garantiza rich results ni citas.

## Oleada 5 — Contenido útil y citable

Lotes separados por intención:

- medición, instalación, retirada y mantenimiento;
- mural frente a papel en rollo;
- non-woven, vinilo y autoadhesivo;
- dormitorio, salón, cocina, baño, hotel, oficina y retail;
- preguntas de compra y resolución de problemas;
- casos B2B con permiso, fotografías y hechos demostrables;
- comparativas, tablas y calculadoras propias.

## Oleada 6 — Panel CEO/CMO

`MW-DASHBOARD-SEO-GEO-015` medirá por país e idioma: ingresos, conversiones,
no-brand, indexación, muestras, CWV, schema, citas, URLs citadas, exactitud,
menciones y enlaces en Google/Gemini, Bing/Edge/Copilot, Yahoo,
Perplexity/Comet, ChatGPT, Claude y Grok.

## Próxima aprobación

Los lotes 009 y 009B están `CORREGIDO Y VERIFICADO`. El diagnóstico y la
propuesta formal de `MW-TECH-JS-ADD-EVENT-LISTENER-010A` están completos. Para
crear y modificar únicamente el tema auxiliar se requiere exactamente:

`MW-TECH-JS-ADD-EVENT-LISTENER-010A` está `VERIFICADO PERO MEJORABLE`: elimina
la excepción y pasa 170/170 pruebas en el auxiliar, pero confirmó que el
tracking dinámico ya estaba roto en el MAIN. Para corregirlo en el mismo tema
auxiliar se requiere exactamente:

`MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2` fue `INCORRECTO` y se revirtió al
checksum de 010A. La auditoría localizó otra llamada nula verificable en el
producto. Para corregir únicamente esa llamada en el auxiliar se requiere:

`APROBADO LOTE MW-TECH-PRODUCT-FILEINPUT-GUARD-010A3`

La aprobación no incluye publicar el tema auxiliar.

010A3 está `VERIFICADO PERO MEJORABLE`: corrige el producto estándar y revela
un siguiente listener nulo en el cargador. Para añadir únicamente la guarda de
`openModalButton` en el mismo auxiliar se requiere:

`APROBADO LOTE MW-TECH-UPLOADER-OPENMODAL-GUARD-010A4`

La aprobación no incluye publicar el tema auxiliar.
