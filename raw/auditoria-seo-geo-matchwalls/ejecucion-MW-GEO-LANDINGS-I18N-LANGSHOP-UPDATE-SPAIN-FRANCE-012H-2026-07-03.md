# Ejecución — MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H

Fecha: 2026-07-03  
Estado final del alcance aprobado: `CORREGIDO Y VERIFICADO`  
Cambios Shopify/LangShop: sí, ejecutados manualmente por Daniel en LangShop / Shopify Translate con guía de Codex.  

## 1. Aprobación

Aprobación exacta recibida:

`APROBADO LOTE MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H`

## 2. Alcance aprobado

Páginas:

- España: `gid://shopify/Page/687276622200`, handle base `papel-pintado-espana`.
- Francia: `gid://shopify/Page/687276654968`, handle base `papel-pintado-francia`.

Idiomas ejecutados:

- España: FR, EN, DE, NL.
- Francia: EN, DE, NL.

Idioma no tocado:

- Francia FR; ya estaba `CORREGIDO Y VERIFICADO` desde 012F.

Campos actualizados:

- `title`
- `body_html`

Campos excluidos:

- handles / slugs localizados;
- SEO title;
- meta description;
- productos;
- colecciones;
- redirecciones;
- tema/Liquid;
- schema;
- inventario;
- precios.

## 3. Ejecución

La ejecución fue manual en LangShop / Shopify Translate. Codex guio campo por campo y Daniel confirmó:

- `GUARDADO ESPAÑA FR 012H`
- `GUARDADO ESPAÑA EN 012H`
- `GUARDADO ESPAÑA DE 012H`
- `GUARDADO ESPAÑA NL 012H`
- `GUARDADO FRANCIA EN 012H`
- `GUARDADO FRANCIA DE 012H`
- `GUARDADO FRANCIA NL 012H`

## 4. Verificación Admin

Shopify Admin GraphQL de solo lectura verificado tras los guardados:

- Todos los `title` y `body_html` actualizados en el alcance figuran con `outdated=false`.
- Los handles localizados mantienen fechas antiguas, señal de que no fueron modificados.
- Francia FR sigue `outdated=false` y no se tocó.

Archivo:

- `admin-post-MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H-2026-07-03.csv`

## 5. QA público

URLs verificadas:

- `https://www.matchwalls.com/pages/papel-pintado-espana?mwqa=012h`
- `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne?mwqa=012h`
- `https://www.matchwalls.com/en/pages/spain-wallpaper?mwqa=012h`
- `https://www.matchwalls.com/de/pages/spanien-tapete?mwqa=012h`
- `https://www.matchwalls.com/nl/pages/spanje-behang?mwqa=012h`
- `https://www.matchwalls.com/pages/papel-pintado-francia?mwqa=012h`
- `https://www.matchwalls.com/fr/pages/papier-peint-en-france?mwqa=012h`
- `https://www.matchwalls.com/en/pages/french-wallpaper?mwqa=012h`
- `https://www.matchwalls.com/de/pages/franzosische-tapete?mwqa=012h`
- `https://www.matchwalls.com/nl/pages/frans-behang?mwqa=012h`

Resultado:

- 10/10 HTTP 200.
- H1 actualizado en todos los idiomas.
- Canonical propio en todos los idiomas.
- 8 hreflang detectados en todos los idiomas.
- Sin `noindex`.
- Sin marcadores del contenido antiguo de envíos gratuitos/listados.

Archivo:

- `qa-publico-post-MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H-2026-07-03.csv`

## 6. QA CTAs

Se verificaron 16 URLs CTA FR/EN/DE/NL.

Resultado:

- 16/16 HTTP 200.

Archivo:

- `qa-ctas-post-MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H-2026-07-03.csv`

## 7. Incidencias y deuda nueva

Incidencia de alcance:

- En LangShop, Daniel observó que el SEO title/meta description de la vista previa seguía en español para al menos una página traducida.
- Codex confirmó que no debía tocarse dentro de 012H porque el alcance aprobado solo incluía `title` y `body_html`.

Deuda nueva:

- `MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I`
  - Diagnosticar campos SEO traducibles de páginas país.
  - Proponer title/meta description por idioma.
  - Ejecutar en lote separado si se aprueba.

Observación:

- LangShop puede seguir mostrando “Páginas” como desactualizado a nivel global porque hay más páginas fuera de este lote. Eso no contradice la verificación específica de las dos páginas de 012H.

## 8. Reversión

Si hiciera falta revertir 012H, usar:

- `copy-map-final-MW-GEO-LANDINGS-I18N-LINGUISTIC-QA-012G2-2026-07-03.md` para re-ejecutar los valores correctos actuales.
- Registros 012G/012G1 para identificar los valores antiguos sustituidos.

No se recomienda restaurar el contenido antiguo salvo necesidad crítica, porque estaba marcado `INCORRECTO`.

## 9. Evidencias

- `copy-map-final-MW-GEO-LANDINGS-I18N-LINGUISTIC-QA-012G2-2026-07-03.md`
- `admin-post-MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H-2026-07-03.csv`
- `qa-publico-post-MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H-2026-07-03.csv`
- `qa-ctas-post-MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H-2026-07-03.csv`

