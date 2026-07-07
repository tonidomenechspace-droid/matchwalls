# 2026-06-27 - Resumen de redirecciones de riesgo

Lote de lectura: `MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C`

Estado: `INCOMPLETO`

## Verificado

- Conteo actual de redirecciones en Shopify Admin GraphQL: `635`.
- Consulta validada contra schema Admin GraphQL antes de ejecutarse.
- No se ha ejecutado ninguna mutación.
- No se ha creado, modificado ni eliminado ninguna redirección.

## Limitaciones

- No existe export local completo de las 635 redirecciones en el workspace revisado.
- Shopify CLI no está disponible en este entorno.
- Por tanto, la matriz completa de 635 redirecciones queda pendiente de exportación específica.

## Búsquedas dirigidas ejecutadas

| Patrón | Resultado verificado | Estado |
|---|---:|---|
| `facade` | 1 redirección encontrada: `/pages/facade-variants/test` -> `/` | `INCORRECTO` porque las variantes localizadas siguen apareciendo en sitemap y redirigen |
| `black-friday` | 0 redirecciones encontradas | `REQUIERE DECISION HUMANA` |
| `matchalls` | 0 redirecciones encontradas | `INCORRECTO` si la URL typo sigue indexable |
| `norid` | 0 redirecciones encontradas | `INCORRECTO` si los productos typo siguen indexables |
| `enchathed` | 0 redirecciones encontradas | `INCORRECTO` si los productos typo siguen indexables |
| `muestra` | 6 redirecciones encontradas | `VERIFICADO PERO MEJORABLE` |
| `matchwallsmurals` | 334 redirecciones encontradas | `REQUIERE DECISION HUMANA` |
| `matchwallswallpapers` | 44 redirecciones encontradas | `REQUIERE DECISION HUMANA` |
| `-1` | 97 coincidencias de búsqueda, no interpretables como sufijo exacto sin export completo | `INCOMPLETO` |

## Conclusión

Las redirecciones existen y son numerosas, pero no se puede declarar correcta la arquitectura de redirecciones sin export completo. El siguiente diagnóstico específico debe generar una matriz con:

- `id`
- `path`
- `target`
- idioma detectado
- tipo de recurso
- si el destino existe
- si el destino redirige de nuevo
- si hay cadena o bucle
- si la ruta antigua sigue en sitemap
- recomendación: conservar, consolidar, corregir, eliminar o crear sustituta

