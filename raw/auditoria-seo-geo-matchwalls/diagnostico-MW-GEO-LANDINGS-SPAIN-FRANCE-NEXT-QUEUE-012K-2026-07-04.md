# Diagnostico - MW-GEO-LANDINGS-SPAIN-FRANCE-NEXT-QUEUE-012K

Fecha: 2026-07-04  
Tipo: diagnostico de continuidad, cola y siguiente lote seguro.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Cambios tema: no.  
Estado global: `VERIFICADO PERO MEJORABLE`

## 1. Documentos leidos

- `registro-cambios-ejecutados.md`
- `programa-ejecucion-seo-geo.md`
- `lista-maestra-errores-cambios-evoluciones-mejoras.md`
- `cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`
- `plan-operativo-vigente-y-cola-lotes-seo-geo-2026-06-30.md`
- `diagnostico-MW-GEO-LANDINGS-CONTENT-REVIEW-012E-2026-07-03.md`
- `ejecucion-MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F-2026-07-03.md`
- `diagnostico-MW-GEO-LANDINGS-I18N-SPAIN-FRANCE-012G-2026-07-03.md`
- `copy-map-MW-GEO-LANDINGS-I18N-COPY-MAP-SPAIN-FRANCE-012G1-2026-07-03.md`
- `linguistic-qa-MW-GEO-LANDINGS-I18N-LINGUISTIC-QA-012G2-2026-07-03.md`
- `ejecucion-MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H-2026-07-03.md`
- `diagnostico-MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I-2026-07-03.md`
- `diagnostico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-CACHE-STABILITY-RECHECK-012J4F-2026-07-04.md`
- `diagnostico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-CACHE-STABILITY-RECHECK-012J4F-R2-2026-07-04.md`

## 2. Estado real comprobado en Shopify Admin

Consulta Shopify Admin GraphQL validada contra esquema y ejecutada en solo lectura.

### Pagina pais Espana

- Recurso: `gid://shopify/Page/687276622200`
- Handle base: `papel-pintado-espana`
- Titulo base ES: `Papel pintado en España para hogares y proyectos profesionales`
- Publicada: si
- `publishedAt`: `2024-11-06T19:44:20Z`
- `updatedAt`: `2026-07-04T00:07:41Z`
- `templateSuffix`: vacio
- `global.title_tag`: `null`
- `global.description_tag`: `null`
- Traducciones globales Admin:
  - FR: `title`, `handle`, `body_html` presentes y `outdated=false`
  - EN: `title`, `handle`, `body_html` presentes y `outdated=false`
  - DE: `title`, `handle`, `body_html` presentes y `outdated=false`
  - NL: `title`, `handle`, `body_html` presentes y `outdated=false`
- Handles traducidos verificados:
  - FR: `papier-peint-en-espagne`
  - EN: `spain-wallpaper`
  - DE: `spanien-tapete`
  - NL: `spanje-behang`

Estado: `CORREGIDO Y VERIFICADO` para titulo/body/handles traducidos; `VERIFICADO PERO MEJORABLE` para meta descriptions porque siguen autogeneradas.

### Pagina pais Francia

- Recurso: `gid://shopify/Page/687276654968`
- Handle base: `papel-pintado-francia`
- Titulo base ES: `Papel pintado en Francia para interiores y proyectos profesionales`
- Publicada: si
- `publishedAt`: `2024-11-06T19:47:59Z`
- `updatedAt`: `2026-07-03T11:57:06Z`
- `templateSuffix`: vacio
- `global.title_tag`: `null`
- `global.description_tag`: `null`
- Traducciones globales Admin:
  - FR: `title`, `handle`, `body_html` presentes y `outdated=false`
  - EN: `title`, `handle`, `body_html` presentes y `outdated=false`
  - DE: `title`, `handle`, `body_html` presentes y `outdated=false`
  - NL: `title`, `handle`, `body_html` presentes y `outdated=false`
- Handles traducidos verificados:
  - FR: `papier-peint-en-france`
  - EN: `french-wallpaper`
  - DE: `franzosische-tapete`
  - NL: `frans-behang`

Estado: `CORREGIDO Y VERIFICADO` para titulo/body/handles traducidos; `VERIFICADO PERO MEJORABLE` para meta descriptions porque siguen autogeneradas.

## 3. QA publica ejecutada

Se verificaron 10 URLs publicas con user-agent de navegador y `Accept-Language` por idioma:

- Espana ES/EN/FR/DE/NL.
- Francia ES/EN/FR/DE/NL.

Resultado:

- 10/10 URLs devuelven HTTP 200.
- 10/10 canonical presentes y bajo `https://www.matchwalls.com/`.
- 10/10 sin `noindex`.
- 10/10 con H1 publico en el idioma esperado.
- 10/10 sin aparicion del valor obsoleto 012J3.
- Meta descriptions publicas presentes, derivadas del body y de longitud aproximada 319-320 caracteres.

Estado: `VERIFICADO Y CORRECTO` para accesibilidad publica basica.  
Estado: `VERIFICADO PERO MEJORABLE` para snippets SEO, porque son automaticos y largos.

## 4. Que queda cerrado

| Lote | Estado 012K | Criterio |
| --- | --- | --- |
| `MW-GEO-LANDINGS-CONTENT-REVIEW-012E` | `VERIFICADO Y CORRECTO` | Revision/documentacion de borradores realizada; no implicaba escritura. |
| `MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F` | `CORREGIDO Y VERIFICADO` | Paginas base ES Espana/Francia actualizadas y publicadas; valores actuales coinciden. |
| `MW-GEO-LANDINGS-I18N-SPAIN-FRANCE-012G` | `VERIFICADO Y CORRECTO` | Diagnostico y preparacion i18n completados. |
| `MW-GEO-LANDINGS-I18N-COPY-MAP-SPAIN-FRANCE-012G1` | `VERIFICADO Y CORRECTO` | Copy map creado para idiomas prioritarios. |
| `MW-GEO-LANDINGS-I18N-LINGUISTIC-QA-012G2` | `VERIFICADO Y CORRECTO` | QA linguistica documentada antes de LangShop. |
| `MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H` | `CORREGIDO Y VERIFICADO` | Traducciones `title`, `body_html` y handles conservados/actualizados en LangShop/Admin; `outdated=false`. |
| `MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I` | `VERIFICADO PERO MEJORABLE` | No se detectaron claves SEO traducibles por Admin; HTML publico correcto pero snippets automaticos. |
| Serie `012J` cache/meta Espana | `VERIFICADO Y CORRECTO` en la muestra final | La incidencia 012J3 no se reproduce en los rechecks finales; limitada a la pagina Espana y a user-agents simulados. |

## 5. Pendiente vigente

| Area | Estado | Motivo |
| --- | --- | --- |
| SEO meta manual/i18n para paginas pais | `STANDBY` | LangShop no guardo de forma fiable los campos SEO; la prueba nativa Shopify 012J3 genero incidencia de cache. No escalar aun. |
| Enlaces internos de las landings pais | `INCOMPLETO` | Se ven CTAs en body, pero falta auditoria de destinos 200/canonical/noindex por idioma. |
| Hreflang/canonical de las 10 URLs pais | `INCOMPLETO` | La QA 012K solo confirma canonical presente, no matriz hreflang completa ni reciprocidad. |
| Schema publico en landings pais | `INCOMPLETO` | Falta comprobar Organization/Breadcrumb/FAQ/Article/WebPage y coherencia con contenido visible. |
| Snippets SEO optimizados por idioma | `STANDBY` | Copy preparado en 012I1, pero no hay ruta de guardado segura aprobada tras incidencia 012J. |
| Landings ciudad Espana/Francia | `INCOMPLETO` | Estrategia recibida: proteger/mejorar las existentes antes de crear nuevas; falta inventario y QA especifica. |
| Briefs DE/NL/UK/BE | `INCOMPLETO` | Deben prepararse en documentos antes de tocar Shopify. |
| GSC/Bing/CrUX/IA real | `NO ACCESIBLE` | Sin acceso directo documentado en este lote; no se declaran datos reales de impresiones/citas. |

## 6. Siguiente lote seguro recomendado

`MW-GEO-LANDINGS-SPAIN-FRANCE-LINKS-HREFLANG-SCHEMA-QA-012L`

Tipo: diagnostico de solo lectura.  
Escritura Shopify/LangShop: no.  
Objetivo:

1. Verificar las 10 URLs Espana/Francia en ES, EN, FR, DE y NL.
2. Extraer y validar:
   - status HTTP;
   - canonical exacto;
   - hreflang y reciprocidad;
   - robots/noindex;
   - H1/title/meta description;
   - JSON-LD/schema visible;
   - CTAs/enlaces internos del body y sus destinos.
3. Clasificar cada problema en matriz con prioridad y riesgo.
4. Definir si el siguiente lote debe ser:
   - correccion de enlaces internos;
   - mejora de schema;
   - reintento controlado de snippets SEO;
   - o inventario de landings ciudad.

Razon: antes de crear mas contenido o tocar metas, conviene asegurar que las dos paginas pais ya mejoradas son perfectamente rastreables, coherentes y citables en los cinco idiomas prioritarios.

## 7. Que NO se debe hacer ahora

- No editar metas SEO nativas de Shopify para estas paginas.
- No intentar guardar SEO meta en LangShop hasta tener ruta fiable o soporte.
- No cambiar handles, URLs ni redirecciones.
- No crear landings DE/NL/UK/BE sin briefing/copy aprobado.
- No hacer noindex masivo de landings geograficas sin GSC y decision humana.

## 8. Decision operativa

012K queda cerrado como diagnostico de continuidad.

Siguiente paso operativo recomendado: `MW-GEO-LANDINGS-SPAIN-FRANCE-LINKS-HREFLANG-SCHEMA-QA-012L`.

Este siguiente lote es de solo lectura y encaja con la estrategia SEO/GEO/AGEO: hacer que las landings existentes sean rastreables, entendibles, enlazables y coherentes antes de escalar nuevas paginas.

