# Diagnostico lote `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-RENDER-SHARD-DIAG-012O5`

Fecha: 2026-07-04  
Tipo: solo lectura  
Estado del lote: `VERIFICADO Y CORRECTO`  
Estado del objetivo publico `012O`: `INCOMPLETO`

## Alcance

Diagnostico de solo lectura sobre las landings pais Espana y Francia en los idiomas prioritarios:

- ES
- EN
- FR
- DE
- NL

No se modifico:

- Shopify Admin.
- LangShop.
- Tema.
- Paginas.
- Handles.
- URLs.
- Titulos.
- SEO title.
- Meta description.
- Canonicals.
- Hreflang.
- Schema.
- Menus.
- Home.
- Footer.
- Productos.
- Colecciones.
- Redirecciones.
- Precios.
- Inventario.

## Documentos y evidencias previas usadas

- `registro-cambios-ejecutados.md`.
- `addendum-plan-operativo-vigente-2026-07-04.md`.
- `resultado-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-WHITESPACE-BUMP-PURGE-012O4-2026-07-04.md`.
- CSV QA publico de `012O4`.
- Estado real Shopify Admin mediante GraphQL de solo lectura.

## Estado Admin comprobado

`VERIFICADO Y CORRECTO`

Paginas:

- Espana: `gid://shopify/Page/687276622200` / `papel-pintado-espana`.
- Francia: `gid://shopify/Page/687276654968` / `papel-pintado-francia`.

Hechos:

- Ambas paginas estan publicadas.
- El bloque editorial de enlazado pais existe en el `body` ES.
- Las traducciones EN, FR, DE y NL contienen el bloque equivalente.
- Las traducciones constan `outdated:false`.
- Handles e idiomas coinciden con lo esperado.

Datos relevantes:

- Espana `updatedAt`: `2026-07-04T14:38:21Z`.
- Francia `updatedAt`: `2026-07-04T14:39:03Z`.
- Espana digest `body_html`: `746c832dbeacf56abf7095b8edb5774803e1243046aec5e55ae20ee10fc2f7a8`.
- Francia digest `body_html`: `1e4ecb69b20f08101ebc238004b89f63143aab91f16e4b6083ebe158847e623d`.

## Matriz publica ejecutada

Archivo:

- `qa-publico-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-RENDER-SHARD-DIAG-012O5-2026-07-04.csv`

Matriz:

- 10 URLs publicas.
- 5 idiomas.
- 2 paginas pais.
- 4 user-agents:
  - Browser Chrome.
  - Googlebot.
  - Bingbot.
  - User-agent generico de QA para busqueda IA.
- 2 rondas.

Total: 80 solicitudes.

## Resultado publico

`INCOMPLETO`

Resumen:

- Total: 80 solicitudes.
- PASS: 11.
- FAIL: 69.
- `noindex`: 0.
- Canonicals incorrectos detectados: 0.
- Timeouts tecnicos puntuales: 2.

Por user-agent:

| User-agent | PASS | FAIL |
|---|---:|---:|
| Browser Chrome | 3 | 17 |
| Googlebot | 2 | 18 |
| Bingbot | 2 | 18 |
| QA generico busqueda IA | 4 | 16 |

Por pagina:

| Pagina | PASS | FAIL |
|---|---:|---:|
| Espana | 2 | 38 |
| Francia | 9 | 31 |

Por idioma:

| Idioma | PASS | FAIL |
|---|---:|---:|
| ES | 0 | 16 |
| EN | 0 | 16 |
| FR | 2 | 14 |
| DE | 3 | 13 |
| NL | 6 | 10 |

Motivos de fallo:

| Motivo | Casos |
|---|---:|
| Falta heading pais y falta enlace pais cruzado | 65 |
| Falta heading pais | 2 |
| Timeout + falta bloque | 2 |

## Evidencia tecnica de headers

Hechos observados:

- La mayoria de respuestas muestran `theme;desc="178399019384"`.
- La mayoria de respuestas muestran `pageType;desc="page"`.
- `cf-cache-status` aparece como `DYNAMIC`.
- No hay concentracion unica en un `servedBy` concreto: hay multiples `servedBy`, con mezcla de PASS y FAIL.
- No hay evidencia de `noindex`.
- No hay evidencia de canonicals rotos.

Interpretacion:

- No parece un problema de tema equivocado.
- No parece un problema de canonical.
- No parece un problema de robots/noindex.
- No parece un problema aislado de un unico bot.
- No parece un simple `HIT` de Cloudflare.

Inferencia tecnica razonable:

El desfase esta probablemente en una capa de render/storefront/translation cache o shard interno entre Shopify storefront y/o LangShop. Esta inferencia esta basada en:

1. Admin GraphQL correcto.
2. Traducciones `outdated:false`.
3. Tema publico correcto en headers.
4. Storefront publico inestable segun idioma/user-agent/ronda.
5. Respuestas mayoritariamente dinamicas y con `servedBy` variable.

No se puede atribuir la causa exacta a Shopify o LangShop sin soporte o herramienta interna de purge/flush.

## Conclusion

El diagnostico `012O5` queda completado como `VERIFICADO Y CORRECTO`.

El objetivo original `012O` no puede cerrarse como `CORREGIDO Y VERIFICADO`, porque el bloque de enlazado interno aun no esta estable en storefront publico.

No conviene seguir haciendo escrituras de contenido a ciegas. Ya se ha comprobado:

1. Escritura normal de contenido: Admin correcto, publico no estable.
2. Same-value purge: insuficiente.
3. Whitespace bump con `updatedAt` real: Admin correcto, publico no estable.
4. Matriz shard/render: confirma desfase publico persistente.

## Recomendacion

Siguiente paso seguro:

`MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SUPPORT-EVIDENCE-012O6`

Tipo: preparacion de evidencia y decision, sin escritura automatica.

Objetivo:

1. Preparar un ticket tecnico para Shopify y/o LangShop con:
   - GIDs.
   - URLs.
   - `updatedAt`.
   - Digests.
   - CSV de 80 solicitudes.
   - Ejemplos `x-request-id`, `servedBy`, `theme`, idioma y user-agent.
2. Pedir confirmacion/purge/flush de cache de storefront/render/traduccion.
3. Mantener prohibido cualquier cambio adicional de contenido hasta respuesta o recheck estable.

Alternativa de bajo riesgo:

`MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-STABILITY-RECHECK-012O5B`

Tipo: solo lectura.

Objetivo: repetir la matriz tras un intervalo de propagacion antes de escalar a soporte.

