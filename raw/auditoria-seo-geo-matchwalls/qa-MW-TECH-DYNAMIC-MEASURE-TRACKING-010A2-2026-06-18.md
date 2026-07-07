# QA — MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2

Fecha: 2026-06-18 21:06 CEST.

Estado final: `INCORRECTO` — cambio revertido.

## Ejecución autorizada

- Aprobación exacta recibida:
  `APROBADO LOTE MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2`.
- Tema: `178399019384`, `/t/46`, `UNPUBLISHED`.
- Archivo único: `snippets/srolling_bar_menu.liquid`.
- Checksum previo: `7d6dfb8df5e4b9ef813eca32aaebc237`.
- Checksum experimental: `fc76e23f024cbda9ba30f40aec5c2c1e`.

## Prueba crítica

El listener delegado se almacenó y apareció en el HTML renderizado. Sin
embargo:

- Anchura `400→401`: 0 eventos `input_mural_outside`.
- Altura `300→301`: 0 eventos `input_mural_outside`.
- Repetición mediante teclado: 0 eventos.
- El campo interno sí cambió con el externo (`403→403`), por lo que la entrada
  y los listeners existentes sí recibieron el evento.

La hipótesis de que bastaba con delegar dentro del mismo callback
`DOMContentLoaded` queda refutada.

## Hallazgo adicional

La página de producto mantiene otra excepción:

`TypeError: Cannot read properties of null (reading 'addEventListener')`

La auditoría de selectores localizó el origen verificable en
`snippets/product-customizer.liquid`:

- `#customImage`: 0 elementos en el producto estándar.
- `fileInput.addEventListener('change', ...)`: llamada sin guarda.
- MD5 del archivo: `3878a24a9bb6cb134247ac6aff707a58`.

## Reversión

`CORREGIDO Y VERIFICADO`

- Restaurado el contenido previo de 010A.
- Checksum posterior: `7d6dfb8df5e4b9ef813eca32aaebc237`.
- Guardas 010A presentes; listener delegado ausente.
- Tema auxiliar sigue `UNPUBLISHED`, sin fallo de procesamiento.
- MAIN `178396463480` intacto, checksum
  `c254cf711a7706dc21ece2f2ad31acea`.

No se ejecutaron las 170 pruebas porque la prueba crítica inicial falló y el
cambio se revirtió antes de continuar.

