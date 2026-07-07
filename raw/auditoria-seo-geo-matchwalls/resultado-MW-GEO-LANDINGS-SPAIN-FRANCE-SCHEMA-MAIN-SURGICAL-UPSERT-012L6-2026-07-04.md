# Resultado - MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-SURGICAL-UPSERT-012L6

Fecha: 2026-07-04  
Hora de registro: 13:08 Europe/Madrid  
Estado final: `NO ACCESIBLE`

## Resumen ejecutivo

El lote fue aprobado por Daniel y se preparó correctamente, pero la escritura no pudo ejecutarse porque el conector Shopify bloquea por política de seguridad cualquier `themeFilesUpsert` contra el tema `MAIN` publicado.

No se modificó Shopify.

## Alcance aprobado

Tema destino:

- ID: `gid://shopify/OnlineStoreTheme/178399019384`
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`
- Rol: `MAIN`

Archivos previstos:

1. `snippets/geo-landing-schema.liquid`
   - Acción prevista: crear.
   - Checksum esperado: `9033b2bfa89dc435b9811b3d897e07c1`.
   - Size esperado: `11723`.

2. `snippets/microdata-schema.liquid`
   - Acción prevista: actualizar con una única llamada `{%- render 'geo-landing-schema' -%}`.
   - Checksum previo obligatorio: `58417e4825aa3d4570a6646f292aaedc`.
   - Checksum propuesto validado: `a3d8e23b4979219149a9c5b5f76723ec`.
   - Size propuesto validado: `10824`.

## Documentos leídos

- `propuesta-lote-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-SURGICAL-UPSERT-012L6-2026-07-04.md`.
- `decision-MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-PROMOTION-DECISION-012L5-2026-07-04.md`.
- `registro-cambios-ejecutados.md`.

## Validaciones previas realizadas

- Documentación Shopify consultada:
  - `themeFilesUpsert`.
  - `stagedUploadsCreate`.
  - Liquid `render`.
- Schema GraphQL inspeccionado:
  - `Mutation`.
  - `OnlineStoreThemeFilesUpsertFileInput`.
  - `StagedUploadInput`.
  - `QueryRoot`.
  - `OnlineStoreThemeFile`.
- GraphQL validado:
  - Query de lectura de tema: válido.
  - Mutación `stagedUploadsCreate`: válida.
  - Mutación `themeFilesUpsert`: válida.
- Liquid validado:
  - `snippets/microdata-schema.liquid`: válido.
  - `snippets/geo-landing-schema.liquid`: válido.

## Estado real previo comprobado en MAIN

- `role`: `MAIN`.
- `processing`: `false`.
- `processingFailed`: `false`.
- `snippets/microdata-schema.liquid`:
  - Checksum: `58417e4825aa3d4570a6646f292aaedc`.
  - Size: `10787`.
  - Estado: `VERIFICADO Y CORRECTO`.
- `snippets/geo-landing-schema.liquid`:
  - Estado: no existe.
  - Estado: `INCOMPLETO`.
- `config/settings_data.json`:
  - Checksum: `d487694e14fe7558034b7d4595075de4`.

## Operaciones ejecutadas

1. Preparación local del payload:
   - Se generó `microdata-schema.liquid` propuesto con checksum exacto `a3d8e23b4979219149a9c5b5f76723ec`.
   - Se confirmó `geo-landing-schema.liquid` con checksum `9033b2bfa89dc435b9811b3d897e07c1`.
2. Subida temporal a Shopify:
   - `microdata`: HTTP `201`.
   - `geo`: HTTP `201`.
3. Intento de `themeFilesUpsert` contra MAIN:
   - Resultado: bloqueado por política de seguridad del conector.

## Mensaje de bloqueo

El conector devolvió que `themeFilesUpsert` fue rechazado porque la operación apunta al tema publicado `MAIN`. La política del conector permite escrituras de archivos de tema solo en temas no publicados.

## Estado posterior comprobado

Lectura posterior de MAIN:

- `updatedAt`: `2026-06-30T16:29:38Z`.
- `snippets/microdata-schema.liquid`:
  - Checksum: `58417e4825aa3d4570a6646f292aaedc`.
  - Size: `10787`.
  - Estado: `VERIFICADO Y CORRECTO`.
- `snippets/geo-landing-schema.liquid`:
  - No existe.
  - Estado: `INCOMPLETO`.

Conclusión: el MAIN sigue intacto. No hubo escritura parcial.

## QA pública

No ejecutada en este lote porque no se aplicó ningún cambio al storefront publicado.

## Riesgo y reversión

- Riesgo material generado: ninguno, porque no hubo escritura en MAIN.
- Reversión requerida: no aplica.

## Próximo paso seguro

Se requiere decisión humana para elegir una vía alternativa:

1. Crear o usar un tema no publicado basado en MAIN, aplicar ahí los dos archivos, hacer QA completa y publicar manualmente desde Shopify Admin.
2. Ejecutar una edición manual quirúrgica en el code editor de Shopify sobre MAIN con instrucciones exactas y post-QA inmediato.

La opción 1 es más segura para estabilidad; la opción 2 es más rápida pero toca el tema publicado directamente.

Lectura adicional de capacidad:

- Biblioteca actual: 20 temas.
- Estado: la ruta de duplicar MAIN requiere liberar un hueco o reutilizar un tema no publicado con decisión expresa.
