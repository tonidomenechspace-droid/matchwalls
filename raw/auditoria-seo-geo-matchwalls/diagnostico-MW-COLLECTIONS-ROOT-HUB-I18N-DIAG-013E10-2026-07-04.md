# Diagnóstico MW-COLLECTIONS-ROOT-HUB-I18N-DIAG-013E10 — 2026-07-04

## Estado

`RIESGO CRITICO`

Diagnóstico público de solo lectura de los hubs raíz de colecciones en los cinco idiomas prioritarios:

- `https://www.matchwalls.com/collections/`
- `https://www.matchwalls.com/en/collections/`
- `https://www.matchwalls.com/fr/collections/`
- `https://www.matchwalls.com/de/collections/`
- `https://www.matchwalls.com/nl/collections/`

No se ha modificado Shopify, Bing, IndexNow, sitemap, DNS, CDN, tema, páginas, colecciones, `robots.txt`, URLs, handles, redirecciones, canonicals, hreflang, LangShop ni campos SEO.

## Motivo del lote

`VERIFICADO PERO MEJORABLE`

En `MW-BING-AI-CITED-EN-COLLECTIONS-ROOT-DIAG-013E8` se confirmó que `https://www.matchwalls.com/en/collections/` fue citada por Microsoft Copilot/partners y que no era una URL accidental: responde `200`, está indexable, aparece en sitemap y está enlazada internamente.

Este lote amplía el diagnóstico a ES, EN, FR, DE y NL para evitar una decisión aislada sobre una sola variante.

## Resultado técnico comparativo

`VERIFICADO Y CORRECTO`

Las cinco URLs:

- Responden HTTP `200`.
- Tienen canonical a sí mismas.
- No tienen `noindex` detectado.
- Tienen `hreflang` con 8 variantes detectadas.
- Están presentes en sitemaps hijos de colecciones.
- Tienen un único H1.
- Funcionan como hubs/listados reales de colecciones.

| Idioma | URL | Title | H1 | H2 detectados | Enlaces únicos | Enlaces a colecciones | Enlaces a productos | Sitemap |
|---|---|---|---|---:|---:|---:|---:|---|
| ES | `https://www.matchwalls.com/collections/` | `Colecciones` | `Todas las colecciones` | 49 | 111 | 76 | 0 | Sí |
| EN | `https://www.matchwalls.com/en/collections/` | `Collections` | `All collections` | 49 | 111 | 76 | 0 | Sí |
| FR | `https://www.matchwalls.com/fr/collections/` | `Collections` | `Toutes les collections` | 49 | 111 | 76 | 0 | Sí |
| DE | `https://www.matchwalls.com/de/collections/` | `Sammlungen` | `Alle Sammlungen` | 49 | 111 | 76 | 0 | Sí |
| NL | `https://www.matchwalls.com/nl/collections/` | `Collecties` | `Alle collecties` | 49 | 111 | 76 | 0 | Sí |

## Sitemap

`VERIFICADO Y CORRECTO`

Se detectaron 29 sitemaps hijos desde `https://www.matchwalls.com/sitemap.xml`.

Cada hub raíz aparece en su sitemap hijo de colecciones correspondiente:

- ES: `https://www.matchwalls.com/sitemap_collections_1.xml?from=436915699939&to=665363448184`.
- EN: `https://www.matchwalls.com/en/sitemap_collections_1.xml?from=436915699939&to=665363448184`.
- FR: `https://www.matchwalls.com/fr/sitemap_collections_1.xml?from=436915699939&to=665363448184`.
- DE: `https://www.matchwalls.com/de/sitemap_collections_1.xml?from=436915699939&to=665363448184`.
- NL: `https://www.matchwalls.com/nl/sitemap_collections_1.xml?from=436915699939&to=665363448184`.

Conclusión: los hubs raíz están enviados activamente a buscadores. Bing/Copilot no los descubre por accidente.

## Hreflang

`VERIFICADO Y CORRECTO`

Las cinco variantes contienen el mismo set de hreflang detectado:

- `x-default`
- `es`
- `pt`
- `fr`
- `de`
- `it`
- `en`
- `nl`

La presencia de IT/PT en hreflang no es un fallo por sí misma, pero IT/PT están fuera de prioridad activa según el addendum vigente salvo autorización expresa.

## Contenido visible

`VERIFICADO PERO MEJORABLE`

Los hubs muestran un patrón muy parecido:

- Título/H1 genérico.
- 49 encabezados H2 de colecciones.
- 76 enlaces a colecciones.
- 0 enlaces directos a productos detectados.
- Mezcla de estilos, colores, materiales, geografías y campañas.
- Presencia de `Black Friday` en los cinco idiomas.
- Presencia de colecciones geográficas mezcladas con categorías comerciales.

Ejemplos detectados:

- ES: `Nuevos Papeles Pintados`, `Ofertas`, `Papel Pintado 3D`, `Papel pintado Albacete`, `Papel pintado Alicante`, `Papel pintado Barcelona`, `Papel Pintado Black Friday`.
- EN: `3D Wallpaper`, `Albacete Wallpaper`, `Alicante Wallpaper`, `Barcelona Wallpaper`, `Black Friday Wallpaper`, `Botanical Wallpaper`, `Castellón Wallpaper`.
- FR: `Nouveaux Papiers Peints`, `Offres`, `Papier Peint 3D`, `Papier Peint Barcelone`, `Papier Peint Black Friday`.
- DE: `Angebote`, `Botanische Tapete`, `Neue Tapeten`, `Tapete Barcelona`, `Tapete Black Friday`.
- NL: `Aanbiedingen`, `Artistiek Behang`, `Behang Barcelona`, `Behang Black Friday`, `Behang Castellón`.

## Diagnóstico SEO/GEO/AGEO

`RIESGO CRITICO`

El problema no es técnico básico. Las URLs son rastreables e indexables. Precisamente por eso hay riesgo:

1. Son hubs genéricos, no respuestas editoriales claras.
2. Están en sitemap y enlazadas.
3. Pueden ser usadas por Bing/Copilot y otros sistemas IA como fuentes de baja calidad contextual.
4. Mezclan colecciones útiles con campañas obsoletas o potencialmente no prioritarias.
5. El contenido no explica suficientemente qué vende MatchWalls, cómo elegir, materiales, estancias, personalización, muestras o uso profesional.
6. Las geografías aparecen como listados de colección, no como arquitectura GEO editorial controlada.

## Impacto por idioma

### ES

`VERIFICADO PERO MEJORABLE`

La página es comprensible, pero genérica. Puede competir con páginas más fuertes como guías, landings país, medición, materiales o colecciones priorizadas.

### EN

`RIESGO CRITICO`

La variante EN ya aparece citada por Microsoft Copilot/partners. Es la señal más urgente de que el hub genérico está entrando en la capa IA.

### FR

`VERIFICADO PERO MEJORABLE`

Indexable y en sitemap. No apareció citada en el CSV actual de Bing AI, pero tiene el mismo patrón de riesgo.

### DE

`VERIFICADO PERO MEJORABLE`

Indexable y en sitemap. El contenido parece traducido, pero sigue siendo un listado genérico. Requiere control antes de escalar estrategia DE.

### NL

`VERIFICADO PERO MEJORABLE`

Indexable y en sitemap. El contenido parece traducido, pero mantiene mezcla de geografías/categorías/campañas.

## Opciones descartadas ahora

`REQUIERE DECISION HUMANA`

No se recomienda ejecutar todavía:

- `noindex` masivo.
- Redirecciones.
- Cambios de handles.
- Eliminación de colecciones.
- Cambios de sitemap.
- Edición de theme/template.
- Cambios en LangShop.

La razón es sencilla: son hubs reales y multilingües. Una acción rápida puede resolver una cita débil, pero crear deuda técnica mayor.

## Recomendación quirúrgica

`REQUIERE DECISION HUMANA`

Siguiente lote recomendado:

`MW-COLLECTIONS-ROOT-HUB-I18N-POLICY-PROPOSAL-013E11`

Objetivo del lote:

- Definir política para los hubs raíz de colecciones.
- Decidir si deben:
  - mantenerse y mejorarse como hubs editoriales/citables;
  - quedar indexables con ajustes mínimos;
  - pasar a `noindex`;
  - redirigirse;
  - o quedar en `STANDBY`.
- Separar decisión por idioma si procede.
- Separar decisión de campañas obsoletas como Black Friday.
- Separar decisión de colecciones geográficas legacy.
- Proponer una ejecución reversible si se decide escribir.

## Recomendación profesional provisional

`REQUIERE DECISION HUMANA`

No cerrar estos hubs con noindex inmediato.

La vía más sólida para SEO/GEO/AGEO es convertirlos en hubs útiles o crear una alternativa editorial fuerte antes de retirar señales. Si se decide mantenerlos indexables, deben dejar de ser un simple listado y convertirse en páginas de ayuda real:

- Qué tipos de papel pintado y murales existen.
- Cómo elegir por estancia, estilo, color y material.
- Enlaces a muestras, medición, instalación, profesionales y personalización.
- Grupos claros de colecciones.
- Eliminación o degradación de campañas obsoletas.
- Coherencia ES/EN/FR/DE/NL.

## Evidencia generada

- Diagnóstico: `diagnostico-MW-COLLECTIONS-ROOT-HUB-I18N-DIAG-013E10-2026-07-04.md`.
- Matriz: `collections-root-hub-i18n-MW-COLLECTIONS-ROOT-HUB-I18N-DIAG-013E10-2026-07-04.csv`.

## Estado final

`RIESGO CRITICO`

Los hubs raíz de colecciones son técnicamente correctos, pero estratégicamente débiles como fuentes IA. La prioridad no es ocultarlos a ciegas, sino decidir una política multilingüe y después ejecutar con aprobación exacta.
