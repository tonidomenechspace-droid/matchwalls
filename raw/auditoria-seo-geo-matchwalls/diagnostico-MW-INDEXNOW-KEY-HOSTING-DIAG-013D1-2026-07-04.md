# Diagnóstico MW-INDEXNOW-KEY-HOSTING-DIAG-013D1 — 2026-07-04

## Estado

`VERIFICADO PERO MEJORABLE`

Lote de solo lectura. No se ha modificado Shopify, LangShop, tema, `robots.txt`, sitemaps, DNS, CDN, Bing Webmaster Tools, páginas, handles, URLs, SEO fields ni mercados.

## Objetivo del lote

Determinar si MatchWalls puede alojar una clave IndexNow verificable para `www.matchwalls.com` antes de preparar cualquier envío a Bing / Edge / Copilot / Yahoo vía Bing.

El objetivo de este lote no es activar IndexNow. Es evitar una implementación falsa o incompleta.

## Documentos revisados

`VERIFICADO Y CORRECTO`

- `registro-cambios-ejecutados.md`
- `diseno-MW-INDEXNOW-BING-COPILOT-DESIGN-013D-2026-07-04.md`
- `propuesta-MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C-2026-07-04.md`
- `diagnostico-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.md`
- `sitemap-summary-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.csv`

## Estado público comprobado

`VERIFICADO PERO MEJORABLE`

| URL comprobada | Estado | Tipo | Resultado |
|---|---:|---|---|
| `https://www.matchwalls.com/indexnow.txt` | 404 | `text/plain; charset=utf-8` | No hay key IndexNow en ruta obvia |
| `https://matchwalls.com/indexnow.txt` | 404 tras resolver a `www` | `text/plain; charset=utf-8` | No hay key en dominio sin `www` |
| `https://www.matchwalls.com/robots.txt` | 200 | `text/plain; charset=utf-8` | Robots accesible |
| `https://www.matchwalls.com/sitemap.xml` | 200 | `application/xml; charset=utf-8` | Sitemap accesible |
| `https://www.matchwalls.com/.well-known/ucp` | 200 | `application/json; charset=utf-8` | UCP accesible |
| `https://www.matchwalls.com/llms.txt` | 200 | `text/markdown; charset=utf-8` | Disponible ahora; en 013B había timeout, por tanto estado actualizado |
| `https://www.matchwalls.com/agents.md` | 200 | `text/markdown; charset=utf-8` | Disponible |

Comprobaciones adicionales:

| URL comprobada | Estado | Resultado |
|---|---:|---|
| `https://www.matchwalls.com/this-file-should-not-exist-indexnow-test-013d1.txt` | 404 | 404 real para TXT arbitrario inexistente |
| `https://www.matchwalls.com/indexnow` | 404 | HTML 404, no sirve como key TXT |
| `https://www.matchwalls.com/pages/indexnow.txt` | 404 | No existe página/recurso útil |
| `https://www.matchwalls.com/cdn/shop/t/46/assets/indexnow.txt` | 404 | No existe asset de tema con esa ruta |

## Estado DNS comprobado

`VERIFICADO PERO MEJORABLE`

- `matchwalls.com` apunta por A record a `23.227.38.65`, IP de Shopify.
- `www.matchwalls.com` resuelve por CNAME a `matchwalls.com`.
- Nameservers: `ns1.dns-parking.com` y `ns2.dns-parking.com`.
- TXT actuales detectados:
  - Microsoft: `MS=ms31802557`
  - SPF: `v=spf1 include:spf.protection.outlook.com -all`
  - Klaviyo verification: `TP2DAu`
  - Klaviyo verification: `WDReig`

Interpretación:

`VERIFICADO PERO MEJORABLE`

No hay evidencia de una capa path-aware ya activa —por ejemplo proxy, worker o edge rule— delante de Shopify que permita servir `https://www.matchwalls.com/{key}.txt` sin tocar Shopify. DNS por sí solo puede publicar TXT records, pero IndexNow requiere un archivo HTTP `.txt` accesible dentro del host, no solo un TXT DNS.

## Fuente oficial IndexNow

`VERIFICADO Y CORRECTO`

La documentación oficial de IndexNow indica:

- Para enviar URLs hay que probar propiedad del host alojando al menos un archivo de texto dentro del host.
- La opción recomendada es alojar `{key}.txt` en la raíz del host.
- También existe `keyLocation`, pero debe indicarse en cada notificación y su ubicación puede limitar el alcance práctico de las URLs.
- Se permiten hasta 10.000 URLs por POST, pero `200 OK` solo confirma recepción; no garantiza indexación.

Fuente: https://www.indexnow.org/documentation

## Fuente oficial Shopify relevante

`VERIFICADO Y CORRECTO`

La documentación pública de Shopify confirma rutas root especiales como:

- `/robots.txt`, mediante `robots.txt.liquid`.
- `/agents.md`, mediante `agents.md.liquid`.
- `/llms.txt`, mediante `llms.txt.liquid`.
- `/llms-full.txt`, mediante `llms-full.txt.liquid`.
- `/sitemap.xml`, generado automáticamente.

No se ha encontrado en la documentación revisada una garantía de que Shopify permita crear cualquier archivo arbitrario `/{indexnow-key}.txt` en raíz mediante tema.

También Shopify advierte que, si un tercero pide subir archivos a la carpeta raíz para verificar una web, normalmente se deben usar meta tags en su lugar. Eso sirve para verificaciones compatibles con meta tag, pero IndexNow no se resuelve con meta tag: necesita key file HTTP.

Fuentes:

- https://shopify.dev/docs/storefronts/themes/architecture/templates
- https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt
- https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map
- https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads

## Evaluación de vías posibles

### Opción A — Archivo `{key}.txt` en raíz desde Shopify theme

`DECLARADO PERO NO VERIFICADO`

No hay evidencia suficiente para afirmar que Shopify permita crear un template arbitrario `indexnow-key.txt.liquid` o `{key}.txt.liquid` servido en raíz.

Riesgo: crear un asset o página puede dar una URL bajo `/cdn/` o `/pages/`, no en raíz. Eso no cumple la vía recomendada de IndexNow para todo el host.

Conclusión: no ejecutar sin prueba en entorno controlado o confirmación oficial específica.

### Opción B — Shopify Files / Content Files

`INCORRECTO` para objetivo root global

Shopify Files sirve archivos como recursos gestionados por Shopify/CDN, no como `https://www.matchwalls.com/{key}.txt` en raíz del dominio.

Conclusión: no usar para IndexNow root.

### Opción C — Página Shopify o URL redirect

`INCORRECTO` para objetivo root global

Una página bajo `/pages/` o una redirección no equivale a un archivo TXT root. Además, si se usara `keyLocation` bajo `/pages/`, no sería una solución limpia para productos, colecciones, blogs y home.

Conclusión: no usar como solución global.

### Opción D — DNS TXT

`INCORRECTO` para IndexNow

DNS TXT verifica propiedad para otros servicios, pero IndexNow exige archivo HTTP `.txt` dentro del host.

Conclusión: no basta con añadir un TXT DNS.

### Opción E — CDN/edge/worker delante de Shopify

`REQUIERE DECISION HUMANA`

Técnicamente es la vía más limpia si Shopify no permite root TXT:

- Interceptar solo `https://www.matchwalls.com/{key}.txt`.
- Devolver `200`.
- `Content-Type: text/plain; charset=utf-8`.
- Body exacto: `{key}`.
- No tocar Shopify ni el tema.

Riesgo: hoy no hay evidencia de esa capa activa. Implementarla podría requerir cambios DNS/proxy, con riesgo operativo si se hace mal.

Conclusión: viable solo con acceso y lote específico de infraestructura, no ahora.

### Opción F — App Shopify de IndexNow

`REQUIERE DECISION HUMANA`

Puede ser viable si demuestra:

- cómo verifica la key;
- si aloja realmente `/{key}.txt` o usa método aprobado;
- qué URLs envía;
- cómo excluye noindex, pruebas, muestras noindex, redirects, filtros y URLs con parámetros;
- logs de respuestas de IndexNow/Bing;
- pausa/reversión.

Conclusión: no instalar ni activar sin auditoría previa de la app.

## Decisión técnica del lote

`REQUIERE DECISION HUMANA`

No está listo para implementar IndexNow.

La ruta segura es:

1. Verificar primero Bing Webmaster Tools.
2. Confirmar con Shopify Support o documentación oficial si Shopify puede servir un archivo TXT arbitrario en raíz para IndexNow.
3. Si Shopify no puede, decidir entre:
   - app IndexNow auditada;
   - solución edge/CDN controlada;
   - posponer IndexNow y seguir solo con sitemap + Bing Webmaster hasta tener vía limpia.

## Recomendación operativa

`VERIFICADO PERO MEJORABLE`

Avanzar en este orden:

1. `MW-BING-WEBMASTER-VERIFICATION-DIAG-013E`
   - Confirmar acceso real a Bing Webmaster Tools.
   - Verificar propiedad de `matchwalls.com`.
   - Confirmar sitemap enviado.
   - Revisar si Bing ofrece IndexNow integrado/diagnóstico para la propiedad.

2. `MW-INDEXNOW-SHOPIFY-ROOT-KEY-SUPPORT-QUESTION-013D2`
   - Preparar una pregunta corta a Shopify Support:
     “¿Puede Shopify Online Store servir un archivo TXT arbitrario `/{indexnow-key}.txt` en raíz del dominio para IndexNow, o solo rutas especiales como robots/sitemap/agents/llms?”

3. `MW-INDEXNOW-APP-EDGE-OPTIONS-PROPOSAL-013D3`
   - Comparar app vs edge/CDN vs posponer.
   - Sin instalar nada.

4. `MW-INDEXNOW-PILOT-PROPOSAL-013F`
   - Solo cuando el key hosting esté resuelto.

## Exclusiones vigentes

`VERIFICADO Y CORRECTO`

- No enviar URLs España/Francia del bloque `012O` mientras Shopify Engineering/TMS no estabilice el storefront.
- No enviar todo el sitemap.
- No enviar IT/PT salvo autorización expresa.
- No enviar muestras noindex, URLs de prueba, redirecciones, 404, filtros, query strings ni URLs sin valor.

## Estado final

`VERIFICADO PERO MEJORABLE`

IndexNow sigue siendo recomendable para Bing / Edge / Copilot / Yahoo vía Bing, pero MatchWalls no debe activarlo hasta resolver el alojamiento verificable del archivo de clave. La web ya tiene señales positivas para descubrimiento —`robots.txt`, `sitemap.xml`, `agents.md`, `llms.txt`— pero falta la pieza específica de IndexNow.
