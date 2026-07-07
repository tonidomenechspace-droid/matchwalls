# Diagnostico tecnico - MW-THEME-PAGE-H1-SEMANTIC-008E

Fecha: 2026-06-17 22:12:59 +02:00

Estado global del bloque: INCOMPLETO

Este documento registra comprobaciones de solo lectura sobre el tema MAIN publicado de Shopify. No se han ejecutado mutaciones, imports de LangShop, cambios de tema, publicaciones ni operaciones masivas.

## Documentos leidos

- `AGENTS.md`
- `auditoria-seo-geo-matchwalls/registro-cambios-ejecutados.md`
- `auditoria-seo-geo-matchwalls/diagnostico-lote-MW-INDEXABILITY-TECH-008-2026-06-17.md`
- `auditoria-seo-geo-matchwalls/propuesta-lote-MW-INDEXABILITY-TECH-008-2026-06-17.md`

## Estado real comprobado

### Tema MAIN

Estado: VERIFICADO Y CORRECTO

- ID: `gid://shopify/OnlineStoreTheme/178383749496`
- Nombre: `SEO schema hotfix - 2026-06-15`
- Rol: `MAIN`

### Seccion base de pagina

Estado: VERIFICADO Y CORRECTO

Archivo MAIN:

- `sections/main-page.liquid`
- Checksum: `8330fa7d1cd5ce4929978d2599b2062c`

Contenido relevante verificado:

- Renderiza `<h1 class="h1 text-center">{{ page.title }}</h1>`.
- Renderiza `{{ page.content }}` cuando `page.content` no esta vacio.

Interpretacion:

- La seccion base `main-page` no es el problema por si misma.
- El problema aparece cuando la plantilla de pagina desactiva esa seccion o no la usa de forma visible.

## Hallazgos verificados

### 1. `templates/page.muestras.json`

Estado: INCORRECTO

Archivo MAIN:

- `templates/page.muestras.json`
- Checksum: `e728dd0047cd35df8ab75fed73f90f96`

Evidencia:

- La seccion `main` de tipo `main-page` existe, pero esta marcada con `"disabled": true`.

Riesgo:

- Cualquier pagina asignada a esta plantilla puede quedar sin H1 y sin contenido principal de `page.content`.

### 2. `templates/page.muestras-2.json`

Estado: INCORRECTO

Archivo MAIN:

- `templates/page.muestras-2.json`
- Checksum: `cde44149a1373f45969718e32ba05772`

Pagina Shopify relacionada:

- ID: `gid://shopify/Page/106299195619`
- Titulo: `Solicita muestras de papel pintado`
- Handle base: `muestras`
- Estado: publicada
- Template suffix: `muestras-2`
- Body summary: existe contenido editorial en la pagina.

Evidencia de plantilla:

- La seccion `main` de tipo `main-page` esta marcada con `"disabled": true`.
- En el orden de secciones, `main` aparece despues de la primera seccion custom.
- Las primeras secciones usan titulos internos como `Acerca de nuestras muestras Matchwalls` con `heading_tag` de nivel inferior (`h4`) o encabezados vacios.

Evidencia publica previa:

- `https://www.matchwalls.com/en/pages/request-your-sample` respondio 200, canonical self y H1 count 0.

Interpretacion:

- La pagina puede tener contenido optimizado en Shopify y traducciones en LangShop, pero la plantilla publicada impide que el titulo/contenido principal de pagina se renderice como H1/contenido semantico.

### 3. `templates/page.sobre-nosotros.json`

Estado: INCORRECTO

Archivo MAIN:

- `templates/page.sobre-nosotros.json`
- Checksum: `5841ae151f305c4de246e2044ffa2ed0`

Pagina Shopify relacionada:

- ID: `gid://shopify/Page/106231464163`
- Titulo: `Sobre Nosotros — MatchWalls, expertos en papel pintado mural`
- Handle base: `sobre-nosotros`
- Estado: publicada
- Template suffix: `sobre-nosotros`
- Body summary: existe contenido editorial en la pagina.

Evidencia de plantilla:

- La seccion `main` de tipo `main-page` esta marcada con `"disabled": true`.
- El hero visible usa el titulo `SOBRE NOSOTROS  #BeMatchWalls`, pero su `heading_tag` esta configurado como `h2`.

Evidencia publica previa:

- `https://www.matchwalls.com/fr/pages/a-propos-de-nous` respondio 200, canonical self y H1 count 0.
- `https://www.matchwalls.com/nl/pages/over-ons` respondio 200, canonical self y H1 count 0.

Interpretacion:

- La pagina se ve visualmente construida con secciones custom, pero no entrega un H1 claro a buscadores y sistemas IA.

### 4. `templates/page.faq.json`

Estado: VERIFICADO Y CORRECTO

Archivo MAIN:

- `templates/page.faq.json`
- Checksum: `d515fbda6fcc75f79d06cdba2d7cc0dd`

Evidencia:

- La seccion `main` de tipo `main-page` esta activa.
- La comprobacion publica previa de `/en/pages/frequent-questions` encontro H1: `Wallpaper and wall mural FAQs`.

## Relacion con LangShop

Estado: VERIFICADO PERO MEJORABLE

Este fallo no se soluciona solo editando traducciones en LangShop. LangShop puede tener textos/traducciones guardados, pero si la plantilla Shopify desactiva `main-page`, el titulo y el contenido principal de la pagina no se renderizan como HTML semantico.

Implicacion:

- Primero hay que reparar la plantilla/HTML.
- Despues hay que verificar que LangShop publica correctamente ES/EN/FR/DE/NL para los textos visibles.

## Acciones no realizadas

- No se modifico Shopify.
- No se modifico LangShop.
- No se importaron CSV.
- No se ejecutaron mutaciones.
- No se modifico el tema MAIN.
- No se publicaron temas.
- No se cambiaron handles, URLs, redirecciones, productos, colecciones ni inventario.

## Estado final

Estado: INCOMPLETO

La causa tecnica de al menos parte de las paginas sin H1 esta verificada: plantillas publicadas con `main-page` desactivado o encabezados hero configurados como H2/H4.

El siguiente paso debe ser un lote acotado de tema, preparado primero en tema auxiliar/unpublished y verificado en preview antes de tocar produccion.
