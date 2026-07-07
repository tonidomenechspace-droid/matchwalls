# Diagnostico de indexabilidad - MW-INDEXABILITY-INVENTORY-DIAG-011A

Fecha: 2026-06-26

## Estado del lote

`INCOMPLETO`

El diagnostico publico del sitemap y una muestra de URLs criticas queda verificado, pero el bloque completo de indexabilidad sigue incompleto porque falta acceso/export actual de:

- Google Search Console.
- Bing Webmaster Tools.
- Redirecciones Shopify actuales.
- Datos de trafico, conversion e ingresos por URL.

No se ha modificado Shopify.

## Documentos leidos

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `programa-ejecucion-seo-geo.md`.
- `lista-maestra-errores-cambios-evoluciones-mejoras.md`.
- `diagnostico-lote-MW-INDEXABILITY-TECH-008-2026-06-17.md`.
- `matriz-lote-MW-INDEXABILITY-TECH-008-2026-06-17.csv`.
- `auditoria-interna-shopify.md`.
- `auditoria-catalogo.csv`.
- `auditoria-internacional.csv`.
- `auditoria-seo-tecnico.csv`.
- `sitemap-urls.txt`.

## Estado real publico comprobado

### Robots

`VERIFICADO Y CORRECTO`

- `https://www.matchwalls.com/robots.txt`: 200.
- Declara `Sitemap: https://www.matchwalls.com/sitemap.xml`.
- Permite rastreo publico general.
- Bloquea superficies privadas/transaccionales: admin, cart, checkout, account, orders, servicios internos y trampas de filtros/sort/previews.
- Declara `https://www.matchwalls.com/agents.md` y UCP/MCP.
- No se detecta bloqueo global de Google/Bing ni bloqueo global de crawlers IA en robots.

Archivos:

- `robots-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.txt`.

### Agents/UCP

`VERIFICADO Y CORRECTO`

- `https://www.matchwalls.com/agents.md`: 200, `text/markdown`.
- `https://www.matchwalls.com/.well-known/ucp`: 200, `application/json`.

La politica fina de crawlers IA no se cierra en este lote; corresponde al bloque Bing/Copilot, IndexNow y crawlers IA.

### Sitemap

`VERIFICADO PERO MEJORABLE`

- `https://www.matchwalls.com/sitemap.xml`: 200.
- Tipo: `sitemapindex`.
- Sub-sitemaps: 36/36 accesibles.
- URLs totales: 7.932.

Distribucion publica:

| Tipo | Total | Por idioma |
| --- | ---: | --- |
| Products | 6.797 | 971 por idioma |
| Collections | 749 | 107 por idioma |
| Pages | 294 | 42 por idioma |
| Blogs | 84 | 12 por idioma |
| Home | 7 | 1 por idioma |
| `agents.md` | 1 | raiz |

Idiomas publicados en sitemap:

- ES: 1.134 URLs.
- EN: 1.133 URLs.
- FR: 1.133 URLs.
- DE: 1.133 URLs.
- NL: 1.133 URLs.
- IT: 1.133 URLs.
- PT: 1.133 URLs.

IT y PT siguen publicados en sitemap, aunque estan fuera del alcance prioritario activo salvo aprobacion expresa.

Archivos:

- `sitemap-index-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.csv`.
- `sitemap-urls-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.csv`.
- `sitemap-summary-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.txt`.

## Hallazgos verificados

### 1. Muestras en sitemap

`VERIFICADO PERO MEJORABLE`

Se detectan 552 URLs de muestra por patrones multilingues:

- ES: 88.
- EN: 85.
- FR: 85.
- DE: 84.
- NL: 43.
- IT: 82.
- PT: 85.

Ejemplos verificados publicamente:

- `https://www.matchwalls.com/products/muestra-abstract-curves-negro`: 200, canonical self, sin `noindex`, H1 `Muestra Abstract Curves Negro`.
- `https://www.matchwalls.com/en/products/muestra-de-wildflower-whisper-lila`: 200, canonical self, sin `noindex`, H1 `Wildflower Whisper Lila`.

Riesgo:

- Canibalizacion de productos principales.
- Expansion del indice con SKUs auxiliares.
- Motores de busqueda o IA pueden recomendar una muestra como si fuera producto principal.

Decision pendiente:

- Noindex masivo.
- Canonical a producto principal cuando exista mapeo fiable.
- Mantener indexables solo muestras con demanda/contenido propio.

No cambiar hasta disponer de mapa producto principal -> muestra.

### 2. URLs internas de prueba `facade-variants/test`

`INCORRECTO`

El sitemap contiene 7 URLs:

- ES, EN, FR, DE, NL, IT, PT.

Comprobacion sin seguir redireccion:

- `https://www.matchwalls.com/pages/facade-variants/test` -> 301 a `/`.
- `https://www.matchwalls.com/en/pages/facade-variants/test` -> 301 a `/en/`.
- `https://www.matchwalls.com/fr/pages/facade-variants/test` -> 301 a `/fr/`.
- `https://www.matchwalls.com/de/pages/facade-variants/test` -> 301 a `/de/`.
- `https://www.matchwalls.com/nl/pages/facade-variants/test` -> 301 a `/nl/`.

Riesgo:

- Sitemap declara URLs que no son canonicas finales.
- Desperdicio de rastreo.
- Senal de baja higiene tecnica.

Accion futura recomendada:

- Localizar origen en metaobject pages/sitemap.
- Retirar del sitemap o devolver 404/410 si son pruebas sin equivalente.
- No hacer cambios sin propuesta y aprobacion.

### 3. Black Friday 2024 indexable

`INCORRECTO`

Se detectan 5 URLs de Black Friday en sitemap:

- ES, EN, FR, IT, NL.

Ejemplos verificados:

- ES `https://www.matchwalls.com/collections/papel-pintado-black-friday`: 200, canonical self, sin `noindex`, H1 `BLACK FRIDAY 2024`.
- EN `https://www.matchwalls.com/en/collections/wallpapers-black-friday`: 200, canonical self, sin `noindex`, H1 `Black Friday 2024`.

Riesgo:

- Campaña obsoleta indexable.
- Senal editorial mala para buscadores y sistemas IA.
- Posible conflicto con ofertas actuales.

Decision pendiente:

- Actualizar a campaña real.
- Convertir en evergreen de ofertas.
- Noindex/despublicar/redirigir si no hay sustituto equivalente.

### 4. Marca mal escrita `matchalls`

`INCORRECTO`

- `https://www.matchwalls.com/fr/collections/nouveaux-matchalls-matchwallsmurals`: 200, canonical self, sin `noindex`.
- H1: `Nouveaux Papiers Peints`.

Riesgo:

- Error de marca en URL indexable.
- Debilita entidad MatchWalls en FR y motores IA.

Accion futura:

- Crear URL correcta y 301 solo con mapa aprobado.
- Verificar canonical, hreflang y enlaces internos.

### 5. Handles con typos de familia

`INCORRECTO`

Inventario actual:

- `norid/noridcas`: 70 URLs.
- `enchathed`: 19 URLs.

Ejemplos verificados:

- `https://www.matchwalls.com/products/lineas-noridcas-negro`: 200, canonical self, H1 `Lineas Nordicas Negro`.
- `https://www.matchwalls.com/en/products/enchathed-garden-symphony-multicolor`: 200, canonical self, H1 `Enchathed Garden Symphony Multicolor`.

Riesgo:

- Errores lexicales persistentes en URLs indexables.
- Cambiar handles sin mapa 301 puede crear 404 y romper hreflang.

Accion futura:

- Diccionario maestro de familias.
- Mapa URL actual -> URL correcta -> 301.
- QA hreflang/canonical/enlazado antes de cualquier cambio.

### 6. Sufijo `-1`

`REQUIERE DECISION HUMANA`

Inventario actual:

- 435 URLs con sufijo `-1`.

Muestreo publico:

- Varias responden 200, canonical self y H1 correcto.

Interpretacion:

- No todo sufijo `-1` es necesariamente error.
- Puede indicar colisiones historicas, duplicados, traducciones o productos distintos.

Accion futura:

- No corregir masivamente.
- Clasificar por familia, idioma y equivalencia antes de proponer handles.

### 7. Colecciones geograficas

`VERIFICADO PERO MEJORABLE`

En sitemap actual se detectan 170 URLs con patron geografico claro:

- ES: 58.
- FR: 56.
- PT: 56.

Ejemplos:

- `https://www.matchwalls.com/collections/comprar-papel-pintado-madrid`.
- `https://www.matchwalls.com/collections/comprar-papel-pintado-barcelona`.

Muestreo:

- Madrid y Barcelona responden 200, canonical self, H1 localizado.

Riesgo:

- Posible doorway/thin content si no tienen valor local unico.
- Duplicacion de surtido y textos.
- Pueden consumir rastreo y diluir autoridad.

Decision pendiente:

- Conservar y enriquecer solo las que tengan demanda, conversion o valor local real.
- Consolidar/noindex/retirar el resto con mapa controlado.

No actuar sin Search Console, ventas y decision humana.

### 8. Uploader personalizado

`VERIFICADO PERO MEJORABLE`

Verificado:

- `https://www.matchwalls.com/products/custom-file-uploader`: 200.
- Canonical self.
- H1: `Tu Mural Personalizado`.
- `meta robots="noindex,nofollow"`.
- No aparece en el sitemap actual.

Interpretacion:

- Tecnicamente coherente si se decide que el uploader no debe indexarse.
- Comercialmente requiere decision: puede ser una URL de alta intencion si se quiere posicionar como mural personalizado.

Accion futura:

- Decidir indexar/noindexar uploader.
- Si se indexa, retirar noindex, revisar contenido y volver a incluir en sitemap solo si aporta valor.

### 9. Paginas corporativas revalidadas

`CORREGIDO Y VERIFICADO` en las muestras revisadas.

Hallazgos historicos de paginas sin H1 no se reproducen en esta muestra actual:

- `https://www.matchwalls.com/fr/pages/a-propos-de-nous`: H1 presente.
- `https://www.matchwalls.com/nl/pages/over-ons`: H1 presente.
- `https://www.matchwalls.com/en/pages/request-your-sample`: H1 presente.

Esto probablemente refleja la publicacion previa de H1/tema. No significa que las 294 paginas esten cerradas; solo que estos ejemplos ya no fallan por H1.

### 10. Redirecciones Shopify

`DECLARADO PERO NO VERIFICADO`

Historico interno:

- `auditoria-interna-shopify.md` declara 635 redirecciones y cadenas concretas.

Estado en 011A:

- No se obtuvo export actual de redirecciones Shopify.
- No se revalida que sigan siendo exactamente 635.

Accion futura:

- Export/lectura actual de redirects.
- Detectar cadenas, bucles, 404 destino y destinos no equivalentes.
- No modificar sin lote aprobado.

## Archivos generados

- `robots-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.txt`.
- `sitemap-index-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.csv`.
- `sitemap-urls-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.csv`.
- `sitemap-summary-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.txt`.
- `inventario-flags-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.csv`.
- `muestra-indexabilidad-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.csv`.

## Siguiente orden recomendado

1. `MW-INDEXABILITY-SAMPLES-POLICY-011B`: decision/propuesta de politica para muestras.
2. `MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C`: propuesta para retirar `facade-variants/test` del sitemap/origen.
3. `MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D`: decidir destino de Black Friday.
4. `MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E`: clasificar geograficas con datos de Search Console/ventas.
5. `MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F`: export y auditoria actual de redirecciones.
6. `MW-INDEXABILITY-HANDLE-TYPO-MAP-011G`: mapa de handles con typos, sin ejecutar cambios.

Ninguno de estos siguientes pasos autoriza cambios en Shopify por si solo.
