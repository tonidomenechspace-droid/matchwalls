# QA post-publicacion MW-PUBLISH-HOTFIX-001

Fecha: 16 de junio de 2026

## Alcance

Daniel confirmo: `PUBLICADO HOTFIX`.

Se ejecutaron comprobaciones exclusivamente de lectura tras la publicacion manual del tema:

- Tema publicado.
- Archivos criticos del hotfix.
- Home, producto principal, producto personalizado, articulo, carrito, contacto y formulario de particulares.
- Idiomas ES, EN, FR, DE y NL.
- Escritorio y movil.
- JSON-LD, Product, Offer, ausencia de GTIN/MPN falsos y ausencia de AggregateRating corporativo fijo.
- App Embeds mediante `config/settings_data.json` y evidencias publicas en HTML.

No se modifico Shopify en esta fase.

## Estado de temas verificado

| Tema | ID | Rol tras publicacion | Estado |
|---|---|---:|---|
| SEO schema hotfix - 2026-06-15 | `gid://shopify/OnlineStoreTheme/178383749496` | MAIN | `CORREGIDO Y VERIFICADO` |
| Production - SEO fix AggregateRating (2026-06-12) | `gid://shopify/OnlineStoreTheme/178379293048` | UNPUBLISHED | `VERIFICADO Y CORRECTO` |
| SEO-GEO staging - 2026-06-15 | `gid://shopify/OnlineStoreTheme/178383585656` | UNPUBLISHED | `VERIFICADO Y CORRECTO` |

Ninguno de los tres temas tiene procesamiento pendiente ni fallo de procesamiento.

## Archivos criticos del tema MAIN

| Archivo | Checksum | Tamano | Estado |
|---|---|---:|---|
| `snippets/microdata-schema.liquid` | `58417e4825aa3d4570a6646f292aaedc` | 10.787 | `CORREGIDO Y VERIFICADO` |
| `snippets/microdata-schema-original.liquid` | `ae9c62e4abb80d1051cbea73b03f1107` | 10.068 | `VERIFICADO Y CORRECTO` |
| `config/settings_data.json` | `a1192f2f698d277e0f69f7156a61a90c` | 10.256 | `VERIFICADO Y CORRECTO` |

La copia auxiliar `snippets/microdata-schema-original.liquid` permanece conservada, segun la instruccion de Daniel.

## Matriz publica revisada

Se revisaron 35 URLs en escritorio y 35 URLs en movil:

- Home: ES, EN, FR, DE, NL.
- Producto principal `Whispering Woods`: ES, EN, FR, DE, NL.
- Producto personalizado: ES, EN, FR, DE, NL.
- Articulo de instalacion: ES, EN, FR, DE, NL.
- Carrito: ES, EN, FR, DE, NL.
- Contacto: ES, EN, FR, DE, NL.
- Formulario particulares: ES, EN, FR, DE, NL.

Todas las URLs revisadas cargan assets publicos desde `/cdn/shop/t/43/`, correspondiente al tema hotfix publicado.

## Resultados criticos

| Validacion | Escritorio | Movil | Estado |
|---|---:|---:|---|
| URLs revisadas | 35/35 | 35/35 | `VERIFICADO Y CORRECTO` |
| Tema publicado `t/43` | 35/35 | 35/35 | `CORREGIDO Y VERIFICADO` |
| Errores de parseo JSON-LD | 0 | 0 | `VERIFICADO Y CORRECTO` |
| `AggregateRating` corporativo fijo | 0 | 0 | `CORREGIDO Y VERIFICADO` |
| GTIN/MPN falsos detectados | 0 | 0 | `CORREGIDO Y VERIFICADO` |
| Productos con `Product` y `Offer` completos | 10/10 | 10/10 | `VERIFICADO Y CORRECTO` |
| Ofertas por producto probado | 4 | 4 | `VERIFICADO Y CORRECTO` |
| App Embeds detectados | Si | Si | `VERIFICADO Y CORRECTO` |

## Evidencia de schema

Producto principal EN retestado tras una carga lenta inicial:

- URL: `https://www.matchwalls.com/en/products/whispering-woods-blue`
- H1: `Whispering Woods Blue`
- JSON-LD: `BreadcrumbList`, `Product`
- `Offer`: 4
- Ofertas completas con precio, moneda, disponibilidad, URL y SKU: 4
- GTIN/MPN falsos: 0
- `AggregateRating`: 0
- Tema publico: `t/43`

El mismo patron critico se verifico en los productos principales y personalizados de ES, EN, FR, DE y NL.

## App Embeds

`config/settings_data.json` conserva el checksum validado antes de publicar:

`a1192f2f698d277e0f69f7156a61a90c`

Evidencia publica detectada en HTML durante el QA:

- Shopify Forms / Qikify Forms.
- GDPR / Pandectes.
- Shopify Inbox.
- Instafeed.
- Klaviyo.
- LangShop.
- Wishlist.

Estado: `VERIFICADO Y CORRECTO`.

## Incidencias no bloqueantes y no atribuibles al hotfix

| Incidencia | Evidencia | Estado |
|---|---|---|
| Carrito sin H1 | ES, EN, FR, DE y NL en escritorio y movil | `VERIFICADO PERO MEJORABLE` |
| Formulario particulares sin H1 | ES, EN, FR, DE y NL en escritorio y movil | `VERIFICADO PERO MEJORABLE` |
| Pequeno desbordamiento horizontal movil | DE home; productos ES/EN/FR/DE/NL; producto personalizado ES/EN/FR/DE/NL; DE articulo, carrito, contacto y formulario | `VERIFICADO PERO MEJORABLE` |
| Traducciones y plantillas editoriales pendientes | FAQ, Profesionales, Social/Prensa/Afiliacion, Muestras, Guia y footer ya documentados | `INCOMPLETO` |

Estas incidencias ya estaban fuera del alcance del hotfix de schema y no bloquean la publicacion realizada.

## Limitacion

No se reejecuto una prueba externa de Google Rich Results en esta fase post-publicacion. La validacion realizada fue:

- lectura publica de la web publicada;
- parseo de JSON-LD sin errores;
- comprobacion de tipos schema, Product y Offer;
- ausencia de identificadores falsos;
- ausencia de AggregateRating corporativo fijo.

El lote previo `MW-QA-HOTFIX-001` ya habia validado el hotfix antes de publicar.

## Decision

Estado final del hotfix publicado:

`CORREGIDO Y VERIFICADO`

El tema `SEO schema hotfix - 2026-06-15` esta publicado como MAIN y el QA post-publicacion no detecta regresiones criticas en schema, productos, home, articulos, carrito, contacto, formularios ni App Embeds dentro del alcance revisado.

No se debe publicar `SEO-GEO staging - 2026-06-15`.
