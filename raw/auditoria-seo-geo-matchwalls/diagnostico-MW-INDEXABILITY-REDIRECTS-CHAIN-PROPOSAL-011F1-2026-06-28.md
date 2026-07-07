# Diagnóstico MW-INDEXABILITY-REDIRECTS-CHAIN-PROPOSAL-011F1

Fecha: 2026-06-28  
Estado global: `VERIFICADO PERO MEJORABLE`

## Alcance

Diagnóstico/propuesta de solo lectura sobre las cadenas de redirección confirmadas en 011F.

No se han creado, modificado ni eliminado redirecciones. No se han tocado handles, canonicals, contenidos, temas ni configuración externa.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `diagnostico-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.md`.
- `redirects-chain-evidence-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.csv`.

## Estado Admin comprobado

`VERIFICADO Y CORRECTO`

Shopify Admin GraphQL confirma que las 5 redirecciones leídas por GID siguen existiendo con estos valores:

| ID | Path actual | Target actual | Estado |
|---|---|---|---|
| `gid://shopify/UrlRedirect/405088796899` | `/pages/como-tomar-medidas-paredes-y-techos-boton` | `/pages/medidas-paredes-techos` | `RIESGO CRITICO` |
| `gid://shopify/UrlRedirect/409984762083` | `/pages/medidas-paredes-techos` | `/pages/medidas-paredes` | `VERIFICADO Y CORRECTO` |
| `gid://shopify/UrlRedirect/410027000035` | `/collections/papeles-pintados` | `/collections/papeles-pintados-old` | `RIESGO CRITICO` |
| `gid://shopify/UrlRedirect/417318207715` | `/collections/papeles-pintados-old` | `/collections/murales` | `VERIFICADO Y CORRECTO` |
| `gid://shopify/UrlRedirect/412625207523` | `/pages/facade-variants/test` | `/` | `INCORRECTO` |

## Verificación pública

`VERIFICADO PERO MEJORABLE`

El navegador interno confirma navegación pública hasta destino final, canonical, title, H1 y ausencia de meta robots `noindex` visible en destino.

Limitación: el entorno no permitió capturar cabeceras HTTP exactas con PowerShell/curl. Por tanto, el código HTTP exacto y la cabecera `Location` pública quedan como `NO ACCESIBLE` en esta sesión. La navegación final sí está verificada.

Archivo de evidencia pública: `qa-publico-MW-INDEXABILITY-REDIRECTS-CHAIN-PROPOSAL-011F1-2026-06-28.csv`.

## Conclusión técnica

`VERIFICADO PERO MEJORABLE`

Hay dos cadenas accionables y acotadas:

1. Medidas:
   - Actual: `/pages/como-tomar-medidas-paredes-y-techos-boton` -> `/pages/medidas-paredes-techos` -> `/pages/medidas-paredes`.
   - Destino final verificado: `/pages/medidas-paredes`.
   - Canonical final: `https://www.matchwalls.com/pages/medidas-paredes`.
   - H1 final: `Cómo tomar medidas de paredes`.

2. Colecciones:
   - Actual: `/collections/papeles-pintados` -> `/collections/papeles-pintados-old` -> `/collections/murales`.
   - Destino final verificado: `/collections/murales`.
   - Canonical final: `https://www.matchwalls.com/collections/murales`.
   - H1 final: `Todos los Papeles Pintados`.

La redirección `/pages/facade-variants/test` -> `/` es un residuo legacy incorrecto, pero no debe mezclarse con la consolidación de cadenas. Requiere lote propio o decisión posterior.

## Recomendación

`REQUIERE DECISION HUMANA`

Crear lote ejecutable separado: `MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2`.

Estrategia recomendada: actualizar solo el primer salto de cada cadena para apuntar directamente al destino final. No borrar las redirecciones intermedias, porque pueden tener enlaces externos o históricos propios.

