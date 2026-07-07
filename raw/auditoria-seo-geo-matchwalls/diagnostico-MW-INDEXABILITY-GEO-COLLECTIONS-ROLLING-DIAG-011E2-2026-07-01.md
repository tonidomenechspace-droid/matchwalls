# Diagnostico MW-INDEXABILITY-GEO-COLLECTIONS-ROLLING-DIAG-011E2

Fecha: 2026-07-01  
Estado final: `VERIFICADO PERO MEJORABLE`  
Tipo: diagnostico de solo lectura  
Shopify: sin cambios

## Alcance

Clasificacion de colecciones geograficas restantes tras el piloto `011E1`, con prioridad limitada a:

- ES.
- EN.
- FR.
- DE.
- NL.

IT y PT-PT se documentan como presencia fuera de alcance activo y quedan en `STANDBY`.

No se modificaron colecciones, handles, redirecciones, traducciones, productos, tema, canonicals, precios, inventario ni metafields.

## Documentos y evidencias leidas

- `AGENTS.md`.
- `diagnostico-MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E-2026-06-27.md`.
- `ejecucion-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.md`.
- `geo-collections-candidates-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`.
- `qa-sitemap-geo-restante-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- `cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`.
- `plan-operativo-vigente-y-cola-lotes-seo-geo-2026-06-30.md`.

## Estado actual de sitemap

Sitemap verificado el 2026-07-01:

- Sitemap index: 29 archivos.
- URLs totales: 7.274.
- Errores de lectura: 0.

Colecciones geograficas candidatas actuales en sitemap:

| Idioma | Historicas 011E | En sitemap actual | Estado |
|---|---:|---:|---|
| ES | 58 | 52 | `VERIFICADO PERO MEJORABLE` |
| EN | 56 | 50 | `VERIFICADO PERO MEJORABLE` |
| FR | 56 | 51 | `VERIFICADO PERO MEJORABLE` |
| DE | 41 | 36 | `VERIFICADO PERO MEJORABLE` |
| NL | 52 | 46 | `VERIFICADO PERO MEJORABLE` |
| PT | 55 | 49 | `STANDBY` |
| IT | 28 | 26 | `STANDBY` |

Total actual:

- Prioridad ES/EN/FR/DE/NL: 235 URLs geograficas todavia en sitemap.
- Fuera de prioridad IT/PT: 75 URLs geograficas todavia en sitemap.
- Total geo candidato actual: 310 URLs.

Evidencias:

- `sitemap-MW-INDEXABILITY-GEO-COLLECTIONS-ROLLING-DIAG-011E2-2026-07-01.csv`.
- `qa-publico-MW-INDEXABILITY-GEO-COLLECTIONS-ROLLING-DIAG-011E2-2026-07-01.csv`.

## Estado Admin Shopify

Consulta Admin GraphQL validada y ejecutada en solo lectura sobre:

`handle:comprar-papel-pintado-*`

Resultado:

- 58 colecciones base leidas.
- 6/58 tienen `seo.hidden=1`, correspondientes al piloto `011E1`.
- 52/58 siguen sin `seo.hidden`.
- 58/58 tienen `productsCount = 73`.
- 58/58 tienen `resourcePublicationsCount = 9`.
- 58/58 tienen `sortOrder = MANUAL`.
- 58/58 comparten los mismos primeros cinco productos:
  - `highland-plaid-marron`.
  - `horizonte-natural-verde`.
  - `brizna-blanco-y-negro`.
  - `whispering-woods-azul`.
  - `bosque-tropical-acuarela-azul`.
- 58/58 muestran `updatedAt = 2026-06-29T18:16:02Z`.

Esto confirma que el patron de repeticion sigue vigente tras el piloto.

Evidencia:

- `admin-read-MW-INDEXABILITY-GEO-COLLECTIONS-ROLLING-DIAG-011E2-2026-07-01.csv`.

## QA publico

Se intento auditoria publica amplia sobre las 235 URLs prioritarias actuales.

Resultado util:

- 106/235 URLs respondieron 200 antes de activar proteccion 429.
- 106/106 tienen canonical self.
- 106/106 no tienen `noindex`.

Limitacion:

- 129/235 quedaron `NO ACCESIBLE` por rate limit 429 durante la auditoria, no por evidencia de caida publica.
- No se clasifican como `INCORRECTO`; se tratan como limitacion tecnica de lectura.
- El inventario de indexabilidad se apoya en sitemap actual + Admin + evidencias publicas previas `011E`.

Estado: `VERIFICADO PERO MEJORABLE`.

## Clasificacion operativa ES/EN/FR/DE/NL

Sobre las 235 URLs prioritarias actuales:

| Clasificacion | URLs | Criterio |
|---|---:|---|
| `REQUIERE DECISION HUMANA` | 147 | Candidatas a noindex rolling por patron repetitivo, productos identicos y ausencia de evidencia accesible de valor unico. |
| `STANDBY` | 88 | Mercados/ciudades con posible valor comercial o internacional; no aplicar noindex automatico sin GSC/ventas o decision editorial. |

Distribucion por idioma:

| Idioma | Candidato noindex / decision | STANDBY |
|---|---:|---:|
| ES | 32 | 20 |
| EN | 31 | 19 |
| FR | 32 | 19 |
| DE | 23 | 13 |
| NL | 29 | 17 |

## Criterio aplicado

### Noindex rolling recomendado

Se recomienda preparar lote de escritura solo para las colecciones geograficas no estrategicas, repetitivas y sin evidencia accesible de valor diferencial.

No significa que esas URLs esten tecnicamente rotas. Significa que, para SEO/GEO, son potencialmente perjudiciales por:

- repeticion de surtido;
- ausencia de contenido local unico verificado;
- escalado geografico masivo;
- traducciones historicamente mejorables;
- riesgo de doorway/canibalizacion;
- dilucion de rastreo y señales para IA.

### STANDBY / reescritura potencial

No se recomienda noindex automatico para ciudades/mercados con posible valor comercial o internacional sin revisar:

- Madrid.
- Barcelona.
- Valencia.
- Sevilla.
- Malaga.
- Zaragoza.
- Murcia.
- Bizkaia/Bilbao.
- Girona.
- Tarragona.
- Paris.
- Toulouse.
- Burdeos/Bordeaux.
- Lyon.
- Marsella/Marseille.
- Montpellier.
- Nantes.
- Niza/Nice.
- Lille.
- Estrasburgo/Strasbourg.

Estas URLs no quedan aprobadas como buenas. Quedan en `STANDBY` hasta decidir si se reescriben con contenido local unico o si tambien se retiran del indice.

## Datos no accesibles

`NO ACCESIBLE`

- Google Search Console por URL.
- Bing Webmaster Tools.
- GA4/Shopify Analytics por landing.
- Conversiones o ingresos por estas URLs.
- Backlinks o menciones reales por ciudad.
- Citas reales en IA.

Sin esos datos no se debe afirmar que una ciudad concreta vende, posiciona o merece conservarse indexable.

## Recomendacion

Siguiente lote de escritura posible:

`MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-ROLLING-011E3`

Pero no debe ejecutarse aun hasta presentar propuesta formal con:

- recursos exactos;
- IDs de coleccion;
- idiomas afectados;
- valores actuales;
- valores propuestos;
- respaldo;
- metodo de reversion;
- QA publico/Admin/sitemap posterior.

Propuesta quirurgica recomendada:

1. Primer rolling sobre un bloque pequeño de colecciones no estrategicas.
2. Excluir STANDBY.
3. Excluir IT/PT.
4. No tocar handles.
5. No borrar colecciones.
6. Aplicar solo `seo.hidden=1`.
7. Verificar Admin, publico y sitemap tras cache.

## Estado final

`VERIFICADO PERO MEJORABLE`

El diagnostico esta cerrado, pero la deuda no esta corregida: quedan 235 URLs geograficas prioritarias en sitemap, de las cuales 147 son candidatas a noindex rolling y 88 quedan en `STANDBY` por decision comercial/editorial.
