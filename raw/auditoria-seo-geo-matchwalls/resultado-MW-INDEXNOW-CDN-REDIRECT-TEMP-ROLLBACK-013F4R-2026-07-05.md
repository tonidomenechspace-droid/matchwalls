# Resultado lote MW-INDEXNOW-CDN-REDIRECT-TEMP-ROLLBACK-013F4R

Fecha: 2026-07-05  
Lote aprobado: `APROBADO LOTE MW-INDEXNOW-CDN-REDIRECT-TEMP-ROLLBACK-013F4R`  
Estado final: `CORREGIDO Y VERIFICADO` para Shopify Admin y para la URL raíz de MatchWalls.  
Incidencia residual: `VERIFICADO PERO MEJORABLE` para caché directa CDN.

## Alcance ejecutado

Eliminar los recursos temporales creados durante la validación IndexNow `013F3`:

- redirect temporal:
  - `gid://shopify/UrlRedirect/1659100168568`
  - `/1fe8851103534006a2a9433fe8b56f2d.txt`
- archivo temporal:
  - `gid://shopify/GenericFile/66247836041592`
  - `1fe8851103534006a2a9433fe8b56f2d.txt`

## Precheck

`VERIFICADO Y CORRECTO`

Antes del rollback:

- el redirect existía en Shopify;
- el archivo existía en Shopify Files;
- el archivo estaba `READY`;
- el archivo tenía MIME `text/plain`;
- no había errores de archivo.

## Operaciones ejecutadas

`CORREGIDO Y VERIFICADO`

1. `urlRedirectDelete`
   - ID: `gid://shopify/UrlRedirect/1659100168568`
   - `userErrors`: `[]`
   - resultado: deletedUrlRedirectId devuelto correctamente
2. `fileDelete`
   - ID: `gid://shopify/GenericFile/66247836041592`
   - `userErrors`: `[]`
   - resultado: deletedFileIds devuelto correctamente

## Verificación Admin posterior

`CORREGIDO Y VERIFICADO`

Admin GraphQL posterior:

- `urlRedirect(id: "gid://shopify/UrlRedirect/1659100168568")` → `null`
- `node(id: "gid://shopify/GenericFile/66247836041592")` → `null`

Conclusión: los recursos ya no existen en Shopify Admin.

## Verificación pública posterior

`CORREGIDO Y VERIFICADO`

URL raíz de MatchWalls:

- `https://www.matchwalls.com/1fe8851103534006a2a9433fe8b56f2d.txt`
- HTTP `404`
- no contiene la key
- no sirve el archivo TXT

Conclusión: la key temporal ya no queda accesible desde `www.matchwalls.com`.

## Incidencia residual CDN

`VERIFICADO PERO MEJORABLE`

La URL directa CDN todavía responde:

- HTTP `200`
- `text/plain`
- cuerpo igual a la key

Interpretación:

- Shopify Admin ya no contiene el archivo.
- El acceso directo CDN puede estar retenido por caché temporal.
- La URL CDN ya no está enlazada desde `www.matchwalls.com` porque el redirect fue borrado.
- No debe usarse para producción IndexNow.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó:

- tema;
- Liquid;
- páginas;
- productos;
- colecciones;
- traducciones;
- LangShop;
- handles;
- robots.txt;
- sitemap.xml;
- DNS;
- Search Console;
- Bing Webmaster Tools;
- IndexNow;
- landings;
- muestras.

No se enviaron nuevas URLs a IndexNow.

## Evidencias

`VERIFICADO Y CORRECTO`

- `rollback-evidence-MW-INDEXNOW-CDN-REDIRECT-TEMP-ROLLBACK-013F4R-2026-07-05.csv`

## Conclusión

`CORREGIDO Y VERIFICADO`

El rollback operativo queda completado:

- Shopify Admin limpio;
- root de MatchWalls limpio;
- no queda key funcional bajo `www.matchwalls.com`.

La vía CDN redirect queda descartada como solución productiva por el resultado del lote `013F4`.

## Próximo lote recomendado

`REQUIERE DECISION HUMANA`

`MW-INDEXNOW-STABLE-IMPLEMENTATION-OPTIONS-013G`

Objetivo: evaluar alternativas estables para IndexNow sin depender de URL Redirect a CDN:

1. app IndexNow de Shopify validada;
2. endpoint/proxy/CDN bajo `www.matchwalls.com` que sirva `200 text/plain`;
3. solución externa controlada con verificación de host, solo si respeta Shopify, SEO internacional y seguridad.
