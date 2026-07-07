# Propuesta de lote MW-INDEXABILITY-REDIRECTS-COLLECTIONS-PAPELES-CONSOLIDATION-011F5

Fecha: 2026-06-28  
Estado: `REQUIERE DECISION HUMANA`

## Objetivo

Consolidar la cadena legacy principal de colecciones para que `/collections/papeles-pintados` apunte directamente a la colección canónica real `/collections/murales`.

## Dependencia cumplida

`CORREGIDO Y VERIFICADO`

El lote 011F4 eliminó la colisión Admin:

- Antes: `/collections/murales` -> `/en/collections/all-matchwallsmurals-murals`.
- Ahora: `path:/collections/murales = 0`, precisión `EXACT`.

## Alcance exacto propuesto

Actualizar 1 redirección Shopify Admin:

- ID: `gid://shopify/UrlRedirect/410027000035`.
- Path: `/collections/papeles-pintados`.
- Target actual: `/collections/papeles-pintados-old`.
- Target propuesto: `/collections/murales`.

No incluye:

- Eliminar redirecciones.
- Cambiar handles.
- Cambiar canonicals.
- Cambiar colecciones.
- Cambiar traducciones.
- Tocar `/collections/papeles-pintados-old`.
- Tocar `/collections/murales-mvp`.
- Tocar `/collections/%20papeles-pintados`.
- Tocar redirects internacionales o `matchwallsmurals`.

## Recursos que se conservarán sin cambios

`VERIFICADO Y CORRECTO`

- `gid://shopify/UrlRedirect/417318207715`: `/collections/papeles-pintados-old` -> `/collections/murales`.

Motivo: mantener compatibilidad con enlaces históricos que apunten directamente a la URL intermedia.

## Evidencia

`VERIFICADO Y CORRECTO`

- `/collections/murales` es colección real: `gid://shopify/Collection/439953719523`.
- Productos: 758.
- Publicaciones: 9.
- `/collections/murales` devuelve 200 directo.
- Canonical público: `https://www.matchwalls.com/collections/murales`.
- H1 público: `Todos los Papeles Pintados`.
- `path:/collections/murales = 0` tras 011F4.
- Mutación `urlRedirectUpdate` validada contra schema Shopify Admin.

## Riesgos

`VERIFICADO PERO MEJORABLE`

- Riesgo bajo: cambio de un solo target.
- Riesgo positivo esperado: elimina un salto de redirección en la cadena principal.
- No garantiza ranking, indexación ni tráfico.
- Puede haber caché/CDN temporal tras la actualización.

## Respaldo disponible

`VERIFICADO Y CORRECTO`

Valor original a restaurar si hiciera falta:

- `gid://shopify/UrlRedirect/410027000035`: `/collections/papeles-pintados` -> `/collections/papeles-pintados-old`.

## Método exacto de ejecución propuesto

`REQUIERE DECISION HUMANA`

Mutación validada:

- `urlRedirectUpdate`.

Input:

- ID: `gid://shopify/UrlRedirect/410027000035`.
- `path`: `/collections/papeles-pintados`.
- `target`: `/collections/murales`.

## Método exacto de reversión

`VERIFICADO Y CORRECTO`

Restaurar con `urlRedirectUpdate`:

- ID: `gid://shopify/UrlRedirect/410027000035`.
- `path`: `/collections/papeles-pintados`.
- `target`: `/collections/papeles-pintados-old`.

## Pruebas posteriores obligatorias

`REQUIERE DECISION HUMANA`

1. Readback Admin por GID.
2. QA público:
   - `/collections/papeles-pintados` debe acabar en `/collections/murales`.
   - `/collections/papeles-pintados-old` debe seguir acabando en `/collections/murales`.
   - `/collections/murales` debe responder 200 directo.
3. Verificar canonical final:
   - `https://www.matchwalls.com/collections/murales`.
4. Verificar H1:
   - `Todos los Papeles Pintados`.
5. Verificar ausencia de meta robots `noindex` en destino final.

## Aprobación requerida

Para ejecutar este lote, Daniel debe responder exactamente:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-COLLECTIONS-PAPELES-CONSOLIDATION-011F5`
