# MW-CRAWLERS-HOME-500-HEADERS-RECHECK-013F1B

Fecha: 2026-07-05  
Hora de registro: 13:14 Europe/Madrid  
Modo: solo lectura  
Estado final: `RIESGO CRITICO`

## Objetivo

Añadir headers técnicos de respuestas `500` al paquete de soporte Shopify antes de enviar el ticket.

## Estado

`VERIFICADO Y CORRECTO`

Se realizó una nueva revalidación pública de la home:

`https://www.matchwalls.com/`

User-agents:

- Bingbot
- OAI-SearchBot
- PerplexityBot
- Googlebot
- Chrome

Muestra:

- Total solicitudes: 20
- Respuestas `200`: 6
- Respuestas `500`: 14
- Tasa de fallo observada: 70%

## Headers relevantes capturados

`VERIFICADO Y CORRECTO`

En las respuestas `500` se capturaron:

- `x-request-id`
- `cf-ray`
- `server: cloudflare`
- `content-type: text/html; charset=utf-8`
- `cache-control: private, no-store`
- `server-timing`
- `theme;desc="178399019384"`
- `pageType;desc="index"`
- `edge;desc="MAD"`
- `servedBy`
- `render;dur=...`

`x-shopify-stage` no apareció informado en las respuestas capturadas.

## Interpretación técnica

`RIESGO CRITICO`

La mejora confirma que el error no es solo por user-agent, ni por bloqueo WAF clásico.

Detalles clave:

- La home falla también con Chrome.
- Las respuestas `500` se sirven desde Cloudflare / edge `MAD`.
- Las respuestas `500` identifican el tema `178399019384` y `pageType=index`.
- Las respuestas `500` incluyen `render;dur` elevado y `cache-control: private, no-store`.
- Hay respuestas `200` y `500` en la misma URL, misma ventana temporal y mismo edge.
- Algunos `servedBy` fallan y otros pasan; no hay un único shard aislado en esta muestra.

Esto refuerza la hipótesis de incidencia de renderizado Storefront / infraestructura / interacción de render, no una política de `robots.txt` ni un bloqueo de bots.

## Ejemplos críticos

`VERIFICADO Y CORRECTO`

Bingbot `500`:

- `x-request-id`: `7d3b7d2d-fec8-45d5-8fe1-de787c4f25ee-1783249963`
- `cf-ray`: `a165efafee8a2183-MAD`
- `servedBy`: `mvhx`
- `render_ms`: `1524`

OAI-SearchBot `500`:

- `x-request-id`: `49062a87-3951-46e0-8cc6-f2d4c9cacd1e-1783249972`
- `cf-ray`: `a165efe70cec2183-MAD`
- `servedBy`: `jxcr`
- `render_ms`: `1419`

PerplexityBot `500`:

- `x-request-id`: `7269f21e-e073-45e4-8b77-70956861b834-1783249984`
- `cf-ray`: `a165f0323f842183-MAD`
- `servedBy`: `sdsh`
- `render_ms`: `1229`

Googlebot `500`:

- `x-request-id`: `6e430cb7-655e-4749-968d-4e4f0ea0c95c-1783249998`
- `cf-ray`: `a165f089cc712183-MAD`
- `servedBy`: `jw58`
- `render_ms`: `1195`

Chrome `500`:

- `x-request-id`: `a639dbfb-c1c6-4c41-bfa7-b5e143324282-1783250006`
- `cf-ray`: `a165f0bbfc662183-MAD`
- `servedBy`: `8p5v`
- `render_ms`: `1471`

## Conclusión

`RIESGO CRITICO`

El ticket a Shopify debe enviarse con el CSV de headers adjunto. La evidencia ya es suficiente para pedir escalación a Storefront Rendering / Infrastructure.

## Archivos generados

`VERIFICADO Y CORRECTO`

- `headers-MW-CRAWLERS-HOME-500-HEADERS-RECHECK-013F1B-2026-07-05.csv`
- `addendum-MW-CRAWLERS-HOME-500-HEADERS-RECHECK-013F1B-2026-07-05.md`
- `ticket-shopify-MW-CRAWLERS-HOME-500-SHOPIFY-INFRA-EVIDENCE-013F1B-2026-07-05.md`

## Próximo paso

Enviar a Shopify:

1. Ticket actualizado `013F1B`.
2. CSV de recheck `013F1`.
3. CSV de headers `013F1B`.

