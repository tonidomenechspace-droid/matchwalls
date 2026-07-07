# Resultado lote MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-QA-012M

Fecha: 2026-07-04 14:37:08 +02:00  
Estado final del diagnóstico: `VERIFICADO PERO MEJORABLE`

## Alcance

Lote de solo lectura.

Objetivo: auditar la descubribilidad y el enlazado interno público de las landings país España/Francia en los idiomas prioritarios ES, EN, FR, DE y NL.

No se modificó Shopify, LangShop, temas, menús, páginas, handles, URLs, canonicals, hreflang, metadatos, productos, precios, redirecciones ni App Embeds.

## Documentos leídos

- `resultado-MW-GEO-LANDINGS-SPAIN-FRANCE-RICH-RESULTS-POSTCHECK-012L7-2026-07-04.md`.
- `registro-cambios-ejecutados.md`.

## Estado real Shopify comprobado

Consulta Shopify Admin de solo lectura:

- MAIN: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- `processing`: `false`.
- `processingFailed`: `false`.
- `updatedAt`: `2026-07-04T12:23:11Z`.
- `config/settings_data.json`: checksum `d487694e14fe7558034b7d4595075de4`.
- `snippets/geo-landing-schema.liquid`: checksum `9033b2bfa89dc435b9811b3d897e07c1`.
- `snippets/microdata-schema.liquid`: checksum `a3d8e23b4979219149a9c5b5f76723ec`.

Estado: `VERIFICADO Y CORRECTO`.

## URLs auditadas

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

## Hallazgos verificados

### Descubrimiento técnico

Estado: `VERIFICADO Y CORRECTO`.

Las 10 landings:

- Responden HTTP 200.
- Tienen canonical propio correcto.
- No tienen `noindex`.
- Están presentes en sitemap.
- Tienen cluster hreflang visible con 7 alternates.

### Enlaces salientes desde las landings

Estado: `VERIFICADO Y CORRECTO`.

Las landings tienen enlaces internos salientes suficientes hacia recursos comerciales o informativos: muestras, profesionales, personalización, colecciones y páginas de soporte. El recuento detectado fue de 74 enlaces internos por landing, incluyendo navegación y contenido.

### Enlaces entrantes desde home/navegación pública probada

Estado: `INCOMPLETO`.

No se detectó enlace HTML directo desde las homes de idioma a ninguna de las 10 landings:

- Home ES: 0 enlaces a landings España/Francia.
- Home EN: 0 enlaces a landings España/Francia.
- Home FR: 0 enlaces a landings España/Francia.
- Home DE: 0 enlaces a landings España/Francia.
- Home NL: 0 enlaces a landings España/Francia.

Los únicos enlaces entrantes detectados desde el conjunto probado eran auto-enlaces internos de la propia página tipo “saltar al contenido”, por lo que no cuentan como enlazado editorial ni navegación real.

### Crosslink entre landings país

Estado: `INCOMPLETO`.

No se detectó enlace same-language entre:

- España ES ↔ Francia ES.
- España EN ↔ Francia EN.
- España FR ↔ Francia FR.
- España DE ↔ Francia DE.
- España NL ↔ Francia NL.

Esto reduce la fuerza del cluster país y deja las landings más dependientes del sitemap/hreflang que de navegación semántica editorial.

## Interpretación SEO/GEO

No hay un problema crítico de indexabilidad: las URLs son accesibles y están en sitemap.

Sí hay una mejora importante de SEO/GEO:

- Añadir enlaces editoriales visibles entre landings país.
- Añadir una ruta de descubrimiento desde home, footer, hub o bloque editorial “Papel pintado por país”.
- Evitar depender solo de sitemap/hreflang para que buscadores e IA entiendan la jerarquía comercial de países.

## Recomendación

No tocar Shopify todavía en este lote.

Siguiente lote recomendado:

`MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-COPY-MAP-012N`

Objetivo: preparar, sin escribir, el mapa exacto de enlaces y textos por idioma para:

1. Crosslinks España ↔ Francia en cada idioma.
2. Bloque editorial mínimo de “Papel pintado por país” o equivalente.
3. Ubicación recomendada: al final de las landings país existentes, antes o después de FAQs, según el HTML actual.
4. Evaluar después si conviene un segundo lote para home/footer/hub.

## Archivos de evidencia

- `qa-internal-linking-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-QA-012M-2026-07-04.csv`.
- `home-linking-summary-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-QA-012M-2026-07-04.csv`.

## Estado final

`VERIFICADO PERO MEJORABLE`

El lote 012M queda cerrado como diagnóstico. No se aplicó ningún cambio en Shopify.
