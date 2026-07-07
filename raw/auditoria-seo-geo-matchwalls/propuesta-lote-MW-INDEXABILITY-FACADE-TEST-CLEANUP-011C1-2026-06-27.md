# Propuesta formal - MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1

Estado: `REQUIERE DECISION HUMANA`

Esta propuesta no ejecuta cambios. La ejecución queda bloqueada hasta recibir aprobación exacta:

`APROBADO LOTE MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1`

## 1. Nombre y alcance exacto

Lote: `MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1`

Objetivo: retirar del sitemap las URLs de prueba `facade-variants/test` sin tocar handles, redirecciones, temas, productos, colecciones ni contenido comercial.

Acción propuesta: cambiar el metaobject `facade_variants/test` de `ACTIVE` a `DRAFT`.

## 2. Recursos, IDs, URLs e idiomas afectados

Recurso Admin principal:

- Tipo: `Metaobject`
- ID: `gid://shopify/Metaobject/65268613347`
- Type: `facade_variants`
- Handle: `test`
- Display name: `Test`
- Estado actual: `ACTIVE`
- Online Store template suffix: `null`

Definición:

- ID: `gid://shopify/MetaobjectDefinition/1111458019`
- Nombre: `Facade variants`
- Type: `facade_variants`
- Metaobjects count: `1`
- Online Store enabled: `true`
- Publishable enabled: `true`

URLs actuales afectadas:

| Idioma | URL | Sitemap |
|---|---|---|
| ES | `https://www.matchwalls.com/pages/facade-variants/test` | `https://www.matchwalls.com/sitemap_metaobject_pages_1.xml` |
| EN | `https://www.matchwalls.com/en/pages/facade-variants/test` | `https://www.matchwalls.com/en/sitemap_metaobject_pages_1.xml` |
| FR | `https://www.matchwalls.com/fr/pages/facade-variants/test` | `https://www.matchwalls.com/fr/sitemap_metaobject_pages_1.xml` |
| DE | `https://www.matchwalls.com/de/pages/facade-variants/test` | `https://www.matchwalls.com/de/sitemap_metaobject_pages_1.xml` |
| NL | `https://www.matchwalls.com/nl/pages/facade-variants/test` | `https://www.matchwalls.com/nl/sitemap_metaobject_pages_1.xml` |
| IT | `https://www.matchwalls.com/it/pages/facade-variants/test` | `https://www.matchwalls.com/it/sitemap_metaobject_pages_1.xml` |
| PT | `https://www.matchwalls.com/pt/pages/facade-variants/test` | `https://www.matchwalls.com/pt/sitemap_metaobject_pages_1.xml` |

Idiomas prioritarios cubiertos: ES, EN, FR, DE, NL. IT y PT se incluyen porque el mismo metaobject genera sus URLs localizadas y aparecen en sitemap.

## 3. Valores actuales

`INCORRECTO`

- El metaobject `facade_variants/test` está `ACTIVE`.
- Las 7 URLs están presentes en sitemaps `sitemap_metaobject_pages_1.xml`.
- Las 7 URLs responden 301 a la home localizada:
  - ES -> `/`
  - EN -> `/en/`
  - FR -> `/fr/`
  - DE -> `/de/`
  - NL -> `/nl/`
  - IT -> `/it/`
  - PT -> `/pt/`
- Existe una redirección Admin:
  - `gid://shopify/UrlRedirect/412625207523`
  - path: `/pages/facade-variants/test`
  - target: `/`

## 4. Valores propuestos

`CORREGIDO Y VERIFICADO` solo si el QA posterior confirma salida del sitemap.

Cambio propuesto:

- `capabilities.publishable.status`: de `ACTIVE` a `DRAFT`.

Sin cambios en:

- handle `test`
- type `facade_variants`
- campo `opts`
- definición del metaobject
- redirección existente
- temas
- páginas normales
- productos referenciados
- colecciones
- canonicals
- hreflang

## 5. Evidencia y motivo técnico

`INCORRECTO`

Una URL listada en sitemap no debe redirigir. En este caso, además, el recurso es una página de prueba:

- sitemap: incluye 7 variantes localizadas;
- público: 301 a home localizada;
- Admin: metaobject de prueba `Test`, tipo `facade_variants`, estado `ACTIVE`;
- fuente del sitemap: `sitemap_metaobject_pages_1.xml`.

La causa verificada es que la definición `facade_variants` tiene Online Store y publicación activadas, y el único metaobject `test` está activo.

## 6. Riesgos y efectos secundarios

Riesgo: `VERIFICADO PERO MEJORABLE`

- Si algún código interno usa este metaobject `test` como fixture de desarrollo, dejará de ser público en Online Store.
- Los productos referenciados en `opts` no se modifican.
- La redirección existente seguirá funcionando; este lote no la elimina.
- Shopify puede tardar en regenerar sitemaps; si hay caché, la verificación puede requerir retest.

No se espera impacto comercial porque:

- es un recurso llamado `Test`;
- está en URL de prueba;
- actualmente no muestra contenido útil, sino que redirige a home.

## 7. Respaldo disponible

`VERIFICADO Y CORRECTO`

Valores actuales registrados:

- `id`: `gid://shopify/Metaobject/65268613347`
- `type`: `facade_variants`
- `handle`: `test`
- `displayName`: `Test`
- `publishable.status`: `ACTIVE`
- `onlineStore.templateSuffix`: `null`
- `fields.opts`: `["gid://shopify/Product/8277681733859","gid://shopify/Product/8277681832163","gid://shopify/Product/8308962623715"]`

Evidencia:

- `diagnostico-admin-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`
- `diagnostico-publico-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`
- `diagnostico-sitemap-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`

## 8. Método exacto de reversión

Si el cambio causa una regresión, revertir con el mismo metaobject:

- `capabilities.publishable.status`: de `DRAFT` a `ACTIVE`.

No requiere recrear contenido ni tocar URLs.

## 9. Pruebas posteriores

Después de ejecutar, verificar:

1. Admin GraphQL:
   - metaobject `gid://shopify/Metaobject/65268613347`;
   - `publishable.status = DRAFT`.
2. Sitemaps:
   - las 7 URLs ya no aparecen en sus sitemaps localizados.
3. Público:
   - comprobar las 7 URLs sin seguir redirección.
   - estado esperado aceptable: 301 existente a home localizada, porque el lote no toca redirecciones.
4. Control:
   - home ES/EN/FR/DE/NL cargan correctamente.
   - no se modifica el total de productos/colecciones/páginas normales.
5. Registro:
   - actualizar `registro-cambios-ejecutados.md` con valores antes/después y evidencia.

## Mutación validada pero no ejecutada

La mutación `metaobjectUpdate` fue validada contra schema Admin GraphQL.

Variables propuestas para ejecución:

```json
{
  "id": "gid://shopify/Metaobject/65268613347",
  "metaobject": {
    "capabilities": {
      "publishable": {
        "status": "DRAFT"
      }
    }
  }
}
```

## Decisión requerida

Para ejecutar, Daniel debe responder exactamente:

`APROBADO LOTE MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1`

