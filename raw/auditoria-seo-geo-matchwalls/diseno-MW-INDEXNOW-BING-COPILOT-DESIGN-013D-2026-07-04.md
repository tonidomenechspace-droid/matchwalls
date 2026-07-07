# Diseño MW-INDEXNOW-BING-COPILOT-DESIGN-013D — 2026-07-04

## Estado

`VERIFICADO Y CORRECTO`

Documento de diseño. No se ha modificado Shopify, LangShop, `robots.txt`, tema, paginas, redirecciones, handles, URLs, SEO fields, sitemaps, apps ni DNS/CDN.

## Objetivo

Diseñar una activacion segura de IndexNow para MatchWalls, orientada a:

- Bing.
- Edge.
- Copilot.
- Yahoo via Bing.
- buscadores participantes de IndexNow.

No se garantiza indexacion, ranking, trafico ni citas. IndexNow solo notifica altas, cambios y eliminaciones de URLs a motores participantes.

## Base verificada

`VERIFICADO PERO MEJORABLE`

Desde `MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B`:

- `robots.txt`: `200`.
- `sitemap.xml`: `200`.
- `Sitemap: https://www.matchwalls.com/sitemap.xml` presente en `robots.txt`.
- `bingbot` permitido para contenido publico por `User-agent: *`.
- `/indexnow.txt`: `404`; IndexNow no queda verificado.
- Sitemaps detectados: `29`.
- URLs publicas contadas en sitemaps: `7274`.
- Idiomas prioritarios: ES, EN, FR, DE, NL.
- IT/PT publicados pero fuera de prioridad activa salvo autorizacion expresa.
- Bloqueo independiente activo: `012O` escalado a Shopify Engineering/TMS; no enviar esas URLs como "resueltas" hasta que el storefront este estable.

## Reglas oficiales relevantes

`VERIFICADO Y CORRECTO`

Segun la documentacion oficial de IndexNow:

- Una URL enviada debe pertenecer al host que se esta notificando.
- La key debe tener entre 8 y 128 caracteres validos.
- Para probar propiedad, debe existir un archivo `.txt` con la key.
- Opcion recomendada: archivo de key en la raiz del host.
- Opcion alternativa: `keyLocation`, pero el alcance queda limitado por la ubicacion del archivo.
- Se pueden enviar hasta 10.000 URLs por POST.
- `200 OK` solo confirma recepcion; no garantiza indexacion.
- `202` indica URL recibida con validacion de key pendiente.
- `403` suele indicar key invalida o no encontrada.
- `422` suele indicar URL fuera del host o desajuste de protocolo/host.
- `429` indica demasiadas solicitudes o posible spam.

Fuente: https://www.indexnow.org/documentation

## Decision tecnica critica: key file

`REQUIERE DECISION HUMANA`

Para MatchWalls, el punto critico no es enviar URLs: es alojar correctamente la key.

### Opcion A — key en raiz del host

`RECOMENDADA SI ES VIABLE`

Ejemplo:

```txt
https://www.matchwalls.com/{indexnow-key}.txt
```

Contenido del archivo:

```txt
{indexnow-key}
```

Ventajas:

- Cubre todo el host `www.matchwalls.com`.
- Es la opcion recomendada por IndexNow.
- Evita problemas de alcance por carpeta.

Riesgo:

- Shopify normalmente no permite crear cualquier archivo arbitrario en la raiz del dominio desde una pagina normal.
- Hay que verificar si el tema, una app, Shopify, DNS/CDN o una regla externa pueden servir ese TXT exacto en raiz.
- No asumir que una pagina `/pages/...`, un asset de tema o una redireccion cumplen la verificacion.

Estado actual:

`NO ACCESIBLE`

No se ha comprobado aun una via segura para servir un TXT root real.

### Opcion B — `keyLocation` dentro del host

`NO RECOMENDADA PARA TODO EL SITE`

Ejemplo:

```txt
https://www.matchwalls.com/pages/indexnow-key
```

Problema:

- IndexNow indica que la ubicacion del archivo determina el conjunto de URLs permitidas.
- Si la key vive bajo `/pages/`, no sirve limpiamente para productos, colecciones, blogs y home.

Uso posible:

- Solo como prueba limitada si se quiere notificar un subconjunto bajo la misma ruta, pero no como solucion global para MatchWalls.

### Opcion C — CDN/edge/worker sirve la key en raiz

`PREFERIBLE SI SHOPIFY NO PERMITE ROOT TXT`

Ejemplo:

- DNS/CDN intercepta `https://www.matchwalls.com/{key}.txt`.
- Devuelve `200`, `Content-Type: text/plain; charset=utf-8`.
- Body exacto: la key.
- No toca Shopify ni el tema.

Ventajas:

- Cubre todo el host.
- Reversible.
- No depende de paginas Shopify.

Riesgos:

- Requiere acceso real a DNS/CDN/WAF.
- Debe respetar TLS, cache, headers y no romper rutas Shopify.
- Necesita aprobacion y QA tecnico.

### Opcion D — app Shopify IndexNow

`REQUIERE VALIDACION`

Posible si una app demuestra:

- que aloja o valida la key correctamente para todo el host;
- que envia solo URLs canonicas valiosas;
- que permite controlar exclusiones;
- que no envia filtros, carrito, samples noindex, redirecciones o URLs sin valor.

No instalar ni activar apps sin aprobacion.

## Politica de URLs a enviar

`VERIFICADO PERO MEJORABLE`

No se debe enviar masivamente todo el sitemap inicial.

IndexNow debe usarse para URLs:

- añadidas;
- modificadas;
- eliminadas;
- noindexadas;
- redirigidas o retiradas, cuando corresponda informar cambio.

### Incluir

`VERIFICADO Y CORRECTO`

Solo URLs que cumplan todo:

- URL canonica final.
- `https://www.matchwalls.com`.
- Respuesta publica `200`, salvo notificacion de eliminacion o retirada.
- No bloqueada por robots.
- Sin `noindex`.
- Sin query string.
- Sin `preview_theme_id`, `oseid`, filtros, sort, `ls`, tracking o variantes.
- Contenido visible, estable y valioso.
- Idioma correcto: ES, EN, FR, DE, NL.
- Cambiada realmente desde la ultima notificacion.

### Excluir

`VERIFICADO Y CORRECTO`

- Carrito, checkout, account, orders.
- `/admin`, `/services`, `/sf_*`.
- `/cdn/wpm/*.js`.
- `/recommendations/products`.
- URLs con filtros/sort/query/tracking.
- URLs noindex.
- URLs de prueba.
- URLs con 404/410 salvo evento de retirada planificado.
- URLs redirigidas si no son destino final.
- URLs afectadas por el bloqueo `012O` hasta que Shopify/TMS cierre la incidencia.
- Muestras confirmadas como noindex por la politica aprobada.
- Colecciones geograficas no priorizadas o en piloto noindex.
- IT/PT salvo lote especifico.

## Priorizacion inicial

`REQUIERE DECISION HUMANA`

Cuando la key este verificada, el primer piloto no debe superar 10–20 URLs.

### Piloto propuesto

Solo despues de un cambio real o una validacion segura:

1. Home ES.
2. Home EN.
3. Home FR.
4. Home DE.
5. Home NL.
6. Pagina pais España ES, solo cuando `012O` este estable.
7. Pagina pais Francia ES, solo cuando `012O` este estable.
8. Version EN de España, solo cuando `012O` este estable.
9. Version FR de Francia, solo cuando `012O` este estable.
10. Una guia o pagina informativa prioritaria que haya sido modificada realmente.

Mientras `012O` siga `INCOMPLETO`, no usar las landings España/Francia como piloto.

## Flujo operativo propuesto

`VERIFICADO Y CORRECTO`

1. Validar metodo de alojamiento de key.
2. Generar key unica y privada.
3. Publicar key file solo con aprobacion exacta.
4. Comprobar que `https://www.matchwalls.com/{key}.txt` devuelve:
   - `200`;
   - texto plano;
   - body exacto con la key;
   - sin redireccion dudosa;
   - accesible para Bingbot.
5. Crear lista de URLs piloto.
6. Validar cada URL piloto:
   - canonical;
   - status;
   - noindex;
   - robots;
   - idioma;
   - valor SEO/GEO;
   - no afectada por `012O`.
7. Enviar POST IndexNow con lote pequeño.
8. Registrar respuesta HTTP:
   - `200`, `202`, `400`, `403`, `422`, `429`.
9. Verificar en Bing Webmaster Tools cuando haya acceso.
10. No ampliar hasta piloto estable.

## Payload POST propuesto

`NO EJECUTAR`

Ejemplo conceptual:

```json
{
  "host": "www.matchwalls.com",
  "key": "{indexnow-key}",
  "urlList": [
    "https://www.matchwalls.com/",
    "https://www.matchwalls.com/en",
    "https://www.matchwalls.com/fr",
    "https://www.matchwalls.com/de",
    "https://www.matchwalls.com/nl"
  ]
}
```

Endpoint:

```txt
POST https://<searchengine>/indexnow
Content-Type: application/json; charset=utf-8
```

No se define endpoint final hasta decidir si se usara Bing, IndexNow genérico o herramienta/app validada.

## Triggers futuros

`VERIFICADO Y CORRECTO`

Enviar IndexNow solo cuando haya:

- nueva pagina publicada;
- producto principal nuevo o modificado;
- coleccion prioritaria modificada;
- guia/blog importante actualizado;
- cambio SEO/canonical importante;
- URL retirada, noindexada o redirigida;
- correccion multilingue relevante.

No enviar por:

- cambios de carrito/checkout;
- cambios de stock menor si no cambia contenido;
- cambios internos no publicos;
- query strings;
- filtros;
- pruebas;
- rechecks de QA;
- cambios todavia no estables por cache storefront.

## Cadencia

`VERIFICADO Y CORRECTO`

- Fase piloto: manual, 10–20 URLs maximo.
- Fase controlada: envio diario o por lote tras cambios aprobados.
- Fase automatizada: solo si existe app/script robusto con exclusiones.
- Limite tecnico oficial: hasta 10.000 URLs por POST, pero no usarlo como estrategia inicial.

## Relacion con Bing Webmaster Tools

`REQUIERE DECISION HUMANA`

IndexNow no sustituye Bing Webmaster Tools.

Se necesita:

- verificar MatchWalls en Bing Webmaster Tools;
- enviar sitemap;
- revisar indexacion;
- revisar AI/Copilot performance si esta disponible;
- revisar errores de rastreo;
- confirmar recepcion de IndexNow.

Lote recomendado:

`MW-BING-WEBMASTER-VERIFICATION-DIAG-013E`

## Relacion con Yahoo

`VERIFICADO PERO MEJORABLE`

Yahoo indica que la inclusion se gestiona via Bing.

Accion:

- tratar Yahoo como dependiente de Bing Webmaster/IndexNow salvo datos separados;
- no crear una estrategia Yahoo independiente ahora.

## Relacion con Copilot

`VERIFICADO PERO MEJORABLE`

Copilot depende del ecosistema Microsoft/Bing para descubrimiento y citas.

Accion:

- reforzar Bing Webmaster Tools;
- mantener sitemap canonico;
- evitar `NOARCHIVE` global en paginas que queremos que puedan citarse;
- no usar IndexNow para URLs debiles o no canonicas.

## Seguridad y reversion

`VERIFICADO Y CORRECTO`

Si se implementa key:

- registrar key location;
- registrar valor hash de la key, no exponerla en documentos compartidos si no es necesario;
- poder retirar key file;
- poder rotar key;
- poder pausar envios;
- poder eliminar app/script si falla;
- no tocar URLs ni contenido como parte de IndexNow.

## Lotes siguientes propuestos

1. `MW-INDEXNOW-KEY-HOSTING-DIAG-013D1`
   - Solo lectura/diagnostico.
   - Confirmar si Shopify, CDN, DNS o app puede servir `/{key}.txt` en raiz.

2. `MW-BING-WEBMASTER-VERIFICATION-DIAG-013E`
   - Verificacion manual/lectura.
   - Confirmar acceso real a Bing Webmaster Tools.

3. `MW-INDEXNOW-PILOT-PROPOSAL-013F`
   - Propuesta formal de piloto con 10–20 URLs maximo.
   - Sin ejecutar hasta aprobacion exacta.

4. `MW-INDEXNOW-PILOT-IMPLEMENTATION-013G`
   - Solo si key hosting esta resuelto y Daniel aprueba.
   - Ejecutar envio piloto y registrar respuestas.

## Estado final

`VERIFICADO Y CORRECTO`

IndexNow es recomendable para MatchWalls, pero no debe implementarse a ciegas. El bloqueo actual no es el protocolo, sino alojar correctamente la key en raiz o encontrar una alternativa validada que cubra todo `www.matchwalls.com`.
