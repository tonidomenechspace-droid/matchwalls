# Propuesta de lote — MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B

Estado: `REQUIERE DECISION HUMANA`.

Esta propuesta sustituye al intento fallido `010A2`. No reutiliza el lote fallido y no modifica el MAIN.

## 1. Nombre y alcance exacto del lote

`MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B`

Modificar unicamente el tema auxiliar `178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`, para corregir el tracking de medidas dinamicas.

Archivos propuestos:

- `snippets/external-selectors.liquid`.
- `snippets/srolling_bar_menu.liquid`.

No se autoriza:

- publicar tema;
- modificar MAIN `178396463480`;
- modificar rollback `178383749496`;
- modificar productos, precios, variantes, inventario, GTM, GA4 o apps.

## 2. Recursos, IDs, URLs e idiomas afectados

Tema afectado:

- `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre actual: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol: `UNPUBLISHED`.
- Prefijo: `/t/46`.

URL critica de QA:

- `https://www.matchwalls.com/products/custom-file-uploader?preview_theme_id=178399019384`.

Idiomas de QA:

- ES.
- EN.
- FR.
- DE.
- NL.

## 3. Valores actuales verificados

`snippets/external-selectors.liquid`:

- MD5 actual en auxiliar: `8a9c233bca52da58ce59fffc3aee8359`.
- Bytes: 10199.
- Contiene los campos `#external-width` y `#external-height`.
- Contiene los listeners funcionales que actualizan inputs internos, superficie, personalizador y `localStorage`.
- No empuja `input_mural_outside`.

`snippets/srolling_bar_menu.liquid`:

- MD5 actual en auxiliar: `7d6dfb8df5e4b9ef813eca32aaebc237`.
- Bytes: 8539.
- Mantiene la guarda de `010A`.
- Sigue conteniendo la responsabilidad de `input_mural_outside` dentro del header global.
- En la prueba publica no genera eventos de medida.

Prueba funcional actual:

- Cambio `402 × 302`: inputs internos sincronizados correctamente.
- Superficie: `4.02m x 3.02m = 12.14 m²`.
- Eventos `input_mural_outside`: 0.
- `window.dataLayer`: no creado por este tracking.
- Errores de consola: 0.

## 4. Valores propuestos

En `snippets/external-selectors.liquid`:

- Añadir una funcion local minima para empujar `input_mural_outside` a `window.dataLayer`.
- Añadir debounce local de 300 ms.
- Invocar el evento de anchura dentro del listener ya existente de `externalWidthInput`.
- Invocar el evento de altura dentro del listener ya existente de `externalHeightInput`.
- Mantener intactas las funciones de calculo, sincronizacion interna, actualizacion de personalizador y guardado en `localStorage`.

En `snippets/srolling_bar_menu.liquid`:

- Retirar solo la responsabilidad de tracking de medidas `input_mural_outside`.
- Mantener intacto el tracking de menu `collection_submenu_click`.
- Mantener la estabilidad alcanzada en `010A`: ningun acceso directo sin comprobacion a elementos inexistentes.

## 5. Evidencia y motivo tecnico

Hechos verificados:

- `010A2` fallo y fue revertido.
- El header renderiza una logica de `input_mural_outside`, pero no genera eventos en el preview del auxiliar.
- `external-selectors.liquid` si recibe los eventos reales de los inputs, demostrado por la sincronizacion de los campos internos y el calculo de superficie.
- `external-selectors.liquid` esta identico en MAIN, auxiliar y rollback, por lo que aun no se ha intervenido el punto funcional correcto.

Inferencia tecnica:

- El evento debe vivir junto al listener que ya funciona, no en el header global.
- Dejar dos sitios con responsabilidad potencial sobre el mismo evento puede producir duplicados si cambia el orden de carga, por eso se propone limpiar el header en el mismo sublote.

## 6. Riesgos y efectos secundarios

- Riesgo de duplicar eventos si no se retira el tracking muerto del header.
- Riesgo de alterar la medicion si se cambia el nombre del evento o las claves `dimension` y `value`; el lote debe conservarlas.
- Riesgo de romper calculo o precio si se toca fuera de los listeners actuales; el lote no debe modificar calculo, unidades, precios ni personalizador.
- Riesgo de declarar el lote correcto solo por `0 userErrors`; la salida exige prueba publica con evento real.

## 7. Respaldo disponible

Valores de reversion del tema auxiliar:

- `snippets/external-selectors.liquid`: `8a9c233bca52da58ce59fffc3aee8359`.
- `snippets/srolling_bar_menu.liquid`: `7d6dfb8df5e4b9ef813eca32aaebc237`.

MAIN y rollback quedan fuera del lote.

## 8. Metodo exacto de reversion

Si falla cualquier prueba critica:

1. Restaurar `snippets/external-selectors.liquid` al contenido con MD5 `8a9c233bca52da58ce59fffc3aee8359`.
2. Restaurar `snippets/srolling_bar_menu.liquid` al contenido con MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`.
3. Confirmar por GraphQL que ambos checksums han vuelto a esos valores.
4. Confirmar que el auxiliar sigue `UNPUBLISHED`.
5. No publicar.

Metodo alternativo de reversion:

- Descartar el tema auxiliar `178399019384` y conservar MAIN/rollback intactos.

## 9. Pruebas posteriores obligatorias

Prueba critica inmediata:

- Abrir `custom-file-uploader` en preview del auxiliar.
- Cambiar anchura y altura.
- Confirmar exactamente 1 evento `input_mural_outside` por dimension tras el debounce.
- Confirmar valores exactos en `dimension` y `value`.
- Confirmar que los inputs internos siguen sincronizados.
- Confirmar que la superficie calculada sigue correcta.
- Confirmar errores de consola: 0.

Si la prueba critica pasa:

- QA en ES/EN/FR/DE/NL, desktop y mobile, en la URL critica.
- QA de producto estandar para comprobar ausencia de regresion global.
- Repeticion de la matriz de 170 pruebas del tema auxiliar.
- Confirmacion de que solo han cambiado los dos archivos autorizados.
- Confirmacion de que MAIN y rollback siguen intactos.

Si la prueba critica falla:

- Reversion inmediata.
- No ejecutar matriz completa.
- Registrar estado `INCORRECTO`.

## 10. Aprobacion requerida

Para ejecutar este lote en el tema auxiliar, responde exactamente:

`APROBADO LOTE MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B`

Esta aprobacion no autoriza publicar el tema ni modificar el MAIN.
