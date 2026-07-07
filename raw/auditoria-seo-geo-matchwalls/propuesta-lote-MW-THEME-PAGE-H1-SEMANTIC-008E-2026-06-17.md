# Propuesta de lote - MW-THEME-PAGE-H1-SEMANTIC-008E

Estado: REQUIERE DECISION HUMANA

## Objetivo

Reparar paginas publicadas que actualmente pueden entregar HTML sin H1 claro, aunque tengan contenido y traducciones guardadas en Shopify/LangShop.

Este lote busca mejorar comprension SEO/GEO basica: titulo principal visible, contenido principal renderizado, jerarquia semantica y consistencia ES/EN/FR/DE/NL.

No garantiza rankings, trafico ni citas de sistemas IA.

## Alcance exacto propuesto

Tema MAIN actual solo como fuente de lectura:

- ID: `gid://shopify/OnlineStoreTheme/178383749496`
- Nombre: `SEO schema hotfix - 2026-06-15`
- Rol: `MAIN`

Archivos afectados propuestos:

- `templates/page.muestras-2.json`
- `templates/page.sobre-nosotros.json`
- Opcional tras verificacion: `templates/page.muestras.json`, solo si hay paginas publicadas asignadas o riesgo real.

Paginas prioritarias:

- `gid://shopify/Page/106299195619`
  - Base ES: `/pages/muestras`
  - Publica EN observada: `/en/pages/request-your-sample`
  - Template: `muestras-2`
- `gid://shopify/Page/106231464163`
  - Base ES: `/pages/sobre-nosotros`
  - Publicas observadas: `/fr/pages/a-propos-de-nous`, `/nl/pages/over-ons`
  - Template: `sobre-nosotros`

## Valores actuales verificados

### `templates/page.muestras-2.json`

- `main` tipo `main-page`: `"disabled": true`
- Pagina `muestras`: publicada, con body summary no vacio.
- Publico EN observado: H1 count 0.

### `templates/page.sobre-nosotros.json`

- `main` tipo `main-page`: `"disabled": true`
- Primer hero: titulo `SOBRE NOSOTROS  #BeMatchWalls`
- Primer hero: `heading_tag`: `h2`
- Paginas FR/NL observadas: H1 count 0.

## Valores propuestos

### Propuesta para `page.sobre-nosotros.json`

Opcion tecnica recomendada:

- Mantener `main-page` desactivado para no duplicar el cuerpo visual.
- Cambiar el primer hero principal de `heading_tag: h2` a `heading_tag: h1`.
- Verificar que solo exista un H1 por idioma en publico.

Motivo:

- Es menos invasivo que activar `main-page`.
- Aprovecha el hero ya visible.
- Reduce riesgo visual.

### Propuesta para `page.muestras-2.json`

Opcion tecnica recomendada para preview:

- Activar `main-page` en un tema auxiliar.
- Mover `main` al inicio del `order`, antes de secciones custom.
- Verificar si `page.content` duplica contenido o mejora la pagina.

Si la preview genera duplicacion visual:

- Alternativa: crear un bloque/section de encabezado semantico controlado para usar `page.title` como H1 sin duplicar el cuerpo.

Motivo:

- La pagina tiene titulo y contenido de pagina en Shopify.
- La plantilla actual lo oculta semanticamente.
- Cambiar solo un `heading_tag` H4 a H1 podria dejar un H1 menos preciso y dependiente de texto hardcoded de seccion.

## Riesgos

- Activar `main-page` puede alterar el layout o duplicar texto.
- Cambiar `heading_tag` puede afectar tamano visual si el CSS diferencia H1/H2.
- LangShop puede tener traducciones de secciones distintas a traducciones de pagina; hay que verificar ambos.
- No debe editarse MAIN directamente.

## Respaldo disponible

Valores originales verificados:

- `templates/page.muestras-2.json`
  - Checksum: `cde44149a1373f45969718e32ba05772`
  - `main.disabled`: `true`
- `templates/page.sobre-nosotros.json`
  - Checksum: `5841ae151f305c4de246e2044ffa2ed0`
  - `main.disabled`: `true`
  - Hero principal `heading_tag`: `h2`

Antes de ejecutar:

- Copiar archivos afectados a respaldo local.
- Trabajar primero sobre tema auxiliar/unpublished.
- No publicar hasta QA.

## Metodo de reversion

- Restaurar los JSON originales en el tema auxiliar si falla la preview.
- Si se publica posteriormente y falla QA critica, volver a publicar el tema MAIN anterior o restaurar los archivos originales, segun el metodo aprobado en ese lote.

## Pruebas posteriores obligatorias

En preview:

- ES/EN/FR/DE/NL.
- Desktop y mobile.
- URLs:
  - `/pages/muestras`
  - `/en/pages/request-your-sample`
  - `/fr/pages/a-propos-de-nous`
  - `/nl/pages/over-ons`
  - `/de/pages/...` equivalente de sobre nosotros y muestras si existe.

Comprobar:

- Status 200.
- Un unico H1.
- H1 correcto y localizado.
- Contenido visible no duplicado.
- Canonical self correcto.
- Hreflang coherente.
- No hay `noindex` accidental.
- No hay regresion visual.
- LangShop muestra/publica traducciones coherentes de los textos visibles.

## Autorizacion necesaria

Para preparar el hotfix en tema auxiliar/unpublished:

`APROBADO LOTE MW-THEME-PAGE-H1-SEMANTIC-008E`

Esa aprobacion no debe interpretarse como autorizacion para publicar el tema. Publicar el tema requeriria un lote posterior y aprobacion especifica.
