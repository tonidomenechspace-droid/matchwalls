# Resultado lote MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-CONTENT-PROTOTYPE-013E13A

Fecha: 2026-07-04  
Hora de cierre documental: 21:00 Europe/Madrid  
Estado final: `CORREGIDO Y VERIFICADO`

## Aprobación

Daniel aprobó exactamente:

`APROBADO LOTE MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-CONTENT-PROTOTYPE-013E13A`

## Documentos y referencias leídas

`VERIFICADO Y CORRECTO`

- `registro-cambios-ejecutados.md`.
- `copy-architecture-MW-COLLECTIONS-ROOT-HUB-I18N-COPY-ARCHITECTURE-013E13-2026-07-04.md`.
- `copy-map-MW-COLLECTIONS-ROOT-HUB-I18N-COPY-ARCHITECTURE-013E13-2026-07-04.csv`.
- `diagnostico-MW-COLLECTIONS-ROOT-HUB-I18N-SOURCE-FEASIBILITY-DIAG-013E12-2026-07-04.md`.
- Backup previo creado para este lote:
  `backups-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-CONTENT-PROTOTYPE-013E13A-2026-07-04/sections-main-list-collections.liquid.before`.

## Alcance ejecutado

`CORREGIDO Y VERIFICADO`

Se prototipó contenido editorial visible para los hubs raíz de colecciones en el tema borrador, sin publicar:

- Tema destino: `gid://shopify/OnlineStoreTheme/178396463480`.
- Nombre: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- Rol comprobado: `UNPUBLISHED`.
- Archivo modificado: `sections/main-list-collections.liquid`.
- Tema MAIN real conservado sin cambios:
  `gid://shopify/OnlineStoreTheme/178399019384`.

No se modificó:

- MAIN publicado.
- LangShop.
- Páginas, productos, colecciones o blogs.
- Handles, URLs, canonicals, hreflang o redirecciones.
- Metadatos SEO.
- Robots.txt, sitemaps, Bing Webmaster Tools o IndexNow.
- Precios, inventario, variantes, imágenes o datos comerciales.

## Valores originales y nuevos

`VERIFICADO Y CORRECTO`

### Original

- Archivo original respaldado: `sections/main-list-collections.liquid`.
- MD5 original: `70C8EAD00D939F15528F6F11E5BFB540`.

### Nuevo en tema borrador

- Archivo preparado localmente:
  `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E/sections/main-list-collections.liquid`.
- MD5 nuevo: `6fc0ff58489b32304e4a3d428e2b0614`.
- Tamaño: `20885` bytes.
- MD5 leído desde Shopify tras la escritura: `6fc0ff58489b32304e4a3d428e2b0614`.

## Contenido prototipado

`VERIFICADO PERO MEJORABLE`

El prototipo añade, antes del grid de colecciones:

- Un bloque editorial `.mw-collections-root`.
- Un único H1 por idioma.
- Introducción breve.
- Texto guía orientado a intención de compra.
- 6 enlaces internos prioritarios por idioma.
- FAQ visible con 3 preguntas.
- Traducciones locales dentro del schema de la sección para ES, EN, FR, DE y NL.

H1 renderizados en preview:

| Idioma | H1 |
|---|---|
| ES | `Colecciones de papel pintado y murales` |
| EN | `Wallpaper and mural collections` |
| FR | `Collections de papiers peints et panoramiques` |
| DE | `Kollektionen für Tapeten und Wandbilder` |
| NL | `Collecties behang en wandprints` |

Nota: DE y NL quedan `VERIFICADO PERO MEJORABLE` hasta QA lingüístico humano antes de cualquier promoción a MAIN.

## Validaciones técnicas

`VERIFICADO Y CORRECTO`

- Validación local Shopify Liquid sobre `sections/main-list-collections.liquid`: correcta.
- Validación de mutación GraphQL `themeFilesUpsert`: correcta.
- Primer intento directo por contenido codificado: rechazado por Shopify con `El contenido incluye caracteres no válidos`; no produjo cambios.
- Vía segura ejecutada:
  1. `stagedUploadsCreate`.
  2. Upload temporal privado con respuesta HTTP `201`.
  3. `themeFilesUpsert` usando URL temporal.
  4. Job Shopify: `gid://shopify/Job/1184f9e6-af36-4ad4-9e57-cb28d6c382a1`.
  5. Job finalizado: `done=true`.
- Resultado `themeFilesUpsert`: sin `userErrors`.

## Post-check Shopify Admin

`CORREGIDO Y VERIFICADO`

- Theme ID leído: `gid://shopify/OnlineStoreTheme/178396463480`.
- Rol leído: `UNPUBLISHED`.
- Theme updatedAt: `2026-07-04T18:54:27Z`.
- File key: `sections/main-list-collections.liquid`.
- File updatedAt: `2026-07-04T18:54:27Z`.
- Checksum Shopify: `6fc0ff58489b32304e4a3d428e2b0614`.
- Size Shopify: `20885`.

## QA público preview y live

`CORREGIDO Y VERIFICADO`

Preview con `?preview_theme_id=178396463480`:

- 5/5 idiomas responden `200`.
- 5/5 idiomas renderizan el bloque `.mw-collections-root`.
- 5/5 idiomas tienen `h1Count=1`.
- 5/5 idiomas tienen `hasMissingTranslation=false`.
- 5/5 idiomas tienen 3 FAQs.
- 5/5 idiomas tienen 6 enlaces rápidos.

Live sin preview:

- 5/5 idiomas responden `200`.
- 5/5 idiomas mantienen `hasRoot=false`.
- 5/5 idiomas mantienen `h1Count=1`.
- Esto confirma que MAIN público no fue alterado por este lote.

## Riesgos detectados

`VERIFICADO PERO MEJORABLE`

- DE y NL requieren revisión lingüística humana antes de publicación.
- El lote 012O mantiene una incidencia externa de render/caché en storefront para páginas geográficas; este lote se verificó en preview y no modifica el storefront publicado.
- El prototipo no añade schema JSON-LD; eso queda fuera del alcance de 013E13A.
- Los enlaces internos existen como rutas propuestas y deben revisarse visualmente y por destino real en el siguiente lote antes de MAIN.

## Reversión

`VERIFICADO Y CORRECTO`

Reversión mínima:

1. En el tema no publicado `gid://shopify/OnlineStoreTheme/178396463480`, restaurar:
   `sections/main-list-collections.liquid`.
2. Usar el backup:
   `backups-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-CONTENT-PROTOTYPE-013E13A-2026-07-04/sections-main-list-collections.liquid.before`.
3. Confirmar MD5 restaurado:
   `70C8EAD00D939F15528F6F11E5BFB540`.

No hay reversión necesaria en MAIN porque MAIN no fue modificado.

## Archivos de evidencia

`VERIFICADO Y CORRECTO`

- `admin-post-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-CONTENT-PROTOTYPE-013E13A-2026-07-04.csv`.
- `qa-publico-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-CONTENT-PROTOTYPE-013E13A-2026-07-04.csv`.
- `resultado-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-CONTENT-PROTOTYPE-013E13A-2026-07-04.md`.

## Siguiente lote seguro

`REQUIERE DECISION HUMANA`

Lote recomendado:

`MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B`

Objetivo:

- QA visual desktop/mobile en preview.
- Revisión de legibilidad ES/EN/FR/DE/NL.
- Verificación de destinos reales de los 6 enlaces por idioma.
- Comprobación de ausencia de regresiones en grid/listado de colecciones.

No queda autorizado publicar, promocionar a MAIN ni tocar LangShop sin nuevo `APROBADO LOTE [...]`.
