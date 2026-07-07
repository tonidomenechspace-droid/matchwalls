# Diagnóstico — MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I

Fecha: 2026-07-03  
Tipo: diagnóstico SEO meta i18n de páginas país España/Francia.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Estado global: `VERIFICADO PERO MEJORABLE`

## 1. Documentos leídos

- `ejecucion-MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H-2026-07-03.md`
- `qa-publico-post-MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H-2026-07-03.csv`
- `admin-post-MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H-2026-07-03.csv`
- `copy-map-final-MW-GEO-LANDINGS-I18N-LINGUISTIC-QA-012G2-2026-07-03.md`
- `registro-cambios-ejecutados.md`

## 2. Pregunta investigada

Daniel observó en LangShop que la vista previa del listado de búsqueda podía seguir mostrando SEO title/meta description en español después de actualizar `title` y `body_html`.

El objetivo de 012I fue comprobar:

- si Shopify expone SEO title/meta description traducibles para estas páginas;
- si existen metafields SEO en las páginas;
- si el HTML público realmente muestra metadatos en español en idiomas no ES;
- si hace falta un lote de corrección o solo un lote posterior de optimización.

## 3. Estado real comprobado en Shopify Admin

### Page schema

El objeto `Page` no expone un campo SEO directo en Admin GraphQL para estas páginas.

Campos relevantes disponibles:

- `title`
- `body`
- `bodySummary`
- `handle`
- `translations(locale:)`
- `metafields`

### TranslatableResource

Para las dos páginas:

- `gid://shopify/Page/687276622200` — `papel-pintado-espana`
- `gid://shopify/Page/687276654968` — `papel-pintado-francia`

Las claves traducibles expuestas son:

- `title`
- `body_html`
- `handle`

No aparecen claves:

- `seo_title`
- `meta_title`
- `meta_description`
- `description_tag`
- otras variantes SEO equivalentes.

### Metafields

Las dos páginas devuelven 0 metafields.

Conclusión Admin:

`VERIFICADO Y CORRECTO` que no hay campo SEO/meta expuesto por Shopify Admin GraphQL ni metafield SEO detectable para estas páginas.

## 4. Estado público comprobado

Se verificaron las 10 URLs públicas:

- ES/FR/EN/DE/NL España.
- ES/FR/EN/DE/NL Francia.

Resultado:

- 10/10 URLs HTTP 200.
- `title` HTML público en idioma correcto.
- `meta name="description"` público en idioma correcto.
- `og:title`, `og:description`, `twitter:title` y `twitter:description` siguen el contenido público traducido.
- No se detectó marcador español en metadatos de idiomas no ES.

Observación:

- Las meta descriptions públicas parecen autogeneradas desde el inicio del body traducido.
- Son correctas por idioma, pero largas/no optimizadas como snippets SEO manuales.

## 5. Interpretación de la preview LangShop

La preview de LangShop puede estar mostrando:

- un campo interno de preview no publicado;
- una preview basada en el idioma base antes de refrescar;
- un módulo SEO no expuesto por Admin GraphQL;
- o un estado global de LangShop, no el HTML público real.

Con la evidencia actual, no se puede afirmar que haya un problema público de SEO meta en español.

Sí se puede afirmar:

- `VERIFICADO Y CORRECTO`: el HTML público no muestra meta title/meta description en español para FR/EN/DE/NL.
- `VERIFICADO PERO MEJORABLE`: las meta descriptions son automáticas y pueden optimizarse con copy SEO específico si LangShop permite editarlo.

## 6. Estado por URL

Ver archivo:

- `qa-publico-meta-MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I-2026-07-03.csv`

## 7. Recomendación

No ejecutar corrección inmediata.

Siguiente lote recomendado:

`MW-GEO-LANDINGS-I18N-SEO-META-COPY-012I1`

Objetivo:

- Preparar SEO title/meta description breves y específicos por idioma.
- No tocar Shopify.
- Mantener coherencia con 012H.

Después, solo si LangShop muestra campos SEO editables y Daniel aprueba ejecución:

`MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-UPDATE-012J`

Objetivo:

- Actualizar manualmente SEO title/meta description en LangShop si el campo existe.
- Verificar HTML público tras guardar.

## 8. Riesgos

- Editar campos SEO en LangShop sin comprobar si publican en HTML real.
- Confundir preview LangShop con output público.
- Sobrescribir title/body ya corregidos en 012H.
- Crear meta descriptions demasiado largas o repetitivas.

## 9. Conclusión

`MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I` queda como diagnóstico cerrado:

- No hay incidencia pública crítica.
- No hay campos SEO/meta expuestos por Shopify Admin GraphQL para estas páginas.
- No hay metafields SEO en estas páginas.
- La capa pública está en el idioma correcto.
- Queda oportunidad de optimización SEO snippet en lote separado, condicionado a disponibilidad real del campo en LangShop.

