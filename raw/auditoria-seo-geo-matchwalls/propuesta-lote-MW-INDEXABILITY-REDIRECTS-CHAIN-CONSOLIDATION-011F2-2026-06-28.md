# Propuesta de lote MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2

Fecha: 2026-06-28  
Estado: `REQUIERE DECISION HUMANA`

## Objetivo

Consolidar de forma quirúrgica dos cadenas de redirección confirmadas, reduciendo un salto intermedio sin eliminar cobertura histórica.

## Alcance exacto

Solo 2 redirecciones Shopify Admin:

1. `gid://shopify/UrlRedirect/405088796899`
2. `gid://shopify/UrlRedirect/410027000035`

No incluye:

- Eliminación de redirecciones.
- Cambios de handles.
- Cambios de canonicals.
- Cambios de contenido, productos, colecciones, páginas, menús ni tema.
- Limpieza de `facade`.
- Bloques `matchwallsmurals` / `matchwallswallpapers`.

## Valores actuales y propuestos

| ID | Path | Target actual | Target propuesto | Estado |
|---|---|---|---|---|
| `gid://shopify/UrlRedirect/405088796899` | `/pages/como-tomar-medidas-paredes-y-techos-boton` | `/pages/medidas-paredes-techos` | `/pages/medidas-paredes` | `REQUIERE DECISION HUMANA` |
| `gid://shopify/UrlRedirect/410027000035` | `/collections/papeles-pintados` | `/collections/papeles-pintados-old` | `/collections/murales` | `REQUIERE DECISION HUMANA` |

## Recursos que se conservarán sin cambios

`VERIFICADO Y CORRECTO`

- `gid://shopify/UrlRedirect/409984762083`: `/pages/medidas-paredes-techos` -> `/pages/medidas-paredes`.
- `gid://shopify/UrlRedirect/417318207715`: `/collections/papeles-pintados-old` -> `/collections/murales`.

Motivo: mantener compatibilidad con enlaces históricos que apunten directamente a las URLs intermedias.

## Evidencia

`VERIFICADO PERO MEJORABLE`

- Admin confirma las 5 redirecciones por GID.
- Navegación pública confirma destino final, canonical, title, H1 y ausencia de meta robots `noindex` visible en destino.
- `urlRedirectUpdate` validado contra schema Shopify Admin antes de proponer ejecución.
- Cabeceras HTTP exactas públicas: `NO ACCESIBLE` desde este entorno por limitación de PowerShell/curl; navegador sí confirmó destino final.

## Riesgos

`VERIFICADO PERO MEJORABLE`

- Riesgo bajo si solo se actualizan los dos targets indicados.
- Riesgo SEO positivo esperado: menor cadena, señales más directas hacia canonical final.
- No garantiza mejora de rankings ni indexación.
- Riesgo de analítica: el histórico de fuente puede cambiar de ruta intermedia a final directo.
- Riesgo de caché/CDN: puede tardar en reflejarse públicamente.

## Respaldo disponible

`VERIFICADO Y CORRECTO`

Valores originales a restaurar si hay fallo:

- `gid://shopify/UrlRedirect/405088796899`: target original `/pages/medidas-paredes-techos`.
- `gid://shopify/UrlRedirect/410027000035`: target original `/collections/papeles-pintados-old`.

## Método exacto de ejecución propuesto

`REQUIERE DECISION HUMANA`

Mutación validada: `urlRedirectUpdate`.

Operación 1:

- ID: `gid://shopify/UrlRedirect/405088796899`.
- Input: `path=/pages/como-tomar-medidas-paredes-y-techos-boton`, `target=/pages/medidas-paredes`.

Operación 2:

- ID: `gid://shopify/UrlRedirect/410027000035`.
- Input: `path=/collections/papeles-pintados`, `target=/collections/murales`.

No ejecutar `urlRedirectDelete` en este lote.

## Método exacto de reversión

`VERIFICADO Y CORRECTO`

Si falla cualquier prueba crítica, restaurar los targets originales mediante `urlRedirectUpdate`:

1. `gid://shopify/UrlRedirect/405088796899` -> `/pages/medidas-paredes-techos`.
2. `gid://shopify/UrlRedirect/410027000035` -> `/collections/papeles-pintados-old`.

## Pruebas posteriores obligatorias

`REQUIERE DECISION HUMANA`

1. Readback Admin por GID: confirmar nuevos targets.
2. Navegación pública:
   - `/pages/como-tomar-medidas-paredes-y-techos-boton` -> `/pages/medidas-paredes`.
   - `/pages/medidas-paredes-techos` -> `/pages/medidas-paredes`.
   - `/collections/papeles-pintados` -> `/collections/murales`.
   - `/collections/papeles-pintados-old` -> `/collections/murales`.
3. Confirmar canonical final:
   - `https://www.matchwalls.com/pages/medidas-paredes`.
   - `https://www.matchwalls.com/collections/murales`.
4. Confirmar ausencia de meta robots `noindex` en destino final.
5. Registrar resultado en `registro-cambios-ejecutados.md`.

## Aprobación requerida para ejecutar

Para ejecutar este lote, Daniel debe responder exactamente:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2`

