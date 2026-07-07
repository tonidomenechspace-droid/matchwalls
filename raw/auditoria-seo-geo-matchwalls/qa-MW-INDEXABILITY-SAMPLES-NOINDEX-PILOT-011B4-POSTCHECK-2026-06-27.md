# QA postcheck - MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK

Fecha/hora: 2026-06-27 00:42:39 +02:00  
Estado: `CORREGIDO Y VERIFICADO`

## Alcance

Control posterior de solo lectura del piloto `MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4`.

No se modifico Shopify.

Se verifico:

- Admin `seo.hidden`.
- Storefront publico ES.
- Storefront publico localizado.
- Product sitemaps.

## Documentos y evidencias previas

- `qa-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-2026-06-27.md`.
- `admin-seohidden-post-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-2026-06-27.csv`.
- `candidatos-piloto-noindex-MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2-2026-06-27.csv`.

## Verificacion Admin

`VERIFICADO Y CORRECTO`

Consulta Admin GraphQL validada contra esquema:

- `ProductSeoHiddenPilotPostcheck`.
- Scope requerido: `read_products`.

Resultado:

- 10/10 productos existen.
- 10/10 siguen `ACTIVE`.
- 10/10 siguen con `productType = Muestra`.
- 10/10 siguen con `templateSuffix = muestra`.
- 10/10 siguen publicados en Online Store.
- 10/10 siguen con `seo.hidden.value = 1`.
- 10/10 siguen con `seo.hidden.type = number_integer`.

Evidencia:

- `admin-seohidden-postcheck-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK-2026-06-27.csv`.

## Verificacion publica ES

`VERIFICADO Y CORRECTO`

10 URLs ES revisadas:

- 10/10 status 200.
- 10/10 acceso directo operativo.
- 10/10 `noindex,nofollow`.
- 10/10 canonical self.
- 10/10 H1 presente.

Evidencia:

- `qa-publico-es-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK-2026-06-27.csv`.

## Verificacion publica localizada

`VERIFICADO Y CORRECTO`

61 URLs localizadas asociadas a los 10 IDs revisadas:

- 61/61 status 200.
- 61/61 `noindex,nofollow`.
- 61/61 canonical self.
- 61/61 H1 presente.

Durante la primera lectura una URL FR no devolvio robots en el CSV inicial, pero se revalido inmediatamente con lectura directa y cache-control. La respuesta correcta contiene:

- `<meta name="robots" content="noindex,nofollow">`.

El CSV final fue actualizado con la lectura verificada.

Evidencia:

- `qa-publico-localizado-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK-2026-06-27.csv`.

## Verificacion sitemap

`VERIFICADO Y CORRECTO`

- `https://www.matchwalls.com/sitemap.xml`: 200.
- Product sitemaps revisados: 7/7.
- Product sitemaps con status 200: 7/7.
- URLs localizadas del piloto revisadas: 61.
- URLs presentes en product sitemaps: 0/61.

Evidencia:

- `qa-sitemap-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK-2026-06-27.csv`.
- `qa-sitemap-products-checked-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK-2026-06-27.csv`.

## Rollback

`VERIFICADO Y CORRECTO`

Rollback disponible si se decide revertir:

- ejecutar `metafieldsDelete` sobre los 10 Product GID;
- namespace `seo`;
- key `hidden`;
- estado esperado tras rollback: `seo.hidden = null`.

No se ha ejecutado rollback.

## Limitaciones

- No se verifica desindexacion real en Google/Bing; eso requiere rastreo e informes externos posteriores.
- El resultado confirma estado tecnico Shopify/storefront/sitemap, no rankings ni citas de IA.

## Estado final

`CORREGIDO Y VERIFICADO`

El piloto sigue estable tras postcheck y es apto para preparar una propuesta de escalado controlado, no para escalar sin propuesta.

Siguiente recomendado:

`MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5`

