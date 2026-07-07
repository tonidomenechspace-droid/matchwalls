# Diagnostico - MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-SOURCE-PROPOSAL-012L1

Fecha: 2026-07-04  
Tipo: diagnostico de fuente + propuesta tecnica.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Cambios tema/Liquid: no.  
Estado global: `VERIFICADO PERO MEJORABLE`

## 1. Alcance

Este lote documenta la fuente real del JSON-LD actual de las landings pais Espana/Francia y propone la siguiente capa schema segura para SEO/GEO/AGEO.

Recursos en alcance:

- Espana: `gid://shopify/Page/687276622200` - `papel-pintado-espana`.
- Francia: `gid://shopify/Page/687276654968` - `papel-pintado-francia`.
- Idiomas prioritarios: ES, EN, FR, DE, NL.

Fuera de alcance:

- Escritura en Shopify.
- Edicion de LangShop.
- Edicion de archivos Liquid.
- Cambios de meta titles/descriptions.
- Cambios de handles, URLs, canonicals o hreflang.
- Cambios de IT/PT, que permanecen en `STANDBY`.

## 2. Documentos leidos

- `diagnostico-MW-GEO-LANDINGS-SPAIN-FRANCE-NEXT-QUEUE-012K-2026-07-04.md`.
- `diagnostico-MW-GEO-LANDINGS-SPAIN-FRANCE-LINKS-HREFLANG-SCHEMA-QA-012L-2026-07-04.md`.
- `matriz-MW-GEO-LANDINGS-SPAIN-FRANCE-NEXT-QUEUE-012K-2026-07-04.csv`.
- `matriz-MW-GEO-LANDINGS-SPAIN-FRANCE-LINKS-HREFLANG-SCHEMA-QA-012L-2026-07-04.csv`.
- `auditoria-schema.md`.
- `cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`.
- `registro-cambios-ejecutados.md`.

## 3. Estado real comprobado

### 3.1 Estado Admin ya verificado en 012K/012L

La lectura Admin previa registrada en 012K/012L confirma:

- Las paginas Espana y Francia estan publicadas.
- `global.title_tag`: `null`.
- `global.description_tag`: `null`.
- Traducciones FR/EN/DE/NL de `title`, `handle` y `body_html`: presentes y `outdated=false`.
- Handles traducidos prioritarios correctos.

Estado: `CORREGIDO Y VERIFICADO` para contenido y handles prioritarios; `STANDBY` para metas SEO manuales por la incidencia 012J.

Limitacion operativa de 012L1:

- En este entorno no hay CLI Shopify disponible; por tanto, no se declara una nueva lectura Admin independiente en 012L1. La propuesta se apoya en la evidencia Admin ya registrada y en comprobaciones publicas actuales de HTML.

### 3.2 HTML publico comprobado en 012L1

Comprobacion publica actual:

| URL | Estado | JSON-LD detectado | H1 publico |
| --- | --- | --- | --- |
| `https://www.matchwalls.com/` | 200 | `BreadcrumbList`, `Organization`, `WebSite`, `SearchAction` | `Papeles pintados para paredes y murales` |
| `https://www.matchwalls.com/pages/papel-pintado-espana` | 200 | `BreadcrumbList` | `Papel pintado en España para hogares y proyectos profesionales` |
| `https://www.matchwalls.com/pages/papel-pintado-francia` | 200 | `BreadcrumbList` | `Papel pintado en Francia para interiores y proyectos profesionales` |

Estado tecnico del schema actual en landings pais: `VERIFICADO Y CORRECTO`.

Estado estrategico SEO/GEO/AGEO: `VERIFICADO PERO MEJORABLE`, porque las landings pais no exponen aun una entidad de pagina suficientemente clara (`WebPage`) ni sus preguntas visibles (`FAQPage`).

## 4. Fuente real del schema actual

Fuente localizada en tema:

| Archivo | Rol observado | Estado |
| --- | --- | --- |
| `layout/theme.liquid` | Llama a `{% render 'microdata-schema' %}` en el `<head>`. | `VERIFICADO Y CORRECTO` |
| `snippets/microdata-schema.liquid` | Genera `BreadcrumbList` global; `Product` en productos; `BlogPosting` en articulos; `WebSite` y `Organization` solo en home. | `VERIFICADO Y CORRECTO` |
| `sections/main-page.liquid` | Renderiza `<h1>{{ page.title }}</h1>` y `{{ page.content }}` para paginas normales. No genera JSON-LD. | `VERIFICADO Y CORRECTO` |
| `sections/faq.liquid` | Puede generar `FAQPage`, pero solo cuando se usa la seccion FAQ con bloques. No es la fuente de las FAQs visibles dentro del body HTML de estas landings. | `VERIFICADO PERO MEJORABLE` |

Tema MAIN documentado en la auditoria vigente:

- `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol: `MAIN`.
- `snippets/microdata-schema.liquid` conserva el mismo checksum schema publicado tras el hotfix de junio documentado en `auditoria-schema.md`.

## 5. Lectura tecnica

Hecho verificado:

- Las landings pais estan usando el flujo general de paginas Shopify:
  - `layout/theme.liquid` -> `snippets/microdata-schema.liquid`.
  - `templates/page.json` -> `sections/main-page.liquid`.
- El JSON-LD actual de las landings pais es valido, pero limitado a breadcrumb.
- La home si tiene una base `Organization`/`WebSite`, por lo que no conviene duplicar sin criterio una entidad Organization completa en cada landing.

Inferencia razonable:

- La ampliacion correcta debe ser una capa adicional especifica para las landings pais, no una sustitucion del BreadcrumbList actual.
- La implementacion futura deberia enlazar los nodos por `@id` para que buscadores y sistemas IA entiendan la relacion entre:
  - la pagina pais;
  - la entidad MatchWalls;
  - el sitio web;
  - las preguntas visibles de la pagina.

## 6. Criterios externos aplicables

Fuentes oficiales consultadas:

- Google Search Central: datos estructurados ayudan a clasificar y explicar el contenido de una pagina, y Google recomienda JSON-LD cuando sea posible.
- Google Structured Data Guidelines: el marcado debe representar contenido visible, estar en la pagina que describe y no garantiza resultados enriquecidos.
- Google Organization Schema: Organization ayuda sobre todo a desambiguar la entidad en la home y debe usar propiedades reales y relevantes.
- Bing Webmaster Blog: Bing declara soporte JSON-LD y advierte contra informacion incorrecta o spam en el marcado.
- Schema.org: vocabulario compartido usado por Google, Microsoft/Bing, Yahoo y otros sistemas.

Enlaces:

- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- https://developers.google.com/search/docs/appearance/structured-data/organization
- https://blogs.bing.com/webmaster/august-2018/Introducing-JSON-LD-Support-in-Bing-Webmaster-Tools
- https://schema.org/

## 7. Propuesta schema segura

### 7.1 Mantener

Mantener sin tocar:

- `BreadcrumbList` actual.
- Canonical actual.
- Hreflang actual.
- Meta titles/descriptions actuales.
- Handles y URLs.
- Contenido visible de pagina.
- Traducciones LangShop.

### 7.2 Anadir posteriormente, si se aprueba un lote de implementacion

Propuesta de capa adicional:

| Tipo schema | Aplicacion | Motivo |
| --- | --- | --- |
| `WebPage` | Una entidad por cada URL pais/idioma. | Define de forma explicita que la pagina es una landing informativa/comercial de pais. |
| `FAQPage` | Solo si las 3 preguntas/respuestas visibles se extraen o replican exactamente por idioma. | Las FAQs ya son visibles en el body; ayuda a estructurar respuestas citables. |
| Referencia a `Organization` | Enlace por `publisher` o `isPartOf`, reutilizando `@id` estable de MatchWalls. | Conecta la pagina con la entidad de marca sin duplicar Organization completo innecesariamente. |
| `WebSite` como referencia | `isPartOf` hacia el sitio. | Refuerza pertenencia y arquitectura semantica. |

No recomendado ahora:

- `LocalBusiness`, porque MatchWalls vende online/internacionalmente y no se ha definido una estrategia local verificable para cada ciudad o pais.
- `Service`, hasta que se defina si la pagina representa un servicio concreto o una categoria editorial/comercial.
- `Article`, porque estas landings no son articulos fechados ni tienen autor/editorial visible.
- `AggregateRating` o `Review`, salvo que exista fuente visible, verificable y elegible.
- GTIN/MPN inventados o heredados de IDs internos.

## 8. Arquitectura recomendada

Opcion recomendada para el siguiente paso:

1. Crear un prototipo Liquid local/no publicado para las landings pais.
2. No tocar tema MAIN.
3. No tocar LangShop.
4. No tocar contenido visible.
5. Validar que el JSON-LD generado:
   - parsea sin errores;
   - no duplica BreadcrumbList;
   - no crea datos invisibles;
   - respeta idioma y URL canonica;
   - se limita a ES/EN/FR/DE/NL.

Decision tecnica preliminar:

- Preferible modificar de forma controlada `snippets/microdata-schema.liquid` en un tema duplicado/no publicado, porque ya es la fuente central del schema.
- Alternativa mas limpia: crear un snippet nuevo tipo `geo-landing-schema` y renderizarlo desde `microdata-schema.liquid`; riesgo menor de mezclar logica, pero deja un archivo adicional que deberia poder revertirse.
- No se recomienda insertar JSON-LD dentro del `body_html` de las paginas: es menos mantenible, depende de LangShop/contenido, y aumenta riesgo de divergencia entre idiomas.

## 9. Riesgos

| Riesgo | Estado | Mitigacion |
| --- | --- | --- |
| Duplicar BreadcrumbList | `RIESGO CRITICO` | No tocar el bloque actual; anadir solo `WebPage`/`FAQPage` si corresponde. |
| Marcar contenido no visible | `RIESGO CRITICO` | Solo usar texto visible ya publicado en las landings. |
| Desalineacion por idioma | `RIESGO CRITICO` | Probar las 10 URLs ES/EN/FR/DE/NL antes de publicar. |
| Organization duplicada o contradictoria | `VERIFICADO PERO MEJORABLE` | Usar referencia por `@id`, no repetir claims corporativos no auditados. |
| Tocar MAIN accidentalmente | `RIESGO CRITICO` | Prototipo primero; escritura solo con `APROBADO LOTE [...]`. |
| Expectativas de ranking/citas IA | `REQUIERE DECISION HUMANA` | Documentar que schema mejora comprension/elegibilidad, no garantiza citas ni rankings. |

## 10. Estado por componente

| Componente | Estado 012L1 | Evidencia |
| --- | --- | --- |
| Fuente BreadcrumbList | `VERIFICADO Y CORRECTO` | `snippets/microdata-schema.liquid`. |
| Schema publico landings pais | `VERIFICADO PERO MEJORABLE` | Solo `BreadcrumbList`. |
| Organization/WebSite en home | `VERIFICADO Y CORRECTO` | HTML publico home con `Organization`, `WebSite`, `SearchAction`. |
| Organization/WebPage en landings pais | `INCOMPLETO` | No detectado en HTML publico. |
| FAQ visible en landings pais | `VERIFICADO PERO MEJORABLE` | Preguntas visibles existen; aun no estan marcadas como `FAQPage`. |
| Ruta de implementacion | `REQUIERE DECISION HUMANA` | Debe decidirse entre snippet central o snippet separado en tema no publicado. |

## 11. Siguiente lote seguro recomendado

`MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-LIQUID-PROTOTYPE-012L2`

Tipo: prototipo local / propuesta tecnica sin escritura Shopify.

Objetivo:

1. Preparar el modelo exacto de JSON-LD para Espana/Francia en ES/EN/FR/DE/NL.
2. Definir si se implementa como bloque dentro de `microdata-schema.liquid` o como snippet separado.
3. Validar Liquid y JSON-LD antes de cualquier escritura.
4. Preparar pruebas post-implementacion:
   - 10 URLs pais;
   - JSON parse;
   - Rich Results Test cuando aplique;
   - canonical/hreflang sin regresion;
   - no stale metas 012J.

No ejecutar escritura en Shopify hasta que Daniel apruebe exactamente:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-LIQUID-PROTOTYPE-012L2`

## 12. Decision

012L1 queda cerrado como propuesta y localizacion de fuente.

No hay cambio urgente que ejecutar en produccion. El siguiente movimiento correcto es prototipar schema en local/no publicado y validarlo antes de tocar Shopify.

