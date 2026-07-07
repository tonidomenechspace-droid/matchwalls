# Diagnostico MW-INDEXABILITY-REDIRECTS-HOME-TARGET-DIAG-011G5

Fecha: 2026-06-30  
Tipo: diagnostico de solo lectura  
Estado final: VERIFICADO PERO MEJORABLE  
Shopify modificado: no

## Documentos leidos

- `cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`
- `registro-cambios-ejecutados.md`
- `diagnostico-MW-INDEXABILITY-REDIRECTS-FR-DEAD-TARGET-DECISION-011G4B-2026-06-30.md`
- `diagnostico-MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G-2026-06-29.md`
- Evidencias historicas de `facade-variants/test` y redirecciones 011F/011G

## Estado real comprobado

- Consulta Admin validada contra schema Shopify: `urlRedirects(query: "target:/")`.
- Resultado actual Shopify: 36 redirects con `target=/`.
- Sitemaps actuales revisados: 29 sitemap files; 0/36 fuentes aparecen en sitemap actual.
- Locale `no` verificado en `shopLocales`: publicado `false`.
- Public QA: 36/36 fuentes terminan en `301 -> 200` hacia `https://www.matchwalls.com/`.

## Cobertura

Cobertura del lote: 36/36 redirects con `target=/`.

| Grupo | Cantidad | Estado | Lectura |
|---|---:|---|---|
| URL de prueba `facade-variants/test` | 1 | INCORRECTO | No tiene valor SEO ni sustituto semantico; redirect a home no es equivalente |
| Colecciones ES antiguas de lienzos/cuadros | 4 | REQUIERE DECISION HUMANA | Puede haber valor comercial historico, pero no se ha demostrado URL equivalente actual |
| URLs legacy `/no/` productos | 21 | STANDBY | Noruego no publicado y fuera de idiomas prioritarios |
| URLs legacy `/no/` paginas | 5 | STANDBY | Noruego no publicado y fuera de idiomas prioritarios |
| URLs legacy `/no/` colecciones | 5 | STANDBY | Noruego no publicado; se solapa con legacy artprints/matchwallsmurals |

## Interpretacion SEO/GEO

- Al no estar en sitemap, estas URLs no se estan promoviendo activamente.
- El redirect a home evita 404, pero transmite una señal semantica pobre: productos, colecciones o pruebas terminan en la home ES.
- Para buscadores e IA, repuntar masivamente a home puede diluir contexto y generar equivalencias falsas.
- No se debe limpiar en masa sin distinguir:
  - basura clara;
  - colecciones antiguas con posible valor comercial;
  - URLs de idioma no prioritario y no publicado.

## Recomendacion

Siguiente sublote recomendado, acotado y de bajo riesgo:

`MW-INDEXABILITY-REDIRECTS-HOME-TARGET-CLEANUP-011G5A`

Alcance recomendado:

- Solo `gid://shopify/UrlRedirect/412625207523`
- Path: `/pages/facade-variants/test`
- Target actual: `/`
- Propuesta: eliminar el redirect si Daniel aprueba que la URL de prueba no debe conservar ninguna equivalencia.

No incluir todavia:

- Las 4 colecciones ES de lienzos/cuadros: requieren decision comercial.
- Las 31 URLs `/no/`: quedan `STANDBY` por idioma no prioritario y locale no publicado.

## Proximos lotes posibles

| Lote | Tipo | Estado | Nota |
|---|---|---|---|
| `MW-INDEXABILITY-REDIRECTS-HOME-TARGET-CLEANUP-011G5A` | Escritura Shopify | REQUIERE DECISION HUMANA | Limpiar solo `/pages/facade-variants/test -> /` |
| `MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-DECISION-011G5B` | Decision/diagnostico | REQUIERE DECISION HUMANA | Decidir politica de lienzos/cuadros |
| `MW-INDEXABILITY-REDIRECTS-HOME-TARGET-NO-STANDBY-011G5C` | Decision/diagnostico | STANDBY | No tocar salvo autorizacion para idioma NO |

## Evidencias generadas

- `admin-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-DIAG-011G5-2026-06-30.csv`
- `qa-publico-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-DIAG-011G5-2026-06-30.csv`
- `clasificacion-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-DIAG-011G5-2026-06-30.csv`

## Confirmacion de seguridad

No se ha modificado Shopify. No se han eliminado redirects, no se han repuntado targets, no se han cambiado handles, sitemaps, canonicals, temas ni traducciones.

