# Diagnostico MW-TECH-HOME-CRAWLABLE-CSS-010D

Fecha: 2026-06-25  
Tipo: diagnostico de solo lectura  
Estado: `INCORRECTO`  

## Documentos leidos

- `AGENTS.md`
- `auditoria-seo-geo-matchwalls/registro-cambios-ejecutados.md`
- `auditoria-seo-geo-matchwalls/cola-maestra-lotes-publicacion-seo-geo-2026-06-18.csv`
- `auditoria-seo-geo-matchwalls/lista-maestra-errores-cambios-evoluciones-mejoras.md`
- `auditoria-seo-geo-matchwalls/auditoria-seo-tecnico.csv`
- `auditoria-seo-geo-matchwalls/estado-real-cobertura-seo-geo-2026-06-15.md`
- `auditoria-seo-geo-matchwalls/plan-publicacion-por-oleadas-seo-geo-2026-06-18.md`
- `auditoria-seo-geo-matchwalls/programa-ejecucion-seo-geo.md`

## Estado real comprobado en Shopify

Consulta de lectura GraphQL validada contra Admin API.

| Rol | Theme ID | Nombre | Archivo | MD5 | Estado |
| --- | --- | --- | --- | --- | --- |
| MAIN | `178396463480` | `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...` | `sections/collection-logo-list.liquid` | `44d02156951a46f0147f3ee3de61f38e` | `INCORRECTO` |
| QA auxiliar | `178399019384` | `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18` | `sections/collection-logo-list.liquid` | `44d02156951a46f0147f3ee3de61f38e` | `INCORRECTO` |
| Reversion | `178383749496` | `SEO schema hotfix - 2026-06-15` | `sections/collection-logo-list.liquid` | `44d02156951a46f0147f3ee3de61f38e` | `INCORRECTO` |

Conclusion: el problema esta heredado en los tres temas comparados. No procede atribuirlo a 010C2 ni a los ultimos sublotes.

## Evidencia tecnica

La home usa `templates/index.json` con la seccion activa:

- `collection_logo_list_qwGRVf`
- tipo: `collection-logo-list`
- bloques activos: 8 categorias visibles

El archivo `sections/collection-logo-list.liquid` imprime un bloque `<style>` dentro del bucle `{% for block in section.blocks %}` y dentro de cada enlace `.logo-link`.

Como la seccion activa tiene 8 bloques, la home renderiza 8 bloques CSS duplicados dentro de enlaces de categoria.

CSS afectado:

- `.logo-link`
- `.logo-list__image`
- `a:hover .logo-list__image`
- `a:hover .logo-text`

## Verificacion en navegador

URLs verificadas:

- MAIN: `https://www.matchwalls.com/`
- Preview auxiliar: `https://www.matchwalls.com/?preview_theme_id=178399019384`

Resultado:

| Medida | MAIN | QA auxiliar |
| --- | ---: | ---: |
| Enlaces `.logo-link` visibles en home | 8 | 8 |
| `<style>` problematicos dentro de `.logo-link` | 8 | 8 |
| CSS `.logo-link/.logo-list__image` en `body.innerText` | No | No |
| CSS `.logo-link/.logo-list__image` en `body.textContent` | Si | Si |
| CSS `.logo-link/.logo-list__image` en HTML bruto | Si | Si |

Interpretacion: el CSS no aparece como texto visible para el usuario, pero si queda dentro del HTML/textContent de la home y puede contaminar extracciones simples de texto usadas por rastreadores, auditores o sistemas IA.

## Enlaces de categoria conservados en el bloque afectado

- `Paisajes` -> `/collections/murales-estilo-paisajes`
- `Artistico` -> `/collections/murales-estilo-artistico`
- `Botanico` -> `/collections/murales-estilo-botanico`
- `Floral` -> `/collections/murales-estilo-floral`
- `Geometricos` -> `/collections/murales-estilo-geometrico`
- `Infantiles` -> `/collections/kids-murales`
- `Graficos` -> `/collections/murales-estilo-grafico`
- `Patrones` -> `/collections/papel-pintado-estampados-pequenos`

## Riesgos detectados

- Riesgo SEO/GEO: contaminacion del texto extraido de la home con reglas CSS no editoriales.
- Riesgo tecnico: CSS duplicado e incrustado dentro de enlaces.
- Riesgo de cambio: bajo/medio si se limita al tema auxiliar y se mantiene el mismo comportamiento visual.
- Riesgo visual a validar: tamanos de logos, grid movil y efecto hover.

## Nota secundaria

El mismo archivo contiene tambien un bloque `<style>` posterior con el selector `div[{{ block.shopify_attributes }}]` fuera del bucle del bloque. Este selector queda fuera de contexto y debe considerarse deuda tecnica secundaria. No se propone mezclarlo con cambios fuera del alcance sin aprobacion expresa.

## Acciones ejecutadas

- Solo lectura de documentos.
- Solo lectura GraphQL de temas y archivo afectado.
- Inspeccion de MAIN y preview auxiliar en navegador.

No se modifico Shopify.
