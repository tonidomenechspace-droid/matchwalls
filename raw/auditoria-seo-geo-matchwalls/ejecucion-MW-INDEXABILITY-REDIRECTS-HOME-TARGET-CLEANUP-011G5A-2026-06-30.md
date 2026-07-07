# Ejecucion MW-INDEXABILITY-REDIRECTS-HOME-TARGET-CLEANUP-011G5A

Fecha: 2026-06-30  
Tipo: escritura Shopify acotada  
Estado final: CORREGIDO Y VERIFICADO

## Autorizacion

Daniel aprobo exactamente:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-HOME-TARGET-CLEANUP-011G5A`

## Alcance aprobado

Eliminar exclusivamente el redirect:

| Campo | Valor |
|---|---|
| ID | `gid://shopify/UrlRedirect/412625207523` |
| Path | `/pages/facade-variants/test` |
| Target anterior | `/` |

No se tocaron otros redirects, productos, colecciones, paginas, handles, sitemaps, canonicals, temas ni traducciones.

## Precheck

| Comprobacion | Resultado |
|---|---|
| Redirect existe antes de ejecutar | VERIFICADO Y CORRECTO |
| Path actual | `/pages/facade-variants/test` |
| Target actual | `/` |
| Conteo `target:/` antes | 36 |

## Operacion ejecutada

Mutacion Shopify Admin:

`urlRedirectDelete(id: "gid://shopify/UrlRedirect/412625207523")`

Resultado:

| Campo | Resultado |
|---|---|
| `deletedUrlRedirectId` | `gid://shopify/UrlRedirect/412625207523` |
| `userErrors` | `[]` |

## Postcheck Admin

| Comprobacion | Resultado |
|---|---|
| `urlRedirect(id)` | `null` |
| Conteo `target:/` despues | 35 |

## QA publico

URL comprobada:

`https://www.matchwalls.com/pages/facade-variants/test?mwqa=011g5a`

Resultado:

| Intento | Estado |
|---:|---|
| 1 | 404 |
| 2 | 404 |
| 3 | 404 |

No hay redirect publico a home.

## Sitemap

- Sitemap index: 29 ficheros.
- Errores de lectura: 0.
- Apariciones de `https://www.matchwalls.com/pages/facade-variants/test`: 0.

## Reversion

Si se requiere rollback:

- Crear redirect con:
  - path: `/pages/facade-variants/test`
  - target: `/`

Esto restauraria el comportamiento anterior, aunque no se recomienda salvo necesidad externa demostrada.

## Evidencias

- `backup-pre-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-CLEANUP-011G5A-2026-06-30.csv`
- `qa-publico-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-CLEANUP-011G5A-2026-06-30.csv`

