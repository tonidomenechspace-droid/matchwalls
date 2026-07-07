# Diagnostico - MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-I18N-META-SAFE-PATH-DIAG-012J4

Fecha: 2026-07-04  
Tipo: diagnostico de solo lectura sobre metadescripciones SEO multidioma en paginas Shopify.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Cambios Shopify Translate: no.  
Estado global: `INCORRECTO`

## 1. Documentos leidos

- `incidencia-post-rollback-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-BASE-PILOT-012J3-2026-07-04.md`
- `diagnostico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SOURCE-DIAG-012J2-2026-07-04.md`
- `diagnostico-MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I-2026-07-03.md`
- `diagnostico-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-SAVE-FAIL-DIAG-012J1B-2026-07-04.md`
- `postcheck-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-PILOT-012J1-2026-07-04.md`
- `admin-read-MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I-2026-07-03.csv`
- `registro-cambios-ejecutados.md`

## 2. Fuentes oficiales / externas consultadas

- Shopify Dev Docs, `Optimize storefront SEO`: los metadatos SEO personalizados de un recurso se almacenan como metafields `global.title_tag` y `global.description_tag`.
- Shopify Help Center, `Localization and translation`: cuando no existen traducciones, la tienda muestra contenido del idioma principal; si los campos SEO se personalizan, se pueden traducir con Translate & Adapt o una app compatible.
- Shopify Help Center, `Adding keywords for SEO`: para paginas, Shopify permite editar `Page title`, `Meta description` y URL handle en el listado de motores de busqueda.
- LangShop Community: indica como orientacion externa que las meta tags deben existir manualmente en Shopify antes de traducirse en LangShop. No se usa como fuente oficial de verdad, solo como pista tecnica.

## 3. Estado real previo verificado

Antes de 012J3:

- `012I`: las metas publicas de ES/FR/EN/DE/NL estaban en idioma correcto y parecian autogeneradas desde el body traducido.
- `012J2A`: Shopify nativo de `papel-pintado-espana` mostraba:
  - `Titulo de la pagina`: `Papel pintado en España para hogares y proyectos profesionales`
  - `Metadescripcion`: `VACIO`
  - `Identificador de URL`: `pages/papel-pintado-espana`
- `012J1B`: LangShop mostraba campos SEO meta, pero el guardado no persistia y no se reflejaba en HTML publico.

## 4. Incidencia provocada por el piloto 012J3

Valor insertado temporalmente en la metadescripcion nativa ES:

`Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural.`

Resultado post-guardado:

- ES: publica correctamente el valor.
- DE/NL: heredaban el valor ES.
- FR: no contaminada.
- EN: inicialmente no concluyente por 503.

Decision 012J3:

- Rollback recomendado.

## 5. Estado post-rollback verificado por UI

Daniel envio captura posterior en Shopify nativo:

- Campo `Metadescripcion`: vacio.
- Contador: `0 de 160 caracteres usados`.
- `Titulo de la pagina`: intacto.
- `Identificador de URL`: intacto.
- Boton `Guardar`: gris/inactivo.

Clasificacion UI nativa:

`VERIFICADO Y CORRECTO`

Evidencia:

- `evidencias/captura-012J3-postrollback-shopify-nativo-meta-vacia-2026-07-04.png`

## 6. QA publico 012J4

Archivo:

- `qa-publico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-I18N-META-SAFE-PATH-DIAG-012J4-2026-07-04.csv`

Resultado por idioma para la landing Espana:

| Idioma | Estado HTML publico | Resultado |
|---|---|---|
| ES | `meta`, `og:description` y `twitter:description` siguen mostrando el valor 012J3 | `INCORRECTO` respecto al rollback |
| FR | meta/og/twitter en frances autogenerado | `VERIFICADO PERO MEJORABLE` |
| EN | meta/og/twitter en ingles autogenerado | `VERIFICADO PERO MEJORABLE` |
| DE | `meta`, `og:description` y `twitter:description` siguen mostrando el valor 012J3 en espanol | `INCORRECTO` |
| NL | meta/og/twitter en neerlandes autogenerado | `VERIFICADO PERO MEJORABLE` |

Todas las URLs verificadas:

- HTTP 200.
- canonical propio correcto.
- H1 correcto en su idioma.
- 8 hreflang detectados.
- sin `noindex`.
- `CF-Cache-Status`: `DYNAMIC`.

## 7. Diagnostico

Hechos verificados:

- Shopify nativo muestra la metadescripcion base ES vacia.
- El HTML publico ES y DE sigue usando el valor de 012J3 en `meta`, `og` y `twitter`.
- FR/EN/NL no muestran ese valor y mantienen metas autogeneradas por idioma.
- No hay evidencia de que title, body o URL hayan cambiado.

Inferencias tecnicas:

- El valor 012J3 no esta procediendo del campo visible nativo tal como lo muestra la UI actual.
- El valor puede haber quedado en una capa no visible desde esa pantalla:
  - metafield SEO `global.description_tag`;
  - traduccion de `description_tag` para DE;
  - cache interna de Shopify/app;
  - almacenamiento propio de LangShop/Shopify Translate;
  - otra capa de render consumida por el tema.

Limite de evidencia:

- No hay acceso API seguro documentado en este lote para leer directamente `global.description_tag` y sus traducciones.
- No se puede afirmar la causa exacta.

## 8. Decision operativa

No ejecutar mas escrituras en SEO meta hasta localizar el almacenamiento real.

No repetir:

- rellenar meta ES nativa sola;
- guardar en LangShop SEO meta sin confirmar persistencia;
- tocar handles;
- tocar title/body;
- modificar tema Liquid para forzar metas.

## 9. Via segura recomendada

Siguiente lote de solo lectura:

`MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-HIDDEN-STORAGE-CHECK-012J4A`

Objetivo:

- Verificar donde esta almacenado el valor 012J3 que todavia aparece en ES/DE.

Comprobaciones recomendadas:

1. Recheck publico ES/DE/NL con cache-buster pasados unos minutos.
2. Inspeccion manual de solo lectura en LangShop:
   - pagina Espana `DE`: comprobar si los campos SEO meta contienen el texto en espanol;
   - pagina Espana `ES`: comprobar si LangShop/Translate muestra un campo SEO meta persistido;
   - no guardar.
3. Si se dispone de acceso seguro API, leer exclusivamente:
   - metafields `global.title_tag` y `global.description_tag` de `gid://shopify/Page/687276622200`;
   - traducciones/metafields equivalentes por locale, especialmente `de`.

Si en 012J4A se localiza el valor:

- preparar lote de limpieza quirurgica separado, con valor actual exacto y rollback.

Si no se localiza:

- mantener automatic metas y abrir decision humana para soporte LangShop/Shopify.

## 10. Regla para futuras metas manuales

No se debe completar la meta ES de una pagina multidioma como cambio aislado.

Si se decide optimizar snippets manuales, debe hacerse mediante una via que permita:

- fuente ES;
- traducciones FR/EN/DE/NL;
- guardado persistente;
- QA publico en los cinco idiomas;
- rollback exacto.

Hasta demostrar esa via, el estado mas seguro es:

- dejar metas automaticas/localizadas desde body;
- priorizar contenido visible, H1, body, enlaces internos y arquitectura GEO.

## 11. Estado final

`MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-I18N-META-SAFE-PATH-DIAG-012J4` queda como:

- Diagnostico publico: `INCORRECTO` por persistencia de meta 012J3 en ES/DE.
- Shopify nativo UI: `VERIFICADO Y CORRECTO` porque el campo visible esta vacio.
- Causa exacta: `NO ACCESIBLE`.
- Siguiente paso seguro: `MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-HIDDEN-STORAGE-CHECK-012J4A`.

