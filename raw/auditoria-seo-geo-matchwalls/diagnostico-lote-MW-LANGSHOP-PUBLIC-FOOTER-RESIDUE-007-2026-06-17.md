# Diagnostico lote MW-LANGSHOP-PUBLIC-FOOTER-RESIDUE-007

**Fecha y hora:** 2026-06-17 20:57 +02:00.  
**Tipo de trabajo:** auditoria y diagnostico de solo lectura.  
**Estado global:** `CORREGIDO Y VERIFICADO`.  
**Motivo:** addendum de 2026-06-17 21:44 +02:00 confirma que el HTML actual servido por HTTP directo sin cache y el DOM renderizado del navegador estan limpios en ES, EN, FR, DE y NL. La evidencia externa previa con residuos queda reclasificada como stale/caché no reproducida en la web actual.

## Documentos leidos

- `AGENTS.md`.
- `auditoria-seo-geo-matchwalls/registro-cambios-ejecutados.md`.
- `auditoria-seo-geo-matchwalls/ejecucion-lote-MW-LANGSHOP-LEGACY-MENU-CLEANUP-006-2026-06-17.md` via registro y estado previo.
- Skill local Shopify Admin para validar el flujo de consultas GraphQL.

## Acciones realizadas

- Consultas Shopify Admin GraphQL de solo lectura.
- Validacion previa de las consultas GraphQL contra esquema Shopify.
- Lectura de todos los menus Shopify accesibles.
- Lectura de archivos criticos del tema MAIN:
  - `config/settings_data.json`.
  - `sections/header-group.json`.
  - `sections/footer-group.json`.
  - `sections/footer.liquid`.
- Lectura de recursos traducibles `MENU` para `en`, `fr`, `de` y `nl`.
- Lectura HTML publica externa de `https://www.matchwalls.com/en`.
- Lectura HTML publica externa de `https://www.matchwalls.com/`.
- Intento de peticion local sin cache desde PowerShell/curl: `NO ACCESIBLE` por error de conexion/proxy/TLS local.

## Estado real comprobado

### Shopify Admin - menus

`VERIFICADO Y CORRECTO` para menus activos del footer:

- `footer` / `AYUDA Y SOPORTE`.
- `footer-profesional` / `PROFESIONALES`.
- `footer-brand` / `EMPRESA`.
- `footer-legal` / `LEGAL`.

No contienen:

- `Tarjeta regalo`.
- `Gift Card`.
- `Black Friday 2024`.
- `Envios internacionales`.
- `International shipments`.

`CORREGIDO Y VERIFICADO` para menu legacy:

- `gid://shopify/Menu/210969952483`.
- Handle `footer-matchwalls`.
- Titulo `ZZ LEGACY - NO USAR - footer-matchwalls`.
- Items `[]`.

### Shopify Admin - tema MAIN

`VERIFICADO Y CORRECTO`:

- Tema MAIN real: `gid://shopify/OnlineStoreTheme/178383749496`.
- Nombre: `SEO schema hotfix - 2026-06-15`.
- `sections/footer-group.json` referencia solo:
  - `footer-profesional`.
  - `footer-brand`.
  - `footer`.
  - `footer-legal`.
- `sections/footer-group.json` no referencia `footer-matchwalls`.
- `sections/footer.liquid` renderiza `block.settings.menu.links`; no contiene enlaces hardcodeados a `Gift Card`, `Black Friday 2024` o `International shipments`.
- `config/settings_data.json` no contiene el footer antiguo.

`VERIFICADO PERO MEJORABLE`:

- `sections/header-group.json` conserva referencias deshabilitadas a `Gift Card` en bloques de header/mobile/mega menu.
- Esto no explica por si solo el residuo del footer publico, pero queda como deuda separada.

### Shopify Admin - traducciones MENU

`VERIFICADO Y CORRECTO` para titulos activos del footer en idiomas prioritarios:

- EN:
  - `AYUDA Y SOPORTE` -> `HELP AND SUPPORT`.
  - `PROFESIONALES` -> `PROFESSIONALS`.
  - `EMPRESA` -> `COMPANY`.
  - `LEGAL` -> `LEGAL`.
- FR:
  - `AIDE ET SUPPORT`.
  - `PROFESSIONNELS`.
  - `ENTREPRISE`.
  - `LEGAL`.
- DE:
  - `HILFE UND SUPPORT`.
  - `FUR FACHKUNDEN`.
  - `UNTERNEHMEN`.
  - `RECHTLICHES`.
- NL:
  - `HULP EN SUPPORT`.
  - `PROFESSIONALS`.
  - `BEDRIJF`.
  - `JURIDISCH`.

`VERIFICADO PERO MEJORABLE`:

- El menu legacy `footer-matchwalls` conserva una traduccion DE antigua de titulo (`Fusszeilen-Matchwalls`) aunque el menu esta vacio y no esta referenciado por el footer MAIN.

### HTML publico

Estado inicial del diagnostico: `INCORRECTO`, por evidencia externa previa.

- `https://www.matchwalls.com/en` sigue mostrando en HTML publico:
  - `Professional & social`.
  - `Gift Card`.
  - `International shipments`.
  - `Black Friday 2024`.
- `https://www.matchwalls.com/` sigue mostrando en HTML publico:
  - `PROFESIONALES & SOCIAL`.
  - `Tarjeta regalo`.
  - `Envios internacionales`.
  - `Black Friday 2024`.

Addendum 2026-06-17 21:44 +02:00: `CORREGIDO Y VERIFICADO`.

- Navegador renderizado real:
  - ES `https://www.matchwalls.com/`: footer sin `Tarjeta regalo`, `Envios internacionales`, `Black Friday 2024` ni `PROFESIONALES & SOCIAL`.
  - EN `https://www.matchwalls.com/en`: footer sin `Gift Card`, `Gift card`, `International shipments`, `Black Friday 2024` ni `Professional & social`.
  - FR `https://www.matchwalls.com/fr`: footer sin `Carte-cadeau`, `Envois internationaux` ni `Black Friday 2024`.
  - DE `https://www.matchwalls.com/de`: footer sin `Geschenkkarte` ni `Black Friday 2024`.
  - NL `https://www.matchwalls.com/nl`: footer sin `Cadeaubon` ni `Black Friday 2024`.
- HTTP directo actual con `cache: no-store` desde entorno Node:
  - ES, EN, FR, DE y NL devuelven status 200.
  - No se detectan los terminos antiguos buscados en el HTML bruto actual.
- Consulta Shopify Admin de solo lectura:
  - Los IDs legacy exportados por LangShop `gid://shopify/Link/493550239971` y `gid://shopify/Link/493550371043` no existen como recursos traducibles actuales.
  - Los IDs antiguos de respaldo `gid://shopify/Link/712964669816`, `gid://shopify/Link/713032991096` y `gid://shopify/Link/493556662499` tampoco existen como recursos traducibles actuales.
  - Todos los menus actuales accesibles por Admin GraphQL fueron leidos; esos IDs y textos antiguos no aparecen en ningun menu vivo.

## Interpretacion tecnica

Hecho verificado:

- La fuente normal esperada del footer en Shopify Admin esta limpia.
- El HTML publico actual servido por HTTP directo sin cache esta limpio en ES, EN, FR, DE y NL.
- El DOM renderizado actual del navegador esta limpio en ES, EN, FR, DE y NL.
- La evidencia externa previa con residuos no se reproduce en las comprobaciones actuales y queda clasificada como cache/extraccion stale o no actual.

Inferencia razonable, no confirmada:

- El residuo observado por la herramienta externa no parece venir de menus Shopify activos, del archivo `footer-group.json` MAIN actual ni de recursos `Link` traducibles vivos.
- El origen probable de esa evidencia previa es cache/extraccion externa stale, no la web actual servida por Shopify en este momento.

No afirmado:

- No afirmo que LangShop sea el causante.
- No afirmo que Google, Bing, Search Console o sistemas IA ya hayan actualizado sus datos.
- No afirmo que no existan otros problemas SEO/GEO fuera del footer.

## Riesgos

- Riesgo SEO/GEO residual: si un buscador trabaja con una cache antigua, puede tardar en reflejar el estado corregido aunque la web actual ya este limpia.
- Riesgo operativo: ejecutar borrados de traducciones o importaciones LangShop sin aislar origen podria romper textos correctos ya publicados.
- Riesgo tecnico: una mutacion "inocua" para forzar cache no debe ejecutarse sin aprobacion exacta y plan de reversion.

## Acciones no realizadas

- No se modifico Shopify.
- No se modifico LangShop.
- No se importo ningun CSV.
- No se borraron traducciones.
- No se ejecutaron mutaciones.
- No se modificaron menus, tema, handles, URLs, redirecciones, productos, colecciones ni inventario.

## Siguiente paso recomendado

Cerrar `MW-LANGSHOP-PUBLIC-FOOTER-RESIDUE-007` como verificacion sin escritura:

1. No ejecutar correccion Shopify/LangShop para este residuo concreto porque no se reproduce en web actual.
2. Mantener como deuda separada los bloques deshabilitados de `sections/header-group.json` con referencias antiguas a Gift Card.
3. Continuar con el siguiente lote tecnico prioritario: indexabilidad, canonical/hreflang, sitemaps, 404/redirects y residuos de Search Console.
4. No prometer recrawl ni trafico; solicitar recrawleo o validacion en Search Console solo cuando exista evidencia de que la URL actual esta limpia.
