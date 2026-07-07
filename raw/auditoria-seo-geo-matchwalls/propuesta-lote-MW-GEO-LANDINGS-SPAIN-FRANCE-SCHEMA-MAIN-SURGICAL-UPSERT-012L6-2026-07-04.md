# Propuesta de lote - MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-SURGICAL-UPSERT-012L6

Fecha propuesta: 2026-07-04  
Tipo: escritura quirurgica en MAIN.  
Estado: `REQUIERE DECISION HUMANA`

## Objetivo

Incorporar al tema MAIN el schema Espana-Francia validado en 012L4, sin publicar el tema QA completo y sin modificar configuracion de tema.

## Aprobacion necesaria

No ejecutar hasta que Daniel apruebe exactamente:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-SURGICAL-UPSERT-012L6`

## Tema destino

- Theme ID: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol actual: `MAIN`.

Condiciones de seguridad previas:

- Releer MAIN justo antes de escribir.
- Abortarlo todo si:
  - el theme ID no coincide;
  - `role` no es `MAIN`;
  - `processing` no es `false`;
  - `processingFailed` no es `false`;
  - `snippets/microdata-schema.liquid` no tiene checksum `58417e4825aa3d4570a6646f292aaedc`;
  - `snippets/geo-landing-schema.liquid` ya existe con contenido no esperado.

## Recursos afectados

Solo en MAIN:

1. `snippets/geo-landing-schema.liquid`
   - Estado actual: no existe.
   - Estado propuesto: crear.
   - Checksum esperado: `9033b2bfa89dc435b9811b3d897e07c1`.
   - Size esperado: `11723`.

2. `snippets/microdata-schema.liquid`
   - Estado actual: checksum `58417e4825aa3d4570a6646f292aaedc`.
   - Estado propuesto: checksum `a3d8e23b4979219149a9c5b5f76723ec`.
   - Cambio: insertar una unica llamada render a `geo-landing-schema`.

## No incluido

- No publicar tema.
- No publicar ni activar el tema QA.
- No tocar `config/settings_data.json`.
- No tocar LangShop.
- No tocar paginas.
- No tocar handles, URLs, canonicals, hreflang ni metadatos.
- No activar schema en IT/PT.

## QA posterior obligatoria

### Landings positivas

- Espana: ES, EN, FR, DE, NL.
- Francia: ES, EN, FR, DE, NL.

Validar:

- HTTP 200.
- canonical propio.
- sin `noindex`.
- `BreadcrumbList`, `WebPage`, `FAQPage`.
- 3 FAQs.
- `inLanguage` correcto.
- JSON-LD parseable.

### Landings negativas

- Espana IT/PT.
- Francia IT/PT.

Validar:

- `WebPage` ausente.
- `FAQPage` ausente.

### Regresion global

- Home: `WebSite` y `Organization`.
- Producto representativo: `Product` y `Offer`.
- Blog/articulo si aplica: JSON-LD parseable.

## Reversion

1. Retirar la llamada render de `snippets/microdata-schema.liquid`.
2. Verificar checksum `58417e4825aa3d4570a6646f292aaedc`.
3. Eliminar o dejar inerte `snippets/geo-landing-schema.liquid`.

## Decision recomendada

Ejecutar 012L6 solo con aprobacion exacta.  
No publicar el tema QA completo.

