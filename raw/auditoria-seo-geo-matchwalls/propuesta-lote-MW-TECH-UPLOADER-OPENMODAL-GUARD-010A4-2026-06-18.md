# Propuesta de lote — MW-TECH-UPLOADER-OPENMODAL-GUARD-010A4

Estado: `CORREGIDO Y VERIFICADO`.

Este lote corrige el siguiente listener nulo del cargador personalizado en el
tema auxiliar. **No publica ni modifica el MAIN.**

## 1. Nombre y alcance exacto

Modificar una única llamada en `snippets/product-customizer.liquid` del tema
auxiliar `178399019384` para registrar el listener del botón opcional solo
cuando `button[open-modal]` exista.

## 2. Recursos, IDs, URLs e idiomas afectados

- Tema: `gid://shopify/OnlineStoreTheme/178399019384`.
- Rol/prefijo: `UNPUBLISHED`, `/t/46`.
- Archivo: `snippets/product-customizer.liquid`.
- Rutas: producto estándar y `custom-file-uploader` en ES/EN/FR/DE/NL.
- MAIN `178396463480`: excluido.

## 3. Valor actual

`INCORRECTO`

- MD5: `8f8a7d213f04ace77c4003647053f763`.
- En el cargador: `button[open-modal]` = 0.
- Una única llamada directa, línea local 605:

```javascript
openModalButton.addEventListener('click', function () {
```

## 4. Valor propuesto

```javascript
openModalButton?.addEventListener('click', function () {
```

No se cambiará el cuerpo del callback ni ninguna otra línea.

## 5. Evidencia y motivo técnico

- Error reproducido 10/10 en el cargador y 0/10 en producto estándar después
  de 010A3.
- Selector ausente verificado en el DOM del cargador.
- La llamada real y única está identificada en Shopify.
- Evidencia: `qa-MW-TECH-PRODUCT-FILEINPUT-GUARD-010A3-2026-06-18.md`.

## 6. Riesgos y efectos secundarios

- En plantillas con botón, el callback debe conservarse sin cambios.
- En el cargador sin botón, no se ejecutará un callback que ya era imposible.
- Puede quedar expuesto otro selector nulo posterior; se detendrá y separará.
- `convertToInches`, tracking y overflow quedan fuera del alcance.

## 7. Respaldo disponible

- Estado actual 010A3: MD5 `8f8a7d213f04ace77c4003647053f763`.
- Original: MD5 `3878a24a9bb6cb134247ac6aff707a58`.
- MAIN y reversión intactos.

## 8. Método exacto de reversión

Restaurar `openModalButton.addEventListener` sin `?.` y comprobar que el
checksum vuelve a `8f8a7d213f04ace77c4003647053f763`.

## 9. Pruebas posteriores

- Verificar que la diferencia es exactamente un `?` adicional.
- Repetir las 20 pruebas específicas de producto y cargador.
- Confirmar ausencia del error en ambos tipos y cinco idiomas.
- Si pasan, repetir las 170 pruebas antes de proponer publicación.
- Mantener registradas las deudas independientes.

## Aprobación requerida

Para modificar únicamente el tema auxiliar, responde exactamente:

`APROBADO LOTE MW-TECH-UPLOADER-OPENMODAL-GUARD-010A4`

Esta aprobación no autoriza publicar el tema ni modificar el MAIN.

## Estado de ejecución

- Aprobación exacta recibida el 18/06/2026.
- Preflight correcto: checksum `8f8a7d213f04ace77c4003647053f763`,
  llamada directa 1, llamada opcional 0.
- Auxiliar `UNPUBLISHED`; MAIN y reversión intactos.
- La edición debe realizarse manualmente porque el conector bloquea este
  archivo de 49 KB y Shopify CLI no está instalado.

## Resultado tras la edición manual

`VERIFICADO Y CORRECTO`

- Tema auxiliar `178399019384`: `UNPUBLISHED`.
- Checksum almacenado: `d5a74ccb15b645eeb79e8c52f7c5a4ac`.
- Tamaño: `49230` bytes, exactamente un byte más que 010A3.
- El checksum coincide con el candidato calculado a partir del respaldo.
- `fileInput?.addEventListener`: 1; `openModalButton?.addEventListener`: 1.
- `openModalButton.addEventListener` directo: 0.
- MAIN `178396463480` y reversión `178383749496` mantienen checksum
  `3878a24a9bb6cb134247ac6aff707a58`.

## QA dinámica

`CORREGIDO Y VERIFICADO`

- Pruebas específicas: 20/20.
- Matriz completa: 170/170.
- Error `addEventListener`: 0.
- Fallos críticos: 0.
- Permanece el error independiente `convertToInches`, fuera del lote.
- Desbordamiento móvil: 34/85, únicamente FR/NL; deuda separada.
- Tema auxiliar sin publicar; MAIN no modificado.
