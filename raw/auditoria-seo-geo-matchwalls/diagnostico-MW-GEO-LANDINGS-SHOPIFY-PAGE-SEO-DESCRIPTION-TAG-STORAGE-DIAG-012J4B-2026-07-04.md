# Diagnostico - MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-DESCRIPTION-TAG-STORAGE-DIAG-012J4B

Fecha: 2026-07-04  
Tipo: diagnostico de solo lectura sobre almacenamiento de `description_tag` SEO en pagina Shopify.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Cambios Shopify Translate: no.  
Mutaciones GraphQL: no.  
Estado global: `INCORRECTO`

## 1. Documentos leidos

- `diagnostico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-I18N-META-SAFE-PATH-DIAG-012J4-2026-07-04.md`
- `protocolo-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-HIDDEN-STORAGE-CHECK-012J4A-2026-07-04.md`
- `registro-cambios-ejecutados.md`
- `qa-publico-accept-language-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-HIDDEN-STORAGE-CHECK-012J4A-2026-07-04.csv`

## 2. Alcance

Recurso inspeccionado:

- Shopify Page: `gid://shopify/Page/687276622200`
- Handle base: `papel-pintado-espana`
- URL base: `https://www.matchwalls.com/pages/papel-pintado-espana`
- Idiomas prioritarios revisados: ES, EN, FR, DE, NL.
- Mercado comprobado adicionalmente: `Spain`, `gid://shopify/Market/15250456803`.

Objetivo:

- Verificar si el valor del piloto 012J3 seguia almacenado en `global.description_tag`, traducciones de pagina o traducciones especificas de mercado.

Valor exacto 012J3 investigado:

`Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural.`

## 3. Estado real comprobado por Shopify Admin GraphQL

Consulta ejecutada como solo lectura, validada previamente contra el esquema Shopify Admin.

Resultado del recurso pagina:

- `id`: `gid://shopify/Page/687276622200`
- `title`: `Papel pintado en España para hogares y proyectos profesionales`
- `handle`: `papel-pintado-espana`
- `updatedAt`: `2026-07-04T00:07:41Z`
- `isPublished`: `true`
- `global.title_tag`: `null`
- `global.description_tag`: `null`
- `metafields.nodes`: `[]`

Resultado de contenidos traducibles:

- Contenido base ES traducible: solo `title`, `body_html`, `handle`.
- Traducciones EN: solo `title`, `body_html`, `handle`.
- Traducciones FR: solo `title`, `body_html`, `handle`.
- Traducciones DE: solo `title`, `body_html`, `handle`.
- Traducciones NL: solo `title`, `body_html`, `handle`.
- Traducciones ES sobre el recurso: `[]`.

Resultado de traducciones especificas del mercado Spain:

- `translatableContent(marketId: Spain)`: `[]`.
- `translations(locale: "es", marketId: Spain)`: `[]`.
- `translations(locale: "en", marketId: Spain)`: `[]`.
- `translations(locale: "fr", marketId: Spain)`: `[]`.
- `translations(locale: "de", marketId: Spain)`: `[]`.
- `translations(locale: "nl", marketId: Spain)`: `[]`.

Clasificacion:

- Almacenamiento `global.description_tag` en API Admin: `VERIFICADO Y CORRECTO` como ausente.
- Traduccion SEO `description_tag` visible en API Admin: `VERIFICADO Y CORRECTO` como ausente.
- Metacampos de pagina: `VERIFICADO Y CORRECTO` como ausentes.

## 4. Estado publico revalidado

Se ejecutaron controles publicos con query strings nuevas y clientes HTTP diferentes.

Resultados limpios:

- Lectura HTTP limpia por Python:
  - ES default: no contiene el valor exacto 012J3.
  - ES con `Accept-Language: es-ES`: no contiene el valor exacto 012J3.
  - DE default y `de-DE`: no contienen el valor exacto 012J3.
  - NL default y `nl-NL`: no contienen el valor exacto 012J3.
  - FR y EN: no contienen el valor exacto 012J3.
  - Meta/OG/Twitter coinciden entre si y salen autogeneradas desde el contenido visible traducido.

Resultados contradictorios:

- `curl` detecto todavia el valor exacto 012J3 en ES bajo algunos contextos:
  - ES con `Accept-Language: es-ES`.
  - ES con cabeceras `Cache-Control: no-cache` / `Pragma: no-cache`.
- En otro contraste `curl`, DE y NL salieron limpios.
- PowerShell `Invoke-WebRequest` mostro resultados variables y no se usa como unica fuente de verdad, pero confirma inestabilidad de respuesta.

Clasificacion:

- HTML publico estable: `INCORRECTO`.
- Motivo: no se puede afirmar que el valor 012J3 haya desaparecido para todos los clientes/cabeceras.
- Metas actuales autogeneradas por idioma: `VERIFICADO PERO MEJORABLE`.

## 5. Diagnostico

Hechos verificados:

- El campo visible nativo de Shopify quedo vacio tras rollback 012J3, segun captura 012J3.
- LangShop ES y DE muestran campos SEO visibles vacios, segun capturas 012J4A.
- Shopify Admin GraphQL no contiene `global.description_tag`, `global.title_tag`, metacampos, traduccion ES ni traducciones SEO por EN/FR/DE/NL.
- El mercado Spain no contiene traducciones especificas para esa pagina en ES/EN/FR/DE/NL.
- El tema usa `page_description` para `meta`, `og:description` y `twitter:description`.
- El storefront publico puede emitir respuestas distintas segun cliente/cabecera.

Inferencia tecnica:

- El valor 012J3 no parece estar almacenado actualmente en el recurso Page ni en sus traducciones Admin API accesibles.
- La persistencia observada es mas compatible con una capa de render/storefront/cache/propagacion que con un `global.description_tag` activo en la pagina.

Limite de evidencia:

- No se dispone de lectura interna de cache Shopify/storefront.
- No se puede demostrar la causa exacta de la respuesta publica contradictoria.
- No se debe ejecutar limpieza de un valor que no aparece como almacenado en Admin API.

## 6. Decision operativa

No ejecutar escrituras.

No hacer:

- No volver a guardar meta description nativa ES.
- No guardar campos SEO en LangShop.
- No tocar handles, URLs, title, body ni tema.
- No crear mutaciones de limpieza, porque API Admin no muestra un valor que limpiar.

## 7. Siguiente lote seguro

Siguiente paso recomendado:

`MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-STOREFRONT-CACHE-RECHECK-012J4C`

Tipo:

- Solo lectura.

Objetivo:

- Repetir QA publico con clientes representativos de crawlers y navegadores:
  - cliente limpio sin cookies;
  - `Accept-Language` ES/EN/FR/DE/NL;
  - user-agents de navegador comun;
  - user-agents de buscador/IA solo como simulacion de cabecera, sin afirmar equivalencia real.

Criterio de salida:

- Si 3 rondas consecutivas no contienen el valor exacto 012J3: cerrar incidencia como `VERIFICADO PERO MEJORABLE` y mantener metas automaticas.
- Si el valor exacto 012J3 persiste: abrir lote de soporte/diagnostico externo con Shopify/LangShop, adjuntando:
  - API Admin con `global.description_tag = null`;
  - UI nativa vacia;
  - LangShop SEO vacio;
  - HTML publico contradictorio.

## 8. Estado final

`MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-DESCRIPTION-TAG-STORAGE-DIAG-012J4B` queda como:

- Almacenamiento Admin/API: `VERIFICADO Y CORRECTO` como limpio.
- Public HTML: `INCORRECTO` por respuestas contradictorias.
- Causa exacta: `NO ACCESIBLE`.
- Accion de escritura: ninguna.
- Siguiente paso seguro: `MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-STOREFRONT-CACHE-RECHECK-012J4C`.
