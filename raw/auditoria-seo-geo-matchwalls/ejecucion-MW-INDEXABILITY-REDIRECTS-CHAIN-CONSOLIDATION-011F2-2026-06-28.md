# Ejecución MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2

Fecha: 2026-06-28  
Estado global: `VERIFICADO PERO MEJORABLE`

## Aprobación

`VERIFICADO Y CORRECTO`

Aprobación exacta recibida:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2`

## Alcance ejecutado

`VERIFICADO PERO MEJORABLE`

Alcance aprobado: 2 actualizaciones de target en redirecciones Shopify Admin.

Resultado real:

1. Medidas: ejecutado y verificado.
2. Colecciones: no ejecutado porque Shopify rechazó el target propuesto con `userErrors`.

No se eliminaron redirecciones. No se cambiaron handles, canonicals, páginas, colecciones, productos, temas ni contenido.

## Respaldo previo

`VERIFICADO Y CORRECTO`

Archivo: `backup-pre-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.csv`.

Valores originales principales:

- `gid://shopify/UrlRedirect/405088796899`: `/pages/como-tomar-medidas-paredes-y-techos-boton` -> `/pages/medidas-paredes-techos`.
- `gid://shopify/UrlRedirect/410027000035`: `/collections/papeles-pintados` -> `/collections/papeles-pintados-old`.

## Operaciones ejecutadas

### Operación 1 - Medidas

`CORREGIDO Y VERIFICADO`

- ID: `gid://shopify/UrlRedirect/405088796899`.
- Path: `/pages/como-tomar-medidas-paredes-y-techos-boton`.
- Target anterior: `/pages/medidas-paredes-techos`.
- Target nuevo: `/pages/medidas-paredes`.
- Resultado Shopify: `userErrors: []`.

### Operación 2 - Colecciones

`INCOMPLETO`

- ID: `gid://shopify/UrlRedirect/410027000035`.
- Path: `/collections/papeles-pintados`.
- Target intentado: `/collections/murales`.
- Resultado Shopify: rechazado.
- Error: `Destino no puede redirigir a otro redireccionamiento`.
- No se modificó esta redirección.

## Causa del bloqueo Shopify

`RIESGO CRITICO`

Shopify Admin confirma que existe una redirección con:

- `gid://shopify/UrlRedirect/1534386274680`: `/collections/murales` -> `/en/collections/all-matchwallsmurals-murals`.

Además, existen redirecciones dependientes que apuntan a `/collections/murales`:

- `/collections/murales-mvp` -> `/collections/murales`.
- `/collections/papeles-pintados-old` -> `/collections/murales`.
- `/collections/%20papeles-pintados` -> `/collections/murales`.

Por este motivo no se debe forzar una consolidación de colecciones dentro de 011F2. Requiere diagnóstico propio.

## Verificación Admin post

`VERIFICADO PERO MEJORABLE`

Archivo: `admin-post-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.csv`.

- Medidas: target nuevo confirmado en Admin.
- Intermedia de medidas: conservada sin cambios.
- Colección principal: sigue con target original por bloqueo Shopify.
- Intermedia de colección: conservada sin cambios.

## Verificación pública post

`VERIFICADO PERO MEJORABLE`

Archivo: `qa-publico-post-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.csv`.

Navegador interno verificó:

- `/pages/como-tomar-medidas-paredes-y-techos-boton` acaba en `/pages/medidas-paredes`.
- `/pages/medidas-paredes-techos` acaba en `/pages/medidas-paredes`.
- `/pages/medidas-paredes` tiene canonical propio y H1 esperado.
- `/collections/papeles-pintados` sigue acabando públicamente en `/collections/murales`.
- `/collections/papeles-pintados-old` sigue acabando públicamente en `/collections/murales`.
- `/collections/murales` muestra canonical propio y H1 esperado en navegador.

Limitación: cabeceras HTTP exactas siguen `NO ACCESIBLE` desde PowerShell/curl en este entorno.

## Decisión de no revertir medidas

`VERIFICADO Y CORRECTO`

No se revirtió la operación 1 porque:

- Fue aceptada por Shopify con `userErrors: []`.
- Readback Admin confirma el target nuevo.
- QA público confirma destino final, canonical y H1.
- El fallo de operación 2 no afecta a la cadena de medidas.

## Método de reversión disponible

`VERIFICADO Y CORRECTO`

Si Daniel decide revertir la consolidación de medidas, ejecutar lote específico para restaurar:

- `gid://shopify/UrlRedirect/405088796899` -> `/pages/medidas-paredes-techos`.

No se recomienda revertir salvo que aparezca incidencia pública real.

## Siguiente paso recomendado

`REQUIERE DECISION HUMANA`

Crear diagnóstico independiente:

`MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEEP-CHAIN-DIAG-011F3`

Objetivo: resolver la contradicción entre Admin y navegación pública en `/collections/murales`, incluyendo el redirect hacia `/en/collections/all-matchwallsmurals-murals`, antes de proponer cualquier consolidación de colecciones.

