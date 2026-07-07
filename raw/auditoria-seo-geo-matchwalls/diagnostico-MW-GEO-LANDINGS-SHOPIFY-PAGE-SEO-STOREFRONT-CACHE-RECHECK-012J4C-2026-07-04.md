# Diagnostico - MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-STOREFRONT-CACHE-RECHECK-012J4C

Fecha: 2026-07-04  
Tipo: recheck publico de solo lectura sobre persistencia de metadescripcion 012J3 en storefront.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Cambios tema: no.  
Mutaciones GraphQL: no.  
Estado global: `INCORRECTO`

## 1. Documentos leidos

- `diagnostico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-DESCRIPTION-TAG-STORAGE-DIAG-012J4B-2026-07-04.md`
- `protocolo-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-HIDDEN-STORAGE-CHECK-012J4A-2026-07-04.md`
- `diagnostico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-I18N-META-SAFE-PATH-DIAG-012J4-2026-07-04.md`
- `registro-cambios-ejecutados.md`

## 2. Estado real previo comprobado

De 012J4B:

- Shopify Admin GraphQL devolvio `global.description_tag = null`.
- `global.title_tag = null`.
- La pagina no tiene metacampos.
- Las traducciones accesibles por API para EN/FR/DE/NL solo contienen `title`, `body_html` y `handle`.
- Las traducciones especificas del mercado Spain estaban vacias.
- Sin embargo el HTML publico aun podia devolver respuestas contradictorias.

## 3. Alcance exacto de 012J4C

Recurso principal:

- Shopify Page: `gid://shopify/Page/687276622200`
- ES: `https://www.matchwalls.com/pages/papel-pintado-espana`
- EN: `https://www.matchwalls.com/en/pages/spain-wallpaper`
- FR: `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`
- DE: `https://www.matchwalls.com/de/pages/spanien-tapete`
- NL: `https://www.matchwalls.com/nl/pages/spanje-behang`

Valor investigado:

`Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural.`

Campos revisados:

- `<meta name="description">`
- `og:description`
- `twitter:description`
- canonical
- `html lang`

## 4. Metodologia

Se hicieron 3 rondas con query strings nuevas.

Clientes/cabeceras:

- Navegador Chrome simulado con `Accept-Language` local ES/EN/FR/DE/NL.
- `curl` con Chrome simulado.
- `curl` con `Cache-Control: no-cache`.
- User-agents de bot como simulacion de cabecera:
  - Googlebot simulado.
  - Bingbot simulado.
  - OAI-SearchBot simulado.

Limitacion importante:

- Esto no valida crawlers reales por IP oficial.
- Solo demuestra que el storefront puede variar la salida segun user-agent/cabecera.

## 5. Resultado

El criterio de cierre exigia 3 rondas consecutivas sin el valor exacto 012J3.

Resultado: criterio no cumplido.

Hallazgos:

- Chrome simulado con idioma local: limpio en ES/EN/FR/DE/NL durante las rondas revisadas.
- DE, NL, FR, EN: limpios en las comprobaciones finales.
- ES: comportamiento inestable.
- Bajo user-agent de bot simulado, el valor 012J3 aparecio intermitentemente:
  - Googlebot simulado: contaminado en ronda 1 y ronda 3 del recheck dirigido.
  - OAI-SearchBot simulado: contaminado en ronda 1 y ronda 2 del recheck dirigido.
  - Bingbot simulado: limpio en el recheck dirigido, aunque una lectura amplia previa mostro una respuesta corta de 134 caracteres que requirio revalidacion.

Ejemplo de valor contaminado detectado:

`Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural.`

Clasificacion:

- Storefront ES bajo navegacion normal simulada: `VERIFICADO PERO MEJORABLE`.
- Storefront ES bajo cabeceras de bot simuladas: `INCORRECTO`.
- Storefront EN/FR/DE/NL en este recheck: `VERIFICADO PERO MEJORABLE`.

## 6. Diagnostico

Hechos verificados:

- La contaminacion no esta localizada en Admin API como `global.description_tag`.
- La contaminacion no esta visible en los campos SEO de LangShop ES/DE comprobados antes.
- El HTML publico puede devolver el valor 012J3 de forma intermitente para ES.
- La variacion depende del contexto de peticion.

Inferencia tecnica:

- El problema parece estar en una capa de storefront/cache/render/propagacion, no en un campo editable de pagina actualmente visible por Admin API.

Limite de evidencia:

- No se puede afirmar si Google, Bing, ChatGPT Search u otros bots reales veran exactamente esta version; no se ha validado IP oficial.
- No se puede purgar ni corregir una capa interna de Shopify desde este lote.

## 7. Decision

No ejecutar escrituras.

No hacer:

- No volver a tocar la metadescripcion nativa.
- No tocar LangShop.
- No tocar Liquid para forzar metadatos.
- No tocar handles, title, body ni rutas.

## 8. Siguiente paso seguro

Siguiente lote recomendado:

`MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SUPPORT-EVIDENCE-012J4D`

Tipo:

- Preparacion documental de evidencia para soporte Shopify/LangShop.
- Sin cambios.

Objetivo:

- Preparar un paquete claro con:
  - API Admin: `global.description_tag = null`.
  - UI nativa: metadescripcion vacia.
  - LangShop ES/DE: campos SEO vacios.
  - Storefront: valor 012J3 aparece intermitentemente bajo cabeceras de bot simuladas.
  - Pregunta tecnica concreta: por que `page_description` entrega un valor no visible ni almacenado en Admin API.

## 9. Estado final

`MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-STOREFRONT-CACHE-RECHECK-012J4C` queda:

- Estado: `INCORRECTO`.
- Causa exacta: `NO ACCESIBLE`.
- Escrituras: ninguna.
- Siguiente paso seguro: `MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SUPPORT-EVIDENCE-012J4D`.
