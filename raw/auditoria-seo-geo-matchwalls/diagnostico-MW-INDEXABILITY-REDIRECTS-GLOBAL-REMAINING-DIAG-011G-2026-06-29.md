# Diagnóstico MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G

Fecha: 2026-06-29  
Hora de registro: 11:07 +02:00  
Tipo: diagnóstico de solo lectura  
Estado final: `VERIFICADO PERO MEJORABLE`

## Alcance

Diagnóstico global de redirecciones Shopify restantes tras 011F4, 011F5 y 011F6.

No se ejecutaron mutaciones, no se modificó Shopify, no se cambiaron redirects, handles, colecciones, productos, páginas, canonicals, sitemaps ni tema.

## Documentos y registros revisados

`VERIFICADO Y CORRECTO`

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `diagnostico-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.md`.
- `ejecucion-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.md`.
- `diagnostico-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEEP-CHAIN-DIAG-011F3-2026-06-28.md`.
- `ejecucion-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-MURALES-COLLISION-CLEANUP-011F4-2026-06-28.md`.
- `ejecucion-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-PAPELES-CONSOLIDATION-011F5-2026-06-28.md`.
- `diagnostico-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-LEGACY-DEPENDENTS-DIAG-011F6-2026-06-29.md`.

## Estado Admin Shopify actual

`VERIFICADO PERO MEJORABLE`

Consulta GraphQL de lectura validada contra schema antes de ejecutarse.

Archivos:

- `redirects-counts-MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G-2026-06-29.csv`
- `redirects-risk-samples-MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G-2026-06-29.csv`

Conteo total actual:

- Redirects Admin: 634.
- Precisión: `EXACT`.

Comparación con 011F:

- 011F tenía 635 redirects.
- Tras la eliminación aprobada de la colisión `/collections/murales` en 011F4, el total actual baja a 634.

Conteos de riesgo actuales:

| Bloque | Conteo | Estado |
|---|---:|---|
| `matchwallsmurals` | 333 | `REQUIERE DECISION HUMANA` |
| `matchwallswallpapers` | 44 | `REQUIERE DECISION HUMANA` |
| `facade` | 1 | `INCORRECTO` |
| `muestra` | 6 | `VERIFICADO PERO MEJORABLE` |
| `copy` | 6 | `VERIFICADO PERO MEJORABLE` |
| `copia` | 12 | `VERIFICADO PERO MEJORABLE` |
| `old` | 1 | `STANDBY` |
| `path:/products/*` | 24 | `VERIFICADO PERO MEJORABLE` |
| `path:/collections/*` | 55 | `RIESGO CRITICO` |
| `path:/pages/*` | 4 | `VERIFICADO PERO MEJORABLE` |
| `target:/` | 36 | `RIESGO CRITICO` |
| `path:/collections/murales` | 0 | `CORREGIDO Y VERIFICADO` |

## Cobertura real de 011G

`VERIFICADO PERO MEJORABLE`

Cobertura Admin:

- Conteo total exacto: 634.
- Conteos exactos por bloques de riesgo.
- Muestras completas para:
  - 24 redirects de productos.
  - 55 redirects de colecciones ES.
  - 4 redirects de páginas.
  - 36 redirects hacia home.
  - 23 redirects FR.
  - 2 redirects EN.
  - 4 redirects AR.

Limitación:

- No se obtuvo export completo fila a fila de las 634 redirecciones. El conector permite paginar, pero transcribir manualmente 634 filas desde respuestas paginadas sería propenso a error y no se considera más riguroso que trabajar por bloques exactos.
- Por tanto, 011G no declara auditado el 100% fila a fila. Declara verificados los conteos globales y los bloques de mayor riesgo accesibles por filtros Admin.

## Sitemap exacto

`RIESGO CRITICO`

Archivo:

- `qa-sitemap-exact-MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G-2026-06-29.csv`

Resultado:

- URLs comprobadas: 244.
- Errores de lectura de sitemap: 0.
- Fuentes de redirects presentes en sitemap exacto: 14.

Las 14 fuentes presentes en sitemap son colecciones ES de color:

- `/collections/papeles-pintados-color-amarillo`
- `/collections/papeles-pintados-color-azul`
- `/collections/papeles-pintados-color-beige`
- `/collections/papeles-pintados-color-blanco`
- `/collections/papeles-pintados-color-blanco-y-negro`
- `/collections/papeles-pintados-color-dorado`
- `/collections/papeles-pintados-color-gris`
- `/collections/papeles-pintados-color-lila`
- `/collections/papeles-pintados-color-marron`
- `/collections/papeles-pintados-color-multicolor`
- `/collections/papeles-pintados-color-negro`
- `/collections/papeles-pintados-color-plateado`
- `/collections/papeles-pintados-color-rosa`
- `/collections/papeles-pintados-color-verde`

Verificación pública posterior:

- Las 14 fuentes cargan `200` como colecciones reales.
- Los 14 targets Admin `murales-en-*` / `blanco-y-negro-murales` devuelven `404`.
- El redirect Admin queda inerte mientras la colección fuente exista, pero es un registro incorrecto y peligroso si el recurso fuente cambia o desaparece.

Estado: `RIESGO CRITICO`.

Recomendación: preparar lote específico para eliminar únicamente esos redirects Admin inertes, sin tocar colecciones, handles ni contenido.

## FR / EN / AR

`RIESGO CRITICO`

Archivo:

- `qa-publico-fr-en-ar-MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G-2026-06-29.csv`
- `qa-publico-recheck-en-black-painted-papers-MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G-2026-06-29.csv`

Resumen:

- 57 paths comprobados entre fuentes y targets FR/EN/AR.
- 42 paths redirigen públicamente.
- 14 casos tienen más de 1 salto.
- 4 casos terminan en 404.
- 1 error inicial EN se resolvió en recheck como `200` directo.

Casos críticos:

- `/ar/pages/...installation-guide...` redirige a `/ar/pages/installation-guide-1`, que devuelve `404`.
- `/fr/collections/painted-papers-baller-matchwallswallpapers` redirige a `/fr/collections/mural-murals-matchwallsmurals`, que devuelve `404`.
- `/fr/collections/mural-murals-matchwallsmurals` devuelve `404`.
- Varias fuentes FR antiguas hacen 2 saltos antes de llegar a una URL final `200`.

Estado: `RIESGO CRITICO`.

Recomendación: no corregir FR en masa dentro de 011G. Abrir sublote específico para mapear IDs intermedios y proponer consolidación o retirada caso por caso.

## Productos y páginas

`INCORRECTO`

Archivos:

- `qa-publico-products-pages-MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G-2026-06-29.csv`
- `qa-publico-recheck-product-errors-MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G-2026-06-29.csv`

Resumen:

- 55 paths comprobados entre fuentes y targets de productos/páginas.
- No se detectaron cadenas múltiples en este bloque.
- Se verificaron redirects de productos que terminan en `404`.

Fuentes con redirect a `404` verificadas:

- `/products/poster-de-papel-mate-calidad-museo-con-marco-de-madera` -> `/products/echoing-corridor-3` -> `404`.
- `/products/endless-horizon-3` -> `/products/echoing-corridor` -> `404`.
- `/products/rusted-horizon-marron-copia` -> `/products/ember-glow-marron` -> `404`.
- `/products/muestra-desnudos-blanco-y-negro` -> `/collections/muestras` -> `404`.
- `/products/urban-geometrico` -> `/products/urban-geometrico-beige` -> `404`.
- `/products/urban-geometrico-beige-copia` -> `/products/urban-geometrico-gris` -> `404`.
- `/products/urban-sketch-beige-copia` -> `/products/melodic-flow` -> `404`.

Estado: `INCORRECTO`.

Recomendación: abrir sublote de diagnóstico/propuesta para decidir si se eliminan, se repuntan a producto equivalente real o se dejan en `STANDBY` si no hay sustituto comercial.

## Redirects hacia home

`RIESGO CRITICO`

Admin verificado:

- `target:/`: 36 redirects, precisión `EXACT`.

Composición observada:

- 1 redirect de prueba: `/pages/facade-variants/test` -> `/`.
- 4 colecciones antiguas de lienzos/cuadros -> `/`.
- 31 redirects `/no/*` -> `/`.

Riesgo:

- Redirigir URLs con intención concreta a home puede ser mala señal de calidad y mala experiencia.
- No se recomienda borrar en masa porque algunos pueden proteger enlaces históricos.

Estado: `RIESGO CRITICO`.

Recomendación: sublote específico para clasificar intención y decidir conservar, repuntar o eliminar.

## Idiomas legacy no prioritarios

`STANDBY`

Conteos exactos:

- `/no/*`: 31.
- `/el/*`: 39.
- `/sv/*`: 39.
- `/he/*`: 38.
- `/pl/*`: 39.
- `/hu/*`: 39.
- `/hi/*`: 39.
- `/ja/*`: 40.
- `/zh/*`: 47.

Estado: `STANDBY`.

No se recomienda tocar estos bloques sin política internacional. Muchos pertenecen a idiomas fuera del alcance prioritario actual.

## Bloques ya estables

`VERIFICADO Y CORRECTO`

- `black-friday`: 0 redirects Admin.
- `matchalls`: 0.
- `norid`: 0.
- `enchathed`: 0.
- `path:/blogs/*`: 0.
- `path:/de/*`: 0.
- `path:/nl/*`: 0.
- `path:/it/*`: 0.
- `path:/pt/*`: 0.

## Conclusión

`VERIFICADO PERO MEJORABLE`

011G confirma que no conviene ejecutar una limpieza masiva. La deuda real está dividida en bloques:

1. `RIESGO CRITICO`: 14 redirects Admin inertes de colecciones ES de color con targets 404.
2. `RIESGO CRITICO`: FR con cadenas y 404.
3. `INCORRECTO`: productos/páginas que redirigen a 404.
4. `RIESGO CRITICO`: 36 redirects hacia home.
5. `STANDBY`: idiomas legacy no prioritarios.

## Siguiente paso recomendado

Abrir primero:

`MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1`

Motivo: es el bloque más quirúrgico y acotado:

- 14 IDs exactos.
- Las fuentes son colecciones reales `200` y están en sitemap.
- Los targets Admin están en `404`.
- La eliminación del redirect Admin debería ser reversible y no debería tocar la URL pública mientras la colección real exista, pero debe verificarse con backup y postcheck antes de afirmar impacto cero.

No ejecutar sin aprobación exacta:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1`
