# Diagnóstico — MW-GEO-LANDINGS-I18N-SPAIN-FRANCE-012G

Fecha: 2026-07-03  
Tipo: diagnóstico y preparación de siguiente lote i18n.  
Cambios Shopify: no.  
Estado global: `VERIFICADO PERO MEJORABLE`

## 1. Documentos leídos

- `AGENTS.md`
- `ejecucion-MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F-2026-07-03.md`
- `admin-post-MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F-2026-07-03.csv`
- `qa-publico-post-MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F-2026-07-03.csv`
- `registro-cambios-ejecutados.md`

## 2. Estado real comprobado en Shopify

Consulta Admin GraphQL de solo lectura validada contra esquema y ejecutada sobre:

- `gid://shopify/Page/687276622200` — `papel-pintado-espana`
- `gid://shopify/Page/687276654968` — `papel-pintado-francia`

También se comprobaron las URLs públicas localizadas ES/FR/EN/DE/NL.

## 3. Resultado por página e idioma

### España

Recurso base:

- ID: `gid://shopify/Page/687276622200`
- Handle base: `papel-pintado-espana`
- Título ES: `Papel pintado en España para hogares y proyectos profesionales`
- Estado ES base: `CORREGIDO Y VERIFICADO`

Traducciones:

- FR: `INCORRECTO`
  - Título publicado: `Papier Peint Espagne`
  - `title.outdated=true`
  - `body_html.outdated=true`
  - Body público conserva contenido antiguo de envíos gratuitos y lista provincial.
  - Handle FR conservado: `papier-peint-en-espagne`
- EN: `INCORRECTO`
  - Título publicado: `Spain wallpaper`
  - `title.outdated=true`
  - `body_html.outdated=true`
  - Body público conserva contenido antiguo de envíos gratuitos y traducciones literales.
  - Handle EN conservado: `spain-wallpaper`
- DE: `INCORRECTO`
  - Título publicado: `Spanien Tapete`
  - `title.outdated=true`
  - `body_html.outdated=true`
  - Body público conserva contenido antiguo y traducciones literales.
  - Handle DE conservado: `spanien-tapete`
- NL: `INCORRECTO`
  - Título publicado: `Spanje behang`
  - `title.outdated=true`
  - `body_html.outdated=true`
  - Body público conserva contenido antiguo y traducciones literales.
  - Handle NL conservado: `spanje-behang`

### Francia

Recurso base:

- ID: `gid://shopify/Page/687276654968`
- Handle base: `papel-pintado-francia`
- Título ES: `Papel pintado en Francia para interiores y proyectos profesionales`
- Estado ES base: `CORREGIDO Y VERIFICADO`

Traducciones:

- FR: `CORREGIDO Y VERIFICADO`
  - Título publicado: `Papier peint en France pour intérieurs résidentiels et projets professionnels`
  - `title.outdated=false`
  - `body_html.outdated=false`
  - Handle FR conservado: `papier-peint-en-france`
- EN: `INCORRECTO`
  - Título publicado: `French wallpaper`
  - `title.outdated=true`
  - `body_html.outdated=true`
  - Body público conserva contenido antiguo de envíos gratuitos.
  - Handle EN conservado: `french-wallpaper`
- DE: `INCORRECTO`
  - Título publicado: `Französische Tapete`
  - `title.outdated=true`
  - `body_html.outdated=true`
  - Body público conserva contenido antiguo y traducciones literales.
  - Handle DE conservado: `franzosische-tapete`
- NL: `INCORRECTO`
  - Título publicado: `Frans behang`
  - `title.outdated=true`
  - `body_html.outdated=true`
  - Body público conserva contenido antiguo y traducciones literales.
  - Handle NL conservado: `frans-behang`

## 4. QA público

Las 10 URLs revisadas responden 200, tienen canonical propio y exponen 8 hreflang.

El problema no es acceso técnico, canonical ni hreflang en este lote. El problema es editorial/i18n:

- FR España, EN España, DE España, NL España: contenido antiguo publicado.
- EN Francia, DE Francia, NL Francia: contenido antiguo publicado.
- FR Francia: correcto tras 012F.
- ES España y ES Francia: correctas tras 012F.

## 5. Regla LangShop / Shopify Translate

Daniel recordó que las traducciones se trabajan con Shopify Translate y la app LangShop.

Por tanto:

- No se debe pisar LangShop con mutaciones API sin decisión expresa.
- La API queda como herramienta de lectura, verificación y, solo si se aprueba, escritura controlada.
- La vía preferente para ejecución editorial i18n debe ser LangShop / Shopify Translate, con mapa exacto de campos.
- Si se usa API, debe limitarse a `title` y `body_html`; no deben modificarse handles localizados.

## 6. Riesgos

- Sobrescribir traducciones gestionadas por LangShop sin control.
- Mantener contenido viejo de envíos gratuitos y listas de ciudades en idiomas prioritarios.
- Mezclar actualización editorial con cambios de handles.
- Publicar traducciones DE/NL no revisadas con calidad nativa insuficiente.

## 7. Decisión técnica recomendada

No ejecutar aún escritura i18n.

Siguiente lote seguro:

`MW-GEO-LANDINGS-I18N-COPY-MAP-SPAIN-FRANCE-012G1`

Objetivo:

- Preparar el mapa exacto de traducciones para FR/EN/DE/NL de España y EN/DE/NL de Francia.
- Mantener FR Francia como referencia ya corregida.
- No tocar Shopify.
- Separar claramente:
  - texto final propuesto;
  - campo Shopify/LangShop afectado;
  - URL pública esperada;
  - estado lingüístico;
  - necesidad de revisión humana para DE/NL si procede.

Lote posterior de ejecución, solo con aprobación exacta:

`MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H`

## 8. Archivos de evidencia

- `admin-read-MW-GEO-LANDINGS-I18N-SPAIN-FRANCE-012G-2026-07-03.csv`
- `qa-publico-MW-GEO-LANDINGS-I18N-SPAIN-FRANCE-012G-2026-07-03.csv`

