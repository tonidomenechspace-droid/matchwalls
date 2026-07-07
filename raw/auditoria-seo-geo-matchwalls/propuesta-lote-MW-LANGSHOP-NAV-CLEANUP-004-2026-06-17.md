# Propuesta lote MW-LANGSHOP-NAV-CLEANUP-004 - 2026-06-17

Estado: PROPUESTA - NO APROBADO

Modo actual: solo lectura.

No se ha modificado Shopify, LangShop, temas, menus, traducciones, productos, colecciones, paginas, URLs, handles, redirecciones, precios, inventario, imagenes, variantes ni App Embeds.

## Objetivo

Auditar y, solo si Daniel lo aprueba expresamente, limpiar residuos internos de navegacion en LangShop que ya no forman parte del footer publicado de Shopify.

El objetivo no es traducir de forma masiva ni actualizar estadisticas globales. El objetivo es confirmar si LangShop conserva recursos huerfanos o antiguos que puedan reinyectarse o confundir futuras revisiones del footer.

## Documentos leidos

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `ejecucion-lote-MW-FOOTER-NAV-GLOBAL-002-2026-06-17.md`.
- `ejecucion-lote-MW-FOOTER-I18N-TRANSLATIONS-003-2026-06-17.md`.
- `auditoria-langshop-dependency-2026-06-16.md`.
- Evidencia manual aportada por Daniel mediante capturas de LangShop y storefront publico.

## Estado real comprobado por Shopify Admin

Consulta de solo lectura ejecutada el 2026-06-17.

Tienda:

- `Matchwalls`.
- Dominio primario: `https://www.matchwalls.com`.
- MyShopify: `matchwalls.myshopify.com`.
- SSL activo.

Tema MAIN:

- `SEO schema hotfix - 2026-06-15`.
- ID: `gid://shopify/OnlineStoreTheme/178383749496`.
- Rol: `MAIN`.
- `processing:false`.
- `processingFailed:false`.

Idiomas publicados:

- `es` primario.
- `en`, `fr`, `de`, `nl`, `it`, `pt-PT` publicados.

Menus footer publicados en Shopify:

- `footer`: `gid://shopify/Menu/210266325219`.
- `footer-profesional`: `gid://shopify/Menu/210972311779`.
- `footer-brand`: `gid://shopify/Menu/210972344547`.
- `footer-legal`: `gid://shopify/Menu/210972410083`.

Estado verificado en Shopify Admin:

- `footer` no contiene `Envios internacionales`.
- `footer` no contiene `Black Friday 2024`.
- `footer-brand` no contiene `Tarjeta regalo`.
- `footer-profesional` contiene `espacios publicos`, no `espacios pubicos`.
- `footer` contiene `FAQ - Envios y devoluciones`, no `FAQ'S`.

LangShop:

- `appByHandle(handle:"langshop")` devuelve app publica `LangShop`.
- `installation:null`.
- Por tanto, la instalacion/configuracion interna de LangShop sigue `NO ACCESIBLE` desde Shopify Admin GraphQL.

## Evidencia manual LangShop aportada por Daniel

Capturas revisadas en LangShop > Traducciones > Navegacion:

EN:

- Busqueda `FAQ`: `FAQ - Envios y devoluciones` -> `FAQ - Shipping and returns`.
- Busqueda `Gift`: aparece `Tarjeta regalo` -> `Gift card`.
- Busqueda `Friday`: sin resultados.
- Busqueda `International`: sin resultados.
- Busqueda `B2B`: aparece al menos un recurso antiguo `B2B Interiorismo` -> `B2B Interiorism`.

FR:

- Busqueda `Gift`: sin resultados.
- Busqueda `tarjeta regalo`: aparece `Tarjeta regalo` -> `Carte-cadeau`.

DE:

- Busqueda `tarjeta`: aparece `Tarjeta regalo` -> `Geschenkkarte`.

NL:

- Busqueda `tarjeta regalo`: aparece `Tarjeta regalo` -> `Cadeaubon`.

Storefront publico verificado por capturas de Daniel:

- EN footer: no aparece `Gift card`, `Black Friday` ni `International shipping`.
- FR footer: no aparece `Carte-cadeau`, Black Friday ni envios internacionales.
- DE footer: no aparece `Geschenkkarte`, Black Friday ni envios internacionales.
- NL footer: no aparece `Cadeaubon`, Black Friday ni envios internacionales.

## Diagnostico

El footer publico prioritario EN/FR/DE/NL esta limpio para los enlaces eliminados.

LangShop conserva registros internos de navegacion que ya no forman parte de los menus publicados de Shopify. El caso mas claro es:

- `Tarjeta regalo` en EN/FR/DE/NL.

Tambien hay indicios de recursos antiguos o duplicados:

- `B2B Interiorismo` -> `B2B Interiorism`.
- Mezcla de versiones antiguas y nuevas de etiquetas B2B.

Estado:

- Footer publico EN/FR/DE/NL: `CORREGIDO Y VERIFICADO` por capturas humanas.
- Menus Shopify Admin: `CORREGIDO Y VERIFICADO`.
- Traducciones nativas Shopify Admin: `CORREGIDO Y VERIFICADO`.
- LangShop Navigation interno: `INCORRECTO`.
- Configuracion interna LangShop desde conector: `NO ACCESIBLE`.

## Alcance propuesto del lote

Fase 1 - Solo lectura:

1. Revisar en LangShop > Traducciones > Navegacion los idiomas EN, FR, DE y NL.
2. Buscar terminos residuales:
   - `Tarjeta regalo`
   - `Gift`
   - `Carte-cadeau`
   - `Geschenkkarte`
   - `Cadeaubon`
   - `Black`
   - `Friday`
   - `Envios internacionales`
   - `International`
   - `B2B Interiorismo`
   - `B2B Hotels`
   - `B2B Interiorism`
3. Documentar resultado por idioma y recurso.
4. No pulsar `Traducir`, `Actualizar`, `Actualizar todas las estadisticas`, `Mas acciones`, flechas de traduccion ni campos editables.

Fase 2 - Solo si se aprueba escritura:

No se propone todavia una escritura concreta porque LangShop no ha mostrado en las capturas una opcion segura de eliminar solo recursos huerfanos.

Antes de cualquier limpieza real habria que identificar:

- Si cada recurso pertenece a un menu activo, menu antiguo, menu de otra ubicacion o recurso huerfano.
- Si LangShop permite eliminar el recurso sin afectar Shopify.
- Si la eliminacion afecta solo a la capa LangShop o tambien al menu de Shopify.
- Si hay backup/export disponible.

## Acciones prohibidas dentro de este lote salvo aprobacion adicional

- No ejecutar traduccion automatica.
- No pulsar `Traducir`.
- No pulsar `Actualizar` en recursos o estadisticas.
- No usar `Actualizar todas las estadisticas`.
- No usar acciones masivas.
- No cambiar idiomas publicados.
- No cambiar configuracion de LangShop.
- No activar traduccion automatica.
- No crear clave API.
- No modificar menus Shopify.
- No modificar traducciones nativas Shopify.
- No modificar tema MAIN ni App Embed.

## Riesgos

- LangShop puede tratar recursos antiguos como historico, no como elementos visibles.
- Una limpieza manual sin identificador tecnico podria borrar una traduccion aun usada en otro menu.
- Pulsar `Actualizar` podria resincronizar desde Shopify o marcar recursos como desactualizados.
- Pulsar `Traducir` podria sobrescribir traducciones humanas ya corregidas.
- Las acciones masivas de LangShop podrian afectar EN/FR/DE/NL y tambien IT/PT-PT.

## Metodo de reversion

No hay metodo de reversion operativo hasta tener export o respaldo interno de LangShop.

Para cualquier accion futura sobre LangShop se requiere previamente:

1. Capturas completas del recurso antes del cambio.
2. Export de traducciones si LangShop lo permite.
3. Confirmacion de que el cambio no modifica Shopify Admin.
4. QA publico posterior en EN/FR/DE/NL.

## Pruebas posteriores si se llegara a ejecutar una limpieza aprobada

- Revisar LangShop Navigation EN/FR/DE/NL con las mismas busquedas.
- Verificar Shopify Admin menus por lectura.
- Verificar traducciones nativas de los recursos `MENU` y `LINK`.
- Verificar storefront publico EN/FR/DE/NL en incognito.
- Comprobar que no reaparecen `Gift card`, `Carte-cadeau`, `Geschenkkarte`, `Cadeaubon`, Black Friday ni envios internacionales.

## Decision requerida

Esta propuesta no autoriza cambios.

Para continuar con solo lectura basta con que Daniel envie nuevas capturas siguiendo las busquedas indicadas.

Para cualquier escritura real en LangShop o Shopify sera necesaria aprobacion exacta:

`APROBADO LOTE MW-LANGSHOP-NAV-CLEANUP-004`

