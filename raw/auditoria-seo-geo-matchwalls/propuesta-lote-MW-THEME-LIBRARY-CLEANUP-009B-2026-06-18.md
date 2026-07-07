# Propuesta de lote — MW-THEME-LIBRARY-CLEANUP-009B

Estado: `CORREGIDO Y VERIFICADO`.

## 1. Nombre y alcance exacto

Respaldar y eliminar exclusivamente el tema no publicado
`gid://shopify/OnlineStoreTheme/142344224995`, llamado `Copy of Production`,
para reducir la biblioteca de 20 a 19 temas.

## 2. Recursos, IDs, URLs e idiomas afectados

- Recurso: un tema Shopify `UNPUBLISHED`.
- ID: `gid://shopify/OnlineStoreTheme/142344224995`.
- Nombre: `Copy of Production`.
- URLs públicas e idiomas: ninguno; el tema no es MAIN.

Quedan excluidos todos los demás temas, incluido el MAIN `178396463480` y la
reversión `178383749496`.

## 3. Valores actuales

`VERIFICADO Y CORRECTO`

- Biblioteca: 20 temas.
- Tema objetivo: `UNPUBLISHED`.
- Creado: 05/09/2024.
- Actualizado: 09/09/2024.
- Archivos: 289; sin errores de lectura.
- Existe un `Copy of Production` posterior, `142418575587`, con los mismos 289
  nombres de archivo y cinco checksums distintos.

## 4. Valores propuestos

- Descargar y verificar un ZIP del tema `142344224995`.
- Eliminar únicamente `142344224995`.
- Biblioteca posterior esperada: 19 temas.
- MAIN y tema de reversión: sin cambios.

## 5. Evidencia y motivo técnico

- Shopify muestra `Theme limit reached`.
- El tema objetivo no está publicado.
- Es el `Copy of Production` más antiguo.
- Un sucesor inmediato conserva la misma estructura de 289 archivos.
- Liberar una plaza es necesario para preparar el tema auxiliar de deuda
  técnica sin tocar producción.

## 6. Riesgos y efectos secundarios

- El tema contiene dos diferencias funcionales respecto de su sucesor:
  `sections/header.liquid` y `snippets/navigation-panel.liquid`.
- La eliminación destruye el ID y sus preview URLs.
- Una restauración desde ZIP generaría un ID nuevo.
- El nombre genérico no permite demostrar quién creó el tema ni su finalidad.

## 7. Respaldo disponible

Estado: `INCOMPLETO`.

El respaldo debe crearse como primera acción del lote. No se eliminará el tema
si no se obtiene un ZIP legible, con tamaño/hash registrados y cobertura de 289
archivos.

## 8. Método exacto de reversión

1. Importar el ZIP respaldado como tema nuevo no publicado.
2. Verificar sus archivos y checksums contra el inventario previo.
3. Mantenerlo `UNPUBLISHED`.

La reversión recupera el contenido, pero no el ID original.

## 9. Pruebas posteriores

- Confirmar 19 temas.
- Confirmar `178396463480` como MAIN.
- Confirmar `178383749496` como `UNPUBLISHED` y disponible para reversión.
- Smoke test de home, producto, colección y carrito en escritorio y móvil.
- Registrar ZIP, hash, eliminación, roles y resultado.

## Aprobación requerida

No ejecutar hasta recibir exactamente:

`APROBADO LOTE MW-THEME-LIBRARY-CLEANUP-009B`

Esta aprobación no autoriza eliminar ningún otro tema.

## Resultado ejecutado y verificado

- Aprobación exacta recibida el 18/06/2026.
- Respaldo ZIP verificado contra los 289 archivos antes del borrado.
- Eliminado exclusivamente `142344224995` mediante Shopify Admin.
- Consulta posterior: 19 temas y objetivo inexistente (`null`).
- MAIN `178396463480` y reversión `178383749496` intactos.
- Smoke test posterior: home, producto, colección y carrito en escritorio y
  móvil sirven `/t/45`, contienen contenido y no presentan 404.
- Evidencia: `qa-post-eliminacion-MW-THEME-LIBRARY-CLEANUP-009B-2026-06-18.md`.
