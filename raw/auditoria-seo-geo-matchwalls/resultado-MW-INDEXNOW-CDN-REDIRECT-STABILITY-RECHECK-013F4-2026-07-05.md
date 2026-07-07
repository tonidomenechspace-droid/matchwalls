# Resultado lote MW-INDEXNOW-CDN-REDIRECT-STABILITY-RECHECK-013F4

Fecha: 2026-07-05  
Tipo: solo lectura  
Estado final: `INCORRECTO` para uso productivo de la vía raíz `www.matchwalls.com/{key}.txt` mediante redirect a Shopify CDN.  
Estado parcial: `VERIFICADO Y CORRECTO` para el archivo en Shopify Files/CDN y para la existencia del redirect en Shopify Admin.

## Alcance

Lote solicitado: `MW-INDEXNOW-CDN-REDIRECT-STABILITY-RECHECK-013F4`

Objetivo: revalidar con baja frecuencia si la key temporal creada en `013F3` sigue sirviendo de forma estable desde:

- `https://www.matchwalls.com/1fe8851103534006a2a9433fe8b56f2d.txt`

sin ejecutar cambios en Shopify ni enviar nuevas URLs a IndexNow.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `resultado-MW-INDEXNOW-CDN-REDIRECT-MANUAL-VALIDATION-013F3-2026-07-05.md`
- `registro-cambios-ejecutados.md`

## Estado real comprobado en Shopify

`VERIFICADO Y CORRECTO`

Consulta Admin GraphQL de solo lectura:

- Redirect:
  - ID: `gid://shopify/UrlRedirect/1659100168568`
  - Path: `/1fe8851103534006a2a9433fe8b56f2d.txt`
  - Target: `https://cdn.shopify.com/s/files/1/0677/5308/3107/files/1fe8851103534006a2a9433fe8b56f2d.txt?v=1783238351`
- Archivo Shopify Files:
  - ID: `gid://shopify/GenericFile/66247836041592`
  - Estado: `READY`
  - URL: `https://cdn.shopify.com/s/files/1/0677/5308/3107/files/1fe8851103534006a2a9433fe8b56f2d.txt?v=1783238351`
  - MIME: `text/plain`
  - Tamaño: 33 bytes
  - Errores: ninguno

Conclusión: el recurso y el redirect existen en Shopify y están configurados como se dejaron en `013F3`.

## Recheck público HTTP

`INCORRECTO`

Resultados con pausas entre comprobaciones:

- CDN directo:
  - HTTP `200`
  - `text/plain`
  - cuerpo exacto igual a la key
- Ruta raíz con user-agent Chrome, sin seguir redirect:
  - HTTP `429`
  - no devuelve `301`
  - no llega al CDN
- Ruta raíz con user-agent Chrome, siguiendo redirect:
  - HTTP `429`
  - no llega al CDN
- Ruta raíz con user-agent Bingbot simulado, siguiendo redirect:
  - HTTP `429`
  - no llega al CDN

## Conclusión técnica

`INCORRECTO`

La vía `Shopify URL Redirect -> Shopify CDN` no es estable actualmente para alojar una key IndexNow desde `www.matchwalls.com`.

Aunque el CDN sirve el TXT correctamente y Shopify conserva el redirect, la ruta raíz pública responde `429` antes de redirigir. Para IndexNow y Bing/Copilot esto es un riesgo: el bot puede no poder recuperar la key cuando quiera verificar propiedad.

## Impacto

`RIESGO CRITICO`

No se debe:

- convertir esta key temporal en producción;
- enviar lotes masivos de URLs;
- automatizar IndexNow con esta vía;
- incluir landings, productos o colecciones hasta resolver el alojamiento estable de la key.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó:

- Shopify Files;
- redirects;
- tema;
- Liquid;
- páginas;
- productos;
- colecciones;
- traducciones;
- LangShop;
- robots.txt;
- sitemap.xml;
- DNS;
- Search Console;
- Bing Webmaster Tools;
- IndexNow.

No se envió ninguna nueva URL a IndexNow.

## Decisión recomendada

`REQUIERE DECISION HUMANA`

Recomiendo revertir la key temporal y el redirect porque no deben quedar como infraestructura SEO/GEO activa si la ruta raíz responde `429`.

Lote exacto recomendado:

`MW-INDEXNOW-CDN-REDIRECT-TEMP-ROLLBACK-013F4R`

Alcance:

1. borrar redirect temporal:
   - `gid://shopify/UrlRedirect/1659100168568`
2. borrar archivo temporal:
   - `gid://shopify/GenericFile/66247836041592`
3. verificar que la URL temporal ya no sirve la key.

Después del rollback, la alternativa correcta es estudiar otra vía de alojamiento de key estable:

- app IndexNow validada para Shopify;
- proxy/CDN/DNS externo que permita servir `/{key}.txt` como `200 text/plain`;
- endpoint controlado fuera de Shopify, solo si puede servir bajo `www.matchwalls.com`.

## Evidencias generadas

`VERIFICADO Y CORRECTO`

- `admin-state-MW-INDEXNOW-CDN-REDIRECT-STABILITY-RECHECK-013F4-2026-07-05.csv`
- `stability-recheck-MW-INDEXNOW-CDN-REDIRECT-STABILITY-RECHECK-013F4-2026-07-05.csv`

## Estado de cierre

`INCORRECTO`

Lote cerrado sin cambios. La vía queda descartada para producción hasta nueva decisión técnica.
