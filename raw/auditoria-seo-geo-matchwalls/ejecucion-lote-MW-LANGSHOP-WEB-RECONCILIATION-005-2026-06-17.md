# Ejecucion lote MW-LANGSHOP-WEB-RECONCILIATION-005

Fecha: 2026-06-17  
Lote aprobado por Daniel: `APROBADO LOTE MW-LANGSHOP-WEB-RECONCILIATION-005`  
Modo de trabajo: auditoria y reconciliacion de solo lectura.  
Estado final del lote: `CORREGIDO Y VERIFICADO` para footer publico ES/EN/FR/DE/NL; `VERIFICADO PERO MEJORABLE` para memoria/navegacion legacy en Shopify y LangShop.

## Limites del lote

No se modifico Shopify, LangShop, temas, menus, traducciones, handles, URLs, redirecciones, productos, colecciones, inventario ni configuracion de apps.

Este lote no autoriza importaciones CSV, traducciones automaticas, borrados de traducciones, cambios de tema ni mutaciones GraphQL. Cualquier limpieza real de menus o LangShop requiere un nuevo lote de escritura con aprobacion exacta.

## Documentos y archivos leidos

- `AGENTS.md`.
- `auditoria-seo-geo-matchwalls/registro-cambios-ejecutados.md`.
- `auditoria-seo-geo-matchwalls/programa-ejecucion-seo-geo.md`.
- `auditoria-seo-geo-matchwalls/lista-maestra-errores-cambios-evoluciones-mejoras.md`.
- `auditoria-seo-geo-matchwalls/auditoria-langshop-dependency-2026-06-16.md`.
- `auditoria-seo-geo-matchwalls/propuesta-lote-MW-LANGSHOP-NAV-CLEANUP-004-2026-06-17.md`.
- `auditoria-seo-geo-matchwalls/langshop-export-navigation-raw-2026-06-17/README-NO-REIMPORTAR.md`.
- Exportaciones LangShop de navegacion:
  - `navigation_export_es_en.csv`.
  - `navigation_export_es_fr.csv`.
  - `navigation_export_es_de.csv`.
  - `navigation_export_es_nl.csv`.

Tambien se detecto una carpeta duplicada fuera de la ruta canonica:

- `auditoria-seo-geo-matchwallslangshop-export-navigation-raw-2026-06-17`.

Estado: `VERIFICADO PERO MEJORABLE`. No debe usarse como fuente operativa mientras exista la carpeta canonica dentro de `auditoria-seo-geo-matchwalls`.

## Shopify Admin comprobado

Consulta de solo lectura mediante Shopify Admin GraphQL.

### Tienda y publicacion

- Tienda: `Matchwalls`.
- Dominio myshopify: `matchwalls.myshopify.com`.
- Dominio principal: `https://www.matchwalls.com`.
- SSL: activo.
- Tema MAIN real: `SEO schema hotfix - 2026-06-15`.
- Tema MAIN ID: `gid://shopify/OnlineStoreTheme/178383749496`.
- Tema MAIN: `processing:false`, `processingFailed:false`.

Estado: `VERIFICADO Y CORRECTO`.

### Idiomas

Idiomas publicados comprobados:

- ES: publicado y primario.
- EN: publicado.
- FR: publicado.
- DE: publicado.
- NL: publicado.
- IT: publicado, fuera de alcance prioritario.
- PT-PT: publicado, fuera de alcance prioritario.

Estado para ES/EN/FR/DE/NL: `VERIFICADO Y CORRECTO`.

### LangShop

- App por handle `langshop`: localizada como `LangShop`.
- `installation` no devuelve informacion util desde esta conexion.
- App Embed LangShop SDK en MAIN: activo (`disabled:false`).
- Configuracion interna LangShop, reglas, glosario, colas, import/export interno y auto-sync: no accesibles por Shopify Admin GraphQL.

Estado App Embed: `VERIFICADO Y CORRECTO`.  
Estado configuracion interna LangShop: `NO ACCESIBLE`.

## Menus activos de footer

Menus que el footer publico actual esta usando:

- `gid://shopify/Menu/210266325219`, handle `footer`, titulo `AYUDA Y SOPORTE`.
- `gid://shopify/Menu/210972311779`, handle `footer-profesional`, titulo `PROFESIONALES`.
- `gid://shopify/Menu/210972344547`, handle `footer-brand`, titulo `EMPRESA`.
- `gid://shopify/Menu/210972410083`, handle `footer-legal`, titulo `LEGAL`.

En estos menus activos no aparecen:

- `Tarjeta regalo`.
- `Black Friday`.
- `Envios internacionales`.
- `Envíos internacionales`.

Estado: `CORREGIDO Y VERIFICADO`.

## Menu legacy detectado

Existe un menu Shopify actual, no visible en el footer publico verificado, que conserva elementos antiguos:

- Menu: `gid://shopify/Menu/210969952483`.
- Handle: `footer-matchwalls`.
- Titulo: `Footer matchwalls`.

Elementos legacy relevantes dentro de ese menu:

- `gid://shopify/MenuItem/493550239971` - `B2B Interiorismo`.
- `gid://shopify/MenuItem/493550371043` - `Tarjeta regalo`.
- `gid://shopify/MenuItem/493550534883` - `Envíos y devoluciones`.
- Otros grupos antiguos: `PROFESIONAL`, `BRAND`, `AYUDA`, `LEGAL`.

Los IDs `493550239971` y `493550371043` siguen existiendo tambien como recursos traducibles en Shopify:

- `B2B Interiorismo` -> EN `B2B Interiorism`, `outdated:false`.
- `Tarjeta regalo` -> EN `Gift card`, `outdated:false`.

Interpretacion verificada: LangShop exporta o muestra navegacion legacy porque esos recursos siguen existiendo en Shopify. Eso no significa que esten visibles en el footer publico actual.

Estado del menu `footer-matchwalls`: `VERIFICADO PERO MEJORABLE`.  
Estado del residuo `Tarjeta regalo` en ese menu legacy: `INCORRECTO` si el menu se considera parte del inventario operativo; `NO visible en footer publico verificado`.

## Web publica comprobada

Comprobacion visual/DOM del footer publico:

- `https://www.matchwalls.com/` ES.
- `https://www.matchwalls.com/en/` EN.
- `https://www.matchwalls.com/fr/` FR.
- `https://www.matchwalls.com/de/` DE.
- `https://www.matchwalls.com/nl/` NL.

Resultado footer publico:

- ES: sin `Tarjeta regalo`, sin `Black Friday`, sin `Envios internacionales`.
- EN: sin `Gift card`, sin `Black Friday`, sin `International shipping`.
- FR: sin `Carte-cadeau`, sin `Black Friday`, sin envio internacional como enlace footer.
- DE: sin `Geschenkkarte`, sin `Black Friday`, sin envio internacional como enlace footer.
- NL: sin `Cadeaubon`, sin `Black Friday`, sin envio internacional como enlace footer.

Estado footer publico ES/EN/FR/DE/NL: `CORREGIDO Y VERIFICADO`.

## Exportaciones LangShop comprobadas

Ruta canonica:

`auditoria-seo-geo-matchwalls/langshop-export-navigation-raw-2026-06-17`

Archivos:

- `navigation_export_es_en.csv`: 189 filas.
- `navigation_export_es_fr.csv`: 189 filas.
- `navigation_export_es_de.csv`: 189 filas.
- `navigation_export_es_nl.csv`: 189 filas.

Hallazgos:

- Las cuatro exportaciones contienen `navigation[493550371043][title]` con fuente `Tarjeta regalo`.
- Las cuatro exportaciones contienen `navigation[493550239971][title]` con fuente `B2B Interiorismo`.
- No se detecto `Black Friday` en estas exportaciones.
- No se detecto `Envios internacionales`, `Envíos internacionales` ni `International shipping` en estas exportaciones.

Estado de las exportaciones raw: `VERIFICADO PERO MEJORABLE`.

Diagnostico: son utiles como respaldo y evidencia, pero mezclan navegacion actual y legacy. No son aptas para reimportacion directa.

## Elementos fuera de footer detectados

Aunque el footer publico esta limpio, se detectaron textos fuera del footer:

- Barra/claim superior ES con referencia a envio internacional gratuito.
- Configuracion de Shopify Inbox en el tema con texto de saludo que incluye `Envío internacional gratuito en pedidos de muestras`.

Estos elementos no pertenecen al footer y no fueron modificados en este lote.

Estado: `VERIFICADO PERO MEJORABLE`.  
Accion recomendada: tratar en lote separado si Daniel quiere eliminar o ajustar cualquier mencion de envio internacional fuera del footer.

## Riesgos

- `RIESGO CRITICO`: reimportar los CSV raw de LangShop podria reactivar o consolidar recursos legacy como `Tarjeta regalo`.
- `RIESGO CRITICO`: usar `Borrar traducciones`, `Traducir` o `Actualizar` en LangShop sin filtrar podria tocar recursos no visibles, recursos historicos y textos ya optimizados en Shopify.
- `VERIFICADO PERO MEJORABLE`: el menu `footer-matchwalls` conserva estructura antigua y puede seguir apareciendo en LangShop aunque no se vea en el footer publico.
- `NO ACCESIBLE`: configuracion interna de LangShop no se puede auditar por Shopify Admin GraphQL.

## No ejecutado

- No se importaron CSV.
- No se exporto desde LangShop desde Codex.
- No se pulsaron acciones de LangShop.
- No se ejecutaron mutaciones GraphQL.
- No se modifico ningun menu.
- No se elimino ningun recurso.
- No se cambio tema MAIN.
- No se tocaron traducciones almacenadas.

## Conclusion

La web publica y los menus activos del footer estan corregidos y verificados en ES/EN/FR/DE/NL.

La causa de que LangShop siga mostrando `Tarjeta regalo` no es una recaida visible del footer, sino la existencia de un menu legacy Shopify llamado `footer-matchwalls` que LangShop sigue considerando dentro de navegacion traducible.

Siguiente paso recomendado: preparar un lote especifico `MW-LANGSHOP-LEGACY-MENU-CLEANUP-006` para verificar referencias del tema a `footer-matchwalls`, respaldar el menu legacy y, solo si no esta en uso, limpiar o retirar sus elementos obsoletos mediante una operacion pequena y reversible.
