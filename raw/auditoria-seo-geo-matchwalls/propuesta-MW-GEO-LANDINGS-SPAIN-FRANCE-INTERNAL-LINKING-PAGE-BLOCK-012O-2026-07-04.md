# Propuesta formal de lote

## Lote

`MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O`

## Estado

`REQUIERE DECISION HUMANA`

Esta propuesta no ejecuta cambios en Shopify ni en LangShop. Define el alcance exacto para aplicar el bloque de enlazado interno España ↔ Francia preparado en `012N`.

## Documentos leídos

- `resultado-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-QA-012M-2026-07-04.md`
- `qa-internal-linking-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-QA-012M-2026-07-04.csv`
- `copy-map-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-COPY-MAP-012N-2026-07-04.csv`
- `resultado-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-COPY-MAP-012N-2026-07-04.md`
- `registro-cambios-ejecutados.md`

## Estado real comprobado en Shopify

Consulta de solo lectura mediante Shopify Admin GraphQL validada antes de ejecutarse.

### Página España

- Recurso: `gid://shopify/Page/687276622200`
- URL base ES: `https://www.matchwalls.com/pages/papel-pintado-espana`
- Título actual: `Papel pintado en España para hogares y proyectos profesionales`
- Handle actual: `papel-pintado-espana`
- Publicada: sí
- `updatedAt`: `2026-07-04T00:07:41Z`
- `body_html` ES actual: no contiene `Papel pintado por país`
- Traducciones `body_html` EN/FR/DE/NL: existentes, `outdated:false`

### Página Francia

- Recurso: `gid://shopify/Page/687276654968`
- URL base ES: `https://www.matchwalls.com/pages/papel-pintado-francia`
- Título actual: `Papel pintado en Francia para interiores y proyectos profesionales`
- Handle actual: `papel-pintado-francia`
- Publicada: sí
- `updatedAt`: `2026-07-03T11:57:06Z`
- `body_html` ES actual: no contiene `Papel pintado por país`
- Traducciones `body_html` EN/FR/DE/NL: existentes, `outdated:false`

## Estado público comprobado

Las 10 URLs de España/Francia en ES, EN, FR, DE y NL responden `200`, no muestran `noindex` y todavía no contienen el bloque propuesto:

- `https://www.matchwalls.com/pages/papel-pintado-espana`
- `https://www.matchwalls.com/en/pages/spain-wallpaper`
- `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`
- `https://www.matchwalls.com/de/pages/spanien-tapete`
- `https://www.matchwalls.com/nl/pages/spanje-behang`
- `https://www.matchwalls.com/pages/papel-pintado-francia`
- `https://www.matchwalls.com/en/pages/french-wallpaper`
- `https://www.matchwalls.com/fr/pages/papier-peint-en-france`
- `https://www.matchwalls.com/de/pages/franzosische-tapete`
- `https://www.matchwalls.com/nl/pages/frans-behang`

## Motivo técnico

El QA `012M` detectó que las landings España/Francia están indexables, en sitemap y con hreflang correcto, pero carecen de enlazado editorial interno entre páginas país:

- Home → landings país: `INCOMPLETO`
- España ↔ Francia por idioma: `INCOMPLETO`

El objetivo de este lote es añadir un bloque contextual visible, pequeño y rastreable para reforzar descubrimiento, relación semántica país/mercado y comprensión por buscadores/IA, sin alterar arquitectura, URL, schema ni metas.

## Alcance exacto propuesto

Añadir un bloque HTML compuesto por:

- 1 `h2`
- 1 párrafo
- 1 enlace interno editorial hacia la landing equivalente del otro país, en el mismo idioma

Ubicación en todas las variantes:

- Insertar después del bloque de ciudades/zonas estratégicas.
- Insertar antes de preguntas frecuentes.

## Recursos e idiomas afectados

| País origen | Idioma | Sistema de escritura previsto | Recurso |
|---|---|---|---|
| España | ES | Shopify native page body | `gid://shopify/Page/687276622200` |
| España | EN | Shopify translations / LangShop-visible translation layer | `gid://shopify/Page/687276622200` |
| España | FR | Shopify translations / LangShop-visible translation layer | `gid://shopify/Page/687276622200` |
| España | DE | Shopify translations / LangShop-visible translation layer | `gid://shopify/Page/687276622200` |
| España | NL | Shopify translations / LangShop-visible translation layer | `gid://shopify/Page/687276622200` |
| Francia | ES | Shopify native page body | `gid://shopify/Page/687276654968` |
| Francia | EN | Shopify translations / LangShop-visible translation layer | `gid://shopify/Page/687276654968` |
| Francia | FR | Shopify translations / LangShop-visible translation layer | `gid://shopify/Page/687276654968` |
| Francia | DE | Shopify translations / LangShop-visible translation layer | `gid://shopify/Page/687276654968` |
| Francia | NL | Shopify translations / LangShop-visible translation layer | `gid://shopify/Page/687276654968` |

## Valores actuales relevantes

No existe actualmente ningún bloque equivalente en las 10 URLs con estos encabezados:

- `Papel pintado por país`
- `Wallpaper by country`
- `Papier peint par pays`
- `Tapeten nach Land`
- `Behang per land`

Punto de inserción actual confirmado:

| Página | Idioma | Después de | Antes de |
|---|---|---|---|
| España | ES | `Ciudades y zonas estratégicas` | `Preguntas frecuentes` |
| España | EN | `Strategic cities and areas` | `Frequently asked questions` |
| España | FR | `Villes et zones stratégiques` | `Questions fréquentes` |
| España | DE | `Strategische Städte und Regionen` | `Häufige Fragen` |
| España | NL | `Strategische steden en regio’s` | `Veelgestelde vragen` |
| Francia | ES | `Ciudades estratégicas en Francia` | `Preguntas frecuentes` |
| Francia | EN | `Strategic cities in France` | `Frequently asked questions` |
| Francia | FR | `Villes stratégiques en France` | `Questions fréquentes` |
| Francia | DE | `Strategische Städte in Frankreich` | `Häufige Fragen` |
| Francia | NL | `Strategische steden in Frankrijk` | `Veelgestelde vragen` |

## Valores propuestos

### España ES

```html
<h2>Papel pintado por país</h2><p>Estás consultando las soluciones para España. Si tu proyecto se desarrolla en Francia o quieres comparar opciones para otro mercado, consulta la guía de <a href="/pages/papel-pintado-francia">papel pintado en Francia</a>.</p>
```

### España EN

```html
<h2>Wallpaper by country</h2><p>You are viewing the solutions for Spain. If your project is in France or you want to compare options for another market, read the guide to <a href="/en/pages/french-wallpaper">wallpaper in France</a>.</p>
```

### España FR

```html
<h2>Papier peint par pays</h2><p>Vous consultez les solutions pour l’Espagne. Si votre projet se situe en France ou si vous souhaitez comparer les options pour un autre marché, consultez notre guide du <a href="/fr/pages/papier-peint-en-france">papier peint en France</a>.</p>
```

### España DE

```html
<h2>Tapeten nach Land</h2><p>Sie sehen die Lösungen für Spanien. Wenn Ihr Projekt in Frankreich liegt oder Sie Optionen für einen anderen Markt vergleichen möchten, lesen Sie den Leitfaden zu <a href="/de/pages/franzosische-tapete">Tapeten in Frankreich</a>.</p>
```

### España NL

```html
<h2>Behang per land</h2><p>U bekijkt de oplossingen voor Spanje. Als uw project zich in Frankrijk bevindt of als u opties voor een andere markt wilt vergelijken, bekijk dan de gids over <a href="/nl/pages/frans-behang">behang in Frankrijk</a>.</p>
```

### Francia ES

```html
<h2>Papel pintado por país</h2><p>Estás consultando las soluciones para Francia. Si tu proyecto se desarrolla en España o quieres comparar opciones para otro mercado, consulta la guía de <a href="/pages/papel-pintado-espana">papel pintado en España</a>.</p>
```

### Francia EN

```html
<h2>Wallpaper by country</h2><p>You are viewing the solutions for France. If your project is in Spain or you want to compare options for another market, read the guide to <a href="/en/pages/spain-wallpaper">wallpaper in Spain</a>.</p>
```

### Francia FR

```html
<h2>Papier peint par pays</h2><p>Vous consultez les solutions pour la France. Si votre projet se situe en Espagne ou si vous souhaitez comparer les options pour un autre marché, consultez notre guide du <a href="/fr/pages/papier-peint-en-espagne">papier peint en Espagne</a>.</p>
```

### Francia DE

```html
<h2>Tapeten nach Land</h2><p>Sie sehen die Lösungen für Frankreich. Wenn Ihr Projekt in Spanien liegt oder Sie Optionen für einen anderen Markt vergleichen möchten, lesen Sie den Leitfaden zu <a href="/de/pages/spanien-tapete">Tapeten in Spanien</a>.</p>
```

### Francia NL

```html
<h2>Behang per land</h2><p>U bekijkt de oplossingen voor Frankrijk. Als uw project zich in Spanje bevindt of als u opties voor een andere markt wilt vergelijken, bekijk dan de gids over <a href="/nl/pages/spanje-behang">behang in Spanje</a>.</p>
```

## Operaciones técnicas previstas si se aprueba

Las mutaciones han sido validadas contra Shopify Admin GraphQL, pero no ejecutadas.

1. Crear respaldo local completo de:
   - `body_html` ES de España y Francia.
   - Traducciones `body_html` EN/FR/DE/NL de España y Francia.
   - Títulos, handles, `updatedAt`, estado `outdated` y URLs públicas.
2. Actualizar solo el campo `body` de las dos páginas base ES mediante `pageUpdate`.
3. Releer ambas páginas y sus `translatableContent.digest` de `body_html`.
4. Si los handles, títulos, publicación y cuerpos base son correctos, registrar las traducciones `body_html` EN/FR/DE/NL mediante `translationsRegister`, usando el digest vigente.
5. Releer traducciones y verificar `outdated:false` cuando Shopify lo devuelva.
6. Verificar en público las 10 URLs.
7. Actualizar `registro-cambios-ejecutados.md`.

## Campos explícitamente fuera de alcance

No se tocará:

- Handles.
- URLs.
- Títulos de página.
- SEO title.
- Meta description.
- Canonicals.
- Hreflang.
- Schema/JSON-LD.
- FAQs existentes.
- Menús.
- Home.
- Footer.
- Colecciones.
- Productos.
- Tema Shopify.
- App embeds.
- Redirecciones.

## Riesgos

| Riesgo | Nivel | Control |
|---|---:|---|
| Que al actualizar el body ES cambie el digest y marque traducciones como desactualizadas | Medio | Relectura inmediata del digest antes de registrar traducciones |
| Que LangShop mantenga una capa visual/cache distinta de Shopify translations | Medio | Verificación pública EN/FR/DE/NL y revisión posterior en LangShop si hay discrepancia |
| Error de inserción por cambios simultáneos en el body | Medio | Releer justo antes de escribir; abortar si no coincide el punto de inserción |
| Duplicación del bloque si ya fue añadido manualmente | Bajo | Comprobación previa de encabezados y enlaces antes de escribir |
| Alteración accidental de title/handle/SEO | Bajo | Mutación limitada a `body` y traducciones `body_html`; no enviar campos de title, handle ni SEO |

## Método de reversión

Si cualquier prueba crítica falla:

1. Restaurar el `body_html` ES original de las dos páginas desde el respaldo local.
2. Restaurar las traducciones `body_html` EN/FR/DE/NL originales desde el respaldo local mediante `translationsRegister`.
3. Releer Admin.
4. Revalidar público en las 10 URLs.
5. Registrar reversión en `registro-cambios-ejecutados.md`.

## Pruebas posteriores obligatorias

### Admin / datos

- España ES mantiene ID, handle, title y publicación.
- Francia ES mantiene ID, handle, title y publicación.
- Traducciones EN/FR/DE/NL mantienen handle traducido.
- No se modifica SEO meta.
- No se modifica schema.

### Público

En las 10 URLs:

- HTTP `200`.
- Sin `noindex`.
- Canonical presente.
- Hreflang no degradado.
- Bloque visible en el idioma correcto.
- Enlace destino visible y rastreable.
- Enlace destino responde `200`.
- No aparecen textos cruzados entre idiomas.
- No se duplica FAQ ni CTA final.

### QA semántico

- España enlaza a Francia en el mismo idioma.
- Francia enlaza a España en el mismo idioma.
- Anchor claro, descriptivo y no sobreoptimizado.
- Texto útil para usuario y rastreable por buscadores/IA.

## Decisión requerida

Para ejecutar este lote, Daniel debe aprobar exactamente:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O`

Hasta recibir esa aprobación exacta, el estado del lote permanece:

`REQUIERE DECISION HUMANA`
