# Resultado lote MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-DRAFT-THEME-UPSERT-012L4

Fecha: 2026-07-04  
Estado final: `CORREGIDO Y VERIFICADO`

## Aprobacion

Daniel aprobo exactamente:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-DRAFT-THEME-UPSERT-012L4`

## Alcance ejecutado

Se escribio exclusivamente en el tema no publicado:

- Theme ID: `gid://shopify/OnlineStoreTheme/178396463480`.
- Nombre: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- Rol verificado antes de escribir: `UNPUBLISHED`.

Archivos modificados:

1. `snippets/geo-landing-schema.liquid`
   - Estado previo: no existia.
   - Estado posterior: creado.
   - Checksum posterior: `9033b2bfa89dc435b9811b3d897e07c1`.
   - Size: `11723`.

2. `snippets/microdata-schema.liquid`
   - Checksum previo: `58417e4825aa3d4570a6646f292aaedc`.
   - Checksum posterior: `a3d8e23b4979219149a9c5b5f76723ec`.
   - Cambio aplicado: una llamada render a `geo-landing-schema`.
   - Size posterior: `10824`.

No se publico ningun tema.  
No se modifico MAIN.  
No se modificaron paginas, LangShop, handles, URLs, canonicals, hreflang, metadatos, precios, productos ni redirecciones.

## Validaciones previas

- Busqueda documentacion Shopify Admin: `themeFilesUpsert mutation`.
- Busqueda documentacion Liquid: `render snippet Liquid json ld`.
- Validacion Liquid individual:
  - `geo-landing-schema.liquid`: `VALID`.
- Validacion Liquid conjunta con locales reales:
  - `microdata-schema.liquid`: `VALID`.
  - `geo-landing-schema.liquid`: `VALID`.
- Validacion GraphQL:
  - `themeFilesUpsert`: `VALID`.

## Escritura Shopify

Metodo usado:

- `stagedUploadsCreate` para preparar carga temporal privada.
- Upload temporal privado: HTTP `201` para ambos archivos.
- `themeFilesUpsert` sobre `gid://shopify/OnlineStoreTheme/178396463480`.
- Resultado mutation: `userErrors=[]`.

## Post-check Shopify

- Tema destino sigue `UNPUBLISHED`.
- `snippets/geo-landing-schema.liquid`: checksum `9033b2bfa89dc435b9811b3d897e07c1`.
- `snippets/microdata-schema.liquid`: checksum `a3d8e23b4979219149a9c5b5f76723ec`.
- MAIN `gid://shopify/OnlineStoreTheme/178399019384` sigue con `snippets/microdata-schema.liquid` checksum `58417e4825aa3d4570a6646f292aaedc`.

## QA preview autenticado

El preview publico simple no servia el tema QA y devolvia MAIN.  
La verificacion real se ejecuto en navegador autenticado con preview del tema `178396463480`.

Resultado:

- 10/10 URLs prioritarias ES/EN/FR/DE/NL con:
  - `BreadcrumbList`;
  - `WebPage`;
  - `FAQPage`;
  - 3 FAQs;
  - `inLanguage` correcto;
  - canonical propio;
  - sin `noindex`;
  - JSON-LD parseable sin errores.
- 4/4 URLs negativas IT/PT con:
  - `BreadcrumbList` existente;
  - sin `WebPage`;
  - sin `FAQPage`;
  - sin `noindex`;
  - JSON-LD parseable sin errores.

## Reversion

Reversion minima:

1. En el tema `gid://shopify/OnlineStoreTheme/178396463480`, retirar de `snippets/microdata-schema.liquid` la linea:
   `{%- render 'geo-landing-schema' -%}`
2. Restaurar checksum de `snippets/microdata-schema.liquid` a `58417e4825aa3d4570a6646f292aaedc`.
3. Si se desea limpieza adicional, eliminar `snippets/geo-landing-schema.liquid`; si no se elimina, queda inerte sin render.

## Estado

`CORREGIDO Y VERIFICADO` en tema no publicado.

No queda autorizado publicar este tema. La publicacion o traslado a MAIN requiere lote nuevo.
