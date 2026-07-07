# QA — MW-TECH-JS-ADD-EVENT-LISTENER-010A

Fecha de cierre de pruebas: 2026-06-18 20:53 CEST.

Estado: `VERIFICADO PERO MEJORABLE`.

El cambio permanece en un tema `UNPUBLISHED`. No se ha publicado ni se ha
modificado el MAIN.

## Ejecución

- Aprobación exacta: `APROBADO LOTE MW-TECH-JS-ADD-EVENT-LISTENER-010A`.
- MAIN fuente: `178396463480`, `/t/45`.
- Tema auxiliar: `178399019384`, `/t/46`, rol `UNPUBLISHED`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Archivo único modificado: `snippets/srolling_bar_menu.liquid`.
- Checksum original: `c254cf711a7706dc21ece2f2ad31acea`.
- Checksum auxiliar: `7d6dfb8df5e4b9ef813eca32aaebc237`.
- El MAIN conserva el checksum original.

## Integridad del duplicado

El duplicado contiene 299 archivos frente a 306 del MAIN. Faltan siete salidas
generadas que conservan sus fuentes `.liquid`:

- `assets/checkmark.svg`
- `assets/country-flags.css`
- `assets/cursor-close.svg`
- `assets/cursor-zoom-in.svg`
- `assets/cursor-zoom-out.svg`
- `assets/sections.js`
- `assets/theme.js`

La vista previa `/t/46` genera y sirve estos recursos desde sus fuentes. No se
observaron errores de carga asociados. Entre los 299 archivos comunes, la única
diferencia posterior es el snippet autorizado.

## Matriz de 170 pruebas

Cobertura: 17 páginas × 5 idiomas × escritorio/móvil.

- Escritorio: 85/85 pruebas críticas correctas.
- Móvil: 85/85 pruebas críticas correctas.
- Tema `/t/46`: 170/170.
- H1 esperado: 170/170.
- Canonical propio: 170/170.
- Hreflang ES/EN/FR/DE/NL: 170/170.
- `html lang`: 170/170.
- Sin `noindex` accidental: 170/170.
- Contenido no vacío y sin 404: 170/170.
- Error `Cannot read properties of null (reading 'addEventListener')`: 0/170.

La primera pasada de escritorio se inició inmediatamente después de duplicar y
70 páginas no expusieron todavía el H1. La comparación directa MAIN/auxiliar y
la repetición completa de esas 70 páginas fueron correctas. Se clasifica como
propagación tardía del duplicado y no como pérdida persistente.

## Deuda independiente mantenida

`VERIFICADO PERO MEJORABLE`

- Overflow móvil: 33/85; FR 17, NL 16, resto 0.
- `SyntaxError: Unexpected token ','` permanece fuera del alcance.

## Prueba de tracking

`INCORRECTO`

- En el auxiliar, cambiar anchura `400→401` y altura `300→301` genera cero
  eventos `input_mural_outside`.
- La misma prueba en el MAIN original también genera cero eventos y reproduce
  la excepción original.
- Los campos aparecen después de `DOMContentLoaded`; las guardas evitan la
  excepción, pero los listeners directos no llegan a registrarse.
- No es una regresión introducida por 010A, pero impide declarar funcional el
  tracking previsto y bloquea la publicación del auxiliar.

## Resultado

La excepción global está corregida y verificada en `/t/46`, pero el criterio de
tracking funcional no se cumple. Se requiere un sublote separado con listener
delegado y nueva QA antes de proponer publicación.

