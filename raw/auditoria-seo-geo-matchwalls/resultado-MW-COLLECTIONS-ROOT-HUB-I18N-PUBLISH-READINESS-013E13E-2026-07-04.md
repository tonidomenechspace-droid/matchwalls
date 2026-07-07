# Resultado MW-COLLECTIONS-ROOT-HUB-I18N-PUBLISH-READINESS-013E13E

Fecha: 2026-07-04  
Estado final: `REQUIERE DECISION HUMANA`

## Alcance aprobado

`APROBADO LOTE MW-COLLECTIONS-ROOT-HUB-I18N-PUBLISH-READINESS-013E13E`

Lote de preparación de decisión. No es un lote de publicación.

No se ejecutaron escrituras en Shopify. No se tocó MAIN, LangShop, páginas, productos, colecciones, handles, URLs, redirecciones, canonicals, hreflang, robots, sitemaps, Bing, IndexNow, precios, inventario ni publicación.

## Documentos y evidencias revisadas

`VERIFICADO Y CORRECTO`

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `resultado-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-FINAL-QA-013E13D-2026-07-04.md`.
- `qa-final-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-FINAL-QA-013E13D-2026-07-04.csv`.
- `qa-collection-list-inherited-debt-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-FINAL-QA-013E13D-2026-07-04.csv`.

## Estado real Shopify comprobado

`VERIFICADO Y CORRECTO`

- Draft: `gid://shopify/OnlineStoreTheme/178396463480`.
- Nombre draft: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- Rol draft: `UNPUBLISHED`.
- Draft `sections/main-list-collections.liquid`: checksum `910b00ca49c28be5258ac2a17f1731d5`, size `20882`.
- MAIN: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre MAIN: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol MAIN: `MAIN`.
- MAIN `sections/main-list-collections.liquid`: checksum `70c8ead00d939f15528f6f11e5bfb540`, size `4934`.
- MAIN no fue modificado.

## Readiness técnico del bloque hub

`CORREGIDO Y VERIFICADO`

El bloque hub de colecciones está técnicamente listo dentro del draft:

- QA 013E13D: 10/10 combinaciones desktop/mobile en ES, EN, FR, DE y NL.
- H1 correcto y único.
- 6 enlaces rápidos.
- 3 FAQs.
- CTA de mural personalizado apunta a páginas informativas indexables.
- Canonical visible coherente.
- 8 alternates hreflang visibles.
- JSON-LD parseable; tipo detectado: `BreadcrumbList`.
- 48 `collection-card` en el listado completo.
- El bloque no genera overflow: `root_overflow_px=0` en 10/10.

## Bloqueos para publicación perfecta

`REQUIERE DECISION HUMANA`

No recomiendo publicar a MAIN todavía por dos motivos:

1. **Incidencia 012O pendiente:** el problema de caché/render de storefront sigue pendiente de ingeniería Shopify según el registro del proyecto. No consta cierre técnico posterior.
2. **Deuda heredada visible en la misma página:** el listado de colecciones mantiene textos mejorables fuera del bloque nuevo:
   - FR: `Nouveaux mortels`, `Le plus vendu`.
   - DE: `Bestverkauf`, `Versicherte Eleganz`.
   - NL: `Best verkopen`, `Nieuwe matchwalls`.
   - EN/FR/DE/NL mantienen algunos handles heredados con `matchwallsmurals`, que siguen en `STANDBY`.

## Opciones de decisión

`REQUIERE DECISION HUMANA`

### Opción A — Recomendada

Esperar cierre o recheck satisfactorio de 012O y corregir antes la deuda heredada visible de colecciones FR/DE/NL.

Estado: `REQUIERE DECISION HUMANA`.

Ventaja: alinea con el objetivo de web excelente, multilingüe y citable por buscadores/IA.  
Coste: retrasa la publicación del hub.

### Opción B — Aceptable solo con decisión humana explícita

Esperar cierre o recheck satisfactorio de 012O y publicar el hub aceptando que la deuda heredada de colecciones queda documentada para un lote posterior.

Estado: `VERIFICADO PERO MEJORABLE`.

Ventaja: acelera la salida del bloque hub ya verificado.  
Riesgo: la misma página seguirá mostrando textos de colecciones poco naturales en FR/DE/NL.

### Opción C — No recomendada

Publicar ahora sin esperar 012O.

Estado: `RIESGO CRITICO`.

Riesgo: promocionar un cambio de tema mientras existe una incidencia de render/caché pública todavía abierta.

### Opción D — No recomendada

No publicar ni corregir.

Estado: `INCOMPLETO`.

Riesgo: se pierde el beneficio SEO/GEO del hub y se mantiene deuda visible.

## Reversión si se ejecuta un lote futuro

`VERIFICADO Y CORRECTO`

Si en un lote posterior se promueve o se replica el archivo, la reversión del draft actual consiste en restaurar:

`sections/main-list-collections.liquid`

desde:

`backups-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-COPY-LINK-REFINE-013E13C-2026-07-04/sections-main-list-collections.liquid.before`

Checksum esperado de reversión del draft: `6fc0ff58489b32304e4a3d428e2b0614`.

## Evidencias generadas

`VERIFICADO Y CORRECTO`

- `admin-read-MW-COLLECTIONS-ROOT-HUB-I18N-PUBLISH-READINESS-013E13E-2026-07-04.csv`.
- `readiness-matrix-MW-COLLECTIONS-ROOT-HUB-I18N-PUBLISH-READINESS-013E13E-2026-07-04.csv`.
- `publication-options-MW-COLLECTIONS-ROOT-HUB-I18N-PUBLISH-READINESS-013E13E-2026-07-04.csv`.

## Siguiente paso recomendado

`REQUIERE DECISION HUMANA`

Para seguir trabajando sin publicar y sin riesgo, recomiendo:

`MW-COLLECTIONS-I18N-CARD-TITLES-DIAG-013E14`

Objetivo: diagnóstico de solo lectura de las 48 tarjetas de colección visibles en `/collections` y sus versiones ES/EN/FR/DE/NL, separando:

- textos visibles incorrectos;
- handles heredados en `STANDBY`;
- prioridad comercial;
- qué puede corregirse sin tocar handles;
- qué requiere decisión humana.

No debe ejecutarse ninguna corrección hasta aprobar un lote posterior de escritura.
