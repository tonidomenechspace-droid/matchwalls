# Prototipo - MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-LIQUID-PROTOTYPE-012L2

Fecha: 2026-07-04  
Tipo: prototipo local Liquid/schema.  
Aprobacion recibida: `APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-LIQUID-PROTOTYPE-012L2`  
Cambios Shopify: no.  
Cambios LangShop: no.  
Cambios tema MAIN: no.  
Estado final: `VERIFICADO Y CORRECTO` como prototipo local; `REQUIERE DECISION HUMANA` para cualquier escritura posterior.

## 1. Alcance ejecutado

Se creo un prototipo local de snippet Liquid para anadir una capa JSON-LD especifica a las landings pais Espana/Francia.

Archivo prototipo:

- `prototypes/MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-LIQUID-PROTOTYPE-012L2/snippets/geo-landing-schema.liquid`

No se escribio en Shopify.  
No se escribio en LangShop.  
No se edito `snippets/microdata-schema.liquid` real.  
No se toco tema MAIN ni tema no publicado.

## 2. Documentos y fuentes usados

Documentos internos:

- `diagnostico-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-SOURCE-PROPOSAL-012L1-2026-07-04.md`.
- `diagnostico-MW-GEO-LANDINGS-SPAIN-FRANCE-LINKS-HREFLANG-SCHEMA-QA-012L-2026-07-04.md`.
- `copy-map-final-MW-GEO-LANDINGS-I18N-LINGUISTIC-QA-012G2-2026-07-03.md`.
- `propuesta-lote-MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F-2026-07-03.md`.
- `auditoria-schema.md`.
- `registro-cambios-ejecutados.md`.

Busqueda tecnica Shopify Liquid:

- `canonical_url`: objeto global disponible.
- `page`: propiedades disponibles `id`, `handle`, `title`, `content`, `url`, `template_suffix`.

## 3. Arquitectura del prototipo

El snippet propuesto:

- Solo se activa si `request.page_type == 'page'`.
- Solo se activa para estos IDs:
  - Espana: `687276622200`.
  - Francia: `687276654968`.
- Solo se activa para idiomas prioritarios:
  - `es`
  - `en`
  - `fr`
  - `de`
  - `nl`
- No se activa para IT/PT aunque existan hreflang publicos.
- No sustituye el `BreadcrumbList` actual.
- No anade `Product`, `Offer`, `AggregateRating`, `Review`, `LocalBusiness`, `Article` ni `Service`.

Tipos JSON-LD propuestos:

- `WebPage`
- `FAQPage`
- Referencia interna a `WebSite`
- Referencia interna a `Organization`
- `Country` como `about`

## 4. Metodo de identificacion

Se usa `page.id`, no handles traducidos.

Motivo:

- Los handles estan localizados por idioma.
- `page.id` identifica el recurso Shopify real y reduce riesgo de que una ruta traducida rompa la condicion.

Estado: `VERIFICADO Y CORRECTO`.

## 5. Idiomas y contenido

Las preguntas/respuestas FAQ se han mapeado por idioma y pais a partir del contenido aprobado en 012F/012G/012H.

Puntos de control:

- ES Espana y ES Francia tienen respuestas diferenciadas donde el contenido visible tambien difiere.
- EN/FR/DE/NL Espana y Francia conservan sus diferencias de copy cuando existen.
- FR usa signos y espacios tipograficos visibles en el copy aprobado.
- DE/NL usan terminologia ya validada en 012G2.

Estado: `VERIFICADO Y CORRECTO` como prototipo.

## 6. Validaciones ejecutadas

### 6.1 Busqueda Shopify Liquid previa

Ejecutada antes de generar codigo:

- `JSON-LD structured data Liquid snippet`: sin resultados utiles.
- `Liquid page object canonical_url localization`: confirma `canonical_url`.
- `Liquid page object id handle title content`: confirma propiedades de `page`.

### 6.2 Validacion oficial Liquid

Validador usado:

- `scripts/validate.mjs`
- Artifact ID: `mw-012l2-geo-schema`
- Revision final: `2`

Resultado:

- `geo-landing-schema.liquid passed all checks`
- Estado: `VERIFICADO Y CORRECTO`

Nota tecnica:

- El validador oficial requeria dependencias locales ausentes. Se restauraron en el paquete local de la skill Shopify Liquid mediante `pnpm install --ignore-scripts`. Esto no modifica Shopify ni el proyecto web.

### 6.3 Validacion JSON-LD de muestras

Se simularon las 10 combinaciones previstas:

- Espana ES/EN/FR/DE/NL.
- Francia ES/EN/FR/DE/NL.

Resultado:

- 10/10 muestras JSON parsean correctamente.
- 10/10 contienen `WebPage`.
- 10/10 contienen `FAQPage`.
- 10/10 contienen 3 preguntas FAQ.

Estado: `VERIFICADO Y CORRECTO`.

## 7. Insercion futura propuesta

Si se aprueba implementacion en tema, la ruta recomendada seria:

1. Subir el snippet nuevo `snippets/geo-landing-schema.liquid` a un tema duplicado/no publicado.
2. Insertar una sola llamada en `snippets/microdata-schema.liquid`.
3. Ubicacion propuesta: despues del bloque actual de `BreadcrumbList` y antes del bloque `request.page_type == 'index'`.
4. Render propuesto:

```liquid
{%- render 'geo-landing-schema' -%}
```

No insertar en `body_html` de las paginas.

Motivo:

- Mantiene el schema centralizado.
- Evita depender de LangShop para JSON-LD.
- Evita mezclar contenido editorial con marcado tecnico.
- Permite revertir con una linea y un snippet.

## 8. Riesgos que siguen vivos

| Riesgo | Estado | Control |
| --- | --- | --- |
| Escribir accidentalmente en MAIN | `RIESGO CRITICO` | Siguiente lote debe verificar tema destino antes de escribir. |
| Duplicar o romper `BreadcrumbList` | `RIESGO CRITICO` | El prototipo no toca BreadcrumbList. |
| Exponer IT/PT con schema en idioma incorrecto | `CORREGIDO Y VERIFICADO` | El prototipo bloquea idiomas fuera de ES/EN/FR/DE/NL. |
| Divergencia futura entre FAQ visible y FAQ schema | `VERIFICADO PERO MEJORABLE` | Requiere QA publico tras implementacion. |
| Organization sin `@id` global estable | `VERIFICADO PERO MEJORABLE` | El prototipo usa objeto minimo; la entidad global queda para auditoria schema 013C/013D. |
| Prometer rich results o citas IA | `REQUIERE DECISION HUMANA` | No se promete; el objetivo es comprension/elegibilidad. |

## 9. Reversion futura si se implementa

Metodo de reversion recomendado en tema no publicado:

1. Eliminar la llamada `{%- render 'geo-landing-schema' -%}` de `snippets/microdata-schema.liquid`.
2. Eliminar o dejar inactivo `snippets/geo-landing-schema.liquid`.
3. Verificar que las landings vuelven a tener solo el JSON-LD previo (`BreadcrumbList`).

Si Shopify bloquea borrado de archivo, basta con retirar la llamada render para desactivar la capa.

## 10. Siguiente lote seguro recomendado

`MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-DRAFT-THEME-TARGET-DIAG-012L3`

Tipo: diagnostico de destino de implementacion.

Objetivo:

1. Identificar el tema no publicado correcto para probar.
2. Confirmar que no es MAIN.
3. Comparar `snippets/microdata-schema.liquid` del tema destino con el prototipo esperado.
4. Preparar propuesta exacta de escritura para un tema no publicado.
5. No ejecutar escritura hasta aprobacion exacta.

No recomiendo saltar directamente a escritura sin este lote, porque el mayor riesgo ya no es el codigo: es escribir en el tema equivocado.

