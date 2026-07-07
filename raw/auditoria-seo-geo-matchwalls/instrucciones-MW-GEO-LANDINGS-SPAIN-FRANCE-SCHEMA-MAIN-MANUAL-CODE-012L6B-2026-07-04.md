# Instrucciones manuales - MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-MANUAL-CODE-012L6B

Fecha: 2026-07-04  
Estado: `APROBADO`

## Objetivo

Aplicar manualmente en el tema MAIN el schema España-Francia validado, evitando el bloqueo del conector Shopify sobre temas publicados.

## Tema destino verificado

- Theme ID: `gid://shopify/OnlineStoreTheme/178399019384`.
- Admin numeric ID: `178399019384`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol: `MAIN`.
- `processing`: `false`.
- `processingFailed`: `false`.

## Archivos locales validados

Carpeta:

`C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\manual-code-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-MANUAL-CODE-012L6B-2026-07-04\snippets`

Archivos:

- `geo-landing-schema.liquid`
  - MD5: `9033b2bfa89dc435b9811b3d897e07c1`.
  - Size: `11723`.
- `microdata-schema.liquid`
  - MD5: `a3d8e23b4979219149a9c5b5f76723ec`.
  - Size: `10824`.

Validación Shopify Liquid:

- `snippets/microdata-schema.liquid`: válido.
- `snippets/geo-landing-schema.liquid`: válido.

## Secuencia manual segura

### Paso 1 - Crear snippet nuevo sin impacto público

1. Abrir Shopify Admin.
2. Ir a `Tienda online > Temas`.
3. En el tema MAIN `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`, abrir `... > Edit code`.
4. En `Snippets`, crear un snippet nuevo llamado exactamente:

   `geo-landing-schema`

   Shopify añadirá `.liquid`.

5. Copiar todo el contenido del archivo local:

   `manual-code-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-MANUAL-CODE-012L6B-2026-07-04\snippets\geo-landing-schema.liquid`

6. Pegar en Shopify.
7. Guardar.
8. No tocar ningún otro archivo.

Confirmación que debe enviar Daniel:

`GUARDADO GEO 012L6B`

### Paso 2 - Activar render en microdata

No ejecutar hasta que Codex verifique el Paso 1.

Acción prevista:

- Abrir `snippets/microdata-schema.liquid`.
- Buscar:

`{%- if request.page_type == 'index' -%}`

- Insertar justo antes:

`{%- render 'geo-landing-schema' -%}`

- Debe quedar con una línea en blanco entre el render y el bloque `index`.

Confirmación que debe enviar Daniel:

`GUARDADO MICRODATA 012L6B`

## Reversión

Si el Paso 2 falla:

1. Eliminar la línea:

   `{%- render 'geo-landing-schema' -%}`

2. Guardar `snippets/microdata-schema.liquid`.
3. Verificar que vuelve a checksum `58417e4825aa3d4570a6646f292aaedc`.
4. El snippet `geo-landing-schema.liquid` puede quedar sin render, inerte, o eliminarse en un lote posterior.

