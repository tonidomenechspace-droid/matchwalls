# Propuesta MW-COLLECTIONS-ROOT-HUB-I18N-POLICY-PROPOSAL-013E11 — 2026-07-04

## Estado

`REQUIERE DECISION HUMANA`

Propuesta de política para los hubs raíz de colecciones en los cinco idiomas prioritarios:

- `https://www.matchwalls.com/collections/`
- `https://www.matchwalls.com/en/collections/`
- `https://www.matchwalls.com/fr/collections/`
- `https://www.matchwalls.com/de/collections/`
- `https://www.matchwalls.com/nl/collections/`

No se ha modificado Shopify, Bing, IndexNow, sitemap, DNS, CDN, tema, páginas, colecciones, `robots.txt`, URLs, handles, redirecciones, canonicals, hreflang, LangShop ni campos SEO.

## Base verificada

`VERIFICADO Y CORRECTO`

Según `MW-COLLECTIONS-ROOT-HUB-I18N-DIAG-013E10`:

- 5/5 hubs responden HTTP `200`.
- 5/5 tienen canonical a sí mismos.
- 5/5 no tienen `noindex`.
- 5/5 tienen hreflang.
- 5/5 están en sitemaps hijos de colecciones.
- 5/5 tienen un H1.
- 5/5 muestran 49 H2 de colecciones.
- 5/5 tienen 76 enlaces a colecciones y 0 enlaces directos a productos detectados.
- La variante EN ya fue citada por Microsoft Copilot/partners.

## Problema que debe resolver la política

`RIESGO CRITICO`

Los hubs raíz de colecciones son técnicamente válidos, pero editorialmente débiles como fuente SEO/GEO/AGEO:

1. Son listados genéricos.
2. Mezclan estilos, colores, materiales, geografías y campañas.
3. Incluyen `Black Friday` en los cinco idiomas.
4. No explican con suficiente claridad qué vende MatchWalls, cómo elegir, qué materiales existen, cuándo pedir muestras, cómo medir, cómo personalizar o cuándo contactar como profesional.
5. Son indexables y están enviados en sitemap, así que pueden ser citados por Bing/Copilot u otros sistemas IA.

## Política recomendada

`REQUIERE DECISION HUMANA`

No aplicar noindex ni redirecciones ahora.

La política recomendada es:

1. Mantener los hubs raíz temporalmente indexables.
2. No aceptarlos como estado final.
3. Auditar primero la fuente real de renderizado en Shopify/theme/LangShop.
4. Si existe vía limpia y reversible, convertirlos en hubs editoriales/citables.
5. Si no existe vía limpia o el coste/riesgo es excesivo, evaluar noindex selectivo en un lote posterior.

## Estado objetivo si se mantienen indexables

`VERIFICADO PERO MEJORABLE`

Cada hub raíz debe pasar de “listado de colecciones” a “página de orientación”:

- Introducción clara en el idioma correspondiente.
- Bloques de navegación por intención:
  - estilos;
  - estancias;
  - colores;
  - materiales;
  - muestras;
  - medición;
  - instalación;
  - personalización;
  - profesionales/B2B;
  - colecciones geográficas solo si están priorizadas.
- Enlaces hacia páginas de alto valor real.
- Reducción de campañas obsoletas o no estratégicas.
- Coherencia editorial ES, EN, FR, DE y NL.
- Sin claims no demostrados.
- Sin cambios de handle ni URL.

## Política por tipo de elemento

### Hubs raíz de colecciones

`REQUIERE DECISION HUMANA`

Mantener temporalmente indexables y preparar mejora editorial solo si la fuente de implementación es segura.

### Black Friday

`REQUIERE DECISION HUMANA`

No resolver dentro del hub raíz. Debe tratarse como sublote independiente porque puede afectar colecciones, navegación, campañas, indexabilidad y enlaces históricos.

Recomendación: separar en un lote posterior de decisión:

`MW-COLLECTIONS-BLACK-FRIDAY-HUB-CLEANUP-DECISION-013E14`

### Colecciones geográficas legacy

`STANDBY`

No resolver dentro del hub raíz. Ya existe deuda previa de colecciones geográficas. Debe seguir la línea de indexabilidad geográfica y no mezclarse con la mejora de hubs raíz.

### IT/PT

`STANDBY`

No ampliar esta política a IT/PT salvo autorización expresa. Pueden aparecer en hreflang y sitemap, pero están fuera de prioridad activa.

### Redirecciones

`INCORRECTO`

No redirigir hubs raíz ahora. El riesgo de romper intención, navegación o señales internas es alto.

### Noindex

`REQUIERE DECISION HUMANA`

No aplicar ahora. Puede ser una opción futura si:

- no se puede convertir el hub en una página útil;
- el hub sigue generando citas IA débiles;
- existen alternativas editoriales mejores ya indexables;
- se prueba primero en un bloque pequeño y reversible.

## Arquitectura editorial recomendada

`VERIFICADO PERO MEJORABLE`

Si se decide mejorar los hubs, la estructura recomendada por idioma sería:

1. H1 más descriptivo, sin cambiar URL.
   - ES: `Colecciones de papel pintado y murales`
   - EN: `Wallpaper and mural collections`
   - FR: `Collections de papiers peints et panoramiques`
   - DE: `Tapeten- und Wandbild-Kollektionen`
   - NL: `Behang- en fotobehangcollecties`
2. Introducción corta y factual.
3. Bloques de ayuda:
   - elegir por estilo;
   - elegir por estancia;
   - elegir por color;
   - elegir por material;
   - pedir muestras;
   - medir paredes;
   - personalizar un mural;
   - soluciones para profesionales.
4. Enlaces editoriales prioritarios.
5. Listado de colecciones filtrado/ordenado si el tema lo permite.

Esta arquitectura es una propuesta editorial. No debe ejecutarse hasta confirmar dónde se controla el contenido.

## Condición crítica antes de escribir

`REQUIERE DECISION HUMANA`

Antes de cualquier escritura hay que identificar la fuente exacta:

- plantilla/theme que renderiza `/collections`;
- secciones o snippets implicados;
- si el H1/title/listado depende del tema, de Shopify nativo o de traducciones;
- si LangShop gestiona textos visibles de esa plantilla;
- si un cambio afectaría todas las variantes o solo un idioma;
- si se puede probar primero en tema draft;
- si existe rollback limpio.

## Lotes recomendados

### Siguiente lote seguro

`MW-COLLECTIONS-ROOT-HUB-I18N-SOURCE-FEASIBILITY-DIAG-013E12`

Estado: solo lectura.

Objetivo:

- Identificar fuente real de renderizado de los hubs raíz.
- Revisar tema actual/publicado y, si procede, draft seguro.
- Determinar si se puede añadir contenido editorial sin romper listados, navegación, idiomas ni rendimiento.
- No escribir nada.

### Lote posterior si 013E12 es favorable

`MW-COLLECTIONS-ROOT-HUB-I18N-COPY-ARCHITECTURE-013E13`

Estado: propuesta/copy map.

Objetivo:

- Preparar arquitectura y copy por idioma ES/EN/FR/DE/NL.
- Definir enlaces internos exactos.
- Separar Black Friday y geografías legacy.
- No escribir Shopify todavía.

### Lote de ejecución futura

Pendiente de nombre y aprobación exacta.

Solo debería proponerse si:

- 013E12 confirma fuente segura;
- 013E13 deja copy validado;
- se define rollback;
- se puede probar en draft o en bloque reversible;
- `012O` no impide validar el resultado público.

## Decisión recomendada ahora

`REQUIERE DECISION HUMANA`

Adoptar la política siguiente:

> Los hubs raíz de colecciones ES/EN/FR/DE/NL se mantienen indexables temporalmente, pero pasan a cola de mejora editorial. No se noindexan ni redirigen hasta confirmar la fuente técnica y preparar una alternativa de contenido útil, multilingüe y reversible.

## Qué no queda autorizado

`STANDBY`

No queda autorizado:

- cambiar H1;
- cambiar title/meta;
- cambiar URL/handle;
- aplicar noindex;
- redirigir;
- editar theme;
- editar LangShop;
- eliminar colecciones;
- cambiar sitemap;
- publicar cambios.

## Criterio de salida futuro

`REQUIERE DECISION HUMANA`

La deuda quedará resuelta cuando:

1. Se confirme la fuente de renderizado.
2. Se apruebe una política final.
3. Se apruebe una ejecución concreta.
4. Se implemente sin romper indexabilidad, hreflang, canonical, navegación ni rendimiento.
5. Se verifique en ES, EN, FR, DE y NL.
6. Se compruebe si Bing/Copilot deja de citar hubs genéricos o empieza a citar páginas más útiles.

## Evidencia generada

- Propuesta: `propuesta-MW-COLLECTIONS-ROOT-HUB-I18N-POLICY-PROPOSAL-013E11-2026-07-04.md`.
- Matriz: `policy-matrix-MW-COLLECTIONS-ROOT-HUB-I18N-POLICY-PROPOSAL-013E11-2026-07-04.csv`.

## Estado final

`REQUIERE DECISION HUMANA`

La política profesional es conservar señales mientras se prepara una mejora real. Lo barato aquí sería noindexar rápido; lo correcto es decidir con evidencia técnica de implementación.
