# Diagnóstico MW-BING-WEBMASTER-VERIFICATION-DIAG-013E — 2026-07-04

## Estado

`INCOMPLETO`

Lote de solo lectura. No se ha modificado Shopify, LangShop, tema, páginas, `robots.txt`, sitemaps, DNS, CDN, Bing Webmaster Tools, IndexNow, URLs, handles, SEO fields ni mercados.

El estado queda `INCOMPLETO` porque la parte pública se ha comprobado, pero el acceso real a Bing Webmaster Tools no está disponible en este lote. No se puede afirmar que la propiedad esté verificada, que el sitemap esté enviado o que existan datos de Bing/Copilot sin ver la cuenta.

## Objetivo

Confirmar qué falta para que MatchWalls tenga una capa Bing / Edge / Copilot / Yahoo vía Bing correctamente controlada:

- Propiedad verificada en Bing Webmaster Tools.
- Sitemap canónico enviado.
- Estado de rastreo/indexación visible.
- Datos de rendimiento Bing.
- Datos AI Performance / Copilot si están disponibles en la cuenta.
- Base preparada para IndexNow cuando se resuelva el alojamiento de key.

## Documentos revisados

`VERIFICADO Y CORRECTO`

- `registro-cambios-ejecutados.md`
- `diseno-MW-INDEXNOW-BING-COPILOT-DESIGN-013D-2026-07-04.md`
- `diagnostico-MW-INDEXNOW-KEY-HOSTING-DIAG-013D1-2026-07-04.md`
- `diagnostico-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.md`
- `robots-matrix-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.csv`
- `sitemap-summary-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.csv`
- `cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`

## Estado público comprobado

`VERIFICADO PERO MEJORABLE`

Desde 013B/013D1:

- `robots.txt`: `200`.
- `sitemap.xml`: `200`.
- `Sitemap: https://www.matchwalls.com/sitemap.xml` presente en robots según diagnóstico 013D.
- `agents.md`: `200`.
- `llms.txt`: `200` en recheck 013D1.
- `/.well-known/ucp`: `200`.
- `/indexnow.txt`: `404`.
- Sitemaps detectados: 29.
- URLs contadas en sitemaps: 7274.

### Robots para Bingbot

`VERIFICADO Y CORRECTO`

La matriz 013B indica que `bingbot` puede rastrear las URLs públicas principales:

- `/`
- `/products/custom-file-uploader`
- `/pages/papel-pintado-espana`
- `/en/pages/spain-wallpaper`
- `/fr/pages/papier-peint-en-france`

Y bloquea correctamente rutas privadas o de bajo valor:

- `/cart/`
- `/checkout`
- `/cdn/wpm/*.js`
- `/recommendations/products`
- colecciones con `sort_by`
- patrones con `+`

### Prueba Bingbot simulada

`DECLARADO PERO NO VERIFICADO`

Se realizó una prueba pública ligera con user-agent de Bingbot simulado desde la sesión local. Devolvió respuestas `429` y una respuesta `500` para algunas rutas. Esto no se usa como prueba de bloqueo a Bing real, porque:

- no era un Bingbot verificado por IP oficial;
- Shopify/CDN/WAF puede tratar bots simulados como tráfico no confiable;
- el dato válido debe obtenerse desde Bing Webmaster Tools o logs reales.

Recomendación: revisar en Bing Webmaster Tools si Bingbot real reporta errores de rastreo, `blocked`, `5xx`, `429` o problemas de fetch.

## Estado de Bing Webmaster Tools

`NO ACCESIBLE`

No se ha accedido a la cuenta real de Bing Webmaster Tools durante este lote. Por tanto, quedan sin verificar:

- Si existe propiedad para `https://www.matchwalls.com/`.
- Si existe propiedad de dominio `matchwalls.com`.
- Método de verificación usado.
- Si está importada desde Google Search Console.
- Si el sitemap `https://www.matchwalls.com/sitemap.xml` está enviado.
- Estado del sitemap: success/error/pending.
- Última fecha de lectura del sitemap.
- URLs descubiertas por Bing.
- Errores de rastreo.
- Indexación.
- Backlinks.
- SEO reports.
- IndexNow tab / actividad.
- AI Performance / Copilot citations si aparece en la cuenta.

## Fuentes oficiales consultadas

`VERIFICADO Y CORRECTO`

### Bing Webmaster Tools + GSC

Bing permite importar sitios verificados desde Google Search Console y también sus sitemaps. La publicación oficial indica que la importación puede verificar automáticamente los sitios seleccionados, y que los datos de tráfico pueden tardar hasta 48 horas en aparecer tras la verificación.

Fuente: https://blogs.bing.com/webmaster/september-2019/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools

### IndexNow en Bing

Bing indica que IndexNow puede comprobarse desde Bing Webmaster Tools y que el flujo requiere:

1. generar key;
2. alojar key;
3. enviar URLs;
4. verificar recepción en Bing Webmaster Tools.

Bing también recuerda que IndexNow no garantiza rastreo ni indexación.

Fuente: https://www.bing.com/indexnow/getstarted

### AI Performance / Copilot

Bing anunció en febrero de 2026 una vista pública previa de AI Performance en Bing Webmaster Tools para ver citas en Microsoft Copilot, resúmenes generados por IA en Bing e integraciones seleccionadas. La disponibilidad exacta debe comprobarse dentro de la cuenta.

Fuente: https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview

## Checklist manual para Daniel

`REQUIERE DECISION HUMANA`

Abrir: https://www.bing.com/webmasters/

Comprobar y responder con estos campos:

```txt
CONFIRMADO 013E BING WEBMASTER:
Cuenta abierta: sí/no
Propiedad matchwalls.com existe: sí/no
Tipo de propiedad: dominio / URL prefix / importada GSC / no lo sé
URL exacta de propiedad visible: [valor exacto]
Estado verificación: verificada / pendiente / error / no visible
Método verificación: importación GSC / DNS TXT / meta tag / XML file / otro / no visible
Sitemap enviado: sí/no
Sitemap exacto: [valor exacto]
Estado sitemap: success / pending / error / no visible
Última lectura sitemap: [fecha o no visible]
URLs descubiertas/indexadas visibles: [número o no visible]
Errores rastreo visibles: sí/no
IndexNow tab visible: sí/no
Actividad IndexNow visible: sí/no
AI Performance/Copilot visible: sí/no
Datos AI Performance: sí/no/no visible
Captura disponible: sí/no
```

## Recomendación de método de verificación

`VERIFICADO PERO MEJORABLE`

Orden recomendado:

1. Importar desde Google Search Console si MatchWalls ya está verificado en GSC.
   - Es el método menos invasivo.
   - No requiere tocar Shopify, DNS ni tema.
   - Puede importar sitemaps.

2. Si no se puede importar desde GSC, usar DNS TXT.
   - Requiere acceso DNS y aprobación expresa.
   - No toca el tema ni el storefront.

3. Evitar XML file root si Shopify no puede alojarlo en raíz.

4. Evitar meta tag en `theme.liquid` salvo lote específico, porque tocaría tema publicado.

## Decisión técnica

`REQUIERE DECISION HUMANA`

No pasar aún a IndexNow piloto ni a cambios de robots.

Antes hay que confirmar:

- propiedad Bing Webmaster verificada;
- sitemap enviado y leído;
- si el panel IndexNow está disponible;
- si AI Performance aparece para la cuenta;
- si hay errores de rastreo reales de Bingbot.

## Siguiente lote recomendado

`MW-BING-WEBMASTER-MANUAL-CONFIRMATION-013E1`

Lote manual/asistido para que Daniel abra Bing Webmaster Tools y confirme los campos del checklist. Sin cambios.

Después, según resultado:

- Si Bing está verificado y sitemap OK: `MW-BING-WEBMASTER-SITEMAP-STATUS-QA-013E2`.
- Si no está verificado: `MW-BING-WEBMASTER-GSC-IMPORT-OR-DNS-PROPOSAL-013E3`.
- Si IndexNow aparece disponible pero sin key: mantener dependencia `MW-INDEXNOW-SHOPIFY-ROOT-KEY-SUPPORT-QUESTION-013D2`.

## Estado final

`INCOMPLETO`

La web tiene base pública suficiente para Bing —robots, sitemap, agentes y llms accesibles—, pero Bing Webmaster Tools no está verificado en este lote porque no hay acceso directo a la cuenta. El siguiente paso profesional no es escribir nada: es confirmar la propiedad y el estado del sitemap dentro de Bing Webmaster Tools.
