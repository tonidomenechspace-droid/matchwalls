# Propuesta — MW-TECH-MOBILE-OVERFLOW-FR-NL-010C

Estado: `INCOMPLETO` — pendiente de aprobación.

## Alcance exacto

- Tema auxiliar `178399019384`, `UNPUBLISHED`, `/t/46`.
- Un único archivo: `assets/theme.css`.
- Impacto directo: footer móvil FR/NL y encabezados largos de secciones
  `multi-column`.
- QA obligatoria: ES, EN, FR, DE y NL.
- Excluidos: MAIN, reversión, publicación, textos, traducciones, handles,
  plantillas JSON y aplicaciones externas.

## Valor actual

- MD5 `89f4729809a0eaac75a764e0fc41888e`; 241968 bytes.
- `.custom-legal__item`: `margin-right: 6rem` también en el último elemento.
- Los grid items del encabezado no tienen `min-width: 0`.
- `.collection-header` no permite ruptura de palabras largas.

## Cambio propuesto

Añadir inmediatamente después de la regla legal actual:

```css
@media screen and (max-width: 699px) {
  .custom-legal__item:last-child {
    margin-right: 0;
  }

  .shopify-section--multi-column .section-header > div {
    min-width: 0;
  }

  .shopify-section--multi-column .collection-header {
    overflow-wrap: anywhere;
  }
}
```

No se propone ocultar overflow ni recortar contenido. El último margen deja de
contribuir al ancho y las palabras excepcionalmente largas pueden ajustarse
dentro del grid móvil.

## Candidato y respaldo

- Anclaje original localizado exactamente una vez.
- Fragmento: cinco llaves de apertura y cinco de cierre; una media query y una
  instancia de cada regla objetivo.
- MD5 candidato calculado: `0ff4bc0320305ef6cda965b1557b6e5f`.
- Tamaño candidato: 242238 bytes; incremento de 270 bytes.
- Respaldo: archivo Shopify actual con MD5
  `89f4729809a0eaac75a764e0fc41888e`.
- MAIN y reversión conservan copias idénticas del original.

## Riesgos y efectos secundarios

- El footer móvil puede cambiar mínimamente el salto de línea del último enlace
  legal.
- Un encabezado largo de una sección `multi-column` puede ocupar dos líneas en
  vez de ampliar el viewport.
- La media query limita el efecto a móvil; escritorio queda fuera.
- Riesgo de sintaxis global por editar un CSS común: se detendrá y revertirá si
  algún recurso `/t/46` no carga o cambia el diseño fuera de lo previsto.
- Theme Check continúa `NO ACCESIBLE`; no se ocultará esta limitación.

## Reversión exacta

1. Retirar únicamente el bloque de 270 bytes.
2. Confirmar MD5 `89f4729809a0eaac75a764e0fc41888e` y 241968 bytes.
3. Repetir las pruebas críticas.
4. Si no coincide, descartar el tema auxiliar. MAIN no se modifica.

## QA posterior obligatoria

- Matriz estándar: 85 URLs en escritorio y 85 a viewport móvil de 375 px:
  170 pruebas.
- Comprobación adicional: las 34 URLs FR/NL a viewport de 390 px.
- Total mínimo: 204 renders.
- Requisitos: `scrollWidth == clientWidth` en las 34 URLs FR/NL a ambos anchos;
  controles ES/EN/DE sin regresión.
- H1 exacto y único, canonical, cinco hreflang, idioma HTML, ausencia de
  `noindex`, contenido, recursos `/t/46` y consola sin errores críticos.
- Inspección visual del footer FR/NL y de `Aanpassingsdiensten`.
- Detener y revertir ante recorte, enlace legal inaccesible, cambio de escritorio
  o cualquier regresión comercial.

## Aprobación requerida

`APROBADO LOTE MW-TECH-MOBILE-OVERFLOW-FR-NL-010C`

Esta aprobación no autoriza publicar el tema ni modificar MAIN.
