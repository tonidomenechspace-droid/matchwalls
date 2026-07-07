# Propuesta — MW-TECH-MOBILE-OVERFLOW-LEGAL-FLEX-010C2

Estado: `INCOMPLETO` — pendiente de aprobación exacta.

## Motivo

El lote `MW-TECH-MOBILE-OVERFLOW-FR-NL-010C` fue ejecutado, falló en QA
centinela y fue revertido. La causa confirmada es que retirar solo el margen del
último enlace legal no elimina el ancho residual del footer FR/NL.

## Alcance exacto

- Tema auxiliar `178399019384`, `UNPUBLISHED`, `/t/46`.
- Un único archivo: `assets/theme.css`.
- Impacto directo: footer legal móvil FR/NL y encabezados largos de secciones
  `multi-column`.
- Idiomas QA: ES, EN, FR, DE y NL.
- Excluidos: MAIN, publicación, textos, traducciones, URLs, handles, plantillas
  JSON, productos, precios, tracking y aplicaciones externas.

## Estado actual verificado

`INCORRECTO`

- 010C fue revertido.
- Preview `/t/46` tras reversión:
  - FR: `clientWidth 375`, `scrollWidth 408`, overflow `+33 px`.
  - NL `/nl/pages/onze-producten`: `clientWidth 375`, `scrollWidth 405`,
    overflow `+30 px`.
- Footer legal:
  - FR `.custom-legal__list`: `clientWidth 335`, `scrollWidth 388`.
  - NL `.custom-legal__list`: `clientWidth 335`, `scrollWidth 362`.
- Los elementos `.custom-legal__item` conservan `margin-right: 6rem`.
- El caso NL largo también necesita mantener las reglas de `min-width: 0` y
  `overflow-wrap: anywhere`, porque el candidato 010C redujo NL de `+30 px` a
  `+6 px` antes de revertirse.

## Cambio propuesto

Añadir una media query móvil, inmediatamente después de la regla actual:

```css
@media screen and (max-width: 699px) {
  .custom-legal__list {
    display: flex;
    flex-wrap: wrap;
    column-gap: 1.5rem;
    row-gap: 0.5rem;
    min-width: 0;
  }

  .custom-legal__item {
    margin-right: 0;
    min-width: 0;
    max-width: 100%;
    overflow-wrap: anywhere;
  }

  .shopify-section--multi-column .section-header > div {
    min-width: 0;
  }

  .shopify-section--multi-column .collection-header {
    overflow-wrap: anywhere;
  }
}
```

## Justificación técnica

- El footer legal no debe depender de márgenes horizontales de `6rem` en móvil.
- `flex-wrap` permite varias líneas sin expandir el documento.
- `column-gap` sustituye el margen rígido por separación controlada.
- `min-width: 0` y `overflow-wrap: anywhere` evitan que textos largos o palabras
  largas fuerce el ancho del grid.
- No se oculta overflow ni se recorta contenido.

## Riesgos

- El footer legal móvil puede cambiar su salto de línea visual.
- Los enlaces legales pueden ocupar más líneas en FR/NL, pero seguirán visibles.
- Si el gap resulta visualmente pobre, se ajustará en otro lote; no se improvisa.
- Theme Check sigue `NO ACCESIBLE` si el entorno mantiene la dependencia ausente.
- No se tocará escritorio por estar dentro de `max-width: 699px`.

## Respaldo y reversión

- Respaldo operativo: estado revertido actual del auxiliar tras 010C.
- Reversión exacta: retirar únicamente el bloque 010C2 añadido.
- Si la reversión no puede verificarse por checksum, se verificará por editor,
  DOM preview `/t/46` y ausencia de reglas 010C2.
- MAIN no se modifica; alternativa extrema: descartar el tema auxiliar.

## QA obligatoria

1. Prueba centinela antes de matriz completa:
   - FR mural a 390 px.
   - NL `/nl/pages/onze-producten` a 390 px.
   - ES control a 390 px.
2. Si pasa:
   - 34 URLs FR/NL a 390 px.
   - 34 URLs FR/NL a 375 px.
   - Controles ES/EN/DE equivalentes.
   - Matriz estándar 85 desktop + 85 mobile si no hay regresiones.
3. Criterios:
   - `scrollWidth == clientWidth` en FR/NL objetivo.
   - H1 único y exacto.
   - Canonical propio.
   - Hreflang prioritarios ES/EN/FR/DE/NL.
   - `html lang` correcto.
   - Sin `noindex`.
   - Recursos `/t/46` presentes.
   - Consola sin errores críticos nuevos.

## Aprobación requerida

`APROBADO LOTE MW-TECH-MOBILE-OVERFLOW-LEGAL-FLEX-010C2`

Esta aprobación no autoriza publicar el tema ni modificar MAIN.
