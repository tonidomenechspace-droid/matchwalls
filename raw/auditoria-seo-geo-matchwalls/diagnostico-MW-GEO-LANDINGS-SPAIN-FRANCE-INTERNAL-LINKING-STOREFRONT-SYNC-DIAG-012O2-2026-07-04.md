# Diagnostico `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SYNC-DIAG-012O2`

Fecha: 2026-07-04  
Estado final del diagnostico: `VERIFICADO PERO MEJORABLE`

## Objetivo

Diagnosticar por que el lote `012O` quedo correcto en Shopify Admin, pero no se refleja de forma estable en la web publica.

## Alcance

Solo lectura. No se modifico Shopify, LangShop, tema, paginas, handles, URLs, SEO fields, canonicals, hreflang, schema, menus, home, footer, productos, colecciones ni redirecciones.

## Documentos revisados

- `registro-cambios-ejecutados.md`
- `plan-operativo-vigente-y-cola-lotes-seo-geo-2026-06-30.md`
- `cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`
- `resultado-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O-2026-07-04.md`
- `backup-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O-2026-07-04.md`
- QA publico del lote `012O`

## Estado real comprobado en Shopify Admin

Consulta de solo lectura validada contra Shopify Admin GraphQL.

### Espana

- ID: `gid://shopify/Page/687276622200`
- Handle: `papel-pintado-espana`
- Title: `Papel pintado en Espana para hogares y proyectos profesionales`
- Publicada: si
- `updatedAt`: `2026-07-04T13:29:58Z`
- `body` Admin contiene el bloque:

```html
<h2>Papel pintado por pais</h2><p>Estas consultando las soluciones para Espana. Si tu proyecto se desarrolla en Francia o quieres comparar opciones para otro mercado, consulta la guia de <a href="/pages/papel-pintado-francia">papel pintado en Francia</a>.</p>
```

- Traducciones `body_html` EN/FR/DE/NL contienen el bloque equivalente.
- Estado de traducciones: `outdated:false`.

### Francia

- ID: `gid://shopify/Page/687276654968`
- Handle: `papel-pintado-francia`
- Title: `Papel pintado en Francia para interiores y proyectos profesionales`
- Publicada: si
- `updatedAt`: `2026-07-04T13:30:39Z`
- `body` Admin contiene el bloque:

```html
<h2>Papel pintado por pais</h2><p>Estas consultando las soluciones para Francia. Si tu proyecto se desarrolla en Espana o quieres comparar opciones para otro mercado, consulta la guia de <a href="/pages/papel-pintado-espana">papel pintado en Espana</a>.</p>
```

- Traducciones `body_html` EN/FR/DE/NL contienen el bloque equivalente.
- Estado de traducciones: `outdated:false`.

## Estado publico comprobado

Archivo de QA:

- `qa-publico-robust-recheck-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SYNC-DIAG-012O2-2026-07-04.csv`

Resultado robusto:

| Pagina | Idioma | Resultado publico |
|---|---|---|
| Espana | ES | `FAIL` |
| Espana | EN | `FAIL` |
| Espana | FR | `FAIL` |
| Espana | DE | `FAIL` |
| Espana | NL | `FAIL` |
| Francia | ES | `FAIL` |
| Francia | EN | `FAIL` |
| Francia | FR | `FAIL` |
| Francia | DE | `FAIL` |
| Francia | NL | `FAIL` |

Las 10 URLs publicas siguen sirviendo el cuerpo anterior: despues del bloque de ciudades aparece directamente `Preguntas frecuentes` / `Frequently asked questions` / equivalentes, sin el nuevo bloque de enlazado interno.

## Hechos verificados

- Shopify Admin si contiene el nuevo bloque en Espana y Francia.
- Shopify Admin si contiene las traducciones EN/FR/DE/NL con el bloque.
- Las traducciones estan `outdated:false`.
- La web publica sigue sirviendo el cuerpo anterior en las 10 URLs.
- No hay evidencia de que el problema sea el copy propuesto.
- No hay evidencia de que el problema sea hreflang, canonical o schema.

## Inferencia tecnica

El desfase mas probable esta en una de estas capas:

1. Cache/render cache de Shopify storefront.
2. Cache o sincronizacion de LangShop.
3. Capa intermedia de renderizado/traduccion que no esta tomando aun el valor actualizado de `body_html`.

No se puede afirmar cual de las tres es la causa unica sin una prueba de purga/no-op o revision UI LangShop.

## Riesgo actual

Estado actual: `INCOMPLETO` para publicacion publica del bloque `012O`.

La web publica no esta peor que antes del lote, porque sigue mostrando el contenido antiguo valido. Pero el objetivo del lote -bloque de enlazado visible Espana <-> Francia- aun no esta conseguido publicamente.

## Recomendacion

No avanzar con nuevos lotes visibles de contenido hasta cerrar esta sincronizacion.

Siguiente lote recomendado:

`MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SAME-VALUE-PURGE-012O3`

Alcance recomendado del lote 012O3:

1. Releer Admin.
2. Ejecutar una actualizacion de mismo valor sobre el `body` ES de ambas paginas para forzar `updatedAt`/purga.
3. Re-registrar las traducciones `body_html` EN/FR/DE/NL con el mismo valor ya aprobado y digest vigente.
4. No tocar handles, URLs, titulos, SEO meta, canonicals, hreflang ni schema.
5. Verificar las 10 URLs publicas hasta obtener estabilidad.
6. Si sigue fallando, pasar a revision manual de LangShop UI o soporte.

Este lote si implica escritura tecnica, aunque no cambie contenido, por lo que requiere aprobacion exacta.
