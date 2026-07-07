# Paquete de soporte - MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SUPPORT-EVIDENCE-012J4D

Fecha: 2026-07-04  
Tipo: paquete documental para soporte Shopify / LangShop.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Cambios tema: no.  
Mutaciones GraphQL: no.  
Estado: `INCORRECTO`

## 1. Resumen ejecutivo

La pagina Shopify `papel-pintado-espana` presenta comportamiento inconsistente en el valor renderizado de `page_description`.

El valor SEO manual introducido temporalmente en 012J3 fue retirado/rollback por UI nativa de Shopify. La API Admin actual no muestra `global.description_tag`, no muestra `global.title_tag`, no muestra metacampos y no muestra traducciones SEO. Sin embargo, el storefront publico puede seguir entregando intermitentemente el valor corto 012J3 en la meta description ES bajo determinadas cabeceras/user-agents simulados.

No se ha localizado un campo editable actual que podamos limpiar con seguridad.

Expected / Actual para soporte:

- Expected: con `global.description_tag = null`, todas las peticiones deberian devolver una meta description vacia o un fallback consistente desde el body actual.
- Actual: peticiones con user-agent tipo bot devuelven intermitentemente un valor obsoleto de 134 caracteres que no coincide con el bodySummary actual ni con ningun campo visible Admin/API.

## 2. Recurso afectado

- Store: `matchwalls`
- Dominio: `https://www.matchwalls.com`
- Recurso Shopify: Page
- Page GID: `gid://shopify/Page/687276622200`
- Handle base: `papel-pintado-espana`
- URL ES: `https://www.matchwalls.com/pages/papel-pintado-espana`
- URLs traducidas:
  - EN: `https://www.matchwalls.com/en/pages/spain-wallpaper`
  - FR: `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`
  - DE: `https://www.matchwalls.com/de/pages/spanien-tapete`
  - NL: `https://www.matchwalls.com/nl/pages/spanje-behang`

## 3. Valor conflictivo

Valor que no deberia seguir apareciendo tras rollback:

`Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural.`

Timeline documentado:

- La metadescripcion SEO nativa fue añadida y retirada el 2026-07-04.
- El valor obsoleto se observa de forma intermitente despues del rollback.
- `updatedAt` actual de la pagina por Admin API: `2026-07-04T00:07:41Z`.
- Ese `updatedAt` parece corresponder al guardado de rollback que limpio la metadescripcion SEO. No consta ningun cambio intencionado posterior en contenido, title, body, handle, traducciones, mercados o tema dentro de este trabajo.
- No se ha ejecutado `no-op save` en 012J4D; se deja como accion pendiente de aprobacion porque aunque no cambie texto sigue siendo un evento de escritura/guardado.

`bodySummary` actual confirmado por API:

`Papel pintado, murales y soluciones a medida en España En MatchWalls diseñamos papel pintado, murales decorativos y soluciones a medida para transf...`

Este `bodySummary` actual no coincide con el valor corto de 134 caracteres, por lo que el valor corto no parece ser el fallback vivo del body actual.

## 4. Estado verificado en Admin/API

Lectura Admin actual, solo lectura:

- `title`: `Papel pintado en España para hogares y proyectos profesionales`
- `handle`: `papel-pintado-espana`
- `updatedAt`: `2026-07-04T00:07:41Z`
- `isPublished`: `true`
- `global.description_tag`: `null`
- `global.title_tag`: `null`
- `metafields.nodes`: `[]`
- Traducciones EN/FR/DE/NL: solo contienen `title`, `body_html`, `handle`.
- Traducciones ES: no hay traduccion SEO adicional localizada.
- Traducciones especificas del mercado Spain, verificadas en 012J4B: vacias para ES/EN/FR/DE/NL.

Clasificacion: `VERIFICADO Y CORRECTO` como limpio en Admin/API.

## 5. Estado verificado por UI

Evidencias ya registradas:

- Shopify nativo tras rollback 012J3:
  - Meta description ES visible vacia.
  - Title intacto.
  - URL/handle intacto.
  - Guardado no pendiente.
  - Evidencia: `evidencias/captura-012J3-postrollback-shopify-nativo-meta-vacia-2026-07-04.png`

- LangShop ES:
  - SEO title visible vacio.
  - Meta description visible vacia.
  - Sin guardado.
  - Evidencia: `evidencias/captura-012J4A-langshop-espana-es-seo-fields-vacios-2026-07-04.png`

- LangShop DE:
  - SEO title visible vacio.
  - Meta description visible vacia.
  - Sin guardado.
  - Evidencia: `evidencias/captura-012J4A-langshop-espana-de-seo-fields-vacios-2026-07-04.png`

Clasificacion: `VERIFICADO Y CORRECTO` como limpio en UI visible.

## 6. Estado verificado en tema

Archivos locales revisados del tema publicado/hotfix:

- `layout/theme.liquid`
- `snippets/social-meta-tags.liquid`

Hallazgo:

- `<meta name="description">` usa `page_description`.
- `og:description` usa `page_description`.
- `twitter:description` usa `page_description` como fallback.

No se ha tocado Liquid para forzar metadatos.

## 7. Reproduccion publica

012J4C mostro intermitencia:

- Chrome simulado con idioma local ES/EN/FR/DE/NL: limpio.
- Googlebot simulado: valor 012J3 detectado intermitentemente en ES.
- OAI-SearchBot simulado: valor 012J3 detectado intermitentemente en ES.
- Bingbot simulado: limpio en recheck dirigido.
- EN/FR/DE/NL: limpios en las ultimas rondas amplias.

Recheck actual de 012J4D:

- Chrome ES: limpio, meta autogenerada de 320 caracteres.
- Googlebot simulado: limpio en esta ronda.
- Bingbot simulado: limpio en esta ronda.
- OAI-SearchBot simulado: contaminado, meta de 134 caracteres con el valor 012J3.

Pasos de reproduccion para soporte:

1. Enviar GET a `https://www.matchwalls.com/pages/papel-pintado-espana` con un User-Agent tipo bot, por ejemplo OAI-SearchBot o Googlebot simulado.
2. Inspeccionar `<meta name="description">`, `og:description` y `twitter:description`.
3. Observar que de forma intermitente aparece el valor obsoleto de 134 caracteres.
4. Repetir con User-Agent de navegador y `Accept-Language: es-ES,es;q=0.9`; normalmente devuelve el fallback actual desde body.

Clasificacion storefront: `INCORRECTO` por comportamiento intermitente.

Limitacion:

- Los user-agents de bots son simulaciones de cabecera; no se afirma que equivalgan a rastreo real por IP oficial.
- La evidencia demuestra variacion del HTML segun contexto de peticion.

## 8. Pregunta tecnica para soporte

¿Por que `page_description` puede seguir devolviendo un valor SEO anterior en storefront cuando:

1. `global.description_tag` es `null` en Admin API.
2. `global.title_tag` es `null`.
3. La pagina no tiene metacampos.
4. Las traducciones accesibles por API no contienen `description_tag`.
5. La UI nativa de Shopify muestra la metadescripcion vacia.
6. LangShop ES/DE muestra los campos SEO vacios.

Solicitamos verificar si existe:

- cache interno de storefront;
- version previa de search engine listing no visible por Admin API;
- almacenamiento interno de traducciones SEO no expuesto en la lectura usada;
- conflicto de app/traduccion;
- forma segura de purgar o regenerar `page_description` sin alterar title, body, handle, URL ni traducciones existentes.

## 8.1. Hipotesis tecnica recibida, no verificada

Se recibe una hipotesis externa util para soporte:

- Si `global.description_tag` / `seo.description` es `null`, Shopify puede generar `page_description` desde el resumen plano del body.
- El valor largo actual de 320 caracteres encaja con una metadescripcion autogenerada desde el contenido visible.
- El valor corto 012J3 no encaja con el body actual, por lo que podria proceder de una variante antigua de cache storefront/CDN o de una capa de app/traduccion.

Clasificacion:

- Fallback desde body actual: `VERIFICADO PERO MEJORABLE` por evidencia publica y API.
- Cache CDN/storefront como causa exacta: `DECLARADO PERO NO VERIFICADO`.
- Cache/capa propia LangShop como causa exacta: `DECLARADO PERO NO VERIFICADO`.

Accion segura:

- Preguntar a Shopify si puede purgar/regenerar la cache de storefront para `gid://shopify/Page/687276622200`.
- Preguntar a LangShop si almacena SEO descriptions fuera de metafields/translations y si puede limpiar el registro ES sin modificar traducciones.
- Mantener el `no-op save` como posible siguiente lote separado, no ejecutado todavia.

## 9. Acciones que NO se solicitan

No queremos:

- cambiar el handle;
- cambiar el title;
- cambiar el body;
- reescribir traducciones;
- modificar Liquid;
- forzar una meta description desde el tema;
- borrar recursos;
- publicar tema;
- alterar mercados o dominios.

## 10. Archivos de evidencia adjuntos/referenciados

- `admin-read-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-DESCRIPTION-TAG-STORAGE-DIAG-012J4B-2026-07-04.csv`
- `qa-publico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-STOREFRONT-CACHE-RECHECK-012J4C-2026-07-04.csv`
- `matriz-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-STOREFRONT-CACHE-RECHECK-012J4C-2026-07-04.csv`
- `qa-publico-current-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SUPPORT-EVIDENCE-012J4D-2026-07-04.csv`
- `admin-read-current-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SUPPORT-EVIDENCE-012J4D-2026-07-04.csv`
- `evidencias/captura-012J3-postrollback-shopify-nativo-meta-vacia-2026-07-04.png`
- `evidencias/captura-012J4A-langshop-espana-es-seo-fields-vacios-2026-07-04.png`
- `evidencias/captura-012J4A-langshop-espana-de-seo-fields-vacios-2026-07-04.png`

## 11. Estado final

`MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SUPPORT-EVIDENCE-012J4D` queda como:

- Paquete de soporte preparado.
- Sin cambios ejecutados.
- Incidencia abierta: `INCORRECTO`.
- Siguiente paso seguro: enviar soporte manualmente a Shopify y/o LangShop.
