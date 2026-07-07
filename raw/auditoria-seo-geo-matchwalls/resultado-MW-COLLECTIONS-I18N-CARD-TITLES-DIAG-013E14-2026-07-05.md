# Resultado MW-COLLECTIONS-I18N-CARD-TITLES-DIAG-013E14

Fecha: 2026-07-05  
Estado final: `VERIFICADO PERO MEJORABLE`

## Alcance aprobado

Daniel aprobó exactamente: `APROBADO LOTE MW-COLLECTIONS-I18N-CARD-TITLES-DIAG-013E14`.

Diagnóstico de solo lectura de las 48 tarjetas de colección visibles en `/collections` y variantes ES/EN/FR/DE/NL.

No se ejecutaron escrituras en Shopify. No se tocó MAIN, LangShop, páginas, productos, colecciones, handles, URLs, redirecciones, canonicals, hreflang, robots, sitemaps, Bing, IndexNow, precios, inventario ni publicación.

## Documentos y evidencias revisadas

`VERIFICADO Y CORRECTO`

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `resultado-MW-COLLECTIONS-ROOT-HUB-I18N-PUBLISH-READINESS-013E13E-2026-07-04.md`.
- `qa-collection-list-inherited-debt-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-FINAL-QA-013E13D-2026-07-04.csv`.
- Evidencias de 011D/011D1 sobre Black Friday noindex/obsolescencia.
- Evidencias de 013E10/013E8 sobre `/en/collections` y cita en Bing/Copilot.

## Estado real Shopify comprobado

`VERIFICADO Y CORRECTO`

- Draft: `gid://shopify/OnlineStoreTheme/178396463480`.
- Nombre draft: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- Rol draft: `UNPUBLISHED`.
- Draft `sections/main-list-collections.liquid`: checksum `910b00ca49c28be5258ac2a17f1731d5`, size `20882`, updatedAt `2026-07-04T21:29:00Z`.
- MAIN: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre MAIN: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol MAIN: `MAIN`.
- MAIN `sections/main-list-collections.liquid`: checksum `70c8ead00d939f15528f6f11e5bfb540`, size `4934`.
- MAIN no fue modificado.

## Cobertura de extracción visible

`VERIFICADO Y CORRECTO`

- ES: 48 tarjetas visibles en `https://www.matchwalls.com/collections`.
- EN: 48 tarjetas visibles en `https://www.matchwalls.com/en/collections`.
- FR: 48 tarjetas visibles en `https://www.matchwalls.com/fr/collections`.
- DE: 48 tarjetas visibles en `https://www.matchwalls.com/de/collections`.
- NL: 48 tarjetas visibles en `https://www.matchwalls.com/nl/collections`.

Total auditado: 240 tarjetas visibles.

## Diferencia frente a deuda histórica 013E13D

`VERIFICADO Y CORRECTO`

En la extracción actual 013E14 no aparecen las cadenas históricas siguientes:

- `Nouveaux mortels`: no presente.
- `Le plus vendu`: no presente.
- `Bestverkauf`: no presente.
- `Versicherte Eleganz`: no presente.
- `Best verkopen`: no presente.
- `Nieuwe matchwalls`: no presente.

Esto no autoriza publicación automática: solo confirma que esos textos concretos no se reprodujeron en el listado actual de 48 tarjetas por idioma.

## Incidencias visibles detectadas

### Black Friday visible en hub/listado evergreen

`REQUIERE DECISION HUMANA`

Se detecta `Black Friday` visible en los cinco idiomas prioritarios:

- ES: `Papel Pintado Black Friday` -> `/collections/papel-pintado-black-friday`.
- EN: `Black Friday Wallpaper` -> `/en/collections/wallpapers-black-friday`.
- FR: `Papier Peint Black Friday` -> `/fr/collections/papiers-peints-black-friday`.
- DE: `Tapete Black Friday` -> `/de/collections/schwarzer-freitag-wallpaper`.
- NL: `Behang Black Friday` -> `/nl/collections/black-friday-wallpaper`.

Motivo: 011D/011D1 ya trató Black Friday como campaña obsoleta/noindex. Mantenerla visible dentro de un hub evergreen de colecciones crea una señal inconsistente para usuarios, buscadores y sistemas IA. No se debe retirar ni cambiar sin lote específico porque puede afectar navegación interna y campaña futura.

### Topónimo traducido incorrectamente

`INCORRECTO`

- EN: `Basin Wallpaper` -> `/en/collections/basin-wallpaper`.

Motivo: corresponde a Cuenca; traducir el topónimo como `Basin` es lingüística y semánticamente incorrecto. La evidencia histórica 011C/013E8 ya lo había señalado, y ahora queda confirmado como visible dentro del listado.

### Mejoras lingüísticas menores

`VERIFICADO PERO MEJORABLE`

- FR: `Papier Peint Alava`, `Papier Peint Almeria`, `Papier Peint Avila`, `Papier Peint Jaen`: revisar coherencia de acentos/nombres propios frente a criterio de marca y SEO local.
- DE: `Tapete 3D`, `Tapete Gold`, `Tapete Japanisch`: títulos entendibles pero mejorables en naturalidad alemana.
- NL: `Behang 3D`, `Geometrische Behangstijlen`: entendibles pero mejorables en naturalidad neerlandesa.

## Handles heredados

`STANDBY`

Se detectan 64 tarjetas con handles heredados que contienen patrones como `matchwallsmurals`, `matchwallsmurs`, `matchwallswallpapers`, `matchwallswalpapers` o `matchalls`.

Además, se detectan 65 casos en FR/DE/NL con handles que conservan fragmentos ingleses como `wallpaper`.

No se recomienda cambiar handles en este lote. Según protocolo, cualquier cambio de handle requiere mapa 301, evaluación de hreflang/canonical, rastreo, QA y aprobación específica.

## Clasificación final

- Cobertura de 48 tarjetas por idioma: `VERIFICADO Y CORRECTO`.
- Ausencia de cadenas históricas más graves de 013E13D: `VERIFICADO Y CORRECTO`.
- `Basin Wallpaper`: `INCORRECTO`.
- Black Friday visible en hub/listado evergreen: `REQUIERE DECISION HUMANA`.
- Mejoras lingüísticas FR/DE/NL: `VERIFICADO PERO MEJORABLE`.
- Handles heredados: `STANDBY`.

Estado global del lote: `VERIFICADO PERO MEJORABLE`.

## Evidencias generadas

`VERIFICADO Y CORRECTO`

- `admin-read-MW-COLLECTIONS-I18N-CARD-TITLES-DIAG-013E14-2026-07-05.csv`.
- `qa-summary-MW-COLLECTIONS-I18N-CARD-TITLES-DIAG-013E14-2026-07-05.csv`.
- `qa-visible-cards-MW-COLLECTIONS-I18N-CARD-TITLES-DIAG-013E14-2026-07-05.csv`.
- `qa-visible-issues-MW-COLLECTIONS-I18N-CARD-TITLES-DIAG-013E14-2026-07-05.csv`.
- `qa-standby-handles-MW-COLLECTIONS-I18N-CARD-TITLES-DIAG-013E14-2026-07-05.csv`.

## Recomendación

`REQUIERE DECISION HUMANA`

No publicar el hub a MAIN como “perfecto” hasta decidir, como mínimo:

1. Qué hacer con Black Friday visible en el hub/listado evergreen.
2. Corregir `Basin Wallpaper` como texto visible, sin tocar handle salvo lote posterior.
3. Preparar copy map FR/DE/NL para mejoras lingüísticas menores.
4. Mantener handles heredados en `STANDBY` hasta mapa 301 aprobado.
5. Mantener vigilancia de la incidencia 012O de render/caché hasta cierre de ingeniería Shopify o recheck estable.

Siguiente lote seguro recomendado, sin escritura:

`MW-COLLECTIONS-I18N-CARD-TITLES-COPY-MAP-013E15`

Objetivo: preparar el mapa exacto de cambios propuestos para títulos visibles y política de Black Friday, sin tocar handles ni Shopify.
