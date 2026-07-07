# QA MW-BING-AI-CITED-URLS-CANONICAL-INDEXABILITY-QA-013E7 — 2026-07-04

## Estado

`VERIFICADO PERO MEJORABLE`

Auditoría pública de solo lectura sobre las 7 URLs citadas por Microsoft Copilot/partners en Bing Webmaster Tools / AI Performance. No se ha modificado Shopify, Bing, IndexNow, sitemap, DNS, CDN, tema, páginas, robots, URLs, handles ni SEO fields.

## Fuente de URLs

`VERIFICADO Y CORRECTO`

- Lote origen: `MW-BING-WEBMASTER-AI-PERFORMANCE-PAGES-EXPORT-013E6`.
- Archivo origen: `C:\Users\d.bermejo\OneDrive - Matchwalls\Escritorio\matchwalls.com_AIPageStatsReport_7_4_2026 ORO.csv`.
- Total URLs auditadas: `7`.
- Total citas auditadas: `10`.

## Resultado técnico global

`VERIFICADO Y CORRECTO`

Las 7 URLs citadas cumplen la base técnica mínima:

- HTTP `200`.
- Canonical a sí mismas.
- Sin `noindex` detectado.
- Permitidas por `robots.txt` para `bingbot`.
- `h1` único detectado.
- `hreflang` presente, con 8 alternates detectados: `x-default`, `es`, `pt`, `fr`, `de`, `it`, `en`, `nl`.

Por tanto, el problema principal no es que Bing/Copilot esté citando URLs técnicamente rotas. El problema es decidir si todas esas URLs son estratégicamente deseables como fuentes IA.

## Matriz resumida

`VERIFICADO PERO MEJORABLE`

| URL | Citas | HTTP | Canonical | Noindex | Robots Bing | HTML lang | H1 | Estado estratégico |
|---|---:|---:|---|---|---|---|---|---|
| `https://www.matchwalls.com/blogs/inspiracion/aprende-a-empapelar-paredes-y-techos-con-calidades-non-woven-vinilicas-y-peel-and-stick` | 2 | 200 | self | no | permitido | `es` | `Aprende a Empapelar Paredes y Techos con Calidades Non Woven, Vinílicas y Peel and Stick` | `VERIFICADO PERO MEJORABLE` |
| `https://www.matchwalls.com/en/collections/castellon-wallpaper` | 2 | 200 | self | no | permitido | `en` | `Castellón Wallpaper` | `VERIFICADO PERO MEJORABLE` |
| `https://www.matchwalls.com/pt/pages/como-fazer-medicoes-de-parede` | 2 | 200 | self | no | permitido | `pt-PT` | `Como medir paredes` | `REQUIERE DECISION HUMANA` |
| `https://www.matchwalls.com/en/pages/professional-form` | 1 | 200 | self | no | permitido | `en` | `Professional form` | `VERIFICADO PERO MEJORABLE` |
| `https://www.matchwalls.com/en/collections/` | 1 | 200 | self | no | permitido | `en` | `All collections` | `RIESGO CRITICO` |
| `https://www.matchwalls.com/pages/medidas-paredes` | 1 | 200 | self | no | permitido | `es` | `Cómo tomar medidas de paredes` | `VERIFICADO PERO MEJORABLE` |
| `https://www.matchwalls.com/products/gingham-charm-rosa` | 1 | 200 | self | no | permitido | `es` | `Gingham Charm Rosa` | `VERIFICADO PERO MEJORABLE` |

## Títulos SEO limpios detectados

`VERIFICADO Y CORRECTO`

Se corrigió una extracción inicial del parser: los iconos SVG de pagos del footer contienen etiquetas internas `<title>`, por lo que el campo de título se recalculó usando el primer `<title>` del `<head>`.

Títulos reales detectados:

- Blog instalación: `Cómo empapelar pared con papel pintado`.
- EN Castellón: `Buy Wallpaper Castellón - MatchWalls`.
- PT mediciones: `Como medir paredes – MatchWalls`.
- EN professional form: `Professional Account – Form`.
- EN collections root: `Collections`.
- ES medidas: `Cómo tomar las medidas de paredes - MatchWalls`.
- Producto: `Papel Pintado Gingham Charm Rosa`.

## Lectura estratégica

### URLs positivas o aprovechables

`VERIFICADO PERO MEJORABLE`

- Blog ES sobre empapelado/materiales: buena candidata para reforzar como contenido citable.
- Página ES de medición: alineada con estrategia de contenido útil.
- Página EN profesional: alineada con B2B y clientes profesionales.
- Producto citado: señal comercial útil, aunque requiere QA de ficha si se decide potenciar.

### URLs que requieren decisión

`REQUIERE DECISION HUMANA`

- `https://www.matchwalls.com/pt/pages/como-fazer-medicoes-de-parede`
  - Está técnicamente correcta.
  - Tiene 2 citas.
  - Pero PT está fuera de prioridad activa según estrategia vigente.
  - No conviene bloquearla ni modificarla sin una decisión explícita sobre PT defensivo.

- `https://www.matchwalls.com/en/collections/castellon-wallpaper`
  - Técnicamente correcta y citada 2 veces.
  - Puede ser oportunidad GEO o deuda de colección geográfica legacy.
  - Castellón no forma parte de la lista prioritaria España/Francia aportada para protección/mejora inicial.
  - Requiere revisión de contenido, finalidad, canibalización y política de colecciones geográficas.

### URL crítica

`RIESGO CRITICO`

- `https://www.matchwalls.com/en/collections/`
  - Técnicamente indexable y citable.
  - H1: `All collections`.
  - Title: `Collections`.
  - Es una ruta genérica, no una respuesta clara a una intención.
  - Que Copilot/partners la citen puede diluir señales y enviar a IA hacia una página poco explicativa.
  - No se debe noindexar ni cambiar sin auditoría, pero sí debe ser el primer diagnóstico de deuda.

## Conclusión

`VERIFICADO PERO MEJORABLE`

Bing/Copilot cita URLs técnicamente válidas de MatchWalls. La prioridad ya no es “hacer que Bing vea la web”: Bing la ve, lee el sitemap, tiene AI Performance y cita páginas.

La prioridad ahora es quirúrgica:

1. evitar que fuentes genéricas como `/en/collections/` sean fuente principal para IA;
2. decidir qué hacer con PT citado fuera de prioridad;
3. reforzar las páginas citable útiles en ES/EN;
4. abrir brecha FR/DE/NL, que no aparecen citados en el export actual.

## Evidencia generada

- Matriz CSV: `canonical-indexability-MW-BING-AI-CITED-URLS-CANONICAL-INDEXABILITY-QA-013E7-2026-07-04.csv`.
- JSON técnico: `diagnostico-data-MW-BING-AI-CITED-URLS-CANONICAL-INDEXABILITY-QA-013E7-2026-07-04.json`.

## Siguiente lote recomendado

`MW-BING-AI-CITED-EN-COLLECTIONS-ROOT-DIAG-013E8`

Objetivo:

- diagnosticar solo lectura `https://www.matchwalls.com/en/collections/`;
- comprobar si está en sitemap;
- revisar contenido visible;
- revisar enlaces internos que apuntan ahí;
- revisar canonical/hreflang ya detectados en más detalle;
- decidir si debe seguir indexable/citable, redirigir a una landing útil, mejorarse o quedar en standby.

No ejecutar cambios todavía.
