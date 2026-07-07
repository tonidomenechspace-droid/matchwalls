# Diagnóstico MW-INDEXABILITY-REDIRECTS-COLLECTIONS-LEGACY-DEPENDENTS-DIAG-011F6

Fecha: 2026-06-29  
Hora de registro: 10:35 +02:00  
Tipo: diagnóstico de solo lectura  
Estado final: `VERIFICADO PERO MEJORABLE`

## Alcance

Se auditaron los redirects legacy dependientes que quedaban tras los lotes 011F4 y 011F5:

- Redirects con destino `/collections/murales`.
- Redirects con destino `/en/collections/all-matchwallsmurals-murals`.
- Verificación pública de cada fuente legacy.
- Verificación exacta de sitemap para fuentes y destinos.
- Verificación ligera de canonical, H1, noindex visible y hreflang en destinos principales.

No se ejecutaron mutaciones, no se modificaron redirects, no se cambiaron handles y no se tocó contenido Shopify.

## Evidencia Admin Shopify

`VERIFICADO Y CORRECTO`

Archivos:

- `admin-redirects-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-LEGACY-DEPENDENTS-DIAG-011F6-2026-06-29.csv`
- `admin-counts-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-LEGACY-DEPENDENTS-DIAG-011F6-2026-06-29.csv`

Conteos verificados:

- `target:/collections/murales`: 4 redirects, precisión `EXACT`.
- `target:/en/collections/all-matchwallsmurals-murals`: 8 redirects, precisión `EXACT`.
- `path:/collections/murales`: 0 redirects, precisión `EXACT`.
- `path:/collections/murales-mvp`: 1 redirect, precisión `EXACT`.
- `path:/collections/%20papeles-pintados`: 1 redirect, precisión `EXACT`.
- `path:/collections/papeles-pintados`: 1 redirect, precisión `EXACT`.
- `path:/collections/papeles-pintados-old`: 1 redirect, precisión `EXACT`.

Conclusión Admin: la colisión crítica `/collections/murales` corregida en 011F4 sigue resuelta. No existe redirect que capture la URL real de colección `/collections/murales`.

## Verificación pública

`VERIFICADO Y CORRECTO`

Archivo:

- `qa-publico-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-LEGACY-DEPENDENTS-DIAG-011F6-2026-06-29.csv`

Resultado:

- 12 fuentes legacy devuelven 1 salto y terminan en `200`.
- 2 destinos canónicos devuelven `200` directo.
- No se detectó meta robots `noindex` ni `X-Robots-Tag: noindex` visible en las URLs finales revisadas.

Destinos finales:

- Fuentes ES legacy: terminan en `https://www.matchwalls.com/collections/murales`.
- Fuentes EN/no prioritarias legacy: terminan en `https://www.matchwalls.com/en/collections/all-matchwallsmurals-murals`.

Canonical y H1:

- `/collections/murales`: canonical `https://www.matchwalls.com/collections/murales`, H1 `Todos los Papeles Pintados`.
- `/en/collections/all-matchwallsmurals-murals`: canonical `https://www.matchwalls.com/en/collections/all-matchwallsmurals-murals`, H1 `All Wallpaper`.

## Verificación sitemap exacta

`VERIFICADO Y CORRECTO`

Archivo:

- `qa-sitemap-exact-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-LEGACY-DEPENDENTS-DIAG-011F6-2026-06-29.csv`

Resultado tras comparación exacta de `<loc>`:

- Las 12 fuentes legacy no están en sitemap exacto.
- Sí están en sitemap exacto las URLs canónicas principales:
  - `https://www.matchwalls.com/collections/murales`
  - `https://www.matchwalls.com/en/collections/all-matchwallsmurals-murals`
  - `https://www.matchwalls.com/fr/collections/tous-les-peintures-murales-matchwallsmurals`
  - `https://www.matchwalls.com/de/collections/alle-matchwallsmurals-wandbilder`
  - `https://www.matchwalls.com/nl/collections/alle-matchwallsmurals-muurschilderingen`

Nota: se detectó inicialmente una falsa coincidencia por prefijo con URLs como `/collections/papeles-pintados-color...`; se corrigió la comprobación para comparar únicamente valores exactos de `<loc>`.

## Verificación hreflang de destinos

`VERIFICADO Y CORRECTO`

Archivo:

- `qa-hreflang-targets-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-LEGACY-DEPENDENTS-DIAG-011F6-2026-06-29.csv`

Los dos destinos principales revisados incluyen 8 hreflang:

- `x-default`
- `es`
- `pt`
- `fr`
- `de`
- `it`
- `en`
- `nl`

IT y PT no forman parte del alcance prioritario actual, pero aparecen publicados como variantes hreflang.

## Clasificación

`VERIFICADO PERO MEJORABLE`

Archivo:

- `clasificacion-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-LEGACY-DEPENDENTS-DIAG-011F6-2026-06-29.csv`

Resumen:

- 1 redirect: `VERIFICADO Y CORRECTO` / conservar.
- 3 redirects: `VERIFICADO PERO MEJORABLE` / conservar en `STANDBY`.
- 8 redirects: `STANDBY`.

Clasificación operativa:

| Grupo | Cantidad | Recomendación |
|---|---:|---|
| `/collections/papeles-pintados` | 1 | Conservar. Legacy ES semántico, 1 salto, sin presencia en sitemap exacto. |
| `/collections/papeles-pintados-old`, `/collections/%20papeles-pintados`, `/collections/murales-mvp` | 3 | Conservar en `STANDBY`; no borrar sin datos de tráfico. |
| EN legacy hacia `/en/collections/all-matchwallsmurals-murals` | 1 | Conservar en `STANDBY`; revisar con datos EN antes de retirar. |
| Idiomas no prioritarios legacy hacia EN | 7 | `STANDBY`; requieren política global de idiomas legacy antes de tocar. |

## Riesgos

`VERIFICADO PERO MEJORABLE`

- Eliminar redirects legacy sin datos de Search Console, logs o analytics puede convertir enlaces históricos en 404.
- Reorientar idiomas no prioritarios sin política global puede generar incoherencias internacionales.
- Aunque los redirects están técnicamente limpios, siguen siendo deuda documental y deben permanecer clasificados.

## Conclusión

`VERIFICADO PERO MEJORABLE`

No se recomienda una mutación inmediata para 011F6.

El estado actual es estable:

- No hay colisión sobre `/collections/murales`.
- Los redirects legacy revisados son de 1 salto.
- Las fuentes legacy no están en sitemap exacto.
- Los destinos finales son canónicos, indexables visualmente y con hreflang presente.

Recomendación: conservar estos redirects en `STANDBY` hasta disponer de datos de tráfico/impresiones o hasta abrir una política global de idiomas legacy. El trabajo de indexabilidad puede continuar con el siguiente bloque de clasificación/redirecciones globales.
