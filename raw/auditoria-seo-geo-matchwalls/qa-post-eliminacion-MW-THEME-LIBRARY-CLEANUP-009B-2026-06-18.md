# QA posterior — MW-THEME-LIBRARY-CLEANUP-009B

Fecha: 2026-06-18 20:15 CEST.

Estado final: `CORREGIDO Y VERIFICADO`.

## Operación verificada

- Tema eliminado: `gid://shopify/OnlineStoreTheme/142344224995`.
- Nombre previo: `Copy of Production`.
- Rol previo: `UNPUBLISHED`.
- Biblioteca antes/después: 20/19 temas.
- El tema eliminado ya no es recuperable por ID: la consulta devuelve `null`.

## Integridad de producción y reversión

- MAIN: `178396463480`, rol `MAIN`, prefijo `/t/45`.
- MAIN procesado sin fallo: `processing=false`, `processingFailed=false`.
- Reversión: `178383749496`, rol `UNPUBLISHED`, prefijo `/t/43`.
- Reversión procesada sin fallo: `processing=false`, `processingFailed=false`.

## Respaldo

- ZIP: `theme_export__www-matchwalls-com-copy-of-production__18JUN2026-0801pm.zip`.
- Tamaño: 2.890.489 bytes.
- SHA-256: `98ED8E69178BAC7A915DA228B4F56499ECF3DC1543B7671569465CD089B3DE74`.
- Cobertura: 289/289 archivos; 0 ausentes, 0 extras y 0 checksums distintos.
- Copia archivada en
  `backups/MW-THEME-LIBRARY-CLEANUP-009B-2026-06-18/`.

## Pruebas públicas posteriores

Rutas comprobadas en escritorio y móvil: `/`,
`/products/lineas-noridcas-marron`,
`/collections/lo-mas-contemporaneo-murales` y `/cart`.

- 8/8 cargas sirven archivos del tema `/t/45`.
- 8/8 cargas tienen contenido público no vacío.
- 8/8 cargas no presentan título de 404.
- Home, producto y colección presentan un H1 en las repeticiones válidas.
- La portada móvil necesitó una repetición por carga transitoria; la repetición
  mostró H1 y ancho `375/375`.

## Incidencias fuera del alcance

`VERIFICADO PERO MEJORABLE`

- El producto representativo mostró desbordamiento móvil `427/375` en dos
  pasadas. Debe localizarse el elemento causante en un sublote técnico; no se
  atribuye a la eliminación de un tema no publicado.
- El carrito no expuso H1 en este smoke test. No se modificó el MAIN durante el
  lote y la incidencia se incorpora al diagnóstico técnico/semántico.
- Una navegación de producto en escritorio agotó el tiempo de espera, pero la
  página quedó cargada con URL, título, contenido, H1 y `/t/45` correctos.

## Reversión disponible

Reimportar el ZIP verificado como tema nuevo `UNPUBLISHED` y contrastar sus 289
archivos con el manifiesto previo. Shopify asignará un ID nuevo.

