# Resultado lote MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-COPY-MAP-012N

Fecha: 2026-07-04  
Estado final: `VERIFICADO Y CORRECTO`

## Alcance

Lote de preparación y propuesta. No se ejecutó ninguna escritura.

Objetivo: preparar el mapa exacto de enlaces internos y copy por idioma para reforzar el cluster país España/Francia sin alterar handles, URLs, metadatos, FAQ, schema, productos ni navegación global.

No se modificó Shopify, LangShop, temas, menús, páginas, handles, URLs, canonicals, hreflang, metadatos, productos, precios, redirecciones ni App Embeds.

## Documentos leídos

- `resultado-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-QA-012M-2026-07-04.md`.
- `qa-internal-linking-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-QA-012M-2026-07-04.csv`.
- `registro-cambios-ejecutados.md`.

## Estado real Shopify comprobado

Tema MAIN:

- ID: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol: `MAIN`.
- `processing`: `false`.
- `processingFailed`: `false`.
- `updatedAt`: `2026-07-04T12:23:11Z`.
- `config/settings_data.json`: checksum `d487694e14fe7558034b7d4595075de4`.
- `snippets/geo-landing-schema.liquid`: checksum `9033b2bfa89dc435b9811b3d897e07c1`.
- `snippets/microdata-schema.liquid`: checksum `a3d8e23b4979219149a9c5b5f76723ec`.

Páginas base ES:

- España: `gid://shopify/Page/687276622200`, handle `papel-pintado-espana`, publicada.
- Francia: `gid://shopify/Page/687276654968`, handle `papel-pintado-francia`, publicada.

## Criterio editorial

Se propone un bloque pequeño, visible y contextual después del apartado de ciudades estratégicas y antes de preguntas frecuentes.

Motivo:

- La sección de ciudades ya establece contexto geográfico.
- La FAQ y su schema quedan intactos.
- El bloque refuerza el cluster país sin convertir la página en un listado artificial de enlaces.
- Es más seguro que tocar home, footer o menús globales en el mismo paso.

## Mapa de copy preparado

Archivo principal:

- `copy-map-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-COPY-MAP-012N-2026-07-04.csv`.

Resumen:

- España ES enlaza a Francia ES.
- España EN enlaza a Francia EN.
- España FR enlaza a Francia FR.
- España DE enlaza a Francia DE.
- España NL enlaza a Francia NL.
- Francia ES enlaza a España ES.
- Francia EN enlaza a España EN.
- Francia FR enlaza a España FR.
- Francia DE enlaza a España DE.
- Francia NL enlaza a España NL.

## Texto propuesto por idioma

### ES

Heading:

`Papel pintado por país`

España → Francia:

`Estás consultando las soluciones para España. Si tu proyecto se desarrolla en Francia o quieres comparar opciones para otro mercado, consulta la guía de papel pintado en Francia.`

Francia → España:

`Estás consultando las soluciones para Francia. Si tu proyecto se desarrolla en España o quieres comparar opciones para otro mercado, consulta la guía de papel pintado en España.`

### EN

Heading:

`Wallpaper by country`

Spain → France:

`You are viewing the solutions for Spain. If your project is in France or you want to compare options for another market, read the guide to wallpaper in France.`

France → Spain:

`You are viewing the solutions for France. If your project is in Spain or you want to compare options for another market, read the guide to wallpaper in Spain.`

### FR

Heading:

`Papier peint par pays`

Espagne → France:

`Vous consultez les solutions pour l’Espagne. Si votre projet se situe en France ou si vous souhaitez comparer les options pour un autre marché, consultez notre guide du papier peint en France.`

France → Espagne:

`Vous consultez les solutions pour la France. Si votre projet se situe en Espagne ou si vous souhaitez comparer les options pour un autre marché, consultez notre guide du papier peint en Espagne.`

### DE

Heading:

`Tapeten nach Land`

Spanien → Frankreich:

`Sie sehen die Lösungen für Spanien. Wenn Ihr Projekt in Frankreich liegt oder Sie Optionen für einen weiteren Markt vergleichen möchten, lesen Sie den Leitfaden zu Tapeten in Frankreich.`

Frankreich → Spanien:

`Sie sehen die Lösungen für Frankreich. Wenn Ihr Projekt in Spanien liegt oder Sie Optionen für einen weiteren Markt vergleichen möchten, lesen Sie den Leitfaden zu Tapeten in Spanien.`

### NL

Heading:

`Behang per land`

Spanje → Frankrijk:

`Je bekijkt de oplossingen voor Spanje. Als je project zich in Frankrijk bevindt of je opties voor een andere markt wilt vergelijken, bekijk dan de gids over behang in Frankrijk.`

Frankrijk → Spanje:

`Je bekijkt de oplossingen voor Frankrijk. Als je project zich in Spanje bevindt of je opties voor een andere markt wilt vergelijken, bekijk dan de gids over behang in Spanje.`

## Sistema de ejecución recomendado

No ejecutar aún.

Lote de escritura recomendado:

`MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O`

Alcance propuesto:

- Shopify nativo:
  - Actualizar body HTML de `gid://shopify/Page/687276622200`.
  - Actualizar body HTML de `gid://shopify/Page/687276654968`.
- LangShop:
  - Actualizar traducción body HTML EN/FR/DE/NL de ambas páginas.
- No tocar:
  - Handles.
  - URLs.
  - Titles.
  - SEO title/meta description.
  - FAQ.
  - Schema Liquid.
  - Menús.
  - Home.
  - Footer.

## Reversión propuesta para 012O

Si se ejecuta 012O, la reversión consistirá en retirar el bloque `Papel pintado por país` / `Wallpaper by country` / `Papier peint par pays` / `Tapeten nach Land` / `Behang per land` de cada body afectado, restaurando los cuerpos anteriores.

## QA posterior recomendada para 012O

- Verificar 10 URLs HTTP 200.
- Verificar canonical propio.
- Verificar noindex ausente.
- Verificar que los enlaces España ↔ Francia aparecen en HTML público por idioma.
- Verificar que FAQ sigue visible y que schema 012L6B sigue parseando.
- Verificar que no se alteraron handles ni metadatos.

## Estado final

`VERIFICADO Y CORRECTO`

El mapa está preparado. Requiere decisión humana antes de cualquier escritura en Shopify o LangShop.
