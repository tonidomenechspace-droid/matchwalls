# Resultado lote MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E

Fecha: 2026-07-05

## Estado final

`INCOMPLETO`

El lote fue aprobado por Daniel, preparado y respaldado, pero no quedó aplicado en MAIN.

## Alcance aprobado

`APROBADO LOTE MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E`

Objetivo: aplicar en el tema MAIN la misma exclusión visual por ID estable de la colección Black Friday ya verificada en el borrador `178396463480`.

## Estado real comprobado

`VERIFICADO Y CORRECTO`

- Tema MAIN: `gid://shopify/OnlineStoreTheme/178399019384`
- Nombre MAIN: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`
- Rol: `MAIN`
- Archivo objetivo: `sections/main-list-collections.liquid`
- Checksum actual leído antes y después del intento: `70c8ead00d939f15528f6f11e5bfb540`
- Tamaño actual: `4934`

MAIN sigue intacto.

## Respaldo creado

`VERIFICADO Y CORRECTO`

Se creó respaldo exacto del archivo MAIN leído desde Shopify:

- `auditoria-seo-geo-matchwalls/backups-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E-2026-07-05/sections-main-list-collections.liquid.before`

Checksum del respaldo:

- `70c8ead00d939f15528f6f11e5bfb540`

## Archivo preparado

`VERIFICADO Y CORRECTO`

Archivo preparado localmente:

- `auditoria-seo-geo-matchwalls/work-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E/sections/main-list-collections.liquid`

Checksum preparado:

- `4fa31878b7bcb38e469ce27c109ffec8`

Validaciones locales:

- Schema JSON válido.
- Exclusión por ID presente.
- Sin literales `black-friday`.
- Un único `unless`.
- Un único `endunless`.
- Un único loop `for collection in collections_list`.

Cambio propuesto:

```liquid
{%- assign mw_collection_id = collection.id | append: '' -%}
{%- unless mw_collection_id == '646234440056' -%}
```

## Intentos de ejecución

`VERIFICADO PERO MEJORABLE`

### 1. API GraphQL Admin

Resultado: bloqueado por política de seguridad del conector.

Motivo devuelto:

`themeFilesUpsert` contra el tema publicado MAIN está bloqueado. La herramienta permite escribir en temas no publicados, pero no en el tema live.

No se produjo cambio en Shopify.

### 2. Shopify Admin / editor web

Resultado: no aplicado.

El editor cargó correctamente el archivo MAIN, pero la automatización del navegador no consiguió insertar el contenido preparado en el editor de código de forma verificable. No se pulsó `Save`.

No se produjo cambio en Shopify.

### 3. Shopify CLI

Resultado: no disponible.

`shopify` no está instalado en el entorno local (`command not found`). No se instaló software ni se ejecutó push.

No se produjo cambio en Shopify.

## QA público live

`INCOMPLETO`

La web pública sigue sirviendo el tema MAIN `178399019384` y Black Friday sigue presente:

| Idioma | URL | HTTP | Tarjetas | Black Friday |
|---|---:|---:|---:|---:|
| ES | `/collections` | 200 | 48 | 3 |
| EN | `/en/collections` | 200 | 48 | 3 |
| FR | `/fr/collections` | 200 | 48 | 2 |
| DE | `/de/collections` | 200 | 48 | 1 |
| NL | `/nl/collections` | 200 | 48 | 2 |

## Conclusión

`REQUIERE DECISION HUMANA`

No sería profesional afirmar que el lote está corregido: el cambio está listo y validado, pero no aplicado al MAIN por bloqueo técnico de escritura segura.

## Opciones seguras para avanzar

### Opción A: manual Admin

Daniel edita en Shopify Admin el archivo:

`sections/main-list-collections.liquid`

Tema:

`178399019384`

Y sustituye el contenido por el archivo preparado:

`auditoria-seo-geo-matchwalls/work-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E/sections/main-list-collections.liquid`

Después se ejecutaría un postcheck:

`MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-POSTCHECK-013E16E1`

### Opción B: instalar y autenticar Shopify CLI

Requiere autorización separada porque instala software/local tooling:

`MW-SHOPIFY-CLI-INSTALL-AUTH-THEME-PUSH-013E16E2`

Objetivo: instalar Shopify CLI, autenticar contra `matchwalls.myshopify.com`, hacer push de un único archivo al tema `178399019384` y verificar.

## Evidencias

- `admin-attempt-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E-2026-07-05.csv`
- `postcheck-live-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E-2026-07-05.csv`
