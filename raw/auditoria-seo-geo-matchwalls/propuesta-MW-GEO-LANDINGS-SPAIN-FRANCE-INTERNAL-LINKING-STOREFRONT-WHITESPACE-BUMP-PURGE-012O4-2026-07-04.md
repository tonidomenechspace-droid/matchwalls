# Propuesta formal de lote

Lote: `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-WHITESPACE-BUMP-PURGE-012O4`  
Fecha: 2026-07-04  
Estado: `REQUIERE DECISION HUMANA`

## Motivo

El lote `012O3` ejecuto un same-value puro. Shopify acepto las operaciones sin errores, pero no cambio `updatedAt` en paginas ni traducciones. La web publica sigue inestable y no muestra el bloque de enlazado interno en 10/10 URLs.

Conclusion tecnica:

- Same-value puro no genera una senal real de purge/sync suficiente.
- El siguiente paso seguro es un cambio tecnico invisible minimo que fuerce una actualizacion real sin cambiar el contenido visible.

## Alcance exacto propuesto

Recursos:

1. Pagina Espana
   - ID: `gid://shopify/Page/687276622200`
   - Handle: `papel-pintado-espana`
   - URL base: `https://www.matchwalls.com/pages/papel-pintado-espana`

2. Pagina Francia
   - ID: `gid://shopify/Page/687276654968`
   - Handle: `papel-pintado-francia`
   - URL base: `https://www.matchwalls.com/pages/papel-pintado-francia`

Idiomas:

- ES base Shopify.
- EN, FR, DE, NL via `translationsRegister`.

## Cambio propuesto

Aplicar un cambio minimo de whitespace HTML, sin alterar texto visible, enlaces, headings ni estructura semantica.

Sistema propuesto:

- En el `body` ES de cada pagina, insertar una linea en blanco entre el bloque `Papel pintado por pais` y el bloque `Preguntas frecuentes`.
- Releer el nuevo digest `body_html`.
- Re-registrar traducciones EN/FR/DE/NL con los mismos textos visibles y el nuevo digest.

Esto debe cambiar el valor almacenado lo suficiente para que Shopify actualice `updatedAt` y emita una senal real de cache/sync, sin cambiar lo que ve el usuario.

## Valores actuales

### Espana

Bloque actual:

```html
<h2>Papel pintado por país</h2><p>Estás consultando las soluciones para España. Si tu proyecto se desarrolla en Francia o quieres comparar opciones para otro mercado, consulta la guía de <a href="/pages/papel-pintado-francia">papel pintado en Francia</a>.</p>

<h2>Preguntas frecuentes</h2>
```

Valor propuesto:

```html
<h2>Papel pintado por país</h2><p>Estás consultando las soluciones para España. Si tu proyecto se desarrolla en Francia o quieres comparar opciones para otro mercado, consulta la guía de <a href="/pages/papel-pintado-francia">papel pintado en Francia</a>.</p>


<h2>Preguntas frecuentes</h2>
```

### Francia

Bloque actual:

```html
<h2>Papel pintado por país</h2><p>Estás consultando las soluciones para Francia. Si tu proyecto se desarrolla en España o quieres comparar opciones para otro mercado, consulta la guía de <a href="/pages/papel-pintado-espana">papel pintado en España</a>.</p>

<h2>Preguntas frecuentes</h2>
```

Valor propuesto:

```html
<h2>Papel pintado por país</h2><p>Estás consultando las soluciones para Francia. Si tu proyecto se desarrolla en España o quieres comparar opciones para otro mercado, consulta la guía de <a href="/pages/papel-pintado-espana">papel pintado en España</a>.</p>


<h2>Preguntas frecuentes</h2>
```

## Campos que NO se tocaran

- Handles.
- URLs.
- Titulos de pagina.
- SEO title.
- Meta description.
- Canonicals.
- Hreflang.
- Schema.
- FAQs visibles.
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

- `resultado-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SAME-VALUE-PURGE-012O3-2026-07-04.md`
- `qa-publico-recheck3-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SAME-VALUE-PURGE-012O3-2026-07-04.csv`

## Riesgos

- Riesgo bajo-medio: es una escritura real, aunque sin cambio visible.
- Puede resolver la cache/sync si el problema es falta de senal `updatedAt`.
- Puede no resolver si el bloqueo esta en una cache externa de LangShop/CDN que necesita intervencion manual.

## Respaldo disponible

- `backup-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SAME-VALUE-PURGE-012O3-2026-07-04.md`
- `backup-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O-2026-07-04.md`

## Metodo exacto de reversion

Si aparece regresion:

1. Retirar la linea en blanco extra.
2. Re-registrar traducciones con el digest vigente.
3. Verificar Admin.
4. Verificar 10 URLs publicas.

## Pruebas posteriores obligatorias

1. Admin:
   - `pageUpdate` sin `userErrors`.
   - `updatedAt` debe cambiar respecto a `012O3`.
   - Nuevo digest `body_html` leido.
   - `translationsRegister` sin `userErrors`.
   - Traducciones EN/FR/DE/NL `outdated:false`.

2. Publico:
   - 10 URLs ES/EN/FR/DE/NL estado 200.
   - 10/10 URLs muestran heading pais y link cruzado correcto.
   - Sin `noindex`.
   - Canonicals intactos.

## Aprobacion requerida

Para ejecutar:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-WHITESPACE-BUMP-PURGE-012O4`
