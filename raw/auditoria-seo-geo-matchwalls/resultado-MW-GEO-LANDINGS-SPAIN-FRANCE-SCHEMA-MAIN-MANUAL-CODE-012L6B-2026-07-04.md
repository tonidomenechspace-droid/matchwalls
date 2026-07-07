# Resultado lote MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-MANUAL-CODE-012L6B

Fecha: 2026-07-04 14:25:25 +02:00  
Estado final: `CORREGIDO Y VERIFICADO`

## Alcance ejecutado

Lote aprobado por Daniel mediante aprobación exacta:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-MANUAL-CODE-012L6B`

Objetivo: incorporar en el tema MAIN el schema JSON-LD WebPage + FAQPage para landings país España/Francia en los idiomas prioritarios ES, EN, FR, DE y NL.

Recursos afectados:

- Tema MAIN: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Archivo creado: `snippets/geo-landing-schema.liquid`.
- Archivo actualizado: `snippets/microdata-schema.liquid`.

No se modificaron páginas, LangShop, handles, URLs, canonicals, hreflang, metadatos nativos, productos, precios, inventario, redirecciones, App Embeds ni `config/settings_data.json`.

## Estado real comprobado antes de escribir

Consulta Shopify Admin previa:

- Tema: MAIN.
- `processing`: `false`.
- `processingFailed`: `false`.
- `snippets/geo-landing-schema.liquid`: no existía.
- `snippets/microdata-schema.liquid`: checksum `58417e4825aa3d4570a6646f292aaedc`, size `10787`.
- `config/settings_data.json`: checksum `d487694e14fe7558034b7d4595075de4`, size `10257`.

## Validaciones previas

- Validación Liquid oficial Shopify: correcta para los dos snippets.
- `snippets/geo-landing-schema.liquid`: checksum local `9033b2bfa89dc435b9811b3d897e07c1`, size `11723`.
- `snippets/microdata-schema.liquid`: checksum local `a3d8e23b4979219149a9c5b5f76723ec`, size `10824`.
- Shopify CLI autenticada y lectura de temas correcta.
- MAIN confirmado por CLI como theme ID `178399019384`, rol `live`.

## Ejecución

La edición manual desde el Code Editor de Shopify fue descartada porque el editor intentaba guardar un archivo sin extensión `.liquid` y abría repetidamente `Save As`.

Se ejecutó la vía técnica controlada con Shopify CLI, limitada a dos archivos:

- `--theme 178399019384`.
- `--allow-live`.
- `--nodelete`.
- `--only snippets/geo-landing-schema.liquid`.
- `--only snippets/microdata-schema.liquid`.

La CLI devolvió subida completada para el tema `178399019384`.

Incidencia menor: la CLI mostró advertencia de carpeta parcial de tema. Se considera esperada porque la carpeta local del lote contenía solo los archivos necesarios. La verificación posterior confirma que los archivos objetivo quedaron exactamente con los checksums esperados y `config/settings_data.json` no cambió.

## Verificación Shopify Admin posterior

Consulta Shopify Admin posterior:

- Tema: MAIN.
- `processing`: `false`.
- `processingFailed`: `false`.
- `updatedAt`: `2026-07-04T12:23:11Z`.
- `config/settings_data.json`: `d487694e14fe7558034b7d4595075de4`, sin cambios.
- `snippets/geo-landing-schema.liquid`: `9033b2bfa89dc435b9811b3d897e07c1`, size `11723`.
- `snippets/microdata-schema.liquid`: `a3d8e23b4979219149a9c5b5f76723ec`, size `10824`.

Archivo de evidencia:

- `admin-post-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-MANUAL-CODE-012L6B-2026-07-04.csv`.

## QA pública

Resultado: `VERIFICADO Y CORRECTO`.

URLs positivas verificadas con HTTP 200, canonical propio, sin `noindex`, JSON-LD parseable, `WebPage`, `FAQPage`, `BreadcrumbList`, 3 FAQs e `inLanguage` correcto:

- España ES: `https://www.matchwalls.com/pages/papel-pintado-espana`.
- España EN: `https://www.matchwalls.com/en/pages/spain-wallpaper`.
- España FR: `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`.
- España DE: `https://www.matchwalls.com/de/pages/spanien-tapete`.
- España NL: `https://www.matchwalls.com/nl/pages/spanje-behang`.
- Francia ES: `https://www.matchwalls.com/pages/papel-pintado-francia`.
- Francia EN: `https://www.matchwalls.com/en/pages/french-wallpaper`.
- Francia FR: `https://www.matchwalls.com/fr/pages/papier-peint-en-france`.
- Francia DE: `https://www.matchwalls.com/de/pages/franzosische-tapete`.
- Francia NL: `https://www.matchwalls.com/nl/pages/frans-behang`.

URLs negativas IT/PT verificadas sin `WebPage`/`FAQPage` geo nuevo:

- `https://www.matchwalls.com/it/pages/sfondo-della-spagna`.
- `https://www.matchwalls.com/it/pages/sfondo-francese`.
- `https://www.matchwalls.com/pt/pages/papel-de-parede-da-espanha`.
- `https://www.matchwalls.com/pt/pages/papel-de-parede-frances`.

Regresión:

- Home: mantiene `WebSite` y `Organization`.
- Producto `custom-file-uploader`: mantiene `Product` y `Offer`.

Observación: `custom-file-uploader` devuelve `noindex,nofollow`. Se registra como estado existente/fuera de alcance del lote 012L6B, no como fallo del schema.

Archivo de evidencia:

- `qa-publico-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-MANUAL-CODE-012L6B-2026-07-04.csv`.

## Reversión

Si fuera necesario revertir:

1. Restaurar `snippets/microdata-schema.liquid` al checksum anterior `58417e4825aa3d4570a6646f292aaedc`, eliminando la línea:
   `{%- render 'geo-landing-schema' -%}`
2. Eliminar `snippets/geo-landing-schema.liquid` del tema MAIN.
3. Verificar que `snippets/microdata-schema.liquid` vuelve a size `10787`.
4. Verificar públicamente que las landings dejan de emitir `WebPage`/`FAQPage` geo del lote.

## Estado final

`CORREGIDO Y VERIFICADO`

El lote 012L6B queda cerrado. La capa schema WebPage + FAQPage para las landings país España/Francia queda activa en producción para ES, EN, FR, DE y NL.
