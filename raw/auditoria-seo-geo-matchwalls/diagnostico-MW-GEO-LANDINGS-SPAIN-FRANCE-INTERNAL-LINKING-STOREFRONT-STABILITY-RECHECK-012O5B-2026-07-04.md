# Diagnostico lote `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-STABILITY-RECHECK-012O5B`

Fecha: 2026-07-04  
Tipo: solo lectura  
Estado del lote: `VERIFICADO Y CORRECTO`  
Estado del objetivo publico `012O`: `INCOMPLETO`

## Alcance

Recheck de estabilidad publica sobre las landings pais Espana y Francia en los cinco idiomas prioritarios:

- ES
- EN
- FR
- DE
- NL

No se modifico:

- Shopify.
- LangShop.
- Tema.
- Paginas.
- Handles.
- URLs.
- Titulos.
- SEO meta.
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

## Metodo

Se repitio una matriz publica de 80 solicitudes:

- 10 URLs publicas.
- 2 paginas pais.
- 5 idiomas.
- 4 user-agents:
  - Browser Chrome.
  - Googlebot.
  - Bingbot.
  - User-agent generico de QA para busqueda IA.
- 2 rondas.

La senal principal fue la presencia del `href` cruzado exacto esperado en el HTML publico:

- Espana debe enlazar a Francia.
- Francia debe enlazar a Espana.

Tambien se comprobaron:

- Estado HTTP.
- Canonical.
- `noindex`.
- Tema reportado en headers.
- `content-language`.
- `x-request-id`.
- `servedBy`.
- `cf-cache-status`.

## Archivos generados

- `qa-publico-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-STABILITY-RECHECK-012O5B-2026-07-04.csv`.
- `diagnostico-data-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-STABILITY-RECHECK-012O5B-2026-07-04.json`.

## Resultado

`INCOMPLETO`

Resumen:

- Total: 80 solicitudes.
- PASS: 14.
- FAIL: 66.
- `noindex`: 0.
- Respuestas relevantes: `200`.
- Tema publico reportado: `178399019384`.

Por pagina:

| Pagina | PASS | FAIL |
|---|---:|---:|
| Espana | 7 | 33 |
| Francia | 7 | 33 |

Por idioma:

| Idioma | PASS | FAIL |
|---|---:|---:|
| ES | 3 | 13 |
| EN | 0 | 16 |
| FR | 2 | 14 |
| DE | 6 | 10 |
| NL | 3 | 13 |

Por user-agent:

| User-agent | PASS | FAIL |
|---|---:|---:|
| Browser Chrome | 5 | 15 |
| Googlebot | 5 | 15 |
| Bingbot | 2 | 18 |
| QA generico busqueda IA | 2 | 18 |

## Comparacion con diagnosticos previos

| Lote | Total | PASS | FAIL | Estado objetivo publico |
|---|---:|---:|---:|---|
| `012O5` | 80 | 11 | 69 | `INCOMPLETO` |
| `012O6` | 40 | 6 | 34 | `INCOMPLETO` |
| `012O5B` | 80 | 14 | 66 | `INCOMPLETO` |

Hay una mejora ligera frente a `012O5`, pero sigue lejos de estabilidad. El resultado no permite cerrar `012O` como `CORREGIDO Y VERIFICADO`.

## Inferencia tecnica

`VERIFICADO PERO MEJORABLE` como inferencia.

El patron sigue apuntando a render/storefront/translation cache o shard:

- Algunas respuestas muestran el bloque nuevo.
- Otras respuestas, con el mismo tema publico, sirven HTML anterior sin el enlace cruzado.
- No hay evidencia de `noindex`.
- No hay evidencia de canonical roto.
- No hay evidencia de tema equivocado.
- El fallo no se limita a un user-agent.

La causa exacta no esta demostrada sin respuesta tecnica de Shopify/LangShop.

## Decision operativa

No ejecutar mas escrituras de contenido sobre estas paginas.

El siguiente paso seguro sigue siendo:

1. Enviar/continuar tickets a Shopify y LangShop con la evidencia ya preparada en `012O6`.
2. Solicitar escalado a Storefront Rendering / Infrastructure en Shopify si el primer nivel no puede actuar.
3. Esperar respuesta tecnica o purge/flush confirmado antes de cualquier nuevo cambio.

## Estado final

El lote `012O5B` queda `VERIFICADO Y CORRECTO` como recheck de solo lectura.  
El objetivo `012O` sigue `INCOMPLETO`.

