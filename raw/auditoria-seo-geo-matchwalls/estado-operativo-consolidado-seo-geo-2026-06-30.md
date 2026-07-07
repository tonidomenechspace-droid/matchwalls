# Estado operativo consolidado SEO/GEO MatchWalls

Fecha: 2026-06-30  
Tipo: revision documental y verificacion publica de solo lectura  
Idiomas prioritarios: ES, EN, FR, DE, NL  
Estado global: INCOMPLETO

## 1. Alcance de esta revision

Se revisaron los documentos maestros, la cola de lotes, la lista maestra, el plan de publicacion y el historico reciente de ejecucion dentro de la carpeta `auditoria-seo-geo-matchwalls`.

No se modifico Shopify.

## 2. Documentos revisados

- `registro-cambios-ejecutados.md`
- `programa-ejecucion-seo-geo.md`
- `plan-publicacion-por-oleadas-seo-geo-2026-06-18.md`
- `cola-maestra-lotes-publicacion-seo-geo-2026-06-18.csv`
- `lista-maestra-errores-cambios-evoluciones-mejoras.md`
- `backlog-priorizado.csv`
- `estado-real-cobertura-seo-geo-2026-06-15.md`
- `control-paquete-maestro-2026-06-17.md`
- Diagnosticos, QA, propuestas y ejecuciones de los lotes `010`, `011B`, `011C`, `011D`, `011E`, `011F` y `011G`.

## 3. Verificacion publica actual

Sitemap publico comprobado el 2026-06-30:

- `https://www.matchwalls.com/sitemap.xml`: accesible.
- Sitemaps detectados: 29.
- URLs actuales en sitemap: 7.274.

Distribucion actual por tipo:

| Tipo | URLs |
|---|---:|
| Products | 6.195 |
| Collections | 700 |
| Pages | 287 |
| Blogs | 84 |
| Home | 7 |
| Other | 1 |

Distribucion actual por idioma:

| Idioma | URLs |
|---|---:|
| ES | 1.046 |
| EN | 1.038 |
| FR | 1.038 |
| DE | 1.038 |
| NL | 1.038 |
| IT | 1.038 |
| PT | 1.038 |

Lectura:

- El inventario inicial `MW-INDEXABILITY-INVENTORY-DIAG-011A` documentaba 7.932 URLs.
- La cifra publica actual es 7.274 URLs.
- La diferencia es coherente con los lotes posteriores de noindex/retirada de sitemap para muestras, pruebas y Black Friday, pero Search Console y Bing Webmaster siguen `NO ACCESIBLE`.

## 4. Estado por bloques

### Publicacion H1 y tema tecnico

Estado: CORREGIDO Y VERIFICADO

- `MW-PUBLISH-H1-SEMANTIC-009`: publicado y verificado.
- `MW-PUBLISH-TECH-DEBT-010P`: publicado y verificado el 2026-06-26.
- Tema activo verificado en el QA 010P: `178399019384`.
- Tema de reversion inmediata verificado en el QA 010P: `178396463480`.

Incidencia trasladada a indexabilidad:

- `custom-file-uploader` funciona, pero la URL limpia tiene `meta robots="noindex,nofollow"`.
- Estado: VERIFICADO PERO MEJORABLE.
- Requiere decision dentro del bloque de indexabilidad, no rollback tecnico.

### Deuda tecnica global

Estado: CORREGIDO Y VERIFICADO para lo publicado en `010P`.

Subbloques cerrados por registro:

- `010A3`: guard contra `customImage`.
- `010A4`: guard contra `openModalButton`.
- `010A5`: conversion inexistente protegida.
- `010A2D`: tracking dinamico corregido.
- `010B`: SyntaxError NL corregido.
- `010C2`: overflow legal FR/NL corregido.
- `010C5`: tooltip/swatch movil corregido.
- `010D`: CSS rastreable de home corregido.
- `010Z3`: regresion completa.
- `010P`: publicacion tecnica.

La cola maestra antigua no refleja completamente este cierre.

### Indexabilidad: inventario general

Estado: INCOMPLETO

Hechos verificados:

- `011A` inventario publico inicial: 7.932 URLs.
- Verificacion publica actual: 7.274 URLs.
- IT y PT siguen publicados en sitemap, pero quedan fuera del alcance prioritario activo salvo autorizacion expresa.

Pendiente:

- Clasificacion completa viva de las URLs restantes.
- Datos de Search Console/Bing por URL.
- Conversiones e ingresos por URL.

### Muestras

Estado: CORREGIDO Y VERIFICADO para productos muestra confirmados tratados.

Politica aprobada por Daniel:

`NOINDEX POR DEFECTO PARA PRODUCTOS MUESTRA CONFIRMADOS; PAGINAS INFORMATIVAS DE MUESTRAS INDEXABLES; EXCEPCIONES SOLO CON EVIDENCIA`

Hechos verificados por registro y sitemap:

- `011B4`, `011B5` y `011B5B` aplicaron `seo.hidden=1` a productos muestra confirmados.
- 602 URLs de productos muestra fueron retiradas del sitemap respecto a `011A`.
- El sitemap actual mantiene 10 URLs con patron de muestra; son paginas informativas, no productos muestra.

Estado de esas 10 URLs informativas: VERIFICADO Y CORRECTO dentro del criterio aprobado.

### URLs de prueba y Black Friday

Estado: CORREGIDO Y VERIFICADO

- `MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1`: 7/7 URLs publicas con noindex y ausentes de sitemap.
- `MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1`: 7/7 URLs publicas con noindex y ausentes de sitemap.

Nota:

- En `facade-variants/test` se mantuvo intencionadamente la redireccion publica a home localizada.

### Colecciones geograficas

Estado: VERIFICADO PERO MEJORABLE

Ejecutado:

- `MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1`: 6 colecciones geograficas no estrategicas con `seo.hidden=1`.
- 36 URLs localizadas afectadas con `noindex,nofollow`.
- 36/36 ausentes de sitemaps tras el piloto.
- `MW-INDEXABILITY-GEO-COLLECTIONS-ROLLING-DIAG-011E2`: diagnostico rolling cerrado sin cambios Shopify.

Estado actual tras `011E2`:

- Siguen 310 candidatas geograficas en sitemap:
  - ES 52.
  - EN 50.
  - FR 51.
  - DE 36.
  - NL 46.
  - PT 49.
  - IT 26.
- En idiomas prioritarios ES/EN/FR/DE/NL quedan 235 URLs.
- 147 URLs prioritarias son candidatas a noindex rolling.
- 88 URLs prioritarias quedan en `STANDBY`.

Alcance recomendado:

- Continuar solo con ES, EN, FR, DE y NL.
- Mantener IT/PT fuera salvo autorizacion expresa.
- No ejecutar rolling sin propuesta formal con IDs exactos.

### Redirecciones

Estado: INCOMPLETO

Ejecutado y verificado:

- `011F2`: consolidacion parcial de cadenas.
- `011F4`: limpieza de colision `collections/murales`.
- `011F5`: consolidacion de `papeles`.
- `011G1`: eliminacion de 14 redirects stale de colecciones/color ES.
- `011G3A`: eliminacion de 6 redirects de producto con destino muerto.
- `011G4A`: consolidacion de 12 cadenas FR `301 -> 301 -> 200` a `301 -> 200`.
- `011G4B2`: eliminacion del redirect FR muerto que terminaba en `301 -> 404`.

Estado Shopify/Admin documentado tras `011G4B2` para el bloqueo FR muerto:

- Redirect eliminado: `gid://shopify/UrlRedirect/417581367523`.
- Path eliminado: `/fr/collections/painted-papers-baller-matchwallswallpapers`.
- Target muerto eliminado: `/fr/collections/mural-murals-matchwallsmurals`.
- Conteo `path:/fr/collections/painted-papers-baller-matchwallswallpapers`: 0 EXACT.
- Conteo `target:/fr/collections/mural-murals-matchwallsmurals`: 0 EXACT.
- Conteo `path:/fr/*`: 22 EXACT.
- Nota: los conteos globales anteriores son fotografia historica; la cola viva y las evidencias posteriores prevalecen.

Pendiente critico:

- `MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-DECISION-011G4B`: cerrado mediante `MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-CLEANUP-011G4B2`, estado `CORREGIDO Y VERIFICADO`.
- `MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-REPOINT-BATHROOM-011G4B1`: alternativa no aplicada, estado `STANDBY`.
- Redirects `target:/`: 011G5, 011G5A y 011G5B1 dejaron 31 redirects `/no/` en `STANDBY`; estado `VERIFICADO PERO MEJORABLE`.
- Bloques legacy `matchwallsmurals` y `matchwallswallpapers`: requieren mapa de equivalencias antes de tocar.
- Idiomas legacy no prioritarios: STANDBY salvo decision expresa.

### Medicion, buscadores y crawlers IA

Estado: NO ACCESIBLE / INCOMPLETO

Pendiente real:

- Google Search Console.
- GA4 / conversiones por URL.
- CrUX / Core Web Vitals de campo.
- Bing Webmaster Tools para Bing, Edge, Copilot y Yahoo.
- Diseno/implementacion de IndexNow.
- Auditoria de robots, CDN y WAF para crawlers IA.
- Politica diferenciada entre bots de busqueda y bots de entrenamiento.

Alcance activo por decision de Daniel:

- Navegadores: Chrome, Edge, Opera, Brave y otros navegadores modernos.
- Buscadores/indices: Google, Bing, Yahoo, Brave Search y otros indices principales.
- IA con busqueda/citas/recomendaciones: ChatGPT, Gemini, Copilot, Claude, Perplexity, Comet, Grok, Meta AI y Ollama/web-search.
- Yandex: STANDBY.

Separacion tecnica obligatoria:

- Chrome, Edge, Opera y Brave como navegadores no requieren un "SEO propio"; requieren HTML semantico, rendimiento, accesibilidad, compatibilidad responsive y ausencia de bloqueos tecnicos.
- Google/Gemini/AI Overviews dependen de indexabilidad en Google Search, contenido textual visible, enlaces internos, experiencia de pagina y datos estructurados coherentes con lo visible. Fuente: `https://developers.google.com/search/docs/appearance/ai-features`.
- Bing, Edge, Copilot y parte del ecosistema Yahoo deben tratarse juntos desde Bing Webmaster Tools, sitemaps canonicos, calidad, indexabilidad e IndexNow. Fuentes: `https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a`, `https://help.yahoo.com/kb/webmaster-resources-sln2248.html`, `https://www.indexnow.org/documentation`.
- Brave Search tiene indice propio, pero su crawler oficial indica que si una pagina no es rastreable por Googlebot, Brave Search tampoco la rastreara. Fuente: `https://search.brave.com/help/brave-search-crawler`.
- ChatGPT requiere diferenciar `OAI-SearchBot` para busqueda/citas de `GPTBot` para entrenamiento. Fuente: `https://developers.openai.com/api/docs/bots`.
- Claude requiere diferenciar `Claude-SearchBot`, `Claude-User` y `ClaudeBot`. Fuente: `https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler`.
- Perplexity/Comet requiere diferenciar `PerplexityBot` y `Perplexity-User`. Fuente: `https://docs.perplexity.ai/docs/resources/perplexity-crawlers`.
- Meta AI debe incluir la politica de Meta web crawlers, especialmente `Meta-WebIndexer`/crawlers Meta aplicables. Fuente: `https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers`.
- Grok/xAI dispone de web search, pero la politica de crawler/indexacion debe quedar `DECLARADO PERO NO VERIFICADO` hasta que se confirme con documentacion oficial aplicable y logs/CDN. Fuente de contexto: `https://docs.x.ai/developers/tools/web-search`.
- Ollama no es un buscador publico clasico por si mismo; su capa web-search puede usar busqueda externa/API. Debe optimizarse indirectamente mediante contenido publico rastreable y citable, no mediante un bot SEO especifico salvo evidencia en logs. Fuente: `https://docs.ollama.com/capabilities/web-search`.

Verificacion puntual de MatchWalls el 2026-06-30:

- `robots.txt`: 200, `User-agent: *` con `Allow: /`, y bloqueos normales de checkout, cart, account, filtros y superficies privadas/transaccionales.
- No se detectaron reglas especificas para `OAI-SearchBot`, `GPTBot`, `Claude-SearchBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`, `Meta-ExternalAgent`, `Meta-WebIndexer`, `Bravebot` o xAI/Grok.
- Estado: VERIFICADO PERO MEJORABLE. Es rastreable de forma general, pero falta politica explicita de crawlers IA y validacion por logs/CDN/WAF.

Hallazgo tecnico/editorial puntual durante la revision 017A:

- Home ES, EN, DE y NL respondieron 200 en comprobacion puntual.
- Home FR tuvo un 500 transitorio en primer intento y 200 en dos reintentos posteriores. Estado: VERIFICADO PERO MEJORABLE; requiere monitorizacion, no conclusion definitiva de caida permanente.
- H1 DE detectado: `Bemalten Papiere für Wände und Wandgemälde`. Estado: VERIFICADO PERO MEJORABLE por calidad linguistica.
- H1 NL detectado: `Matchwalls: Papeadra Papel -specialisten`. Estado: INCORRECTO editorialmente si se confirma como texto visible estable.

Actualizacion 017B:

- Lote `MW-I18N-HOME-H1-DE-NL-META-FIX-017B` ejecutado con aprobacion exacta.
- H1 DE corregido publicamente a `Tapeten und Wandbilder für jeden Raum`. Estado: CORREGIDO Y VERIFICADO.
- H1 NL corregido publicamente a `Behang en fotobehang voor elke ruimte`. Estado: CORREGIDO Y VERIFICADO.
- Title/meta description NL registrados en Shopify y verificados publicamente. Estado: CORREGIDO Y VERIFICADO.
- EN mantiene `meta_title` y `meta_description` con `outdated=true` en Admin; no fue modificado en 017B. Estado: VERIFICADO PERO MEJORABLE.

### Entidad factual, schema y contenido citable

Estado: INCOMPLETO

Ya ejecutado:

- Hotfix de `AggregateRating` corporativo fijo no verificable: CORREGIDO Y VERIFICADO.

Pendiente:

- Auditoria global de datos estructurados.
- Base factual MatchWalls ES/EN/FR/DE/NL.
- Coherencia visible entre contenido y schema.
- Organization, WebSite, Product, Offer, Breadcrumb, Article y FAQs/HowTo cuando proceda.
- Contenido util y citable: medicion, instalacion, materiales, comparativas, mantenimiento, retirada, soluciones por estancia y casos B2B.

## 5. Contradicciones o documentos desactualizados

### Cola maestra del 18/06

Estado: VERIFICADO PERO MEJORABLE

La cola es valida como estructura, pero no como estado actual completo. Tiene lotes que quedaron obsoletos por ejecuciones posteriores:

- J02/deuda tecnica aparece incompleta, pero `010P` ya fue publicado y verificado.
- J04/muestras aparece incompleto, pero los productos muestra confirmados tratados estan corregidos y retirados del sitemap.
- J05/redirecciones aparece no accesible/incompleto, pero hay multiples sublotes ejecutados hasta `011G4A`.

Requiere actualizacion documental.

### Lista maestra

Estado: VERIFICADO PERO MEJORABLE

La seccion J del 18/06 sigue siendo util, pero debe ser reescrita con el estado posterior a:

- `010P`.
- `011B4`, `011B5`, `011B5B`.
- `011C1`.
- `011D1`.
- `011E1`.
- `011F2`, `011F4`, `011F5`, `011G1`, `011G3A`, `011G4A`, `011G4B`, `011G4B2`.

### Plan de publicacion por oleadas

Estado: VERIFICADO PERO MEJORABLE

La secuencia estrategica sigue vigente, pero el orden operativo debe moverse de:

1. deuda tecnica,
2. muestras,
3. limpieza basica,

a:

1. cierre de redirecciones/indexabilidad restantes,
2. medicion y Bing/IndexNow/crawlers,
3. entidad factual y schema,
4. contenidos citables,
5. panel CEO/CMO.

## 6. Siguiente orden recomendado

### Paso 1: consolidacion documental

Estado recomendado: CORREGIDO Y VERIFICADO cuando se actualicen la cola y la lista maestra.

Objetivo:

- Actualizar `cola-maestra-lotes-publicacion-seo-geo-2026-06-18.csv`.
- Actualizar la seccion J de `lista-maestra-errores-cambios-evoluciones-mejoras.md`.
- Mantener este documento como fotografia operativa del 2026-06-30.

No implica Shopify.

### Paso 2: redirect FR muerto

Estado actual: CORREGIDO Y VERIFICADO

Lote ejecutado:

- `MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-CLEANUP-011G4B2`.

La alternativa `MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-REPOINT-BATHROOM-011G4B1` queda en `STANDBY` salvo nueva decision comercial con equivalencia demostrada.

### Paso 3: canonicals/hreflang post-limpieza

Estado actual: VERIFICADO PERO MEJORABLE tras `MW-INDEXABILITY-CANONICAL-HREFLANG-DIAG-011H`.

Resultado:

- 39 URLs prioritarias ES/EN/FR/DE/NL auditadas.
- 0 fallos criticos canonical/hreflang en la muestra.
- Observacion menor: `/en/`, `/fr/`, `/de/` y `/nl/` responden 200 y canonizan a la version sin slash. No proponer escritura salvo evidencia externa de duplicacion.

### Paso 4: propuesta formal noindex rolling geo

Siguiente paso recomendado:

`MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-ROLLING-011E3`

Tipo:

- Escritura Shopify solo si se aprueba despues de propuesta formal.
- Preparar primer bloque pequeno con IDs exactos.
- Excluir `STANDBY`.
- No tocar IT/PT salvo autorizacion expresa.

### Paso 5: medicion y buscadores

Orden:

1. Google Search Console / GA4 / CrUX.
2. Bing Webmaster Tools para Bing, Edge, Copilot y Yahoo.
3. IndexNow.
4. Crawlers IA: OAI-SearchBot, Claude-SearchBot, PerplexityBot, y decision separada para bots de entrenamiento.

### Paso 6: entidad, schema y contenido

Orden:

1. Base factual MatchWalls ES/EN/FR/DE/NL.
2. Schema alineado con contenido visible.
3. Guias y comparativas citables.
4. Casos B2B con evidencia real.
5. Panel CEO/CMO.

## 7. Regla de avance

No ejecutar ningun cambio en Shopify sin propuesta formal y aprobacion exacta:

`APROBADO LOTE [NOMBRE]`

Esta revision solo deja el mapa operativo preparado para continuar.
