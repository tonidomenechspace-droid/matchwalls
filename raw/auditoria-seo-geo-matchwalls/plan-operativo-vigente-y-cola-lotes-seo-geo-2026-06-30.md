# Plan operativo vigente y cola de lotes SEO/GEO MatchWalls

Fecha: 2026-06-30  
Documento de control: `MW-DOCS-OPERATING-MASTER-016A`  
Estado global: `INCOMPLETO`  
Idiomas prioritarios: ES, EN, FR, DE, NL  
Idiomas publicados fuera de prioridad activa: IT, PT  
Yandex: `STANDBY`

## 1. Objetivo real del programa

El objetivo operativo es maximizar impresiones, rastreo, indexacion, comprension semantica y elegibilidad de MatchWalls en buscadores, navegadores y capas IA.

No se puede garantizar ranking, indexacion, trafico, menciones ni citas en IA. Lo que si se puede cerrar al 100% es el plan controlable:

- que la web sea rastreable;
- que las URLs valiosas sean indexables;
- que las URLs sin valor no contaminen sitemaps ni resultados;
- que el HTML visible sea claro para usuarios, buscadores e IA;
- que ES, EN, FR, DE y NL sean coherentes;
- que schema y contenido visible digan lo mismo;
- que los bots utiles puedan acceder segun politica aprobada;
- que las mediciones permitan saber que gana impresiones, clics, conversiones y citas.

## 2. Capas incluidas en la auditoria

### Navegadores

Alcance: Chrome, Edge, Opera, Brave y navegadores modernos.

No requieren un SEO independiente. Requieren:

- HTML semantico;
- CSS/JS sin ocultar contenido esencial;
- compatibilidad mobile;
- rendimiento y Core Web Vitals;
- accesibilidad basica;
- formularios y botones funcionales;
- no depender de interacciones JavaScript para que el contenido principal exista.

Estado actual: `VERIFICADO PERO MEJORABLE`.

Motivo:

- La deuda tecnica publicada en `MW-PUBLISH-TECH-DEBT-010P` esta `CORREGIDO Y VERIFICADO`.
- Quedan revisiones editoriales/linguisticas y medicion de campo no accesible.

### Buscadores

Alcance: Google, Bing, Yahoo, Brave Search y otros indices principales.

Principios:

- Google/Gemini/AI Overviews: SEO solido, contenido textual visible, indexabilidad, experiencia de pagina y structured data coherente. Fuente: `https://developers.google.com/search/docs/appearance/ai-features`.
- Bing/Edge/Copilot/Yahoo: Bing Webmaster Tools, sitemaps canonicos, calidad, IndexNow y URLs valiosas. Fuentes: `https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a`, `https://help.yahoo.com/kb/webmaster-resources-sln2248.html`, `https://www.indexnow.org/documentation`.
- Brave Search: requiere rastreo compatible; su documentacion indica que si una pagina no es rastreable por Googlebot, Brave Search tampoco la rastreara. Fuente: `https://search.brave.com/help/brave-search-crawler`.

Estado actual: `INCOMPLETO`.

Motivo:

- Sitemap publico actual verificado: 7.274 URLs.
- Robots permite rastreo general.
- Search Console, Bing Webmaster Tools, CrUX y datos de impresiones reales siguen `NO ACCESIBLE`.

### IA / GEO / LLMO

Alcance: ChatGPT, Gemini, Copilot, Claude, Perplexity, Comet, Grok, Meta AI, Ollama/web-search y capas IA de mercado.

Principios:

- ChatGPT: diferenciar `OAI-SearchBot` para busqueda/citas de `GPTBot` para entrenamiento. Fuente: `https://developers.openai.com/api/docs/bots`.
- Claude: diferenciar `Claude-SearchBot`, `Claude-User` y `ClaudeBot`. Fuente: `https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler`.
- Perplexity/Comet: diferenciar `PerplexityBot` y `Perplexity-User`. Fuente: `https://docs.perplexity.ai/docs/resources/perplexity-crawlers`.
- Meta AI: incluir politica de crawlers Meta aplicables. Fuente: `https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers`.
- Grok/xAI y Ollama/web-search: optimizacion indirecta mediante contenido publico rastreable y citable, salvo evidencia especifica en logs/documentacion.

Estado actual: `INCOMPLETO`.

Motivo:

- `robots.txt` no bloquea de forma general.
- No hay politica explicita separando bots de busqueda/cita y bots de entrenamiento.
- No hay validacion por logs/CDN/WAF.
- Falta base factual multilingue y contenido citable suficiente.

## 3. Estado consolidado actual

### Cerrado y publicado

| Bloque | Estado | Evidencia |
|---|---|---|
| H1 semantico | `CORREGIDO Y VERIFICADO` | `MW-PUBLISH-H1-SEMANTIC-009` |
| Deuda tecnica tema | `CORREGIDO Y VERIFICADO` | `MW-PUBLISH-TECH-DEBT-010P` |
| CSS rastreable home | `CORREGIDO Y VERIFICADO` | incluido en 010P |
| SyntaxError NL | `CORREGIDO Y VERIFICADO` | incluido en 010P |
| Overflow FR/NL tecnico tratado | `CORREGIDO Y VERIFICADO` | incluido en 010P |
| Tracking medidas dinamicas | `CORREGIDO Y VERIFICADO` | incluido en 010P |
| Productos muestra confirmados tratados | `CORREGIDO Y VERIFICADO` | 602 URLs producto muestra retiradas respecto a 011A |
| URLs `facade-variants/test` | `CORREGIDO Y VERIFICADO` | noindex y ausentes de sitemap |
| Black Friday obsoleto | `CORREGIDO Y VERIFICADO` | noindex y ausente de sitemap |
| Primer piloto geo collections | `CORREGIDO Y VERIFICADO` | 6 colecciones / 36 URLs localizadas |
| Redirecciones color/productos muertos/cadenas FR/redirect FR muerto | `CORREGIDO Y VERIFICADO` | 011G1, 011G3A, 011G4A, 011G4B2 |

### Deuda vigente

| Bloque | Estado | Que falta |
|---|---|---|
| H1/editorial DE/NL/FR home | `INCOMPLETO` | Revalidar hallazgo: FR 500 transitorio, DE/NL H1 mejorables o incorrectos |
| Geo collections restantes | `VERIFICADO PERO MEJORABLE` | 011E2: 235 URLs prioritarias actuales; 147 candidatas a noindex rolling y 88 en STANDBY; IT/PT fuera de alcance |
| Redireccion FR a 404 | `CORREGIDO Y VERIFICADO` | 011G4B2 elimino el redirect FR muerto; fuente 404 directo; sitemap limpio |
| Redirects a home | `VERIFICADO PERO MEJORABLE` | 011G5 clasifico 36; 011G5A elimino 1 prueba; 011G5B1 elimino 4 ES art/lienzos; quedan 31 `/no/` en `STANDBY` |
| Legacy `matchwallsmurals`/`matchwallswallpapers` | `STANDBY` | No tocar handles sin mapa aprobado |
| Products/pages/collections redirects restantes | `CORREGIDO Y VERIFICADO` | 011G7 cerrado; 011G7A1 repunto la muestra a `/pages/muestras`; 011G7B1 cerro 5 colecciones con target 404; 011G7C elimino la cadena de rayas |
| Canonicals/hreflang post-limpieza | `VERIFICADO PERO MEJORABLE` | 011H: 39 URLs prioritarias auditadas; 0 fallos criticos; observacion menor trailing slash en homes localizadas |
| GSC/GA4/CrUX/Merchant Center | `NO ACCESIBLE` | Requiere acceso o exportacion |
| Bing Webmaster/Yahoo/Copilot | `NO ACCESIBLE` | Requiere verificacion Bing |
| IndexNow | `INCOMPLETO` | Diseno e implementacion aprobada |
| Crawlers IA | `INCOMPLETO` | Politica explicita y validacion tecnica |
| Entidad factual | `INCOMPLETO` | Base factual ES/EN/FR/DE/NL |
| Schema global | `INCOMPLETO` | Auditoria y alineacion con contenido visible |
| Contenido citable | `INCOMPLETO` | Guias, comparativas, calculadoras, casos B2B |
| Panel CEO/CMO | `NO ACCESIBLE` | Requiere fuentes reales |

## 4. Cola maestra vigente

La cola operativa en formato CSV queda en:

`cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`

Esta cola sustituye como referencia de trabajo a la foto antigua del 18/06. La cola antigua se conserva como historico.

Resumen por prioridad:

### Prioridad 1: estabilidad visible y editorial critica

1. `MW-I18N-HOME-H1-DE-NL-FR-DIAG-017A`
   - Tipo: solo lectura.
   - Motivo: detectar si DE/NL home tienen H1 incorrecto estable y si FR/EN 500 fue transitorio.
   - Estado: `CORREGIDO Y VERIFICADO`.
   - Resultado: DE/NL confirmados `INCORRECTO`; NL hereda title/meta description en español; FR/EN 500 transitorio documentado.

2. `MW-I18N-HOME-H1-DE-NL-META-FIX-017B`
   - Tipo: escritura Shopify ejecutada.
   - Estado: `CORREGIDO Y VERIFICADO`.
   - Resultado: DE/NL `general.logo.seo` corregido; NL `meta_title` y `meta_description` registrados; EN `outdated=true` documentado sin cambio.
   - Evidencias: `backup-MW-I18N-HOME-H1-DE-NL-META-FIX-017B-2026-06-30.md` y `qa-publico-MW-I18N-HOME-H1-DE-NL-META-FIX-017B-2026-06-30.csv`.

### Prioridad 2: redirecciones e indexabilidad

3. `MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-DECISION-011G4B`
   - Estado: `CORREGIDO Y VERIFICADO`.
   - Resultado: decision cerrada con `MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-CLEANUP-011G4B2`.
   - Redirect FR muerto eliminado; no se repunto a `/fr/collections/salles-de-bain-peintes` porque la equivalencia comercial no estaba demostrada.

4. `MW-INDEXABILITY-REDIRECTS-HOME-TARGET-DIAG-011G5`
   - Tipo: solo lectura.
   - Alcance: 36 redirects a home.
   - Estado: `VERIFICADO PERO MEJORABLE`.
   - Resultado: 36/36 clasificados; 0/36 en sitemap; todos terminaban en home. Escritura `MW-INDEXABILITY-REDIRECTS-HOME-TARGET-CLEANUP-011G5A` ejecutada para la URL de prueba.
   - Estado: `INCOMPLETO`.

5. `MW-INDEXABILITY-REDIRECTS-PRODUCTS-PAGES-DIAG-011G7`
   - Tipo: solo lectura.
   - Alcance: redirects restantes de productos, paginas y colecciones.

6. `MW-INDEXABILITY-CANONICAL-HREFLANG-DIAG-011H`
   - Tipo: solo lectura.
   - Alcance: canonicals/hreflang ES/EN/FR/DE/NL tras limpieza.
   - Estado: `VERIFICADO PERO MEJORABLE`.
   - Resultado: 39 URLs prioritarias auditadas; 0 fallos criticos canonical/hreflang; 4 homes localizadas con slash final canonizan a version sin slash y quedan como observacion de bajo riesgo.

### Prioridad 3: colecciones geograficas

7. `MW-INDEXABILITY-GEO-COLLECTIONS-ROLLING-DIAG-011E2`
   - Tipo: solo lectura.
   - Alcance: clasificar geograficas restantes en ES/EN/FR/DE/NL.
   - Estado: `VERIFICADO PERO MEJORABLE`.
   - Resultado: 235 URLs prioritarias actuales; 147 candidatas a noindex rolling y 88 en `STANDBY`; no se modifico Shopify.

8. `MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-ROLLING-011E3`
   - Tipo: escritura Shopify si se aprueba.
   - Estado: `REQUIERE DECISION HUMANA`.
   - Requiere propuesta formal con IDs exactos y primer bloque pequeno; no ejecutar directamente.
   - Aprobacion necesaria:
     `APROBADO LOTE MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-ROLLING-011E3`

### Prioridad 4: buscadores, navegadores e IA

9. `MW-CRAWLERS-SEARCH-AI-POLICY-DIAG-012D1`
   - Tipo: solo lectura.
   - Alcance: robots, agents.md, sitemap, bots IA, Google/Bing/Yahoo/Brave, renderizado y señales ES/EN/FR/DE/NL.

10. `MW-BING-WEBMASTER-012B`
   - Estado: `NO ACCESIBLE`.
   - Requiere acceso a Bing Webmaster Tools.

11. `MW-INDEXNOW-DESIGN-012C`
   - Tipo: diseno tecnico.

12. `MW-INDEXNOW-IMPLEMENTATION-012C2`
   - Tipo: implementacion si se aprueba.
   - Aprobacion necesaria:
     `APROBADO LOTE MW-INDEXNOW-IMPLEMENTATION-012C2`

13. `MW-CRAWLERS-SEARCH-AI-POLICY-IMPLEMENTATION-012D2`
   - Tipo: escritura robots/CDN/Shopify si procede.
   - Aprobacion necesaria:
     `APROBADO LOTE MW-CRAWLERS-SEARCH-AI-POLICY-IMPLEMENTATION-012D2`

### Prioridad 5: entidad, schema y contenido citable

14. `MW-ENTITY-EVIDENCE-013A`
   - Crear base factual verificable.

15. `MW-ENTITY-CONTENT-I18N-013B`
   - Publicar o ajustar entidad en ES/EN/FR/DE/NL.

16. `MW-SCHEMA-GLOBAL-AUDIT-013C`
   - Auditoria de JSON-LD y datos estructurados.

17. `MW-SCHEMA-ENTITY-IMPLEMENTATION-013D`
   - Implementacion schema si se aprueba.

18. `MW-CONTENT-DEMAND-MAP-014A`
   - Mapa editorial de demanda y citas.

19. `MW-CONTENT-GUIDES-CORE-014B`
   - Guias core: medicion, instalacion, materiales, mantenimiento, retirada.

20. `MW-CONTENT-COMPARISONS-CALCULATORS-014C`
   - Comparativas, tablas y calculadoras.

21. `MW-CONTENT-B2B-CASES-014D`
   - Casos B2B con evidencia real.

### Prioridad 6: medicion CEO/CMO

22. `MW-ACCESS-MEASUREMENT-012A`
   - Acceso a GSC, GA4, Merchant Center, CrUX.

23. `MW-DASHBOARD-SEO-GEO-DESIGN-015A`
   - Diseno del panel.

24. `MW-DASHBOARD-SEO-GEO-IMPLEMENTATION-015B`
   - Implementacion con fuentes reales.

## 5. Proximo paso recomendado

Para seguir con maxima seguridad tras cerrar 017B, 011G5, 011G5A, 011G5B1, 011G7A1, 011G7B, 011G7B1, 011G7C, 011G4B2, 011H y 011E2, el siguiente paso recomendado es preparar la propuesta formal de:

`MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-ROLLING-011E3`

Motivo:

- 011E2 confirmo que siguen en sitemap 235 URLs geograficas prioritarias.
- 147 URLs son candidatas a noindex rolling por patron repetitivo y falta de evidencia accesible de valor unico.
- 88 URLs quedan en `STANDBY` por posible valor comercial o internacional; no se deben tocar sin datos o decision editorial.
- El siguiente paso no es ejecutar: es presentar propuesta formal de primer bloque, con IDs, valores actuales, valores propuestos, respaldo, reversion y QA.

## 6. Reglas de avance

- Auditorias y lecturas: autorizadas.
- Escrituras Shopify, tema, robots, redirects, schema, contenidos o integraciones: requieren propuesta formal.
- La aprobacion debe ser exacta:

`APROBADO LOTE [NOMBRE]`

- Ningun lote debe mezclar tema, productos, redirecciones, contenidos y medicion externa.
- Cada lote debe cerrar con evidencia, QA y reversion documentada.

## 7. Criterio de 100% realizado

El programa se considerara `CORREGIDO Y VERIFICADO` internamente solo cuando:

1. No queden URLs basura indexables en sitemaps prioritarios.
2. ES/EN/FR/DE/NL tengan H1, metadatos, canonicals, hreflang y contenido visible coherentes.
3. Redirecciones criticas no terminen en home sin equivalencia ni en 404.
4. Robots, sitemaps, agents.md y politica IA esten definidos y verificados.
5. Google/Bing/Yahoo/Brave tengan acceso a URLs canonicas valiosas.
6. ChatGPT, Gemini, Copilot, Claude, Perplexity/Comet, Grok, Meta AI y capas web-search tengan contenido factual rastreable y citable.
7. Schema este alineado con el contenido visible y sin datos inventados.
8. Exista contenido editorial util para compra, instalacion, materiales, mantenimiento, retirada y B2B.
9. El panel CEO/CMO mida impresiones, clics, ingresos, indexacion, CWV, schema, citas IA y menciones.
10. Todo cambio tenga respaldo y metodo de reversion.

Este 100% es controlable internamente. No equivale a garantizar rankings, impresiones o citas externas.
