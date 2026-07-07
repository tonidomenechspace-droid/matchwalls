# Propuesta de lote MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1

Estado: `REQUIERE DECISION HUMANA`  
Tipo: ejecución Shopify reversible  
No ejecutado.

## Objetivo

Aplicar un piloto de noindex a 6 colecciones geográficas no estratégicas, sin tocar handles, redirecciones, productos, precios, inventario, navegación, tema ni contenido visible.

## Recurso y alcance exacto

Colecciones propuestas:

| Handle | ID Shopify | Estado actual | Valor propuesto |
|---|---:|---|---|
| `comprar-papel-pintado-alava` | `gid://shopify/Collection/443626914019` | `seo.hidden = null` | `seo.hidden = 1` |
| `comprar-papel-pintado-albacete` | `gid://shopify/Collection/646109593976` | `seo.hidden = null` | `seo.hidden = 1` |
| `comprar-papel-pintado-alicante` | `gid://shopify/Collection/646109626744` | `seo.hidden = null` | `seo.hidden = 1` |
| `comprar-papel-pintado-almeria` | `gid://shopify/Collection/646109659512` | `seo.hidden = null` | `seo.hidden = 1` |
| `comprar-papel-pintado-badajoz` | `gid://shopify/Collection/646109757816` | `seo.hidden = null` | `seo.hidden = 1` |
| `comprar-papel-pintado-burgos` | `gid://shopify/Collection/646109856120` | `seo.hidden = null` | `seo.hidden = 1` |

## Evidencia y motivo técnico

- Las colecciones geográficas ocupan 346 URLs actuales en sitemap.
- Las 6 propuestas son parte del patrón geográfico masivo.
- Admin verifica en muestra:
  - 73 productos exactos por colección;
  - primeros 8 productos idénticos;
  - 9 publicaciones;
  - `seo.hidden = null`;
  - misma fecha de actualización `2026-06-15T12:49:07Z`.
- La muestra pública confirma que las páginas geográficas están indexables, con canonical self y sin noindex.
- Se excluyen del piloto Madrid, Barcelona, París, Toulouse y otros destinos estratégicos.

## Riesgos

`REQUIERE DECISION HUMANA`

- Podría perderse tráfico orgánico de long-tail local si alguna URL está posicionada.
- No hay acceso verificado a Search Console, GA4 ni datos de conversión por URL en este diagnóstico.
- Shopify debería retirar del sitemap las variantes localizadas del recurso, pero debe verificarse idioma por idioma tras el cambio.

## Respaldo disponible

- Valores actuales documentados en:
  - `admin-muestra-MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E-2026-06-27.csv`.
  - `qa-publico-muestra-MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E-2026-06-27.csv`.
  - `qa-sitemap-geo-MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E-2026-06-27.csv`.

## Método exacto de reversión

Si el piloto falla o se decide revertir:

1. Eliminar el metafield `seo.hidden` creado en cada colección afectada.
2. Verificar en Admin que `seo.hidden` vuelve a `null`.
3. Verificar públicamente que las URLs vuelven a no tener robots `noindex`.
4. Verificar sitemap tras regeneración/caché de Shopify.

## Pruebas posteriores obligatorias

1. Admin:
   - verificar `seo.hidden=1` en las 6 colecciones.
2. Público:
   - verificar 200 accesible;
   - verificar robots `noindex,nofollow`;
   - verificar que no se modifica contenido visible.
3. Sitemap:
   - comprobar ausencia de las URLs base y localizadas afectadas.
4. Idiomas:
   - mínimo ES, EN, FR, DE y NL para cada colección cuando exista URL localizada.
5. Registro:
   - actualizar `registro-cambios-ejecutados.md` con valores previos, operación, evidencia, QA y reversión.

## Aprobación requerida

Ejecutar solo si Daniel responde exactamente:

`APROBADO LOTE MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1`

