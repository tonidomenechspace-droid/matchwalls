# Resultado lote MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-DRAFT-ID-EXCLUDE-013E16D

Fecha: 2026-07-05

## Estado final

`CORREGIDO Y VERIFICADO`

## Alcance aprobado

`APROBADO LOTE MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-DRAFT-ID-EXCLUDE-013E16D`

Se ha aplicado una exclusión visual quirúrgica de la colección Black Friday en el hub/listado de colecciones del tema borrador.

No se ha tocado el tema MAIN, no se ha publicado ningún tema y no se han modificado colecciones, productos, handles, URLs, redirecciones, SEO, LangShop, mercados, inventario ni precios.

## Recurso afectado

- Tema borrador: `gid://shopify/OnlineStoreTheme/178396463480`
- Nombre: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`
- Rol: `UNPUBLISHED`
- Archivo: `sections/main-list-collections.liquid`
- Colección excluida visualmente: `gid://shopify/Collection/646234440056`
- ID numérico usado en Liquid: `646234440056`

## Respaldo

`VERIFICADO Y CORRECTO`

Se creó respaldo del archivo anterior:

- `auditoria-seo-geo-matchwalls/backups-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-DRAFT-ID-EXCLUDE-013E16D-2026-07-05/sections-main-list-collections.liquid.before`

Checksum previo del archivo en draft:

- `910b00ca49c28be5258ac2a17f1731d5`

## Cambio aplicado

`VERIFICADO Y CORRECTO`

Dentro del loop de colecciones se añadió una condición por ID estable:

```liquid
{%- assign mw_collection_id = collection.id | append: '' -%}
{%- unless mw_collection_id == '646234440056' -%}
  ...
{%- endunless -%}
```

Motivo: evitar depender de títulos o handles traducidos. La colección puede seguir existiendo para decisiones futuras, pero deja de pintarse en el listado evergreen del borrador.

## Verificación admin Shopify

`VERIFICADO Y CORRECTO`

Lectura posterior desde Shopify:

- Tema draft: `gid://shopify/OnlineStoreTheme/178396463480`
- `updatedAt`: `2026-07-04T23:06:03Z`
- `processing`: `false`
- `processingFailed`: `false`
- Archivo: `sections/main-list-collections.liquid`
- Checksum posterior: `d75fb34f3716c218221b8607b91d9002`
- Tamaño posterior: `21109`
- Exclusión por ID presente: sí
- Literales `black-friday` en Liquid: 0

Nota técnica: la salida de la mutación GraphQL quedó truncada por límite de contexto, por lo que el cierre se basa en la lectura admin posterior y el QA público de preview.

## Verificación MAIN

`VERIFICADO Y CORRECTO`

MAIN real identificado:

- Tema MAIN: `gid://shopify/OnlineStoreTheme/178399019384`
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`
- Archivo MAIN: `sections/main-list-collections.liquid`
- Checksum MAIN: `70c8ead00d939f15528f6f11e5bfb540`

El lote no ha escrito sobre MAIN.

## QA público del preview del borrador

`CORREGIDO Y VERIFICADO`

Se probó el preview con cookie de sesión de Shopify para asegurar que el HTML venía del tema `178396463480`.

| Idioma | URL probada | HTTP | Tema preview | Tarjetas | Black Friday |
|---|---:|---:|---:|---:|---:|
| ES | `https://www.matchwalls.com/collections` | 200 | sí | 47 | 0 |
| EN | `https://www.matchwalls.com/en/collections` | 200 | sí | 47 | 0 |
| FR | `https://www.matchwalls.com/fr/collections` | 200 | sí | 47 | 0 |
| DE | `https://www.matchwalls.com/de/collections` | 200 | sí | 47 | 0 |
| NL | `https://www.matchwalls.com/nl/collections` | 200 | sí | 47 | 0 |

En los cinco idiomas prioritarios:

- `mw-collections-root` presente.
- `theme;desc="178396463480"` confirmado en `server-timing`.
- `black_friday_hits = 0`.
- Canonicals conservados.

## Evidencias generadas

- `admin-post-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-DRAFT-ID-EXCLUDE-013E16D-2026-07-05.csv`
- `postcheck-public-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-DRAFT-ID-EXCLUDE-013E16D-2026-07-05.csv`

## Reversión

`VERIFICADO Y CORRECTO`

Para revertir, restaurar en el mismo tema draft el archivo respaldado:

- `auditoria-seo-geo-matchwalls/backups-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-DRAFT-ID-EXCLUDE-013E16D-2026-07-05/sections-main-list-collections.liquid.before`

Esto devolvería el checksum del draft a `910b00ca49c28be5258ac2a17f1731d5`.

## Estado operativo

`REQUIERE DECISION HUMANA`

La corrección está validada en borrador. Para que la web pública MAIN deje de mostrar Black Friday en el hub de colecciones, hace falta un lote separado y aprobación exacta para MAIN.

Siguiente lote recomendado:

`MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E`
