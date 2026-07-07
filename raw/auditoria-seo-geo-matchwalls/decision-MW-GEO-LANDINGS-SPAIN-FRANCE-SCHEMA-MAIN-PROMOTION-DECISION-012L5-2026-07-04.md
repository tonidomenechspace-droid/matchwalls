# Decision MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-PROMOTION-DECISION-012L5

Fecha: 2026-07-04  
Estado: `REQUIERE DECISION HUMANA`

## 1. Objetivo

Decidir la ruta segura para llevar a produccion el schema Espana-Francia validado en el tema no publicado durante 012L4.

## 2. Estado verificado

### MAIN actual

- Theme ID: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol: `MAIN`.
- `processing`: `false`.
- `processingFailed`: `false`.
- `updatedAt`: `2026-06-30T16:29:38Z`.

Archivos relevantes:

- `snippets/microdata-schema.liquid`
  - Checksum actual: `58417e4825aa3d4570a6646f292aaedc`.
  - Size: `10787`.
  - Estado: `VERIFICADO Y CORRECTO`.
- `snippets/geo-landing-schema.liquid`
  - Estado actual: no existe en MAIN.
  - Estado: `INCOMPLETO`.
- `config/settings_data.json`
  - Checksum MAIN: `d487694e14fe7558034b7d4595075de4`.

### Tema QA validado

- Theme ID: `gid://shopify/OnlineStoreTheme/178396463480`.
- Nombre: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- Rol: `UNPUBLISHED`.
- `processing`: `false`.
- `processingFailed`: `false`.
- `updatedAt`: `2026-07-04T02:53:34Z`.

Archivos relevantes:

- `snippets/geo-landing-schema.liquid`
  - Checksum: `9033b2bfa89dc435b9811b3d897e07c1`.
  - Size: `11723`.
  - Estado: `CORREGIDO Y VERIFICADO`.
- `snippets/microdata-schema.liquid`
  - Checksum: `a3d8e23b4979219149a9c5b5f76723ec`.
  - Size: `10824`.
  - Estado: `CORREGIDO Y VERIFICADO`.
- `config/settings_data.json`
  - Checksum QA: `a1192f2f698d277e0f69f7156a61a90c`.
  - Difiere de MAIN.
  - Estado: `VERIFICADO PERO MEJORABLE`.

### Publico actual de MAIN

Comprobacion de baseline:

- `https://www.matchwalls.com/pages/papel-pintado-espana?mwqa=012l5-live-baseline`
  - HTTP 200.
  - `BreadcrumbList`: presente.
  - `WebPage`: ausente.
  - `FAQPage`: ausente.
- `https://www.matchwalls.com/fr/pages/papier-peint-en-france?mwqa=012l5-live-baseline`
  - HTTP 200.
  - `BreadcrumbList`: presente.
  - `WebPage`: ausente.
  - `FAQPage`: ausente.

## 3. Opciones evaluadas

### Opcion A - Publicar el tema QA completo

Estado: `RIESGO CRITICO`

No recomendado.

Motivo:

- El tema QA tiene `config/settings_data.json` distinto al MAIN.
- Publicarlo moveria mucho mas que el schema.
- Podria introducir regresiones visuales, de configuracion, app embeds o ajustes de tema.

Decision:

- No publicar el tema QA.

### Opcion B - Duplicar MAIN, aplicar schema y publicar duplicado tras QA completa

Estado: `VERIFICADO PERO MEJORABLE`

Es la ruta mas conservadora si se quiere evitar escribir directamente en MAIN.

Limitacion:

- La biblioteca tiene 20 temas.
- Crear otro duplicado requiere antes limpiar temas no usados con un lote separado.

Decision:

- Posible, pero mas lenta.
- Requiere `MW-THEME-LIBRARY-CLEANUP` previo si se quiere crear un nuevo duplicado.

### Opcion C - Promocion quirurgica al MAIN de solo dos archivos

Estado: `REQUIERE DECISION HUMANA`

Recomendado con aprobacion especifica.

Alcance:

1. Crear en MAIN:
   - `snippets/geo-landing-schema.liquid`
   - Checksum esperado: `9033b2bfa89dc435b9811b3d897e07c1`.
2. Actualizar en MAIN:
   - `snippets/microdata-schema.liquid`
   - Checksum previo obligatorio: `58417e4825aa3d4570a6646f292aaedc`.
   - Checksum posterior esperado: `a3d8e23b4979219149a9c5b5f76723ec`.
   - Cambio: insertar una unica llamada render a `geo-landing-schema`.

Ventajas:

- No publica el tema QA.
- No toca `settings_data.json`.
- No toca paginas, LangShop, handles, URLs, canonicals, hreflang ni metas.
- Aprovecha el QA ya superado en 012L4.
- Reversion simple: retirar el render y dejar/eliminar el snippet.

Riesgo:

- Es una escritura directa sobre MAIN; requiere aprobacion exacta y post-QA inmediato.

## 4. Decision recomendada

La ruta recomendada es:

`MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-SURGICAL-UPSERT-012L6`

No se recomienda publicar el tema QA.

## 5. Pruebas obligatorias posteriores si se aprueba 012L6

### QA positiva

10 URLs:

- Espana ES, EN, FR, DE, NL.
- Francia ES, EN, FR, DE, NL.

Comprobar:

- HTTP 200.
- canonical propio.
- sin `noindex`.
- `BreadcrumbList` presente.
- `WebPage` presente.
- `FAQPage` presente.
- 3 FAQs.
- `inLanguage` correcto.
- JSON-LD parseable sin errores.

### QA negativa

IT/PT:

- Espana IT/PT.
- Francia IT/PT.

Comprobar:

- `BreadcrumbList` mantiene estado previo.
- `WebPage` ausente.
- `FAQPage` ausente.

### QA de regresion por archivo global

Como `microdata-schema.liquid` es global, comprobar tambien:

- Home: `WebSite` y `Organization` siguen presentes.
- Producto representativo: `Product` y `Offer` siguen presentes.
- Articulo/blog si aplica: sin errores JSON-LD.

## 6. Reversion propuesta

En MAIN:

1. Retirar de `snippets/microdata-schema.liquid` la linea:
   `{%- render 'geo-landing-schema' -%}`
2. Verificar que `snippets/microdata-schema.liquid` vuelve al checksum:
   `58417e4825aa3d4570a6646f292aaedc`.
3. Eliminar `snippets/geo-landing-schema.liquid` si la herramienta lo permite; si no, dejarlo inerte sin render.

## 7. Aprobacion necesaria para ejecutar

No ejecutar escritura en MAIN hasta que Daniel apruebe exactamente:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-SURGICAL-UPSERT-012L6`

