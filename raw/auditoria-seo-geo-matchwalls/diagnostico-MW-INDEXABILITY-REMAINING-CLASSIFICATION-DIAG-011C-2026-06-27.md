# 2026-06-27 - Diagnóstico de indexabilidad restante

Lote de lectura: `MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C`

Estado global: `INCOMPLETO`

No se ha modificado Shopify. No se han tocado productos, colecciones, páginas, handles, canonicals, redirecciones, temas, apps ni configuración externa.

## Documentos y artefactos revisados

- `AGENTS.md`
- `registro-cambios-ejecutados.md`
- `programa-ejecucion-seo-geo.md`
- `diagnostico-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.md`
- Artefactos 011B/011B4/011B5/011B5B de muestras noindex.
- Sitemap, robots y matrices generadas para este diagnóstico.

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

- Sitemaps leídos: 36/36.
- URLs actuales en sitemap: 7.330.
- URLs del inventario 011A: 7.932.
- Diferencia desde 011A: 602 URLs menos en sitemap, 0 URLs nuevas detectadas.
- Las 602 URLs retiradas son productos de muestra localizados: 86 productos x 7 idiomas.
- Conteo actual de redirecciones en Shopify Admin: 635.

## Distribución actual del sitemap

| Tipo | URLs |
|---|---:|
| Productos | 6.195 |
| Colecciones | 749 |
| Páginas | 294 |
| Blogs/artículos | 84 |
| Homes localizadas | 7 |
| `agents.md` | 1 |

| Idioma | URLs |
|---|---:|
| ES | 1.048 |
| EN | 1.047 |
| FR | 1.047 |
| DE | 1.047 |
| NL | 1.047 |
| IT | 1.047 |
| PT | 1.047 |

## Clasificación maestra actual

Archivo: `classification-master-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`

| Estado | URLs |
|---|---:|
| `DECLARADO PERO NO VERIFICADO` | 6.535 |
| `REQUIERE DECISION HUMANA` | 688 |
| `INCORRECTO` | 97 |
| `VERIFICADO PERO MEJORABLE` | 10 |

Detalle por grupo:

| Grupo | URLs | Estado |
|---|---:|---|
| Sin bandera automática prioritaria | 6.535 | `DECLARADO PERO NO VERIFICADO` |
| Colección geográfica candidata | 346 | `REQUIERE DECISION HUMANA` |
| Sufijo `-1` posible duplicado | 337 | `REQUIERE DECISION HUMANA` |
| Typo `norid/noridcas` | 70 | `INCORRECTO` |
| Typo `enchathed` | 19 | `INCORRECTO` |
| Prueba `facade-variants/test` | 7 | `INCORRECTO` |
| Black Friday | 5 | `REQUIERE DECISION HUMANA` |
| Typo `matchalls` | 1 | `INCORRECTO` |
| Páginas informativas de muestras | 10 | `VERIFICADO PERO MEJORABLE` |

## Comprobación pública prioritaria

Archivo: `public-check-priority-classified-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`

Se comprobaron 482 URLs sensibles:

| Estado | URLs |
|---|---:|
| `INCOMPLETO` | 248 |
| `INCORRECTO` | 95 |
| `REQUIERE DECISION HUMANA` | 129 |
| `VERIFICADO PERO MEJORABLE` | 10 |

Limitación: 244 respuestas fueron `429` por protección del servidor y 4 quedaron sin respuesta concluyente. Esas lecturas se han marcado como `INCOMPLETO`; no se usarán como base para cambios.

## Hallazgos críticos accionables

### 1. URLs de prueba `facade-variants/test`

Estado: `INCORRECTO`

- 7 URLs en sitemap.
- Respuesta pública: 301 a home local.
- Redirección Admin verificada solo para `/pages/facade-variants/test` -> `/`.
- Problema: una URL en sitemap no debe redirigir; además es una ruta de prueba.

Acción recomendada: lote específico para retirar estas URLs del sitemap y dejar comportamiento estable por idioma.

### 2. Typos en handles o slugs

Estado: `INCORRECTO`

- `norid/noridcas`: 70 URLs detectadas.
- `enchathed`: 19 URLs detectadas.
- `matchalls`: 1 URL detectada.
- No se encontraron redirecciones Admin para esos tres patrones.

Acción recomendada: no cambiar handles todavía. Primero crear mapa de destino correcto y 301 por idioma/producto/colección.

### 3. Black Friday

Estado: `REQUIERE DECISION HUMANA`

- 5 colecciones activas en sitemap.
- Respuesta pública verificada: 200.
- Canonical self verificado en las comprobadas.
- No se encontraron redirecciones Admin para `black-friday`.

Acción recomendada: decidir si se mantiene como evergreen, se noindexa, se retira o se redirige a ofertas actuales.

### 4. Colecciones geográficas

Estado: `REQUIERE DECISION HUMANA`

- 346 colecciones candidatas.
- Reparto por idioma: ES 58, EN 56, FR 56, NL 52, PT 55, DE 41, IT 28.
- 105 comprobaciones públicas fueron 200; 241 quedaron incompletas por 429/sin respuesta.
- Ejemplo verificado: `Papel pintado Álava`, `Papel pintado Barcelona`, etc.

Acción recomendada: no retirar masivamente. Clasificar por país/idioma con datos de demanda, contenido, canibalización e ingresos.

### 5. Sufijos `-1`

Estado: `REQUIERE DECISION HUMANA`

- 337 URLs actuales clasificadas como posible duplicado tras excluir grupos de mayor prioridad.
- 24 se comprobaron públicamente; 19 dieron 200 y 5 quedaron incompletas por 429.

Acción recomendada: clasificar por tipo de recurso antes de tocar nada.

### 6. Páginas de muestras restantes

Estado: `VERIFICADO PERO MEJORABLE`

- 10 URLs no-producto con término de muestra.
- Son páginas informativas, no productos de muestra.
- Deben mantenerse indexables solo si responden una intención informativa real.

## Redirecciones

Estado: `INCOMPLETO`

- Conteo actual verificado: 635.
- Resumen de riesgo: `redirects-risk-summary-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.md`.
- No existe export completo local.
- Shopify CLI no está disponible en este entorno.

Acción recomendada: crear diagnóstico específico de export/matriz de redirecciones antes de cambios 301.

## Próximo orden recomendado

1. `MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1`
2. `MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D`
3. `MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E`
4. `MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F`
5. `MW-INDEXABILITY-HANDLE-TYPO-MAP-011G`
6. `MW-INDEXABILITY-SUFFIX-1-CLASSIFICATION-011H`
7. `MW-INDEXABILITY-SAMPLE-PAGES-CONTENT-011I`

## Criterio de seguridad

No se recomienda ejecutar cambios masivos de indexabilidad hasta resolver primero:

- URLs de prueba en sitemap.
- Política Black Friday.
- Mapa de redirecciones exportado.
- Decisión documentada sobre colecciones geográficas.
- Mapa 301 de typos.

