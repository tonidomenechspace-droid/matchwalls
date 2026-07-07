# QA - MW-TECH-QA-FULL-REGRESSION-010Z3

Fecha: 2026-06-26 21:38:50 +02:00

## Estado

`VERIFICADO Y CORRECTO`

Regresión completa de solo lectura sobre el tema QA `178399019384`. No se modificó Shopify.

## Alcance

- Lote: `MW-TECH-QA-FULL-REGRESSION-010Z3`.
- Tipo: QA y diagnóstico de solo lectura.
- Matriz principal: 17 páginas × 5 idiomas × desktop/mobile = 170 pruebas.
- Idiomas: ES, EN, FR, DE y NL.
- Tema QA probado en navegador con preview: `178399019384`, assets `/t/46`.
- Live público sin sesión comprobado por HTTP limpio: home carga assets `/t/45` y 0 assets `/t/46`.

No se publicó, duplicó, renombró ni eliminó ningún tema. No se cambiaron productos, precios, variantes, inventario, handles, redirecciones, canonicals, hreflang, GA4, GTM, Merchant Center ni apps.

## Limitación de acceso

`NO ACCESIBLE` en este turno: Shopify CLI/Admin API. El comando `shopify` no estaba disponible en PATH, por lo que no se revalidaron roles de tema vía Admin API dentro de 010Z3.

Evidencia usada:

- Roles e IDs ya verificados en 010Z2: MAIN `178396463480` y QA `178399019384`.
- Estado público actual live: home sin sesión cargó `/t/45`, canonical home y 8 hreflang.
- Estado público actual QA: navegador con preview cargó `/t/46` y 0 `/t/45` en 170/170 pruebas.

## Resultado de la matriz principal

`CORREGIDO Y VERIFICADO`

- Total: 170/170.
- Desktop: 85/85.
- Mobile: 85/85.
- Tema QA `/t/46`: 170/170.
- Assets MAIN `/t/45`: 0/170.
- H1 esperado y único: 170/170.
- Canonical propio: 170/170.
- Hreflang prioritario ES/EN/FR/DE/NL: 170/170.
- `html lang`: 170/170.
- Sin `noindex`: 170/170.
- Contenido no vacío: 170/170.
- Overflow real: 0/170.
- CSS visible/rastreable no filtrado como texto: 0/170.
- Errores críticos de consola: 0/170.

Matriz: `matriz-MW-TECH-QA-FULL-REGRESSION-010Z3-2026-06-26.csv`.

## Anexo técnico

`CORREGIDO Y VERIFICADO`

Total: 13/13.

Incluye:

- Home ES mobile y desktop.
- Producto estándar ES mobile.
- Uploader ES/EN/FR/DE/NL mobile.
- Uploader FR/NL mobile 375.
- Uploader FR/NL desktop.
- Tracking `input_mural_outside` con marcador QA `mwqa=010a2d`.

Resultados:

- Assets QA `/t/46`: correctos.
- Assets MAIN `/t/45`: 0.
- Overflow real: 0.
- Consola: 0 errores.
- Swatch tooltip en mobile: `display:none`.
- Swatch tooltip en desktop FR/NL: `display:block`.
- Uploader sincronizado: `externalWidth=423`, `internalWidth=423`, `externalHeight=223`, `internalHeight=223`.
- Tracking: `data-mw010a2d-count=2`; último evento `input_mural_outside` para `height=223`.

Matriz técnica: `matriz-tecnica-MW-TECH-QA-FULL-REGRESSION-010Z3-2026-06-26.csv`.

## Incidencias

No se detectaron incidencias bloqueantes en el alcance probado.

Incidencia operativa no atribuible a la web:

- Durante el anexo técnico se perdió una pestaña del navegador interno. Se repitió el anexo con una pestaña nueva y preview QA recuperado. La repetición fue correcta.

## Cobertura no incluida

Estado: `INCOMPLETO` fuera del alcance de 010Z3.

No se probó checkout real, subida de archivo real, pago, creación de pedido, apps externas con datos reales, GA4, GTM, Search Console, Merchant Center, Bing Webmaster Tools ni CrUX.

## Conclusión

`VERIFICADO Y CORRECTO`.

El tema QA `178399019384` supera la matriz completa 170/170 y el anexo técnico 13/13. No hay evidencia de regresión crítica pendiente dentro del alcance técnico probado.

Siguiente paso recomendado: preparar propuesta formal de publicación/revisión final, sin ejecutar todavía ninguna publicación.
