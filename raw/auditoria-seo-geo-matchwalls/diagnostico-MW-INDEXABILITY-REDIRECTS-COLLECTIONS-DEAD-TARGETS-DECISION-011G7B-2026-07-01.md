# MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-DECISION-011G7B

Fecha: 2026-07-01  
Tipo: diagnostico/decision de solo lectura  
Estado final: `REQUIERE DECISION HUMANA`

## 1. Alcance

Lote de decision para 5 redirects de colecciones ES que apuntan a targets 404.

No se modifico Shopify. No se tocaron redirects, colecciones, productos, paginas, tema, traducciones, canonicals, precios ni inventario.

## 2. Documentos leidos

- `registro-cambios-ejecutados.md`.
- `cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`.
- `plan-operativo-vigente-y-cola-lotes-seo-geo-2026-06-30.md`.
- `diagnostico-MW-INDEXABILITY-REDIRECTS-PRODUCTS-PAGES-DIAG-011G7-2026-06-30.md`.
- Evidencias de cierre `MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-REPOINT-PAGE-011G7A1`.

## 3. Estado Admin verificado

Los 5 redirects siguen existiendo en Shopify:

| ID | Path | Target |
|---|---|---|
| `gid://shopify/UrlRedirect/405254897891` | `/collections/kids` | `/collections/kids-rollos` |
| `gid://shopify/UrlRedirect/408478843107` | `/collections/patrones-grandes-rollos` | `/collections/papel-pintado-estampado-grande` |
| `gid://shopify/UrlRedirect/408478974179` | `/collections/semi-lisos-rollos` | `/collections/semi-lisos-papel-pintado` |
| `gid://shopify/UrlRedirect/408479006947` | `/collections/moderno-rollos` | `/collections/moderno-papel-pintado` |
| `gid://shopify/UrlRedirect/408719425763` | `/collections/lienzos-artista` | `/collections/lienzos-abstractos` |

Comprobacion exacta por handle:

- `kids-rollos`: no existe como coleccion Admin.
- `papel-pintado-estampado-grande`: no existe como coleccion Admin.
- `semi-lisos-papel-pintado`: no existe como coleccion Admin.
- `moderno-papel-pintado`: no existe como coleccion Admin.
- `lienzos-abstractos`: no existe como coleccion Admin.

## 4. QA publico y sitemap

Resultado publico:

- Los 5 paths fuente devuelven 301.
- Los 5 targets devuelven 404.
- Las 5 rutas terminan con canonical `https://www.matchwalls.com/404`.
- Ninguna fuente ni ningun target aparece en sitemap.

Sitemap:

- 29 archivos leidos.
- 7.274 URLs.
- 0 errores en lectura repetida.

## 5. Candidatos encontrados

| Fuente | Candidato | Estado | Confianza | Motivo |
|---|---|---|---|---|
| `/collections/kids` | `/collections/kids-murales` | 200 / en sitemap | alta | Equivalencia semantica fuerte: infantil/kids, coleccion viva, 294 productos |
| `/collections/patrones-grandes-rollos` | `/collections/papel-pintado-estampados-pequenos` | 200 / en sitemap | baja | No equivale: fuente y target antiguo hablan de grandes; candidato tiene handle de pequenos |
| `/collections/semi-lisos-rollos` | sin candidato seguro | n/a | nula | No se encontro coleccion actual equivalente |
| `/collections/moderno-rollos` | `/collections/lo-mas-contemporaneo-murales` | 200 / en sitemap | media-baja | Moderno/contemporaneo podria ser cercano, pero no es equivalencia exacta demostrada |
| `/collections/lienzos-artista` | `/collections/murales-estilo-artistico` | 200 / en sitemap | baja | Lienzos no equivale a papel pintado artistico; ademas la linea lienzos/cuadros fue limpiada en 011G5B1 |

## 6. Decision recomendada

Recomendacion quirurgica y conservadora:

1. Repuntar solo `/collections/kids` hacia `/collections/kids-murales`.
2. Eliminar los otros 4 redirects porque no tienen equivalencia segura:
   - `/collections/patrones-grandes-rollos`.
   - `/collections/semi-lisos-rollos`.
   - `/collections/moderno-rollos`.
   - `/collections/lienzos-artista`.

Motivo:

- Mantiene el valor de un redirect con equivalencia fuerte.
- Evita enviar usuarios y crawlers a paginas no equivalentes o demasiado genericas.
- Elimina 301 -> 404, que es peor que un 404 directo cuando no hay destino real.
- No inventa equivalencias comerciales.

## 7. Lote de ejecucion propuesto

Nombre recomendado:

`MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-SAFE-CLEANUP-011G7B1`

Alcance propuesto:

- Actualizar 1 redirect:
  - `gid://shopify/UrlRedirect/405254897891`
  - `/collections/kids`
  - de `/collections/kids-rollos`
  - a `/collections/kids-murales`
- Eliminar 4 redirects:
  - `gid://shopify/UrlRedirect/408478843107`
  - `gid://shopify/UrlRedirect/408478974179`
  - `gid://shopify/UrlRedirect/408479006947`
  - `gid://shopify/UrlRedirect/408719425763`

No autorizado todavia. Requiere aprobacion exacta:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-SAFE-CLEANUP-011G7B1`

## 8. Riesgos

- Si existe una decision comercial no documentada para conservar "moderno", "patrones grandes", "semi-lisos" o "lienzos", debe indicarse antes de aprobar el lote de ejecucion.
- Repuntar a categorias parciales podria contaminar señales SEO/GEO por falta de equivalencia semantica.
- Eliminar redirects sin equivalencia puede hacer que enlaces antiguos pasen a 404 directo; aun asi es mas honesto que 301 -> 404 o 301 hacia una categoria no equivalente.

## 9. Pruebas posteriores exigidas si se aprueba 011G7B1

- Admin: 1 redirect actualizado y 4 eliminados.
- Publico:
  - `/collections/kids` -> 301 -> `/collections/kids-murales` -> 200.
  - Las otras 4 fuentes -> 404 directo.
- Sitemaps:
  - Fuentes antiguas 0 apariciones.
  - Targets muertos 0 apariciones.
  - `/collections/kids-murales` 1 aparicion.
- Canonical destino: `https://www.matchwalls.com/collections/kids-murales`.

## 10. Evidencias

- `admin-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-DECISION-011G7B-2026-07-01.csv`.
- `qa-publico-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-DECISION-011G7B-2026-07-01.csv`.
- `candidatos-MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-DECISION-011G7B-2026-07-01.csv`.
