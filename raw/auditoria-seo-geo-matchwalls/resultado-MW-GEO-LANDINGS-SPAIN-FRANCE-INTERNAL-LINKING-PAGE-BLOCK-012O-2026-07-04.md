# Resultado del lote `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O`

Fecha: 2026-07-04  
Estado final: `INCOMPLETO`

## Resumen ejecutivo

El lote fue aprobado y ejecutado sobre los recursos previstos. La escritura en Shopify Admin fue aceptada sin `userErrors`, los títulos/handles permanecen intactos y las traducciones EN/FR/DE/NL quedaron registradas con `outdated:false`.

Sin embargo, la verificación pública del storefront no es estable: tras varias comprobaciones, el bloque nuevo no aparece de forma consistente en las 10 URLs públicas. Por tanto, el lote no puede cerrarse como `CORREGIDO Y VERIFICADO`.

No se ha ejecutado rollback porque:

- Los valores almacenados en Shopify Admin son correctos.
- Los cambios son de bajo riesgo y están dentro del alcance aprobado.
- El fallo detectado está en propagación pública/caché/capa LangShop, no en los datos Admin.
- Revertir ahora eliminaría un estado Admin correcto sin resolver la causa de storefront.

## Recursos modificados

### España

- Recurso: `gid://shopify/Page/687276622200`
- Handle mantenido: `papel-pintado-espana`
- Título mantenido: `Papel pintado en España para hogares y proyectos profesionales`
- `updatedAt` después de escritura base ES: `2026-07-04T13:29:58Z`
- Nuevo digest `body_html`: `1171b8996598abe8d2e3f5790fff27c2664bca44f34595a7517ad5d397dfe6e9`

Bloque añadido en ES:

```html
<h2>Papel pintado por país</h2><p>Estás consultando las soluciones para España. Si tu proyecto se desarrolla en Francia o quieres comparar opciones para otro mercado, consulta la guía de <a href="/pages/papel-pintado-francia">papel pintado en Francia</a>.</p>
```

Traducciones actualizadas:

| Idioma | Key | Estado Admin |
|---|---|---|
| EN | `body_html` | `outdated:false`, `updatedAt: 2026-07-04T13:31:56Z` |
| FR | `body_html` | `outdated:false`, `updatedAt: 2026-07-04T13:31:56Z` |
| DE | `body_html` | `outdated:false`, `updatedAt: 2026-07-04T13:31:56Z` |
| NL | `body_html` | `outdated:false`, `updatedAt: 2026-07-04T13:31:56Z` |

### Francia

- Recurso: `gid://shopify/Page/687276654968`
- Handle mantenido: `papel-pintado-francia`
- Título mantenido: `Papel pintado en Francia para interiores y proyectos profesionales`
- `updatedAt` después de escritura base ES: `2026-07-04T13:30:39Z`
- Nuevo digest `body_html`: `c610e2d374bd399794d96a4e9b43defb0d911a6e1db724e434ce5fbf43ca2b48`

Bloque añadido en ES:

```html
<h2>Papel pintado por país</h2><p>Estás consultando las soluciones para Francia. Si tu proyecto se desarrolla en España o quieres comparar opciones para otro mercado, consulta la guía de <a href="/pages/papel-pintado-espana">papel pintado en España</a>.</p>
```

Traducciones actualizadas:

| Idioma | Key | Estado Admin |
|---|---|---|
| EN | `body_html` | `outdated:false`, `updatedAt: 2026-07-04T13:32:55Z` |
| FR | `body_html` | `outdated:false`, `updatedAt: 2026-07-04T13:32:55Z` |
| DE | `body_html` | `outdated:false`, `updatedAt: 2026-07-04T13:32:55Z` |
| NL | `body_html` | `outdated:false`, `updatedAt: 2026-07-04T13:32:55Z` |

## Campos no modificados

No se modificaron:

- Handles.
- URLs.
- Títulos de página.
- SEO title.
- Meta description.
- Canonicals.
- Hreflang.
- Schema/JSON-LD.
- FAQ existente.
- Menús.
- Home.
- Footer.
- Tema Shopify.
- Productos.
- Colecciones.
- Redirecciones.

## Verificación Admin

Resultado Admin: `VERIFICADO Y CORRECTO`

- `pageUpdate`: 2 operaciones, `userErrors: []`.
- `translationsRegister`: 2 operaciones, `userErrors: []`.
- España y Francia mantienen ID, title, handle y publicación.
- Traducciones `body_html` EN/FR/DE/NL quedan `outdated:false`.

## Verificación pública

Resultado público: `INCOMPLETO`

Archivos QA:

- `qa-publico-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O-2026-07-04.csv`
- `qa-publico-cachebuster-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O-2026-07-04.csv`
- `qa-publico-recheck2-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O-2026-07-04.csv`
- `qa-publico-recheck3-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O-2026-07-04.csv`

Última comprobación pública registrada:

| Página | Idioma | Resultado |
|---|---|---|
| España | ES | `FAIL` |
| España | EN | `FAIL` |
| España | FR | `FAIL` |
| España | DE | `FAIL` |
| España | NL | `PASS` |
| Francia | ES | `FAIL` |
| Francia | EN | `FAIL` |
| Francia | FR | `FAIL` |
| Francia | DE | `PASS` |
| Francia | NL | `FAIL` |

Observación: los resultados públicos son inconsistentes entre reintentos y user-agents. Las respuestas devuelven `200`, sin `noindex`, y Cloudflare aparece como `DYNAMIC`; aun así, la capa pública no refleja de forma uniforme los cuerpos Admin actualizados.

## Diagnóstico

Hechos verificados:

- Shopify Admin almacena los cuerpos actualizados.
- Shopify Admin almacena traducciones actualizadas con `outdated:false`.
- No se cambiaron handles ni títulos.
- La web pública todavía no refleja el bloque de forma estable.

Inferencia razonable, no demostrada al 100%:

- El bloqueo parece estar en caché/propagación de storefront y/o en la capa de LangShop que sirve las traducciones públicas.

## Siguiente lote seguro propuesto

`MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SYNC-DIAG-012O2`

Alcance recomendado:

1. Releer Admin sin escribir.
2. Comprobar LangShop UI para estas dos páginas y 4 idiomas.
3. Verificar si LangShop ve los nuevos `body_html`.
4. Si LangShop no los ve, preparar lote separado de actualización/sincronización LangShop.
5. Si LangShop sí los ve, preparar lote de no-op save/cache purge específico.
6. No hacer rollback salvo evidencia de contenido incorrecto público o decisión humana.

Estado del lote 012O:

`INCOMPLETO`
