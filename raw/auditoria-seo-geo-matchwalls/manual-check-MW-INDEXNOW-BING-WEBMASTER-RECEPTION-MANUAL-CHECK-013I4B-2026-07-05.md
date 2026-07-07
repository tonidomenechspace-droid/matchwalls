# MW-INDEXNOW-BING-WEBMASTER-RECEPTION-MANUAL-CHECK-013I4B

Fecha: 2026-07-05  
Modo: verificación manual con capturas de Daniel.  
Estado final: `CORREGIDO Y VERIFICADO`.

## Objetivo

Comprobar en Bing Webmaster Tools, con sesión autenticada de Daniel, si existe señal de recepción/registro de IndexNow tras instalar y configurar la app.

## Estado real comprobado en capturas

`CORREGIDO Y VERIFICADO`

Propiedad:

- `matchwalls.com/`

Sección:

- `IndexNow`
- URL visible: `bing.com/webmasters/indexnow?siteUrl=https://matchwalls.com/`

Panel `IndexNow Insights`:

- Submitted URLs: `13`

Tabla `Submitted Urls list`:

1. `https://www.matchwalls.com/`
   - Submitted: `Today at 10:02`
   - Source: `Self`
   - Details: `View`

2. `https://www.matchwalls.com/products/custom-file-uploader`
   - Submitted: `15 Jun 2026 at 22:52`
   - Source: `Shopify`
   - Details: `View`

3. `https://www.matchwalls.com/products`
   - Submitted: `15 Jun 2026 at 14:49`
   - Source: `Shopify`
   - Details: `View`

La tabla indica `3 rows` visibles, aunque el panel total indica `13` URLs enviadas.

## Interpretación

`CORREGIDO Y VERIFICADO`

Bing Webmaster Tools sí muestra actividad de IndexNow para MatchWalls.

La home `https://www.matchwalls.com/` aparece recibida/enviada hoy con source `Self`. Esto es coherente con el envío observado en la app IndexNow.

No se confirma indexación ni ranking. Solo se confirma recepción/registro en Bing Webmaster Tools.

## Riesgos / cautelas

`VERIFICADO PERO MEJORABLE`

- `Submitted` no significa indexado.
- El total de 13 URLs requiere export o revisión completa si se quiere auditar todas las URLs.
- Hay URLs antiguas enviadas por Shopify el 15 de junio de 2026.
- Antes de usar envíos manuales, conviene exportar/listar las 13 URLs para verificar que no haya muestras, URLs sin valor o rutas no deseadas.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se usó Export, View, Submit URL, Manual submissions, API key ni ninguna acción de envío. No se modificó Bing, Shopify ni la app.

## Próximo lote recomendado

`MW-INDEXNOW-BING-WEBMASTER-SUBMITTED-URLS-AUDIT-013I5`

Objetivo:

1. exportar o listar las 13 URLs enviadas;
2. clasificar fuente, fecha y tipo;
3. detectar si hay URLs no deseadas;
4. decidir si se permite un piloto manual controlado o si se mantiene solo auto-submit.
