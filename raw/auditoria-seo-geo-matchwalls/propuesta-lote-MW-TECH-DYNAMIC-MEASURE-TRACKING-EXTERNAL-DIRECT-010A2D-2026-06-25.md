# Propuesta de lote - MW-TECH-DYNAMIC-MEASURE-TRACKING-EXTERNAL-DIRECT-010A2D

Estado: `REQUIERE DECISION HUMANA`.

Esta propuesta deriva del diagnostico `MW-TECH-DYNAMIC-MEASURE-TRACKING-DIAG-010A2C`. No reutiliza el candidato fallido `010A2B`.

## 1. Nombre y alcance exacto del lote

`MW-TECH-DYNAMIC-MEASURE-TRACKING-EXTERNAL-DIRECT-010A2D`

Modificar unicamente el tema auxiliar `178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.

Archivo propuesto:

- `snippets/external-selectors.liquid`.

No se autoriza:

- publicar tema;
- modificar MAIN `178396463480`;
- modificar `snippets/srolling_bar_menu.liquid` en este sublote;
- modificar productos, precios, variantes, inventario, GTM, GA4 o apps;
- modificar URLs, handles, canonicals, hreflang o redirecciones.

## 2. Recursos, IDs, URLs e idiomas afectados

Tema afectado:

- `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre actual: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Rol: `UNPUBLISHED`.
- Prefijo: `/t/46`.

URL critica de QA:

- `https://www.matchwalls.com/products/custom-file-uploader?preview_theme_id=178399019384&mwqa=010a2d`.

Idiomas de QA inicial:

- ES como centinela tecnico.

Idiomas posteriores si la prueba critica pasa:

- ES.
- EN.
- FR.
- DE.
- NL.

## 3. Valores actuales verificados

`snippets/external-selectors.liquid` en auxiliar:

- MD5: `8a9c233bca52da58ce59fffc3aee8359`.
- Bytes: 10199.
- Estado: `VERIFICADO Y CORRECTO`.
- Contiene los listeners funcionales de `externalWidthInput` y `externalHeightInput`.
- No contiene `pushExternalWidthTracking`.
- No empuja `input_mural_outside`.

Prueba actual:

- `401 x 301` sincroniza inputs internos.
- Superficie: `4.01m x 3.01m = 12.07 m²`.
- Eventos `input_mural_outside`: 0 en QA soportada.
- Errores de consola: 0.

## 4. Valores propuestos

En `snippets/external-selectors.liquid`:

- Añadir una funcion local minima para empujar a `window.dataLayer` el evento `input_mural_outside`.
- Usar las claves existentes: `event`, `dimension`, `value`.
- Invocar la funcion directamente al final del listener de anchura ya existente.
- Invocar la funcion directamente al final del listener de altura ya existente.
- No introducir debounce/helper nuevo en esta iteracion.
- No modificar calculo de superficie, unidades, precio, personalizador ni `localStorage`.
- Añadir una senal QA temporal y condicionada por `mwqa=010a2d` para escribir en DOM el ultimo evento generado y poder verificarlo sin depender de lectura directa de `window.dataLayer`.

## 5. Evidencia y motivo tecnico

Hechos verificados:

- `external-selectors.liquid` recibe los eventos reales de los campos.
- `srolling_bar_menu.liquid` contiene tracking historico, pero `010A2` y la QA actual no demostraron que genere el evento.
- `010A2B` fallo pese a mover responsabilidad a `external-selectors.liquid`; no debe repetirse tal cual.
- La lectura puente del `window` real no esta disponible en el navegador por politica de seguridad, por lo que hace falta una senal QA visible en DOM.

Inferencia tecnica:

- El punto correcto de intervencion sigue siendo `external-selectors.liquid`, pero el cambio debe ser mas simple que `010A2B` y verificable con senal QA propia.

## 6. Riesgos y efectos secundarios

- Riesgo de duplicado si el tracking historico de `srolling_bar_menu.liquid` tambien disparase en algun escenario. Por eso este sublote no limpia el header: primero mide si hay 1 o mas eventos.
- Riesgo de ensuciar el tema con senal QA. La senal debe quedar limitada por parametro `mwqa=010a2d` y retirarse o evaluarse antes de publicar.
- Riesgo de declarar exito solo por `0 userErrors`; el lote exige QA publica con evento real.
- Riesgo de romper calculo/precio si se toca fuera de los listeners actuales; queda prohibido.

## 7. Respaldo disponible

Valor de reversion:

- `snippets/external-selectors.liquid`: MD5 `8a9c233bca52da58ce59fffc3aee8359`, bytes 10199.

MAIN queda fuera del lote.

## 8. Metodo exacto de reversion

Si falla cualquier prueba critica:

1. Restaurar `snippets/external-selectors.liquid` al contenido con MD5 `8a9c233bca52da58ce59fffc3aee8359`.
2. Confirmar por GraphQL que el checksum vuelve a `8a9c233bca52da58ce59fffc3aee8359`.
3. Confirmar que el auxiliar sigue `UNPUBLISHED`.
4. No publicar.

## 9. Pruebas posteriores obligatorias

Prueba critica inmediata:

- Abrir `custom-file-uploader` en preview del auxiliar con `mwqa=010a2d`.
- Cambiar anchura y altura.
- Confirmar que los inputs internos siguen sincronizados.
- Confirmar que la superficie calculada sigue correcta.
- Confirmar que la senal QA en DOM registra `input_mural_outside`.
- Confirmar `dimension=width` y `dimension=height`.
- Confirmar valores exactos.
- Confirmar si hay 1 evento por dimension o duplicados.
- Confirmar errores de consola: 0.

Si la prueba critica pasa:

- QA ES/EN/FR/DE/NL en desktop y mobile.
- QA producto estandar para comprobar ausencia de regresion global.
- Evaluar sublote posterior para limpiar `srolling_bar_menu.liquid` si procede.
- Repetir matriz de 170 pruebas antes de cualquier publicacion.

Si la prueba critica falla:

- Reversion inmediata.
- No ejecutar matriz completa.
- Registrar estado `INCORRECTO`.

## 10. Aprobacion requerida

Para ejecutar este lote en el tema auxiliar, responde exactamente:

`APROBADO LOTE MW-TECH-DYNAMIC-MEASURE-TRACKING-EXTERNAL-DIRECT-010A2D`

Esta aprobacion no autoriza publicar el tema ni modificar el MAIN.
## Resultado ejecutado

Estado: `CORREGIDO Y VERIFICADO`.

- Ejecutado sobre tema auxiliar `178399019384`, rol `UNPUBLISHED`.
- Archivo: `snippets/external-selectors.liquid`.
- MD5 previo: `8a9c233bca52da58ce59fffc3aee8359`.
- MD5 final: `95266feda1603e9c9ef028f0dae74c6f`.
- QA critica ES superada con eventos `input_mural_outside` para anchura y altura.
- Mini-QA ES/EN/FR/DE/NL superada en URL critica.
- Producto estandar verificado sin errores de consola; altura no reescrita por limitacion del navegador de QA.
- MAIN no modificado.
- Ningun tema publicado.

Evidencia: `qa-MW-TECH-DYNAMIC-MEASURE-TRACKING-EXTERNAL-DIRECT-010A2D-2026-06-25.md`.