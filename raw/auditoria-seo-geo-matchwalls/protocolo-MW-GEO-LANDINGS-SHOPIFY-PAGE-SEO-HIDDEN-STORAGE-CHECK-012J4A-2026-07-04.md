# Protocolo - MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-HIDDEN-STORAGE-CHECK-012J4A

Fecha: 2026-07-04  
Tipo: diagnostico de solo lectura para localizar almacenamiento oculto de metadescripcion SEO.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Cambios Shopify Translate: no.  
Estado: `INCOMPLETO`

## 1. Documentos leidos

- `diagnostico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-I18N-META-SAFE-PATH-DIAG-012J4-2026-07-04.md`
- `incidencia-post-rollback-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-BASE-PILOT-012J3-2026-07-04.md`
- `registro-cambios-ejecutados.md`

## 2. Estado publico revalidado

Archivo:

- `qa-publico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-HIDDEN-STORAGE-CHECK-012J4A-2026-07-04.csv`

Resultado:

- ES: `meta`, `og:description` y `twitter:description` siguen mostrando el valor 012J3. `INCORRECTO`
- DE: `meta`, `og:description` y `twitter:description` siguen mostrando el valor 012J3 en espanol. `INCORRECTO`
- FR: limpio, autogenerado en frances. `VERIFICADO PERO MEJORABLE`
- EN: limpio, autogenerado en ingles. `VERIFICADO PERO MEJORABLE`
- NL: limpio, autogenerado en neerlandes. `VERIFICADO PERO MEJORABLE`

Valor persistente:

`Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural.`

## 3. Objetivo del protocolo manual

Localizar si el valor persistente esta guardado en LangShop para la traduccion alemana de la pagina Espana.

Recurso:

- Shopify Page historico: `gid://shopify/Page/687276622200`
- Pagina: `papel-pintado-espana`
- Idioma afectado prioritario: `DE`
- Ruta LangShop probable: `admin.shopify.com/store/matchwalls/apps/langshop/translations/pages/687276622200/de`

## 4. Prohibido durante 012J4A

No modificar:

- SEO title.
- Meta description.
- URL / handle.
- Title.
- Body.
- Metacampos.
- Traduccion automatica.

No pulsar:

- `Guardar`.
- traduccion automatica / iconos de IA.
- botones de sincronizacion global.

Si aparece `Cambios no guardados`, no guardar; informar.

## 5. Paso manual 1 - LangShop Espana DE

Abrir:

`https://admin.shopify.com/store/matchwalls/apps/langshop/translations/pages/687276622200/de`

En la pagina:

1. Scroll hasta `Vista previa del listado del motor de busqueda`.
2. Revisar solo los campos SEO visibles.
3. No escribir.
4. No guardar.

Respuesta esperada:

```text
CHECK 012J4A LANGSHOP ESPAÑA DE
SEO title DE: "[valor exacto o VACIO]"
Meta description DE: "[valor exacto o VACIO]"
Contiene texto español 012J3: "sí/no"
Banner cambios no guardados: "sí/no"
URL tocada: no
Guardado: no
```

## 6. Criterio de salida parcial

Si `Meta description DE` contiene el valor 012J3:

- almacenamiento probable localizado en LangShop DE;
- preparar propuesta de limpieza quirurgica en lote separado.

Si esta vacio:

- ampliar lectura a LangShop ES y/o Shopify Translate;
- no escribir.

Si no aparecen campos:

- clasificar LangShop DE como `NO ACCESIBLE`;
- valorar soporte LangShop/Shopify o lectura API segura.

## 7. Estado actual

Paso manual 1 ejecutado por captura de Daniel.

Resultado LangShop Espana DE:

- URL: `admin.shopify.com/store/matchwalls/apps/langshop/translations/pages/687276622200/de`
- Campos SEO visibles: si.
- `SEO title DE`: `VACIO` en campo editable visible.
- `Meta description DE`: `VACIO` en campo editable visible.
- Preview superior: muestra texto en espanol/fallback, incluido contenido base.
- Banner `Cambios no guardados`: no visible en captura.
- URL tocada: no.
- Guardado: no.

Clasificacion:

- Campos SEO DE visibles y vacios: `VERIFICADO Y CORRECTO`.
- Preview LangShop DE en espanol: `VERIFICADO PERO MEJORABLE`.
- Almacenamiento oculto del valor 012J3: `NO ACCESIBLE` en esta pantalla.

Evidencia:

- `evidencias/captura-012J4A-langshop-espana-de-seo-fields-vacios-2026-07-04.png`

## 8. Siguiente comprobacion manual segura

Abrir LangShop Espana ES:

`https://admin.shopify.com/store/matchwalls/apps/langshop/translations/pages/687276622200/es`

Revisar solo los campos SEO visibles de la seccion `Vista previa del listado del motor de busqueda`.

No escribir. No guardar.

Respuesta esperada:

```text
CHECK 012J4A LANGSHOP ESPAÑA ES
SEO title ES: "[valor exacto o VACIO]"
Meta description ES: "[valor exacto o VACIO]"
Contiene texto español 012J3: "sí/no"
Banner cambios no guardados: "sí/no"
URL tocada: no
Guardado: no
```

## 9. Resultado LangShop Espana ES

Paso manual ejecutado por captura de Daniel.

Resultado:

- URL: `admin.shopify.com/store/matchwalls/apps/langshop/translations/pages/687276622200/es`
- Campos SEO visibles: si.
- `SEO title ES`: `VACIO` en campo editable visible.
- `Meta description ES`: `VACIO` en campo editable visible.
- Preview superior: muestra espanol/fallback.
- Banner `Cambios no guardados`: no visible en captura.
- URL tocada: no.
- Guardado: no.

Evidencia:

- `evidencias/captura-012J4A-langshop-espana-es-seo-fields-vacios-2026-07-04.png`

Clasificacion:

- Campos SEO ES visibles y vacios: `VERIFICADO Y CORRECTO`.
- Preview LangShop ES en espanol/fallback: `VERIFICADO PERO MEJORABLE`.
- Almacenamiento oculto del valor 012J3: `NO ACCESIBLE` en esta pantalla.

## 10. Recheck publico posterior

Archivo:

- `qa-publico-recheck-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-HIDDEN-STORAGE-CHECK-012J4A-2026-07-04.csv`

Resultado:

- ES: sigue mostrando valor 012J3.
- DE: sigue mostrando valor 012J3 en ese recheck.
- NL: tambien mostro valor 012J3 en ese recheck.

Archivo con control `Accept-Language`:

- `qa-publico-accept-language-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-HIDDEN-STORAGE-CHECK-012J4A-2026-07-04.csv`

Resultado:

- DE sin cabecera y con `de-DE`: meta autogenerada en aleman. `VERIFICADO PERO MEJORABLE`.
- NL sin cabecera: muestra valor 012J3. `INCORRECTO`.
- NL con `nl-NL`: meta autogenerada en neerlandes. `VERIFICADO PERO MEJORABLE`.
- FR/EN con cabecera local: metas autogeneradas correctas.

Interpretacion:

- El problema no esta localizado en los campos SEO visibles de LangShop ES/DE.
- Existe comportamiento variable por contexto/cabecera/propagacion.
- Para crawlers sin `Accept-Language`, el riesgo sigue abierto especialmente en NL y en ES.

## 11. Evidencia de tema local

Busqueda local en tema:

- `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E/layout/theme.liquid`
- `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E/snippets/social-meta-tags.liquid`

Hallazgo:

- `meta name="description"` usa `page_description`.
- `og:description` usa `page_description`.
- `twitter:description` usa `page_description` como fallback.

Clasificacion:

`VERIFICADO Y CORRECTO` que el valor observado en HTML procede de `page_description` entregado al tema, no de body visible.

## 12. Cierre del protocolo 012J4A

Estado:

`VERIFICADO PERO MEJORABLE`

No se localizo el almacenamiento oculto en campos visibles de LangShop ES/DE.

Siguiente paso seguro:

`MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-DESCRIPTION-TAG-STORAGE-DIAG-012J4B`

Objetivo:

- inspeccionar especificamente `global.description_tag` / traducciones del recurso pagina si existe acceso API seguro o exportacion de traducciones;
- no escribir;
- decidir limpieza solo con valor exacto localizado.
