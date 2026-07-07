# Propuesta — MW-TECH-CUSTOMIZER-CONVERT-INCHES-010A5

Estado: `CORREGIDO Y VERIFICADO`.

## Alcance

- Tema auxiliar `178399019384`, `UNPUBLISHED`, `/t/46`.
- Único archivo: `assets/customizer.js`.
- MAIN y reversión excluidos.

## Evidencia y valor actual

- MD5 real: `2a26be9d6af37a992526274df431deaa`; 40768 bytes.
- `ProductCustomizer.connectedCallback()` llama una vez a
  `this.convertToInches()`, pero el método no existe.
- Error reproducido en 20/20 cargas de producto/cargador.
- Ocho versiones históricas revisadas desde 2024 contienen la llamada y no la
  implementación; no existe una versión histórica fiable para copiar.
- Borrar solo la llamada no es seguro: permitiría ejecutar inmediatamente
  `unitConverter()` con campos imperiales inicializados a cero.

## Cambio propuesto

Sustituir únicamente:

```javascript
this.convertToInches();
this.unitConverter();
```

por:

```javascript
if (typeof this.convertToInches === 'function') {
  this.convertToInches();
  this.unitConverter();
}
```

El guard conserva el estado inicial actualmente calculado y evita ejecutar la
conversión dependiente cuando el método no existe.

## Validación previa, riesgo y reversión

- Objetivo único localizado: 1; guard candidato: 1.
- Sintaxis JavaScript candidata: válida.
- MD5 candidato: `6684ed205824c8ba660bd4c67a5e26fc`; 40832 bytes.
- Riesgo: puede aparecer un fallo posterior hoy oculto por la excepción.
- Reversión: restaurar las dos llamadas y el MD5
  `2a26be9d6af37a992526274df431deaa`.

## QA obligatoria

- Medidas, superficie, cantidad, precio y variante antes/después.
- Producto y cargador × ES/EN/FR/DE/NL × escritorio/móvil: 20 pruebas.
- Consola sin `convertToInches` ni nuevos errores críticos.
- Después, matriz completa de 170 pruebas.
- Detener y revertir ante cualquier cambio comercial o funcional inesperado.

## Aprobación

`APROBADO LOTE MW-TECH-CUSTOMIZER-CONVERT-INCHES-010A5`

No autoriza publicar el tema ni modificar MAIN.

## Ejecución y verificación

- Aprobación exacta recibida.
- Shopify almacenó `assets/customizer.js` con cero `userErrors`.
- MD5 final `6684ed205824c8ba660bd4c67a5e26fc`; 40832 bytes.
- Tema `178399019384` continúa `UNPUBLISHED`; MAIN no modificado.
- Medidas y precio frente a MAIN: 400×300 cm, cantidad 12 y 402 €.
- QA específica: 20/20, sin errores nuevos.
- Matriz móvil: 85/85.
- Matriz escritorio: 85/85. Las 74 comprobaciones pendientes se repitieron en
  una sesión estable y fueron correctas.
- Resultado completo: 20/20 específicas y 170/170 de regresión.
- Errores nuevos `convertToInches` o `addEventListener`: 0.
