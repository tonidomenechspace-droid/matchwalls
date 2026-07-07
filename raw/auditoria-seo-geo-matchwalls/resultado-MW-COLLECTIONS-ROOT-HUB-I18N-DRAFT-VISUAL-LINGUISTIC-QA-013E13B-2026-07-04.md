# Resultado lote MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B

Fecha: 2026-07-04  
Hora de cierre documental: 21:22 Europe/Madrid  
Estado final: `VERIFICADO PERO MEJORABLE`

## Aprobación

Daniel aprobó exactamente:

`APROBADO LOTE MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B`

## Alcance ejecutado

`VERIFICADO Y CORRECTO`

QA de solo lectura sobre el prototipo del hub raíz de colecciones creado en 013E13A:

- Tema draft: `gid://shopify/OnlineStoreTheme/178396463480`.
- Rol comprobado: `UNPUBLISHED`.
- Archivo evaluado: `sections/main-list-collections.liquid`.
- MAIN comprobado y no modificado: `gid://shopify/OnlineStoreTheme/178399019384`.
- Idiomas evaluados: ES, EN, FR, DE y NL.
- Viewports evaluados:
  - Desktop: `1440x1000`.
  - Mobile: `390x844`.

No se modificó Shopify, LangShop, MAIN, temas, páginas, productos, colecciones, URLs, handles, canonicals, hreflang, redirecciones, robots, sitemaps, Bing, IndexNow, metadatos, precios ni inventario.

## Estado real comprobado en Shopify Admin

`VERIFICADO Y CORRECTO`

### Draft

- Theme ID: `gid://shopify/OnlineStoreTheme/178396463480`.
- Nombre: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- Rol: `UNPUBLISHED`.
- Processing: `false`.
- Processing failed: `false`.
- File: `sections/main-list-collections.liquid`.
- Checksum: `6fc0ff58489b32304e4a3d428e2b0614`.
- Size: `20885`.
- UpdatedAt: `2026-07-04T18:54:27Z`.

### MAIN

- Theme ID: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol: `MAIN`.
- Processing: `false`.
- Processing failed: `false`.
- File: `sections/main-list-collections.liquid`.
- Checksum: `70c8ead00d939f15528f6f11e5bfb540`.
- Size: `4934`.
- UpdatedAt del archivo: `2026-06-18T18:30:51Z`.

Conclusión: el prototipo sigue solo en draft. MAIN público no contiene este cambio.

## QA visual y funcional del bloque

`CORREGIDO Y VERIFICADO`

En los 10 casos evaluados, 5 idiomas por 2 viewports:

- Bloque `.mw-collections-root` presente.
- Bloque visible.
- `h1Count=1`.
- 6 enlaces rápidos.
- 3 FAQs.
- 48 tarjetas de colecciones renderizadas después del bloque.
- Sin `translation missing`.

Capturas guardadas:

- `evidencias/MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04/013E13B-ES-desktop.png`.
- `evidencias/MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04/013E13B-EN-desktop.png`.
- `evidencias/MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04/013E13B-FR-desktop.png`.
- `evidencias/MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04/013E13B-DE-desktop.png`.
- `evidencias/MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04/013E13B-NL-desktop.png`.
- `evidencias/MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04/013E13B-ES-mobile.png`.
- `evidencias/MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04/013E13B-EN-mobile.png`.
- `evidencias/MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04/013E13B-FR-mobile.png`.
- `evidencias/MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04/013E13B-DE-mobile.png`.
- `evidencias/MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04/013E13B-NL-mobile.png`.

Limitación visual:

- Las capturas móviles muestran banner de cookies y barra de preview de Shopify. Esto no altera el HTML del bloque, pero limita la lectura visual completa en primera pantalla.

## Overflow móvil

`VERIFICADO PERO MEJORABLE`

- Desktop ES/EN/FR/DE/NL: sin overflow horizontal.
- Mobile ES/EN/DE: sin overflow horizontal de página.
- Mobile FR/NL: se detecta overflow horizontal de página.
- Medición específica del bloque nuevo:
  - `.mw-collections-root`: sin overflow.
  - `.mw-collections-root__intro`: sin overflow.
  - `.mw-collections-root__quick-links`: sin overflow.
  - `.mw-collections-root__faq`: sin overflow.

Conclusión: el overflow observado en FR/NL móvil procede de elementos heredados del header/barra de anuncios, no del bloque nuevo. No bloquea el prototipo, pero debe quedar como deuda visual global antes de publicación final si se exige cero overflow.

## QA de enlaces internos

`VERIFICADO PERO MEJORABLE`

Se verificaron 30 destinos mediante navegación real de navegador:

- 30/30 destinos navegables sin plantilla 404 visible.
- 25/30 destinos: `VERIFICADO Y CORRECTO`.
- 5/30 destinos: `VERIFICADO PERO MEJORABLE` porque funcionan pero contienen `noindex`.

Los 5 destinos `noindex` son el producto de mural personalizado y equivalentes por idioma:

- `/products/custom-file-uploader`.
- `/en/products/custom-file-uploader`.
- `/fr/products/telechargeur-de-fichiers-personnalise`.
- `/de/products/benutzerdefinierte-datei-uploader`.
- `/nl/products/aangepaste-bestandsbelaster`.

Interpretación:

- Como ruta funcional de usuario, el enlace es correcto.
- Como señal SEO/GEO, es mejorable porque apunta a una URL no indexable.
- Recomendación: decidir en lote separado si se mantiene por conversión o si se crea/enlaza una página informativa indexable sobre mural personalizado.

## QA lingüístico

`VERIFICADO PERO MEJORABLE`

- ES: `VERIFICADO Y CORRECTO`.
- EN: `VERIFICADO Y CORRECTO`.
- FR: `VERIFICADO Y CORRECTO` en contenido principal; el enlace `Voir tous les designs` es `VERIFICADO PERO MEJORABLE` por anglicismo.
- DE: `VERIFICADO PERO MEJORABLE`; copy correcto y entendible, pero conviene QA humano antes de MAIN.
- NL: `VERIFICADO PERO MEJORABLE`; copy correcto y entendible, pero conviene QA humano antes de MAIN.

Hallazgo externo al bloque:

- Las páginas destino del formulario profesional tienen H1 heredados poco naturales en FR/DE/NL:
  - FR: `Forme professionnelle`.
  - DE: `Professionelle Form`.
  - NL: `Professionele vorm`.
- No pertenecen al cambio del hub, pero quedan detectadas como deuda i18n.

## Estado de promoción a MAIN

`REQUIERE DECISION HUMANA`

No se recomienda promocionar todavía a MAIN sin decidir antes:

1. Si refinamos FR/DE/NL en el propio bloque.
2. Si mantenemos el enlace al producto noindex de mural personalizado o lo sustituimos por una página informativa indexable.
3. Si corregimos o abrimos lote separado para H1 del formulario profesional en FR/DE/NL.
4. Si aceptamos el overflow heredado FR/NL móvil o lo corregimos antes.

## Evidencias

`VERIFICADO Y CORRECTO`

- `qa-visual-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04.csv`.
- `qa-links-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04.csv`.
- `qa-linguistica-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04.csv`.
- `admin-read-MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04.csv`.
- `evidencias/MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04/visual-browser-results-013E13B.json`.
- `evidencias/MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-VISUAL-LINGUISTIC-QA-013E13B-2026-07-04/link-navigation-results-013E13B.json`.

## Siguiente lote seguro

`REQUIERE DECISION HUMANA`

Lote recomendado:

`MW-COLLECTIONS-ROOT-HUB-I18N-DRAFT-COPY-LINK-REFINE-013E13C`

Alcance propuesto:

- Solo tema draft `178396463480`.
- Refinar copy FR/DE/NL del bloque.
- Decidir y ajustar, si procede, el enlace “Crear mural personalizado” hacia una ruta indexable informativa o mantener el producto noindex por conversión.
- No tocar MAIN.
- No publicar.

No está autorizado hasta aprobación exacta.
