# Propuesta de politica - MW-INDEXABILITY-SAMPLES-POLICY-011B

Fecha/hora: 2026-06-27 00:08:43 +02:00  
Estado inicial: `REQUIERE DECISION HUMANA`  
Estado del criterio tras decision de Daniel: `VERIFICADO Y CORRECTO`  
Estado de ejecucion en Shopify: `INCOMPLETO`

## Decision humana recibida

Fecha/hora: 2026-06-27 00:12:18 +02:00

Daniel aprueba el criterio:

`APROBADO CRITERIO MW-INDEXABILITY-SAMPLES-POLICY-011B: NOINDEX POR DEFECTO PARA PRODUCTOS MUESTRA CONFIRMADOS; PAGINAS INFORMATIVAS DE MUESTRAS INDEXABLES; EXCEPCIONES SOLO CON EVIDENCIA`

Esta aprobacion no autoriza todavia escritura en Shopify. La ejecucion requiere un lote posterior con IDs, valores actuales, valores propuestos, impacto en busqueda interna, respaldo, rollback y pruebas.

## Alcance

- Lote/documento: `MW-INDEXABILITY-SAMPLES-POLICY-011B`.
- Tipo: decision SEO/GEO de politica para muestras.
- Escritura en Shopify: no realizada.
- Publicacion de tema: no realizada.
- Recursos revisados: sitemap publico verificado en `MW-INDEXABILITY-INVENTORY-DIAG-011A`, inventario especifico de muestras y muestra publica acotada.
- Idiomas prioritarios: ES, EN, FR, DE, NL.
- Idiomas publicados fuera del alcance prioritario: IT y PT-PT.

## Documentos y evidencias usados

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `programa-ejecucion-seo-geo.md`.
- `lista-maestra-errores-cambios-evoluciones-mejoras.md`.
- `diagnostico-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.md`.
- `sitemap-urls-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.csv`.
- `inventario-muestras-MW-INDEXABILITY-SAMPLES-POLICY-011B-2026-06-26.csv`.
- `muestra-publica-muestras-MW-INDEXABILITY-SAMPLES-POLICY-011B-2026-06-26.csv`.
- Fuente oficial Shopify Help Center: `https://help.shopify.com/en/manual/promoting-marketing/seo/hide-a-page-from-search-engines`.
- Fuente oficial Shopify Dev Docs: `https://shopify.dev/docs/apps/build/marketing-analytics/optimize-storefront-seo`.

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

En el sitemap publico se detectan 552 URLs con patrones de muestra o equivalente multilingue.

Distribucion por tipo:

| Tipo | URLs |
|---|---:|
| Productos candidatos a muestra | 541 |
| Paginas informativas/de instalacion con termino muestra | 10 |
| Coleccion/listado con termino muestra | 1 |

Distribucion por idioma:

| Idioma | URLs totales | Productos muestra |
|---|---:|---:|
| ES | 88 | 86 |
| EN | 85 | 83 |
| FR | 85 | 83 |
| DE | 84 | 82 |
| NL | 43 | 43 |
| IT | 82 | 81 |
| PT | 85 | 83 |

Agrupacion de alcance:

| Grupo | URLs |
|---|---:|
| Prioritarias ES/EN/FR/DE/NL | 385 |
| Fuera de alcance prioritario IT/PT | 167 |
| Productos muestra prioritarios ES/EN/FR/DE/NL | 377 |
| Productos muestra IT/PT | 164 |

La muestra publica acotada revisada contiene 35 URLs representativas:

- 35/35 responden `200`.
- 35/35 canonical self.
- 0/35 con `noindex` detectado.
- 35/35 con H1.
- 0/35 redirigen.

Conclusion factual: las muestras revisadas son URLs rastreables, canonicas e indexables. El sitemap ademas incluye 541 productos candidatos a muestra.

## Anomalias detectadas

`VERIFICADO PERO MEJORABLE`

- 42 URLs NL contienen terminos no neerlandeses de muestra.
- 1 URL EN contiene `muestra`.
- 1 URL FR contiene `muestra`.
- 1 coleccion DE contiene `muster`: `https://www.matchwalls.com/de/collections/papierpapier-kleine-muster-matchwalswallpapers`.
- 37 URLs con sufijo numerico.
- 26 URLs con sufijo `-1`.
- IT/PT suman 167 URLs con terminos de muestra, pero estan fuera del alcance prioritario actual salvo autorizacion expresa.

## Riesgo SEO/GEO

`VERIFICADO PERO MEJORABLE`

Riesgos si los productos muestra siguen indexables sin politica:

- Canibalizacion de productos principales.
- Expansion del indice con SKUs auxiliares de baja intencion SEO.
- Motores de busqueda o asistentes IA pueden citar/recomendar una muestra como si fuera el mural o producto principal.
- Duplicacion de metadatos y contenido entre muestra y producto principal.
- Senales internacionales menos limpias por terminos cruzados entre idiomas.

No se puede afirmar que esto este causando perdida de trafico sin Search Console, Bing Webmaster Tools y datos de conversion por URL.

## Politica recomendada

`REQUIERE DECISION HUMANA`

Recomendacion principal:

1. Tratar los productos muestra como productos auxiliares de conversion, no como landings SEO.
2. Mantener indexables las paginas informativas de muestras e instalacion cuando tengan contenido util y localizado.
3. No aplicar cambios masivos hasta construir un mapa fiable `producto principal -> muestra`.
4. Aplicar `noindex` por defecto solo a productos muestra confirmados, con excepciones documentadas si una muestra tiene demanda, enlaces, conversiones o contenido propio suficiente.
5. No modificar handles en este bloque.
6. No redirigir ni canonizar de forma global sin correspondencia uno a uno verificada.

### Metodo Shopify preferente para ejecucion futura

Shopify documenta el metafield del sistema:

- namespace: `seo`
- key: `hidden`
- value: `1`
- type: `number_integer`

Segun la documentacion oficial, este metodo oculta el recurso de sitemap, buscadores y busqueda interna de la tienda, y anade `noindex`/`nofollow` cuando se usa para ocultar recursos de buscadores y sitemaps.

Implicacion critica: antes de usarlo hay que aceptar que las muestras dejarian de aparecer en la busqueda interna de la tienda. La pagina del producto seguiria siendo accesible por URL directa.

## Alternativas evaluadas

| Opcion | Ventaja | Riesgo | Recomendacion |
|---|---|---|---|
| `seo.hidden=1` en productos muestra confirmados | Limpio para sitemap y buscadores; reversible por metafield | Tambien los elimina de la busqueda interna de Shopify | Recomendada para piloto controlado |
| `noindex` por tema/Liquid | Puede conservar busqueda interna | No retira de sitemap por si solo; depende del tema publicado | Solo si el impacto en busqueda interna no se acepta |
| Canonical a producto principal | Puede consolidar senales si hay equivalencia exacta | Peligroso si el mapeo es incorrecto; no retira necesariamente del sitemap | Solo con mapa uno a uno verificado |
| Redireccionar muestras | Limpia indice rapidamente | Puede romper compra/pedido de muestras | No recomendado de forma global |
| Robots.txt | Reduce rastreo | No es metodo correcto para retirar URLs ya indexadas; puede impedir ver el noindex | No recomendado |
| Dejar todo indexable | Sin esfuerzo operativo | Mantiene canibalizacion y ruido GEO/LLMO | No recomendado |

## Propuesta de ejecucion posterior, no incluida en 011B

### Fase 011B2 - diagnostico/mapeo sin escritura

Nombre sugerido: `MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2`.

Objetivo:

- Exportar o consultar productos muestra reales con IDs.
- Confirmar estado publicado, idioma, handle, plantilla, tipo, tags/metafields y relacion con producto principal.
- Separar:
  - productos muestra confirmados;
  - paginas informativas de muestra;
  - colecciones/listados;
  - falsos positivos;
  - IT/PT fuera de alcance.
- Preparar una lista piloto de bajo riesgo.

Sin cambios en Shopify.

### Fase 011B3 - piloto con escritura, solo si se aprueba despues

Nombre sugerido: `MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B3`.

No ejecutar hasta tener propuesta formal con:

- IDs de producto.
- Valores actuales de `seo.hidden`.
- Valores propuestos.
- Impacto aceptado en busqueda interna.
- Respaldo por producto.
- Metodo de reversion: borrar/dejar vacio `seo.hidden`.
- Pruebas: HTML `noindex,nofollow`, desaparicion posterior de sitemap, URL directa accesible, compra/pedido de muestra operativo, no afectacion de productos principales.

## Decision que necesita Daniel

No aprobar ejecucion todavia.

Decision recomendada para esta politica:

`APROBADO CRITERIO MW-INDEXABILITY-SAMPLES-POLICY-011B: NOINDEX POR DEFECTO PARA PRODUCTOS MUESTRA CONFIRMADOS; PAGINAS INFORMATIVAS DE MUESTRAS INDEXABLES; EXCEPCIONES SOLO CON EVIDENCIA`

Despues de esa decision, el siguiente trabajo seguro es:

`MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2`

## Estado final de 011B

`REQUIERE DECISION HUMANA`

No se ha modificado Shopify.
