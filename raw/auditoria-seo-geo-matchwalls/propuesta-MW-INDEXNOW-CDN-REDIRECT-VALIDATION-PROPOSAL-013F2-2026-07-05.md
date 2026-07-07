# Propuesta MW-INDEXNOW-CDN-REDIRECT-VALIDATION-PROPOSAL-013F2

Fecha: 2026-07-05

## Estado final

`VERIFICADO PERO MEJORABLE`

Lote de propuesta y diseño de validación. No se ha modificado Shopify, no se ha creado key, no se ha subido archivo, no se ha creado redirect y no se ha enviado ninguna URL a IndexNow.

## Alcance aprobado

`APROBADO LOTE MW-INDEXNOW-CDN-REDIRECT-VALIDATION-PROPOSAL-013F2`

Objetivo: evaluar si el workaround `Shopify Files + URL redirect` puede validarse de forma segura para IndexNow/Bing/Copilot antes de cualquier implementación.

## Documentos y evidencias revisadas

`VERIFICADO Y CORRECTO`

- `readiness-MW-INDEXNOW-BING-COPILOT-IMPLEMENTATION-READINESS-013F-2026-07-05.md`
- `diagnostico-MW-INDEXNOW-KEY-HOSTING-DIAG-013D1-2026-07-04.md`
- `readiness-matrix-MW-INDEXNOW-BING-COPILOT-IMPLEMENTATION-READINESS-013F-2026-07-05.csv`
- Respuesta de Sidekick facilitada por Daniel.

## Fuentes oficiales contrastadas

`VERIFICADO Y CORRECTO`

IndexNow:

- La key debe estar entre 8 y 128 caracteres válidos.
- Para probar propiedad se debe alojar un archivo de texto dentro del host.
- La opción recomendada es root: `https://www.example.com/{key}.txt`.
- También existe `keyLocation`, pero la ubicación limita las URLs válidas si no está en raíz.
- `200 OK` solo confirma recepción; no garantiza indexación.

Fuentes:

- `https://www.indexnow.org/documentation`
- `https://www.bing.com/indexnow/getstarted`

Shopify:

- Shopify Files permite subir archivos públicos y usarlos desde URLs CDN.
- Shopify advierte que, si un tercero pide subir archivos a la carpeta raíz, normalmente se deben usar meta tags; esto no resuelve IndexNow, porque IndexNow necesita key file.
- Shopify URL Redirects permite crear redirects.
- Shopify Flow documenta que el target de un redirect puede ser una URL interna o externa.
- Shopify documenta rutas root especiales como `robots.txt`, pero no un root TXT arbitrario genérico.

Fuentes:

- `https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads`
- `https://help.shopify.com/en/manual/shopify-admin/productivity-tools/rich-text-editor`
- `https://help.shopify.com/en/manual/online-store/menus-and-links/url-redirect`
- `https://help.shopify.com/en/manual/shopify-flow/reference/actions/create-redirect-url`
- `https://shopify.dev/docs/storefronts/themes/architecture/templates/robots-txt-liquid`

## Evaluación de la respuesta de Sidekick

`DECLARADO PERO NO VERIFICADO`

Sidekick afirma:

- Shopify no soporta nativamente un `.txt` arbitrario en root.
- Propone subir el `.txt` a Shopify Files y redirigir `/{key}.txt` hacia el CDN.

La primera parte coincide con la evidencia documental previa. La segunda parte es una hipótesis operativa, no una validación IndexNow.

## Decisión técnica de Codex

`REQUIERE DECISION HUMANA`

El workaround merece una prueba controlada, pero no debe adoptarse directamente.

Motivo:

- El root path de MatchWalls devolvería probablemente un `301` hacia `cdn.shopify.com`, no un `200` directo.
- IndexNow recomienda key root dentro del host.
- No hay garantía en la especificación de que un redirect hacia un host CDN externo sea aceptado como prueba de propiedad.
- Usar `keyLocation` directo con `cdn.shopify.com` no es recomendable porque la keyLocation dejaría de estar dentro de `www.matchwalls.com`.

## Arquitectura de prueba recomendada

`VERIFICADO PERO MEJORABLE`

Probar con key temporal y path único:

```txt
https://www.matchwalls.com/{temporary-key}.txt
```

que redirige a:

```txt
https://cdn.shopify.com/.../{temporary-key}.txt
```

En el payload IndexNow, si se llega a probar, usar:

```json
{
  "host": "www.matchwalls.com",
  "key": "{temporary-key}",
  "keyLocation": "https://www.matchwalls.com/{temporary-key}.txt",
  "urlList": [
    "https://www.matchwalls.com/"
  ]
}
```

No usar:

```json
"keyLocation": "https://cdn.shopify.com/..."
```

## Por qué solo la home

`VERIFICADO Y CORRECTO`

Si se aprueba una validación real, el POST mínimo debe contener solo:

```txt
https://www.matchwalls.com/
```

No enviar:

- sitemap completo;
- landings España/Francia afectadas por `012O`;
- muestras noindex;
- IT/PT;
- filtros;
- URLs con query;
- productos o colecciones sin revisión previa.

## Resultado esperado de una prueba real

`REQUIERE DECISION HUMANA`

El workaround solo puede considerarse viable si:

1. `GET CDN_URL` devuelve `200` y body exacto.
2. `GET https://www.matchwalls.com/{key}.txt` sin seguir redirect devuelve `301/302` hacia CDN.
3. `GET -L https://www.matchwalls.com/{key}.txt` devuelve `200` final y body exacto.
4. Bingbot simulado accede igual.
5. IndexNow responde `200` o `202` usando `keyLocation` en `www.matchwalls.com`.

Si IndexNow devuelve `403`, `422` o `400`, la vía se descarta.

## Riesgo principal

`RIESGO CRITICO`

El riesgo no es romper la web, porque el path sería único y reversible. El riesgo es creer que IndexNow está activo cuando solo hemos creado un redirect que los validadores no aceptan.

Por eso el criterio de éxito depende de la respuesta de IndexNow/Bing, no de que el navegador abra el archivo.

## Rollback

`VERIFICADO Y CORRECTO`

Si se ejecuta una prueba posterior:

1. Eliminar redirect `/{temporary-key}.txt`.
2. Eliminar archivo de Shopify Files.
3. Verificar que `https://www.matchwalls.com/{temporary-key}.txt` vuelve a `404`.
4. No reutilizar la key temporal.

## Siguiente lote exacto

`REQUIERE DECISION HUMANA`

Para ejecutar la prueba controlada:

`MW-INDEXNOW-CDN-REDIRECT-MANUAL-VALIDATION-013F3`

Alcance:

- generar una key temporal;
- crear archivo TXT local;
- subirlo a Shopify Files;
- crear redirect temporal;
- validar HTTP/CDN/Bingbot;
- si pasa, enviar un único POST IndexNow con la home;
- registrar respuesta;
- eliminar o mantener según resultado y decisión.

Este lote sí implica cambios públicos reversibles en Shopify y una notificación externa mínima si llega al POST. Requiere aprobación exacta.

## Evidencias generadas

`VERIFICADO Y CORRECTO`

- `propuesta-MW-INDEXNOW-CDN-REDIRECT-VALIDATION-PROPOSAL-013F2-2026-07-05.md`
- `validation-matrix-MW-INDEXNOW-CDN-REDIRECT-VALIDATION-PROPOSAL-013F2-2026-07-05.csv`
- `manual-test-plan-MW-INDEXNOW-CDN-REDIRECT-VALIDATION-PROPOSAL-013F2-2026-07-05.md`
