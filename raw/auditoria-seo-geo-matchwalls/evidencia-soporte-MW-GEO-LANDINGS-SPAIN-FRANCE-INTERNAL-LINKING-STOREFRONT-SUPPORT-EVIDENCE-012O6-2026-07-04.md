# Paquete de evidencia soporte `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SUPPORT-EVIDENCE-012O6`

Fecha: 2026-07-04  
Tipo: documental / soporte  
Estado del lote: `VERIFICADO Y CORRECTO`  
Estado del objetivo `012O`: `INCOMPLETO`

## Resumen ejecutivo

Shopify Admin contiene correctamente el bloque editorial de enlazado interno entre las paginas pais de Espana y Francia en ES, EN, FR, DE y NL. Las traducciones estan `outdated:false` y los digests son vigentes.

Sin embargo, el storefront publico sigue sirviendo HTML inconsistente: algunas respuestas muestran el bloque y otras sirven el cuerpo anterior sin el bloque, aun con el mismo tema publicado y sin errores de canonical o `noindex`.

No se recomienda seguir haciendo escrituras de contenido a ciegas. Se recomienda escalar a soporte Shopify y/o LangShop con evidencia para confirmar/purgar/limpiar cache de render/storefront/traduccion.

## Recursos afectados

### Espana

- GID: `gid://shopify/Page/687276622200`
- Handle base: `papel-pintado-espana`
- `updatedAt`: `2026-07-04T14:38:21Z`
- Digest `body_html`: `746c832dbeacf56abf7095b8edb5774803e1243046aec5e55ae20ee10fc2f7a8`

URLs:

- ES: `https://www.matchwalls.com/pages/papel-pintado-espana`
- EN: `https://www.matchwalls.com/en/pages/spain-wallpaper`
- FR: `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`
- DE: `https://www.matchwalls.com/de/pages/spanien-tapete`
- NL: `https://www.matchwalls.com/nl/pages/spanje-behang`

### Francia

- GID: `gid://shopify/Page/687276654968`
- Handle base: `papel-pintado-francia`
- `updatedAt`: `2026-07-04T14:39:03Z`
- Digest `body_html`: `1e4ecb69b20f08101ebc238004b89f63143aab91f16e4b6083ebe158847e623d`

URLs:

- ES: `https://www.matchwalls.com/pages/papel-pintado-francia`
- EN: `https://www.matchwalls.com/en/pages/french-wallpaper`
- FR: `https://www.matchwalls.com/fr/pages/papier-peint-en-france`
- DE: `https://www.matchwalls.com/de/pages/franzosische-tapete`
- NL: `https://www.matchwalls.com/nl/pages/frans-behang`

## Estado Admin verificado

`VERIFICADO Y CORRECTO`

- Ambas paginas estan publicadas.
- El bloque editorial pais existe en `body` ES.
- Las traducciones `body_html` EN, FR, DE y NL contienen el bloque equivalente.
- Las traducciones constan `outdated:false`.
- Handles y titulos permanecen intactos.
- No se tocaron precios, inventario, redirecciones, colecciones, productos, menus ni tema.

## Bloque esperado en storefront

La pagina de Espana debe enlazar a Francia.

Ejemplo ES:

```html
<h2>Papel pintado por país</h2>
<p>Estás consultando las soluciones para España. Si tu proyecto se desarrolla en Francia o quieres comparar opciones para otro mercado, consulta la guía de <a href="/pages/papel-pintado-francia">papel pintado en Francia</a>.</p>
```

La pagina de Francia debe enlazar a Espana.

Ejemplo ES:

```html
<h2>Papel pintado por país</h2>
<p>Estás consultando las soluciones para Francia. Si tu proyecto se desarrolla en España o quieres comparar opciones para otro mercado, consulta la guía de <a href="/pages/papel-pintado-espana">papel pintado en España</a>.</p>
```

## Evidencia publica 012O5

Archivo:

- `qa-publico-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-RENDER-SHARD-DIAG-012O5-2026-07-04.csv`

Resultado:

- Total: 80 solicitudes.
- PASS: 11.
- FAIL: 69.
- `noindex`: 0.
- Canonicals incorrectos detectados: 0.
- Tema publico mayoritario: `178399019384`.
- `cf-cache-status`: mayoritariamente `DYNAMIC`.

Por user-agent:

- Browser Chrome: 3 PASS / 17 FAIL.
- Googlebot: 2 PASS / 18 FAIL.
- Bingbot: 2 PASS / 18 FAIL.
- QA generico busqueda IA: 4 PASS / 16 FAIL.

## Recheck publico 012O6

Archivo:

- `qa-publico-recheck-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SUPPORT-EVIDENCE-012O6-2026-07-04.csv`

Resultado:

- Total: 40 solicitudes.
- PASS: 6.
- FAIL: 34.
- Todas las respuestas relevantes fueron `200`.
- No se detecto `noindex`.
- Canonicals correctos.
- Tema publico en headers: `178399019384`.
- `cf-cache-status`: `DYNAMIC`.

Por pagina:

- Espana: 2 PASS / 18 FAIL.
- Francia: 4 PASS / 16 FAIL.

Por idioma:

- ES: 0 PASS / 8 FAIL.
- EN: 0 PASS / 8 FAIL.
- FR: 1 PASS / 7 FAIL.
- DE: 3 PASS / 5 FAIL.
- NL: 2 PASS / 6 FAIL.

Por user-agent:

- Browser Chrome: 2 PASS / 8 FAIL.
- Googlebot: 1 PASS / 9 FAIL.
- Bingbot: 2 PASS / 8 FAIL.
- QA generico busqueda IA: 1 PASS / 9 FAIL.

## Ejemplos de FAIL actuales 012O6

| Pagina | Idioma | User-agent | Estado | `x-request-id` | `servedBy` | Tema | Observacion |
|---|---|---|---:|---|---|---|---|
| Espana | ES | Browser Chrome | 200 | `7fea94a5-0d7a-4817-89aa-26300d73679d-1783177654` | `jhkr` | `178399019384` | No aparece `href="/pages/papel-pintado-francia"`. |
| Espana | EN | Googlebot | 200 | `edd4b1f6-b3d3-436e-b5a9-def365e5fd88-1783177658` | `7lh9` | `178399019384` | No aparece `href="/en/pages/french-wallpaper"`. |
| Espana | FR | Bingbot | 200 | `e7025196-795e-4189-8b8b-42a333cd3cb0-1783177660` | `9gtz` | `178399019384` | No aparece `href="/fr/pages/papier-peint-en-france"`. |
| Francia | ES | Browser Chrome | 200 | `816649a6-85b9-40bc-a8b6-7317c9ad1d7e-1783177666` | `ww4c` | `178399019384` | No aparece `href="/pages/papel-pintado-espana"`. |
| Francia | EN | Bingbot | 200 | `d50080d9-5903-4e33-9837-db9b6db4662f-1783177670` | `b4rn` | `178399019384` | No aparece `href="/en/pages/spain-wallpaper"`. |
| Francia | FR | Googlebot | 200 | `35dd691c-a833-4b4e-b83e-9dcd18361142-1783177672` | `8492` | `178399019384` | No aparece `href="/fr/pages/papier-peint-en-espagne"`. |

## Ejemplos de PASS actuales 012O6

| Pagina | Idioma | User-agent | Estado | `x-request-id` | `servedBy` | Tema | Observacion |
|---|---|---|---:|---|---|---|---|
| Espana | DE | Browser Chrome | 200 | `462c1375-4875-4985-a471-b1ac2a96abb6-1783177662` | `r9cv` | `178399019384` | Aparece `href="/de/pages/franzosische-tapete"`. |
| Espana | NL | Bingbot | 200 | `645d94ee-5acd-400c-9d4d-4fb92ea1853d-1783177665` | `7w8t` | `178399019384` | Aparece `href="/nl/pages/frans-behang"`. |
| Francia | FR | Browser Chrome | 200 | `cecb72d8-7cb6-48ce-a26c-009bb31f4683-1783177671` | `nxlw` | `178399019384` | Aparece `href="/fr/pages/papier-peint-en-espagne"`. |
| Francia | DE | Googlebot | 200 | `85f86c48-eee4-402f-928e-e4abb7ea273b-1783177674` | `wtg9` | `178399019384` | Aparece `href="/de/pages/spanien-tapete"`. |

## Interpretacion

`VERIFICADO PERO MEJORABLE` como inferencia tecnica.

No parece:

- Tema equivocado.
- Canonical roto.
- `noindex`.
- Error aislado de Googlebot/Bingbot.
- Error de una unica URL.
- Error de un unico `servedBy`.
- Simple cache HIT de Cloudflare.

Parece:

- Desfase de render/storefront/traduccion/cache/shard.
- Posible cache de HTML renderizado por locale/user-agent/edge/shard.
- Posible cache o capa de traduccion asociada a LangShop.

La causa exacta requiere soporte interno de Shopify/LangShop.

## Restricciones para soporte

No cambiar:

- Handles.
- URLs.
- Page title.
- Body HTML.
- Traducciones.
- Markets.
- Theme files.
- Published theme.
- SEO title/meta description.
- Redirecciones.
- Menus.
- Productos.
- Colecciones.

Solo se solicita identificar fuente tecnica del render desfasado y, si procede, purgar/limpiar cache de storefront/render/traduccion.

## Recomendacion operativa

Siguiente decision:

1. Enviar ticket a Shopify con el borrador `ticket-shopify-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SUPPORT-EVIDENCE-012O6-2026-07-04.md`.
2. Enviar ticket separado a LangShop con el borrador `ticket-langshop-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SUPPORT-EVIDENCE-012O6-2026-07-04.md`.
3. Adjuntar CSV `012O5` y recheck `012O6`.
4. No hacer nuevos cambios visibles de contenido pais hasta respuesta o recheck estable.

