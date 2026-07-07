# Diagnóstico MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3

Fecha: 2026-06-29  
Hora de registro: 16:23 +02:00  
Tipo: diagnóstico de solo lectura  
Estado final: `INCORRECTO`

## Alcance

Diagnóstico de los redirects de productos/páginas detectados en 011G que terminaban en `404`.

No se ejecutaron mutaciones, no se modificó Shopify, no se cambiaron redirects, productos, colecciones, páginas, handles, canonicals, sitemaps, tema ni contenido visible.

## Documentos y registros revisados

`VERIFICADO Y CORRECTO`

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `diagnostico-MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G-2026-06-29.md`.
- `ejecucion-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.md`.

## Estado Admin Shopify

`INCORRECTO`

Consulta GraphQL de lectura validada contra schema antes de ejecutarse.

Archivos:

- `admin-redirects-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3-2026-06-29.csv`
- `admin-resource-existence-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3-2026-06-29.csv`

Resultado:

- Los 7 redirects siguen existiendo en Admin.
- Total redirects Admin actual: 620.
- Precisión: `EXACT`.
- `path:/products/*`: 24 redirects, precisión `EXACT`.
- `path:/pages/*`: 4 redirects, precisión `EXACT`.

## Redirects verificados

`INCORRECTO`

| ID | Fuente | Target | Estado público |
|---|---|---|---|
| `gid://shopify/UrlRedirect/408237834467` | `/products/poster-de-papel-mate-calidad-museo-con-marco-de-madera` | `/products/echoing-corridor-3` | 301 -> 404 |
| `gid://shopify/UrlRedirect/408370151651` | `/products/endless-horizon-3` | `/products/echoing-corridor` | 301 -> 404 |
| `gid://shopify/UrlRedirect/408474484963` | `/products/rusted-horizon-marron-copia` | `/products/ember-glow-marron` | 301 -> 404 |
| `gid://shopify/UrlRedirect/412616229091` | `/products/muestra-desnudos-blanco-y-negro` | `/collections/muestras` | 301 -> 404 |
| `gid://shopify/UrlRedirect/408525930723` | `/products/urban-geometrico` | `/products/urban-geometrico-beige` | 301 -> 404 |
| `gid://shopify/UrlRedirect/408525996259` | `/products/urban-geometrico-beige-copia` | `/products/urban-geometrico-gris` | 301 -> 404 |
| `gid://shopify/UrlRedirect/408514429155` | `/products/urban-sketch-beige-copia` | `/products/melodic-flow` | 301 -> 404 |

## Verificación pública

`INCORRECTO`

Archivo:

- `qa-publico-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3-2026-06-29.csv`

Resultado:

- 7/7 fuentes redirigen a `404`.
- 7/7 targets devuelven `404`.
- No hay cadenas múltiples; cada fuente hace un salto hacia un destino muerto.
- Los destinos finales canónicos son páginas `404`.

## Verificación sitemap

`VERIFICADO Y CORRECTO`

Archivo:

- `qa-sitemap-exact-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3-2026-06-29.csv`

Resultado:

- 0/7 fuentes están en sitemap exacto.
- 0/7 targets están en sitemap exacto.
- Errores de lectura de sitemap: 0.

Esto reduce el riesgo de exposición directa en sitemap, pero no corrige el problema de calidad: cualquier usuario, bot o enlace antiguo que llegue a esas fuentes recibe una redirección hacia `404`.

## Existencia de recursos en Admin

`VERIFICADO PERO MEJORABLE`

Se verificaron handles individuales en Admin para evitar depender de una búsqueda amplia.

Resultado:

- 13 handles producto/colección no existen en Admin.
- 1 producto existe, pero está en `DRAFT`:
  - `gid://shopify/Product/8561719247075`
  - handle: `muestra-desnudos-blanco-y-negro`
  - title: `Muestra de Desnudos Blanco y negro`
  - status: `DRAFT`
- La colección `muestras` no existe por ese handle.

## Clasificación

Archivo:

- `clasificacion-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3-2026-06-29.csv`

Resultado:

- 6 redirects: `INCORRECTO` / recomendación técnica: eliminar redirect, salvo que Daniel identifique un sustituto comercial real.
- 1 redirect: `RIESGO CRITICO` / `REQUIERE DECISION HUMANA`:
  - `/products/muestra-desnudos-blanco-y-negro` -> `/collections/muestras`

Motivo del caso especial:

- La fuente existe en Admin como producto `DRAFT`.
- El target `/collections/muestras` no existe.
- No se debe eliminar o repuntar automáticamente porque afecta a política de muestras: podría requerir publicar, noindex, repuntar a una página informativa de muestras o eliminar el redirect.

## Riesgo SEO/GEO

`INCORRECTO`

- Redirects que terminan en `404` son mala experiencia y señal técnica pobre.
- Aunque no están en sitemap, pueden recibir tráfico por enlaces antiguos, cachés, snippets, bots o historiales.
- No se debe repuntar a productos parecidos sin evidencia comercial: sería un soft-404 o una sustitución engañosa.

## Recomendación

`REQUIERE DECISION HUMANA`

No ejecutar cambios todavía dentro de 011G3.

Siguiente lote propuesto:

`MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-CLEANUP-011G3A`

Alcance sugerido:

1. Eliminar 6 redirects claramente muertos:
   - `gid://shopify/UrlRedirect/408237834467`
   - `gid://shopify/UrlRedirect/408370151651`
   - `gid://shopify/UrlRedirect/408474484963`
   - `gid://shopify/UrlRedirect/408525930723`
   - `gid://shopify/UrlRedirect/408525996259`
   - `gid://shopify/UrlRedirect/408514429155`

2. Dejar en `STANDBY` el redirect de muestra:
   - `gid://shopify/UrlRedirect/412616229091`
   - hasta decidir política exacta para producto `DRAFT` y muestras.

No ejecutar sin propuesta formal y aprobación exacta.

## Estado final

`INCORRECTO`

011G3 queda cerrado como diagnóstico de solo lectura. No hay cambios que revertir.
