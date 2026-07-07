# QA — MW-TECH-UPLOADER-OPENMODAL-GUARD-010A4

Fecha: 2026-06-18

Estado: `CORREGIDO Y VERIFICADO`

## Cambio verificado

- Tema auxiliar: `178399019384`, `/t/46`, `UNPUBLISHED`.
- Archivo: `snippets/product-customizer.liquid`.
- MD5: `d5a74ccb15b645eeb79e8c52f7c5a4ac`.
- Tamaño: `49230` bytes.
- Diferencia de 010A4: un único `?` adicional.
- El candidato calculado desde el respaldo produce el mismo MD5 y tamaño.
- MAIN y reversión mantienen MD5
  `3878a24a9bb6cb134247ac6aff707a58`.

## QA específica

`CORREGIDO Y VERIFICADO`

- Producto estándar y cargador en ES/EN/FR/DE/NL, escritorio y móvil: 20/20.
- Recursos servidos desde `/cdn/shop/t/46/`: 20/20.
- H1 único, contenido suficiente y ausencia de 404: 20/20.
- `#customImage`: 0/10 en producto estándar y 10/10 en cargador, esperado.
- Error `addEventListener`: 0/20.
- Error independiente `convertToInches`: reproducido en las 20 cargas; queda
  fuera de 010A4.

## Matriz completa

`CORREGIDO Y VERIFICADO`

- URLs: 85.
- Pruebas: 170, escritorio y móvil.
- Resultado crítico: 170/170.
- Verificado en cada prueba: `/t/46`, H1 exacto y único, canonical propio,
  cinco hreflang, idioma HTML, ausencia de `noindex`, contenido, ausencia de
  404 y ausencia de errores `addEventListener`.
- Fallos críticos: 0.

## Deudas independientes

`VERIFICADO PERO MEJORABLE`

- Desbordamiento móvil observado en 34/85 URLs: 17 FR y 17 NL.
- El recuento anterior era 33/85; la diferencia requiere análisis en el lote
  específico de overflow y no se atribuye a este guard.
- `convertToInches` requiere un sublote separado.

El tema continúa `UNPUBLISHED`.
