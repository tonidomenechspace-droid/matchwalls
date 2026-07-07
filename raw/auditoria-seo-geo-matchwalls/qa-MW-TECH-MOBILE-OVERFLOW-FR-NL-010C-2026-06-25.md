# QA — MW-TECH-MOBILE-OVERFLOW-FR-NL-010C

Fecha: 2026-06-25.

Estado final: `INCORRECTO`.

## Resultado ejecutivo

- Aprobación exacta recibida: `APROBADO LOTE MW-TECH-MOBILE-OVERFLOW-FR-NL-010C`.
- Tema afectado: auxiliar `178399019384`, `/t/46`, no publicado.
- Archivo afectado: `assets/theme.css`.
- MAIN no fue publicado ni modificado.
- El candidato aprobado se guardó en el auxiliar y se sirvió en preview.
- La prueba centinela falló: el overflow móvil FR/NL persistió.
- Se detuvo la matriz completa para no consumir pruebas sobre un candidato fallido.
- El bloque 010C fue revertido en el auxiliar.

## Evidencia del fallo

Con el candidato activo a viewport configurado de 390 px:

- FR `https://www.matchwalls.com/fr/pages/tout-sur-nos-peintures-murales`:
  - Recursos `/t/46`: 7.
  - `clientWidth`: 375.
  - `scrollWidth`: 408.
  - Overflow: 33 px.
  - Último enlace legal: `margin-right: 0px`.
  - H1 único y exacto.
  - Canonical propio, hreflang prioritarios, `html lang="fr"`, sin `noindex`.
  - Errores críticos de consola: 0.

- NL `https://www.matchwalls.com/nl/pages/onze-producten`:
  - Recursos `/t/46`: 7.
  - `clientWidth`: 375.
  - `scrollWidth`: 381.
  - Overflow: 6 px.
  - Último enlace legal: `margin-right: 0px`.
  - H1 único y exacto.
  - Canonical propio, hreflang prioritarios, `html lang="nl"`, sin `noindex`.
  - Errores críticos de consola: 0.

- Control ES `https://www.matchwalls.com/pages/papel-pintado-murales`:
  - Recursos `/t/46`: 7.
  - `clientWidth`: 375.
  - `scrollWidth`: 375.
  - Overflow: 0 px.

## Causa corregida parcialmente

`VERIFICADO PERO MEJORABLE`

- La regla aprobada sí hizo efecto sobre el último enlace legal:
  `margin-right: 0px`.
- Las reglas de `min-width: 0` y `overflow-wrap: anywhere` redujeron el caso NL
  de `+30 px` a `+6 px`.
- Sin embargo, el objetivo era `scrollWidth == clientWidth` en FR/NL, y no se
  alcanzó.

## Causa restante

`INCORRECTO`

- Los tres primeros `.custom-legal__item` conservaban `margin-right: 96px`.
- FR:
  - `.custom-legal__list`: `clientWidth 335`, `scrollWidth 388`.
  - El footer propagaba el overflow hasta `main` y documento: `+33 px`.
- NL:
  - `.custom-legal__list`: `clientWidth 335`, `scrollWidth 362`.
  - El footer propagaba el overflow hasta `main` y documento.
- La corrección de solo `:last-child` era insuficiente.

## Reversión ejecutada

`VERIFICADO Y CORRECTO`

- Se eliminó el bloque 010C del editor de código.
- Verificación previa a guardar:
  - `.custom-legal__item:last-child`: ausente.
  - `.shopify-section--multi-column .section-header > div`: ausente.
  - `.shopify-section--multi-column .collection-header`: ausente.
  - `.facade-wrapper`: presente.
  - Editor: `No Problems`.
- Reversión guardada en el auxiliar.
- Verificación preview tras reversión:
  - FR: último enlace legal `margin-right: 96px`, overflow `+33 px`.
  - NL `/nl/pages/onze-producten`: último enlace legal `margin-right: 96px`,
    overflow `+30 px`.
- No se publicó el tema.

## Limitaciones

`NO ACCESIBLE`

- En este turno no estuvo disponible un conector GraphQL/Shopify para leer
  checksum final del archivo. No se declara MD5 restaurado como verificado.
- La reversión queda verificada por editor de código y preview público `/t/46`.

## Decisión

`INCORRECTO`

El lote 010C queda ejecutado, fallido y revertido. Requiere un lote nuevo:
`MW-TECH-MOBILE-OVERFLOW-LEGAL-FLEX-010C2`.

