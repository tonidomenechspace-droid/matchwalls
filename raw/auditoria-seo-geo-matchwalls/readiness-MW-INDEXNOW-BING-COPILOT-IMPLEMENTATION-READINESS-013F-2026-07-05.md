# Readiness MW-INDEXNOW-BING-COPILOT-IMPLEMENTATION-READINESS-013F

Fecha: 2026-07-05

## Estado final

`VERIFICADO PERO MEJORABLE`

El lote queda cerrado como diagnóstico y preparación. No se ha implementado IndexNow, no se ha generado ni publicado ninguna key, y no se ha enviado ninguna URL.

## Alcance aprobado

`APROBADO LOTE MW-INDEXNOW-BING-COPILOT-IMPLEMENTATION-READINESS-013F`

Objetivo: determinar si MatchWalls está listo para implementar IndexNow para Bing / Edge / Copilot / Yahoo vía Bing, y dejar definida la vía segura de implementación posterior.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `registro-cambios-ejecutados.md`
- `diseno-MW-INDEXNOW-BING-COPILOT-DESIGN-013D-2026-07-04.md`
- `diagnostico-MW-INDEXNOW-KEY-HOSTING-DIAG-013D1-2026-07-04.md`
- `propuesta-MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C-2026-07-04.md`
- `qa-MW-BING-WEBMASTER-SITEMAP-STATUS-QA-013E2-2026-07-04.md`
- Evidencias Bing/AI Performance 013E3-013E7.
- Cierre `MW-SHOPIFY-CLI-INSTALL-AUTH-THEME-PUSH-013E16E2`.

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

Comprobación pública del 2026-07-05:

| URL | HTTP | Tipo | Estado |
|---|---:|---|---|
| `https://www.matchwalls.com/robots.txt` | 200 | `text/plain; charset=utf-8` | `VERIFICADO Y CORRECTO` |
| `https://www.matchwalls.com/sitemap.xml` | 200 | `application/xml; charset=utf-8` | `VERIFICADO Y CORRECTO` |
| `https://www.matchwalls.com/indexnow.txt` | 404 | `text/plain; charset=utf-8` | `INCOMPLETO` |
| `https://www.matchwalls.com/agents.md` | 200 | `text/markdown; charset=utf-8` | `VERIFICADO Y CORRECTO` |
| `https://www.matchwalls.com/llms.txt` | 200 | `text/markdown; charset=utf-8` | `VERIFICADO Y CORRECTO` |

Interpretación: MatchWalls tiene buena base de descubrimiento para Bing/IA, pero IndexNow no está activo porque no existe key file verificable.

## Fuentes oficiales contrastadas

`VERIFICADO Y CORRECTO`

IndexNow exige probar propiedad del host alojando un archivo de texto dentro del host. La opción recomendada es alojar `{key}.txt` en la raíz del host. También permite `keyLocation`, pero la ubicación de la key limita qué URLs pueden incluirse si no está en raíz. IndexNow permite hasta 10.000 URLs por POST, pero `200 OK` solo confirma recepción; no garantiza rastreo ni indexación.

Fuentes:

- `https://www.indexnow.org/documentation`
- `https://www.bing.com/indexnow/getstarted`

Shopify confirma que `robots.txt` vive en la raíz del dominio principal y puede personalizarse con `robots.txt.liquid`, pero la documentación revisada no confirma que Shopify Online Store pueda servir un archivo TXT arbitrario `/{indexnow-key}.txt` en raíz del dominio.

Fuente:

- `https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt`

## Decisión técnica

`REQUIERE DECISION HUMANA`

No estamos listos para ejecutar IndexNow todavía.

El punto bloqueante no es Bing. Bing Webmaster ya está verificado y el sitemap está correcto. El punto bloqueante es el alojamiento verificable de la key IndexNow en una ubicación que cubra todo `www.matchwalls.com`.

## Arquitectura recomendada

### Opción 1 — root key file real

`RECOMENDADA`

Objetivo:

```txt
https://www.matchwalls.com/{indexnow-key}.txt
```

Debe devolver:

- HTTP `200`;
- `Content-Type: text/plain`;
- body exacto con la key;
- sin HTML;
- sin redirect dudoso;
- accesible por Bingbot.

Estado actual: `INCOMPLETO`.

No hay evidencia de que Shopify permita crear ese TXT arbitrario en raíz mediante tema.

### Opción 2 — `keyLocation`

`VERIFICADO PERO MEJORABLE`

Solo sería aceptable si la ubicación cubre todas las URLs que se van a enviar. Si la key queda bajo `/pages/`, no sirve limpiamente para productos, colecciones, blogs y home.

No recomendada como solución global inicial.

### Opción 3 — App Shopify IndexNow

`REQUIERE DECISION HUMANA`

Puede ser viable solo si la app demuestra:

- cómo aloja/verifica la key;
- qué URLs envía;
- cómo excluye noindex, muestras, redirecciones, filtros, pruebas y URLs con parámetros;
- logs de respuesta;
- pausa y reversión.

No instalar apps sin lote específico.

### Opción 4 — Edge/CDN/worker

`REQUIERE DECISION HUMANA`

Técnicamente limpia si existe control real de infraestructura, porque permite servir solo `/{key}.txt` sin tocar Shopify. Pero implica riesgo DNS/proxy si se ejecuta mal.

No ejecutar sin acceso, diseño y aprobación separados.

## Política de URLs para futuro piloto

`VERIFICADO Y CORRECTO`

Cuando la key esté resuelta, el primer piloto debe ser pequeño: 5-10 URLs, no todo el sitemap.

Incluir solo URLs que cumplan:

- canónica final;
- `https://www.matchwalls.com`;
- HTTP 200;
- sin query string;
- sin `noindex`;
- no bloqueada por robots;
- no redirigida;
- contenido estable y valioso;
- idiomas prioritarios ES, EN, FR, DE, NL;
- cambio real reciente o página estratégica que justifique notificación.

Excluir:

- muestras noindex;
- URLs de prueba;
- filtros, sort, search, carrito, checkout, account;
- 404/410 no planificados;
- redirecciones intermedias;
- IT/PT salvo aprobación expresa;
- landings España/Francia afectadas por la incidencia `012O` hasta cierre de Shopify Engineering.

## Piloto recomendado cuando se resuelva la key

`REQUIERE DECISION HUMANA`

No usar todavía landings España/Francia por el caso `012O` pendiente.

Piloto seguro candidato:

1. `https://www.matchwalls.com/`
2. `https://www.matchwalls.com/en`
3. `https://www.matchwalls.com/fr`
4. `https://www.matchwalls.com/de`
5. `https://www.matchwalls.com/nl`

Y solo si hay cambio real o QA estable:

6. `https://www.matchwalls.com/pages/medidas-paredes`
7. `https://www.matchwalls.com/blogs/inspiracion/aprende-a-empapelar-paredes-y-techos-con-calidades-non-woven-vinilicas-y-peel-and-stick`

## Riesgos si se implementa mal

`RIESGO CRITICO`

- Enviar URLs no canónicas o noindex.
- Enviar las 7.8K URLs descubiertas por Bing como si todas fueran valiosas.
- Enviar landings con HTML/cache inconsistente mientras Shopify Engineering no cierre `012O`.
- Usar una key en `/pages/` y pretender cubrir productos/colecciones/blogs.
- Instalar una app que envíe todo el sitemap sin exclusiones.
- Confundir `200 OK` de IndexNow con indexación real.

## Siguiente lote seguro

`REQUIERE DECISION HUMANA`

Recomendación:

`MW-INDEXNOW-ROOT-KEY-HOSTING-SUPPORT-QUESTION-013F1`

Alcance:

- Preparar y enviar pregunta exacta a Shopify Support:
  “¿Puede Shopify Online Store servir un archivo TXT arbitrario `/{indexnow-key}.txt` en la raíz del dominio principal para IndexNow, o solo rutas especiales como `robots.txt`, `sitemap.xml`, `agents.md` y `llms.txt`?”
- No tocar Shopify.
- No generar key real.
- No enviar URLs.

Lote posterior, solo si Shopify confirma que NO puede:

`MW-INDEXNOW-APP-EDGE-OPTIONS-PROPOSAL-013F2`

Alcance:

- Comparar app IndexNow vs edge/CDN/worker vs posponer.
- Evaluar riesgos y control de exclusiones.
- Sin instalación ni cambios.

## Evidencias generadas

`VERIFICADO Y CORRECTO`

- `public-check-MW-INDEXNOW-BING-COPILOT-IMPLEMENTATION-READINESS-013F-2026-07-05.csv`
- `readiness-matrix-MW-INDEXNOW-BING-COPILOT-IMPLEMENTATION-READINESS-013F-2026-07-05.csv`
- `readiness-MW-INDEXNOW-BING-COPILOT-IMPLEMENTATION-READINESS-013F-2026-07-05.md`

## Estado de Shopify

`VERIFICADO Y CORRECTO`

No se ha modificado Shopify, tema, páginas, productos, colecciones, traducciones, LangShop, robots, sitemaps, DNS, Bing Webmaster Tools ni IndexNow.
