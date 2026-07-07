# MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-CLEANUP-011G5B1

Fecha: 2026-06-30  
Tipo: escritura Shopify acotada  
Estado final: `CORREGIDO Y VERIFICADO`

## 1. Autorizacion recibida

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-CLEANUP-011G5B1`

## 2. Alcance aprobado

Eliminar exclusivamente 4 redirecciones antiguas ES de lienzos/cuadros que apuntaban a la home `/`.

No se modificaron paginas, productos, colecciones, handles, tema, traducciones, sitemaps, canonicals ni configuraciones externas.

## 3. Precheck

Consulta Admin GraphQL validada contra schema.

| ID | Path | Target | Estado |
|---|---|---|---|
| `gid://shopify/UrlRedirect/1518269596024` | `/collections/lienzos` | `/` | `VERIFICADO Y CORRECTO` |
| `gid://shopify/UrlRedirect/1518269628792` | `/collections/cuadros-rollos` | `/` | `VERIFICADO Y CORRECTO` |
| `gid://shopify/UrlRedirect/1518269661560` | `/collections/nuevos-cuadros-matchwalls` | `/` | `VERIFICADO Y CORRECTO` |
| `gid://shopify/UrlRedirect/1518269694328` | `/collections/nuevos-lienzos-matchwalls` | `/` | `VERIFICADO Y CORRECTO` |

Conteo `urlRedirectsCount(query:"target:/")` antes: 35.

## 4. Respaldo

Respaldo creado:

- `backup-pre-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-CLEANUP-011G5B1-2026-06-30.csv`.

## 5. Operacion ejecutada

Mutacion Admin GraphQL `urlRedirectDelete` validada contra schema.

Resultados:

| Operacion | deletedUrlRedirectId | userErrors |
|---|---|---|
| `deleteLienzos` | `gid://shopify/UrlRedirect/1518269596024` | `[]` |
| `deleteCuadrosRollos` | `gid://shopify/UrlRedirect/1518269628792` | `[]` |
| `deleteNuevosCuadros` | `gid://shopify/UrlRedirect/1518269661560` | `[]` |
| `deleteNuevosLienzos` | `gid://shopify/UrlRedirect/1518269694328` | `[]` |

## 6. Postcheck Admin

Consulta Admin GraphQL validada contra schema.

Resultado:

- `urlRedirect(id: gid://shopify/UrlRedirect/1518269596024)` devuelve `null`.
- `urlRedirect(id: gid://shopify/UrlRedirect/1518269628792)` devuelve `null`.
- `urlRedirect(id: gid://shopify/UrlRedirect/1518269661560)` devuelve `null`.
- `urlRedirect(id: gid://shopify/UrlRedirect/1518269694328)` devuelve `null`.
- Conteo `urlRedirectsCount(query:"target:/")` despues: 31.

## 7. QA publico

Las 4 fuentes devuelven 404 directo y ya no redirigen a home.

| URL | Resultado |
|---|---|
| `/collections/lienzos?mwqa=011g5b1` | `404`, sin location |
| `/collections/cuadros-rollos?mwqa=011g5b1` | `404`, sin location |
| `/collections/nuevos-cuadros-matchwalls?mwqa=011g5b1` | `404`, sin location |
| `/collections/nuevos-lienzos-matchwalls?mwqa=011g5b1` | `404`, sin location |

Sitemaps:

- 29 ficheros revisados.
- 7.274 URLs `loc`.
- 0 errores.
- 0 apariciones de las 4 URLs exactas.

## 8. Metodo de reversion

Si se necesitara revertir, crear de nuevo estas redirecciones:

- `/collections/lienzos -> /`, o nuevo target canonico aprobado.
- `/collections/cuadros-rollos -> /`, o nuevo target canonico aprobado.
- `/collections/nuevos-cuadros-matchwalls -> /`, o nuevo target canonico aprobado.
- `/collections/nuevos-lienzos-matchwalls -> /`, o nuevo target canonico aprobado.

No se recomienda revertir a home salvo decision expresa, porque el diagnostico 011G5B no demostro equivalencia semantica entre esas colecciones antiguas y la home.

## 9. Evidencias

- `backup-pre-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-CLEANUP-011G5B1-2026-06-30.csv`.
- `mutation-results-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-CLEANUP-011G5B1-2026-06-30.csv`.
- `qa-publico-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-CLEANUP-011G5B1-2026-06-30.csv`.

