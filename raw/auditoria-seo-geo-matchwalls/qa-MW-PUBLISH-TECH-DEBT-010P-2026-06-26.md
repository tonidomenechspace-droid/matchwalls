# QA post-publicacion - MW-PUBLISH-TECH-DEBT-010P

Fecha: 2026-06-26 23:47:11 +02:00

## Estado del lote

`CORREGIDO Y VERIFICADO`

## Resultado ejecutivo

Se publico el tema tecnico QA `178399019384` como tema activo de Shopify.

El tema anterior `178396463480` quedo disponible en borradores con boton `Publish`, por lo que sigue siendo la reversion inmediata.

No se modificaron productos, precios, variantes, inventario, handles, redirecciones, canonicals, hreflang, GA4, GTM, Merchant Center ni apps.

## Preflight verificado

Antes de publicar:

- MAIN visual en Shopify Admin: `178396463480`.
- Nombre MAIN visual: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- Candidato visual en borradores: `178399019384`.
- Nombre candidato: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Boton `Publish` localizado unicamente sobre el candidato.
- Modal de confirmacion contenia el nombre del candidato.

Despues de publicar:

- Tema activo visual en Shopify Admin: `178399019384`.
- Nombre activo: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Tema `178396463480` visible en borradores con boton `Publish`.

## Verificacion publica inmediata

Home live ES mobile:

- URL: `https://www.matchwalls.com/`.
- H1: `Papeles pintados para paredes y murales`.
- Canonical: `https://www.matchwalls.com/`.
- `html lang`: `es`.
- `noindex`: `false`.
- Assets tema nuevo `/t/46`: presentes.
- Assets tema anterior `/t/45`: 0.
- Overflow: 0.

## Matriz publica 170 URLs

`CORREGIDO Y VERIFICADO`

- Total: 170/170.
- Metodo: lectura publica HTTP sobre las 17 paginas, 5 idiomas y desktop/mobile.
- Comprobado: HTTP 200, H1, canonical, `html lang`, hreflang prioritario ES/EN/FR/DE/NL, ausencia de `noindex`, contenido no vacio, ausencia de fuga CSS visible, assets `/t/46` presentes y `/t/45` ausentes.
- Hubo 2 timeouts SSL transitorios en primer intento; ambos se reintentaron y pasaron correctamente.

Matriz: `matriz-MW-PUBLISH-TECH-DEBT-010P-post-2026-06-26.csv`.

## Anexo tecnico en navegador real

Resultado funcional: `CORREGIDO Y VERIFICADO`.

Resultado de indexabilidad detectado en uploader: `VERIFICADO PERO MEJORABLE`.

Pruebas funcionales verificadas:

- Home ES mobile y desktop: correcto.
- Producto estandar ES mobile: correcto.
- Uploader ES/EN/FR/DE/NL mobile: correcto funcionalmente.
- Uploader FR/NL mobile 375 y 390: overflow 0.
- Uploader FR/NL desktop: overflow 0.
- Assets live: `/t/46` presentes y `/t/45` ausentes.
- Consola: 0 errores criticos en el alcance probado.
- Swatch tooltip mobile: `none`.
- Swatch tooltip desktop FR/NL: `block`.
- Medidas externas/internas: `423 x 223` sincronizadas.
- Tracking diagnostico `mwqa=010a2d`: marcador verificado con `data-mw010a2d-count=4` y ultimo evento `input_mural_outside` para `height=223`.

Matriz tecnica: `matriz-tecnica-MW-PUBLISH-TECH-DEBT-010P-post-2026-06-26.csv`.

## Incidencia no bloqueante detectada

`VERIFICADO PERO MEJORABLE`

Las URLs limpias del producto uploader tienen:

`meta robots="noindex,nofollow"`

Ejemplo verificado:

- `https://www.matchwalls.com/products/custom-file-uploader`
- Canonical: `https://www.matchwalls.com/products/custom-file-uploader`.
- H1: `Tu Mural Personalizado`.
- Assets `/t/46`: presentes.
- Assets `/t/45`: 0.
- Robots: `noindex,nofollow`.

Interpretacion:

- No hay evidencia de regresion visual o funcional causada por la publicacion.
- No se recomienda rollback por esta incidencia.
- Debe trasladarse al bloque de indexabilidad, porque requiere decision: si el uploader debe indexarse como URL comercial o mantenerse fuera del indice.

## Reversion disponible

Si se detectara un fallo critico posterior:

1. Abrir Shopify Admin > Online Store > Themes.
2. Publicar de nuevo el tema `178396463480`.
3. Confirmar que `178396463480` vuelve a `Active`.
4. Repetir prueba centinela live y matriz tecnica reducida.

## Decision sobre siguientes lotes

Continuar con:

1. Indexabilidad: incluir el caso `custom-file-uploader` con `noindex,nofollow`.
2. Clasificacion de 7.932 URLs.
3. Politica de muestras, colecciones geograficas y redirecciones.
4. Bing/Copilot, IndexNow, crawlers IA.
5. Entidad factual y schema.
