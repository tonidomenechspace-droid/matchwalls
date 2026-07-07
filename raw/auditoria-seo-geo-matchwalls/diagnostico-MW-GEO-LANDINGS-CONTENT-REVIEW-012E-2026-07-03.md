# Diagnóstico MW-GEO-LANDINGS-CONTENT-REVIEW-012E

Fecha: 2026-07-03  
Modo: solo lectura / revisión editorial y técnica  
Cambios Shopify: ninguno  
Estado final: `VERIFICADO PERO MEJORABLE`

## 1. Alcance

Revisión de los borradores `012D` para las páginas país:

- España: `papel-pintado-espana`
- Francia: `papel-pintado-francia`, con versión pública localizada FR en `/fr/pages/papier-peint-en-france`

El objetivo era validar si los borradores estaban listos para una futura propuesta de escritura. No se ha escrito en Shopify, no se han cambiado páginas, handles, traducciones, redirects, sitemap, robots, schema ni tema.

## 2. Documentos leídos

- `AGENTS.md`
- `plan-operativo-vigente-y-cola-lotes-seo-geo-2026-06-30.md`
- `cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`
- `handoff-chatgpt-MW-GEO-LANDINGS-CONTENT-DRAFTS-012D-2026-07-02.md`
- `matriz-MW-GEO-LANDINGS-CONTENT-DRAFTS-012D-2026-07-02.csv`

## 3. Estado real comprobado en Shopify Admin

Consulta Shopify Admin GraphQL validada y ejecutada en solo lectura.

### España

- ID: `gid://shopify/Page/687276622200`
- Handle base: `papel-pintado-espana`
- Título: `Papel Pintado España`
- Publicada: sí
- Última actualización: `2024-11-06T19:45:27Z`
- Metafields leídos: 0
- Body actual: listado antiguo de envíos gratis a provincias.

### Francia

- ID: `gid://shopify/Page/687276654968`
- Handle base: `papel-pintado-francia`
- Título: `Papel Pintado Francia`
- Publicada: sí
- Última actualización: `2024-11-06T19:47:59Z`
- Metafields leídos: 0
- Body actual: listado antiguo de envíos gratis a ciudades de Francia.

## 4. Estado público comprobado

| URL | Estado | Canonical | H1 | Resultado |
|---|---:|---|---|---|
| `https://www.matchwalls.com/pages/papel-pintado-espana` | 200 | propio | `Papel Pintado España` | `VERIFICADO PERO MEJORABLE` |
| `https://www.matchwalls.com/pages/papel-pintado-francia` | 200 | propio | `Papel Pintado Francia` | `VERIFICADO PERO MEJORABLE` |
| `https://www.matchwalls.com/fr/pages/papel-pintado-francia` | 200 | `/fr/pages/papier-peint-en-france` | `Papier peint France` | `VERIFICADO PERO MEJORABLE` |
| `https://www.matchwalls.com/fr/pages/papier-peint-france` | 404 | no aplica | no aplica | `INCORRECTO` |

La URL francesa correcta ya existente es:

`https://www.matchwalls.com/fr/pages/papier-peint-en-france`

El handle `papier-peint-france` propuesto en 012D no existe públicamente y no debe usarse como destino sin lote formal de handle/redirect.

## 5. Revisión editorial de los borradores 012D

Los borradores son una mejora clara frente al contenido actual porque:

- abandonan el formato de listado de envíos;
- añaden propuesta de valor;
- cubren B2C y B2B;
- incluyen materiales, muestras, personalización, ciudades y FAQ;
- evitan promesas fuertes sobre plazos, devoluciones o aduanas.

Pero no están listos para publicar porque:

1. El handle FR propuesto `papier-peint-france` es `INCORRECTO` públicamente.
2. Alicante aparece como geo protegida en 012B/012D, pero la URL pública está en `noindex,nofollow`.
3. Las traducciones actuales EN/DE/NL de estas páginas son antiguas y contienen errores automáticos.
4. El copy francés debe pasar revisión humana/nativa.
5. Faltan enlaces internos finales exactos por idioma.
6. El sitemap no pudo revalidarse en esta ronda por timeout local; debe comprobarse antes de cualquier escritura.

## 6. Enlaces internos auditados

Enlaces base verificados como 200, canonical propio y sin noindex:

- `/pages/muestras`
- `/pages/profesionales`
- `/pages/crea-tu-mural`
- `/pages/crea-tu-papel-pintado-rollo`
- `/collections/murales`
- `/collections/murales-estilo-botanico`
- `/collections/murales-estilo-geometrico`
- `/collections/murales-estilo-floral`
- `/collections/kids-murales`
- `/collections/murales-para-el-dormitorio`
- `/collections/murales-para-el-salon`
- `/collections/murales-para-la-cocina`
- `/pages/medidas-paredes`
- `/pages/estudios-profesionales`

Geos ES estratégicas verificadas como 200, canonical propio y sin noindex:

- Barcelona
- Madrid
- Valencia
- Málaga
- Sevilla
- Girona
- Tarragona
- Bizkaia
- Gipuzkoa
- Granada
- Murcia
- Zaragoza

Alicante no debe tratarse como enlace estratégico hasta decisión humana:

- `https://www.matchwalls.com/collections/comprar-papel-pintado-alicante`
- Estado público: 200 con `robots: noindex,nofollow`

Geos FR estratégicas base verificadas como 200, canonical propio y sin noindex:

- Paris
- Lyon
- Toulouse
- Marsella
- Burdeos
- Nantes
- Lille
- Niza
- Montpellier
- Estrasburgo

## 7. Traducciones

Shopify Admin confirma traducciones publicadas para FR/EN/DE/NL/IT en estas páginas. No se revisa IT como prioridad activa.

Problema detectado:

- Las traducciones EN/DE/NL mantienen el contenido antiguo de envíos.
- Hay traducciones automáticas deficientes de ciudades y términos, por ejemplo `Basin`, `Hübsch`, `Leuk`, entre otras.

Conclusión: no conviene publicar una nueva versión solo en ES/FR sin plan posterior de coherencia en ES/EN/FR/DE/NL usando Shopify Translate/LangShop.

## 8. Decisión recomendada

No recomiendo pasar todavía a escritura Shopify.

Siguiente lote seguro:

`MW-GEO-LANDINGS-SPAIN-FRANCE-COPY-FINAL-QA-012F`

Tipo:

- editorial/técnico;
- sin escritura Shopify;
- preparar copy final España + Francia;
- decidir Alicante;
- fijar enlaces internos exactos;
- preparar versión y estrategia de traducción ES/EN/FR/DE/NL;
- dejar listo el futuro lote de escritura con backup/diff/rollback.

El lote de escritura futuro, si procede después, debería ser separado, por ejemplo:

`MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012G`

No debe ejecutarse sin propuesta formal y aprobación exacta:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012G`

## 9. Evidencias generadas

- `admin-read-MW-GEO-LANDINGS-CONTENT-REVIEW-012E-2026-07-03.csv`
- `qa-publico-MW-GEO-LANDINGS-CONTENT-REVIEW-012E-2026-07-03.csv`
- `matriz-MW-GEO-LANDINGS-CONTENT-REVIEW-012E-2026-07-03.csv`

