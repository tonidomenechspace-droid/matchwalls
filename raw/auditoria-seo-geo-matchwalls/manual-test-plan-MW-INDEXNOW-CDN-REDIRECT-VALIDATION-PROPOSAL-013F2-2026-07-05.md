# Plan manual de validación IndexNow vía Shopify Files + URL Redirect — 013F2

Fecha: 2026-07-05

## Estado

`REQUIERE DECISION HUMANA`

Este documento es un plan. No se ha ejecutado. No contiene una key real.

## Objetivo

Validar si el workaround propuesto por Sidekick —subir `{key}.txt` a Shopify Files y crear un redirect desde `https://www.matchwalls.com/{key}.txt` hacia el CDN— es aceptado por IndexNow/Bing como prueba de propiedad.

## Lo que NO se debe hacer en 013F2

`VERIFICADO Y CORRECTO`

- No generar key real.
- No subir archivo a Shopify Files.
- No crear URL redirect.
- No enviar URLs a IndexNow.
- No tocar `robots.txt`, `sitemap.xml`, tema, DNS, páginas, productos, colecciones, LangShop ni Bing Webmaster.

## Preparación del siguiente lote, si Daniel aprueba

Lote propuesto:

`MW-INDEXNOW-CDN-REDIRECT-MANUAL-VALIDATION-013F3`

### Paso 1 — crear key temporal

Generar una key temporal de 32 caracteres, alfanumérica simple, sin espacios.

Ejemplo de formato —no usar este literal—:

```txt
0123456789abcdef0123456789abcdef
```

Archivo local:

```txt
{key}.txt
```

Contenido exacto:

```txt
{key}
```

Requisitos:

- UTF-8.
- Sin HTML.
- Sin espacios antes/después.
- Preferiblemente sin BOM.
- Nueva línea final aceptable, pero idealmente body exacto.

### Paso 2 — subir a Shopify Files

Ruta manual:

```txt
Shopify Admin > Content > Files > Upload files
```

Resultado esperado:

```txt
https://cdn.shopify.com/.../{key}.txt
```

Validar CDN antes del redirect:

```txt
GET CDN_URL
```

Debe devolver:

- HTTP 200.
- `Content-Type` compatible con texto plano.
- body exacto: `{key}`.

### Paso 3 — crear URL redirect temporal

Ruta manual:

```txt
Shopify Admin > Content > Menus > URL redirects > Create URL redirect
```

Campos:

```txt
Redirect from: /{key}.txt
Redirect to: CDN_URL
```

No usar paths genéricos como `/indexnow.txt`.

### Paso 4 — validación HTTP pública

Validar sin seguir redirect:

```txt
GET https://www.matchwalls.com/{key}.txt
```

Resultado esperado:

- 301/302 hacia CDN URL.

Validar siguiendo redirect:

```txt
GET -L https://www.matchwalls.com/{key}.txt
```

Resultado esperado:

- HTTP final 200.
- body exacto `{key}`.
- sin HTML.
- tipo texto.

Repetir con user-agent tipo Bingbot:

```txt
Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)
```

### Paso 5 — validación IndexNow mínima

Solo si los pasos HTTP pasan.

Enviar un único POST a:

```txt
https://api.indexnow.org/indexnow
```

Payload propuesto:

```json
{
  "host": "www.matchwalls.com",
  "key": "{key}",
  "keyLocation": "https://www.matchwalls.com/{key}.txt",
  "urlList": [
    "https://www.matchwalls.com/"
  ]
}
```

Motivo:

- `keyLocation` se mantiene en el host `www.matchwalls.com`.
- No se usa el CDN URL directamente como keyLocation.
- Solo se notifica la home, no sitemap, no landings, no productos.

Interpretación:

- `200`: recibido correctamente.
- `202`: recibido, validación de key pendiente.
- `403`: key inválida/no encontrada.
- `422`: URL/host/keyLocation no encajan.
- `400`: formato incorrecto.
- `429`: demasiadas solicitudes; detener.

### Paso 6 — Bing Webmaster

Si IndexNow responde `200` o `202`, revisar después en Bing Webmaster:

```txt
Bing Webmaster Tools > matchwalls.com > IndexNow
```

No solicitar indexación masiva.

## Criterio de éxito

`VERIFICADO Y CORRECTO` solo si se cumple todo:

1. CDN URL devuelve body exacto.
2. Root URL `/KEY.txt` redirige correctamente.
3. Root URL siguiendo redirect devuelve body exacto.
4. Bingbot simulado puede acceder.
5. IndexNow devuelve `200` o `202`.
6. Bing Webmaster refleja recepción o no muestra errores bloqueantes.

## Criterio de fallo

`INCORRECTO` si ocurre cualquiera:

- Shopify no permite redirect a CDN externo.
- CDN no devuelve texto plano/body exacto.
- Root URL devuelve HTML o 404.
- IndexNow devuelve `403`, `422` o `400`.
- Bing Webmaster no reconoce la key.

## Rollback obligatorio

Si falla o si se decide no seguir:

1. Eliminar URL redirect `/{key}.txt`.
2. Eliminar archivo `{key}.txt` de Shopify Files.
3. Comprobar que `https://www.matchwalls.com/{key}.txt` vuelve a 404.
4. No reutilizar esa key para producción.

## Decisión posterior

Si la prueba funciona, no se convierte automáticamente en producción.

Siguiente lote posterior:

`MW-INDEXNOW-PRODUCTION-KEY-AND-PILOT-URLS-PROPOSAL-013F4`

Alcance:

- decidir si se conserva o rota la key;
- preparar lista piloto de URLs;
- excluir muestras noindex, landings 012O, IT/PT, filtros, redirecciones y URLs sin valor;
- definir logs y cadencia.
