# Propuesta de lote MW-INDEXABILITY-REDIRECTS-COLLECTIONS-MURALES-COLLISION-CLEANUP-011F4

Fecha: 2026-06-28  
Estado: `REQUIERE DECISION HUMANA`

## Objetivo

Eliminar una redirección Admin legacy que colisiona con una colección real e indexable y bloquea la consolidación futura de redirects de colecciones.

## Alcance exacto

Eliminar 1 redirección Shopify Admin:

- ID: `gid://shopify/UrlRedirect/1534386274680`.
- Path: `/collections/murales`.
- Target: `/en/collections/all-matchwallsmurals-murals`.

No incluye:

- Cambiar handles.
- Cambiar canonicals.
- Cambiar colecciones.
- Cambiar traducciones.
- Cambiar productos.
- Cambiar sitemap manualmente.
- Consolidar `/collections/papeles-pintados`.
- Eliminar otros redirects hacia `/collections/murales`.
- Tocar redirects `matchwallsmurals` globales.

## Evidencia

`VERIFICADO Y CORRECTO`

- La colección real `gid://shopify/Collection/439953719523` existe con handle base `murales`.
- `/collections/murales` devuelve 200 público y `pageType=collection`.
- `/collections/murales` está en sitemap exacto.
- `/collections/murales` tiene canonical propio.
- `/en/collections/all-matchwallsmurals-murals` es el handle traducido EN de la misma colección, no una colección independiente.
- La redirección conflictiva existe en Admin y bloqueó 011F2 con el error: `Destino no puede redirigir a otro redireccionamiento`.

## Valor actual

`RIESGO CRITICO`

Redirect Admin:

- `gid://shopify/UrlRedirect/1534386274680`: `/collections/murales` -> `/en/collections/all-matchwallsmurals-murals`.

## Valor propuesto

`REQUIERE DECISION HUMANA`

- Eliminar la redirección `gid://shopify/UrlRedirect/1534386274680`.
- No crear sustitución.
- Mantener intacta la colección real `/collections/murales`.

## Riesgos

`VERIFICADO PERO MEJORABLE`

- Riesgo bajo en storefront ES porque `/collections/murales` ya responde 200 como colección real.
- Riesgo bajo en EN porque `/en/collections/all-matchwallsmurals-murals` ya responde 200 como URL localizada.
- Riesgo técnico: la reversión por `urlRedirectCreate` está validada contra schema, pero no ejecutada. Shopify podría rechazar recrear una redirección cuyo path colisiona con una colección real.
- No garantiza mejora de rankings ni indexación.

## Respaldo disponible

`VERIFICADO Y CORRECTO`

Valor a restaurar si fuera necesario:

- Path: `/collections/murales`.
- Target: `/en/collections/all-matchwallsmurals-murals`.

## Método exacto de ejecución propuesto

`REQUIERE DECISION HUMANA`

Mutación validada contra schema:

- `urlRedirectDelete(id: "gid://shopify/UrlRedirect/1534386274680")`.

## Método de reversión

`VERIFICADO PERO MEJORABLE`

Intentar recrear el redirect con mutación validada:

- `urlRedirectCreate(urlRedirect: { path: "/collections/murales", target: "/en/collections/all-matchwallsmurals-murals" })`.

Limitación explícita: al ser una colisión con una colección real, la reversión está validada técnicamente por schema, pero no puede considerarse garantizada hasta probarse. Por eso este lote debe ejecutarse solo si aceptamos que el redirect es deuda legacy no pública y que su eliminación es el estado deseado.

## Pruebas posteriores obligatorias

`REQUIERE DECISION HUMANA`

1. Readback Admin por GID: confirmar que el redirect eliminado ya no existe.
2. Búsqueda Admin `path:/collections/murales`: confirmar 0 redirects.
3. QA público:
   - `/collections/murales` -> 200.
   - canonical `https://www.matchwalls.com/collections/murales`.
   - H1 `Todos los Papeles Pintados`.
   - sin meta robots `noindex`.
4. QA localizado:
   - `/en/collections/all-matchwallsmurals-murals` -> 200.
5. Reintentar diagnóstico de consolidación de `/collections/papeles-pintados` solo después de verificar 011F4.

## Aprobación requerida

Para ejecutar este lote, Daniel debe responder exactamente:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-COLLECTIONS-MURALES-COLLISION-CLEANUP-011F4`
