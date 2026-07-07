# Diagnostico MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-DECISION-011G4B

Fecha: 2026-06-30  
Tipo: diagnostico de solo lectura y decision requerida  
Estado final: REQUIERE DECISION HUMANA  

## 1. Contexto

Este diagnostico continua el bloque de indexabilidad y redirecciones despues de:

- `MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1`
- `MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-CLEANUP-011G3A`
- `MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A`

El objetivo es revisar el unico redirect FR prioritario que seguia terminando en 404 tras consolidar las cadenas FR.

No se modifico Shopify.

## 2. Estado real Shopify comprobado

Consulta de lectura en Shopify Admin:

- Total redirects Shopify: 614 EXACT.
- `/fr/*`: 23 redirects EXACT.
- `/en/*`: 2 redirects EXACT.
- `/ar/*`: 4 redirects EXACT.
- `path:/products/*`: 18 redirects EXACT.
- `path:/pages/*`: 4 redirects EXACT.
- `path:/collections/*`: 41 redirects EXACT.
- `target:/`: 36 redirects EXACT.
- `muestra`: 6 redirects EXACT.
- `matchwallsmurals`: 333 redirects EXACT.
- `matchwallswallpapers`: 44 redirects EXACT.

## 3. Redirect FR incorrecto revisado

| ID Shopify | Path | Target actual | Resultado publico |
|---|---|---|---|
| `gid://shopify/UrlRedirect/417581367523` | `/fr/collections/painted-papers-baller-matchwallswallpapers` | `/fr/collections/mural-murals-matchwallsmurals` | `301 -> 404` |

Estado: INCORRECTO.

## 4. Candidata FR encontrada

Se revisaron sitemaps publicos buscando colecciones FR potencialmente relacionadas.

Archivo:

- `sitemap-fr-collection-candidates-dead-target-011G4B-2026-06-30.csv`

Resultado:

- URLs FR de coleccion en sitemap: 100.
- Candidatas por patron semantico: 4.
- Candidata mas plausible por tema de "salle de bain":
  - `/fr/collections/salles-de-bain-peintes`

Verificacion publica:

| URL | Estado | Canonical | H1 | Noindex |
|---|---:|---|---|---|
| `/fr/collections/salles-de-bain-peintes` | 200 | `https://www.matchwalls.com/fr/collections/salles-de-bain-peintes` | `Papier Peint pour Salle de Bain` | NO |

Archivo:

- `qa-publico-fr-dead-target-candidate-detail-011G4B-2026-06-30.csv`

## 5. Limitacion critica

No queda demostrado al 100% que el antiguo path:

`/fr/collections/painted-papers-baller-matchwallswallpapers`

equivalga semanticamente a:

`/fr/collections/salles-de-bain-peintes`

La candidata es razonable por busqueda de sitemap y tema de coleccion, pero el handle antiguo contiene una forma defectuosa (`baller`) y no permite confirmar intencion comercial sin decision humana.

## 6. Opciones de decision

### Opcion A: repuntar a candidata FR real

Lote posible:

`MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-REPOINT-BATHROOM-011G4B1`

Accion:

- Actualizar el redirect:
  - Path: `/fr/collections/painted-papers-baller-matchwallswallpapers`
  - Target actual: `/fr/collections/mural-murals-matchwallsmurals`
  - Target propuesto: `/fr/collections/salles-de-bain-peintes`

Ventaja:

- La URL antigua dejaria de terminar en 404 y pasaria previsiblemente a `301 -> 200`.

Riesgo:

- Si la intencion antigua no era "salle de bain", el repuntado seria semanticamente incorrecto.

### Opcion B: eliminar redirect muerto

Lote posible:

`MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-CLEANUP-011G4B2`

Accion:

- Eliminar el redirect `gid://shopify/UrlRedirect/417581367523`.

Ventaja:

- Se elimina una regla `301 -> 404`.

Riesgo:

- La URL antigua pasaria previsiblemente a 404 directo, sin recuperar valor hacia una coleccion equivalente.

### Opcion C: mantener en STANDBY

Accion:

- No tocar hasta revisar historico comercial, Search Console, backlinks o mapa de equivalencias de colecciones FR.

Ventaja:

- Evita un repuntado semantico incorrecto.

Riesgo:

- Se mantiene un `301 -> 404` en FR.

## 7. Recomendacion profesional

Estado recomendado: REQUIERE DECISION HUMANA.

No recomiendo ejecutar automaticamente ni repuntado ni eliminacion sin confirmacion de Daniel.

Si Daniel confirma que el antiguo path corresponde a la intencion "papier peint salle de bain", preparar propuesta formal de escritura:

`MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-REPOINT-BATHROOM-011G4B1`

Si Daniel no puede confirmar equivalencia o prefiere no asumirla, preparar propuesta formal de eliminacion:

`MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-CLEANUP-011G4B2`

## 8. Estado final

REQUIERE DECISION HUMANA.

