# MW-INDEXNOW-NOINDEX-HISTORIC-SUBMISSION-DECISION-013I6

Fecha: 2026-07-05  
Hora de registro: 12:24 Europe/Madrid  
Modo: solo lectura  
Estado final: `VERIFICADO Y CORRECTO`

## Objetivo

Definir la política operativa para URLs históricas enviadas a Bing/IndexNow que actualmente no son indexables, con foco en:

- `https://www.matchwalls.com/products/custom-file-uploader`

Esta URL apareció en el export de Bing Webmaster Tools como envío histórico de Shopify del 15 de junio de 2026.

## Documentos revisados

`VERIFICADO Y CORRECTO`

- `registro-cambios-ejecutados.md`
- `audit-MW-INDEXNOW-BING-WEBMASTER-SUBMITTED-URLS-AUDIT-013I5-2026-07-05.md`
- `monitor-MW-INDEXNOW-BING-WEBMASTER-DISCREPANCY-MONITOR-013I5C-2026-07-05.md`
- CSV recibido de Bing: `matchwalls.com_IndexNowSubmittedUrls_7_5_2026 AAAAAAAA.csv`

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

URL comprobada:

- `https://www.matchwalls.com/products/custom-file-uploader`

Resultado público actual:

- HTTP: `200`
- Canonical: `https://www.matchwalls.com/products/custom-file-uploader`
- Robots meta: `noindex,nofollow`
- Title: `Papel pintado y mural personalizado | MatchWalls`
- Sitemap productos ES: no contiene `custom-file-uploader`

## Interpretación

`VERIFICADO Y CORRECTO`

La URL fue enviada históricamente a IndexNow, pero el estado público actual comunica exclusión clara a buscadores:

- `noindex` indica que no debe indexarse;
- `nofollow` reduce la transmisión de señales desde esa URL;
- no aparece en el sitemap público de productos ES;
- no hay evidencia de que deba formar parte de una estrategia de captación orgánica.

Por tanto, no es un incidente crítico. Es una deuda histórica controlada.

## Decisión de política

`VERIFICADO Y CORRECTO`

Para URLs históricas ya enviadas por Shopify/IndexNow pero actualmente no indexables:

1. No reenviarlas manualmente.
2. No incluirlas en whitelists de IndexNow.
3. No intentar “borrarlas” de Bing si no hay evidencia de indexación activa.
4. Mantener el `noindex,nofollow` cuando la URL tenga función técnica, QA, personalización, subida de archivos o uso no editorial.
5. Mantenerlas fuera de sitemaps públicos siempre que no sean landings comerciales indexables.
6. Documentarlas como `VERIFICADO PERO MEJORABLE`, no como `RIESGO CRITICO`, salvo que aparezcan indexadas o citadas.

## Política para la app IndexNow

`VERIFICADO PERO MEJORABLE`

La app IndexNow puede enviar cambios automáticos de productos, colecciones, páginas y blogs. En este momento no se modifica su configuración.

Si en el futuro la app permite exclusiones por patrón o URL, conviene excluir:

- URLs con `noindex`.
- URLs técnicas o de carga/subida.
- URLs de prueba.
- URLs internas sin intención SEO.
- URLs de muestras cuando estén bajo política `noindex`.

No se recomienda desactivar envíos de productos globalmente solo por esta URL, porque eso podría perjudicar productos comerciales válidos.

## Acciones no recomendadas ahora

`VERIFICADO Y CORRECTO`

No hacer ahora:

- Envío manual de `custom-file-uploader`.
- Cambio de handle.
- Redirección.
- Eliminación.
- Cambio de `noindex`.
- Cambio de sitemap.
- Cambio masivo en la app IndexNow.
- Solicitud de retirada en Bing sin evidencia de indexación real.

## Riesgo residual

`VERIFICADO PERO MEJORABLE`

Riesgo bajo:

- Bing conoce la URL por un envío histórico.
- Si la rastrea, encontrará `noindex,nofollow`.
- No está en el sitemap de productos ES.

El riesgo aumentaría si:

- aparece indexada en Bing/Google;
- empieza a recibir impresiones orgánicas relevantes;
- la app la reenvía repetidamente por cambios técnicos;
- aparece citada por Copilot/IA;
- se elimina el `noindex` accidentalmente.

## Criterio de reactivación

Abrir lote específico solo si ocurre alguno de estos casos:

1. Bing o Google muestran la URL indexada.
2. La URL aparece en informes de impresiones/clics.
3. La app IndexNow la reenvía repetidamente.
4. La URL aparece citada en AI Performance/Copilot.
5. Se decide convertirla en una landing comercial indexable.

## Conclusión

`VERIFICADO Y CORRECTO`

La política queda definida:

- `custom-file-uploader` se acepta como envío histórico no prioritario.
- Se mantiene excluida de estrategia IndexNow manual.
- No se hace ninguna acción correctiva inmediata.
- Se monitoriza solo si aparece evidencia de indexación, impresión, cita o reenvío repetido.

## Próximo lote recomendado

`MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C-REVIEW`

Objetivo: retomar la política de bots/buscadores/IA con la capa Bing-Copilot ya activada y la app IndexNow funcionando.

Alternativa:

`MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J`

Objetivo: registrar línea base real de Bing Search Performance para futuras comparativas CEO/CMO.

