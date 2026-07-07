# MW-INDEXNOW-APP-BING-RECEPTION-RECHECK-013I4

Fecha: 2026-07-05  
Modo: solo lectura.  
Estado final: `VERIFICADO PERO MEJORABLE`.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `result-MW-INDEXNOW-APP-I18N-LANGUAGES-ACTIVATION-013I3-2026-07-05.md`
- `decision-MW-INDEXNOW-APP-I18N-LANGUAGES-DECISION-013I2-2026-07-05.md`
- `settings-logs-MW-INDEXNOW-APP-POSTINSTALL-SETTINGS-LOGS-QA-013I1-2026-07-05.md`
- `postinstall-MW-INDEXNOW-APP-PILOT-INSTALL-CONFIG-013I-STORESpark-PREMIUM-2026-07-05.md`
- `registro-cambios-ejecutados.md`

## Objetivo

Comprobar tras la activación de idiomas `013I3`:

1. si la app IndexNow generó nuevos envíos;
2. si hay fallos;
3. si Bing Webmaster Tools muestra recepción/estado relacionado con IndexNow.

## Recheck en app IndexNow

`CORREGIDO Y VERIFICADO`

Pantalla revisada:

- `https://admin.shopify.com/store/matchwalls/apps/indexnow-18/app`

Estado visible:

- Mensaje: `Your store is now connected to IndexNow`
- Mensaje operativo: `Every time a page changes, we will automatically submit your updates to Bing, ChatGPT, Yandex, etc.`
- Last 30 Days Submissions: `1`
- Failed Submissions: `0`
- Failure Rate: `0.0%`
- Breakdown: `Home update` con `1` successful

Interpretación:

- No hay subida de contador tras activar EN/FR/DE/NL.
- No se observan envíos retroactivos.
- No se observan fallos.

## Recheck en Bing Webmaster Tools

`NO ACCESIBLE`

Se intentó abrir:

- `https://www.bing.com/webmasters/indexnow?siteUrl=https://matchwalls.com/`

Resultado:

- Redirección a pantalla pública de Bing Webmaster Tools.
- Se muestra `Sign In`.
- No hay sesión autenticada disponible en la pestaña abierta.

Conclusión: no se puede verificar desde Codex si Bing recibió o muestra la URL enviada por la app. No se pulsó Sign In ni se aceptaron cookies.

## Estado técnico

`VERIFICADO PERO MEJORABLE`

La app indica envío correcto de la home y sin fallos. Bing Webmaster Tools no pudo verificarse por falta de sesión autenticada en el navegador accesible.

## Riesgos

`VERIFICADO PERO MEJORABLE`

- App log `Submitted` no equivale necesariamente a recepción visible en Bing Webmaster Tools.
- Bing puede tardar en reflejar datos.
- No se debe usar Manual submissions hasta tener al menos una comprobación de recepción o una decisión explícita.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se hicieron envíos manuales. No se modificó app, idiomas, tipos de contenido, API Key, tema, Liquid, robots, sitemap, `llms.txt`, URLs, handles, redirecciones, metadatos ni traducciones.

## Próximo lote recomendado

`MW-INDEXNOW-BING-WEBMASTER-RECEPTION-MANUAL-CHECK-013I4B`

Objetivo:

1. abrir Bing Webmaster Tools con sesión autenticada de Daniel;
2. revisar sección IndexNow / URL Submission / actividad reciente si está disponible;
3. comprobar si aparece la home o algún registro relacionado;
4. documentar resultado;
5. seguir sin usar Manual submissions salvo aprobación posterior.
