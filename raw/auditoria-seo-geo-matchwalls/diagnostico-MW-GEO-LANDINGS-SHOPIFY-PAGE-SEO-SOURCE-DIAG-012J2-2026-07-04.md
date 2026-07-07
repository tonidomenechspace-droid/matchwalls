# Diagnostico — MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SOURCE-DIAG-012J2

Fecha: 2026-07-04  
Tipo: diagnostico de fuente SEO nativa Shopify para paginas.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Estado global: `VERIFICADO PERO MEJORABLE`

## 1. Documentos leidos

- `diagnostico-MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I-2026-07-03.md`
- `diagnostico-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-SAVE-FAIL-DIAG-012J1B-2026-07-04.md`
- `postcheck-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-PILOT-012J1-2026-07-04.md`
- `registro-cambios-ejecutados.md`

## 2. Fuentes externas oficiales consultadas

- Shopify Help Center — Creating and editing pages: `https://help.shopify.com/en/manual/online-store/add-edit-pages`
- Shopify Help Center — Adding keywords for SEO: `https://help.shopify.com/en/manual/promoting-marketing/seo/adding-keywords`
- Shopify Admin GraphQL — Page object: `https://shopify.dev/docs/api/admin-graphql/latest/objects/Page`

## 3. Estado documentado por Shopify

Shopify Help Center confirma que en el editor nativo de paginas existe una seccion de vista previa/listado de motor de busqueda para paginas.

Campos indicados por Shopify para paginas:

- Page title.
- Meta description.
- URL handle.

Tambien indica limites/recomendaciones:

- Titulo hasta 70 caracteres; recomendado practico hasta 60 para evitar truncado.
- Meta description recomendada alrededor de 160 caracteres.

Clasificacion:

- Existencia de campos SEO nativos en la UI de Shopify Pages: `VERIFICADO Y CORRECTO` por documentacion oficial.

## 4. Estado API / GraphQL

012I ya habia verificado que para las paginas:

- `gid://shopify/Page/687276622200` — `papel-pintado-espana`.
- `gid://shopify/Page/687276654968` — `papel-pintado-francia`.

el objeto `Page` en Admin GraphQL expone:

- `title`
- `body`
- `bodySummary`
- `handle`
- `translations(locale:)`
- `metafields`

y no expone como claves traducibles:

- `seo_title`
- `meta_title`
- `meta_description`
- `description_tag`

La documentacion actual de `Page` confirma que el listado de campos del objeto Page no incluye un campo `seo` directo.

Clasificacion:

- Fuente SEO nativa via Admin GraphQL para Page: `NO ACCESIBLE`.
- Campos SEO como traducciones API de Page: `NO ACCESIBLE`.

## 5. Estado publico comprobado en MatchWalls

URLs verificadas:

- `https://www.matchwalls.com/pages/papel-pintado-espana?mwqa=012j2`
- `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne?mwqa=012j2`

Archivo:

- `qa-publico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SOURCE-DIAG-012J2-2026-07-04.csv`

Resultado ES:

- HTTP 200.
- Title publico: `Papel pintado en España para hogares y proyectos profesionales`.
- Longitud title: 62.
- Meta description publica: 320 caracteres, autogenerada desde el inicio del body.
- H1 coincide con el title publico.
- Canonical propio.

Resultado FR:

- HTTP 200.
- Title publico: `Papier peint en Espagne pour intérieurs résidentiels et projets profes`.
- Longitud title: 70.
- Meta description publica: 320 caracteres, autogenerada desde el inicio del body.
- H1 correcto.
- Canonical propio.

Interpretacion:

- La pagina ES parece usar como title publico el titulo/H1 de la pagina, no un SEO title manual diferenciado.
- La meta description ES parece autogenerada desde el contenido visible.
- La pagina FR sigue usando fallback automatico, no los campos SEO que se intentaron introducir en LangShop.

Clasificacion:

- HTML publico base ES: `VERIFICADO PERO MEJORABLE`.
- HTML publico FR: `VERIFICADO PERO MEJORABLE`.

## 6. Diagnostico

Hecho verificado:

- Shopify nativo dispone de UI para editar search engine listing en paginas.
- Shopify Admin GraphQL Page no ofrece un campo SEO directo accesible en este diagnostico.
- El HTML publico de MatchWalls se comporta como fallback automatico de title/body.

Inferencia tecnica:

- Es probable que la pagina base ES no tenga SEO title/meta description manuales configurados en Shopify nativo, o que no sean accesibles por la via API usada.
- Esta ausencia de fuente SEO manual podria explicar que LangShop muestre una UI SEO traducida pero no consiga persistir los campos traducidos.

Limite de evidencia:

- No se ha abierto el editor nativo Shopify Pages de `papel-pintado-espana` en este lote.
- Por tanto, el valor exacto de los campos nativos `Page title` y `Meta description` en Admin UI queda `NO ACCESIBLE`.

## 7. Decision operativa

No escribir en Shopify nativo todavia.

No intentar de nuevo LangShop SEO meta.

Siguiente paso seguro:

`MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-MANUAL-CHECK-012J2A`

Objetivo:

- Abrir Shopify Admin nativo > Online Store > Pages > `papel-pintado-espana`.
- Abrir Search engine listing preview / Edit website SEO.
- Leer sin modificar:
  - Page title.
  - Meta description.
  - URL handle.
- Confirmar si estan vacios, autogenerados o poblados manualmente.
- No guardar.

## 8. Criterio para avanzar

Si los campos nativos estan vacios:

- Estado: `VERIFICADO PERO MEJORABLE`.
- Se podria proponer un piloto ES base separado, con aprobacion exacta, sabiendo que afectaria al HTML publico ES.

Si estan poblados:

- Copiar valores exactos.
- Investigar por que no coinciden con HTML publico/API.

Si no aparecen:

- Estado: `NO ACCESIBLE`.
- Abandonar via metas manuales de paginas por ahora.

## 9. Riesgos

- Editar la fuente ES afectaria la pagina publica ES.
- Si Shopify usa el campo fuente como fallback multidioma, podria afectar previews o traducciones.
- Cambiar URL handle crearia riesgo critico de redirecciones/canonicals; no debe tocarse.
- Guardar accidentalmente cambios en pagina nativa podria modificar contenido ya verificado en 012F/012H.

## 10. Conclusion

012J2 confirma que:

- La via LangShop SEO meta no debe escalarse.
- La existencia de campos SEO nativos en Shopify esta documentada oficialmente.
- La fuente exacta de MatchWalls en el editor nativo queda pendiente de comprobacion manual de solo lectura.
- El siguiente paso debe ser una comprobacion manual nativa, no una escritura.

