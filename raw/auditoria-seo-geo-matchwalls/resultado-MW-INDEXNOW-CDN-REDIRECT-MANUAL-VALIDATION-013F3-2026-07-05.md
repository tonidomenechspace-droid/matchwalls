# Resultado lote MW-INDEXNOW-CDN-REDIRECT-MANUAL-VALIDATION-013F3

Fecha: 2026-07-05  
Estado final: `VERIFICADO PERO MEJORABLE` para la vía CDN + redirect.  
Estado operativo: `REQUIERE DECISION HUMANA` para decidir si esta clave temporal se mantiene como producción, se rota o se elimina.

## Alcance aprobado

`APROBADO LOTE MW-INDEXNOW-CDN-REDIRECT-MANUAL-VALIDATION-013F3`

Validar de forma controlada si MatchWalls puede alojar una key IndexNow usando:

- archivo `.txt` en Shopify Files;
- redirect raíz desde `www.matchwalls.com`;
- `keyLocation` apuntando a la URL raíz de MatchWalls;
- envío mínimo a IndexNow de una sola URL segura: `https://www.matchwalls.com/`.

## Recursos creados

`VERIFICADO Y CORRECTO`

- Archivo Shopify Files:
  - ID: `gid://shopify/GenericFile/66247836041592`
  - Estado: `READY`
  - MIME: `text/plain`
  - Tamaño: 33 bytes
  - URL CDN: `https://cdn.shopify.com/s/files/1/0677/5308/3107/files/1fe8851103534006a2a9433fe8b56f2d.txt?v=1783238351`
- Redirect Shopify:
  - ID: `gid://shopify/UrlRedirect/1659100168568`
  - From: `/1fe8851103534006a2a9433fe8b56f2d.txt`
  - To: URL CDN del archivo TXT
- Key temporal:
  - Mask: `1fe88511...6f2d`
  - SHA-256 local del archivo: `f706214baac32783674b4184582546d0a333d7a1a11c2fa324ca089ab55a2dd1`

## Validación pública HTTP

`VERIFICADO PERO MEJORABLE`

- CDN directo:
  - HTTP `200`
  - `content-type`: `text/plain`
  - cuerpo: coincide exactamente con la key
- Root con user-agent Chrome:
  - sin seguir redirect: HTTP `301` hacia CDN
  - siguiendo redirect: HTTP `200`, `text/plain`, cuerpo exacto
- Root con user-agent Bingbot:
  - sin seguir redirect: HTTP `301` hacia CDN
  - siguiendo redirect: HTTP `200`, `text/plain`, cuerpo exacto

Incidencia menor:

- Una primera prueba con `curl` sin user-agent de navegador devolvió `503`. Se repitió con user-agent Chrome y Bingbot, que son las evidencias válidas para este lote.

Post-check posterior:

- Después de varias comprobaciones, la URL raíz temporal empezó a devolver HTTP `429` desde la IP local tanto con user-agent Bingbot simulado como con user-agent Chrome.
- Interpretación: posible rate limit / anti-bot / protección de storefront tras pruebas repetidas.
- Esto no invalida el `200` ya recibido de IndexNow, pero impide considerar la vía lista para producción masiva sin un lote adicional de estabilidad.

## Validación IndexNow

`VERIFICADO Y CORRECTO`

Prueba GET:

- Endpoint: `https://api.indexnow.org/indexnow`
- URL enviada: `https://www.matchwalls.com/`
- `keyLocation`: `https://www.matchwalls.com/1fe8851103534006a2a9433fe8b56f2d.txt`
- Respuesta: HTTP `200`

Prueba POST estricta:

- Endpoint: `https://api.indexnow.org/IndexNow`
- Content-Type: `application/json; charset=utf-8`
- Payload leído desde archivo JSON UTF-8
- URL enviada: `https://www.matchwalls.com/`
- Respuesta: HTTP `200`

Incidencia corregida:

- Un primer POST generado como string directo devolvió HTTP `400 InvalidRequestParameters`.
- La repetición con archivo JSON estricto y endpoint `/IndexNow` devolvió HTTP `200`.
- Conclusión: el fallo fue de formato de envío, no de la clave, redirect ni `keyLocation`.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó:

- tema Shopify;
- Liquid;
- páginas;
- productos;
- colecciones;
- traducciones;
- LangShop;
- handles;
- URLs;
- canonical/hreflang;
- robots.txt;
- sitemap.xml;
- DNS;
- GA4/GTM/GSC/Merchant Center/Ads;
- landings España/Francia afectadas por 012O;
- muestras noindex;
- IT/PT.

## Riesgos pendientes

`REQUIERE DECISION HUMANA`

La vía fue aceptada por IndexNow, pero la URL raíz temporal mostró `429` en post-check local tras repetición de pruebas. Además, la clave creada en este lote nació como temporal. Hay que decidir:

1. mantener esta key como producción;
2. rotar a una key definitiva y repetir validación mínima;
3. eliminar el redirect y el archivo temporal.

No se recomienda enviar lotes masivos de URLs hasta tomar esta decisión y definir la política de URLs permitidas.

No se recomienda usar esta vía en producción hasta completar un recheck de estabilidad con baja frecuencia y, si procede, revisar WAF/CDN/Shopify para no bloquear validaciones de crawlers reales.

## Reversión

`VERIFICADO Y CORRECTO`

Si Daniel decide revertir:

1. borrar redirect:
   - `urlRedirectDelete(id: "gid://shopify/UrlRedirect/1659100168568")`
2. borrar archivo:
   - `fileDelete(fileIds: ["gid://shopify/GenericFile/66247836041592"])`
3. verificar:
   - `https://www.matchwalls.com/1fe8851103534006a2a9433fe8b56f2d.txt` ya no debe servir la key.

## Evidencias

`VERIFICADO Y CORRECTO`

- `admin-operations-MW-INDEXNOW-CDN-REDIRECT-MANUAL-VALIDATION-013F3-2026-07-05.csv`
- `http-validation-MW-INDEXNOW-CDN-REDIRECT-MANUAL-VALIDATION-013F3-2026-07-05.csv`
- `indexnow-response-MW-INDEXNOW-CDN-REDIRECT-MANUAL-VALIDATION-013F3-2026-07-05.csv`
- `indexnow-get-response-MW-INDEXNOW-CDN-REDIRECT-MANUAL-VALIDATION-013F3-2026-07-05.csv`
- `indexnow-post-strict-response-MW-INDEXNOW-CDN-REDIRECT-MANUAL-VALIDATION-013F3-2026-07-05.csv`
- `postcheck-rate-limit-MW-INDEXNOW-CDN-REDIRECT-MANUAL-VALIDATION-013F3-2026-07-05.csv`

## Próximo lote recomendado

`REQUIERE DECISION HUMANA`

`MW-INDEXNOW-CDN-REDIRECT-STABILITY-RECHECK-013F4`

Alcance propuesto: esperar una ventana sin rate-limit, revalidar la URL raíz temporal con baja frecuencia, comprobar si sigue dando `301 -> 200 text/plain`, y solo después decidir si se mantiene/rota la key y se prepara la whitelist inicial de URLs canónicas y valiosas.
