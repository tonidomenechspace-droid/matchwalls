# Propuesta formal - MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B

Fecha/hora: 2026-06-27 01:07:24 +02:00  
Estado: `REQUIERE DECISION HUMANA`

## 1. Nombre y alcance exacto del lote

Lote propuesto:

`MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B`

Tipo: escritura Shopify puntual y reversible.

Objetivo:

Aplicar `noindex` a la muestra anomala excluida del lote rolling `011B5`, sin cambiar el producto principal ni corregir todavia el `productType`.

Alcance exacto:

- 1 producto Shopify.
- 7 URLs localizadas de muestra.
- Campo a modificar: metafield de producto `seo.hidden`.

No incluye:

- Producto principal `abstract-curves-negro`.
- Cambio de `productType`.
- Handles.
- Canonicals.
- Redirecciones.
- Tema Shopify.
- Precios.
- Inventario.
- Variantes.
- Apps.
- Search Console, Bing, GA4, GTM o Merchant Center.

## 2. Recursos, IDs, URLs e idiomas afectados

Producto:

- Product GID: `gid://shopify/Product/8554043474147`
- Legacy ID: `8554043474147`
- Titulo Admin: `Muestra Abstract Curves Negro`
- Handle Admin: `muestra-abstract-curves-negro`
- URL Admin/ES: `https://www.matchwalls.com/products/muestra-abstract-curves-negro`

URLs localizadas afectadas:

- ES: `https://www.matchwalls.com/products/muestra-abstract-curves-negro`
- EN: `https://www.matchwalls.com/en/products/black-curves-abstract-sample-1`
- FR: `https://www.matchwalls.com/fr/products/courbes-noires-echantillon-abstrait`
- DE: `https://www.matchwalls.com/de/products/schwarze-kurven-abstrakte-probe`
- NL: `https://www.matchwalls.com/nl/products/black-curves-abstract-sample`
- IT: `https://www.matchwalls.com/it/products/curve-nere-campione-astratto`
- PT: `https://www.matchwalls.com/pt/products/curvas-pretas-amostra-abstrata`

Producto principal inferido, no afectado:

- ES: `https://www.matchwalls.com/products/abstract-curves-negro`

## 3. Valores actuales

Lectura Admin directa:

- `status=ACTIVE`
- `productType=Mural`
- `templateSuffix=muestra`
- `onlineStoreUrl` presente.
- `seo.title=null`
- `seo.description=null`
- `seo.hidden=null`

Lectura publica:

- 7/7 URLs de muestra responden HTTP 200.
- 7/7 URLs de muestra no tienen `noindex`.
- 7/7 URLs de muestra estan presentes en sitemap de producto.
- Producto principal inferido responde HTTP 200.
- Producto principal inferido no tiene `noindex`.
- Producto principal inferido esta presente en sitemap de producto.

## 4. Valores propuestos

Para el producto `gid://shopify/Product/8554043474147`:

- namespace: `seo`
- key: `hidden`
- value: `1`
- type: `number_integer`

## 5. Evidencia y motivo tecnico

Evidencia que lo clasifica como muestra aunque `productType` sea `Mural`:

- Titulo Admin empieza por `Muestra`.
- Handle ES empieza por `muestra-`.
- Plantilla Shopify: `muestra`.
- Las 7 URLs localizadas contienen terminos de muestra: `sample`, `echantillon`, `probe`, `campione`, `amostra`.
- Existe producto principal inferido `abstract-curves-negro`, verificado con HTTP 200.

Motivo tecnico:

- Cumple el criterio aprobado en `MW-INDEXABILITY-SAMPLES-POLICY-011B`: noindex por defecto para productos muestra confirmados.
- Actualmente genera una URL auxiliar indexable que puede competir con el producto principal.
- La correccion mantiene la muestra accesible por URL directa/flujos comerciales y la retira de indexacion/sitemap.

## 6. Riesgos y efectos secundarios

Estado: `REQUIERE DECISION HUMANA`

Riesgos aceptados si se aprueba:

- Shopify ocultara esta muestra de sitemaps y motores de busqueda.
- Shopify tambien puede ocultarla de la busqueda interna de la tienda.
- Google/Bing no desindexaran al instante; dependera de recrawl.
- No corrige la deuda de datos `productType=Mural`.
- No corrige la URL NL con termino ingles `sample`.

Riesgos mitigados:

- No se toca el producto principal.
- No se cambian handles ni redirecciones.
- No se cambia el `productType`.
- Se modifica un unico metafield reversible.
- El comportamiento fue validado en piloto `011B4` y rolling `011B5`.

## 7. Respaldo disponible

Valor original:

- `seo.hidden=null`

Evidencias:

- `diagnostico-admin-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`
- `diagnostico-publico-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`
- `diagnostico-sitemap-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`
- `diagnostico-sitemaps-products-checked-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`

## 8. Metodo exacto de reversion

Ejecutar `metafieldsDelete` para:

- ownerId: `gid://shopify/Product/8554043474147`
- namespace: `seo`
- key: `hidden`

Estado esperado tras rollback:

- `seo.hidden=null`

## 9. Pruebas posteriores

Tras aprobacion y escritura:

1. Leer Admin:
   - `seo.hidden.value=1`
   - `seo.hidden.type=number_integer`
2. Verificar 7 URLs localizadas:
   - HTTP 200.
   - meta robots `noindex,nofollow`.
   - canonical self.
   - H1 presente.
3. Verificar sitemap:
   - 7/7 URLs de muestra ausentes de product sitemaps.
   - producto principal `abstract-curves-negro` sigue presente.
4. Registrar resultado en `registro-cambios-ejecutados.md`.

## 10. Mutacion propuesta

Mutacion validada contra esquema Shopify:

`SetSeoHiddenSampleAnomaly`

Input:

```json
{
  "ownerId": "gid://shopify/Product/8554043474147",
  "namespace": "seo",
  "key": "hidden",
  "value": "1",
  "type": "number_integer"
}
```

## Estado de aprobacion

No ejecutar hasta que Daniel apruebe exactamente:

`APROBADO LOTE MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B`
