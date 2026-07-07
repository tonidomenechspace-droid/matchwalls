# Resultado - MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-RENDER-SOURCE-DIAG-013E16C

Fecha: 2026-07-05  
Hora de cierre: 00:56 Europe/Madrid

## Estado final

`VERIFICADO Y CORRECTO`

Lote indicado por Daniel:

`MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-RENDER-SOURCE-DIAG-013E16C`

Este lote fue diagnóstico de solo lectura. No se modificó Shopify.

No se tocaron colecciones, handles, URLs, redirecciones, tema MAIN, tema draft, Liquid, LangShop, productos, precios, inventario, robots, sitemaps, Bing, IndexNow, GA4, GTM ni Search Console.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `resultado-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-EXCLUDE-DECISION-013E16B-2026-07-05.md`
- `admin-read-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-EXCLUDE-DECISION-013E16B-2026-07-05.csv`
- `public-qa-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-EXCLUDE-DECISION-013E16B-2026-07-05.csv`
- `resultado-MW-COLLECTIONS-ROOT-HUB-I18N-PUBLISH-READINESS-013E13E-2026-07-04.md`
- `registro-cambios-ejecutados.md`

## Estado real Shopify comprobado

`VERIFICADO Y CORRECTO`

Tema MAIN:

- Theme ID: `gid://shopify/OnlineStoreTheme/178399019384`
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`
- Rol: `MAIN`
- Archivo: `sections/main-list-collections.liquid`
- Checksum: `70c8ead00d939f15528f6f11e5bfb540`
- Size: `4934`

Tema draft:

- Theme ID: `gid://shopify/OnlineStoreTheme/178396463480`
- Nombre: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`
- Rol: `UNPUBLISHED`
- Archivo: `sections/main-list-collections.liquid`
- Checksum: `910b00ca49c28be5258ac2a17f1731d5`
- Size: `20882`

Template en ambos temas:

- Archivo: `templates/list-collections.json`
- Checksum: `ed986adca1c69295e3274878ff603039`
- Configuración: `settings.collections = []`

Colección Black Friday:

- Resource ID: `gid://shopify/Collection/646234440056`
- Handle base: `papel-pintado-black-friday`
- Título base: `Papel Pintado Black Friday`
- Tipo: colección manual
- Productos: `0`
- `availablePublicationsCount`: `6`
- `resourcePublicationsCount(onlyPublished: true)`: `9`
- Metafield: `seo.hidden = 1`
- SEO/metas: mantienen referencias Black Friday 2024/2025.

## Fuente exacta del render

`VERIFICADO Y CORRECTO`

La fuente no es LangShop ni un bloque editorial fijo. La fuente es el render automático de colecciones del archivo:

`sections/main-list-collections.liquid`

El patrón confirmado en MAIN y draft es:

- `paginate collections by 48`
- `assign collections_list = section.settings.collections | default: collections`
- `for collection in collections_list`
- enlace con `collection.url`
- título visible con `collection.title`

Como `templates/list-collections.json` tiene `settings.collections = []`, Shopify usa el fallback `collections`, es decir, el listado global de colecciones disponibles/publicadas.

La colección Black Friday sigue publicada/disponible aunque tenga `seo.hidden = 1`. Ese `noindex` afecta a la indexación de la URL, pero no impide que el objeto entre en el listado global de colecciones del tema.

## Verificación pública

`VERIFICADO PERO MEJORABLE`

Se confirmó en HTML público EN:

- URL: `https://www.matchwalls.com/en/collections`
- Evidencia: enlace de tarjeta `href="/en/collections/wallpapers-black-friday"` con clase `collection-card`.
- Evidencia: título visible `Black Friday Wallpaper`.

El muestreo público posterior recibió 429 en ES y variabilidad en algunas URLs directas; por estabilidad no se forzó más tráfico. La evidencia pública EN actual es coherente con 013E16B, donde ya se habían detectado enlaces Black Friday en hubs EN/FR/NL y texto en DE.

## Diagnóstico SEO/GEO/AEO

`INCORRECTO`

Mantener Black Friday dentro de un hub/listado evergreen envía una señal contradictoria:

- La colección tiene `0` productos.
- Está marcada como `seo.hidden = 1`.
- Conserva metadatos estacionales de 2024/2025.
- Sin embargo aparece como tarjeta normal dentro del listado de colecciones.

Para Google, Bing/Copilot y sistemas IA, esto mezcla una campaña temporal obsoleta con una arquitectura evergreen que debería ser limpia, actual y citable.

## Qué NO recomiendo

`VERIFICADO Y CORRECTO`

- No borrar la colección.
- No cambiar handles.
- No cambiar URLs.
- No crear redirecciones.
- No tocar LangShop para resolver esto.
- No confiar en `seo.hidden = 1` como mecanismo de exclusión visual.
- No curar manualmente 47/48 colecciones en el template sin una justificación superior, porque sería más frágil y más costoso de mantener.

## Solución técnica recomendada para lote posterior

`REQUIERE DECISION HUMANA`

Recomiendo una exclusión quirúrgica en `sections/main-list-collections.liquid`, preferiblemente por ID estable de colección:

- ID estable objetivo: `646234440056`
- Objetivo: no renderizar esa tarjeta dentro de hubs/listados evergreen.
- No cambiar la colección.
- No cambiar handle.
- No cambiar URL.
- No crear redirección.
- No cambiar SEO/metas.
- No cambiar LangShop.

La corrección debe validarse primero en draft y, solo después, decidir si se replica/publica en MAIN.

## Siguiente lote seguro recomendado

`REQUIERE DECISION HUMANA`

`MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-DRAFT-ID-EXCLUDE-013E16D`

Alcance propuesto:

- Tema: draft `gid://shopify/OnlineStoreTheme/178396463480`.
- Archivo: `sections/main-list-collections.liquid`.
- Cambio: añadir condición de exclusión visual para la colección ID `646234440056` dentro del loop de tarjetas.
- Pruebas: preview `/collections`, `/en/collections`, `/fr/collections`, `/de/collections`, `/nl/collections`; confirmar que Black Friday no aparece y que el resto de tarjetas siguen renderizando.
- Reversión: restaurar el archivo desde el backup del draft o retirar la condición añadida.

Lote posterior, solo tras QA correcta:

`MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E`

## Evidencias

`VERIFICADO Y CORRECTO`

- `source-map-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-RENDER-SOURCE-DIAG-013E16C-2026-07-05.csv`
- `resultado-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-RENDER-SOURCE-DIAG-013E16C-2026-07-05.md`
