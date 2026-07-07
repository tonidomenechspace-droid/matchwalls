# Propuesta de lote — MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2

Estado: `INCORRECTO` — ejecutado y revertido.

Este lote corrige el tracking dinámico en el tema auxiliar. **No publica ni
modifica el MAIN.**

## 1. Nombre y alcance exacto

Modificar únicamente `snippets/srolling_bar_menu.liquid` en el tema auxiliar
`178399019384` para sustituir listeners directos por un listener delegado que
funcione cuando los campos se insertan después de `DOMContentLoaded`.

## 2. Recursos, IDs, URLs e idiomas afectados

- Tema: `gid://shopify/OnlineStoreTheme/178399019384`.
- Rol/prefijo: `UNPUBLISHED`, `/t/46`.
- Archivo: `snippets/srolling_bar_menu.liquid`.
- Idiomas de QA: ES, EN, FR, DE y NL.
- MAIN `178396463480`: excluido.

## 3. Valores actuales

`VERIFICADO PERO MEJORABLE`

- Checksum: `7d6dfb8df5e4b9ef813eca32aaebc237`.
- La excepción global está ausente.
- Los listeners solo se registran si los campos existen durante
  `DOMContentLoaded`.
- Los campos del personalizador aparecen después y generan 0 eventos de
  `dataLayer` al cambiar sus valores.
- El MAIN original también genera 0 eventos: es deuda preexistente.

## 4. Valores propuestos

Reemplazar las dos guardas directas por:

```javascript
const debouncedWidthEvent = debounce((value) => {
  pushInputMuralOutsideEvent('width', value);
}, 300);

const debouncedHeightEvent = debounce((value) => {
  pushInputMuralOutsideEvent('height', value);
}, 300);

document.addEventListener('input', function (event) {
  const target = event.target;
  if (!target) return;

  if (target.id === 'external-width') {
    debouncedWidthEvent(target.value);
  } else if (target.id === 'external-height') {
    debouncedHeightEvent(target.value);
  }
});
```

No se propone ninguna otra diferencia.

## 5. Evidencia y motivo técnico

- MAIN y auxiliar: ambos generan 0 eventos con los campos ya visibles.
- MAIN: además lanza la excepción original durante `DOMContentLoaded`.
- Auxiliar: la guarda evita la excepción, pero no observa campos añadidos más
  tarde.
- Un listener delegado en `document` observa esos campos sin depender de su
  momento de inserción.
- Evidencia: `qa-MW-TECH-JS-ADD-EVENT-LISTENER-010A-2026-06-18.md`.

## 6. Riesgos y efectos secundarios

- Posible doble evento si coexistiera otro listener; el lote sustituirá, no
  añadirá, los listeners actuales.
- Posible evento sobre un elemento ajeno que reutilice los mismos IDs; se
  limita estrictamente a `external-width` y `external-height`.
- El `SyntaxError`, overflow y `convertToInches` quedan fuera del alcance.

## 7. Respaldo disponible

- Original MAIN local/remoto: MD5 `c254cf711a7706dc21ece2f2ad31acea`.
- Estado actual del auxiliar: MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`.
- El MAIN y la reversión permanecen intactos.

## 8. Método exacto de reversión

Restaurar en el auxiliar el bloque con guardas aprobado en 010A y comprobar que
el checksum vuelve a `7d6dfb8df5e4b9ef813eca32aaebc237`. Si la QA crítica
falla, no publicar.

## 9. Pruebas posteriores

- Verificar contenido almacenado y que solo difiere el archivo autorizado.
- Cambiar anchura y altura y confirmar un evento por dimensión con valores
  `401` y `301` tras el debounce.
- Confirmar ausencia del error `addEventListener`.
- Repetir las 170 pruebas del tema auxiliar.
- Mantener documentadas las incidencias independientes.

## Aprobación requerida

Para modificar únicamente el tema auxiliar, responde exactamente:

`APROBADO LOTE MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2`

Esta aprobación no autoriza publicar el tema ni modificar el MAIN.

## Resultado ejecutado

- El listener delegado se almacenó con checksum
  `fc76e23f024cbda9ba30f40aec5c2c1e` y apareció en el HTML.
- Las pruebas de anchura, altura y teclado generaron 0 eventos.
- La prueba crítica falló; no se ejecutó la matriz completa.
- Reversión completada al checksum `7d6dfb8df5e4b9ef813eca32aaebc237`.
- Auxiliar `UNPUBLISHED`; MAIN intacto; ninguna publicación realizada.
