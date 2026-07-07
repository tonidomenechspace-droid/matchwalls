# Decisión MW-BING-AI-CITED-EN-COLLECTIONS-ROOT-DECISION-013E9 — 2026-07-04

## Estado

`REQUIERE DECISION HUMANA`

Documento de decisión estratégica sobre `https://www.matchwalls.com/en/collections/`, URL citada por Microsoft Copilot/partners en Bing Webmaster Tools / AI Performance.

No se ha modificado Shopify, Bing, IndexNow, sitemap, DNS, CDN, tema, páginas, colecciones, `robots.txt`, URLs, handles, redirecciones, canonicals, hreflang ni campos SEO.

## Documentos y evidencias leídos

`VERIFICADO Y CORRECTO`

- `diagnostico-MW-BING-AI-CITED-EN-COLLECTIONS-ROOT-DIAG-013E8-2026-07-04.md`.
- `collections-root-diagnostic-MW-BING-AI-CITED-EN-COLLECTIONS-ROOT-DIAG-013E8-2026-07-04.csv`.
- `qa-MW-BING-AI-CITED-URLS-CANONICAL-INDEXABILITY-QA-013E7-2026-07-04.md`.
- `qa-MW-BING-WEBMASTER-AI-PERFORMANCE-PAGES-EXPORT-013E6-2026-07-04.md`.
- `addendum-plan-operativo-vigente-2026-07-04.md`.
- `registro-cambios-ejecutados.md`.

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

La URL `https://www.matchwalls.com/en/collections/` no es una URL accidental ni rota.

Hechos verificados en 013E8:

- HTTP `200`.
- HTML lang `en`.
- Title limpio: `Collections`.
- H1: `All collections`.
- Canonical: `https://www.matchwalls.com/en/collections`.
- Sin `noindex` detectado.
- Permitida por robots para Bingbot según 013E7.
- Presente en sitemap hijo EN de colecciones.
- Enlazada internamente desde páginas públicas revisadas.
- 105 enlaces internos únicos detectados.
- 76 enlaces a colecciones.
- 0 enlaces directos a productos detectados en esa extracción.

## Problema

`RIESGO CRITICO`

La URL funciona técnicamente, pero no es una buena fuente prioritaria para IA/GEO/AGEO:

1. El title `Collections` y el H1 `All collections` son genéricos.
2. No responde una intención clara de compra, medición, instalación, materiales, B2B o GEO.
3. Mezcla colecciones geográficas, estilos, colores, categorías y campañas como Black Friday.
4. Puede competir con páginas más útiles y citables, como guías, landings país, páginas de medición, formularios profesionales o categorías editoriales.
5. Ya aparece citada por Microsoft Copilot/partners, por lo que el riesgo no es teórico.

## Opciones evaluadas

### Opción 1 — No hacer nada

Estado: `VERIFICADO PERO MEJORABLE`

No recomendada como cierre. Mantener la URL sin actuar evita riesgo inmediato, pero deja viva una fuente genérica que ya está siendo usada como cita por IA.

### Opción 2 — Noindex inmediato de `/en/collections/`

Estado: `REQUIERE DECISION HUMANA`

No recomendado ahora. Puede reducir la probabilidad de cita de una URL genérica, pero sería una decisión parcial sobre una sola variante EN sin auditar equivalentes ES, FR, DE y NL. También puede afectar navegación, sitemap, hreflang o señales internas si se aplica mal.

### Opción 3 — Redirección inmediata

Estado: `INCORRECTO`

No recomendada. Una redirección desde un índice de colecciones a una landing o categoría concreta puede romper expectativa de usuario, crear conflicto de intención y generar deuda de redirecciones.

### Opción 4 — Mantener indexable de forma temporal y convertir el hub en una fuente útil

Estado: `REQUIERE DECISION HUMANA`

Opción preferida, pero solo después de diagnóstico completo de los hubs raíz de colecciones por idioma. La idea sería transformar el índice genérico en un hub útil, claro y citable:

- Introducción editorial breve.
- Agrupación por intención: estilos, estancias, colores, materiales, colecciones geográficas priorizadas.
- Eliminación o degradación de colecciones obsoletas/no estratégicas.
- Enlaces hacia páginas prioritarias reales.
- Coherencia ES, EN, FR, DE y NL.

### Opción 5 — Ajuste mínimo de title/H1/meta

Estado: `VERIFICADO PERO MEJORABLE`

Puede mejorar algo, pero no resuelve el problema central si el cuerpo sigue siendo un listado mixto y poco explicativo. No debe ser la única acción.

## Decisión recomendada

`REQUIERE DECISION HUMANA`

No ejecutar noindex, redirección ni cambio de contenido ahora.

Mantener `/en/collections/` indexable de forma temporal, pero no aceptarla como estado final. El siguiente paso correcto es auditar todos los hubs raíz de colecciones en idiomas prioritarios antes de tocar Shopify:

`MW-COLLECTIONS-ROOT-HUB-I18N-DIAG-013E10`

Alcance recomendado del siguiente lote:

- `/collections/`
- `/en/collections/`
- `/fr/collections/`
- `/de/collections/`
- `/nl/collections/`

Comprobar en cada idioma:

- HTTP, canonical, noindex, hreflang y sitemap.
- Title, H1, meta description y texto visible.
- Cantidad y tipo de enlaces internos.
- Presencia de colecciones geográficas, Black Friday, campañas obsoletas y colecciones no prioritarias.
- Si el hub ayuda o diluye la estrategia SEO/GEO/AGEO.
- Relación con citas Bing/Copilot actuales.

## Qué queda prohibido hasta nueva aprobación

`STANDBY`

No hacer todavía:

- Noindex.
- Redirección.
- Cambio de handle o URL.
- Edición de plantilla/theme.
- Edición masiva de colecciones.
- Eliminación de enlaces.
- Cambios de sitemap.
- Cambios de LangShop.

## Riesgos controlados

`VERIFICADO PERO MEJORABLE`

La decisión evita dos errores:

1. Dejar una URL genérica citada por IA sin plan.
2. Hacer un noindex/redirect precipitado sobre una URL real, enlazada e incluida en sitemap.

## Criterio de salida futuro

`REQUIERE DECISION HUMANA`

El problema se considerará encaminado cuando exista:

- Diagnóstico comparativo ES/EN/FR/DE/NL.
- Decisión aprobada sobre si los hubs raíz de colecciones deben:
  - mantenerse y mejorarse;
  - quedarse indexables con ajustes mínimos;
  - pasar a noindex;
  - redirigirse;
  - o quedar en standby.
- Propuesta de ejecución reversible si hay escritura.
- QA público posterior.

## Evidencia generada en este lote

- Documento: `decision-MW-BING-AI-CITED-EN-COLLECTIONS-ROOT-DECISION-013E9-2026-07-04.md`.
- Matriz: `decision-matrix-MW-BING-AI-CITED-EN-COLLECTIONS-ROOT-DECISION-013E9-2026-07-04.csv`.

## Estado final del lote

`REQUIERE DECISION HUMANA`

La URL `/en/collections/` debe tratarse como un hub real, no como basura indexable. La recomendación profesional es no tocarla todavía y abrir un diagnóstico de hubs raíz de colecciones en los cinco idiomas prioritarios.
