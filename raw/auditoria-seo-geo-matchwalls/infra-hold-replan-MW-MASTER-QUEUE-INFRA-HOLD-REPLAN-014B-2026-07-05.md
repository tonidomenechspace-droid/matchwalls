# MW-MASTER-QUEUE-INFRA-HOLD-REPLAN-014B

Fecha: 2026-07-05  
Modo: documental / solo lectura / sin cambios externos.  
Estado final: `VERIFICADO Y CORRECTO`

## Objetivo

`VERIFICADO Y CORRECTO`

Replanificar la cola maestra de SEO/GEO/AEO de MatchWalls después de la nueva evidencia de infraestructura:

- Ticket Shopify `68731900` sigue abierto.
- El reintento `013J6R` ya no mostró `429`, pero sí devolvió `500` en 2 de 5 URLs públicas.
- La actualización `013J6R1` dejó preparado el mensaje para Shopify Engineering con nuevos `x-request-id`.

Este lote no modifica Shopify, Bing Webmaster Tools, IndexNow, LangShop, Cloudflare, tema, URLs, handles, contenidos, redirecciones, robots, sitemap, schema ni apps.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `reconciliacion-MW-MASTER-QUEUE-RECONCILIATION-014A-2026-07-05.md`
- `cola-maestra-reconciliada-MW-MASTER-QUEUE-RECONCILIATION-014A-2026-07-05.csv`
- `cola-segura-mientras-shopify-engineering-2026-07-05.md`
- `public-qa-analysis-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.md`
- `support-evidence-MW-CRAWLERS-WAF-CLOUDFLARE-429-SUPPORT-EVIDENCE-013J6B-2026-07-05.md`
- `public-qa-retry-analysis-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6R-2026-07-05.md`
- `shopify-ticket-update-MW-SHOPIFY-INFRA-500-REQUEST-ID-UPDATE-013J6R1-2026-07-05.md`
- `status-MW-SHOPIFY-INFRA-500-REQUEST-ID-UPDATE-013J6R1-2026-07-05.csv`
- `registro-cambios-ejecutados.md`

## Estado real comprobado

`RIESGO CRITICO`

Hechos verificados por archivos del proyecto:

- `013J6`: 42 URLs priorizadas; 6 verificadas con `200`; 36 quedaron `INCOMPLETO` por `429`; Bingbot-like devolvió `429` en 42/42 desde el entorno QA.
- `013J6B`: se documentó el riesgo Cloudflare/WAF sin afirmar bloqueo real de Bingbot.
- `013J6R`: safety gate de 5 URLs; `200` en 3/5, `500` en 2/5, `429` en 0/5.
- `013J6R1`: mensaje preparado para ticket Shopify `68731900` con 2 nuevos `x-request-id`.

Eventos `500` añadidos a la investigación:

| URL | HTTP | CF-Ray | Shopify x-request-id |
|---|---:|---|---|
| `https://www.matchwalls.com/products/gingham-charm-verde` | 500 | `a1677b84fa654bd6-MAD` | `085d24e5-299a-4e8c-bd90-f0ba737e13bb-1783266176` |
| `https://www.matchwalls.com/en/collections/salamanca-wallpaper` | 500 | `a1677c42ca9cf91f-MAD` | `84b5fb4a-fca0-48bb-80b9-1ee7399344c6-1783266207` |

## Regla operativa vigente

`VERIFICADO Y CORRECTO`

Hasta respuesta de Shopify Engineering:

- No ejecutar crawls públicos amplios.
- No publicar temas.
- No tocar Liquid, snippets, schema en tema, app embeds, home ni layout.
- No editar páginas España/Francia, LangShop, traducciones, SEO fields visibles, handles, URLs, canonicals, redirecciones, robots, sitemap, `llms.txt`, `agents.md` ni IndexNow masivo.
- No interpretar los `500` como fallo SEO/editorial sin confirmación de ingeniería.

## Cola replanificada por carriles

### Carril A — Bloqueado por infraestructura Shopify

`STANDBY` / `RIESGO CRITICO`

No avanzar hasta respuesta de ingeniería o instrucción explícita de Shopify:

- Home / entidad principal.
- QA público completo de URLs priorizadas Bing.
- Landings España/Francia 012.
- Interlinking visible ES/FR 012O.
- Schema visible en tema.
- Hub `/collections` si implica tema/render público.
- LangShop y traducciones.
- SEO title/meta description en Shopify/LangShop.
- Robots, sitemap, `llms.txt`, `agents.md`.
- IndexNow manual o masivo.
- Cualquier publicación de tema o cambio en MAIN.

### Carril B — Seguro offline/documental

`VERIFICADO Y CORRECTO`

Se puede seguir sin tocar storefront:

- Consolidar estrategia SEO/GEO/AEO con datos ya exportados.
- Diseñar panel CEO/CMO.
- Preparar briefs DE/NL/UK/BE/USA/MX sin crear páginas.
- Redactar entidad factual MatchWalls en ES/EN/FR/DE/NL como borrador local.
- Diseñar estructura de contenidos citables.
- Mapear oportunidades Bing Search Performance sin implementación.
- Preparar checklist de QA post-infra.
- Preparar borradores de soporte y respuestas a Shopify.

### Carril C — Preparar, pero no publicar

`REQUIERE DECISION HUMANA`

Puede prepararse en documentos, pero no ejecutarse en Shopify:

- Propuestas de mejora para las 42 URLs Bing priorizadas.
- Propuestas de title/meta/H1 para colecciones/productos con señal Bing.
- Propuesta de schema global/entity, solo diseño.
- Propuesta de hub `/collections` i18n, solo documento.
- Propuesta de contenido citables/FAQ/HowTo, solo copy local.
- Propuesta de corrección de canonical/hreflang 011H, solo matriz y decisión.

### Carril D — STANDBY estratégico

`STANDBY`

No accionar salvo autorización expresa:

- PT, IT y BR.
- Legacy `matchwallsmurals` / `matchwallsmurais`.
- Noindex masivo de geográficas.
- Creación de nuevas landings fuera de España/Francia.
- Cambios de handles o arquitectura URL.
- Acciones con crawlers IA que cambien política pública.

## Orden recomendado desde ahora

`VERIFICADO Y CORRECTO`

1. Enviar o confirmar envío del mensaje preparado para ticket Shopify `68731900`.
2. Trabajar solo carril B mientras ingeniería responde.
3. Preparar carril C únicamente como documentos, sin aplicar en Shopify.
4. Cuando Shopify responda, ejecutar un postcheck de infraestructura antes de desbloquear QA pública.

## Siguiente lote seguro recomendado

`REQUIERE DECISION HUMANA`

`MW-CEO-CMO-PANEL-SPEC-014C`

Motivo:

- Es 100% documental.
- No depende de la web pública.
- Ayuda a convertir todo el trabajo SEO/GEO/AEO en medición ejecutiva.

Alternativa también segura:

`MW-ENTITY-FACTUAL-BRIEF-ES-EN-FR-DE-NL-015A`

Motivo:

- Prepara la base factual citable de MatchWalls en los cinco idiomas prioritarios.
- No requiere tocar Shopify hasta aprobación posterior.

## Archivos generados

`VERIFICADO Y CORRECTO`

- `infra-hold-replan-MW-MASTER-QUEUE-INFRA-HOLD-REPLAN-014B-2026-07-05.md`
- `infra-hold-replan-queue-MW-MASTER-QUEUE-INFRA-HOLD-REPLAN-014B-2026-07-05.csv`
- `status-MW-MASTER-QUEUE-INFRA-HOLD-REPLAN-014B-2026-07-05.csv`

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó Shopify, Bing Webmaster Tools, IndexNow, LangShop, Cloudflare, tema, URLs, handles, redirecciones, contenidos, traducciones, SEO fields, robots, sitemap, schema, productos, páginas, colecciones ni apps.
