# Resultado MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-COPY-LINK-REFINE-013E13C

Fecha: 2026-07-04  
Estado final: `CORREGIDO Y VERIFICADO`

## Alcance aprobado

`APROBADO LOTE MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-COPY-LINK-REFINE-013E13C`

- Tema afectado: draft `gid://shopify/OnlineStoreTheme/178396463480`.
- Archivo afectado: `sections/main-list-collections.liquid`.
- Idiomas dentro del alcance: ES, EN, FR, DE y NL.
- MAIN verificado y no modificado: `gid://shopify/OnlineStoreTheme/178399019384`.
- Sin cambios en LangShop, páginas, productos, colecciones, handles, URLs, redirecciones, canonicals, hreflang, robots, sitemaps, Bing, IndexNow, precios, inventario ni tema publicado.

## Cambios ejecutados

`CORREGIDO Y VERIFICADO`

- Se sustituyó el enlace del CTA de mural personalizado desde URLs de producto noindex hacia páginas informativas indexables verificadas:
  - ES: `/pages/crea-tu-mural`.
  - EN: `/en/pages/create-your-own-mural`.
  - FR: `/fr/pages/creez-votre-propre-murale`.
  - DE: `/de/pages/erstellen-sie-ihr-eigenes-wandbild`.
  - NL: `/nl/pages/maak-je-eigen-muurschildering`.
- Se refinó copy visible en FR, DE y NL:
  - FR: mayor naturalidad comercial y `Voir toutes les collections`.
  - DE: tono formal homogéneo y `Alle Kollektionen ansehen` / `Wand ausmessen`.
  - NL: `Behang- en wandprintcollecties`, `Alle collecties bekijken` y `Wandprint op maat maken`.

## Evidencia técnica

`VERIFICADO Y CORRECTO`

- Respaldo creado antes de escribir:
  `auditoria-seo-geo-matchwalls/backups-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-COPY-LINK-REFINE-013E13C-2026-07-04/sections-main-list-collections.liquid.before`.
- Checksum antes en draft: `6fc0ff58489b32304e4a3d428e2b0614`.
- Checksum después en draft: `910b00ca49c28be5258ac2a17f1731d5`.
- MAIN permanece con checksum: `70c8ead00d939f15528f6f11e5bfb540`.
- Validación Liquid: pasada antes de subir.
- `themeFilesUpsert`: `0 userErrors`.

## QA público en preview autenticado

`CORREGIDO Y VERIFICADO`

- 5/5 idiomas con bloque `.mw-collections-root` renderizado.
- 5/5 H1 correctos.
- 5/5 idiomas con 6 enlaces rápidos.
- 5/5 CTAs de mural personalizado apuntan a páginas informativas indexables.
- 0 tokens inválidos dentro del bloque: sin `translation missing`, sin claves Liquid visibles y sin URLs antiguas de producto custom uploader.

Detalle guardado en:

- `admin-post-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-COPY-LINK-REFINE-013E13C-2026-07-04.csv`.
- `qa-publico-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-COPY-LINK-REFINE-013E13C-2026-07-04.csv`.

## Incidencias y límites

`VERIFICADO PERO MEJORABLE`

- La validación por `curl` público no se usa como evidencia de fallo porque no mantiene el contexto de preview Shopify y puede devolver el tema live.
- Persisten deudas externas fuera del alcance de este lote:
  - H1 heredados mejorables en páginas destino de cuenta profesional FR/DE/NL.
  - Incidencia 012O de render/caché storefront pendiente de respuesta de ingeniería Shopify.

## Reversión

`VERIFICADO Y CORRECTO`

Restaurar en el draft `178396463480` el archivo:

`sections/main-list-collections.liquid`

desde:

`auditoria-seo-geo-matchwalls/backups-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-COPY-LINK-REFINE-013E13C-2026-07-04/sections-main-list-collections.liquid.before`

Resultado esperado de reversión: checksum `6fc0ff58489b32304e4a3d428e2b0614`. MAIN no requiere reversión porque no fue modificado.

## Siguiente lote recomendado

`REQUIERE DECISION HUMANA`

`MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-FINAL-QA-013E13D`

Objetivo: QA final de lectura sobre el draft completo antes de decidir cualquier promoción a MAIN: desktop/mobile, enlaces, H1, schema, canonicals, hreflang visible, ausencia de overflow nuevo y comprobación de que la incidencia Shopify 012O no contamina la evaluación.
