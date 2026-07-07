# Diagnóstico MW-COLLECTIONS-ROOT-HUB-I18N-SOURCE-FEASIBILITY-DIAG-013E12 — 2026-07-04

## Estado

`VERIFICADO PERO MEJORABLE`

Diagnóstico de solo lectura para identificar la fuente técnica de los hubs raíz de colecciones ES/EN/FR/DE/NL y evaluar si existe una vía segura para convertirlos en hubs editoriales/citables.

No se ha modificado Shopify, Bing, IndexNow, sitemap, DNS, CDN, tema, páginas, colecciones, `robots.txt`, URLs, handles, redirecciones, canonicals, hreflang, LangShop ni campos SEO.

## Documentos y evidencias leídos

`VERIFICADO Y CORRECTO`

- `propuesta-MW-COLLECTIONS-ROOT-HUB-I18N-POLICY-PROPOSAL-013E11-2026-07-04.md`.
- `diagnostico-MW-COLLECTIONS-ROOT-HUB-I18N-DIAG-013E10-2026-07-04.md`.
- `decision-MW-BING-AI-CITED-EN-COLLECTIONS-ROOT-DECISION-013E9-2026-07-04.md`.
- `addendum-plan-operativo-vigente-2026-07-04.md`.
- `registro-cambios-ejecutados.md`.
- Copia local de tema: `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E`.

## Estado público comprobado

`VERIFICADO Y CORRECTO`

Las cinco URLs revisadas siguen sirviendo el tema MAIN público:

- `https://www.matchwalls.com/collections/`
- `https://www.matchwalls.com/en/collections/`
- `https://www.matchwalls.com/fr/collections/`
- `https://www.matchwalls.com/de/collections/`
- `https://www.matchwalls.com/nl/collections/`

Evidencia pública común:

- `Shopify.theme` visible en HTML:
  - nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`
  - id: `178399019384`
  - schema: `Impact`
  - versión: `5.1.0`
  - role: `main`
- Las cinco variantes contienen:
  - `shopify-section--main-list-collections`
  - `<collection-list>`
  - `collection-card`
  - `content-over-media`
  - H1 traducido de “all collections”.

Conclusión: el storefront público real usa una sección de tipo `main-list-collections`. No es una página Shopify normal ni un bloque editorial de página.

## Fuente local encontrada

`VERIFICADO PERO MEJORABLE`

Solo se encontró una copia local completa de tema:

- `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E`

Archivos relevantes:

- `templates/list-collections.json`
- `sections/main-list-collections.liquid`
- `layout/theme.liquid`
- `locales/es.json`
- `locales/en.default.json`
- `locales/fr.json`
- `locales/de.json`
- `locales/nl.json`

Limitación:

`NO ACCESIBLE`

No se ha podido leer directamente el asset actual del theme MAIN desde Shopify Admin/CLI en este lote. La CLI `shopify` no está disponible en el entorno local. Por tanto, la copia local no debe tratarse como fuente absoluta del MAIN actual. Aun así, el HTML público confirma que el MAIN renderiza la misma clase/sección esperada.

## Fuente del template

`VERIFICADO PERO MEJORABLE`

En la copia local:

`templates/list-collections.json`

contiene:

```json
{
  "sections": {
    "main": {
      "type": "main-list-collections",
      "settings": {
        "collections": [],
        "collections_per_row_mobile": "1",
        "collections_per_row": 3,
        "text_color": "#ffffff",
        "overlay_color": "#000000",
        "overlay_opacity": 30
      }
    }
  },
  "order": ["main"]
}
```

También existe:

`templates/page.list-collections.json`

con:

```json
{
  "sections": {
    "main": {
      "type": "main-list-collections",
      "settings": {}
    }
  },
  "order": ["main"]
}
```

Interpretación:

- La ruta raíz `/collections` usa el template de listado de colecciones.
- No es una página editable como `Online Store > Pages`.
- El contenido visible principal depende de `sections/main-list-collections.liquid` y de la configuración del template.

## Fuente del H1

`VERIFICADO Y CORRECTO`

En `sections/main-list-collections.liquid`, el H1 se genera así:

```liquid
<h1 class="h1 text-center">{{ 'collection.general.all_collections' | t }}</h1>
```

Valores localizados encontrados:

| Archivo | Valor |
|---|---|
| `es.json` | `Todas las colecciones` |
| `en.default.json` | `All collections` |
| `fr.json` | `Toutes les collections` |
| `de.json` | `Alle Sammlungen` |
| `nl.json` | `Alle collecties` |

Interpretación:

- El H1 visible no viene de una página Shopify.
- Viene de una clave de idioma del tema.
- Cambiar solo la traducción del H1 es técnicamente posible, pero no resolvería el problema estratégico del hub.

## Fuente del listado de colecciones

`VERIFICADO Y CORRECTO`

En `sections/main-list-collections.liquid`, el listado se genera así:

```liquid
{%- paginate collections by 48 -%}
  <collection-list class="collection-list">
    {% assign collections_list = section.settings.collections | default: collections %}

    {%- for collection in collections_list -%}
      <a href="{{ collection.url }}" class="collection-card" reveal-js>
        ...
        <h2 class="h2">{{ collection.title | escape }}</h2>
        ...
      </a>
    {%- endfor -%}
  </collection-list>
{%- endpaginate -%}
```

Interpretación:

- Si `section.settings.collections` está vacío, Shopify usa el objeto global `collections`.
- Esto explica que aparezcan colecciones mezcladas: estilos, colores, geografías y Black Friday.
- El schema de la sección permite seleccionar una lista manual de colecciones con `collection_list`, límite `48`.

## Fuente del title/meta/canonical/hreflang

`VERIFICADO PERO MEJORABLE`

En `layout/theme.liquid`, la copia local muestra:

- `<title>` basado en `page_title`.
- `<meta name="description">` basado en `page_description`.
- canonical basado en `canonical_url`.
- `content_for_header` con reemplazos de hreflang.

Interpretación:

- El title y meta description del hub no están dentro de `main-list-collections.liquid`.
- Vienen del comportamiento global de Shopify/theme para `page_title` y `page_description`.
- La gestión SEO del head no debe mezclarse con el contenido visible sin confirmar la fuente actual del MAIN.

## Vías de implementación futuras

### Vía A — Curar la lista de colecciones desde settings

Estado: `VERIFICADO PERO MEJORABLE`

Posible porque la sección tiene setting:

```json
{
  "type": "collection_list",
  "id": "collections",
  "label": "Selected collections",
  "limit": 48
}
```

Ventajas:

- No requiere tocar Liquid si se puede hacer desde Theme Editor o JSON del template.
- Permite excluir `Black Friday`, geografías legacy o colecciones no prioritarias del hub raíz.
- Reversible.
- Afecta a todos los idiomas usando las mismas colecciones con sus traducciones.

Limitaciones:

- No añade explicación editorial.
- No mejora por sí solo el H1/title/meta.
- Requiere elegir una lista exacta de colecciones.
- Debe probarse en draft o con rollback.

### Vía B — Añadir sección editorial antes del listado

Estado: `REQUIERE DECISION HUMANA`

Posible si el template `list-collections.json` permite añadir secciones como `rich-text`, `custom-liquid` o una sección específica.

Ventajas:

- Añade contexto SEO/GEO/AGEO sin reescribir todo el listado.
- Puede enlazar a muestras, medición, instalación, materiales, personalización y profesionales.
- Menor riesgo que modificar directamente la lógica del listado.

Riesgos:

- Puede generar contenido duplicado si se añade otro H1.
- Las traducciones deberían gestionarse con LangShop/theme translations.
- Necesita QA público en ES/EN/FR/DE/NL.
- El bloqueo histórico `012O` aconseja validar con rechecks múltiples después de cualquier escritura.

### Vía C — Modificar `main-list-collections.liquid`

Estado: `REQUIERE DECISION HUMANA`

Posible, pero de mayor riesgo.

Ventajas:

- Permite control total sobre H1, intro, grupos, enlaces y render.
- Puede convertir realmente la página en un hub editorial.

Riesgos:

- Afecta la plantilla global de `/collections`.
- Puede impactar todos los idiomas.
- Requiere validación Liquid, prueba en draft y rollback exacto.
- Requiere traducciones de tema bien controladas.

### Vía D — Cambiar solo claves de idioma del H1

Estado: `VERIFICADO PERO MEJORABLE`

Posible, pero insuficiente.

Ventajas:

- Cambio pequeño.
- Mejora el H1.

Riesgos:

- No resuelve el listado mixto ni la ausencia de contexto.
- Puede afectar cualquier otro uso de `collection.general.all_collections`.

### Vía E — Noindex o redirección

Estado: `INCORRECTO`

No recomendado ahora. Esta vía no mejora el hub; solo lo retira o redirige. Según 013E11, debe quedar como opción futura si no existe una vía segura de mejora.

## Feasibility final

`VERIFICADO PERO MEJORABLE`

Sí existe una vía técnica plausible para mejorar los hubs raíz sin tocar handles ni redirecciones:

1. Curar manualmente la lista de colecciones.
2. Añadir contexto editorial antes del listado.
3. Traducir/validar ES, EN, FR, DE y NL.
4. Probar primero en un entorno/draft.

Pero no queda autorizado ejecutar nada todavía.

## Recomendación quirúrgica

`REQUIERE DECISION HUMANA`

Siguiente lote recomendado:

`MW-COLLECTIONS-ROOT-HUB-I18N-COPY-ARCHITECTURE-013E13`

Objetivo:

- Definir estructura editorial exacta del hub.
- Preparar copy ES/EN/FR/DE/NL.
- Definir enlaces internos prioritarios.
- Definir lista de colecciones recomendada para el hub.
- Separar Black Friday y geografías legacy.
- No escribir Shopify.

Después, si Daniel aprueba, se podrá preparar una propuesta de ejecución en draft/theme con:

- recurso exacto;
- valor actual;
- valor propuesto;
- respaldo;
- rollback;
- QA público;
- validación por idioma.

## Qué no queda autorizado

`STANDBY`

No queda autorizado:

- editar `templates/list-collections.json`;
- editar `sections/main-list-collections.liquid`;
- cambiar claves de idioma;
- cambiar H1/title/meta;
- seleccionar colecciones manualmente;
- tocar LangShop;
- aplicar noindex;
- redirigir;
- publicar.

## Evidencia generada

- Diagnóstico: `diagnostico-MW-COLLECTIONS-ROOT-HUB-I18N-SOURCE-FEASIBILITY-DIAG-013E12-2026-07-04.md`.
- Matriz: `source-feasibility-MW-COLLECTIONS-ROOT-HUB-I18N-SOURCE-FEASIBILITY-DIAG-013E12-2026-07-04.csv`.

## Estado final

`VERIFICADO PERO MEJORABLE`

La fuente visible de los hubs raíz está en el tema, no en páginas Shopify. La ruta profesional es preparar copy/arquitectura y ejecutar solo después en draft o con un lote de escritura quirúrgico aprobado.
