# Diagnostico - MW-GEO-LANDINGS-SPAIN-FRANCE-LINKS-HREFLANG-SCHEMA-QA-012L

Fecha: 2026-07-04  
Tipo: QA publico + lectura Admin.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Cambios tema: no.  
Estado global: `VERIFICADO PERO MEJORABLE`

## 1. Alcance

Se revisaron las landings pais de Espana y Francia en los cinco idiomas prioritarios:

- ES
- EN
- FR
- DE
- NL

Recursos Shopify:

- Espana: `gid://shopify/Page/687276622200` - `papel-pintado-espana`
- Francia: `gid://shopify/Page/687276654968` - `papel-pintado-francia`

URLs publicas auditadas:

- `https://www.matchwalls.com/pages/papel-pintado-espana`
- `https://www.matchwalls.com/en/pages/spain-wallpaper`
- `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`
- `https://www.matchwalls.com/de/pages/spanien-tapete`
- `https://www.matchwalls.com/nl/pages/spanje-behang`
- `https://www.matchwalls.com/pages/papel-pintado-francia`
- `https://www.matchwalls.com/en/pages/french-wallpaper`
- `https://www.matchwalls.com/fr/pages/papier-peint-en-france`
- `https://www.matchwalls.com/de/pages/franzosische-tapete`
- `https://www.matchwalls.com/nl/pages/frans-behang`

## 2. Documentos leidos

- `diagnostico-MW-GEO-LANDINGS-SPAIN-FRANCE-NEXT-QUEUE-012K-2026-07-04.md`
- `qa-publico-MW-GEO-LANDINGS-SPAIN-FRANCE-NEXT-QUEUE-012K-2026-07-04.csv`
- `matriz-MW-GEO-LANDINGS-SPAIN-FRANCE-NEXT-QUEUE-012K-2026-07-04.csv`
- `registro-cambios-ejecutados.md`

## 3. Estado real comprobado en Shopify Admin

Consulta Shopify Admin GraphQL validada contra esquema y ejecutada en solo lectura.

Resultado:

- Las dos paginas siguen publicadas.
- `global.title_tag`: `null`.
- `global.description_tag`: `null`.
- Traducciones FR/EN/DE/NL de `title`, `body_html` y `handle`: presentes y `outdated=false`.
- No se detecta cambio de estado respecto a 012K.

Estado: `VERIFICADO Y CORRECTO`.

## 4. Canonical, indexabilidad y contenido visible

Resultado publico sobre las 10 URLs:

- 10/10 HTTP 200.
- 10/10 canonical exacto a la URL solicitada.
- 10/10 sin `noindex`.
- 10/10 con H1 visible en idioma correcto.
- 10/10 sin valor obsoleto 012J3.
- Meta descriptions presentes, pero autogeneradas y largas: 319-320 caracteres.

Estado canonical/indexabilidad basica: `VERIFICADO Y CORRECTO`.  
Estado meta descriptions: `VERIFICADO PERO MEJORABLE`.

## 5. Hreflang

En las URLs revisadas se detectan alternates para:

- `x-default`
- `es`
- `en`
- `fr`
- `de`
- `nl`
- `it`
- `pt`

Para los cinco idiomas prioritarios:

- Espana: ES/EN/FR/DE/NL apuntan a las URLs esperadas.
- Francia: ES/EN/FR/DE/NL apuntan a las URLs esperadas.
- La comprobacion de reciprocidad dentro del set prioritario no encontro errores.
- `x-default` apunta a la version ES de cada pagina pais.

Estado ES/EN/FR/DE/NL: `VERIFICADO Y CORRECTO`.

Limitacion:

- IT y PT aparecen en hreflang publico, pero no se auditaron editorialmente en este lote porque quedan fuera del alcance prioritario. Estado IT/PT: `STANDBY`.

## 6. Enlaces internos / CTAs editoriales

Se comprobaron los 4 CTAs editoriales principales por idioma:

- Colecciones / ver papeles pintados.
- Muestras.
- Crear mural personalizado.
- Profesionales.

Resultado:

- Los CTAs esperados estan presentes en las 10 landings.
- Los 20 destinos unicos por idioma devuelven HTTP 200.
- Los 20 destinos tienen canonical.
- Los 20 destinos revisados no contienen `noindex`.

Estado: `VERIFICADO Y CORRECTO`.

Observacion:

- La auditoria bruta detecto tambien enlaces de menu/header con esos mismos destinos. Para el criterio de 012L se aislaron los CTAs editoriales esperados del contenido pais.

## 7. Schema / JSON-LD

Resultado:

- 10/10 URLs contienen JSON-LD valido.
- 10/10 URLs tienen 1 bloque JSON-LD valido.
- 0 errores de parseo JSON-LD.
- Tipos detectados:
  - `BreadcrumbList`
  - `ListItem`

Estado tecnico: `VERIFICADO Y CORRECTO` porque el JSON-LD existente es valido.

Estado estrategico SEO/GEO/AGEO: `VERIFICADO PERO MEJORABLE` porque las landings pais no exponen schema especifico de pagina factual/citable, por ejemplo:

- `WebPage`
- `FAQPage`
- `Organization` enlazada cuando aplique
- `BreadcrumbList` ya existe
- posible `Service`/`Article` solo si queda alineado con contenido visible y sin claims no demostrados

No se recomienda insertar schema todavia sin localizar primero la fuente actual y evitar duplicados.

## 8. Riesgos detectados

| Riesgo | Estado | Motivo |
| --- | --- | --- |
| Rotura canonical | `VERIFICADO Y CORRECTO` | 10/10 canonical exactos. |
| Rotura hreflang prioritario | `VERIFICADO Y CORRECTO` | ES/EN/FR/DE/NL apuntan a URLs esperadas. |
| CTAs editoriales rotos | `VERIFICADO Y CORRECTO` | Destinos 200, canonical y sin noindex. |
| Schema insuficiente para GEO/AGEO | `VERIFICADO PERO MEJORABLE` | Solo BreadcrumbList/ListItem; falta capa factual de pagina/FAQ. |
| IT/PT en hreflang no auditados | `STANDBY` | Detectados publicamente, fuera de prioridad por instruccion vigente. |
| Meta descriptions largas/autogeneradas | `STANDBY` | No tocar por incidencia 012J hasta ruta segura. |

## 9. Decision

No hay correccion critica inmediata en canonical, hreflang o enlaces internos de las landings pais Espana/Francia.

El siguiente avance quirurgico debe ser schema/factualidad, no metas ni handles.

## 10. Siguiente lote seguro recomendado

`MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-SOURCE-PROPOSAL-012L1`

Tipo: solo lectura/propuesta.  
Objetivo:

1. Localizar la fuente real del `BreadcrumbList` actual.
2. Comprobar si el tema ya genera Organization/WebSite/WebPage en otro punto.
3. Preparar una propuesta exacta de schema adicional para las 10 URLs pais, sin duplicados.
4. Definir si la futura implementacion debe hacerse en tema, plantilla, metafield, body HTML o app.
5. No ejecutar ningun cambio hasta aprobacion exacta.

No se recomienda pasar directamente a escritura de schema sin este paso, porque duplicar JSON-LD puede empeorar la calidad semantica.

