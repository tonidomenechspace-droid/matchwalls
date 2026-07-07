# Resultado - MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-EXCLUDE-DECISION-013E16B

Fecha: 2026-07-05

## Estado final

`REQUIERE DECISION HUMANA`

Lote indicado por Daniel:

`MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-EXCLUDE-DECISION-013E16B`

Este lote fue diagnóstico/de decisión. No se modificó Shopify.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `black-friday-policy-MW-COLLECTIONS-I18N-CARD-TITLES-COPY-MAP-013E15-2026-07-05.md`
- `copy-map-MW-COLLECTIONS-I18N-CARD-TITLES-COPY-MAP-013E15-2026-07-05.csv`
- `registro-cambios-ejecutados.md`

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

Shopify Admin GraphQL confirma un único recurso Black Friday:

- Resource ID: `gid://shopify/Collection/646234440056`
- Handle base: `papel-pintado-black-friday`
- Título base: `Papel Pintado Black Friday`
- Productos: `0`
- SEO base: referencia Black Friday 2024.
- EN meta title: referencia Black Friday 2025.
- FR `body_html`: anomalía detectada, contiene `Acheter du papier peint Toulouse - MatchWalls`.
- Traducciones visibles:
  - EN: `Black Friday Wallpaper`
  - FR: `Papier Peint Black Friday`
  - DE: `Tapete Black Friday`
  - NL: `Behang Black Friday`

## Verificación pública

`VERIFICADO PERO MEJORABLE`

Muestreo público:

- EN hub `/en/collections`: enlaza `/en/collections/wallpapers-black-friday`.
- FR hub `/fr/collections`: enlaza `/fr/collections/papiers-peints-black-friday`.
- NL hub `/nl/collections`: enlaza `/nl/collections/black-friday-wallpaper`.
- DE hub `/de/collections`: contiene texto `Black Friday`, aunque en el muestreo final no se extrajo href `black-friday`.
- ES hub `/collections`: `NO ACCESIBLE` por 429 en el muestreo.

Páginas directas:

- FR, DE y NL respondieron `200` y contienen `noindex,nofollow`.
- EN respondió `503` en el muestreo directo final.
- ES respondió `429` en el muestreo directo final.

La variabilidad pública indica que debe evitarse una escritura ciega y localizar primero la fuente exacta del render del hub.

## Diagnóstico SEO/GEO/AEO

`INCORRECTO`

Black Friday no debe estar enlazado desde hubs evergreen en temporada no activa porque:

- Es una campaña temporal.
- Tiene `0` productos.
- Conserva metadatos de 2024/2025.
- Algunas variantes están `noindex,nofollow`.
- Hay una anomalía editorial en FR.
- Envía señal contradictoria a Google, Bing/Copilot, buscadores e IA: página enlazada como categoría permanente, pero tratada como contenido sin valor evergreen/noindex.

## Decisión técnica recomendada

`REQUIERE DECISION HUMANA`

Recomendación: excluir Black Friday de la visualización en hubs/listados evergreen, sin borrar la colección, sin cambiar handles, sin cambiar URLs y sin crear redirecciones.

No recomiendo todavía ejecutar una exclusión directa hasta confirmar si el render procede de:

1. `sections/main-list-collections.liquid` del tema MAIN/draft.
2. Configuración del template/listado de colecciones.
3. Contenido traducido o bloque específico creado en la arquitectura de hubs.

## Qué NO hacer

`VERIFICADO Y CORRECTO`

- No borrar colecciones Black Friday.
- No cambiar handles.
- No cambiar URLs.
- No crear redirecciones.
- No cambiar meta titles/metas en este lote.
- No tocar LangShop.
- No tocar tema MAIN sin diagnóstico de fuente y aprobación exacta.

## Siguiente lote seguro recomendado

`REQUIERE DECISION HUMANA`

`MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-RENDER-SOURCE-DIAG-013E16C`

Objetivo:

- Identificar exactamente de dónde sale Black Friday en los hubs/listados evergreen.
- Comparar MAIN y draft si aplica.
- Proponer una exclusión quirúrgica y reversible.
- No escribir Shopify.

Lote posterior, solo si 013E16C confirma la fuente:

`MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-SAFE-EXCLUDE-013E16D`

## Evidencias

`VERIFICADO Y CORRECTO`

- `admin-read-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-EXCLUDE-DECISION-013E16B-2026-07-05.csv`
- `public-qa-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-EXCLUDE-DECISION-013E16B-2026-07-05.csv`
- `resultado-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-EXCLUDE-DECISION-013E16B-2026-07-05.md`
