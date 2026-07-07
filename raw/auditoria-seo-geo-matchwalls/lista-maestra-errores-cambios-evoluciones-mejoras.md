# Lista maestra de errores, cambios, evoluciones y mejoras

Fecha de consolidaciÃ³n: 15 de junio de 2026.  
Regla de ejecuciÃ³n: ninguna acciÃ³n implica autorizaciÃ³n para modificar Shopify. Antes de cambiar URLs, contenido, tema, datos estructurados, aplicaciones o configuraciÃ³n, se requiere validaciÃ³n y autorizaciÃ³n de Daniel.

## Lectura rÃ¡pida

- **Errores verificados:** deben corregirse porque existe evidencia pÃºblica concreta.
- **Por validar:** hay indicios suficientes para investigarlos, pero no deben tratarse todavÃ­a como errores confirmados.
- **Cambios:** correcciones o ajustes necesarios durante los prÃ³ximos 90 dÃ­as.
- **Evoluciones:** desarrollos de proceso, arquitectura o contenido para 3-6 meses.
- **Mejoras estratÃ©gicas:** autoridad, mediciÃ³n y visibilidad SEO/GEO para 6-12 meses.

## A. Errores crÃ­ticos verificados

- [ ] **A01. Retirar pÃ¡ginas internas de prueba del Ã­ndice y sitemap.** Evidencia: `/en/pages/facade-variants/test` y `/de/pages/facade-variants/test` responden `200` y canonizan a sus homes. Decidir `404/410` o redirecciÃ³n Ãºnicamente si existe sustituto equivalente; eliminar enlaces internos.
- [ ] **A02. Corregir el bloque que expone CSS como texto rastreable en la home.** Evidencia: reglas `.logo-link` y `.logo-list__image` aparecen como contenido visible para rastreadores en `https://www.matchwalls.com/`. Diagnostico 010D del 25/06/2026: origen verificado en `sections/collection-logo-list.liquid`; corregido y verificado en tema auxiliar `178399019384` con MD5 `e246746230f64c88b529db9aa370f3e2`; pendiente publicacion para corregir MAIN.
- [ ] **A03. Corregir la mezcla de idiomas de la home espaÃ±ola.** Revisar tÃ©rminos visibles como `Professionals`, `Wallpaper` y nombres/traducciones incoherentes.
- [ ] **A04. Corregir la mezcla de idiomas en atenciÃ³n al cliente.** La pÃ¡gina inglesa y la alemana contienen el H1 espaÃ±ol `AtenciÃ³n al cliente â€” MatchWalls`.
- [ ] **A05. Corregir errores visibles de marca y texto.** Ejemplos verificados: `Matchalls.com`, `MarrÃ²n` y el handle espaÃ±ol `transfroma-tu-cocina...`.
- [ ] **A06. Corregir handles con errores ortogrÃ¡ficos propagados.** El sitemap contiene 70 URLs con `norid/noridcas`, 19 con `enchathed` y ejemplos con `recoto` y `suctan`.
- [ ] **A07. Corregir la colecciÃ³n francesa con marca incorrecta.** Evidencia: `/fr/collections/nouveaux-matchalls-matchwallsmurals`.
- [ ] **A08. Corregir URLs de muestras con idioma incorrecto.** Evidencia: `/en/products/muestra-de-wildflower-whisper-lila` y `/fr/products/muestra-de-wildflower-whisper-lila`.
- [ ] **A09. Definir y aplicar una polÃ­tica SEO para muestras.** Se detectaron al menos 541 URLs de muestras indexables; pueden canibalizar productos principales y ser recomendadas errÃ³neamente por motores de IA.
- [ ] **A10. Auditar la veracidad y elegibilidad de `AggregateRating`.** Aparece en las 7 homes localizadas y no se observÃ³ `Review` schema. Confirmar entidad valorada, fuente, recuento, valor y reseÃ±as visibles.
- [ ] **A11. AÃ±adir H1 Ãºnico y localizado a pÃ¡ginas sin H1.** Se observaron 34 pÃ¡ginas HTML vÃ¡lidas sin H1, principalmente pÃ¡ginas corporativas traducidas.
- [ ] **A12. Eliminar H1 duplicados o mÃºltiples.** Se observaron 15 pÃ¡ginas con dos H1; convertir el secundario en H2 o texto normal.
- [ ] **A13. Corregir metadatos duplicados en muestras.** Ejemplo: muestras alemanas Blue Classic Grid y Green Classic Grid comparten meta description.
- [ ] **A14. Corregir errores editoriales y metadatos del blog.** Revisar handles mal escritos, H1 con marca errÃ³nea y descriptions de hasta 320 caracteres.

## B. Incidencias que deben validarse antes de actuar

- [ ] **B01. Repetir la comprobaciÃ³n del error HTTP 500.** Durante el rastreo, `/en/products/black-noridcas-lines` devolviÃ³ `500`; revisar monitorizaciÃ³n y logs solo si vuelve a reproducirse.
- [ ] **B02. Auditar los 359 handles de producto terminados en `-1`.** Determinar cuÃ¡les son colisiones, duplicados reales, traducciones o productos distintos antes de consolidar.
- [ ] **B03. Validar hreflang completo y recÃ­proco.** La muestra vÃ¡lida declarÃ³ ocho alternates por pÃ¡gina, pero debe verificarse toda la matriz internacional con export completo/Search Console.
- [ ] **B04. Validar canonicals de todo el catÃ¡logo.** Confirmar que cada producto, muestra, familia, colecciÃ³n y traducciÃ³n canoniza a la URL correcta.
- [ ] **B05. Validar cobertura completa de datos estructurados.** La muestra confirmÃ³ Product/Offer en 116 productos, FAQPage en 14 pÃ¡ginas y Breadcrumb en 564; falta comprobar todas las plantillas e idiomas.
- [ ] **B06. Validar precio, disponibilidad, moneda e identificadores de producto.** Contrastar JSON-LD con contenido visible, Merchant Center, SKU y GTIN/MPN cuando proceda.
- [ ] **B07. Medir Core Web Vitals de campo.** Obtener datos de Search Console/CrUX antes de priorizar cambios de rendimiento.
- [ ] **B08. Revisar errores 4XX/5XX y cadenas de redirecciÃ³n con un rastreo completo sin rate limiting.** Los `429` observados fueron una limitaciÃ³n metodolÃ³gica y no deben registrarse como errores SEO.
- [ ] **B09. Revisar indexaciÃ³n real frente a sitemap.** Comparar las 7.932 URLs declaradas con Search Console para detectar excluidas, rastreadas sin indexar, duplicadas y soft 404.
- [ ] **B10. Detectar contenido cortado, cruzado o vacÃ­o mediante export de Shopify de solo lectura.** Priorizar ES, EN, FR, DE y NL.

## C. Cambios prioritarios de 0-30 dÃ­as

- [ ] **C01. Crear un inventario maestro producto principal â†” muestra â†” variante â†” familia.**
- [ ] **C02. Decidir para cada muestra si debe ser `noindex`, consolidarse, diferenciarse o mantenerse indexable.**
- [ ] **C03. Preparar un mapa de redirecciones 301 uno-a-uno para handles errÃ³neos.** No cambiar URLs hasta aprobar el mapa.
- [ ] **C04. Actualizar canonicals, hreflang y enlaces internos en cada propuesta de cambio de URL.**
- [ ] **C05. Realizar QA editorial manual de la home en ES, EN, FR, DE y NL.**
- [ ] **C06. Revisar pÃ¡ginas corporativas prioritarias en ES, EN, FR, DE y NL.** Incluir contacto, atenciÃ³n al cliente, nosotros, profesionales, envÃ­os, devoluciones, materiales, instalaciÃ³n, sostenibilidad y FAQ.
- [ ] **C07. Crear un glosario maestro multilingÃ¼e.** Definir nombres de familias, colores, materiales, estancias, tÃ©rminos tÃ©cnicos, marca y quÃ© nombres propios no deben traducirse.
- [ ] **C08. Crear una lista de errores prohibidos y variantes correctas.** Incluir `MatchWalls`, tÃ©rminos de materiales, colores y familias.
- [ ] **C09. Corregir tÃ­tulos, H1 y meta descriptions prioritarios.** Empezar por errores de marca, mezcla de idioma, duplicados y pÃ¡ginas con mayor potencial comercial.
- [ ] **C10. Validar `AggregateRating`, Product, Offer, Organization, WebSite, Article y FAQ con herramientas de schema antes de publicar cambios.**
- [ ] **C11. Mantener `robots.txt`, `agents.md`, UCP/MCP y sitemap operativos; no bloquear agentes Ãºtiles sin una estrategia explÃ­cita.**

## D. Cambios de 31-90 dÃ­as

- [ ] **D01. Completar QA editorial de todo el catÃ¡logo prioritario ES, EN, FR, DE y NL.**
- [ ] **D02. Clasificar las 7.932 URLs por valor e intenciÃ³n.** Separar producto principal, muestra, variante, familia, colecciÃ³n, contenido y pÃ¡gina corporativa.
- [ ] **D03. Reducir la expansiÃ³n innecesaria del Ã­ndice.** Mantener indexables solo pÃ¡ginas con demanda, contenido Ãºnico y propÃ³sito claro.
- [ ] **D04. Normalizar handles localizados.** Evitar palabras del idioma equivocado, errores, sufijos automÃ¡ticos y variaciones incoherentes.
- [ ] **D05. Reescribir metadatos por plantilla, intenciÃ³n e idioma.** Evitar descriptions truncadas, genÃ©ricas o duplicadas.
- [ ] **D06. Crear reglas de alt de imagen.** Alt descriptivo para producto/ambiente; alt vacÃ­o para imÃ¡genes puramente decorativas.
- [ ] **D07. Auditar imÃ¡genes principales.** Revisar alt, nombres, peso, dimensiones, formato, lazy loading y relaciÃ³n con el producto.
- [ ] **D08. Revisar enlaces internos.** Conectar familias, colecciones, productos, muestras, guÃ­as, FAQ y pÃ¡ginas B2B; eliminar enlaces a pruebas o URLs sustituidas.
- [ ] **D09. Validar reciprocidad hreflang, cÃ³digos regionales y `x-default`.**
- [ ] **D10. Crear una ficha estable de entidad Matchwalls.** QuiÃ©n es, quÃ© fabrica, ubicaciÃ³n, mercados, materiales, personalizaciÃ³n, envÃ­os, devoluciones, sostenibilidad y contacto.
- [ ] **D11. Consolidar Organization schema.** AÃ±adir identidad consistente, logo, contacto y `sameAs` verificados.
- [ ] **D12. Mejorar Product schema.** Alinear oferta, disponibilidad, moneda, imÃ¡genes, marca, SKU e identificadores con el contenido visible.
- [ ] **D13. Mejorar Article/BlogPosting.** Incluir autor experto, fecha de publicaciÃ³n/modificaciÃ³n, imagen y entidad editora.
- [ ] **D14. Mantener FAQPage sincronizado con preguntas y respuestas visibles.**
- [ ] **D15. Conectar Search Console, GA4 y Merchant Center a un panel de control.**
- [ ] **D16. Monitorizar semanalmente sitemap, indexables, exclusiones, errores y redirecciones.**

## E. Evoluciones de 3-6 meses

- [ ] **E01. Reestructurar las familias de producto como entidades claras.** Cada familia debe explicar concepto, variantes, colores, materiales, estancias y productos relacionados.
- [ ] **E02. Separar semÃ¡nticamente producto principal, muestra y variante.** Los usuarios y motores de IA deben identificar cuÃ¡l comprar y para quÃ© sirve cada URL.
- [ ] **E03. DiseÃ±ar una arquitectura de colecciones por intenciÃ³n Ãºtil.** Temas, estilos, colores, estancias y usos, evitando crear pÃ¡ginas dÃ©biles o duplicadas.
- [ ] **E04. Crear contenido Ãºnico para colecciones prioritarias.** AÃ±adir explicaciÃ³n, criterios de elecciÃ³n, enlaces a guÃ­as y preguntas frecuentes.
- [ ] **E05. Reforzar pÃ¡ginas de materiales.** Explicar diferencias entre non-woven, vinilo autoadhesivo, mural y otras calidades.
- [ ] **E06. Crear guÃ­as tÃ©cnicas expertas.** MediciÃ³n, instalaciÃ³n, retirada, mantenimiento, selecciÃ³n por estancia y resoluciÃ³n de problemas.
- [ ] **E07. AÃ±adir autorÃ­a experta, fecha de revisiÃ³n, fuentes y metodologÃ­a a guÃ­as.**
- [ ] **E08. Crear casos B2B verificables.** Incluir sector, reto, soluciÃ³n, material, resultado, fotografÃ­as, autor y productos utilizados.
- [ ] **E09. Mejorar la propuesta para arquitectos, interioristas, instaladores y distribuidores.**
- [ ] **E10. Automatizar controles antes de publicar.** Idioma, campos vacÃ­os/cortados, duplicados, handles, H1, metadatos, imÃ¡genes, schema, enlaces y hreflang.
- [ ] **E11. Crear alertas para cambios masivos o propagaciÃ³n de errores entre idiomas.**
- [ ] **E12. Optimizar rendimiento segÃºn datos CWV reales.** Reducir recursos, scripts, peso de imÃ¡genes y coste de plantillas donde los datos lo justifiquen.
- [ ] **E13. Establecer un proceso de revisiÃ³n para nuevas familias y traducciones antes de indexarlas.**

## F. Mejoras GEO/AEO y de autoridad de 6-12 meses

- [ ] **F01. Convertir Matchwalls en una fuente factual citable.** Publicar respuestas claras y verificables sobre materiales, personalizaciÃ³n, mediciÃ³n, instalaciÃ³n, envÃ­o y devoluciones.
- [ ] **F02. Crear comparativas Ãºtiles.** Non-woven vs vinilo autoadhesivo vs mural; soluciones por cocina, baÃ±o, dormitorio, hotel, oficina y retail.
- [ ] **F03. Publicar activos citables.** Estudios, guÃ­as descargables, calculadoras de medidas, tablas tÃ©cnicas y comparativas.
- [ ] **F04. Crear un programa editorial basado en preguntas reales de compra e instalaciÃ³n.**
- [ ] **F05. Reforzar seÃ±ales de experiencia y confianza.** Autores, expertos, proyectos, metodologÃ­a, polÃ­ticas claras y evidencia visual.
- [ ] **F06. Desarrollar colaboraciones con diseÃ±adores, arquitectos, instaladores y medios.**
- [ ] **F07. Obtener menciones y enlaces relevantes por mercado e idioma.**
- [ ] **F08. Reforzar la diferenciaciÃ³n frente a Photowall, Rebel Walls, Wallism y Bimago.** Posicionar Matchwalls como especialista en papel pintado y murales personalizados a medida.
- [ ] **F09. Mejorar el contenido de marca y profesional tomando como referencia la claridad de Rebel Walls.**
- [ ] **F10. Mejorar rutas semÃ¡nticas de descubrimiento tomando como referencia la taxonomÃ­a de Wallism, sin generar thin content.**
- [ ] **F11. Medir mensualmente presencia y citas en Google/Gemini, Bing/Edge/Copilot, Yahoo, Perplexity/Comet, ChatGPT, Claude y Grok.**
- [ ] **F12. Mantener un conjunto fijo de preguntas GEO/AEO.** Registrar si Matchwalls aparece, quÃ© URL se cita, posiciÃ³n, exactitud y competidores mencionados.
- [ ] **F13. Revisar trimestralmente SEO internacional, catÃ¡logo, hreflang, indexaciÃ³n y contenido.**

## G. MediciÃ³n y gobernanza obligatorias

- [ ] **G01. Crear responsables por Ã¡rea.** SEO tÃ©cnico, catÃ¡logo, traducciÃ³n, contenido, desarrollo, datos estructurados y analÃ­tica.
- [ ] **G02. Definir KPIs sin inventar datos.** Indexables vÃ¡lidas, exclusiones, errores, pÃ¡ginas con clics, cobertura de traducciÃ³n, duplicados, CWV, rich results y citaciones IA.
- [ ] **G03. Crear un registro de cambios SEO.** Fecha, URL, motivo, responsable, autorizaciÃ³n, redirecciÃ³n y resultado.
- [ ] **G04. Aplicar el flujo obligatorio:** evidencia â†’ propuesta â†’ revisiÃ³n editorial/tÃ©cnica â†’ autorizaciÃ³n de Daniel â†’ despliegue controlado â†’ verificaciÃ³n.
- [ ] **G05. Probar cambios primero sobre una familia o conjunto pequeÃ±o.** Medir antes de extender al catÃ¡logo completo.
- [ ] **G06. Revisar todas las redirecciones despuÃ©s de cada cambio.** Evitar cadenas, bucles, destinos irrelevantes y pÃ©rdida de hreflang.
- [ ] **G07. Verificar sitemap, canonicals, hreflang, enlaces y schema despuÃ©s de cada despliegue.**
- [ ] **G08. Mantener copias/exportaciones previas y plan de reversiÃ³n para cambios masivos.**

## Orden recomendado de ejecuciÃ³n

1. Resolver A01-A14 y validar B01-B10.
2. Aprobar polÃ­tica de muestras, glosario y mapa de redirecciones.
3. Ejecutar C01-C11 mediante cambios controlados.
4. Completar limpieza internacional y mediciÃ³n D01-D16.
5. Desarrollar arquitectura, contenido experto y automatizaciÃ³n E01-E13.
6. Construir autoridad y visibilidad GEO/AEO F01-F13.
7. Mantener de forma permanente la gobernanza G01-G08.

## H. Incidencias internas verificadas tras acceso Shopify

- [ ] **H01. Restaurar urgentemente `MÃ©todos de pago` y `Conoce nuestros productos`.** Sus cuerpos estÃ¡n cruzados y varias traducciones recientes mezclan contenido, metadatos y handles de intenciones distintas.
- [ ] **H02. Validar o retirar el `AggregateRating` fijo del tema principal.** El Organization schema publicado declara 4,5 y 13 reseÃ±as de forma hardcodeada; debe demostrarse la fuente y elegibilidad.
- [ ] **H03. Completar el QA de Serene Vista.** IT/PT contienen texto de `Jungle Rhapsody`; existen metadatos en idioma incorrecto, doble espacio y media alt deficiente.
- [ ] **H04. Completar el QA de Whispering Woods.** Corregir nombres como `Whispending Woods Green`, traducciones forzadas, handles con sufijos y la muestra con inventario negativo.
- [ ] **H05. Auditar las 1.990 muestras internas.** Resolver descripciones vacÃ­as o cruzadas, colores que no coinciden con handles, duplicados, vendors y polÃ­tica de indexaciÃ³n.
- [ ] **H06. Auditar las 635 redirecciones.** Eliminar cadenas y corregir destinos entre productos no equivalentes.
- [ ] **H07. Revisar la arquitectura de colecciones.** Alinear tÃ­tulos, handles, reglas y contenido; evaluar el riesgo de las colecciones por ciudad con productos idÃ©nticos.
- [ ] **H08. Completar o excluir conscientemente IT/PT en cada lote de publicaciÃ³n.** No publicar actualizaciones parciales que dejen idiomas antiguos, vacÃ­os o marcados como desactualizados.
- [ ] **H09. Corregir el Breadcrumb schema de artÃ­culos.** El elemento del artÃ­culo usa `blog.title` en lugar de `article.title`.
- [ ] **H10. Implantar un criterio de aceptaciÃ³n obligatorio antes de publicar.** Validar recurso, idioma, contenido, handle, metadatos, imÃ¡genes, schema, enlaces, redirects y aprobaciÃ³n humana.
# ActualizaciÃ³n verificada del 15 de junio de 2026

## CrÃ­ticas

- **GTIN falsos en producciÃ³n:** en una muestra de 50 productos activos y 65 variantes, 65/65 barcodes coinciden con el ID interno de Shopify. El tema principal los publica como GTIN. SoluciÃ³n preparada y validada en `SEO schema hotfix - 2026-06-15`; pendiente de publicaciÃ³n manual.
- **ColecciÃ³n principal incoherente:** `/collections/murales` se llama `Todos los Papeles Pintados`, pero su regla excluye `Papel Pintado`. Debe definirse si serÃ¡ la colecciÃ³n de murales o la colecciÃ³n general antes de cambiar tÃ­tulo, reglas, enlaces, canonicals o traducciones.
- **PÃ¡ginas geogrÃ¡ficas de bajo valor:** existen 58 colecciones `comprar-papel-pintado-*`. La muestra Madrid, Barcelona, ParÃ­s y Toulouse comparte 73 productos y el mismo surtido inicial.
- **Traducciones geogrÃ¡ficas defectuosas:** hay mezcla de idiomas y traducciones literales incorrectas en EN, FR, DE y NL, aunque Shopify las marca como no desactualizadas.

## Cambios ya realizados y verificados

- Corregido el contenido cruzado de `MÃ©todos de pago` y `Conoce nuestros productos`.
- Reescrita y traducida la pÃ¡gina corporativa de productos en ES, EN, FR, DE y NL.
- Corregidos tÃ­tulos y metadatos del piloto Vista Serena y Whispering Woods.
- Preparado y validado un hotfix aislado de schema sin modificar ni publicar el tema principal.
- Corregida la gramÃ¡tica visible de la colecciÃ³n `Papeles Pintados ContemporÃ¡neos`.
- Corregidos tÃ­tulos y metatÃ­tulos de tres murales BambÃºze en ES, EN, FR, DE y NL.
- Corregida la familia de diez murales `LÃ­neas NÃ³rdicas` en tÃ­tulos y metadatos ES, EN, FR, DE y NL, sin cambiar URLs.

## Decisiones pendientes antes de ejecutar

- Publicar manualmente el hotfix de schema despuÃ©s de revisiÃ³n visual.
- Elegir arquitectura definitiva para murales, papel pintado y muestras.
- Usar datos de Search Console, Bing Webmaster Tools y ventas para decidir el futuro de las 58 colecciones geogrÃ¡ficas.
- No corregir masivamente sus traducciones hasta decidir cuÃ¡les merecen seguir indexadas.
- No limpiar barcodes hasta revisar impacto en feeds, logÃ­stica, Merchant Center y otros canales; la correcciÃ³n segura inmediata es impedir que se publiquen como GTIN.

## I. Nuevos hallazgos y ejecuciÃ³n de contenidos prioritarios

- [x] **I01. Corregir metadatos del blog raÃ­z en ES/EN/FR/DE/NL.** Ejecutado sin cambiar handles.
- [ ] **I02. Revisar los 11 artÃ­culos publicados y sus versiones localizadas.** Diez no tienen resumen; revisar autorÃ­a, vigencia, metadatos, enlaces, imÃ¡genes y Article schema.
- [ ] **I03. Corregir el handle `transfroma` solo con redirecciÃ³n y QA hreflang.**
- [ ] **I04. Resolver pÃ¡ginas localizadas vacÃ­as por plantilla.** Muestras EN, Sobre nosotros FR/NL y FAQ EN no muestran contenido principal.
- [ ] **I05. Consolidar FAQ.** Un H1, un Ãºnico FAQPage y respuestas comerciales verificadas.
- [ ] **I06. Validar propuesta B2B antes de mantener descuentos, muestras, envÃ­o prioritario y plazos de respuesta.**
- [ ] **I07. Corregir coordinadamente el footer ES/EN/FR/DE/NL.** No reemplazar el menÃº completo sin preservar traducciones y destinos.
- [x] **I08. Retirar la promesa no demostrada de uso exterior en Espacios pÃºblicos.** Ejecutado en ES/EN/FR/DE/NL.
- [x] **I09. Reescribir Floral y corregir su gramÃ¡tica.** Ejecutado en ES/EN/FR/DE/NL.
- [ ] **I10. Revisar 38 colecciones de Estilos, Colores y Espacios.** Retirar plantillas repetitivas y validar materiales/prestaciones por colecciÃ³n.
## Actualizacion 16 de junio de 2026 - schema hotfix

- [x] **A10-HOTFIX. Eliminar `AggregateRating` corporativo fijo no verificable.** El tema `SEO schema hotfix - 2026-06-15` esta publicado como MAIN. QA post-publicacion: 35 URLs en escritorio y 35 en movil, ES/EN/FR/DE/NL, 0 errores JSON-LD, 0 `AggregateRating` corporativos fijos y 0 GTIN/MPN falsos. Estado: `CORREGIDO Y VERIFICADO`.
- [ ] **A10-GLOBAL. Mantener auditoria completa de datos estructurados.** Sigue pendiente validar todo el catalogo, Merchant Center/Search Console, Organization, FAQ, Article, Product y posibles identificadores comerciales reales. Estado: `INCOMPLETO`.

## J. PublicaciÃ³n y elegibilidad IA â€” actualizaciÃ³n 18 de junio de 2026

- [x] **J01. Publicar el tema H1 con `MW-PUBLISH-H1-SEMANTIC-009`.** Estado: `CORREGIDO Y VERIFICADO`. Tema `178396463480` publicado; 170/170 pruebas correctas; MAIN anterior conservado para reversiÃ³n.
- [ ] **J02. Corregir deuda tecnica en sublotes.** `addEventListener`, tracking dinamico, `SyntaxError` de las cinco paginas «Nuestros productos», overflow FR/NL y CSS rastreable. Estado: `INCOMPLETO`. 010A, 010A3, 010A4, 010A5, 010B, 010C2 y 010D estan verificados en el tema auxiliar; 010A2 fue revertido al fallar su prueba critica. 010C fue ejecutado, fallo en QA centinela y quedo revertido. 010A2B fue aprobado y ejecutado el 25/06/2026, pero fallo QA con 0 eventos `input_mural_outside`; rollback R1 restauró `external-selectors.liquid`. 010A2C diagnostico el estado estable. 010A2D corrigio y verifico el tracking dinamico en el tema auxiliar con MD5 `95266feda1603e9c9ef028f0dae74c6f`; MAIN intacto y sin publicar. 010Z verifico regresion compacta, pero detecto overflow movil en uploader FR/NL dentro de `related-products`. 010C3 fue aprobado y ejecutado el 25/06/2026; el candidato MD5 `e1637667eebf1ec246786deaa2a45297` no corrigio el overflow y fue revertido. Rollback final verificado: QA `sections/related-products.liquid` MD5 `d8822a8c73cee73d61744c0b68b7a375`, igual que MAIN; `assets/theme.css` intacto. J02 sigue `INCOMPLETO`; proximo recomendado: diagnostico fino `MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-DIAG-010C4` antes de otro parche.
- [ ] **J03. Obtener CWV de campo.** Requiere CrUX/Search Console real. Estado: `NO ACCESIBLE`.
- [ ] **J04. Clasificar 7.932 URLs y aprobar polÃ­tica para 541+ muestras.** Estado: `INCOMPLETO`.
- [ ] **J05. Decidir 58 colecciones geogrÃ¡ficas y auditar 635 redirecciones.** Estado: `NO ACCESIBLE`.
- [ ] **J06. Verificar Bing Webmaster Tools para Bing/Edge/Copilot, diseÃ±ar IndexNow y medir Yahoo por separado.** Estado: `NO ACCESIBLE`.
- [ ] **J07. Aprobar polÃ­tica de crawlers IA para ChatGPT, Claude, Perplexity/Comet y Grok tras auditar robots, CDN y WAF.** Estado: `DECLARADO PERO NO VERIFICADO`.
- [ ] **J08. Crear entidad factual MatchWalls ES/EN/FR/DE/NL.** Estado: `INCOMPLETO`.
- [ ] **J09. Alinear Organization, WebSite, Product, Offer, Breadcrumb y Article.** Estado: `INCOMPLETO`.
- [ ] **J10. Crear guÃ­as, comparativas, casos B2B, tablas y calculadoras.** Estado: `INCOMPLETO`.
- [ ] **J11. Implantar panel mensual CEO/CMO.** Estado: `NO ACCESIBLE`.
- [x] **J12. Excluir Yandex del alcance activo.** Estado: `STANDBY` por decisiÃ³n de Daniel del 18/06/2026.

Secuencia completa: `plan-publicacion-por-oleadas-seo-geo-2026-06-18.md` y
`cola-maestra-lotes-publicacion-seo-geo-2026-06-18.csv`.





