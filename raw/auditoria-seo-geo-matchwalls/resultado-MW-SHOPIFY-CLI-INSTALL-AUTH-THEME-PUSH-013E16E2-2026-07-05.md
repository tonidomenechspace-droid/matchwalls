# Resultado lote MW-SHOPIFY-CLI-INSTALL-AUTH-THEME-PUSH-013E16E2

Fecha: 2026-07-05

Hora local de cierre: 06:06:02 +02:00

## Estado final

`CORREGIDO Y VERIFICADO`

El lote aprobado se ejecutó correctamente mediante Shopify CLI local. Se aplicó únicamente el archivo `sections/main-list-collections.liquid` al tema MAIN `178399019384`.

## Alcance aprobado

`APROBADO LOTE MW-SHOPIFY-CLI-INSTALL-AUTH-THEME-PUSH-013E16E2`

Objetivo: instalar/verificar Shopify CLI local, autenticar contra `matchwalls.myshopify.com` si era necesario, y subir de forma quirúrgica un único archivo al tema MAIN para excluir la colección evergreen Black Friday del hub público de colecciones.

## Estado real comprobado antes de ejecutar

`VERIFICADO Y CORRECTO`

- Store: `matchwalls.myshopify.com`
- Tema MAIN: `gid://shopify/OnlineStoreTheme/178399019384`
- Nombre MAIN: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`
- Archivo objetivo: `sections/main-list-collections.liquid`
- Checksum previo MAIN: `70c8ead00d939f15528f6f11e5bfb540`
- Tamaño previo MAIN: `4934`

## Respaldo disponible

`VERIFICADO Y CORRECTO`

Se reutiliza el respaldo exacto creado en el lote anterior `013E16E`:

- `auditoria-seo-geo-matchwalls/backups-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E-2026-07-05/sections-main-list-collections.liquid.before`

Checksum del respaldo:

- `70c8ead00d939f15528f6f11e5bfb540`

## Archivo publicado

`VERIFICADO Y CORRECTO`

Archivo local preparado:

- `auditoria-seo-geo-matchwalls/work-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E/sections/main-list-collections.liquid`

Validación previa:

- Checksum preparado: `4fa31878b7bcb38e469ce27c109ffec8`
- Tamaño preparado: `5161`
- Exclusión por ID estable presente: `{%- unless mw_collection_id == '646234440056' -%}`
- No se tocaron handles, URLs, traducciones, mercados, productos, colecciones ni SEO fields.

## Ejecución

`VERIFICADO Y CORRECTO`

Shopify CLI local:

- Directorio local: `.shopify-cli-local-013E16E2`
- Versión CLI: `4.3.0`
- Conexión verificada contra `matchwalls.myshopify.com`
- Tema live detectado: `178399019384`

Comando ejecutado de forma acotada:

```powershell
shopify theme push --store matchwalls.myshopify.com --theme 178399019384 --path auditoria-seo-geo-matchwalls/work-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E --only "sections/main-list-collections.liquid" --nodelete --allow-live --json
```

Resultado CLI:

- `Theme upload complete`
- Tema devuelto: `178399019384`
- Rol: `live`
- No se usó `--publish`.
- No se subieron otros archivos por alcance `--only`.
- No se eliminaron archivos remotos por `--nodelete`.

La CLI mostró un aviso de que el directorio no era un tema completo. El aviso no bloqueó el push porque el lote usaba `--only` sobre un archivo existente dentro de una estructura válida `sections/`.

## Verificación Admin API posterior

`VERIFICADO Y CORRECTO`

Consulta Admin GraphQL posterior:

- Tema MAIN: `gid://shopify/OnlineStoreTheme/178399019384`
- Archivo: `sections/main-list-collections.liquid`
- Checksum nuevo: `4fa31878b7bcb38e469ce27c109ffec8`
- Tamaño nuevo: `5161`
- `updatedAt`: `2026-07-05T04:00:31Z`
- `processing`: `false`
- `processingFailed`: `false`

## QA público live

`VERIFICADO Y CORRECTO`

| Idioma | URL | HTTP | Tema | Tarjetas | Black Friday | Resultado |
|---|---|---:|---:|---:|---:|---|
| ES | `https://www.matchwalls.com/collections` | 200 | 178399019384 | 47 | 0 | PASS |
| EN | `https://www.matchwalls.com/en/collections` | 200 | 178399019384 | 47 | 0 | PASS |
| FR | `https://www.matchwalls.com/fr/collections` | 200 | 178399019384 | 47 | 0 | PASS |
| DE | `https://www.matchwalls.com/de/collections` | 200 | 178399019384 | 47 | 0 | PASS |
| NL | `https://www.matchwalls.com/nl/collections` | 200 | 178399019384 | 47 | 0 | PASS |

## Incidencias

`VERIFICADO PERO MEJORABLE`

- La instalación local de Shopify CLI requirió reconstruir dependencias con el runtime Node local disponible en Codex.
- Shopify CLI emitió un aviso no bloqueante sobre directorio de tema incompleto.
- No se detectaron incidencias en Admin API ni storefront público después del push.

## Método exacto de reversión

`VERIFICADO Y CORRECTO`

Si fuera necesario revertir, restaurar únicamente:

- `sections/main-list-collections.liquid`

con el respaldo:

- `auditoria-seo-geo-matchwalls/backups-MW-COLLECTIONS-BLACK-FRIDAY-EVERGREEN-MAIN-SURGICAL-EXCLUDE-013E16E-2026-07-05/sections-main-list-collections.liquid.before`

La reversión debe hacerse con el mismo método acotado:

```powershell
shopify theme push --store matchwalls.myshopify.com --theme 178399019384 --path [directorio_con_respaldo_en_sections] --only "sections/main-list-collections.liquid" --nodelete --allow-live
```

Después de revertir, el checksum esperado sería:

- `70c8ead00d939f15528f6f11e5bfb540`

## Evidencias generadas

`VERIFICADO Y CORRECTO`

- `admin-post-MW-SHOPIFY-CLI-INSTALL-AUTH-THEME-PUSH-013E16E2-2026-07-05.csv`
- `postcheck-live-MW-SHOPIFY-CLI-INSTALL-AUTH-THEME-PUSH-013E16E2-2026-07-05.csv`
- `resultado-MW-SHOPIFY-CLI-INSTALL-AUTH-THEME-PUSH-013E16E2-2026-07-05.md`

## Próximo paso recomendado

`REQUIERE DECISION HUMANA`

El siguiente paso natural del plan SEO/GEO/AEO es volver a la cola tras este cierre:

1. Esperar respuesta de Shopify Engineering sobre el problema de caché/render shard de las páginas geográficas.
2. Continuar con Bing/Copilot/IndexNow y política de crawlers, sin tocar tema ni páginas hasta que la incidencia de infraestructura esté estable o documentada.
3. Mantener pendiente la reparación global de SEO meta multiidioma hasta que se defina la vía segura entre Shopify nativo y LangShop.
