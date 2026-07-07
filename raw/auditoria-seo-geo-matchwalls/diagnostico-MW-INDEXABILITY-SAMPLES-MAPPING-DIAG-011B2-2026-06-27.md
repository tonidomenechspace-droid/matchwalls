# Diagnostico - MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2

Fecha/hora: 2026-06-27  
Estado: `INCOMPLETO`

## Alcance

- Lote: `MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2`.
- Tipo: diagnostico/mapeo de solo lectura.
- Escritura en Shopify: no realizada.
- Objetivo: mapear productos muestra reales, IDs publicos, URLs localizadas, relacion probable con producto principal y preparar el siguiente paso sin ejecutar `noindex`.

## Documentos y datos leidos

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `propuesta-politica-MW-INDEXABILITY-SAMPLES-POLICY-011B-2026-06-27.md`.
- `inventario-muestras-MW-INDEXABILITY-SAMPLES-POLICY-011B-2026-06-26.csv`.
- `muestra-publica-muestras-MW-INDEXABILITY-SAMPLES-POLICY-011B-2026-06-26.csv`.
- `sitemap-urls-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.csv`.
- `inventario-urls.csv`.
- Endpoints publicos Shopify `.js` de productos muestra.

## Acceso real comprobado

`VERIFICADO PERO MEJORABLE`

- Shopify CLI no esta instalado en este entorno local.
- Admin API / valores exactos de metafields `seo.hidden`: `NO ACCESIBLE`.
- IDs publicos de producto via endpoint `.js`: `VERIFICADO Y CORRECTO`.
- Escritura/mutacion: no ejecutada.

## Resultado principal

`VERIFICADO PERO MEJORABLE`

Las 541 URLs de productos muestra del sitemap corresponden a 86 IDs publicos unicos de producto.

Esto significa que la politica debe ejecutarse por producto Shopify, no URL por URL. Una accion de ocultacion SEO sobre el producto puede afectar sus URLs localizadas.

### Cobertura

| Elemento | Resultado |
|---|---:|
| URLs de productos muestra | 541 |
| URLs no producto con termino muestra | 11 |
| IDs publicos unicos de producto muestra | 86 |
| IDs publicos recuperados | 86/86 |
| URLs `.js` recuperadas | 541/541 |
| URLs prioritarias ES/EN/FR/DE/NL | 377 |
| URLs IT/PT fuera de alcance prioritario | 164 |

### Distribucion de URLs localizadas por ID

| URLs por ID | IDs |
|---:|---:|
| 7 | 42 |
| 6 | 40 |
| 4 | 1 |
| 1 | 3 |

## Mapeo producto muestra -> producto principal

`VERIFICADO PERO MEJORABLE`

El mapeo por handle exacto se ha inferido con prudencia, comparando variantes del handle de muestra contra productos del mismo idioma presentes en sitemap.

| Nivel | Resultado |
|---|---:|
| URLs con candidato exacto por handle | 195 |
| URLs sin candidato exacto publico | 346 |
| IDs con mapeo ES exacto | 86/86 |

Por idioma:

| Idioma | URLs muestra | Candidato exacto | Sin candidato exacto |
|---|---:|---:|---:|
| ES | 86 | 86 | 0 |
| EN | 83 | 48 | 35 |
| FR | 83 | 17 | 66 |
| DE | 82 | 12 | 70 |
| NL | 43 | 5 | 38 |
| IT | 81 | 8 | 73 |
| PT | 83 | 19 | 64 |

Lectura: el espanol permite mapear todos los IDs de muestra hacia un posible producto principal. En idiomas no ES, muchos handles no permiten inferencia exacta publica; no se debe usar ese dato para hacer canonicals automaticos.

## Anomalias prioritarias

`VERIFICADO PERO MEJORABLE`

43 de 86 IDs tienen alguna anomalia en idiomas prioritarios:

- 42 IDs con URLs NL que contienen terminologia no neerlandesa de muestra.
- 1 URL EN contiene `muestra`.
- 1 URL FR contiene `muestra`.

Ademas:

- 37 URLs tienen sufijo numerico.
- 26 URLs tienen sufijo `-1`.
- 1 ID (`8554043474147`) tiene productos muestra con `product_type` publico no alineado como muestra en varios idiomas: `Mural`, `Murale`, `Muurschildering`, `Wandgemalde`.

## Estado de indexabilidad publica

`VERIFICADO PERO MEJORABLE`

Evidencia fuerte disponible:

- Las 541 URLs de productos muestra estan en sitemap.
- La muestra publica 011B verifico 24 URLs de producto muestra: 24/24 sin `noindex` detectado, canonical self y 200.
- Las 11 URLs no producto de muestra revisadas en 011B incluyen paginas informativas y una coleccion; no deben tratarse como productos muestra.

Limitacion:

- No se ha leido el valor Admin exacto de `seo.hidden`.
- Aunque la presencia en sitemap y ausencia de `noindex` en muestra sugieren que no estan ocultas SEO, el valor real del metafield sigue `NO ACCESIBLE`.

## No productos con termino muestra

`VERIFICADO Y CORRECTO`

Separados de la politica de productos muestra:

- 10 paginas informativas/de instalacion.
- 1 coleccion/listado alemana.

Recomendacion: no aplicarles noindex por defecto. Deben revisarse editorialmente y mantenerse indexables si responden una intencion util.

## Candidatos piloto

`INCOMPLETO`

Se genera una lista tecnica de 10 IDs candidatos para un futuro piloto de noindex, seleccionados por:

- ID publico recuperado.
- Mapeo ES exacto.
- Sin anomalias en idiomas prioritarios.
- Producto disponible publicamente.

Esto no autoriza escribir en Shopify.

Antes de ejecutar el piloto hace falta:

1. Validar el ID Admin exacto por Admin API/CLI.
2. Leer valor actual de `seo.hidden`.
3. Confirmar que ocultar el producto de busqueda interna de Shopify es aceptable.
4. Crear respaldo por ID.
5. Preparar rollback exacto.

## Archivos generados

- `mapeo-productos-muestra-MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2-2026-06-27.csv`.
- `mapeo-no-productos-muestra-MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2-2026-06-27.csv`.
- `agrupacion-productos-muestra-por-id-MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2-2026-06-27.csv`.
- `candidatos-piloto-noindex-MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2-2026-06-27.csv`.
- `resumen-MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2-2026-06-27.txt`.

## Estado final

`INCOMPLETO`

011B2 cumple el mapeo publico y deja una base mucho mas precisa: 86 productos muestra unicos, no 541 productos independientes.

Queda pendiente acceso Admin/CLI para leer `seo.hidden` y preparar una propuesta de piloto reversible.

## Siguiente lote recomendado

`MW-INDEXABILITY-SAMPLES-ADMIN-SEOHIDDEN-DIAG-011B3`

Tipo: solo lectura.

Objetivo:

- Confirmar IDs Admin/GID.
- Leer `seo.hidden` actual para los 10 candidatos piloto y, si es viable, para los 86 IDs.
- Confirmar si Shopify permite aplicar `seo.hidden=1` sobre esos productos sin efectos no deseados adicionales.
- Preparar propuesta posterior de escritura `MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4`.

