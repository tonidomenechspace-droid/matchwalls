# Diagnostico - MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-DRAFT-THEME-TARGET-DIAG-012L3

Fecha: 2026-07-04  
Tipo: diagnostico de destino de tema para implementacion futura.  
Aprobacion recibida: `APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-DRAFT-THEME-TARGET-DIAG-012L3`  
Cambios Shopify: no.  
Cambios LangShop: no.  
Cambios tema/Liquid: no.  
Estado final: `VERIFICADO PERO MEJORABLE`

## 1. Alcance

Objetivo del lote:

1. Comprobar el estado real actual de temas en Shopify.
2. Confirmar cual es el MAIN real.
3. Identificar si existe un tema no publicado apto para probar el schema de 012L2.
4. Comparar archivos relevantes del candidato contra MAIN.
5. Preparar la propuesta exacta de escritura futura, sin ejecutarla.

No se ha escrito ningun archivo en Shopify.  
No se ha publicado ningun tema.  
No se ha duplicado ni eliminado ningun tema.

## 2. Documentos leidos

- `diagnostico-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-SOURCE-PROPOSAL-012L1-2026-07-04.md`.
- `prototipo-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-LIQUID-PROTOTYPE-012L2-2026-07-04.md`.
- `validacion-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-LIQUID-PROTOTYPE-012L2-2026-07-04.csv`.
- `matriz-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-LIQUID-PROTOTYPE-012L2-2026-07-04.csv`.
- `registro-cambios-ejecutados.md`.

## 3. Consultas Shopify Admin ejecutadas

Se uso Shopify Admin GraphQL en modo solo lectura.

Consultas validadas antes de ejecutar:

- `MW012L3ThemesInventory`.
- `MW012L3ThemeFilesCompare`.

Scopes indicados por el validador:

- `read_themes`.

Estado: `VERIFICADO Y CORRECTO`.

## 4. Estado real actual de temas

Resultado principal:

- Total de temas listados: 20.
- `hasNextPage`: `false`.
- MAIN actual:
  - ID: `gid://shopify/OnlineStoreTheme/178399019384`.
  - Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
  - Rol: `MAIN`.
  - Prefix: `/t/46`.
  - `updatedAt`: `2026-06-30T16:29:38Z`.
  - `processing`: `false`.
  - `processingFailed`: `false`.

Estado MAIN: `VERIFICADO Y CORRECTO`.

Observacion importante:

- Shopify muestra 20 temas. Crear un duplicado fresco de MAIN requeriria liberar espacio o eliminar un tema, lo cual no esta autorizado en este lote.

## 5. Candidatos revisados

### 5.1 Candidato recomendado para QA aislada

Tema:

- ID: `gid://shopify/OnlineStoreTheme/178396463480`.
- Nombre: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- Rol: `UNPUBLISHED`.
- Prefix: `/t/45`.
- `updatedAt`: `2026-06-26T21:36:42Z`.
- `processing`: `false`.
- `processingFailed`: `false`.

Estado: `VERIFICADO PERO MEJORABLE`.

Motivo:

- Es no publicado.
- No esta procesando ni fallido.
- Sus archivos schema relevantes coinciden con MAIN.
- Pero `config/settings_data.json` no coincide con MAIN, por lo que no debe tratarse como candidato de publicacion directa sin una regresion completa.

Uso recomendado:

- Apto para prueba aislada de schema.
- No apto todavia para publicacion.

### 5.2 Candidatos descartados para este avance

| Tema | Rol | Motivo |
| --- | --- | --- |
| `178399019384` | `MAIN` | No se debe escribir en MAIN. |
| `178383749496` | `UNPUBLISHED` | Tema de reversion/schema hotfix antiguo; archivos relevantes coinciden, pero es mas antiguo y no debe contaminarse sin necesidad. |
| `178383585656` | `UNPUBLISHED` | `snippets/microdata-schema.liquid` no coincide con MAIN; descartado para este schema. |
| Temas antiguos 2024/2025 | `UNPUBLISHED` | Obsoletos para QA actual. |

## 6. Comparacion MAIN vs candidato recomendado

MAIN: `178399019384`  
Candidato QA: `178396463480`

| Archivo | MAIN checksum | Candidato checksum | Estado |
| --- | --- | --- | --- |
| `layout/theme.liquid` | `13cf45059f0dd8095055644fafd3da8d` | `13cf45059f0dd8095055644fafd3da8d` | `VERIFICADO Y CORRECTO` |
| `snippets/microdata-schema.liquid` | `58417e4825aa3d4570a6646f292aaedc` | `58417e4825aa3d4570a6646f292aaedc` | `VERIFICADO Y CORRECTO` |
| `sections/main-page.liquid` | `8330fa7d1cd5ce4929978d2599b2062c` | `8330fa7d1cd5ce4929978d2599b2062c` | `VERIFICADO Y CORRECTO` |
| `templates/page.json` | `d8085538dc93d34f2457f8df79e37e50` | `d8085538dc93d34f2457f8df79e37e50` | `VERIFICADO Y CORRECTO` |
| `config/settings_data.json` | `d487694e14fe7558034b7d4595075de4` | `a1192f2f698d277e0f69f7156a61a90c` | `VERIFICADO PERO MEJORABLE` |
| `snippets/geo-landing-schema.liquid` | no existe en lectura | no existe en lectura | `INCOMPLETO` |

Decision:

- Para probar schema aislado, el candidato `178396463480` es aceptable.
- Para publicar, no es aceptable sin QA/regresion completa y decision posterior.

## 7. Propuesta tecnica futura calculada

Archivo nuevo propuesto:

- `snippets/geo-landing-schema.liquid`
- Origen: prototipo 012L2 validado.
- MD5 local del snippet: `9033b2bfa89dc435b9811b3d897e07c1`.
- Tamano: `11723` bytes.

Archivo existente a modificar:

- `snippets/microdata-schema.liquid`
- Checksum actual en candidato: `58417e4825aa3d4570a6646f292aaedc`.
- Checksum propuesto local tras insertar una linea render: `a3d8e23b4979219149a9c5b5f76723ec`.

Insercion propuesta:

```liquid
{%- render 'geo-landing-schema' -%}
```

Ubicacion propuesta:

- Despues del bloque actual que emite `BreadcrumbList`.
- Antes del bloque `{%- if request.page_type == 'index' -%}`.

Motivo:

- No toca `BreadcrumbList`.
- No toca el bloque `Organization/WebSite` de la home.
- Activa el nuevo schema solo si el snippet lo permite por `page.id` e idioma.

## 8. Riesgos

| Riesgo | Estado | Mitigacion |
| --- | --- | --- |
| Escribir en MAIN | `RIESGO CRITICO` | Siguiente lote debe revalidar rol `UNPUBLISHED` justo antes de escribir. |
| Tema candidato no igual a MAIN completo | `VERIFICADO PERO MEJORABLE` | Usarlo solo para QA aislada; no para publicacion. |
| Limite de 20 temas | `REQUIERE DECISION HUMANA` | No duplicar MAIN sin limpieza aprobada. |
| Borrado de snippet bloqueado por Shopify | `VERIFICADO PERO MEJORABLE` | Reversion critica es retirar el render; el snippet inerte no afecta. |
| Divergencia FAQ visible/schema | `VERIFICADO PERO MEJORABLE` | Postcheck publico en 10 URLs tras escritura. |
| Publicar sin regresion | `RIESGO CRITICO` | La implementacion futura no debe publicar. |

## 9. Decision 012L3

Se selecciona como destino recomendado para el siguiente lote de escritura aislada:

`gid://shopify/OnlineStoreTheme/178396463480`

Nombre:

`MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`

Estado:

- `UNPUBLISHED`.
- Apto para QA aislada de schema.
- No apto para publicacion directa.

## 10. Siguiente lote recomendado

`MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-DRAFT-THEME-UPSERT-012L4`

Tipo: escritura acotada en tema no publicado.

Alcance propuesto:

1. Releer el tema `178396463480` justo antes de escribir.
2. Abortarlo si el rol ya no es `UNPUBLISHED`.
3. Crear `snippets/geo-landing-schema.liquid`.
4. Modificar `snippets/microdata-schema.liquid` con una sola llamada render.
5. No publicar.
6. No tocar MAIN.
7. Hacer QA de preview sobre las 10 landings ES/EN/FR/DE/NL.

No ejecutar hasta aprobacion exacta.

