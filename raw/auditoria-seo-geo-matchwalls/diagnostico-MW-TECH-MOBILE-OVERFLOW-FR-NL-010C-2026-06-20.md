# Diagnóstico — MW-TECH-MOBILE-OVERFLOW-FR-NL-010C

Fecha: 2026-06-20.

Estado del diagnóstico: `VERIFICADO Y CORRECTO`.

Estado del problema: `INCORRECTO`.

## Estado real comprobado

- Tema auxiliar `178399019384`, `/t/46`, `UNPUBLISHED`.
- `assets/theme.css`: MD5 `89f4729809a0eaac75a764e0fc41888e`;
  241968 bytes.
- El archivo coincide exactamente en auxiliar, MAIN `178396463480`, reversión
  `178383749496` y copia local.
- No se modificó Shopify durante el diagnóstico.

## Cobertura reproducida

- Matriz: 85 URLs, 17 por cada idioma prioritario.
- A viewport configurado de 390 px, el navegador dispone de 375 px de ancho de
  contenido por la barra vertical.
- FR: 17/17 URLs con 33 px de overflow.
- NL: 17/17 URLs con overflow; 16 muestran 6 px y
  `/nl/pages/onze-producten` muestra 30 px.
- Controles ES, EN y DE: 0 px en páginas equivalentes.
- A viewport configurado de 375 px, ancho de contenido 360 px:
  - FR: 48 px.
  - NL general: 21 px.
  - NL «Nuestros productos»: 45 px.
  - Control ES: 0 px.

## Causa global del footer

Regla actual:

```css
.custom-legal__item {
  display: inline;
  margin-right: 6rem;
}
```

- Los cuatro elementos, incluido el último, reciben 96 px de margen derecho.
- Ancho útil de la lista legal a 390 px: 335 px.
- Scroll interno FR: 388 px; NL: 362 px.
- Los textos más largos FR/NL hacen que el margen residual del último elemento
  amplíe el documento.
- La causa se repite en las 34/34 URLs y reside en `assets/theme.css`, no en 34
  plantillas distintas.

## Causa adicional en NL «Nuestros productos»

- `Aanpassingsdiensten` se renderiza en `.collection-header` a 44 px.
- La palabra mide 385 px dentro de un `section-header` de 335 px.
- El elemento grid conserva su tamaño intrínseco y expande esa sección hasta
  405 px.
- El origen estructural está en el encabezado común de secciones
  `multi-column`; no es el H1 ni el cambio 010B.

## Elementos descartados como causa

- Carruseles con `overflow-x: auto` y el marquee del anuncio: desbordamiento
  interno intencional y recortado por su contenedor.
- Popup de cookies, chat, Product/Offer, H1, canonical y hreflang.
- 010B: el overflow coincide con su línea base anterior.

## Limitación de validación

`NO ACCESIBLE`

- El validador empaquetado de Theme Check no inicia porque falta
  `@shopify/theme-check-common`.
- No se declara validación Theme Check superada.
- La propuesta se apoya en métricas DOM reales, checksums Shopify, una
  sustitución CSS acotada y QA obligatoria posterior.
