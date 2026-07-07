# Propuesta formal - MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5

Fecha/hora: 2026-06-27 00:48:13 +02:00  
Estado: `REQUIERE DECISION HUMANA`

## 1. Nombre y alcance exacto del lote

Lote propuesto:

`MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5`

Tipo: escritura Shopify controlada por bloques.

Objetivo:

Escalar el noindex de muestras despues del piloto exitoso `011B4`, aplicando `seo.hidden=1` a productos muestra limpios pendientes.

Alcance propuesto:

- 75 productos muestra limpios.
- 473 URLs localizadas asociadas.
- Ejecucion en 3 bloques de 25 productos.

No incluye:

- Los 10 productos ya corregidos en `011B4`.
- El producto anomalo `8554043474147`, con URL/handle/template de muestra pero `productType` de mural.
- Paginas informativas de muestras.
- Colecciones.
- Handles.
- Canonicals.
- Redirecciones.
- Tema Shopify.
- Precios.
- Inventario.
- Variantes.
- Apps.
- Search Console, Bing, GA4, GTM, Merchant Center.

## 2. Recursos, IDs, URLs e idiomas afectados

Exactos en:

- `candidatos-limpios-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- `bloque-01-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- `bloque-02-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- `bloque-03-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.

Resumen:

| Grupo | Productos | URLs localizadas |
|---|---:|---:|
| Ya corregidos en 011B4 | 10 | 61 |
| Propuestos para 011B5 | 75 | 473 |
| Excluidos por anomalia de productType | 1 | 7 |
| Total productos muestra mapeados | 86 | 541 |

Bloques propuestos:

| Bloque | Productos | URLs localizadas |
|---|---:|---:|
| `011B5-01` | 25 | 173 |
| `011B5-02` | 25 | 144 |
| `011B5-03` | 25 | 156 |

## 3. Valores actuales

Lectura Admin directa por IDs:

- 86/86 productos muestra leidos.
- 10/86 ya tienen `seo.hidden=1`; corresponden al piloto `011B4`.
- 76/86 siguen con `seo.hidden=null`.
- De esos 76:
  - 75 tienen `productType=Muestra`, `templateSuffix=muestra`, `status=ACTIVE`, publicados en Online Store.
  - 1 queda excluido por anomalia de `productType`.

Valores actuales de los 75 propuestos:

- `seo.hidden = null`.
- `status = ACTIVE`.
- `productType = Muestra`.
- `templateSuffix = muestra`.
- `onlineStoreUrl` presente.

## 4. Valores propuestos

Para cada uno de los 75 productos:

- namespace: `seo`
- key: `hidden`
- value: `1`
- type: `number_integer`

## 5. Evidencia y motivo tecnico

Evidencia:

- `011B`: criterio aprobado por Daniel.
- `011B2`: 541 URLs de muestras corresponden a 86 productos muestra unicos.
- `011B4`: piloto de 10 productos ejecutado.
- `011B4-POSTCHECK`: piloto estable en Admin, storefront ES, storefront localizado y sitemap.

Motivo tecnico:

- Reducir canibalizacion y ruido indexable de productos muestra.
- Evitar que buscadores y sistemas IA recomienden muestras como producto principal.
- Mantener las muestras accesibles por URL directa y desde flujos comerciales.
- Retirar del sitemap Shopify los productos muestra auxiliares.

## 6. Riesgos y efectos secundarios

`REQUIERE DECISION HUMANA`

Riesgos aceptados si se ejecuta:

- Shopify oculta estos productos de sitemap y buscadores.
- Shopify tambien los oculta de la busqueda interna de la tienda.
- Google/Bing no desindexan al instante; necesitan recrawl.
- `0 userErrors` solo confirmara aceptacion de Shopify, no desindexacion real.
- Algunos idiomas tienen anomalías linguisticas en URLs; el noindex no corrige esas URLs, solo las retira de indexacion.

Riesgos mitigados:

- El piloto `011B4` funciono correctamente.
- No se cambian handles.
- No se redirige.
- No se toca el producto principal.
- Se ejecuta por bloques de 25.
- Se verifica cada bloque antes de continuar.
- Rollback exacto disponible.

## 7. Respaldo disponible

Valores originales para los 75 propuestos:

- `seo.hidden = null`.

Respaldo/matriz:

- `matriz-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- `candidatos-limpios-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.

## 8. Metodo exacto de reversion

Para cada producto afectado:

- Ejecutar `metafieldsDelete`.
- ownerId: Product GID afectado.
- namespace: `seo`.
- key: `hidden`.

Estado esperado tras rollback:

- `seo.hidden = null`.

Rollback ya validado contra esquema en 011B4:

- `RollbackSeoHiddenForSamplePilot`.

## 9. Pruebas posteriores

Por cada bloque:

1. Leer Admin:
   - `seo.hidden.value = 1`.
   - `seo.hidden.type = number_integer`.
2. Verificar storefront:
   - muestra representativa ES de cada producto.
   - status 200.
   - `noindex,nofollow`.
   - canonical self.
   - H1 presente.
3. Verificar URLs localizadas asociadas del bloque:
   - status 200.
   - `noindex,nofollow`.
   - canonical self.
4. Verificar sitemap:
   - URLs del bloque ausentes de product sitemaps.
5. Detener ante cualquier fallo critico.
6. Registrar resultado en `registro-cambios-ejecutados.md`.

## 10. Exclusion deliberada

Producto excluido:

- `gid://shopify/Product/8554043474147`
- Titulo ES: `Muestra Abstract Curves Negro`
- URL ES: `https://www.matchwalls.com/products/muestra-abstract-curves-negro`
- Motivo: URL/handle/template indican muestra, pero `productType` Admin aparece como `Mural` y en idiomas como `Murale`, `Muurschildering`, `Wandgemalde`.

Recomendacion:

Tratarlo en lote separado:

`MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B`

## Mutacion propuesta

Mutacion validada contra esquema Shopify:

`SetSeoHiddenRollingSamples`

Input por producto:

```json
{
  "ownerId": "gid://shopify/Product/...",
  "namespace": "seo",
  "key": "hidden",
  "value": "1",
  "type": "number_integer"
}
```

## Estado de aprobacion

No ejecutar hasta que Daniel apruebe exactamente:

`APROBADO LOTE MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5`

