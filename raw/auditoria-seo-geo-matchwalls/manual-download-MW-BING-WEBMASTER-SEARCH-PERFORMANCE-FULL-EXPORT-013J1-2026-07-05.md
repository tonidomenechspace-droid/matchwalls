# Descarga manual requerida — MW-BING-WEBMASTER-SEARCH-PERFORMANCE-FULL-EXPORT-013J1

Fecha: 2026-07-05  
Hora de registro: 16:00 Europe/Madrid  
Estado: `INCOMPLETO`  
Modo: solo lectura / sin cambios externos

## Objetivo del lote

Descargar el export completo de Bing Webmaster Tools > Search Performance para analizar las 88 keywords completas y, si Bing lo permite, páginas, países y dispositivos.

## Estado real comprobado

`NO ACCESIBLE`

Codex intentó abrir:

`https://www.bing.com/webmasters/searchperf?siteUrl=https://matchwalls.com/`

Resultado:

- La pestaña del navegador integrado no tiene sesión autenticada en Bing.
- Bing redirige a la pantalla pública de Webmaster Tools con botón `Sign In`.
- No se pudo acceder al informe autenticado ni pulsar `Download all`.

## Comprobación de archivos locales

`INCOMPLETO`

Se revisaron:

- `C:\Users\d.bermejo\OneDrive - Matchwalls\Escritorio`
- `C:\Users\d.bermejo\Downloads`

No se encontró un CSV nuevo de Bing Search Performance. Solo aparece el CSV previo de IndexNow:

- `matchwalls.com_IndexNowSubmittedUrls_7_5_2026 AAAAAAAA.csv`

## Qué debe hacer Daniel

`REQUIERE DECISION HUMANA`

En la sesión de navegador donde Bing Webmaster Tools sí está autenticado:

1. Ir a `Bing Webmaster Tools`.
2. Seleccionar la propiedad `matchwalls.com/`.
3. Abrir `Search Performance`.
4. Confirmar rango `3 M`, salvo que se decida otro rango.
5. Pulsar `Download all`.
6. Guardar el CSV en el Escritorio.
7. Avisar con:

`GUARDADO 013J1`

Si Bing permite varios exports, descargar en este orden:

1. `Keywords`
2. `Pages`
3. `Country`
4. `Device`

## Qué hará Codex después

Cuando el CSV exista localmente, Codex:

1. Verificará nombre, fecha, tamaño y columnas.
2. Confirmará rango y propiedad si el CSV lo contiene.
3. Analizará las 88 keywords completas.
4. Separará brand / no-brand.
5. Clasificará por idioma: ES, EN, FR, DE, NL y fuera de prioridad.
6. Detectará oportunidades GEO/AEO sin ejecutar cambios.
7. Creará matrices de prioridad para próximos lotes.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó:

- Shopify.
- Bing Webmaster Tools.
- IndexNow.
- Search Performance.
- Sitemap.
- Robots.
- URLs.
- Handles.
- Tema.
- Traducciones.
- SEO fields.
- Apps.

## Estado final

`INCOMPLETO`

El lote queda bloqueado hasta disponer del export CSV autenticado.
