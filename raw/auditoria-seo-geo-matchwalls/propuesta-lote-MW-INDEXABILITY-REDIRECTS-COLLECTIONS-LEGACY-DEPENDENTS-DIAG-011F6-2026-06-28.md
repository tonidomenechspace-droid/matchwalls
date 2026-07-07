# Propuesta de diagnóstico MW-INDEXABILITY-REDIRECTS-COLLECTIONS-LEGACY-DEPENDENTS-DIAG-011F6

Fecha: 2026-06-28  
Estado: `REQUIERE DECISION HUMANA`

## Objetivo

Auditar de solo lectura los redirects legacy dependientes que quedan tras 011F4 y 011F5, antes de decidir si conviene conservarlos, consolidarlos o eliminarlos.

## Alcance propuesto

Solo diagnóstico, sin mutaciones.

Recursos a revisar:

- `/collections/murales-mvp` -> `/collections/murales`.
- `/collections/%20papeles-pintados` -> `/collections/murales`.
- 8 redirects con target `/en/collections/all-matchwallsmurals-murals`.

## Motivo

`VERIFICADO PERO MEJORABLE`

Tras 011F5, la cadena principal está corregida. Aún quedan redirects legacy menores que pueden ser útiles para tráfico histórico o pueden ser deuda técnica. No deben tocarse sin comprobar si están en sitemap, si reciben tráfico, si son idioma prioritario y si su destino es correcto.

## Resultado esperado

`REQUIERE DECISION HUMANA`

Clasificación de cada redirect como:

- Conservar.
- Consolidar.
- Eliminar.
- Mantener en `STANDBY`.

## Aprobación

Este diagnóstico no requiere escritura, pero si Daniel quiere abrirlo como siguiente lote operativo puede indicar:

`MW-INDEXABILITY-REDIRECTS-COLLECTIONS-LEGACY-DEPENDENTS-DIAG-011F6`
