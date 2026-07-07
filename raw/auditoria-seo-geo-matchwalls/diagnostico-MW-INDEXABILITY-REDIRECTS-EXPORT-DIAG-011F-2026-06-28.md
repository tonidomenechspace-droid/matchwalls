# Diagnóstico MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F

Fecha: 2026-06-28  
Estado global: `INCOMPLETO`

## Alcance

Diagnóstico de solo lectura sobre redirecciones Shopify Admin. No se han creado, modificado ni eliminado redirecciones.

## Documentos leídos

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `redirects-risk-summary-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.md`.
- Evidencias previas de 011C, 011D, 011E y 011E1.

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

- Conteo actual Shopify Admin GraphQL: 635 redirecciones.
- Precisión: `EXACT`.
- Schema verificado: `UrlRedirect` expone solo `id`, `path`, `target`.
- Query validada contra schema antes de ejecutarse.
- Primer bloque exportado: 50 redirecciones.
- Export completo 635 filas: `INCOMPLETO` en esta sesión.

Motivo de incompletitud: el conector permite paginar y leer, pero no dispone de una operación de exportación directa a archivo. La página efectiva usada fue de 50 registros. Transcribir manualmente 635 filas desde respuestas paginadas sería propenso a error y no se considera riguroso.

## Conteos de riesgo verificados

`VERIFICADO PERO MEJORABLE`

- Total: 635.
- `matchwallsmurals`: 334.
- `matchwallswallpapers`: 44.
- `facade`: 1.
- `black-friday`: 0.
- `matchalls`: 0.
- `norid`: 0.
- `enchathed`: 0.
- `muestra`: 6.
- `copy`: 6.
- `copia`: 12.
- `old`: 2.

## Cadenas confirmadas por Admin

`RIESGO CRITICO`

1. Medidas:
   - `/pages/como-tomar-medidas-paredes-y-techos-boton` -> `/pages/medidas-paredes-techos`.
   - `/pages/medidas-paredes-techos` -> `/pages/medidas-paredes`.

2. Colecciones papel pintado:
   - `/collections/papeles-pintados` -> `/collections/papeles-pintados-old`.
   - `/collections/papeles-pintados-old` -> `/collections/murales`.

Estas cadenas no deben corregirse sin validar destino final, tráfico, enlaces internos y Search Console.

## Bloques relevantes

### `matchwallsmurals` / `matchwallswallpapers`

`REQUIERE DECISION HUMANA`

- 334 coincidencias `matchwallsmurals`.
- 44 coincidencias `matchwallswallpapers`.
- La muestra contiene slugs traducidos/literales en FR/EN y destinos con `matchwallsmurals`.
- No se recomienda borrar ni consolidar masivamente sin export completo y validación de destinos.

### `facade`

`INCORRECTO`

- Redirección Admin encontrada: `gid://shopify/UrlRedirect/412625207523`, `/pages/facade-variants/test` -> `/`.
- Tras 011C1 el metaobject de prueba salió de sitemap, pero esta redirección legacy sigue existiendo.
- No tocar sin lote específico.

### Typos conocidos

`VERIFICADO PERO MEJORABLE`

- `black-friday`: 0 redirecciones.
- `matchalls`: 0.
- `norid`: 0.
- `enchathed`: 0.

Esto no significa que los problemas estén resueltos; significa que no existen redirecciones Admin para esos patrones.

## Archivos creados

- `redirects-counts-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.csv`.
- `redirects-risk-samples-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.csv`.
- `redirects-chain-evidence-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.csv`.
- `redirects-export-first50-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.csv`.

## Conclusión

`INCOMPLETO`

011F confirma que las redirecciones son una deuda real y que existen cadenas accionables. Sin embargo, no se debe ejecutar ninguna corrección hasta disponer de export completo de las 635 redirecciones o de una propuesta acotada y verificada sobre cadenas concretas.

## Siguiente paso recomendado

`MW-INDEXABILITY-REDIRECTS-CHAIN-PROPOSAL-011F1`

Preparar propuesta, todavía sin escritura, para consolidar únicamente las dos cadenas confirmadas si los destinos finales responden correctamente.
