# Propuesta formal - MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4

Fecha/hora: 2026-06-27  
Estado: `REQUIERE DECISION HUMANA`

## 1. Nombre y alcance exacto del lote

Lote propuesto:

`MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4`

Tipo: escritura Shopify acotada.

Objetivo:

Aplicar `seo.hidden=1` a 10 productos muestra piloto para validar de forma reversible la politica aprobada en `011B`.

No incluye:

- Noindex masivo de los 86 productos muestra.
- Cambios en handles.
- Cambios en canonicals.
- Cambios en redirecciones.
- Cambios en paginas informativas de muestras.
- Cambios en colecciones.
- Cambios de tema.
- Cambios de inventario, precio, variantes o textos comerciales.
- Cambios en Search Console, Bing, Merchant Center, GA4, GTM o apps.

## 2. Recursos, IDs, URLs e idiomas afectados

Se afectaran 10 productos Shopify. Al ser productos localizados, el impacto puede extenderse a sus URLs traducidas asociadas.

| # | Product GID | Producto ES | URL ES |
|---:|---|---|---|
| 1 | `gid://shopify/Product/14835721306488` | Muestra de Cuadricula Clasica Gris | `https://www.matchwalls.com/products/muestra-de-cuadricula-clasica-gris` |
| 2 | `gid://shopify/Product/14835721175416` | Muestra de Cuadricula Clasica Verde | `https://www.matchwalls.com/products/muestra-de-cuadricula-clasica-verde` |
| 3 | `gid://shopify/Product/14835721372024` | Muestra de Cuadricula Clasica Blanco y negro | `https://www.matchwalls.com/products/muestra-de-cuadricula-clasica-blanco-y-negro` |
| 4 | `gid://shopify/Product/14835719176568` | Muestra de Damas Clasicas Gris | `https://www.matchwalls.com/products/muestra-de-damas-clasicas-gris` |
| 5 | `gid://shopify/Product/14835719307640` | Muestra de Damas Clasicas Verde | `https://www.matchwalls.com/products/muestra-de-damas-clasicas-verde` |
| 6 | `gid://shopify/Product/14858207789432` | Muestra de Forest Study Retreat | `https://www.matchwalls.com/products/muestra-de-forest-study-retreat` |
| 7 | `gid://shopify/Product/14835717210488` | Muestra de Golden Woodland Amarillo | `https://www.matchwalls.com/products/muestra-de-golden-woodland-amarillo` |
| 8 | `gid://shopify/Product/14835717341560` | Muestra de Golden Woodland Lila | `https://www.matchwalls.com/products/muestra-de-golden-woodland-lila` |
| 9 | `gid://shopify/Product/14835717079416` | Muestra de Golden Woodland Marron | `https://www.matchwalls.com/products/muestra-de-golden-woodland-marron` |
| 10 | `gid://shopify/Product/14858732339576` | Muestra de Highland Plaid Marron | `https://www.matchwalls.com/products/muestra-de-highland-plaid-marron` |

## 3. Valores actuales

Lectura Admin `011B3`:

- `status = ACTIVE` en 10/10.
- `templateSuffix = muestra` en 10/10.
- `productType = Muestra` en 10/10.
- `publishedAt`: presente en 10/10.
- `onlineStoreUrl`: presente en 10/10.
- `seo.title = null` en 10/10.
- `seo.description = null` en 10/10.
- `seo.hidden = null` en 10/10.

Evidencia:

- `admin-seohidden-lectura-piloto-MW-INDEXABILITY-SAMPLES-ADMIN-SEOHIDDEN-DIAG-011B3-2026-06-27.csv`.

## 4. Valores propuestos

Crear en cada uno de los 10 productos:

- namespace: `seo`
- key: `hidden`
- value: `1`
- type: `number_integer`

## 5. Evidencia y motivo tecnico

Evidencia previa:

- `011B`: criterio aprobado por Daniel: noindex por defecto para productos muestra confirmados; paginas informativas indexables; excepciones solo con evidencia.
- `011B2`: 541 URLs de productos muestra corresponden a 86 productos muestra unicos.
- `011B3`: estos 10 productos tienen `seo.hidden = null`.

Motivo:

Validar en un piloto pequeno si el metodo oficial de Shopify retira productos muestra de sitemap/buscadores sin romper el acceso directo ni la operativa de compra/pedido.

## 6. Riesgos y efectos secundarios

`REQUIERE DECISION HUMANA`

Riesgos aceptados al ejecutar:

- Shopify puede retirar estos productos de sitemap.
- Shopify puede anadir `noindex,nofollow` a las URLs.
- Shopify documenta que estos productos tambien se ocultaran de la busqueda interna de la tienda.
- El efecto en sitemap no tiene por que ser instantaneo.
- Google/Bing pueden tardar en recrawlear y desindexar.
- `0 userErrors` solo demostrara que Shopify acepto la mutacion, no que Google haya desindexado ni que la experiencia comercial sea correcta.

Riesgos mitigados:

- Lote pequeno: 10 productos.
- Todos son productos muestra confirmados.
- No se cambian handles ni URLs.
- No se redirige.
- No se toca producto principal.
- Rollback exacto disponible.

## 7. Respaldo disponible

Valores originales:

- `seo.hidden = null` en 10/10.

Archivo respaldo:

- `admin-seohidden-lectura-piloto-MW-INDEXABILITY-SAMPLES-ADMIN-SEOHIDDEN-DIAG-011B3-2026-06-27.csv`.

## 8. Metodo exacto de reversion

Si falla cualquier prueba critica:

Ejecutar `metafieldsDelete` para:

- ownerId: cada uno de los 10 Product GID.
- namespace: `seo`.
- key: `hidden`.

Esto devuelve el estado original `seo.hidden = null`.

Rollback validado contra esquema GraphQL:

- `RollbackSeoHiddenForSamplePilot`.

## 9. Pruebas posteriores

Despues de ejecutar:

1. Leer Admin otra vez:
   - `seo.hidden.value = 1`.
   - `seo.hidden.type = number_integer`.
2. Verificar HTML publico de las 10 URLs ES:
   - status 200.
   - URL directa accesible.
   - `meta robots` contiene `noindex` y/o `nofollow` segun salida Shopify.
   - H1 sigue presente.
   - CTA/compra de muestra no se rompe.
3. Verificar en URLs localizadas asociadas si hay impacto.
4. Revisar sitemap:
   - comprobar si siguen o no presentes inmediatamente.
   - si siguen presentes, registrar como pendiente de refresco de Shopify; no forzar acciones adicionales.
5. Registrar resultado en `registro-cambios-ejecutados.md`.

## Mutacion propuesta

Mutacion validada contra esquema Shopify:

`SetSeoHiddenForSamplePilot`

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

Daniel envio antes:

`APROBADO LOTE MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4`

Pero esa aprobacion llego antes de presentar esta propuesta formal y antes de documentar los valores actuales `011B3`.

Para cumplir el protocolo del proyecto, la ejecucion queda pendiente de una nueva aprobacion exacta posterior a esta propuesta:

`APROBADO LOTE MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4`

