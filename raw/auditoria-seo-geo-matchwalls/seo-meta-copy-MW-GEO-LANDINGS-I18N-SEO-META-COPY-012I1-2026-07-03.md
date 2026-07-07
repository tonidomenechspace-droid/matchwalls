# Copy SEO meta — MW-GEO-LANDINGS-I18N-SEO-META-COPY-012I1

Fecha: 2026-07-03 19:14 +02:00  
Tipo: preparacion de copy SEO meta i18n para paginas pais Espana/Francia.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Estado del lote documental: `VERIFICADO Y CORRECTO`  
Estado de ejecucion en Shopify/LangShop: `INCOMPLETO`

## 1. Documentos leidos

- `diagnostico-MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I-2026-07-03.md`
- `qa-publico-meta-MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I-2026-07-03.csv`
- `ejecucion-MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H-2026-07-03.md`
- `copy-map-final-MW-GEO-LANDINGS-I18N-LINGUISTIC-QA-012G2-2026-07-03.md`
- `registro-cambios-ejecutados.md`

## 2. Estado real usado como base

Segun el diagnostico cerrado 012I:

- El HTML publico de las 10 URLs ES/FR/EN/DE/NL de Espana y Francia esta en el idioma correcto.
- No se detecto meta title/meta description en espanol en URLs no ES.
- Shopify Admin GraphQL no expone para estas paginas campos `seo_title`, `meta_title`, `meta_description` ni `description_tag`.
- `TranslatableResource` expone solo `title`, `body_html` y `handle`.
- Las paginas no tienen metafields SEO detectables.
- La mejora pendiente no es una correccion critica, sino una optimizacion de snippet si LangShop muestra un campo SEO editable real.

Nota de control 012I1:

- Una descarga directa adicional de las URLs publicas en 012I1 no se usa como fuente de verdad para valores actuales porque devolvio una respuesta no representativa de la pagina final. Por rigor, los valores actuales exactos deberan tomarse de LangShop o de una verificacion publica fiable justo antes de ejecutar 012J.

## 3. Alcance

Paginas:

- Espana: `gid://shopify/Page/687276622200`, handle base `papel-pintado-espana`.
- Francia: `gid://shopify/Page/687276654968`, handle base `papel-pintado-francia`.

Idiomas prioritarios:

- ES
- FR
- EN
- DE
- NL

Campos propuestos, solo si LangShop los muestra como editables y publicables:

- SEO title / meta title.
- SEO meta description / search listing description.

## 4. Fuera de alcance

No se modifica ni se propone modificar en este lote:

- `title`.
- `body_html`.
- handles / slugs.
- URLs.
- canonicals.
- hreflang.
- redirecciones.
- tema Shopify / Liquid.
- schema.
- productos, colecciones, inventario, precios o imagenes.

## 5. Reglas editoriales aplicadas

- Mantener el pais al inicio del enfoque semantico: Espana / Francia.
- Mantener MatchWalls como marca al final del SEO title.
- No usar claims logisticos no verificados.
- No prometer ranking, indexacion, plazos, stock ni fabricacion local.
- Meta descriptions breves, claras y entendibles por buscadores e IA.
- Coherencia con el contenido ya aprobado en 012H.
- No traducir ni alterar handles.

## 6. Copy propuesto

| Pais | Idioma | SEO title propuesto | Long. | Meta description propuesta | Long. |
|---|---:|---|---:|---|---:|
| Espana | ES | Papel pintado en España \| MatchWalls | 36 | Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural. | 134 |
| Espana | FR | Papier peint en Espagne \| MatchWalls | 36 | Papiers peints, panoramiques et solutions sur mesure en Espagne pour intérieurs résidentiels et projets professionnels. Commandez des échantillons. | 147 |
| Espana | EN | Wallpaper in Spain \| MatchWalls | 31 | Wallpaper, wall murals and made-to-measure solutions in Spain for homes, retail spaces and professional projects. Order samples online. | 135 |
| Espana | DE | Tapeten in Spanien \| MatchWalls | 31 | Tapeten, Wandbilder und maßgefertigte Lösungen in Spanien für Wohnräume, Ladengeschäfte und gewerbliche Projekte. Muster bestellen. | 131 |
| Espana | NL | Behang in Spanje \| MatchWalls | 29 | Behang, wanddecoratie en maatwerkoplossingen in Spanje voor woningen, winkels en professionele projecten. Bestel monsters online. | 129 |
| Francia | ES | Papel pintado en Francia \| MatchWalls | 37 | Papel pintado, murales y soluciones a medida para viviendas, hoteles, tiendas y proyectos profesionales en Francia. Solicita muestras. | 134 |
| Francia | FR | Papier peint en France \| MatchWalls | 35 | Papiers peints, panoramiques et solutions sur mesure en France pour particuliers, hôtels, boutiques et projets professionnels. | 126 |
| Francia | EN | Wallpaper in France \| MatchWalls | 32 | Wallpaper, wall murals and made-to-measure solutions in France for homes, hotels, retail spaces and professional interiors. Order samples. | 138 |
| Francia | DE | Tapeten in Frankreich \| MatchWalls | 34 | Tapeten, Wandbilder und maßgefertigte Lösungen in Frankreich für Wohnräume, Hotels, Ladengeschäfte und gewerbliche Projekte. | 124 |
| Francia | NL | Behang in Frankrijk \| MatchWalls | 32 | Behang, wanddecoratie en maatwerkoplossingen in Frankrijk voor woningen, hotels, winkels en professionele projecten. | 116 |

Archivo matriz:

- `matriz-MW-GEO-LANDINGS-I18N-SEO-META-COPY-012I1-2026-07-03.csv`

## 7. Criterio de ejecucion posterior

No ejecutar escritura todavia.

Antes de 012J debe confirmarse en LangShop / Shopify Translate:

1. Que existe un campo SEO title/meta title editable para estas paginas e idiomas.
2. Que existe un campo SEO meta description/search listing description editable.
3. Que guardar ese campo no sobrescribe `title`, `body_html` ni `handle`.
4. Que el campo publicado modifica el HTML publico real, no solo una preview interna.

Si cualquiera de esos puntos no se puede verificar, el estado debe ser:

`REQUIERE DECISION HUMANA`

## 8. Riesgos

- LangShop puede mostrar una preview interna que no se publica en el HTML real.
- Un campo SEO no confirmado podria sobrescribir contenido ya corregido en 012H.
- Si no hay respaldo de valores actuales exactos antes de 012J, la reversion no seria quirurgica.
- Titles/metas demasiado comerciales o genericos podrian reducir claridad semantica.

## 9. Reversion prevista para 012J

Este lote no requiere reversion porque no modifica Shopify.

Si se ejecuta 012J, antes de escribir debera guardarse:

- valor actual exacto del SEO title/meta title por pagina e idioma;
- valor actual exacto del SEO meta description por pagina e idioma;
- captura o exportacion del campo en LangShop si esta disponible;
- URL publica verificada antes y despues.

La reversion de 012J consistira en restaurar exactamente esos valores previos.

## 10. Siguiente lote seguro

Siguiente lote recomendado:

`MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-FIELD-CHECK-012I2`

Objetivo:

- Verificar en LangShop, sin escribir, si los campos SEO meta existen y son editables para paginas.
- Identificar la ruta exacta de UI y los campos disponibles.

Solo despues, si existe campo real y Daniel aprueba escritura:

`MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-UPDATE-012J`

