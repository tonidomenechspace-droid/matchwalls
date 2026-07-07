# Propuesta formal de lote

Lote: `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SAME-VALUE-PURGE-012O3`  
Fecha: 2026-07-04  
Estado: `REQUIERE DECISION HUMANA`

## Motivo

El lote `012O` esta correcto en Shopify Admin, pero no aparece de forma estable en la web publica.

Diagnostico `012O2`:

- Admin contiene el bloque nuevo en Espana y Francia.
- Admin contiene traducciones EN/FR/DE/NL con el bloque.
- Traducciones `body_html`: `outdated:false`.
- QA publico robusto: 0/10 URLs muestran el bloque.
- La web publica sigue sirviendo el cuerpo anterior.

Inferencia tecnica: probable desfase de cache/render cache Shopify, sincronizacion LangShop o capa intermedia de traduccion/renderizado.

## Alcance exacto propuesto

Recursos afectados:

1. Pagina Espana
   - ID: `gid://shopify/Page/687276622200`
   - Handle: `papel-pintado-espana`
   - URL base: `https://www.matchwalls.com/pages/papel-pintado-espana`

2. Pagina Francia
   - ID: `gid://shopify/Page/687276654968`
   - Handle: `papel-pintado-francia`
   - URL base: `https://www.matchwalls.com/pages/papel-pintado-francia`

Idiomas afectados:

- ES base Shopify.
- EN, FR, DE y NL via traducciones `body_html`.

## Valores actuales verificados

### Espana

- Title: `Papel pintado en Espana para hogares y proyectos profesionales`
- Handle: `papel-pintado-espana`
- Publicada: si
- `updatedAt` post-012O: `2026-07-04T13:29:58Z`
- Admin contiene el bloque:

```html
<h2>Papel pintado por pais</h2><p>Estas consultando las soluciones para Espana. Si tu proyecto se desarrolla en Francia o quieres comparar opciones para otro mercado, consulta la guia de <a href="/pages/papel-pintado-francia">papel pintado en Francia</a>.</p>
```

### Francia

- Title: `Papel pintado en Francia para interiores y proyectos profesionales`
- Handle: `papel-pintado-francia`
- Publicada: si
- `updatedAt` post-012O: `2026-07-04T13:30:39Z`
- Admin contiene el bloque:

```html
<h2>Papel pintado por pais</h2><p>Estas consultando las soluciones para Francia. Si tu proyecto se desarrolla en Espana o quieres comparar opciones para otro mercado, consulta la guia de <a href="/pages/papel-pintado-espana">papel pintado en Espana</a>.</p>
```

## Valores propuestos

No se propone cambiar el contenido editorial.

Se propone:

1. Releer Admin antes de escribir.
2. Guardar de nuevo el mismo `body` ES vigente de cada pagina.
3. Re-registrar las traducciones `body_html` EN/FR/DE/NL con los mismos valores ya aprobados.
4. Forzar nueva senal `updatedAt`/purga/sync sin alterar copy, estructura ni SEO.

## Campos que NO se tocaran

- Handles.
- URLs.
- Titulos de pagina.
- SEO title.
- Meta description.
- Canonicals.
- Hreflang.
- Schema.
- FAQs.
- Menus.
- Home.
- Footer.
- Tema.
- Productos.
- Colecciones.
- Redirecciones.
- Precios.
- Inventario.

## Evidencia

- Resultado `012O`: `resultado-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O-2026-07-04.md`.
- Diagnostico `012O2`: `diagnostico-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SYNC-DIAG-012O2-2026-07-04.md`.
- QA publico robusto `012O2`: `qa-publico-robust-recheck-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SYNC-DIAG-012O2-2026-07-04.csv`.

## Riesgos

- Riesgo bajo-medio: aunque el contenido sea el mismo, la operacion es escritura tecnica en paginas y traducciones.
- Puede no resolver si el bloqueo esta en cache profunda de Shopify/CDN o cache interna de LangShop.
- Puede requerir posteriormente una revision manual en LangShop UI o soporte.

## Respaldo disponible

- Backup previo de `012O`: `backup-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O-2026-07-04.md`.
- Estado Admin actual leible antes de ejecutar.

## Metodo exacto de reversion

Si aparece una regresion:

1. Restaurar cuerpos ES desde el backup de `012O`.
2. Re-registrar traducciones `body_html` EN/FR/DE/NL con los valores previos.
3. Verificar Admin.
4. Verificar las 10 URLs publicas.

## Pruebas posteriores obligatorias

1. Shopify Admin:
   - `pageUpdate` sin `userErrors`.
   - `translationsRegister` sin `userErrors`.
   - Handles y titulos intactos.
   - Traducciones `outdated:false`.

2. Storefront publico:
   - Espana ES/EN/FR/DE/NL: bloque visible.
   - Francia ES/EN/FR/DE/NL: bloque visible.
   - Estado HTTP 200.
   - Sin `noindex`.
   - Canonical no alterado.

3. Cierre:
   - Si 10/10 pasa: marcar `012O` como `CORREGIDO Y VERIFICADO`.
   - Si falla: mantener `012O` como `INCOMPLETO` y pasar a revision LangShop/soporte.

## Aprobacion requerida

Para ejecutar este lote, Daniel debe responder exactamente:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SAME-VALUE-PURGE-012O3`
