# Propuesta de lote — MW-TECH-JS-ADD-EVENT-LISTENER-010A

Estado: `VERIFICADO PERO MEJORABLE`.

Este lote prepara y prueba la corrección. **No publica el tema auxiliar.**

## 1. Nombre y alcance exacto

1. Duplicar el MAIN `178396463480` como tema `UNPUBLISHED` con nombre
   `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
2. Editar únicamente `snippets/srolling_bar_menu.liquid` en el tema auxiliar.
3. Añadir comprobaciones de existencia a los listeners de anchura y altura.
4. Ejecutar QA del tema auxiliar. No publicar ni modificar el MAIN.

## 2. Recursos, IDs, URLs e idiomas afectados

- Tema fuente: `gid://shopify/OnlineStoreTheme/178396463480`, MAIN `/t/45`.
- Tema destino: nuevo `UNPUBLISHED`; Shopify asignará el ID al duplicarlo.
- Único archivo propuesto: `snippets/srolling_bar_menu.liquid`.
- Idiomas de QA: ES, EN, FR, DE y NL.
- Rutas: matriz de 17 URLs usada en el lote 009, escritorio y móvil; además se
  probarán los campos reales del personalizador.

No incluye publicación, URLs, handles, contenido, traducciones, schema,
inventario, precios, Apps Embeds ni plataformas externas.

## 3. Valores actuales

`INCORRECTO`

- MD5: `c254cf711a7706dc21ece2f2ad31acea`.
- `widthInput` y `heightInput` pueden ser `null`.
- El código registra ambos listeners sin validarlos.
- Error público reproducido en home, producto, colección y carrito.

Código funcional actual:

```javascript
const debouncedWidthEvent = debounce(() => {
  pushInputMuralOutsideEvent('width', widthInput.value);
}, 300);

const debouncedHeightEvent = debounce(() => {
  pushInputMuralOutsideEvent('height', heightInput.value);
}, 300);

widthInput.addEventListener('input', debouncedWidthEvent);
heightInput.addEventListener('input', debouncedHeightEvent);
```

## 4. Valores propuestos

```javascript
if (widthInput) {
  const debouncedWidthEvent = debounce(() => {
    pushInputMuralOutsideEvent('width', widthInput.value);
  }, 300);

  widthInput.addEventListener('input', debouncedWidthEvent);
}

if (heightInput) {
  const debouncedHeightEvent = debounce(() => {
    pushInputMuralOutsideEvent('height', heightInput.value);
  }, 300);

  heightInput.addEventListener('input', debouncedHeightEvent);
}
```

No se propone ninguna otra diferencia.

## 5. Evidencia y motivo técnico

- Consola: excepción en el `DOMContentLoaded` del HTML público.
- HTML renderizado: bloque con ambos listeners sin guardas.
- Shopify: archivo fuente identificado y leído, sin errores.
- El snippet se renderiza desde el encabezado global.
- Diagnóstico completo:
  `diagnostico-MW-TECH-JS-ADD-EVENT-LISTENER-010A-2026-06-18.md`.

## 6. Riesgos y efectos secundarios

- Riesgo bajo de alterar el tracking `input_mural_outside` si la guarda se
  implementa incorrectamente.
- Riesgo de que el tema auxiliar herede una configuración incompleta durante
  la duplicación; se compararán roles, archivos y App Embeds antes del cambio.
- El error independiente `convertToInches` permanecerá y no debe confundirse
  con un fallo del lote.
- No existe impacto público durante este lote porque el destino será
  `UNPUBLISHED`.

## 7. Respaldo disponible

`VERIFICADO Y CORRECTO`

- Copia local exacta:
  `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E/snippets/srolling_bar_menu.liquid`.
- Tamaño 8.581 bytes y MD5
  `c254cf711a7706dc21ece2f2ad31acea`, igual que Shopify.
- ZIP válido `MW-THEME-PAGE-H1-SEMANTIC-008E-patched-QA-2026-06-17-2331.zip`
  contiene el mismo archivo, tamaño y MD5.
- El MAIN y la reversión `178383749496` no se modificarán.

## 8. Método exacto de reversión

Antes de publicar:

1. Restaurar el archivo original en el tema auxiliar y comprobar el MD5; o
2. eliminar el tema auxiliar mediante un lote de limpieza separado.

Si posteriormente se aprobara y publicara en otro lote, la reversión sería
republicar `178396463480`, que permanecerá intacto como tema no publicado.

## 9. Pruebas posteriores

- Confirmar que solo difiere el archivo autorizado.
- Confirmar ausencia del error `addEventListener` en las 170 combinaciones.
- Confirmar un H1, canonical, hreflang, `lang`, contenido y ausencia de 404.
- Probar home, producto, colección, carrito y formularios.
- Probar escritorio, 390 px y 375 px.
- Probar que `input_mural_outside` sigue entrando en `dataLayer` al modificar
  anchura y altura en una plantilla que sí contiene ambos campos.
- Registrar cualquier error independiente sin atribuirlo a 010A.

## Aprobación requerida

Para crear y modificar únicamente el tema auxiliar, responde exactamente:

`APROBADO LOTE MW-TECH-JS-ADD-EVENT-LISTENER-010A`

Esta aprobación no autoriza publicar el tema ni modificar el MAIN.

## Resultado ejecutado

- Tema auxiliar creado: `178399019384`, `/t/46`, `UNPUBLISHED`.
- Único archivo modificado: `snippets/srolling_bar_menu.liquid`.
- Checksum nuevo: `7d6dfb8df5e4b9ef813eca32aaebc237`.
- MAIN intacto con checksum `c254cf711a7706dc21ece2f2ad31acea`.
- 170/170 pruebas críticas correctas y 0/170 apariciones del error.
- El tracking genera 0 eventos tanto en MAIN como en auxiliar: deuda
  preexistente confirmada y criterio funcional no cumplido.
- No se publicó el auxiliar. Requiere el sublote 010A2.
