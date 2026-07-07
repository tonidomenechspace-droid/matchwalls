# Diagnóstico MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEEP-CHAIN-DIAG-011F3

Fecha: 2026-06-28  
Estado global: `RIESGO CRITICO`

## Alcance

Diagnóstico de solo lectura sobre la cadena profunda de redirecciones de colecciones detectada en 011F2.

No se han creado, modificado ni eliminado redirecciones. No se han cambiado handles, canonicals, colecciones, productos, páginas, temas ni contenido.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `ejecucion-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.md`.
- `shopify-blocker-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.csv`.

## Hallazgo principal

`RIESGO CRITICO`

Existe una colisión entre una colección real y una redirección legacy:

- Colección real Admin:
  - ID: `gid://shopify/Collection/439953719523`.
  - Handle base: `murales`.
  - URL pública ES: `https://www.matchwalls.com/collections/murales`.
  - Título: `Todos los Papeles Pintados`.
  - Productos: 758.
  - Publicaciones: 9.
  - `seo.hidden`: null.
  - Sitemap: presente.

- Redirect Admin conflictivo:
  - ID: `gid://shopify/UrlRedirect/1534386274680`.
  - Path: `/collections/murales`.
  - Target: `/en/collections/all-matchwallsmurals-murals`.

El storefront responde `200` para `/collections/murales` como colección real; sin embargo, el registro de redirección sigue existiendo en Admin y bloquea mutaciones porque Shopify no permite usar como target una ruta que también aparece como path de redirect.

## Traducciones verificadas

`VERIFICADO Y CORRECTO`

`/en/collections/all-matchwallsmurals-murals` no es una colección independiente. Es el handle traducido EN de la colección base `murales`.

Handles traducidos verificados:

- EN: `all-matchwallsmurals-murals`.
- FR: `tous-les-peintures-murales-matchwallsmurals`.
- DE: `alle-matchwallsmurals-wandbilder`.
- NL: `alle-matchwallsmurals-muurschilderingen`.

## Redirecciones Admin relacionadas

`VERIFICADO PERO MEJORABLE`

Cadena principal:

1. `/collections/papeles-pintados` -> `/collections/papeles-pintados-old`.
2. `/collections/papeles-pintados-old` -> `/collections/murales`.

Colisión:

3. `/collections/murales` -> `/en/collections/all-matchwallsmurals-murals`.

Dependientes hacia `/collections/murales`:

- `/collections/murales-mvp` -> `/collections/murales`.
- `/collections/%20papeles-pintados` -> `/collections/murales`.

También existen redirects internacionales legacy hacia `/en/collections/all-matchwallsmurals-murals`, en idiomas fuera del alcance prioritario inmediato.

Archivo: `admin-redirects-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEEP-CHAIN-DIAG-011F3-2026-06-28.csv`.

## QA público HTTP

`VERIFICADO Y CORRECTO`

Cabeceras HTTP reales verificadas:

- `/collections/papeles-pintados` devuelve 301 -> `/collections/papeles-pintados-old` -> 301 -> `/collections/murales` -> 200.
- `/collections/papeles-pintados-old` devuelve 301 -> `/collections/murales` -> 200.
- `/collections/murales` devuelve 200 directo como `pageType=collection`.
- `/collections/murales-mvp` devuelve 301 -> `/collections/murales` -> 200.
- `/collections/%20papeles-pintados` devuelve 301 -> `/collections/murales` -> 200.
- `/en/collections/all-matchwallsmurals-murals` devuelve 200.
- FR/DE/NL localizados devuelven 200.

Archivo: `qa-publico-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEEP-CHAIN-DIAG-011F3-2026-06-28.csv`.

## Sitemap exacto

`VERIFICADO Y CORRECTO`

Presentes en sitemap:

- `https://www.matchwalls.com/collections/murales`.
- `https://www.matchwalls.com/en/collections/all-matchwallsmurals-murals`.
- `https://www.matchwalls.com/fr/collections/tous-les-peintures-murales-matchwallsmurals`.
- `https://www.matchwalls.com/de/collections/alle-matchwallsmurals-wandbilder`.
- `https://www.matchwalls.com/nl/collections/alle-matchwallsmurals-muurschilderingen`.

No presentes como URL exacta en sitemap:

- `https://www.matchwalls.com/collections/papeles-pintados`.
- `https://www.matchwalls.com/collections/papeles-pintados-old`.
- `https://www.matchwalls.com/collections/murales-mvp`.
- `https://www.matchwalls.com/collections/%20papeles-pintados`.

Archivo exacto: `qa-sitemap-exact-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEEP-CHAIN-DIAG-011F3-2026-06-28.csv`.

## Conclusión

`RIESGO CRITICO`

La URL `/collections/murales` debe considerarse una URL canónica real, publicada e indexable. El redirect Admin con el mismo path es deuda legacy/conflictiva.

No se recomienda consolidar `/collections/papeles-pintados` hasta retirar o resolver primero la colisión del redirect `/collections/murales`.

## Recomendación

`REQUIERE DECISION HUMANA`

Crear lote ejecutable separado:

`MW-INDEXABILITY-REDIRECTS-COLLECTIONS-MURALES-COLLISION-CLEANUP-011F4`

Objetivo: eliminar únicamente el redirect Admin conflictivo `/collections/murales` -> `/en/collections/all-matchwallsmurals-murals`, sin tocar todavía la cadena `/collections/papeles-pintados`.

Después de verificar 011F4, preparar un segundo lote para consolidar la cadena principal:

`MW-INDEXABILITY-REDIRECTS-COLLECTIONS-PAPELES-CONSOLIDATION-011F5`.
