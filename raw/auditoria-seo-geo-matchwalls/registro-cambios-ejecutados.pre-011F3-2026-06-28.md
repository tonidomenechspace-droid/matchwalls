# 2026-06-28 15:25:00 +02:00 - Ejecución MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2

## Aprobación y alcance

`VERIFICADO PERO MEJORABLE`

- Aprobación exacta recibida: `APROBADO LOTE MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2`.
- Alcance aprobado: actualizar 2 targets de redirecciones Shopify Admin.
- No se eliminaron redirecciones.
- No se cambiaron handles, canonicals, páginas, colecciones, productos, temas ni contenido visible.

## Respaldo previo

`VERIFICADO Y CORRECTO`

- Archivo: `backup-pre-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.csv`.
- Valores originales registrados para las 4 redirecciones implicadas.

## Operación 1 - Medidas

`CORREGIDO Y VERIFICADO`

- ID: `gid://shopify/UrlRedirect/405088796899`.
- Path: `/pages/como-tomar-medidas-paredes-y-techos-boton`.
- Target anterior: `/pages/medidas-paredes-techos`.
- Target nuevo: `/pages/medidas-paredes`.
- Mutación: `urlRedirectUpdate`.
- Resultado Shopify: `userErrors: []`.
- Readback Admin confirmado.
- QA público confirmado: destino final `/pages/medidas-paredes`, canonical propio, H1 `Cómo tomar medidas de paredes`, sin meta robots `noindex` visible.

## Operación 2 - Colecciones

`INCOMPLETO`

- ID: `gid://shopify/UrlRedirect/410027000035`.
- Path: `/collections/papeles-pintados`.
- Target actual conservado: `/collections/papeles-pintados-old`.
- Target intentado: `/collections/murales`.
- Resultado Shopify: rechazado.
- Error: `Destino no puede redirigir a otro redireccionamiento`.
- No se modificó esta redirección.

## Causa verificada del bloqueo

`RIESGO CRITICO`

- Existe redirect Admin: `gid://shopify/UrlRedirect/1534386274680`, `/collections/murales` -> `/en/collections/all-matchwallsmurals-murals`.
- Shopify bloquea usar como target una ruta que es a su vez redirección.
- También existen rutas dependientes hacia `/collections/murales`:
  - `/collections/murales-mvp` -> `/collections/murales`.
  - `/collections/papeles-pintados-old` -> `/collections/murales`.
  - `/collections/%20papeles-pintados` -> `/collections/murales`.

## Verificación pública

`VERIFICADO PERO MEJORABLE`

- Archivo: `qa-publico-post-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.csv`.
- Medidas consolidado públicamente y verificado.
- Colecciones sigue funcionando públicamente hacia `/collections/murales`, pero Admin mantiene estructura conflictiva.
- Cabeceras HTTP exactas: `NO ACCESIBLE` desde PowerShell/curl en este entorno; navegador interno sí confirmó navegación final.

## Evidencia creada

- `ejecucion-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.md`.
- `backup-pre-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.csv`.
- `admin-post-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.csv`.
- `qa-publico-post-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.csv`.
- `shopify-blocker-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.csv`.

## Decisión de no revertir medidas

`VERIFICADO Y CORRECTO`

- No se revirtió la operación de medidas porque fue aceptada por Shopify, confirmada en Admin y verificada públicamente.
- El fallo de colecciones no afecta a la cadena de medidas.

## Reversión disponible

`VERIFICADO Y CORRECTO`

Si se decide revertir medidas, restaurar mediante `urlRedirectUpdate`:

- `gid://shopify/UrlRedirect/405088796899`: target `/pages/medidas-paredes-techos`.

## Siguiente paso recomendado

`REQUIERE DECISION HUMANA`

- Diagnóstico independiente recomendado: `MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEEP-CHAIN-DIAG-011F3`.
- Objetivo: resolver la estructura conflictiva de `/collections/murales` antes de proponer cambios en redirecciones de colecciones.

---
# 2026-06-28 15:14:00 +02:00 - Diagnóstico/propuesta MW-INDEXABILITY-REDIRECTS-CHAIN-PROPOSAL-011F1

## Tipo de trabajo

`VERIFICADO PERO MEJORABLE`

- Diagnóstico/propuesta de solo lectura sobre cadenas de redirección confirmadas en 011F.
- No se ejecutaron mutaciones.
- No se crearon, modificaron ni eliminaron redirecciones.
- No se tocaron handles, canonicals, productos, colecciones, páginas, temas ni configuración externa.

## Documentos y evidencias leídas

`VERIFICADO Y CORRECTO`

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `diagnostico-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.md`.
- `redirects-chain-evidence-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.csv`.

## Estado real Admin comprobado

`VERIFICADO Y CORRECTO`

- `gid://shopify/UrlRedirect/405088796899`: `/pages/como-tomar-medidas-paredes-y-techos-boton` -> `/pages/medidas-paredes-techos`.
- `gid://shopify/UrlRedirect/409984762083`: `/pages/medidas-paredes-techos` -> `/pages/medidas-paredes`.
- `gid://shopify/UrlRedirect/410027000035`: `/collections/papeles-pintados` -> `/collections/papeles-pintados-old`.
- `gid://shopify/UrlRedirect/417318207715`: `/collections/papeles-pintados-old` -> `/collections/murales`.
- `gid://shopify/UrlRedirect/412625207523`: `/pages/facade-variants/test` -> `/`.

## Verificación pública

`VERIFICADO PERO MEJORABLE`

- Navegador interno verificó destino final, canonical, title, H1 y ausencia visible de meta robots `noindex` en destino.
- `/pages/como-tomar-medidas-paredes-y-techos-boton` acaba en `/pages/medidas-paredes`.
- `/pages/medidas-paredes-techos` acaba en `/pages/medidas-paredes`.
- `/collections/papeles-pintados` acaba en `/collections/murales`.
- `/collections/papeles-pintados-old` acaba en `/collections/murales`.
- `/pages/facade-variants/test` acaba en `/`.
- Cabeceras HTTP exactas públicas: `NO ACCESIBLE` desde PowerShell/curl en este entorno; navegador sí confirmó navegación final.

## Propuesta creada

`REQUIERE DECISION HUMANA`

- Archivo: `propuesta-lote-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.md`.
- Lote propuesto: `MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2`.
- Alcance propuesto: actualizar solo dos targets.
- No se propone borrar redirecciones intermedias.
- `facade` queda fuera de alcance y en revisión posterior.

## Mutaciones validadas pero no ejecutadas

`VERIFICADO Y CORRECTO`

- `urlRedirectUpdate` validada contra schema Shopify Admin.
- `urlRedirectDelete` validada contra schema Shopify Admin solo para confirmar disponibilidad, pero no recomendada para 011F2.

## Evidencia creada

- `diagnostico-MW-INDEXABILITY-REDIRECTS-CHAIN-PROPOSAL-011F1-2026-06-28.md`.
- `qa-publico-MW-INDEXABILITY-REDIRECTS-CHAIN-PROPOSAL-011F1-2026-06-28.csv`.
- `propuesta-lote-MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2-2026-06-28.md`.

## Siguiente paso recomendado

`REQUIERE DECISION HUMANA`

Ejecutar solo si Daniel aprueba exactamente:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-CHAIN-CONSOLIDATION-011F2`

---
# 2026-06-28 15:05:00 +02:00 - Diagnóstico MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F

## Tipo de trabajo

`INCOMPLETO`

- Diagnóstico de solo lectura sobre redirecciones Shopify Admin.
- No se ejecutaron mutaciones.
- No se crearon, modificaron ni eliminaron redirecciones.
- No se tocaron handles, canonicals, productos, colecciones, páginas, temas ni configuración externa.

## Documentos y evidencias leídas

`VERIFICADO Y CORRECTO`

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `redirects-risk-summary-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.md`.
- Evidencias de 011C, 011D, 011E y 011E1.

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

- Conteo actual Shopify Admin GraphQL: 635 redirecciones.
- Precisión: `EXACT`.
- Schema `UrlRedirect` verificado: campos disponibles `id`, `path`, `target`.
- Query Admin GraphQL validada antes de ejecutar.
- Primer bloque exportado: 50 redirecciones.
- Export completo de 635 filas: `INCOMPLETO` en esta sesión porque no hay operación directa de export a archivo y la transcripción manual paginada no es suficientemente fiable.

## Conteos de riesgo verificados

`VERIFICADO PERO MEJORABLE`

- `matchwallsmurals`: 334.
- `matchwallswallpapers`: 44.
- `facade`: 1.
- `black-friday`: 0.
- `matchalls`: 0.
- `norid`: 0.
- `enchathed`: 0.
- `muestra`: 6.
- `copy`: 6.
- `copia`: 12.
- `old`: 2.

## Cadenas confirmadas

`RIESGO CRITICO`

- Cadena medidas:
  - `/pages/como-tomar-medidas-paredes-y-techos-boton` -> `/pages/medidas-paredes-techos`.
  - `/pages/medidas-paredes-techos` -> `/pages/medidas-paredes`.
- Cadena colecciones:
  - `/collections/papeles-pintados` -> `/collections/papeles-pintados-old`.
  - `/collections/papeles-pintados-old` -> `/collections/murales`.
- Redirección legacy de prueba:
  - `/pages/facade-variants/test` -> `/`.

## Limitaciones

`INCOMPLETO`

- No se ha generado export completo local de 635 filas.
- No se ha ejecutado validación pública masiva de destinos.
- No se ha cruzado el 100% de redirects con sitemap, Search Console ni analytics.
- Los filtros `path:` de Shopify se registran como conteos Admin, no como clasificación semántica completa.

## Evidencia creada

- `diagnostico-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.md`.
- `redirects-counts-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.csv`.
- `redirects-risk-samples-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.csv`.
- `redirects-chain-evidence-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.csv`.
- `redirects-export-first50-MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F-2026-06-28.csv`.

## Incidencias de entorno

`VERIFICADO PERO MEJORABLE`

- Quedó un archivo temporal de prueba de escritura: `_sandbox_write_test_011f.tmp`.
- No forma parte de la evidencia SEO/GEO del lote.

## Siguiente paso recomendado

`REQUIERE DECISION HUMANA`

- Siguiente diagnóstico/propuesta: `MW-INDEXABILITY-REDIRECTS-CHAIN-PROPOSAL-011F1`.
- Objetivo: validar destinos finales y preparar propuesta de consolidación solo para las dos cadenas confirmadas.
- No ejecutar cambios de redirección sin lote formal y aprobación exacta.

---
# 2026-06-27 11:49:20 +02:00 - Ejecucion MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1

## AprobaciÃ³n y alcance

`CORREGIDO Y VERIFICADO`

- AprobaciÃ³n exacta recibida: `APROBADO LOTE MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1`.
- Alcance: piloto reversible de noindex sobre 6 colecciones geogrÃ¡ficas no estratÃ©gicas.
- No se modificaron handles.
- No se modificaron redirecciones.
- No se modificaron productos, precios, inventario, contenido visible, tema, navegaciÃ³n, traducciones ni canonicals manuales.

## Recursos modificados

`CORREGIDO Y VERIFICADO`

- `gid://shopify/Collection/443626914019` â€” `comprar-papel-pintado-alava`.
- `gid://shopify/Collection/646109593976` â€” `comprar-papel-pintado-albacete`.
- `gid://shopify/Collection/646109626744` â€” `comprar-papel-pintado-alicante`.
- `gid://shopify/Collection/646109659512` â€” `comprar-papel-pintado-almeria`.
- `gid://shopify/Collection/646109757816` â€” `comprar-papel-pintado-badajoz`.
- `gid://shopify/Collection/646109856120` â€” `comprar-papel-pintado-burgos`.

## Respaldo previo

`VERIFICADO Y CORRECTO`

- Archivo: `backup-pre-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- Valor previo: `seo.hidden = null` en 6/6.
- `productsCount = 73` en 6/6.
- `resourcePublicationsCount = 9` en 6/6.

## OperaciÃ³n ejecutada

`CORREGIDO Y VERIFICADO`

- MutaciÃ³n Admin GraphQL validada: `metafieldsSet`.
- Namespace `seo`.
- Key `hidden`.
- Type `number_integer`.
- Value `1`.
- Resultado Shopify: `userErrors: []`.

Metafields creados:

- `gid://shopify/Metafield/198966948921720` â€” Ãlava.
- `gid://shopify/Metafield/198966948954488` â€” Albacete.
- `gid://shopify/Metafield/198966948987256` â€” Alicante.
- `gid://shopify/Metafield/198966949020024` â€” AlmerÃ­a.
- `gid://shopify/Metafield/198966949052792` â€” Badajoz.
- `gid://shopify/Metafield/198966949085560` â€” Burgos.

## VerificaciÃ³n Admin

`CORREGIDO Y VERIFICADO`

- Archivo: `admin-post-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- 6/6 colecciones con `seo.hidden = 1`.
- Type `number_integer`.
- UpdatedAt postcambio: `2026-06-27T09:45:49Z`.

## VerificaciÃ³n pÃºblica

`CORREGIDO Y VERIFICADO`

- Archivo: `qa-publico-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- 36/36 URLs localizadas responden 200.
- 36/36 URLs tienen robots `noindex,nofollow`.
- Las pÃ¡ginas siguen accesibles directamente; no se eliminaron ni redirigieron.

DistribuciÃ³n pÃºblica verificada:

- ES 6.
- EN 6.
- FR 5.
- DE 5.
- NL 6.
- PT 6.
- IT 2.

## VerificaciÃ³n sitemap

`CORREGIDO Y VERIFICADO`

- Archivo: `qa-sitemap-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- 36/36 URLs afectadas ausentes de sitemap.
- Los sitemaps de colecciones revisados pasan de 106 a 100 URLs cada uno.
- Archivo adicional: `qa-sitemap-geo-restante-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- GeogrÃ¡ficas candidatas restantes en sitemap: 310.
  - ES 52.
  - EN 50.
  - FR 51.
  - DE 36.
  - NL 46.
  - PT 49.
  - IT 26.

## MÃ©todo de reversiÃ³n

`VERIFICADO Y CORRECTO`

Eliminar los 6 metafields creados en este lote:

- `gid://shopify/Metafield/198966948921720`.
- `gid://shopify/Metafield/198966948954488`.
- `gid://shopify/Metafield/198966948987256`.
- `gid://shopify/Metafield/198966949020024`.
- `gid://shopify/Metafield/198966949052792`.
- `gid://shopify/Metafield/198966949085560`.

Verificaciones tras reversiÃ³n:

1. Admin: `seo.hidden = null`.
2. PÃºblico: ausencia de robots `noindex`.
3. Sitemap: reapariciÃ³n tras regeneraciÃ³n/cachÃ© si Shopify lo permite.

## Evidencia

- EjecuciÃ³n: `ejecucion-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.md`.
- DiagnÃ³stico base: `diagnostico-MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E-2026-06-27.md`.
- Propuesta: `propuesta-lote-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.md`.
- Respaldo previo: `backup-pre-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- Admin postcambio: `admin-post-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- QA pÃºblico: `qa-publico-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- QA sitemap: `qa-sitemap-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.
- Resumen QA: `qa-summary-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.txt`.
- Geo restante: `qa-sitemap-geo-restante-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.csv`.

---

# 2026-06-27 11:41:22 +02:00 - Diagnostico MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E

## Tipo de trabajo

`REQUIERE DECISION HUMANA`

- DiagnÃ³stico de solo lectura sobre colecciones geogrÃ¡ficas detectadas en sitemap.
- No se ejecutaron mutaciones.
- No se modificaron colecciones, handles, redirecciones, traducciones, productos, temas, canonicals ni metafields.

## Documentos y evidencias leÃ­das

`VERIFICADO Y CORRECTO`

- `geo-collections-candidates-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`.
- `classification-master-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`.
- `registro-cambios-ejecutados.md`.
- Sitemaps actuales de colecciones ES, EN, FR, DE, NL, IT y PT.
- Muestra pÃºblica controlada de 28 URLs.
- Muestra Admin GraphQL de colecciones geogrÃ¡ficas.

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

- 346 URLs geogrÃ¡ficas siguen presentes actualmente en sitemap:
  - ES 58;
  - EN 56;
  - FR 56;
  - NL 52;
  - DE 41;
  - PT 55;
  - IT 28.
- Cada sitemap de colecciones revisado responde 200 y contiene 106 URLs.
- 0/346 URLs candidatas han salido de sitemap por cambios previos.
- La muestra pÃºblica 28/28 responde 200, sin `noindex` y con canonical self.
- La muestra Admin confirma colecciones reales publicadas, `seo.hidden=null`, 73 productos exactos y primeros productos idÃ©nticos.

## Riesgo

`RIESGO CRITICO`

- Las pÃ¡ginas geogrÃ¡ficas son elegibles para buscadores y sistemas IA, pero muestran patrÃ³n masivo/repetitivo.
- Se detectan seÃ±ales de doorway/geolocalizaciÃ³n artificial: misma fecha, mismo surtido inicial, traducciones irregulares, handles localizados con sufijos y bajo valor diferencial.
- No hay acceso verificado a Search Console, GA4, ventas por URL ni Bing Webmaster Tools en este lote.

## DecisiÃ³n recomendada

`REQUIERE DECISION HUMANA`

- No cambiar handles ni redirecciones.
- No eliminar colecciones.
- Mantener en `STANDBY` ciudades estratÃ©gicas como Madrid, Barcelona, ParÃ­s, Toulouse y similares hasta disponer de criterio editorial/comercial.
- Ejecutar piloto reversible de noindex en 6 colecciones geogrÃ¡ficas no estratÃ©gicas:
  - `comprar-papel-pintado-alava`;
  - `comprar-papel-pintado-albacete`;
  - `comprar-papel-pintado-alicante`;
  - `comprar-papel-pintado-almeria`;
  - `comprar-papel-pintado-badajoz`;
  - `comprar-papel-pintado-burgos`.

## Evidencia creada

- `diagnostico-MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E-2026-06-27.md`.
- `qa-publico-muestra-MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E-2026-06-27.csv`.
- `qa-sitemap-geo-MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E-2026-06-27.csv`.
- `admin-muestra-MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E-2026-06-27.csv`.
- `propuesta-lote-MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1-2026-06-27.md`.

## AprobaciÃ³n requerida para ejecutar el siguiente lote

`APROBADO LOTE MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1`

---

# 2026-06-27 11:15:36 +02:00 - Ejecucion MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1

## Aprobacion y alcance

`CORREGIDO Y VERIFICADO`

- Aprobacion exacta recibida: `APROBADO LOTE MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1`.
- Recurso modificado: colecciÃ³n `gid://shopify/Collection/646234440056`.
- Legacy ID: `646234440056`.
- TÃ­tulo base: `Papel Pintado Black Friday`.
- Handle base: `papel-pintado-black-friday`.
- Template suffix: `black-friday`.
- Alcance: aplicar noindex reversible a la landing Black Friday obsoleta mediante `seo.hidden=1`.
- No se modificaron handles.
- No se modificaron redirecciones.
- No se modificaron plantilla, traducciones, productos, navegaciÃ³n, precios, inventario ni contenido visible.

## Respaldo previo

`VERIFICADO Y CORRECTO`

- Archivo: `backup-pre-MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1-2026-06-27.csv`.
- Valor previo:
  - `seo.hidden`: `null`.
- Valores de control:
  - updatedAt previo: `2026-04-20T15:23:00Z`;
  - productsCount Admin: `0`;
  - templateSuffix: `black-friday`.

## Operacion ejecutada

`CORREGIDO Y VERIFICADO`

- MutaciÃ³n: `metafieldsSet`.
- Owner:
  - `gid://shopify/Collection/646234440056`.
- Metafield creado:
  - namespace: `seo`;
  - key: `hidden`;
  - type: `number_integer`;
  - value: `1`.
- Resultado Shopify:
  - metafield ID: `gid://shopify/Metafield/198966658466168`;
  - owner typename: `Collection`;
  - `userErrors`: `[]`.

## Verificacion Admin

`CORREGIDO Y VERIFICADO`

- Archivo: `admin-post-MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1-2026-06-27.csv`.
- Valor postcambio:
  - `seo.hidden = 1`;
  - type `number_integer`;
  - updatedAt colecciÃ³n `2026-06-27T09:13:45Z`.

## Verificacion publica

`CORREGIDO Y VERIFICADO`

- Archivo: `qa-publico-MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1-2026-06-27.csv`.
- Resultado:
  - 7/7 URLs responden 200;
  - 7/7 URLs tienen robots `noindex,nofollow`;
  - 7/7 URLs siguen accesibles directamente, como estaba previsto.
- URLs verificadas:
  - ES `https://www.matchwalls.com/collections/papel-pintado-black-friday`;
  - EN `https://www.matchwalls.com/en/collections/wallpapers-black-friday`;
  - FR `https://www.matchwalls.com/fr/collections/papiers-peints-black-friday`;
  - NL `https://www.matchwalls.com/nl/collections/black-friday-wallpaper`;
  - IT `https://www.matchwalls.com/it/collections/sfondi-del-black-friday`;
  - DE `https://www.matchwalls.com/de/collections/schwarzer-freitag-wallpaper`;
  - PT `https://www.matchwalls.com/pt/collections/papel-de-parede-de-sexta-feira-negra`.

## Verificacion sitemap

`CORREGIDO Y VERIFICADO`

- Archivo: `qa-sitemap-MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1-2026-06-27.csv`.
- Resultado:
  - 7/7 URLs ausentes de sitemap tras el cambio.

## Metodo de reversion

`VERIFICADO Y CORRECTO`

Para revertir:

- Ejecutar `metafieldsDelete`.
- Identificador:
  - ownerId: `gid://shopify/Collection/646234440056`;
  - namespace: `seo`;
  - key: `hidden`.
- MutaciÃ³n de rollback validada en la fase 011D.
- Esto elimina el noindex y permite que Shopify vuelva a incluir la colecciÃ³n en indexaciÃ³n/sitemap si sigue publicada.

## Evidencia

- Propuesta: `propuesta-lote-MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1-2026-06-27.md`.
- DiagnÃ³stico base: `diagnostico-MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D-2026-06-27.md`.
- Respaldo previo: `backup-pre-MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1-2026-06-27.csv`.
- Admin postcambio: `admin-post-MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1-2026-06-27.csv`.
- QA pÃºblico: `qa-publico-MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1-2026-06-27.csv`.
- QA sitemap: `qa-sitemap-MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1-2026-06-27.csv`.
- Resumen QA: `qa-summary-MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1-2026-06-27.txt`.

---

# 2026-06-27 01:52:31 +02:00 - Diagnostico MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D

## Tipo de trabajo

`REQUIERE DECISION HUMANA`

- Diagnostico y propuesta de decision.
- No se modifico Shopify.
- No se ejecutaron mutaciones.
- No se cambiaron colecciones, handles, redirecciones, plantillas, productos ni traducciones.

## Alcance

`INCORRECTO`

- Revisar la landing Black Friday detectada en indexabilidad.
- El inventario 011C habia detectado 5 URLs por patron `black-friday`.
- El diagnostico 011D amplia la cobertura real a 7 URLs porque DE y PT usan handles traducidos.

## Recurso Shopify real

`VERIFICADO PERO MEJORABLE`

- Tipo: `Collection`.
- ID: `gid://shopify/Collection/646234440056`.
- Legacy ID: `646234440056`.
- Titulo base: `Papel Pintado Black Friday`.
- Handle base: `papel-pintado-black-friday`.
- Template suffix: `black-friday`.
- UpdatedAt: `2026-04-20T15:23:00Z`.
- ProductsCount Admin: `0`.
- Publicaciones: `9`.
- `seo.hidden`: `null`.

## Estado publico verificado

`INCORRECTO`

- 7/7 URLs responden 200.
- 7/7 URLs estan en sitemap.
- 7/7 URLs son indexables.
- 7/7 URLs tienen canonical self.
- 7/7 contienen seÃ±ales obsoletas:
  - `Black Friday 2024`;
  - contador a `Nov 29, 2024`;
  - mensaje `La oferta ha finalizado`.
- EN mezcla meta title 2025 con H1 2024.
- FR contiene traduccion `body_html` no relacionada: `Acheter du papier peint Toulouse - MatchWalls`.

## Redirecciones

`VERIFICADO PERO MEJORABLE`

- Busqueda Admin `black-friday`: 0 redirecciones.
- Busqueda Admin `black`: 2 redirecciones no relacionadas con estas URLs.

## Decision recomendada

`REQUIERE DECISION HUMANA`

- No borrar.
- No redirigir todavia.
- No cambiar handles.
- No tocar plantilla ni traducciones en este lote.
- Recomendacion: ejecutar lote separado `MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1`.
- Accion propuesta 011D1: crear `seo.hidden=1` en `gid://shopify/Collection/646234440056`.

## Mutaciones validadas pero no ejecutadas

`VERIFICADO Y CORRECTO`

- `metafieldsSet` para aplicar `seo.hidden=1`.
- `metafieldsDelete` para rollback eliminando `seo.hidden`.

## Evidencia creada

- `diagnostico-MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D-2026-06-27.md`
- `diagnostico-admin-MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D-2026-06-27.csv`
- `diagnostico-publico-MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D-2026-06-27.csv`
- `diagnostico-sitemap-MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D-2026-06-27.csv`
- `diagnostico-publico-ampliado-MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D-2026-06-27.csv`
- `diagnostico-sitemap-ampliado-MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D-2026-06-27.csv`
- `propuesta-lote-MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1-2026-06-27.md`

## Aprobacion requerida para ejecutar

`APROBADO LOTE MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1`

---

# 2026-06-27 01:44:40 +02:00 - Ejecucion MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1

## Aprobacion y alcance

`CORREGIDO Y VERIFICADO`

- Aprobacion exacta recibida: `APROBADO LOTE MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1`.
- Recurso modificado: metaobject `gid://shopify/Metaobject/65268613347`.
- Type: `facade_variants`.
- Handle: `test`.
- Display name: `Test`.
- Alcance: retirar de sitemap las URLs de prueba `facade-variants/test` pasando el metaobject de `ACTIVE` a `DRAFT`.
- No se modificaron redirecciones.
- No se modificaron handles.
- No se modificaron temas.
- No se modificaron productos, colecciones, paginas normales, precios, inventario, canonicals ni hreflang.

## Respaldo previo

`VERIFICADO Y CORRECTO`

- Archivo: `backup-pre-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`.
- Valores previos:
  - `publishable.status`: `ACTIVE`.
  - `onlineStore.templateSuffix`: `null`.
  - `fields.opts`: `["gid://shopify/Product/8277681733859","gid://shopify/Product/8277681832163","gid://shopify/Product/8308962623715"]`.
  - `updatedAt`: `2024-11-20T16:57:46Z`.

## Operacion ejecutada

`CORREGIDO Y VERIFICADO`

- Mutacion: `metaobjectUpdate`.
- Campo modificado:
  - `capabilities.publishable.status`: `ACTIVE` -> `DRAFT`.
- Resultado Shopify:
  - `userErrors`: `[]`.
  - Metaobject devuelto con `publishable.status = DRAFT`.

## Verificacion Admin

`CORREGIDO Y VERIFICADO`

- Archivo: `admin-post-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`.
- Metaobject postcambio:
  - ID `gid://shopify/Metaobject/65268613347`.
  - type `facade_variants`.
  - handle `test`.
  - displayName `Test`.
  - updatedAt `2026-06-26T23:43:38Z`.
  - `publishable.status`: `DRAFT`.
  - `onlineStore.templateSuffix`: `null`.
  - campo `opts` conservado.

## Verificacion publica

`CORREGIDO Y VERIFICADO`

- Archivo: `qa-publico-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`.
- Resultado: 7/7 URLs responden 301 a home localizada.
- Esto se acepta porque la redireccion existente no formaba parte del lote y se dejo intacta.

## Verificacion sitemap

`CORREGIDO Y VERIFICADO`

- Archivo: `qa-sitemap-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`.
- Resultado: 7/7 URLs retiradas de sus sitemaps localizados.
- Sitemaps revisados:
  - `https://www.matchwalls.com/sitemap_metaobject_pages_1.xml`
  - `https://www.matchwalls.com/en/sitemap_metaobject_pages_1.xml`
  - `https://www.matchwalls.com/fr/sitemap_metaobject_pages_1.xml`
  - `https://www.matchwalls.com/de/sitemap_metaobject_pages_1.xml`
  - `https://www.matchwalls.com/nl/sitemap_metaobject_pages_1.xml`
  - `https://www.matchwalls.com/it/sitemap_metaobject_pages_1.xml`
  - `https://www.matchwalls.com/pt/sitemap_metaobject_pages_1.xml`

## Metodo de reversion

`VERIFICADO Y CORRECTO`

Si se requiere revertir:

- Ejecutar `metaobjectUpdate` sobre `gid://shopify/Metaobject/65268613347`.
- Cambiar `capabilities.publishable.status`: `DRAFT` -> `ACTIVE`.
- No hay que recrear campos ni URLs.
- Valores originales documentados en `backup-pre-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`.

## Evidencia

- Propuesta: `propuesta-lote-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.md`.
- Diagnostico Admin previo: `diagnostico-admin-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`.
- Diagnostico publico previo: `diagnostico-publico-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`.
- Diagnostico sitemap previo: `diagnostico-sitemap-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`.
- Respaldo previo: `backup-pre-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`.
- Admin postcambio: `admin-post-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`.
- QA publico: `qa-publico-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`.
- QA sitemap: `qa-sitemap-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`.
- Resumen QA: `qa-summary-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.txt`.

---

# 2026-06-27 01:41:14 +02:00 - Propuesta MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1

## Tipo de trabajo

`REQUIERE DECISION HUMANA`

- Propuesta formal creada.
- No se modifico Shopify.
- No se ejecuto la mutacion validada.

## Alcance propuesto

`INCORRECTO`

- Limpiar 7 URLs de prueba `facade-variants/test` presentes en sitemaps metaobject localizados.
- Recurso real identificado: metaobject `gid://shopify/Metaobject/65268613347`.
- Type: `facade_variants`.
- Handle: `test`.
- Display name: `Test`.
- Estado actual: `ACTIVE`.

## Evidencia verificada

`VERIFICADO PERO MEJORABLE`

- No existe como Page normal: consulta `pages(query:"facade")` sin resultados.
- Existe como metaobject:
  - definicion `gid://shopify/MetaobjectDefinition/1111458019`;
  - name `Facade variants`;
  - type `facade_variants`;
  - metaobjectsCount `1`;
  - onlineStore enabled `true`;
  - publishable enabled `true`.
- Metaobject:
  - ID `gid://shopify/Metaobject/65268613347`;
  - handle `test`;
  - displayName `Test`;
  - publishable.status `ACTIVE`;
  - updatedAt `2024-11-20T16:57:46Z`;
  - field `opts` con 3 productos referenciados.
- Las 7 URLs estan presentes en sitemap.
- Las 7 URLs responden 301 a home localizada.
- Redireccion Admin existente:
  - `gid://shopify/UrlRedirect/412625207523`;
  - path `/pages/facade-variants/test`;
  - target `/`.

## Cambio propuesto

`REQUIERE DECISION HUMANA`

- Ejecutar `metaobjectUpdate` solo sobre `gid://shopify/Metaobject/65268613347`.
- Cambiar `capabilities.publishable.status` de `ACTIVE` a `DRAFT`.
- No tocar handle, campos, definicion, redireccion, temas, productos ni colecciones.

## Mutacion

`VERIFICADO Y CORRECTO`

- Mutacion `metaobjectUpdate` validada contra schema Admin GraphQL.
- Requiere scopes `write_metaobjects`, `read_metaobjects`.
- No ejecutada.

## Evidencia creada

- `propuesta-lote-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.md`
- `diagnostico-admin-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`
- `diagnostico-publico-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`
- `diagnostico-sitemap-MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1-2026-06-27.csv`

## Aprobacion requerida

`APROBADO LOTE MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1`

---

# 2026-06-27 01:33:52 +02:00 - Diagnostico MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C

## Tipo de trabajo

`INCOMPLETO`

- Diagnostico de solo lectura.
- No se modifico Shopify.
- No se ejecutaron mutaciones.
- No se cambiaron productos, colecciones, paginas, handles, redirecciones, canonicals, temas, apps ni configuraciones externas.

## Alcance

`VERIFICADO PERO MEJORABLE`

- Clasificacion de indexabilidad restante tras los lotes 011B4, 011B5 y 011B5B.
- Comparacion del sitemap actual contra el inventario 011A.
- Revision de:
  - 7.932 URLs historicas del inventario 011A.
  - 7.330 URLs actuales en sitemap.
  - 602 URLs retiradas del sitemap desde 011A.
  - colecciones geograficas candidatas.
  - URLs de prueba/sin valor.
  - typos en handles/slugs.
  - Black Friday.
  - sufijos `-1`.
  - conteo y patrones de redirecciones.

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

- Sitemaps leidos: 36/36.
- URLs actuales en sitemap: 7.330.
- URLs en inventario 011A: 7.932.
- URLs retiradas desde 011A: 602.
- URLs nuevas desde 011A: 0.
- Las 602 URLs retiradas corresponden a productos de muestra localizados: 86 productos x 7 idiomas.
- Conteo actual de redirecciones Shopify Admin GraphQL: 635.

## Clasificacion maestra

`INCOMPLETO`

- `DECLARADO PERO NO VERIFICADO`: 6.535 URLs sin bandera automatica prioritaria en este lote.
- `REQUIERE DECISION HUMANA`: 688 URLs.
- `INCORRECTO`: 97 URLs.
- `VERIFICADO PERO MEJORABLE`: 10 URLs.

Detalle principal:

- 346 colecciones geograficas candidatas: `REQUIERE DECISION HUMANA`.
- 337 URLs con sufijo `-1` posible duplicado: `REQUIERE DECISION HUMANA`.
- 70 URLs con typo `norid/noridcas`: `INCORRECTO`.
- 19 URLs con typo `enchathed`: `INCORRECTO`.
- 7 URLs `facade-variants/test`: `INCORRECTO`.
- 5 colecciones Black Friday: `REQUIERE DECISION HUMANA`.
- 1 URL `matchalls`: `INCORRECTO`.
- 10 paginas informativas de muestras: `VERIFICADO PERO MEJORABLE`.

## Comprobacion publica prioritaria

`INCOMPLETO`

- URLs sensibles comprobadas: 482.
- `INCORRECTO`: 95.
- `REQUIERE DECISION HUMANA`: 129.
- `VERIFICADO PERO MEJORABLE`: 10.
- `INCOMPLETO`: 248.
- Limitacion: 244 respuestas `429` y 4 respuestas no concluyentes; no se usan como base de cambios.

## Redirecciones

`INCOMPLETO`

- Conteo verificado: 635.
- No existe export local completo.
- Shopify CLI no esta disponible en este entorno.
- Busquedas dirigidas:
  - `facade`: 1 redireccion Admin encontrada.
  - `black-friday`: 0.
  - `matchalls`: 0.
  - `norid`: 0.
  - `enchathed`: 0.
  - `muestra`: 6.
  - `matchwallsmurals`: 334.
  - `matchwallswallpapers`: 44.
  - `-1`: 97 coincidencias no interpretables como sufijo exacto sin export completo.

## Evidencia creada

- `diagnostico-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.md`
- `classification-master-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`
- `classification-master-summary-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.txt`
- `classification-removed-since-011A-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`
- `classification-removed-since-011A-summary-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.txt`
- `public-check-priority-classified-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`
- `public-check-priority-classified-summary-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.txt`
- `geo-collections-candidates-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`
- `redirects-risk-summary-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.md`
- `sitemap-urls-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`
- `sitemap-removed-since-011A-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`
- `robots-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.txt`

## Siguiente orden recomendado

`REQUIERE DECISION HUMANA`

1. `MW-INDEXABILITY-FACADE-TEST-CLEANUP-011C1`
2. `MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D`
3. `MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E`
4. `MW-INDEXABILITY-REDIRECTS-EXPORT-DIAG-011F`
5. `MW-INDEXABILITY-HANDLE-TYPO-MAP-011G`
6. `MW-INDEXABILITY-SUFFIX-1-CLASSIFICATION-011H`
7. `MW-INDEXABILITY-SAMPLE-PAGES-CONTENT-011I`

---

# 2026-06-27 01:10:36 +02:00 - Ejecucion MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B

## Estado

`CORREGIDO Y VERIFICADO`

## Aprobacion

Daniel aprobo exactamente:

`APROBADO LOTE MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B`

## Alcance ejecutado

- Escritura Shopify puntual y reversible.
- 1 producto anomalo confirmado como muestra.
- 7 URLs localizadas de muestra.
- Campo modificado: metafield de producto `seo.hidden`.
- Valor anterior registrado: `null`.
- Valor nuevo: `1`.
- Tipo: `number_integer`.

No incluido:

- Producto principal `https://www.matchwalls.com/products/abstract-curves-negro`.
- Cambio de `productType`.
- Handles.
- Canonicals.
- Redirecciones.
- Tema Shopify.
- Precios.
- Inventario.
- Variantes.
- Apps.
- Search Console, Bing, GA4, GTM o Merchant Center.

## Estado real comprobado antes de escribir

- Product GID: `gid://shopify/Product/8554043474147`.
- Legacy ID: `8554043474147`.
- Titulo: `Muestra Abstract Curves Negro`.
- Handle: `muestra-abstract-curves-negro`.
- `status=ACTIVE`.
- `productType=Mural`.
- `templateSuffix=muestra`.
- `onlineStoreUrl=https://www.matchwalls.com/products/muestra-abstract-curves-negro`.
- `seo.hidden=null`.

## Operacion ejecutada

Mutacion validada contra esquema Shopify:

`SetSeoHiddenSampleAnomaly`

Operacion aplicada mediante `metafieldsSet`:

- ownerId: `gid://shopify/Product/8554043474147`.
- namespace: `seo`.
- key: `hidden`.
- value: `1`.
- type: `number_integer`.

Resultado:

- `userErrors=[]`.

## Verificacion posterior

Admin:

- 1/1 producto verificado por lectura GraphQL final.
- `seo.hidden.value=1`.
- `seo.hidden.type=number_integer`.
- `productType=Mural` permanece sin cambios.
- `templateSuffix=muestra` permanece sin cambios.

Storefront:

- 7/7 URLs de muestra con HTTP 200.
- 7/7 URLs de muestra con meta robots `noindex,nofollow`.
- 7/7 URLs de muestra con canonical self.
- 7/7 URLs de muestra con H1 presente.
- Producto principal inferido sigue HTTP 200, sin `noindex`, con canonical self y H1.

Sitemap:

- 7 product sitemaps revisados.
- 7/7 URLs de muestra ausentes de product sitemaps.
- Producto principal `https://www.matchwalls.com/products/abstract-curves-negro` sigue presente en product sitemap.

## Incidencias

- Sin incidencias abiertas.
- Deuda no corregida por alcance: `productType=Mural`.
- Deuda no corregida por alcance: URL NL usa termino ingles `sample`.

## Evidencias

- Propuesta aprobada: `propuesta-lote-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.md`.
- Admin prediagnostico: `diagnostico-admin-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`.
- Diagnostico publico previo: `diagnostico-publico-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`.
- Diagnostico sitemap previo: `diagnostico-sitemap-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`.
- Admin final: `admin-seohidden-post-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`.
- QA publica final: `qa-publico-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`.
- QA sitemap final: `qa-sitemap-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`.
- Sitemaps revisados: `qa-sitemap-products-checked-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`.
- Informe QA final: `qa-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.md`.

## Reversion

Rollback exacto disponible:

- Ejecutar `metafieldsDelete`.
- ownerId: `gid://shopify/Product/8554043474147`.
- namespace: `seo`.
- key: `hidden`.
- Estado esperado tras rollback: `seo.hidden=null`.

## Estado final

`CORREGIDO Y VERIFICADO`

## Siguiente recomendado

- Continuar con indexabilidad restante: clasificacion de 7.932 URLs, colecciones geograficas, URLs de prueba/sin valor y redirecciones.

# 2026-06-27 01:07:24 +02:00 - Propuesta MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B

## Estado

`REQUIERE DECISION HUMANA`

## Alcance

- Lote solicitado: `MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B`.
- Tipo: diagnostico y propuesta formal.
- Recursos revisados: 1 producto anomalo excluido de `011B5`, 7 URLs localizadas de muestra y producto principal inferido.
- No se modifico Shopify.
- No se ejecutaron mutaciones.
- No se cambiaron productos, metafields, handles, canonicals, redirecciones, tema, precios, inventario ni apps.

## Estado real comprobado

Admin:

- Product GID: `gid://shopify/Product/8554043474147`.
- Legacy ID: `8554043474147`.
- Titulo: `Muestra Abstract Curves Negro`.
- Handle: `muestra-abstract-curves-negro`.
- `status=ACTIVE`.
- `productType=Mural`.
- `templateSuffix=muestra`.
- `onlineStoreUrl=https://www.matchwalls.com/products/muestra-abstract-curves-negro`.
- `seo.hidden=null`.

Publico:

- 7/7 URLs de muestra responden HTTP 200.
- 7/7 URLs de muestra estan indexables actualmente, sin `noindex`.
- 7/7 URLs de muestra estan presentes en product sitemaps.
- Producto principal inferido `https://www.matchwalls.com/products/abstract-curves-negro` responde HTTP 200, no tiene `noindex` y esta presente en sitemap.

## Propuesta

Aplicar `seo.hidden=1` solo al producto `gid://shopify/Product/8554043474147`.

Valores propuestos:

- namespace: `seo`
- key: `hidden`
- value: `1`
- type: `number_integer`

## Motivo

Aunque `productType=Mural`, la evidencia publica y Admin confirma que es una muestra:

- Titulo empieza por `Muestra`.
- Handle empieza por `muestra-`.
- Plantilla: `muestra`.
- URLs localizadas contienen terminos de muestra.
- Existe producto principal inferido e indexable.

## Evidencia

- Propuesta formal: `propuesta-lote-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.md`.
- Diagnostico Admin: `diagnostico-admin-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`.
- Diagnostico publico: `diagnostico-publico-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`.
- Diagnostico sitemap: `diagnostico-sitemap-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`.
- Sitemaps revisados: `diagnostico-sitemaps-products-checked-MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B-2026-06-27.csv`.

## Riesgos

- Shopify ocultara esta muestra de sitemap y busqueda interna.
- Google/Bing no desindexaran al instante.
- No se corrige la deuda `productType=Mural`.
- No se corrige la URL NL con termino ingles `sample`.

## Reversion

- Ejecutar `metafieldsDelete`.
- ownerId: `gid://shopify/Product/8554043474147`.
- namespace: `seo`.
- key: `hidden`.
- Estado esperado: `seo.hidden=null`.

## Siguiente requerido

Para ejecutar escritura:

`APROBADO LOTE MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B`

# 2026-06-27 01:00:00 +02:00 - Ejecucion MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5

## Estado

`CORREGIDO Y VERIFICADO`

## Aprobacion

Daniel aprobo exactamente:

`APROBADO LOTE MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5`

## Alcance ejecutado

- Escritura Shopify controlada por bloques.
- 75 productos muestra limpios.
- 473 URLs localizadas asociadas.
- 3 bloques de 25 productos.
- Campo modificado: metafield de producto `seo.hidden`.
- Valor anterior registrado: `null`.
- Valor nuevo: `1`.
- Tipo: `number_integer`.

No incluido:

- Producto anomalo `gid://shopify/Product/8554043474147` / `muestra-abstract-curves-negro`.
- Productos ya corregidos en el piloto `011B4`.
- Paginas informativas de muestras.
- Colecciones.
- Handles.
- Canonicals.
- Redirecciones.
- Tema Shopify.
- Precios.
- Inventario.
- Variantes.
- Apps.
- Search Console, Bing, GA4, GTM o Merchant Center.

## Estado real comprobado antes de escribir

- 75/75 productos leidos en Admin antes de ejecutar.
- 75/75 con `status=ACTIVE`.
- 75/75 con `productType=Muestra`.
- 75/75 con `templateSuffix=muestra`.
- 75/75 con `onlineStoreUrl` presente.
- 75/75 con `seo.hidden=null`.
- Anomalia `8554043474147` no incluida en ningun bloque.

## Operaciones ejecutadas

Mutacion validada contra esquema Shopify:

`SetSeoHiddenRollingSamples`

Operacion aplicada por bloque mediante `metafieldsSet`:

- `011B5-01`: 25 productos, 173 URLs localizadas.
- `011B5-02`: 25 productos, 144 URLs localizadas.
- `011B5-03`: 25 productos, 156 URLs localizadas.

Resultado de mutaciones:

- Bloque 1: `userErrors=[]`.
- Bloque 2: `userErrors=[]`.
- Bloque 3: `userErrors=[]`.

## Verificacion posterior

Admin:

- 75/75 productos verificados por lectura GraphQL final.
- 75/75 con `seo.hidden.value=1`.
- 75/75 con `seo.hidden.type=number_integer`.

Storefront:

- 473/473 URLs con HTTP 200.
- 473/473 con meta robots `noindex,nofollow`.
- 473/473 con canonical self.
- 473/473 con H1 presente.

Sitemap:

- 7 sitemaps de producto revisados.
- 473/473 URLs ausentes de los sitemaps de producto.

## Incidencias

- Primera pasada del bloque 2 detecto una URL IT sin meta robots por respuesta transitoria/cache: `https://www.matchwalls.com/it/products/armony-rosa-stripe-sample`.
- Reintento aislado: 4/4 correcto con `noindex,nofollow`, canonical self y H1.
- Re-QA completa del bloque 2: 144/144 correcto.
- No queda incidencia abierta en el lote.

## Evidencias

- Propuesta aprobada: `propuesta-lote-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.md`.
- Candidatos limpios: `candidatos-limpios-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- Bloque 01: `bloque-01-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- Bloque 02: `bloque-02-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- Bloque 03: `bloque-03-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- Admin final: `admin-seohidden-post-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- QA publica consolidada: `qa-publico-localizado-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- QA sitemap consolidada: `qa-sitemap-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- Sitemaps revisados: `qa-sitemap-products-checked-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- Informe QA final: `qa-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.md`.

## Reversion

Rollback exacto disponible:

- Ejecutar `metafieldsDelete` por cada Product GID afectado.
- Namespace: `seo`.
- Key: `hidden`.
- Estado esperado tras rollback: `seo.hidden=null`.

## Estado final

`CORREGIDO Y VERIFICADO`

## Siguiente recomendado

- Lote separado para la anomalia excluida: `MW-INDEXABILITY-SAMPLES-NOINDEX-ANOMALY-011B5B`.
- Despues continuar con indexabilidad restante: clasificacion de 7.932 URLs, colecciones geograficas, URLs de prueba/sin valor y redirecciones.

# 2026-06-27 00:48:13 +02:00 - Propuesta MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5

## Estado

`REQUIERE DECISION HUMANA`

## Alcance

- Lote solicitado: `MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5`.
- Tipo: preparacion/propuesta formal de escalado.
- Recursos revisados: 86 productos muestra unicos, piloto 011B4, postcheck 011B4, lectura Admin directa por IDs.
- No se modifico Shopify.
- No se ejecutaron mutaciones.
- No se cambiaron productos, metafields, handles, canonicals, redirecciones, tema, precios, inventario ni apps.

## Estado real comprobado

- Productos muestra unicos mapeados: 86.
- Productos ya corregidos en 011B4: 10.
- Productos pendientes con `seo.hidden=null`: 76.
- Productos limpios propuestos para 011B5: 75.
- URLs localizadas afectadas por los 75 propuestos: 473.
- Producto excluido por anomalia `productType=Mural`: 1 ID / 7 URLs.

## Propuesta

Aplicar `seo.hidden=1` a 75 productos muestra limpios, en 3 bloques de 25.

Valores propuestos:

- namespace: `seo`
- key: `hidden`
- value: `1`
- type: `number_integer`

Rollback:

- `metafieldsDelete` por Product GID, namespace `seo`, key `hidden`.

## Evidencia

- Propuesta formal: `propuesta-lote-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.md`.
- Matriz completa: `matriz-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- Candidatos 76: `candidatos-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- Candidatos limpios 75: `candidatos-limpios-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- Bloque 01: `bloque-01-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- Bloque 02: `bloque-02-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- Bloque 03: `bloque-03-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.
- Exclusion/anomalia: `exclusiones-anomalias-MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5-2026-06-27.csv`.

## Siguiente requerido

Para ejecutar escritura:

`APROBADO LOTE MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5`

# 2026-06-27 00:42:39 +02:00 - Postcheck MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK

## Estado

`CORREGIDO Y VERIFICADO`

## Alcance

- Lote solicitado: `MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK`.
- Tipo: control posterior de solo lectura.
- Recursos revisados: 10 productos piloto, 61 URLs localizadas asociadas, sitemap root y 7 product sitemaps.
- No se modifico Shopify.
- No se ejecutaron mutaciones.
- No se cambiaron productos, metafields, handles, canonicals, redirecciones, tema, precios, inventario ni apps.

## Resultados

- Admin: 10/10 productos siguen `seo.hidden.value = 1`.
- Admin: 10/10 productos siguen `seo.hidden.type = number_integer`.
- Admin: 10/10 productos siguen `ACTIVE`, publicados y con `templateSuffix = muestra`.
- Publico ES: 10/10 status 200, `noindex,nofollow`, canonical self, H1 presente.
- Publico localizado: 61/61 status 200, `noindex,nofollow`, canonical self, H1 presente.
- Sitemap root: 200.
- Product sitemaps revisados: 7/7 con status 200.
- URLs localizadas piloto presentes en product sitemaps: 0/61.

## Incidencias

- Sin incidencias criticas.
- Una URL FR mostro una lectura inicial sin robots en el CSV temporal, pero fue revalidada inmediatamente con lectura directa y cache-control; el HTML correcto contiene `noindex,nofollow`. El CSV final quedo actualizado.

## Evidencia

- QA: `qa-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK-2026-06-27.md`.
- Admin: `admin-seohidden-postcheck-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK-2026-06-27.csv`.
- Publico ES: `qa-publico-es-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK-2026-06-27.csv`.
- Publico localizado: `qa-publico-localizado-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK-2026-06-27.csv`.
- Sitemap URLs: `qa-sitemap-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK-2026-06-27.csv`.
- Sitemap product sitemaps revisados: `qa-sitemap-products-checked-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK-2026-06-27.csv`.

## Rollback

Rollback disponible y no ejecutado:

- `metafieldsDelete` en los 10 Product GID;
- namespace `seo`;
- key `hidden`;
- estado esperado: `seo.hidden = null`.

## Siguiente recomendado

Preparar propuesta formal de escalado controlado:

`MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5`

No ejecutar escalado masivo sin propuesta y aprobacion exacta.

# 2026-06-27 00:36:39 +02:00 - Ejecucion MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4

## Estado

`CORREGIDO Y VERIFICADO`

## Aprobacion

Daniel aprobo despues de la propuesta formal:

`APROBADO LOTE MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4`

## Alcance ejecutado

- Escritura Shopify acotada a 10 productos muestra piloto.
- Cambio aplicado: `seo.hidden=1`.
- Metodo: Admin GraphQL `metafieldsSet`.
- No se modificaron handles, canonicals, redirecciones, paginas, colecciones, tema, precios, inventario, variantes, apps ni plataformas externas.

## Valores anteriores

- 10/10 productos: `seo.hidden = null`.
- Evidencia: `admin-seohidden-lectura-piloto-MW-INDEXABILITY-SAMPLES-ADMIN-SEOHIDDEN-DIAG-011B3-2026-06-27.csv`.

## Valores nuevos

- 10/10 productos: `seo.hidden.value = 1`.
- 10/10 productos: `seo.hidden.type = number_integer`.
- Evidencia: `admin-seohidden-post-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-2026-06-27.csv`.

## Resultado de la mutacion

- Metafields creados/actualizados: 10/10.
- `userErrors`: 0.

## Verificaciones realizadas

- Admin posterior: 10/10 `seo.hidden=1`.
- Publico ES: 10/10 status 200, `noindex,nofollow`, canonical self, H1 presente.
- Publico localizado: 61/61 status 200, `noindex,nofollow`, canonical self, H1 presente.
- Sitemap inmediato: 0/10 URLs ES piloto presentes en product sitemaps revisados.

## Evidencias

- QA: `qa-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-2026-06-27.md`.
- Admin post: `admin-seohidden-post-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-2026-06-27.csv`.
- Publico ES: `qa-publico-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-2026-06-27.csv`.
- Publico localizado: `qa-publico-localizado-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-2026-06-27.csv`.
- Sitemap: `qa-sitemap-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-2026-06-27.csv`.

## Rollback

Rollback exacto disponible:

- Ejecutar `metafieldsDelete` para los 10 Product GID, namespace `seo`, key `hidden`.
- Estado esperado tras rollback: `seo.hidden = null`, igual que antes del lote.

## Incidencias

- Sin incidencias criticas.
- Recordatorio: esto no garantiza desindexacion inmediata en Google/Bing; solo deja las URLs noindex y retiradas del sitemap Shopify segun verificacion inmediata.

## Siguiente recomendado

Esperar/refrescar y ejecutar un control posterior antes de escalar a los 86 productos:

`MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-POSTCHECK`

Despues, si el piloto sigue correcto, preparar propuesta formal:

`MW-INDEXABILITY-SAMPLES-NOINDEX-ROLLING-011B5`

# 2026-06-27 00:31:54 +02:00 - Diagnostico Admin 011B3 y propuesta formal 011B4

## Estado

`REQUIERE DECISION HUMANA`

## Contexto

Daniel envio:

`APROBADO LOTE MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4`

La aprobacion se recibio antes de disponer de la lectura Admin `011B3` y antes de presentar la propuesta formal con valores actuales, riesgos, respaldo, rollback y pruebas.

Por protocolo, no se ejecuto escritura.

## Operaciones realizadas

- Lectura Admin GraphQL de 10 productos candidatos piloto.
- Validacion de consulta `ProductSeoHiddenPilot`.
- Validacion de mutacion propuesta `SetSeoHiddenForSamplePilot`.
- Validacion de rollback `RollbackSeoHiddenForSamplePilot`.
- Creacion de diagnostico `011B3`.
- Creacion de propuesta formal `011B4`.
- No se modifico Shopify.
- No se ejecutaron mutaciones.

## Resultados 011B3

- 10/10 productos existen en Admin.
- 10/10 `status = ACTIVE`.
- 10/10 publicados en Online Store.
- 10/10 `templateSuffix = muestra`.
- 10/10 `productType = Muestra`.
- 10/10 `seo.hidden = null`.

## Propuesta 011B4

Aplicar a los 10 productos piloto:

- namespace: `seo`
- key: `hidden`
- value: `1`
- type: `number_integer`

Rollback:

- borrar `seo.hidden` para volver a `null`.

## Evidencia

- Diagnostico: `diagnostico-MW-INDEXABILITY-SAMPLES-ADMIN-SEOHIDDEN-DIAG-011B3-2026-06-27.md`.
- CSV lectura Admin: `admin-seohidden-lectura-piloto-MW-INDEXABILITY-SAMPLES-ADMIN-SEOHIDDEN-DIAG-011B3-2026-06-27.csv`.
- Propuesta formal: `propuesta-lote-MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4-2026-06-27.md`.

## Siguiente requerido

Para ejecutar escritura ahora, Daniel debe aprobar de nuevo despues de esta propuesta:

`APROBADO LOTE MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4`

# 2026-06-27 00:27:28 +02:00 - Diagnostico MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2

## Estado

`INCOMPLETO`

## Alcance

- Lote solicitado: `MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2`.
- Tipo: diagnostico/mapeo de solo lectura.
- Recursos revisados: inventario 011B, sitemap 011A, auditoria local de URLs, muestra publica 011B y endpoints publicos Shopify `.js` de productos.
- No se modifico Shopify.
- No se ejecutaron mutaciones.
- No se cambiaron productos, metafields, handles, canonicals, redirecciones, noindex, temas, precios, inventario ni apps.

## Resultados

- URLs de productos muestra en sitemap: 541.
- URLs no producto con termino muestra: 11.
- IDs publicos unicos de producto muestra: 86.
- IDs publicos recuperados via `.js`: 86/86.
- URLs `.js` recuperadas: 541/541.
- URLs prioritarias ES/EN/FR/DE/NL: 377.
- URLs IT/PT fuera de alcance prioritario: 164.
- Distribucion por ID: 42 IDs con 7 URLs localizadas, 40 IDs con 6 URLs, 1 ID con 4 URLs y 3 IDs con 1 URL.
- Mapeo URL muestra -> posible producto principal por handle exacto: 195 URLs.
- URLs sin mapeo exacto publico: 346.
- IDs con mapeo ES exacto: 86/86.
- IDs con anomalias en idiomas prioritarios: 43.
- IDs sin anomalias en idiomas prioritarios: 43.
- Candidatos tecnicos para futuro piloto: 10 IDs.

## Limitaciones

- Shopify CLI no esta instalado en el entorno local.
- Admin API: `NO ACCESIBLE`.
- Valor actual de `seo.hidden`: `NO ACCESIBLE`.
- No se puede ejecutar ni proponer escritura final sin leer el valor Admin actual y preparar rollback exacto.

## Evidencia

- Informe: `diagnostico-MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2-2026-06-27.md`.
- Mapeo URL producto muestra: `mapeo-productos-muestra-MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2-2026-06-27.csv`.
- No productos: `mapeo-no-productos-muestra-MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2-2026-06-27.csv`.
- Agrupacion por ID: `agrupacion-productos-muestra-por-id-MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2-2026-06-27.csv`.
- Candidatos piloto: `candidatos-piloto-noindex-MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2-2026-06-27.csv`.
- Resumen: `resumen-MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2-2026-06-27.txt`.

## Siguiente recomendado

`MW-INDEXABILITY-SAMPLES-ADMIN-SEOHIDDEN-DIAG-011B3`

Tipo: solo lectura.

Objetivo: confirmar IDs Admin/GID y leer `seo.hidden` actual para los 10 candidatos piloto y, si es viable, para los 86 IDs.

No ejecutar escritura hasta propuesta posterior `MW-INDEXABILITY-SAMPLES-NOINDEX-PILOT-011B4` con aprobacion exacta.

# 2026-06-27 00:12:18 +02:00 - Aprobacion de criterio MW-INDEXABILITY-SAMPLES-POLICY-011B

## Estado

`VERIFICADO Y CORRECTO`

## Decision recibida

Daniel aprueba exactamente:

`APROBADO CRITERIO MW-INDEXABILITY-SAMPLES-POLICY-011B: NOINDEX POR DEFECTO PARA PRODUCTOS MUESTRA CONFIRMADOS; PAGINAS INFORMATIVAS DE MUESTRAS INDEXABLES; EXCEPCIONES SOLO CON EVIDENCIA`

## Alcance de la aprobacion

- Aprobada la politica SEO/GEO para muestras.
- Productos muestra confirmados: noindex por defecto, salvo excepciones con evidencia.
- Paginas informativas de muestras: mantener indexables si son utiles y localizadas.
- Excepciones: solo con evidencia verificable.
- No autoriza todavia escritura en Shopify.
- No autoriza noindex masivo.
- No autoriza cambios de handles, canonicals, redirecciones, productos, colecciones, paginas, tema, inventario, precios, apps ni configuracion externa.

## Operaciones realizadas

- Actualizada la propuesta `propuesta-politica-MW-INDEXABILITY-SAMPLES-POLICY-011B-2026-06-27.md`.
- Actualizado este registro.
- No se modifico Shopify.

## Siguiente recomendado

Ejecutar diagnostico/mapeo sin escritura:

`MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2`

Objetivo: construir la lista real de productos muestra confirmados con IDs, idioma, handle, estado, posible producto principal, valores actuales de `seo.hidden`, falsos positivos y excepciones candidatas.

# 2026-06-27 00:08:43 +02:00 - Politica MW-INDEXABILITY-SAMPLES-POLICY-011B

## Estado

`REQUIERE DECISION HUMANA`

## Alcance

- Lote/documento solicitado: `MW-INDEXABILITY-SAMPLES-POLICY-011B`.
- Tipo: politica SEO/GEO de muestras; solo lectura y documentacion.
- Recursos revisados: sitemap publico de 7.932 URLs ya verificado en 011A, inventario especifico de muestras, muestra publica acotada y documentacion oficial Shopify.
- No se modifico Shopify.
- No se publicaron, duplicaron, renombraron ni eliminaron temas.
- No se cambiaron productos, colecciones, paginas, handles, redirecciones, canonicals, robots, noindex, precios, inventario, schema, GA4, GTM, Merchant Center ni apps.

## Resultados

- URLs con terminos de muestra en sitemap: 552.
- Productos candidatos a muestra: 541.
- Paginas informativas/de instalacion con terminos de muestra: 10.
- Colecciones/listados con terminos de muestra: 1.
- URLs prioritarias ES/EN/FR/DE/NL: 385.
- Productos muestra prioritarios ES/EN/FR/DE/NL: 377.
- URLs IT/PT fuera de alcance prioritario actual: 167.
- Muestra publica acotada: 35/35 responden 200, 35/35 canonical self, 0/35 con noindex detectado, 35/35 con H1.
- Anomalias detectadas: 42 URLs NL con terminos no neerlandeses de muestra, 1 URL EN con `muestra`, 1 URL FR con `muestra`, 37 URLs con sufijo numerico y 26 con sufijo `-1`.

## Politica recomendada

- Tratar productos muestra como productos auxiliares de conversion, no como landings SEO.
- Mantener indexables las paginas informativas de muestras/instalacion cuando tengan contenido util y localizado.
- No aplicar noindex, canonical ni redirecciones de forma masiva sin mapa fiable `producto principal -> muestra`.
- Metodo futuro preferente: `seo.hidden=1` en productos muestra confirmados, con aceptacion previa de que Shopify tambien los oculta de la busqueda interna de tienda.
- No usar robots.txt para retirar muestras ya indexables.
- No cambiar handles en este bloque.

## Evidencia

- Propuesta: `propuesta-politica-MW-INDEXABILITY-SAMPLES-POLICY-011B-2026-06-27.md`.
- Inventario: `inventario-muestras-MW-INDEXABILITY-SAMPLES-POLICY-011B-2026-06-26.csv`.
- Muestra publica: `muestra-publica-muestras-MW-INDEXABILITY-SAMPLES-POLICY-011B-2026-06-26.csv`.
- Fuente Shopify Help Center: `https://help.shopify.com/en/manual/promoting-marketing/seo/hide-a-page-from-search-engines`.
- Fuente Shopify Dev Docs: `https://shopify.dev/docs/apps/build/marketing-analytics/optimize-storefront-seo`.

## Siguiente recomendado

Decision recomendada:

`APROBADO CRITERIO MW-INDEXABILITY-SAMPLES-POLICY-011B: NOINDEX POR DEFECTO PARA PRODUCTOS MUESTRA CONFIRMADOS; PAGINAS INFORMATIVAS DE MUESTRAS INDEXABLES; EXCEPCIONES SOLO CON EVIDENCIA`

Siguiente trabajo sin escritura:

`MW-INDEXABILITY-SAMPLES-MAPPING-DIAG-011B2`

No ejecutar escritura hasta una propuesta posterior con IDs, valores actuales, valores propuestos, impacto en busqueda interna, respaldo, rollback y pruebas.

# 2026-06-26 23:58:00 +02:00 - Diagnostico MW-INDEXABILITY-INVENTORY-DIAG-011A

## Estado

`INCOMPLETO`

## Alcance

- Lote solicitado: `MW-INDEXABILITY-INVENTORY-DIAG-011A`.
- Tipo: diagnostico de solo lectura.
- Recursos revisados: robots.txt, agents.md, UCP, sitemap index, 36 sub-sitemaps, 7.932 URLs de sitemap, inventario de patrones y muestra de URLs criticas.

## Operaciones realizadas

- Lectura de documentos internos del proyecto.
- Descarga publica de `robots.txt`.
- Descarga publica de `sitemap.xml`.
- Descarga de 36/36 sub-sitemaps.
- Clasificacion inicial de 7.932 URLs.
- Muestreo publico de URLs criticas de indexabilidad.
- No se modifico Shopify.
- No se publicaron, duplicaron, renombraron ni eliminaron temas.
- No se cambiaron productos, colecciones, paginas, handles, redirecciones, canonicals, hreflang, robots, noindex, precios, inventario, schema, GA4, GTM, Merchant Center ni apps.

## Resultados

- `robots.txt`: 200, sitemap declarado, rastreo publico general permitido y superficies privadas/transaccionales bloqueadas.
- `agents.md`: 200.
- `.well-known/ucp`: 200.
- `sitemap.xml`: 200, `sitemapindex`.
- Sub-sitemaps: 36/36 accesibles.
- URLs sitemap: 7.932.
- Productos: 6.797, 971 por idioma.
- Colecciones: 749, 107 por idioma.
- Paginas: 294, 42 por idioma.
- Blogs: 84, 12 por idioma.
- Muestras detectadas por patron multilingue: 552.
- URLs `facade-variants/test`: 7 en sitemap; responden 301 a home localizada.
- Black Friday: 5 URLs indexables.
- Marca mal escrita `matchalls`: 1 URL FR indexable.
- Typos `norid/noridcas`: 70 URLs.
- Typos `enchathed`: 19 URLs.
- Sufijo `-1`: 435 URLs; requiere clasificacion, no correccion masiva.
- Colecciones geograficas por patron claro: 170 URLs, con 58 ES verificadas en sitemap.
- Uploader personalizado: 200 con `noindex,nofollow` y ausente del sitemap.
- Paginas FR/NL/EN antes problematicas por H1 en la muestra revisada: H1 presente.

## Limitaciones

- Redirecciones Shopify actuales: `DECLARADO PERO NO VERIFICADO`; historico interno declara 635, pero no se obtuvo export actual en este lote.
- Search Console: `NO ACCESIBLE`.
- Bing Webmaster Tools: `NO ACCESIBLE`.
- Datos de ventas/conversion por URL: `NO ACCESIBLE`.
- No se puede decidir retirada/noindex/redirect de URLs sin datos y aprobacion humana.

## Evidencia

- Informe: `diagnostico-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.md`.
- Robots: `robots-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.txt`.
- Sitemap index: `sitemap-index-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.csv`.
- URLs sitemap: `sitemap-urls-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.csv`.
- Flags: `inventario-flags-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.csv`.
- Muestra critica: `muestra-indexabilidad-MW-INDEXABILITY-INVENTORY-DIAG-011A-2026-06-26.csv`.

## Siguiente recomendado

Preparar `MW-INDEXABILITY-SAMPLES-POLICY-011B` como lote de decision/propuesta, sin aplicar cambios, para definir la politica de las 552 muestras en sitemap y contrastarla con las 1.990 muestras internas declaradas historicamente.

# 2026-06-26 23:47:11 +02:00 - Publicacion MW-PUBLISH-TECH-DEBT-010P

## Estado

`CORREGIDO Y VERIFICADO`

## Alcance

- Lote aprobado por Daniel: `MW-PUBLISH-TECH-DEBT-010P`.
- Tipo: publicacion de tema tecnico QA.
- Tema publicado: `178399019384`.
- Nombre publicado: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Tema anterior conservado para reversion: `178396463480`.
- Nombre rollback: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.

## Valores anteriores y nuevos

Antes:

- `178396463480`: `MAIN` / `Active`.
- `178399019384`: borrador / `Draft`.

Despues:

- `178399019384`: `MAIN` / `Active`.
- `178396463480`: borrador / rollback publicable.

## Operacion ejecutada

- Publicacion realizada desde Shopify Admin tras preflight visual.
- El boton `Publish` usado correspondia al tema `178399019384`.
- El modal de confirmacion contenia el nombre `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- No se editaron archivos Liquid.
- No se tocaron productos, precios, variantes, inventario, handles, redirecciones, canonicals, hreflang, GA4, GTM, Merchant Center ni apps.

## Verificacion posterior

- Shopify Admin: `178399019384` aparece como `Active`.
- Shopify Admin: `178396463480` aparece en borradores con boton `Publish`, disponible para reversion.
- Home live ES mobile: H1 correcto, canonical correcto, `html lang=es`, sin `noindex`, assets `/t/46` presentes y `/t/45` ausentes.
- Matriz publica: 170/170 `CORREGIDO Y VERIFICADO`.
- Assets tema nuevo `/t/46`: presentes.
- Assets tema anterior `/t/45`: 0.
- Anexo tecnico funcional en navegador: correcto.
- Overflow FR/NL mobile 375/390: 0.
- Consola en alcance tecnico: 0 errores criticos.
- Swatch tooltip mobile: `none`.
- Swatch tooltip desktop FR/NL: `block`.
- Medidas externas/internas: sincronizadas a `423 x 223`.
- Tracking diagnostico `mwqa=010a2d`: `data-mw010a2d-count=4`, ultimo evento `input_mural_outside` para `height=223`.

## Evidencia

- Informe QA: `qa-MW-PUBLISH-TECH-DEBT-010P-2026-06-26.md`.
- Matriz publica: `matriz-MW-PUBLISH-TECH-DEBT-010P-post-2026-06-26.csv`.
- Matriz tecnica: `matriz-tecnica-MW-PUBLISH-TECH-DEBT-010P-post-2026-06-26.csv`.

## Incidencia no bloqueante

`VERIFICADO PERO MEJORABLE`

Las URLs limpias del producto uploader muestran `meta robots="noindex,nofollow"`.

Ejemplo verificado: `https://www.matchwalls.com/products/custom-file-uploader`.

No hay evidencia de regresion visual o funcional causada por la publicacion. No se recomienda rollback por esta incidencia. Debe pasar al bloque de indexabilidad para decision humana: indexar o mantener fuera del indice el uploader.

## Reversion

Si aparece un fallo critico posterior:

1. Publicar de nuevo el tema `178396463480` desde Shopify Admin.
2. Confirmar que vuelve a `Active`.
3. Repetir prueba centinela live y matriz tecnica reducida.

# 2026-06-26 23:40:00 +02:00 - Preflight MW-PUBLISH-TECH-DEBT-010P

## Estado

`INCOMPLETO`

## Alcance

- Lote aprobado por Daniel: `MW-PUBLISH-TECH-DEBT-010P`.
- Tipo: publicacion de tema tecnico QA tras preflight.
- Tema candidato propuesto: `178399019384`.
- Tema rollback propuesto: `178396463480`.

## Resultado del preflight

- Shopify no fue modificado.
- No se publico, duplico, renombro ni elimino ningun tema.
- No se cambiaron archivos Liquid, productos, precios, variantes, inventario, handles, redirecciones, canonicals, hreflang, GA4, GTM, Merchant Center ni apps.
- Shopify CLI local: `NO ACCESIBLE`; `shopify` no esta disponible en PATH.
- Shopify Admin visual: `NO ACCESIBLE` en este punto por bloqueo de verificacion de conexion: "Se debe verificar tu conexion antes de poder continuar".

## Incidencia

La publicacion queda detenida antes de ejecutar cualquier cambio porque no se puede confirmar el MAIN real, el tema candidato y el rollback dentro de Shopify Admin.

## Reversion

No aplica reversion: no hubo escritura ni cambio de estado en Shopify.

## Siguiente accion requerida

Daniel debe completar la verificacion de conexion en Shopify Admin y avisar para reanudar el preflight. Tras recuperar acceso, se debe confirmar visualmente `178399019384`, `178396463480` y el MAIN real antes de publicar.

# 2026-06-26 21:38:50 +02:00 - QA MW-TECH-QA-FULL-REGRESSION-010Z3

## Estado

`VERIFICADO Y CORRECTO`

## Alcance

- Lote solicitado: `MW-TECH-QA-FULL-REGRESSION-010Z3`.
- Tipo: diagnÃ³stico y QA de solo lectura.
- Matriz principal: 17 pÃ¡ginas Ã— 5 idiomas Ã— desktop/mobile = 170 pruebas.
- Anexo tÃ©cnico: 13 pruebas adicionales sobre home, producto estÃ¡ndar, uploader y tracking.
- Tema QA probado en navegador con preview: `178399019384`, assets `/t/46`.
- Live pÃºblico sin sesiÃ³n comprobado por HTTP limpio: home cargÃ³ `/t/45` y 0 `/t/46`.
- No se modificÃ³ Shopify.
- No se publicÃ³, duplicÃ³, renombrÃ³ ni eliminÃ³ ningÃºn tema.
- No se cambiaron productos, precios, variantes, inventario, handles, redirecciones, canonicals, hreflang, GA4, GTM, Merchant Center ni apps.

## LimitaciÃ³n de acceso

- Shopify CLI/Admin API: `NO ACCESIBLE` en este turno; `shopify` no estaba disponible en PATH.
- Roles e IDs se apoyan en verificaciÃ³n 010Z2 y evidencia pÃºblica actual de live/preview.

## Resultados

- Matriz principal: 170/170 `CORREGIDO Y VERIFICADO`.
- Desktop: 85/85.
- Mobile: 85/85.
- Assets QA `/t/46`: 170/170.
- Assets MAIN `/t/45`: 0/170.
- H1 esperado y Ãºnico: 170/170.
- Canonical propio: 170/170.
- Hreflang prioritario ES/EN/FR/DE/NL: 170/170.
- `html lang`: 170/170.
- Sin `noindex`: 170/170.
- Contenido no vacÃ­o: 170/170.
- Overflow real: 0/170.
- Errores crÃ­ticos de consola: 0/170.
- Anexo tÃ©cnico: 13/13 `CORREGIDO Y VERIFICADO`.
- Tracking `input_mural_outside`: `data-mw010a2d-count=2`, externos/internos sincronizados a `423Ã—223`.

## Incidencias

- No se detectaron incidencias bloqueantes en el alcance probado.
- Incidencia operativa no atribuible a la web: pÃ©rdida de una pestaÃ±a del navegador interno durante el anexo; el anexo se repitiÃ³ correctamente con pestaÃ±a nueva.
- No se probÃ³ checkout real, subida de archivo real, pago, creaciÃ³n de pedido, apps externas con datos reales, GA4, GTM, Search Console, Merchant Center, Bing Webmaster Tools ni CrUX.

## Evidencia

- Documento QA: `qa-MW-TECH-QA-FULL-REGRESSION-010Z3-2026-06-26.md`.
- Matriz principal: `matriz-MW-TECH-QA-FULL-REGRESSION-010Z3-2026-06-26.csv`.
- Matriz tÃ©cnica: `matriz-tecnica-MW-TECH-QA-FULL-REGRESSION-010Z3-2026-06-26.csv`.

## ReversiÃ³n

No aplica reversiÃ³n: no hubo escritura ni cambio de estado en Shopify.

# 2026-06-26 21:10:31 +02:00 - QA MW-TECH-QA-REGRESSION-MATRIX-010Z2

## Estado

`VERIFICADO Y CORRECTO` dentro del alcance compacto de regresiÃ³n 010Z2.

## Alcance

- Lote solicitado: `MW-TECH-QA-REGRESSION-MATRIX-010Z2`.
- Tipo: diagnÃ³stico y QA de solo lectura.
- Tema QA verificado: `gid://shopify/OnlineStoreTheme/178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.
- MAIN verificado y no modificado: `gid://shopify/OnlineStoreTheme/178396463480`, rol `MAIN`, prefijo `/t/45`.
- No se modificÃ³ Shopify.
- No se publicÃ³, duplicÃ³, renombrÃ³ ni eliminÃ³ ningÃºn tema.
- No se cambiaron productos, precios, variantes, inventario, handles, redirecciones, canonicals, hreflang, GA4, GTM, Merchant Center ni apps.

## Pruebas realizadas

- Home ES mobile 390 y desktop 1440.
- Cart ES mobile 390.
- ColecciÃ³n ofertas ES mobile 390.
- Producto estÃ¡ndar ES mobile 390.
- Uploader ES/EN/FR/DE/NL mobile 390.
- Uploader FR/NL mobile 375.
- Uploader FR/NL desktop 1440.
- Tracking de medidas con marcador QA `mwqa=010a2d`.

## Resultados

- Assets QA `/t/46` cargados en las pÃ¡ginas medidas; assets MAIN `/t/45`: 0.
- Consola: 0 errores capturados en todas las pÃ¡ginas de la matriz.
- Overflow real: 0 en todas las pÃ¡ginas medidas.
- Home CSS rastreable: `cssLeak=false`.
- H1, canonical y 8 hreflang presentes en pÃ¡ginas orgÃ¡nicas crÃ­ticas probadas.
- 010C5 confirmado: swatch tooltip oculto en mobile y conservado en desktop.
- 010A2D confirmado: tras introducir `421` y `221`, externos e internos sincronizan y el marcador QA registra `data-mw010a2d-count=2`.

## Incidencias

- Cart ES no mostrÃ³ H1 en esta mediciÃ³n. Estado: `VERIFICADO PERO MEJORABLE`; no bloquea este lote tÃ©cnico.
- Lectura directa de `window.dataLayer` desde el entorno de inspecciÃ³n: `NO ACCESIBLE`; el marcador QA incorporado confirmÃ³ el evento.
- No se ejecutaron las 170 pruebas completas.

## Evidencia

- Documento QA: `qa-MW-TECH-QA-REGRESSION-MATRIX-010Z2-2026-06-26.md`.

## ReversiÃ³n

No aplica reversiÃ³n: no hubo escritura ni cambio de estado en Shopify.
# 2026-06-26 10:20:37 +02:00 - EjecuciÃƒÂ³n MW-TECH-MOBILE-OVERFLOW-SWATCH-TOOLTIP-010C5

## Estado

`CORREGIDO Y VERIFICADO`

## AprobaciÃƒÂ³n y alcance

- AprobaciÃƒÂ³n exacta recibida: `APROBADO LOTE MW-TECH-MOBILE-OVERFLOW-SWATCH-TOOLTIP-010C5`.
- Tema afectado: `gid://shopify/OnlineStoreTheme/178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.
- Archivo modificado: `snippets/variant-picker.liquid`.
- MAIN verificado y no modificado: `gid://shopify/OnlineStoreTheme/178396463480`, rol `MAIN`, prefijo `/t/45`.
- No se publicÃƒÂ³ ningÃƒÂºn tema.
- No se modificaron productos, precios, variantes, inventario, handles, redirecciones, canonicals, hreflang, GA4, GTM, Merchant Center ni apps.

## Valores

- QA `snippets/variant-picker.liquid` antes: MD5 `48ef3d83e49275ccea7f044c1b56d2d8`, size `14811`.
- QA `snippets/variant-picker.liquid` despuÃƒÂ©s: MD5 `44af7568d1ddeb65f5fabe7b782c7a05`, size `14968`.
- MAIN `snippets/variant-picker.liquid`: MD5 `48ef3d83e49275ccea7f044c1b56d2d8`, size `14811`.
- QA `assets/theme.css`: MD5 `b86a0e260263eed6a2586a3e7bca8e05`, size `242427`, sin cambios.
- QA `sections/related-products.liquid`: MD5 `d8822a8c73cee73d61744c0b68b7a375`, size `10705`, sin cambios.

## Cambio ejecutado

Se aÃƒÂ±adiÃƒÂ³ en `snippets/variant-picker.liquid` una regla mÃƒÂ³vil acotada para neutralizar el pseudo-tooltip de swatches dentro de `.product-info__variant-picker`:

```css
@media screen and (max-width: 699px) {
  .product-info__variant-picker .block-swatch[data-tooltip]::after {
    content: none;
    display: none;
  }
}
```

Motivo: 010C4 demostrÃƒÂ³ que `.block-swatch[data-tooltip]::after`, aun invisible, computaba ancho por `content: attr(data-tooltip)` y `white-space: nowrap`, generando overflow mÃƒÂ³vil en FR/NL.

## EjecuciÃƒÂ³n

- MutaciÃƒÂ³n: `themeFilesUpsert`.
- Cuerpo: `BASE64`.
- Resultado Shopify: `userErrors=[]`.
- Readback: MD5 `44af7568d1ddeb65f5fabe7b782c7a05`, size `14968`, `processing=false`, `processingFailed=false`.

## QA

`CORREGIDO Y VERIFICADO`

- FR uploader mÃƒÂ³vil 390: `docScrollWidth=375`, `docClientWidth=375`, overflow `0`.
- FR uploader mÃƒÂ³vil 375: `docScrollWidth=360`, `docClientWidth=360`, overflow `0`.
- NL uploader mÃƒÂ³vil 390: `docScrollWidth=375`, `docClientWidth=375`, overflow `0`.
- NL uploader mÃƒÂ³vil 375: `docScrollWidth=360`, `docClientWidth=360`, overflow `0`.
- ES uploader mÃƒÂ³vil 390: overflow `0`.
- EN uploader mÃƒÂ³vil 390: overflow `0`.
- DE uploader mÃƒÂ³vil 390: overflow `0`.
- Desktop FR 1440: overflow `0`; tooltip desktop conservado.
- Desktop NL 1440: overflow `0`; tooltip desktop conservado.
- Carrusel de relacionados conserva scroll interno y no ensancha el documento.
- Assets QA `/t/46`: 11; assets MAIN `/t/45`: 0 en las verificaciones pÃƒÂºblicas.
- Consola: 0 errores capturados.

## ValidaciÃƒÂ³n y limitaciones

- GraphQL validado contra schema antes de ejecutar.
- Shopify aceptÃƒÂ³ el archivo con `userErrors=[]`.
- Readback confirmÃƒÂ³ MD5 esperado.
- El validador local `shopify-liquid/scripts/validate.mjs` no pudo completarse por dependencia ausente del runtime (`@shopify/theme-check-common`). Se registra como limitaciÃƒÂ³n de herramienta local, no como error del cÃƒÂ³digo.
- No se ejecutÃƒÂ³ matriz completa de 170 pruebas en este cierre.

## ReversiÃƒÂ³n

Restaurar `snippets/variant-picker.liquid` del tema QA `178399019384` al MD5 original `48ef3d83e49275ccea7f044c1b56d2d8`, size `14811`.

Fuente de rollback verificada: MAIN `gid://shopify/OnlineStoreTheme/178396463480`, mismo archivo, mismo MD5 y size.

## Evidencia

- Documento QA: `qa-MW-TECH-MOBILE-OVERFLOW-SWATCH-TOOLTIP-010C5-2026-06-26.md`.

---

# 2026-06-26 09:53:05 +02:00 - DiagnÃƒÂ³stico MW-TECH-MOBILE-OVERFLOW-VARIANT-SWATCH-DIAG-010C4

## Estado

`VERIFICADO Y CORRECTO` como diagnÃƒÂ³stico de causa. La incidencia visual queda `INCOMPLETO` hasta ejecutar un lote de correcciÃƒÂ³n.

## Alcance

- Lote indicado por Daniel: `MW-TECH-MOBILE-OVERFLOW-VARIANT-SWATCH-DIAG-010C4`.
- Tipo: solo lectura.
- Tema QA auditado: `gid://shopify/OnlineStoreTheme/178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.
- MAIN no modificado.
- No se publicÃƒÂ³ ningÃƒÂºn tema.
- No se modificaron productos, precios, variantes, inventario, handles, redirecciones, canonicals, hreflang, GA4, GTM, Merchant Center ni apps.

## Evidencia principal

- FR uploader mÃƒÂ³vil 390: `docScrollWidth=447`, `docClientWidth=375`, overflow vs `innerWidth` `+57 px`.
- FR uploader mÃƒÂ³vil 375: `docScrollWidth=447`, `docClientWidth=360`, overflow vs `innerWidth` `+72 px`.
- NL uploader mÃƒÂ³vil 390: `docScrollWidth=427`, `docClientWidth=375`, overflow vs `innerWidth` `+37 px`.
- NL uploader mÃƒÂ³vil 375: `docScrollWidth=427`, `docClientWidth=360`, overflow vs `innerWidth` `+52 px`.
- Assets QA `/t/46`: 11; assets MAIN `/t/45`: 0.
- `related-products` no es la causa: `.shopify-section--product-recommendations` tiene `ownScroll=0`; el carrusel tiene scroll interno `overflow-x:auto`.
- Causa acotada: `.product-info__variant-picker` / `variant-picker#div-to-duplicate` / `.variant-picker__option-values` ensanchan el `main`.
- Causa exacta identificada: pseudo-elemento `.block-swatch[data-tooltip]::after` en `snippets/variant-picker.liquid`, con `content: attr(data-tooltip)`, `position:absolute`, `white-space:nowrap`, `opacity:0`, `visibility:hidden`.
- Aunque invisible, el tooltip absoluto cuenta para el `scrollWidth` mÃƒÂ³vil.

## Estado Shopify verificado

- QA `snippets/variant-picker.liquid`: MD5 `48ef3d83e49275ccea7f044c1b56d2d8`, size `14811`.
- QA `snippets/option-value.liquid`: MD5 `f2fd22527bc9b48182911c0c54f23399`, size `17066`.
- QA `assets/theme.css`: MD5 `b86a0e260263eed6a2586a3e7bca8e05`, size `242427`.

## ConclusiÃƒÂ³n

`MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3` queda confirmado como candidato fallido por causa mal atribuida.

PrÃƒÂ³ximo lote recomendado: `MW-TECH-MOBILE-OVERFLOW-SWATCH-TOOLTIP-010C5`, escritura acotada a QA para neutralizar el pseudo-tooltip de swatches en mÃƒÂ³vil.

## Evidencia

- Documento QA: `qa-MW-TECH-MOBILE-OVERFLOW-VARIANT-SWATCH-DIAG-010C4-2026-06-26.md`.

---

# 2026-06-25 20:01:31 +02:00 - EjecuciÃƒÂ³n MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3

## Estado

`INCORRECTO` para el candidato 010C3. Rollback final: `CORREGIDO Y VERIFICADO`.

## AprobaciÃƒÂ³n y alcance

- AprobaciÃƒÂ³n exacta recibida: `APROBADO LOTE MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3`.
- Tema afectado: `gid://shopify/OnlineStoreTheme/178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.
- Archivo afectado: `sections/related-products.liquid`.
- MAIN verificado y no modificado: `gid://shopify/OnlineStoreTheme/178396463480`, rol `MAIN`, prefijo `/t/45`.
- No se publicÃƒÂ³ ningÃƒÂºn tema.
- No se modificaron productos, precios, variantes, inventario, handles, redirecciones, canonicals, hreflang, GA4, GTM, Merchant Center ni apps.

## Valores originales verificados

- QA `sections/related-products.liquid`: MD5 `d8822a8c73cee73d61744c0b68b7a375`, size `10705`.
- QA `assets/theme.css`: MD5 `b86a0e260263eed6a2586a3e7bca8e05`, size `242427`.
- MAIN `sections/related-products.liquid`: MD5 `d8822a8c73cee73d61744c0b68b7a375`, size `10705`.
- MAIN `assets/theme.css`: MD5 `89f4729809a0eaac75a764e0fc41888e`, size `241968`.

## Cambio candidato ejecutado

- Se aÃƒÂ±adiÃƒÂ³ CSS mÃƒÂ³vil acotado dentro de `sections/related-products.liquid` para intentar contener el overflow de `scroll-carousel.scroll-area.bleed` en la secciÃƒÂ³n `shopify-section--product-recommendations`.
- `themeFilesUpsert`: `userErrors=[]`.
- Readback del candidato: MD5 `e1637667eebf1ec246786deaa2a45297`, size `11112`.
- `assets/theme.css` no fue modificado.

## QA crÃƒÂ­tica del candidato

`INCORRECTO`

- FR uploader mÃƒÂ³vil 390: overflow siguiÃƒÂ³ en `+57 px`; assets `/t/46`; assets `/t/45` = 0; consola sin errores.
- NL uploader mÃƒÂ³vil 390: overflow siguiÃƒÂ³ en `+37 px`; assets `/t/46`; assets `/t/45` = 0; consola sin errores.
- El candidato no resolviÃƒÂ³ la incidencia detectada por `MW-TECH-QA-REGRESSION-MATRIX-010Z`.

## Rollback ejecutado

`CORREGIDO Y VERIFICADO`

- Se revirtiÃƒÂ³ `sections/related-products.liquid` en el tema QA.
- Primera lectura de rollback detectÃƒÂ³ una discrepancia temporal en QA: MD5 `ccd037da6ce4b2f41963e823e3845e48`, size `10699`, causada por una diferencia de clase en una ocurrencia de `animated-arrow--reverse`. No se aceptÃƒÂ³ como estado final.
- Se restaurÃƒÂ³ de nuevo desde el archivo local verificado contra MAIN.
- Readback final QA: MD5 `d8822a8c73cee73d61744c0b68b7a375`, size `10705`, `processing=false`, `processingFailed=false`.
- MAIN final: MD5 `d8822a8c73cee73d61744c0b68b7a375`, size `10705`, `processing=false`, `processingFailed=false`.
- QA `assets/theme.css` final: MD5 `b86a0e260263eed6a2586a3e7bca8e05`; sin cambios.
- MAIN `assets/theme.css` final: MD5 `89f4729809a0eaac75a764e0fc41888e`; sin cambios.

## QA pÃƒÂºblica despuÃƒÂ©s del rollback

`VERIFICADO PERO MEJORABLE`

- NL uploader mÃƒÂ³vil 390: assets `/t/46` = 11, assets `/t/45` = 0, canonical correcto, hreflang = 8, consola sin errores, overflow `+37 px`.
- FR uploader mÃƒÂ³vil 390: assets `/t/46` = 11, assets `/t/45` = 0, canonical correcto, hreflang = 8, consola sin errores, overflow `+57 px`.
- El overflow queda exactamente como incidencia pendiente; no hay parche parcial activo.

## Estado final del lote

`INCORRECTO`

- 010C3 queda rechazado: no publicar, no promover y no reutilizar como soluciÃƒÂ³n.
- QA queda estable y revertido al mismo MD5 que MAIN para `sections/related-products.liquid`.
- PrÃƒÂ³ximo paso recomendado: `MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-DIAG-010C4`, diagnÃƒÂ³stico de solo lectura para localizar el elemento exacto que genera `scrollWidth` en FR/NL antes de proponer otro cambio.

## Evidencia

- Documento QA: `qa-MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3-2026-06-25.md`.
- Propuesta original: `propuesta-lote-MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3-2026-06-25.md`.

---# 2026-06-25 16:11:34 +02:00 - QA MW-TECH-QA-REGRESSION-MATRIX-010Z

## Estado

`VERIFICADO PERO MEJORABLE`

## Alcance

- QA de regresiÃƒÂ³n compacta de solo lectura.
- Tema MAIN verificado: `gid://shopify/OnlineStoreTheme/178396463480`, rol `MAIN`, prefijo `/t/45`.
- Tema QA verificado: `gid://shopify/OnlineStoreTheme/178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.
- No se modificÃƒÂ³ Shopify.
- No se publicÃƒÂ³ ningÃƒÂºn tema.
- No se modificÃƒÂ³ MAIN.

## Resultado correcto

- Home ES, carrito ES y colecciÃƒÂ³n `/collections/ofertas`: assets `/t/46`, 0 assets `/t/45`, canonical/hreflang presentes, consola sin errores.
- Uploader ES/EN/FR/DE/NL desktop: inputs presentes, sincronizaciÃƒÂ³n correcta y evento `input_mural_outside` verificado con seÃƒÂ±al QA.
- Producto estÃƒÂ¡ndar `lineas-noridcas-verde`: inputs presentes, sincronizaciÃƒÂ³n correcta y evento `input_mural_outside` verificado.
- Home mÃƒÂ³vil ES 390: sin errores de consola y sin fuga CSS visible de home.

## Incidencia

`INCORRECTO`

- Uploader FR mÃƒÂ³vil: overflow +57 px a 390 y +72 px a 375.
- Uploader NL mÃƒÂ³vil: overflow +37 px a 390 y +52 px a 375.
- Causa probable acotada a `shopify-section--product-recommendations` / `scroll-carousel` / `REVEAL-ITEMS` en `sections/related-products.liquid`.
- No corresponde al bloque legal corregido en `MW-TECH-MOBILE-OVERFLOW-LEGAL-FLEX-010C2`.

## PrÃƒÂ³ximo lote recomendado

`MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3`

## Evidencia

- QA: `qa-MW-TECH-QA-REGRESSION-MATRIX-010Z-2026-06-25.md`.
- Propuesta: `propuesta-lote-MW-TECH-MOBILE-OVERFLOW-RELATED-PRODUCTS-010C3-2026-06-25.md`.

---
# 2026-06-25 15:48:06 +02:00 - Ejecucion MW-TECH-DYNAMIC-MEASURE-TRACKING-EXTERNAL-DIRECT-010A2D

## Estado

`CORREGIDO Y VERIFICADO`

## Aprobacion y alcance

- Aprobacion exacta recibida: `APROBADO LOTE MW-TECH-DYNAMIC-MEASURE-TRACKING-EXTERNAL-DIRECT-010A2D`.
- Tema afectado: `gid://shopify/OnlineStoreTheme/178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.
- Archivo afectado: `snippets/external-selectors.liquid`.
- MAIN `gid://shopify/OnlineStoreTheme/178396463480` no fue modificado.
- No se publico ningun tema.

## Cambio ejecutado

- `snippets/external-selectors.liquid` paso de MD5 `8a9c233bca52da58ce59fffc3aee8359`, size `10199`, a MD5 `95266feda1603e9c9ef028f0dae74c6f`, size `11109`.
- Se aÃƒÂ±adio `pushInputMuralOutsideEvent` junto a los listeners funcionales de `externalWidthInput` y `externalHeightInput`.
- Se aÃƒÂ±adio seÃƒÂ±al QA `data-mw010a2d-*` limitada a URLs con `mwqa=010a2d`.
- No se modifico `snippets/srolling_bar_menu.liquid`.

## Verificacion almacenada

`VERIFICADO Y CORRECTO`

- `themeFilesUpsert`: `userErrors=[]`.
- Lectura posterior: tema `UNPUBLISHED`, `processing=false`, `processingFailed=false`.
- MD5 almacenado: `95266feda1603e9c9ef028f0dae74c6f`.

## QA publica

`CORREGIDO Y VERIFICADO`

- URL critica ES `custom-file-uploader` en `/t/46`: anchura y altura generan evento `input_mural_outside`.
- Prueba secuencial ES: count `2 -> 3 -> 4`; `width=422`, `height=322`; superficie correcta.
- Mini-QA ES/EN/FR/DE/NL en URL critica: eventos verificados, assets `/t/46`, campos presentes, consola sin errores.
- Producto estandar `lineas-noridcas-verde`: carga en `/t/46`, sin errores de consola, anchura verificada; altura no reescrita por limitacion del navegador de QA.

## Reversion disponible

Restaurar `snippets/external-selectors.liquid` al MD5 `8a9c233bca52da58ce59fffc3aee8359`, size `10199`, y confirmar por GraphQL.

## Evidencia

- QA: `qa-MW-TECH-DYNAMIC-MEASURE-TRACKING-EXTERNAL-DIRECT-010A2D-2026-06-25.md`.
- Propuesta actualizada: `propuesta-lote-MW-TECH-DYNAMIC-MEASURE-TRACKING-EXTERNAL-DIRECT-010A2D-2026-06-25.md`.

---
# 2026-06-25 16:05:00 +02:00 - Diagnostico MW-TECH-DYNAMIC-MEASURE-TRACKING-DIAG-010A2C

## Estado

`REQUIERE DECISION HUMANA`

## Alcance

- Diagnostico de solo lectura.
- MAIN verificado: `gid://shopify/OnlineStoreTheme/178396463480`, rol `MAIN`, prefijo `/t/45`.
- Auxiliar verificado: `gid://shopify/OnlineStoreTheme/178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.
- No se modifico Shopify.
- No se publico ningun tema.
- No se modifico MAIN.

## Resultado

- `snippets/external-selectors.liquid` del auxiliar: MD5 `8a9c233bca52da58ce59fffc3aee8359`, size `10199`; coincide con MAIN tras rollback R1.
- `snippets/srolling_bar_menu.liquid` del auxiliar: MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`, size `8539`.
- QA preview `/t/46` en `custom-file-uploader`: campos externos e internos presentes.
- Prueba `401 x 301`: sincronizacion y superficie correctas.
- Eventos `input_mural_outside`: 0 en QA soportada.
- Errores de consola: 0.

## Diagnostico

`INCORRECTO`

El tracking dinamico sigue pendiente. No se recomienda reutilizar el candidato `010A2B`. Se crea propuesta de lote nuevo:

`MW-TECH-DYNAMIC-MEASURE-TRACKING-EXTERNAL-DIRECT-010A2D`

## Evidencia

- Diagnostico: `diagnostico-MW-TECH-DYNAMIC-MEASURE-TRACKING-DIAG-010A2C-2026-06-25.md`.
- Propuesta: `propuesta-lote-MW-TECH-DYNAMIC-MEASURE-TRACKING-EXTERNAL-DIRECT-010A2D-2026-06-25.md`.

---
# 2026-06-25 15:08:00 +02:00 - Rollback verificado MW-TECH-ROLLBACK-EXTERNAL-SELECTORS-010A2B-R1

## Estado

`CORREGIDO Y VERIFICADO`

## Aprobacion y alcance

- Aprobacion exacta recibida: `APROBADO LOTE MW-TECH-ROLLBACK-EXTERNAL-SELECTORS-010A2B-R1`.
- Tema afectado: `gid://shopify/OnlineStoreTheme/178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.
- Archivo afectado: `snippets/external-selectors.liquid`.
- MAIN no fue modificado ni publicado.

## Cambio ejecutado

- `snippets/external-selectors.liquid` restaurado desde respaldo local mediante editor Shopify.
- MD5 antes del rollback R1: `46dc6dcb927f9e8005d0c3bdcba4751d`, size `11062`.
- MD5 final verificado: `8a9c233bca52da58ce59fffc3aee8359`, size `10199`.
- `snippets/srolling_bar_menu.liquid` se mantiene verificado en MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`, size `8539`.

## Verificacion almacenada

`VERIFICADO Y CORRECTO`

- Tema `178399019384`: `UNPUBLISHED`, `processing=false`, `processingFailed=false`.
- `snippets/external-selectors.liquid`: MD5 `8a9c233bca52da58ce59fffc3aee8359`.
- `snippets/srolling_bar_menu.liquid`: MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`.

## QA publico

`VERIFICADO Y CORRECTO`

- Preview del producto `custom-file-uploader` con assets `/t/46`.
- Inputs externos e internos presentes.
- Prueba `407 x 307`: sincronizacion correcta y superficie `4.07m x 3.07m = 12.49 mÃ‚Â²`.
- Funciones experimentales de `external-selectors.liquid` del candidato 010A2B (`pushExternalWidthTracking`, `pushExternalHeightTracking`) ausentes.
- `window.dataLayer` no creado e `input_mural_outside = 0`; esto confirma que el tracking sigue pendiente, no que este resuelto.

## Estado posterior

- Riesgo critico del tema auxiliar resuelto.
- Tracking dinamico sigue `INCORRECTO`.
- No publicar el tema auxiliar como solucion de tracking.
- Cualquier nueva intervencion debe partir de un lote nuevo y acotado.

## Evidencia

- Documento QA: `qa-MW-TECH-ROLLBACK-EXTERNAL-SELECTORS-010A2B-R1-2026-06-25.md`.

---
# 2026-06-25 14:35:00 +02:00 - Ejecucion fallida y reversion parcial MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B

## Estado

`RIESGO CRITICO`

## Aprobacion y alcance

- Aprobacion exacta recibida: `APROBADO LOTE MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B`.
- Tema afectado: `gid://shopify/OnlineStoreTheme/178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.
- MAIN `gid://shopify/OnlineStoreTheme/178396463480` confirmado como `MAIN` y no modificado.
- Archivos afectados: `snippets/external-selectors.liquid` y `snippets/srolling_bar_menu.liquid`.

## Ejecucion

- `themeFilesUpsert` validado contra schema.
- `snippets/external-selectors.liquid` paso de MD5 `8a9c233bca52da58ce59fffc3aee8359` a `46dc6dcb927f9e8005d0c3bdcba4751d`.
- `snippets/srolling_bar_menu.liquid` paso de MD5 `7d6dfb8df5e4b9ef813eca32aaebc237` a `eec87a2c8dc9790a6c499a72e5323337`.
- Shopify acepto la mutacion inicial sin `userErrors`.

## QA

`INCORRECTO`

- URL probada: `https://www.matchwalls.com/products/custom-file-uploader?preview_theme_id=178399019384&mwqa=010a2b_run_20260625`.
- Assets `/t/46`: `VERIFICADO Y CORRECTO`.
- Sincronizacion de medidas `405 x 305`: `VERIFICADO Y CORRECTO`.
- Superficie visual: `4.05m x 3.05m = 12.35 mÃ‚Â²`.
- Errores de consola: `0`.
- `window.dataLayer`: no creado.
- Eventos `input_mural_outside`: `0`.

## Reversion

`INCOMPLETO`

- `snippets/srolling_bar_menu.liquid` revertido y verificado a MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`.
- `snippets/external-selectors.liquid` sigue en MD5 `46dc6dcb927f9e8005d0c3bdcba4751d`.
- Dos intentos de reversion de `external-selectors.liquid` mediante `themeFilesUpsert` fueron rechazados por Shopify con `El contenido incluye caracteres no validos`.
- Respaldo local de `external-selectors.liquid`: MD5 `8a9c233bca52da58ce59fffc3aee8359`, tamaÃƒÂ±o `10199`, sin caracteres de control invalidos.
- MAIN conserva `external-selectors.liquid` con MD5 `8a9c233bca52da58ce59fffc3aee8359`.

## Estado real final

- Tema `178399019384`: `UNPUBLISHED`, `processing=false`, `processingFailed=false`.
- `snippets/external-selectors.liquid`: `RIESGO CRITICO`; MD5 `46dc6dcb927f9e8005d0c3bdcba4751d`, size `11062`.
- `snippets/srolling_bar_menu.liquid`: `VERIFICADO Y CORRECTO`; MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`, size `8539`.

## Decisiones pendientes

`REQUIERE DECISION HUMANA`

- No avanzar sobre el tema auxiliar `178399019384` hasta revertir manualmente `snippets/external-selectors.liquid` o aprobar un nuevo lote que parta del candidato actual.
- No publicar este tema.
- No usar 010A2B como base para MAIN.

## Evidencia

- Documento QA: `qa-MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B-2026-06-25.md`.

---
# 2026-06-25 13:58:54 +02:00 - Diagnostico MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B

## Estado

`REQUIERE DECISION HUMANA`

## Resultado de solo lectura

- Revisado el historial de `MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2`.
- Confirmado que `010A2` fue `INCORRECTO`, fallo con 0 eventos `input_mural_outside` y quedo revertido.
- Consulta Admin GraphQL de solo lectura validada contra esquema.
- MAIN actual confirmado: `gid://shopify/OnlineStoreTheme/178396463480`, rol `MAIN`, prefijo `/t/45`.
- Auxiliar confirmado: `gid://shopify/OnlineStoreTheme/178399019384`, rol `UNPUBLISHED`, prefijo `/t/46`.
- Rollback confirmado: `gid://shopify/OnlineStoreTheme/178383749496`, rol `UNPUBLISHED`, prefijo `/t/43`.
- `snippets/external-selectors.liquid` en MAIN, auxiliar y rollback: MD5 `8a9c233bca52da58ce59fffc3aee8359`, 10199 bytes.
- `snippets/srolling_bar_menu.liquid` en MAIN y rollback: MD5 `c254cf711a7706dc21ece2f2ad31acea`, 8581 bytes.
- `snippets/srolling_bar_menu.liquid` en auxiliar: MD5 `7d6dfb8df5e4b9ef813eca32aaebc237`, 8539 bytes.

## QA publica de diagnostico

- URL probada: `https://www.matchwalls.com/products/custom-file-uploader?preview_theme_id=178399019384&mwqa=010a2b_diag_20260625`.
- Assets del auxiliar `/t/46`: `VERIFICADO Y CORRECTO`.
- Campos `#external-width`, `#external-height`, `#width` y `#height`: 1 cada uno.
- Cambio `402 x 302`: inputs internos sincronizados y superficie `4.02m x 3.02m = 12.14 mÃ‚Â²`.
- `window.dataLayer`: no creado.
- Eventos `input_mural_outside`: 0.
- Errores de consola: 0.

## Diagnostico

`INCORRECTO`

El tracking de medida dinamica permanece roto. La evidencia indica que `snippets/external-selectors.liquid` es el propietario funcional de los inputs de medida y debe ser el punto de intervencion. `snippets/srolling_bar_menu.liquid` contiene tracking de medida en el header global, pero no genera el evento en la prueba publica.

## Propuesta creada

- `diagnostico-MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B-2026-06-25.md`.
- `propuesta-lote-MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2B-2026-06-25.md`.

## Cambios realizados

- No se modifico Shopify.
- No se publico ningun tema.
- No se modifico MAIN.
- No se ejecutaron mutaciones.

---
# Registro de cambios ejecutados

Todos los cambios se realizan mediante Shopify Admin API con operaciones validadas y lectura posterior. No se muestran ni almacenan credenciales.

> **Alcance:** este documento registra ÃƒÆ’Ã‚Âºnicamente lotes concretos ejecutados.
> No certifica que toda la web, todo el catÃƒÆ’Ã‚Â¡logo o todos los idiomas estÃƒÆ’Ã‚Â©n
> optimizados. El programa SEO/GEO permanece **EN CURSO - NO CERRADO**.

## 15 de junio de 2026

### Lote MW-SEO-001: pÃƒÆ’Ã‚Â¡ginas cruzadas

**Estado:** ejecutado y verificado internamente.

**Recursos:**

- `gid://shopify/Page/106278387939` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â `MÃƒÆ’Ã‚Â©todos de pago`
- `gid://shopify/Page/106278256867` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â `Conoce nuestros productos`

**Cambios ejecutados:**

- Restaurado el cuerpo espaÃƒÆ’Ã‚Â±ol de `MÃƒÆ’Ã‚Â©todos de pago`.
- Restaurado el cuerpo espaÃƒÆ’Ã‚Â±ol de `Conoce nuestros productos`.
- No se modificaron tÃƒÆ’Ã‚Â­tulos, handles, plantillas ni estado de publicaciÃƒÆ’Ã‚Â³n.
- Registrados en `MÃƒÆ’Ã‚Â©todos de pago` los cuerpos, tÃƒÆ’Ã‚Â­tulos y metadatos EN, FR, DE y NL que estaban publicados errÃƒÆ’Ã‚Â³neamente en la pÃƒÆ’Ã‚Â¡gina de productos.
- Conservados los handles localizados existentes de la pÃƒÆ’Ã‚Â¡gina de pagos.

**VerificaciÃƒÆ’Ã‚Â³n:**

- Las dos operaciones `pageUpdate` terminaron sin `userErrors`.
- Las 16 traducciones registradas en la pÃƒÆ’Ã‚Â¡gina de pagos terminaron sin `userErrors`.
- La lectura posterior confirmÃƒÆ’Ã‚Â³ que los cuerpos espaÃƒÆ’Ã‚Â±oles corresponden de nuevo a cada pÃƒÆ’Ã‚Â¡gina.
- Las traducciones EN, FR, DE y NL de pagos figuran como no desactualizadas.

**Pendiente:**

- Sustituir en `Conoce nuestros productos` los contenidos EN, FR, DE y NL de pagos que todavÃƒÆ’Ã‚Â­a permanecen como traducciones desactualizadas.
- Validar comercialmente los mÃƒÆ’Ã‚Â©todos de pago, disponibilidad por paÃƒÆ’Ã‚Â­s y afirmaciones de seguridad antes de una reescritura definitiva.

### Lote MW-SEO-002: pÃƒÆ’Ã‚Â¡ginas corporativas y traducciones

**Estado:** ejecutado y verificado internamente.

**Cambios ejecutados:**

- Reescrito y traducido el contenido de `Conoce nuestros productos` en ES, EN, FR, DE y NL.
- Registradas traducciones EN, FR, DE y NL de `MÃƒÆ’Ã‚Â©todos de pago`.
- Eliminados los H1 incluidos dentro del cuerpo de ambas pÃƒÆ’Ã‚Â¡ginas para evitar duplicarlos cuando se publique la plantilla corregida.
- No se modificaron handles, URLs, redirecciones ni estado de publicaciÃƒÆ’Ã‚Â³n.

**LimitaciÃƒÆ’Ã‚Â³n verificada:**

- El tema principal actual no muestra `page.content` en estas plantillas. Los tÃƒÆ’Ã‚Â­tulos y metadatos estÃƒÆ’Ã‚Â¡n activos, pero los cuerpos corregidos requieren publicar una plantilla previamente validada.

### Lote MW-SEO-003: catÃƒÆ’Ã‚Â¡logo piloto Vista Serena y Whispering Woods

**Estado:** ejecutado y verificado internamente.

**Cambios ejecutados:**

- Corregidos los tÃƒÆ’Ã‚Â­tulos SEO espaÃƒÆ’Ã‚Â±oles de los cinco productos Vista Serena.
- Resincronizados tÃƒÆ’Ã‚Â­tulos y metadatos EN, FR, DE y NL de Vista Serena.
- Resincronizados tÃƒÆ’Ã‚Â­tulos y metadatos prioritarios de siete productos Whispering Woods.
- Conservadas como pendientes las descripciones FR y NL que requieren reescritura editorial; no se marcaron artificialmente como correctas.
- No se modificaron handles, URLs, imÃƒÆ’Ã‚Â¡genes, inventario ni reglas comerciales.

### Lote MW-SEO-004: hotfix de datos estructurados

**Estado:** preparado y verificado en tema no publicado; pendiente de publicaciÃƒÆ’Ã‚Â³n manual.

**Tema:** `SEO schema hotfix - 2026-06-15`.

**Cambios preparados:**

- EliminaciÃƒÆ’Ã‚Â³n del `AggregateRating` fijo y no demostrable de Organization.
- SupresiÃƒÆ’Ã‚Â³n de GTIN cuando el barcode coincide con el ID interno de la variante.
- CorrecciÃƒÆ’Ã‚Â³n del breadcrumb de artÃƒÆ’Ã‚Â­culos.
- ConservaciÃƒÆ’Ã‚Â³n de Product, Offer, SKU, disponibilidad, Breadcrumb, WebSite y Organization.

**VerificaciÃƒÆ’Ã‚Â³n:**

- Producto de prueba: JSON-LD vÃƒÆ’Ã‚Â¡lido, cuatro ofertas, cuatro SKU, cero GTIN falsos y un H1.
- Home: WebSite y Organization vÃƒÆ’Ã‚Â¡lidos, sin AggregateRating no demostrable.
- ArtÃƒÆ’Ã‚Â­culo: BlogPosting y BreadcrumbList vÃƒÆ’Ã‚Â¡lidos; el tercer breadcrumb corresponde al artÃƒÆ’Ã‚Â­culo.
- No se ha publicado ni modificado el tema principal.

### AuditorÃƒÆ’Ã‚Â­as de escala verificadas, sin mutaciones

- 58 colecciones geogrÃƒÆ’Ã‚Â¡ficas con handle `comprar-papel-pintado-*`.
- Madrid, Barcelona, ParÃƒÆ’Ã‚Â­s y Toulouse muestran 73 productos y el mismo surtido inicial.
- Se detectÃƒÆ’Ã‚Â³ mezcla de idiomas y traducciones automÃƒÆ’Ã‚Â¡ticas defectuosas en pÃƒÆ’Ã‚Â¡ginas geogrÃƒÆ’Ã‚Â¡ficas marcadas como actualizadas.
- `Todos los Papeles Pintados` (`/collections/murales`) excluye por regla el tipo `Papel Pintado`; no se cambiÃƒÆ’Ã‚Â³ por su gran impacto comercial.
- En una muestra de 50 productos activos y 65 variantes, 65/65 barcodes coinciden con el ID interno de Shopify. No se modificaron los barcodes.

### Lote MW-SEO-005: quick wins de colecciÃƒÆ’Ã‚Â³n y familia BambÃƒÆ’Ã‚Âºze

**Estado:** ejecutado y verificado internamente.

**Cambios ejecutados:**

- Corregido el tÃƒÆ’Ã‚Â­tulo espaÃƒÆ’Ã‚Â±ol de la colecciÃƒÆ’Ã‚Â³n `Papeles Pintados ContemporÃƒÆ’Ã‚Â¡neos`.
- Resincronizados sus tÃƒÆ’Ã‚Â­tulos EN, FR, DE y NL; mejorado tambiÃƒÆ’Ã‚Â©n el metatÃƒÆ’Ã‚Â­tulo NL.
- Corregidos espacios dobles en los tÃƒÆ’Ã‚Â­tulos y metatÃƒÆ’Ã‚Â­tulos espaÃƒÆ’Ã‚Â±oles de `BambÃƒÆ’Ã‚Âºze Negro`, `BambÃƒÆ’Ã‚Âºze Beige` y `BambÃƒÆ’Ã‚Âºze Blanco y Negro`.
- Resincronizados tÃƒÆ’Ã‚Â­tulos y metatÃƒÆ’Ã‚Â­tulos EN, FR, DE y NL de esos tres murales.

**GarantÃƒÆ’Ã‚Â­as:**

- No se modificaron handles, URLs, reglas de colecciÃƒÆ’Ã‚Â³n, productos asociados ni descripciones de producto.
- Todas las operaciones terminaron sin `userErrors`.
- La lectura posterior confirmÃƒÆ’Ã‚Â³ que los campos traducidos revisados no estÃƒÆ’Ã‚Â¡n desactualizados.

### Lote MW-SEO-006: familia LÃƒÆ’Ã‚Â­neas NÃƒÆ’Ã‚Â³rdicas

**Estado:** ejecutado y verificado internamente.

**ÃƒÆ’Ã‚Âmbito:** diez murales activos de la familia.

**Cambios ejecutados:**

- Corregido `LÃƒÆ’Ã‚Â­neas NÃƒÆ’Ã‚Â³ridcas` a `LÃƒÆ’Ã‚Â­neas NÃƒÆ’Ã‚Â³rdicas` en tÃƒÆ’Ã‚Â­tulos visibles, tÃƒÆ’Ã‚Â­tulos SEO y descripciones SEO espaÃƒÆ’Ã‚Â±olas.
- Eliminados espacios dobles en los tÃƒÆ’Ã‚Â­tulos afectados.
- Reescritos y sincronizados tÃƒÆ’Ã‚Â­tulos, metatÃƒÆ’Ã‚Â­tulos y metadescripciones EN, FR, DE y NL.
- Corregida durante el propio lote una sustituciÃƒÆ’Ã‚Â³n temporal de descripciones SEO causada por el comportamiento de reemplazo completo de `SEOInput`.

**GarantÃƒÆ’Ã‚Â­as:**

- No se modificaron handles, URLs, redirecciones, inventario, imÃƒÆ’Ã‚Â¡genes, variantes ni muestras.
- Las diez descripciones SEO espaÃƒÆ’Ã‚Â±olas fueron comprobadas como no vacÃƒÆ’Ã‚Â­as.
- Todos los tÃƒÆ’Ã‚Â­tulos y metadatos traducidos revisados quedaron con `outdated: false`.
- Todas las mutaciones terminaron sin `userErrors`.

**VerificaciÃƒÆ’Ã‚Â³n pÃƒÆ’Ã‚Âºblica representativa:**

- `/products/lineas-noridcas-marron`: H1 `LÃƒÆ’Ã‚Â­neas NÃƒÆ’Ã‚Â³rdicas MarrÃƒÆ’Ã‚Â³n`, title y metadescripciÃƒÆ’Ã‚Â³n corregidos, canonical sin cambios.
- `/en/products/brown-noridcas-lines`: H1 `Nordic Lines Brown`, title y metadescripciÃƒÆ’Ã‚Â³n corregidos, canonical sin cambios.
- `/fr/products/lignes-brunes-de-noridcas`: H1 `Lignes Nordiques Marron`, title y metadescripciÃƒÆ’Ã‚Â³n corregidos, canonical sin cambios.
- `/de/products/brown-noridcas-linien`: H1 `Nordische Linien Braun`, title y metadescripciÃƒÆ’Ã‚Â³n corregidos, canonical sin cambios.
- `/nl/products/bruine-noridcas-lijnen`: title y metadescripciÃƒÆ’Ã‚Â³n corregidos; la comprobaciÃƒÆ’Ã‚Â³n posterior confirmÃƒÆ’Ã‚Â³ tambiÃƒÆ’Ã‚Â©n el H1 renderizado.
- `/products/bambuze-negro`: H1, title, metadescripciÃƒÆ’Ã‚Â³n y canonical correctos.
- `/collections/lo-mas-contemporaneo-murales`: H1 `Papeles Pintados ContemporÃƒÆ’Ã‚Â¡neos`, metadatos y canonical correctos.

### ReauditorÃƒÆ’Ã‚Â­a y correcciÃƒÆ’Ã‚Â³n del lote MW-SEO-004

**Estado:** corregido y verificado en tema no publicado; no publicado.

- Se comprobÃƒÆ’Ã‚Â³ que la primera versiÃƒÆ’Ã‚Â³n del hotfix reescribÃƒÆ’Ã‚Â­a mÃƒÆ’Ã‚Â¡s campos de schema de los previstos.
- Se sustituyÃƒÆ’Ã‚Â³ por una versiÃƒÆ’Ã‚Â³n mÃƒÆ’Ã‚Â­nima derivada del schema MAIN.
- Checksum validado local/Shopify: `58417e4825aa3d4570a6646f292aaedc`.
- Se conservan SKU, peso, ImageObject, Offer, disponibilidad, home BreadcrumbList y todos los campos existentes de BlogPosting.
- Se eliminan ÃƒÆ’Ã‚Âºnicamente GTIN/MPN basados en IDs internos, AggregateRating corporativo fijo y el nombre errÃƒÆ’Ã‚Â³neo del tercer breadcrumb de artÃƒÆ’Ã‚Â­culos.
- Google Rich Results Test detectÃƒÆ’Ã‚Â³ 3 elementos vÃƒÆ’Ã‚Â¡lidos y ningÃƒÆ’Ã‚Âºn error crÃƒÆ’Ã‚Â­tico.
- Home, producto ES/EN, artÃƒÆ’Ã‚Â­culo, carrito y formularios fueron comprobados en escritorio y mÃƒÆ’Ã‚Â³vil.
- `config/settings_data.json` coincide con MAIN; App Embeds no cambiaron.
- Shopify bloqueÃƒÆ’Ã‚Â³ el borrado de `snippets/microdata-schema-original.liquid`; permanece como copia sin uso del schema MAIN.
- No se modificÃƒÆ’Ã‚Â³ ni publicÃƒÆ’Ã‚Â³ el tema MAIN.

**Evidencia detallada:** `qa-hotfix-schema-2026-06-15.md`.

### AprobaciÃƒÆ’Ã‚Â³n de publicaciÃƒÆ’Ã‚Â³n del lote MW-SEO-004

**Estado:** aprobado por Daniel; pendiente de publicaciÃƒÆ’Ã‚Â³n manual.

- Daniel aprobÃƒÆ’Ã‚Â³ publicar ÃƒÆ’Ã‚Âºnicamente `SEO schema hotfix - 2026-06-15`.
- Daniel aprobÃƒÆ’Ã‚Â³ conservar temporalmente la copia auxiliar sin uso.
- La comprobaciÃƒÆ’Ã‚Â³n final confirmÃƒÆ’Ã‚Â³ rol `UNPUBLISHED`, ausencia de fallos de procesamiento y checksum funcional `58417e4825aa3d4570a6646f292aaedc`.
- La conexiÃƒÆ’Ã‚Â³n disponible bloquea por seguridad la publicaciÃƒÆ’Ã‚Â³n automÃƒÆ’Ã‚Â¡tica de temas.
- `SEO-GEO staging - 2026-06-15` continÃƒÆ’Ã‚Âºa expresamente excluido de publicaciÃƒÆ’Ã‚Â³n.

### Lote MW-SEO-007: primeras URLs estratÃƒÆ’Ã‚Â©gicas solicitadas

**Estado:** ejecutado parcialmente y verificado pÃƒÆ’Ã‚Âºblicamente; no equivale a cierre global.

**Recursos modificados:**

- Producto `custom-file-uploader`.
- ColecciÃƒÆ’Ã‚Â³n `murales-mas-vendidos-mural`.
- PÃƒÆ’Ã‚Â¡gina `contact`.

**Cambios ejecutados:**

- Reescritos tÃƒÆ’Ã‚Â­tulo, descripciÃƒÆ’Ã‚Â³n y metadatos del producto de personalizaciÃƒÆ’Ã‚Â³n en ES, EN, FR, DE y NL.
- Reescritos tÃƒÆ’Ã‚Â­tulo, descripciÃƒÆ’Ã‚Â³n y metadatos de la colecciÃƒÆ’Ã‚Â³n de papeles pintados y murales mÃƒÆ’Ã‚Â¡s vendidos en ES, EN, FR, DE y NL.
- Corregida la pÃƒÆ’Ã‚Â¡gina de contacto en ES, EN, FR, DE y NL, eliminando el H1 duplicado y mejorando tÃƒÆ’Ã‚Â­tulos, contenido y metadatos.
- No se modificaron handles, URLs, redirecciones, reglas de colecciÃƒÆ’Ã‚Â³n, productos asociados, variantes ni estado de publicaciÃƒÆ’Ã‚Â³n.

**VerificaciÃƒÆ’Ã‚Â³n pÃƒÆ’Ã‚Âºblica:**

- Contacto muestra un ÃƒÆ’Ã‚Âºnico H1 y metadatos localizados correctos en los cinco idiomas prioritarios.
- La colecciÃƒÆ’Ã‚Â³n muestra el nuevo H1, descripciÃƒÆ’Ã‚Â³n y metadatos.
- El producto de personalizaciÃƒÆ’Ã‚Â³n muestra los nuevos metadatos, pero su plantilla publicada continÃƒÆ’Ã‚Âºa ocultando la descripciÃƒÆ’Ã‚Â³n guardada y mantiene un H1 fijo distinto del tÃƒÆ’Ã‚Â­tulo del producto.

**Estado real:**

- Contacto: correcciÃƒÆ’Ã‚Â³n editorial y tÃƒÆ’Ã‚Â©cnica bÃƒÆ’Ã‚Â¡sica completada; pendiente QA integral de conversiÃƒÆ’Ã‚Â³n, accesibilidad y GEO/AEO.
- ColecciÃƒÆ’Ã‚Â³n mÃƒÆ’Ã‚Â¡s vendidos: contenido principal corregido; handles localizados y arquitectura pendientes de anÃƒÆ’Ã‚Â¡lisis con redirecciones.
- Producto de personalizaciÃƒÆ’Ã‚Â³n: datos corregidos; pendiente correcciÃƒÆ’Ã‚Â³n y QA de plantilla en tema no publicado.

### AuditorÃƒÆ’Ã‚Â­a de plantillas de pÃƒÆ’Ã‚Â¡ginas prioritarias

**Estado:** verificado; correcciones de tema aÃƒÆ’Ã‚Âºn no publicadas.

- La pÃƒÆ’Ã‚Â¡gina pÃƒÆ’Ã‚Âºblica `muestras` usa `templates/page.muestras-2.json`, no `templates/page.muestras.json`.
- `templates/page.muestras-2.json`: la secciÃƒÆ’Ã‚Â³n `main-page` estÃƒÆ’Ã‚Â¡ desactivada; ES muestra texto fijo sin H1 y EN aparece sin contenido principal.
- `templates/page.guias-de-instalacion.json`: la secciÃƒÆ’Ã‚Â³n `main-page` estÃƒÆ’Ã‚Â¡ desactivada y el contenido principal SEO/HowTo no es visible.
- La guÃƒÆ’Ã‚Â­a de instalaciÃƒÆ’Ã‚Â³n conserva enlaces `file:///C:/Users/...` que no son accesibles para clientes ni buscadores.
- Corregido el HTML roto de la traducciÃƒÆ’Ã‚Â³n neerlandesa guardada de la guÃƒÆ’Ã‚Â­a.
- Se probÃƒÆ’Ã‚Â³ una activaciÃƒÆ’Ã‚Â³n mÃƒÆ’Ã‚Â­nima en `templates/page.muestras.json`, se comprobÃƒÆ’Ã‚Â³ que no era la plantilla asignada y se revirtiÃƒÆ’Ã‚Â³.
- La lectura posterior muestra el mismo cuerpo funcional que MAIN, con `main-page` desactivado, pero el checksum de staging difiere por la reescritura del archivo. No afecta producciÃƒÆ’Ã‚Â³n y debe conservarse como diferencia conocida hasta el siguiente QA del tema auxiliar.
- El tema MAIN no se modificÃƒÆ’Ã‚Â³.

### Lote MW-SEO-008: pÃƒÆ’Ã‚Â¡ginas estratÃƒÆ’Ã‚Â©gicas y colecciones de intenciÃƒÆ’Ã‚Â³n

**Estado:** ejecutado parcialmente y verificado mediante lectura posterior de Shopify; QA pÃƒÆ’Ã‚Âºblica pendiente en las colecciones.

**Cambios ejecutados:**

- Corregido el HTML roto de la guÃƒÆ’Ã‚Â­a de instalaciÃƒÆ’Ã‚Â³n neerlandesa.
- Neutralizadas las metadescripciones EN, FR, DE y NL de `Sobre nosotros` para retirar promesas no verificadas de envÃƒÆ’Ã‚Â­o gratuito, nÃƒÆ’Ã‚Âºmero de diseÃƒÆ’Ã‚Â±os y materiales.
- Corregido el tÃƒÆ’Ã‚Â­tulo francÃƒÆ’Ã‚Â©s de `Sobre nosotros`.
- Neutralizadas las metadescripciones EN, FR, DE y NL de `Profesionales` para retirar promesas no verificadas de descuentos, muestras y ventajas.
- Reescrita la colecciÃƒÆ’Ã‚Â³n `Papeles pintados para espacios pÃƒÆ’Ã‚Âºblicos` en ES, EN, FR, DE y NL, eliminando la afirmaciÃƒÆ’Ã‚Â³n no demostrada de aptitud para exteriores.
- Reescrita la colecciÃƒÆ’Ã‚Â³n `Papel Pintado Floral` en ES, EN, FR, DE y NL, corrigiendo gramÃƒÆ’Ã‚Â¡tica y retirando enumeraciones de materiales no verificadas para toda la colecciÃƒÆ’Ã‚Â³n.

**GarantÃƒÆ’Ã‚Â­as:**

- No se modificaron handles, URLs, redirecciones, reglas de colecciÃƒÆ’Ã‚Â³n, productos asociados, inventario ni temas publicados.
- Todas las mutaciones terminaron sin `userErrors`.
- Las traducciones registradas quedaron con `outdated: false`.

**Hallazgos pÃƒÆ’Ã‚Âºblicos crÃƒÆ’Ã‚Â­ticos del lote:**

- Muestras ES no tiene H1; Muestras EN no muestra contenido principal.
- Sobre nosotros FR y NL no muestran contenido principal; DE muestra una traducciÃƒÆ’Ã‚Â³n fija de baja calidad distinta del contenido guardado.
- FAQ ES tiene dos H1 y varios bloques `FAQPage`; FAQ EN no muestra contenido principal.
- Profesionales ES tiene dos H1 y publica ventajas y plazos pendientes de validaciÃƒÆ’Ã‚Â³n comercial.
- El footer ES contiene errores visibles y el enlace estacional `Black Friday 2024`; el footer EN conserva traducciones defectuosas.

### Lote MW-SEO-009: blog raÃƒÆ’Ã‚Â­z e inventario editorial

**Estado:** metadatos del blog raÃƒÆ’Ã‚Â­z ejecutados y verificados mediante lectura posterior; artÃƒÆ’Ã‚Â­culos pendientes de revisiÃƒÆ’Ã‚Â³n individual.

**Cambios ejecutados:**

- Reescritos metatÃƒÆ’Ã‚Â­tulo y metadescripciÃƒÆ’Ã‚Â³n del blog `InspiraciÃƒÆ’Ã‚Â³n` en ES, EN, FR, DE y NL.
- Reforzada la intenciÃƒÆ’Ã‚Â³n sobre papel pintado, murales, instalaciÃƒÆ’Ã‚Â³n y decoraciÃƒÆ’Ã‚Â³n sin aÃƒÆ’Ã‚Â±adir afirmaciones comerciales.
- No se modificaron tÃƒÆ’Ã‚Â­tulo visible, handles, artÃƒÆ’Ã‚Â­culos, fechas, autores ni estado de publicaciÃƒÆ’Ã‚Â³n.

**Hallazgos del inventario:**

- Existen 11 artÃƒÆ’Ã‚Â­culos publicados en el blog espaÃƒÆ’Ã‚Â±ol.
- Diez artÃƒÆ’Ã‚Â­culos no tienen resumen guardado.
- El artÃƒÆ’Ã‚Â­culo de cocina conserva el handle con error `transfroma`.
- Los handles del blog FR y DE conservan sufijos `inspiration-2` e `inspiration-1`.
- El artÃƒÆ’Ã‚Â­culo `Colores del Papel Pintado: Tendencias 2025` requiere actualizaciÃƒÆ’Ã‚Â³n de vigencia antes de considerarlo evergreen.

**Pendiente:**

- Revisar cada artÃƒÆ’Ã‚Â­culo en ES, EN, FR, DE y NL: contenido visible, autorÃƒÆ’Ã‚Â­a, fecha, resumen, title, meta description, H1-H3, enlaces internos, imÃƒÆ’Ã‚Â¡genes, Article schema y citabilidad GEO/AEO.
- Cambiar handles ÃƒÆ’Ã‚Âºnicamente con mapa de redirecciones y QA de hreflang.

### Control MW-SEO-010: lectura posterior y trazabilidad del backlog

**Estado:** verificado por consulta de solo lectura; sin mutaciones en Shopify.

- Confirmado que `Papel Pintado Floral` conserva el contenido y los metadatos corregidos en ES, EN, FR, DE y NL.
- Confirmado que `Papeles pintados para espacios pÃƒÆ’Ã‚Âºblicos` conserva el contenido y los metadatos corregidos en ES, EN, FR, DE y NL.
- Confirmado que el blog raÃƒÆ’Ã‚Â­z `InspiraciÃƒÆ’Ã‚Â³n` conserva sus metatÃƒÆ’Ã‚Â­tulos y metadescripciones corregidos en ES, EN, FR, DE y NL.
- Todas las traducciones leÃƒÆ’Ã‚Â­das de estos tres recursos figuran como `outdated: false`.
- Se aÃƒÆ’Ã‚Â±adieron al backlog los bloqueos crÃƒÆ’Ã‚Â­ticos de pÃƒÆ’Ã‚Â¡ginas localizadas vacÃƒÆ’Ã‚Â­as, FAQ, Profesionales, footer, colecciones con prestaciones no verificadas y auditorÃƒÆ’Ã‚Â­a individual de artÃƒÆ’Ã‚Â­culos.
- Se corrigieron identificadores duplicados en `auditoria-catalogo.csv`; no implica ningÃƒÆ’Ã‚Âºn cambio en el catÃƒÆ’Ã‚Â¡logo de Shopify.
- No se modificaron temas, menÃƒÆ’Ã‚Âºs, URLs, redirecciones, productos, inventario ni publicaciones.

### Lote MW-SEO-011: Profesionales y FAQ gobernadas

**Estado:** contenido guardado corregido en ES, EN, FR, DE y NL; bloqueo pÃƒÆ’Ã‚Âºblico de plantilla confirmado.

**Cambios ejecutados en Shopify:**

- Reescritos tÃƒÆ’Ã‚Â­tulo, cuerpo y metadatos de `Profesionales` en los cinco idiomas prioritarios.
- Retirados del contenido guardado descuentos, muestras gratuitas, envÃƒÆ’Ã‚Â­o prioritario, cantidades de catÃƒÆ’Ã‚Â¡logo, prestaciones tÃƒÆ’Ã‚Â©cnicas y respuesta en 24 horas no validadas.
- Reescritos tÃƒÆ’Ã‚Â­tulo, cuerpo y metadatos de `Preguntas frecuentes` en los cinco idiomas prioritarios.
- Retiradas del contenido guardado afirmaciones no validadas sobre materiales, lavabilidad, envÃƒÆ’Ã‚Â­o gratuito, plazos, pagos, financiaciÃƒÆ’Ã‚Â³n, garantÃƒÆ’Ã‚Â­as y devoluciones.
- Eliminados del cuerpo guardado de FAQ el H1 adicional y los scripts FAQPage duplicados.
- Todas las traducciones registradas terminaron sin `userErrors` y con `outdated: false`.
- No se modificaron handles, URLs, redirecciones, menÃƒÆ’Ã‚Âºs, temas, productos ni estado de publicaciÃƒÆ’Ã‚Â³n.

**VerificaciÃƒÆ’Ã‚Â³n y bloqueo pÃƒÆ’Ã‚Âºblico:**

- `Profesionales` usa `templates/page.profesionales.json`; MAIN y staging son idÃƒÆ’Ã‚Â©nticos, checksum `c02c11dc82a2d4ca90c756a5ae81d960`.
- `FAQ` usa `templates/page.faq.json`; MAIN y staging son idÃƒÆ’Ã‚Â©nticos, checksum `d515fbda6fcc75f79d06cdba2d7cc0dd`.
- Ambas plantillas contienen bloques de texto fijos que continÃƒÆ’Ã‚Âºan apareciendo pÃƒÆ’Ã‚Âºblicamente y no coinciden con el contenido editorial corregido.
- La FAQ pÃƒÆ’Ã‚Âºblica sigue mostrando afirmaciones comerciales y polÃƒÆ’Ã‚Â­ticas que requieren validaciÃƒÆ’Ã‚Â³n.
- La pÃƒÆ’Ã‚Â¡gina pÃƒÆ’Ã‚Âºblica de Profesionales sigue mostrando mensajes fijos sobre programa exclusivo, planes y ventajas.
- Ninguna de las dos URLs puede marcarse como completada hasta corregir y validar sus plantillas en un tema auxiliar.

### Lote MW-SEO-012: Colaboraciones, afiliaciÃƒÆ’Ã‚Â³n y prensa

**Estado:** contenido guardado corregido en ES, EN, FR, DE y NL; bloqueo pÃƒÆ’Ã‚Âºblico de plantilla confirmado.

**Cambios ejecutados en Shopify:**

- Reescritos tÃƒÆ’Ã‚Â­tulo, cuerpo y metadatos de `social-prensa-y-afiliacion` en los cinco idiomas prioritarios.
- Convertida la pÃƒÆ’Ã‚Â¡gina en un punto de contacto para propuestas de colaboraciÃƒÆ’Ã‚Â³n, consultas de afiliaciÃƒÆ’Ã‚Â³n y solicitudes de prensa.
- Retiradas del contenido guardado las promesas no validadas de comisiones, seguimiento en tiempo real, muestras gratuitas, ausencia de exclusividad, pagos mensuales y respuesta en 24-48 horas.
- Todas las traducciones registradas terminaron sin `userErrors` y con `outdated: false`.
- No se modificaron handles, URLs, redirecciones, menÃƒÆ’Ã‚Âºs, temas ni estado de publicaciÃƒÆ’Ã‚Â³n.

**VerificaciÃƒÆ’Ã‚Â³n y bloqueo pÃƒÆ’Ã‚Âºblico:**

- La pÃƒÆ’Ã‚Â¡gina usa `templates/page.social_prensa_afiliacion.json`.
- MAIN y staging son idÃƒÆ’Ã‚Â©nticos, checksum `78504a72d8cf077256e68dc4bbb1421f`, tamaÃƒÆ’Ã‚Â±o 17.323 bytes.
- La URL pÃƒÆ’Ã‚Âºblica inglesa sigue mostrando bloques fijos con comisiones, mensajes de ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œstart earningÃƒÂ¢Ã¢â€šÂ¬Ã‚Â, testimonios y permiso amplio para usar imÃƒÆ’Ã‚Â¡genes.
- La URL no puede marcarse como completada hasta corregir y validar su plantilla en un tema auxiliar.

## 16 de junio de 2026

### Control MW-GOV-001: aplicaciÃƒÆ’Ã‚Â³n de AGENTS.md y conciliaciÃƒÆ’Ã‚Â³n del historial

**Estado:** `VERIFICADO PERO MEJORABLE`.

**Acciones locales realizadas:**

- LeÃƒÆ’Ã‚Â­do ÃƒÆ’Ã‚Â­ntegramente `AGENTS.md` y adoptado como protocolo permanente para el proyecto y sus subcarpetas.
- LeÃƒÆ’Ã‚Â­dos los 29 archivos existentes dentro de `auditoria-seo-geo-matchwalls`, incluidas todas las matrices CSV completas, inventario de 7.932 URLs, sitemap, evidencias, scripts y archivo Liquid del hotfix.
- Conciliados los documentos histÃƒÆ’Ã‚Â³ricos con el registro de cambios mÃƒÆ’Ã‚Â¡s reciente.
- No se ha modificado Shopify durante este control.

**Incidencia de gobernanza detectada:**

- Los lotes `MW-SEO-011` y `MW-SEO-012` estÃƒÆ’Ã‚Â¡n documentados como cambios ejecutados en Shopify.
- En los documentos del proyecto no consta la aprobaciÃƒÆ’Ã‚Â³n literal requerida por el protocolo: `APROBADO LOTE [NOMBRE]`.
- Esta ausencia de evidencia de aprobaciÃƒÆ’Ã‚Â³n se clasifica como `INCORRECTO` y `REQUIERE DECISION HUMANA`.
- No se ejecutarÃƒÆ’Ã‚Â¡ ninguna nueva mutaciÃƒÆ’Ã‚Â³n, ampliaciÃƒÆ’Ã‚Â³n, reversiÃƒÆ’Ã‚Â³n ni modificaciÃƒÆ’Ã‚Â³n relacionada sin un lote presentado y aprobado conforme a `AGENTS.md`.

**Diferencias histÃƒÆ’Ã‚Â³ricas relevantes:**

- Algunos documentos iniciales describen estados anteriores al acceso interno y a los lotes ejecutados; deben tratarse como evidencia histÃƒÆ’Ã‚Â³rica, no como estado actual.
- Estados antiguos como `Verificado`, `Parcialmente corregido` o `Corregido` no siguen exactamente la clasificaciÃƒÆ’Ã‚Â³n obligatoria definida despuÃƒÆ’Ã‚Â©s en `AGENTS.md`. Se conservarÃƒÆ’Ã‚Â¡n como histÃƒÆ’Ã‚Â³rico hasta aprobar una normalizaciÃƒÆ’Ã‚Â³n documental especÃƒÆ’Ã‚Â­fica.

**Siguiente acciÃƒÆ’Ã‚Â³n autorizada:**

- Contrastar exclusivamente mediante consultas de lectura el estado real actual de Shopify y presentar el prÃƒÆ’Ã‚Â³ximo lote recomendado.

### Control MW-GOV-002: verificaciÃƒÆ’Ã‚Â³n de solo lectura del estado actual de Shopify

**Estado:** `INCOMPLETO`.

**Alcance y seguridad:**

- Consultas GraphQL exclusivamente de lectura, validadas contra el esquema de Shopify antes de ejecutarse.
- No se ejecutaron mutaciones, publicaciones, cambios de tema, traducciones, URLs, redirecciones, productos ni configuraciones.

**Temas verificados:**

- MAIN: `gid://shopify/OnlineStoreTheme/178379293048`, `Production - SEO fix AggregateRating (2026-06-12)`, rol `MAIN`, sin procesamiento pendiente.
- Staging: `gid://shopify/OnlineStoreTheme/178383585656`, `SEO-GEO staging - 2026-06-15`, rol `UNPUBLISHED`, sin procesamiento pendiente.
- Hotfix: `gid://shopify/OnlineStoreTheme/178383749496`, `SEO schema hotfix - 2026-06-15`, rol `UNPUBLISHED`, sin procesamiento pendiente.

**Diferencias completas MAIN frente a hotfix:**

- MAIN contiene 255 archivos y el hotfix 256.
- El hotfix aÃƒÆ’Ã‚Â±ade `snippets/microdata-schema-original.liquid`, copia exacta del schema MAIN con checksum `ae9c62e4abb80d1051cbea73b03f1107`.
- `snippets/microdata-schema.liquid` cambia de `ae9c62e4abb80d1051cbea73b03f1107` a `58417e4825aa3d4570a6646f292aaedc`.
- TambiÃƒÆ’Ã‚Â©n difieren `assets/country-flags.css`, `assets/sections.js` y `assets/theme.js`.
- El resto de los archivos comparados coincide por nombre y checksum.
- La causa y el efecto funcional de los tres activos compilados distintos se clasifican como `DECLARADO PERO NO VERIFICADO`.
- Hasta completar esa clasificaciÃƒÆ’Ã‚Â³n y repetir QA visual y funcional, la publicaciÃƒÆ’Ã‚Â³n del hotfix se clasifica como `RIESGO CRITICO`.

**Schema verificado por lectura del cÃƒÆ’Ã‚Â³digo:**

- El MAIN todavÃƒÆ’Ã‚Â­a contiene `AggregateRating` corporativo fijo y publica como GTIN cualquier barcode de longitud compatible.
- El hotfix elimina el `AggregateRating` corporativo fijo, cambia el breadcrumb de artÃƒÆ’Ã‚Â­culo para usar el tÃƒÆ’Ã‚Â­tulo del artÃƒÆ’Ã‚Â­culo y omite GTIN/MPN cuando `barcode == variant.id`.
- En una muestra actual de los primeros 50 productos activos, los 193 barcodes de variante leÃƒÆ’Ã‚Â­dos coinciden exactamente con el ID numÃƒÆ’Ã‚Â©rico interno de su variante.
- La correcciÃƒÆ’Ã‚Â³n del hotfix para excluir estos identificadores internos se clasifica como `VERIFICADO Y CORRECTO` a nivel de cÃƒÆ’Ã‚Â³digo.
- La validaciÃƒÆ’Ã‚Â³n de ejecuciÃƒÆ’Ã‚Â³n completa en Rich Results, carrito, formularios, App Embeds, mÃƒÆ’Ã‚Â³vil y escritorio no se ha repetido en este control y se clasifica como `INCOMPLETO`.

**Contenido y traducciones prioritarias:**

- Las pÃƒÆ’Ã‚Â¡ginas Contacto, Muestras, GuÃƒÆ’Ã‚Â­a de instalaciÃƒÆ’Ã‚Â³n, FAQ, Social/Prensa/AfiliaciÃƒÆ’Ã‚Â³n, Sobre nosotros y Profesionales estÃƒÆ’Ã‚Â¡n publicadas.
- Sus registros de traducciÃƒÆ’Ã‚Â³n prioritarios EN, FR, DE y NL figuran como `outdated: false`.
- Esto verifica existencia y vigencia tÃƒÆ’Ã‚Â©cnica, pero no calidad editorial ni coincidencia con el contenido pÃƒÆ’Ã‚Âºblico visible.
- Las plantillas de FAQ, Profesionales, Social/Prensa/AfiliaciÃƒÆ’Ã‚Â³n, Muestras y GuÃƒÆ’Ã‚Â­a de instalaciÃƒÆ’Ã‚Â³n son idÃƒÆ’Ã‚Â©nticas en MAIN, staging y hotfix; por tanto, los bloqueos de contenido fijo documentados continÃƒÆ’Ã‚Âºan.
- Este estado se clasifica como `VERIFICADO PERO MEJORABLE` y, para las pÃƒÆ’Ã‚Â¡ginas bloqueadas por plantilla, `INCOMPLETO`.

**Idiomas publicados verificados:**

- ES es el idioma principal.
- EN, FR, DE, NL, IT y PT-PT estÃƒÆ’Ã‚Â¡n publicados.
- El resto de idiomas configurados consultados no estÃƒÆ’Ã‚Â¡ publicado.

**Recursos prioritarios verificados:**

- El producto personalizado, la colecciÃƒÆ’Ã‚Â³n de mÃƒÆ’Ã‚Â¡s vendidos, la colecciÃƒÆ’Ã‚Â³n de espacios pÃƒÆ’Ã‚Âºblicos, la colecciÃƒÆ’Ã‚Â³n floral y el blog raÃƒÆ’Ã‚Â­z `InspiraciÃƒÆ’Ã‚Â³n` conservan los contenidos y metadatos documentados.
- Sus traducciones prioritarias consultadas figuran como `outdated: false`.

**DecisiÃƒÆ’Ã‚Â³n operativa:**

- No publicar el hotfix.
- No ampliar cambios editoriales ni de tema sin presentar un lote y recibir la aprobaciÃƒÆ’Ã‚Â³n literal exigida por `AGENTS.md`.

### Lote MW-QA-HOTFIX-001: QA integral del tema `SEO schema hotfix - 2026-06-15`

**AprobaciÃƒÆ’Ã‚Â³n recibida:** `APROBADO LOTE MW-QA-HOTFIX-001`.

**Estado final:** `VERIFICADO Y CORRECTO`.

**Alcance ejecutado:**

- ComparaciÃƒÆ’Ã‚Â³n MAIN vs hotfix.
- ValidaciÃƒÆ’Ã‚Â³n de schema en home, productos, artÃƒÆ’Ã‚Â­culos, carrito y formularios.
- RevisiÃƒÆ’Ã‚Â³n ES, EN, FR, DE y NL.
- QA escritorio y mÃƒÆ’Ã‚Â³vil.
- VerificaciÃƒÆ’Ã‚Â³n de App Embeds por `config/settings_data.json`.

**Seguridad:**

- No se publicÃƒÆ’Ã‚Â³ ningÃƒÆ’Ã‚Âºn tema.
- No se modificÃƒÆ’Ã‚Â³ Shopify.
- No se ejecutaron mutaciones GraphQL.
- No se cambiaron productos, traducciones, URLs, redirecciones, App Embeds ni archivos de tema.

**Evidencias clave:**

- MAIN real: `gid://shopify/OnlineStoreTheme/178379293048`, `Production - SEO fix AggregateRating (2026-06-12)`, rol `MAIN`.
- Hotfix: `gid://shopify/OnlineStoreTheme/178383749496`, `SEO schema hotfix - 2026-06-15`, rol `UNPUBLISHED`.
- El hotfix carga en vista previa desde `/cdn/shop/t/43/`; MAIN carga desde `/cdn/shop/t/41/`.
- `snippets/microdata-schema.liquid` cambia a checksum `58417e4825aa3d4570a6646f292aaedc`.
- `snippets/microdata-schema-original.liquid` permanece como copia auxiliar exacta del schema MAIN.
- `assets/country-flags.css`, `assets/sections.js` y `assets/theme.js` tienen checksums distintos, pero son semÃƒÆ’Ã‚Â¡nticamente idÃƒÆ’Ã‚Â©nticos tras normalizar ID de tema y versiÃƒÆ’Ã‚Â³n CDN.
- `config/settings_data.json` coincide exactamente entre MAIN y hotfix: checksum `a1192f2f698d277e0f69f7156a61a90c`.

**Schema y render:**

- Homes ES, EN, FR, DE y NL: JSON-LD parseable, `BreadcrumbList`, `WebSite`, `Organization`, `SearchAction`, 0 `AggregateRating` fijo en hotfix.
- Producto `Whispering Woods` ES, EN, FR, DE y NL: `Product`, `Brand`, `ImageObject`, `QuantitativeValue`, 4 `Offer`, SKU, precio, moneda, disponibilidad y URL conservados.
- Producto personalizado: mismo resultado, 4 `Offer` y 0 identificadores falsos.
- GTIN/MPN falsos en hotfix: 0 en todas las fichas probadas.
- ArtÃƒÆ’Ã‚Â­culo probado en ES, EN, FR, DE y NL: `BlogPosting` y `BreadcrumbList` parseables; tercer breadcrumb con tÃƒÆ’Ã‚Â­tulo real del artÃƒÆ’Ã‚Â­culo.
- Carrito, contacto y formulario de particulares renderizan sin errores JSON-LD.
- QA escritorio y mÃƒÆ’Ã‚Â³vil: sin regresiÃƒÆ’Ã‚Â³n funcional atribuible al hotfix.

**Incidencias no bloqueantes fuera del hotfix:**

- Carrito y formulario de particulares siguen sin H1.
- Algunos productos mantienen pequeÃƒÆ’Ã‚Â±o desbordamiento horizontal en mÃƒÆ’Ã‚Â³vil, ya observado en MAIN.
- ContinÃƒÆ’Ã‚Âºan pendientes las traducciones deficientes DE/NL y los bloqueos de plantillas documentados en lotes anteriores.

**Documento generado:**

- `qa-hotfix-schema-2026-06-16-MW-QA-HOTFIX-001.md`.

**DecisiÃƒÆ’Ã‚Â³n:**

- El hotfix queda tÃƒÆ’Ã‚Â©cnicamente recomendado para publicaciÃƒÆ’Ã‚Â³n manual.
- La publicaciÃƒÆ’Ã‚Â³n no estÃƒÆ’Ã‚Â¡ incluida en este lote y queda en `REQUIERE DECISION HUMANA`.
- No publicar `SEO-GEO staging - 2026-06-15`.
- Conservar temporalmente la copia auxiliar `snippets/microdata-schema-original.liquid`.

### Lote MW-PUBLISH-HOTFIX-001: intento de publicaciÃƒÆ’Ã‚Â³n del hotfix de schema

**AprobaciÃƒÆ’Ã‚Â³n recibida:** `APROBADO LOTE MW-PUBLISH-HOTFIX-001`.

**Estado final:** `NO ACCESIBLE` y `REQUIERE DECISION HUMANA`.

**Alcance autorizado:**

- Publicar exclusivamente el tema `SEO schema hotfix - 2026-06-15`.
- No publicar `SEO-GEO staging - 2026-06-15`.
- No modificar productos, colecciones, pÃƒÆ’Ã‚Â¡ginas, menÃƒÆ’Ã‚Âºs, traducciones, apps, mercados, configuraciÃƒÆ’Ã‚Â³n general, URLs, handles, precios, inventario, imÃƒÆ’Ã‚Â¡genes ni variantes.
- No eliminar `snippets/microdata-schema-original.liquid`.
- Ejecutar QA post-publicaciÃƒÆ’Ã‚Â³n inmediato en ES, EN, FR, DE y NL solo si la publicaciÃƒÆ’Ã‚Â³n se completa.

**Estado pre-publicaciÃƒÆ’Ã‚Â³n verificado:**

- MAIN antes del intento: `gid://shopify/OnlineStoreTheme/178379293048`, `Production - SEO fix AggregateRating (2026-06-12)`, rol `MAIN`, `processing: false`, `processingFailed: false`.
- Staging: `gid://shopify/OnlineStoreTheme/178383585656`, `SEO-GEO staging - 2026-06-15`, rol `UNPUBLISHED`, `processing: false`, `processingFailed: false`.
- Hotfix autorizado: `gid://shopify/OnlineStoreTheme/178383749496`, `SEO schema hotfix - 2026-06-15`, rol `UNPUBLISHED`, `processing: false`, `processingFailed: false`.
- Hotfix conserva `snippets/microdata-schema.liquid` con checksum `58417e4825aa3d4570a6646f292aaedc`.
- Hotfix conserva `snippets/microdata-schema-original.liquid` con checksum `ae9c62e4abb80d1051cbea73b03f1107`.
- `config/settings_data.json` coincide con MAIN: `a1192f2f698d277e0f69f7156a61a90c`.

**Intentos realizados:**

- Se validÃƒÆ’Ã‚Â³ correctamente la mutaciÃƒÆ’Ã‚Â³n GraphQL `themePublish(id: ...)` contra el esquema Admin.
- Al ejecutarla, la conexiÃƒÆ’Ã‚Â³n de Shopify bloqueÃƒÆ’Ã‚Â³ la operaciÃƒÆ’Ã‚Â³n con el mensaje: publicar un tema estÃƒÆ’Ã‚Â¡ bloqueado y debe hacerse manualmente desde Shopify Admin para evitar cambios accidentales del storefront.
- Se intentÃƒÆ’Ã‚Â³ abrir Shopify Admin en navegador integrado: `https://admin.shopify.com/store/matchwalls/themes`.
- Shopify redirigiÃƒÆ’Ã‚Â³ a login: `accounts.shopify.com/lookup`.

**Resultado:**

- No se publicÃƒÆ’Ã‚Â³ ningÃƒÆ’Ã‚Âºn tema.
- No se modificÃƒÆ’Ã‚Â³ Shopify.
- No se ejecutÃƒÆ’Ã‚Â³ QA post-publicaciÃƒÆ’Ã‚Â³n porque la publicaciÃƒÆ’Ã‚Â³n no se completÃƒÆ’Ã‚Â³.
- El tema hotfix permanece pendiente de publicaciÃƒÆ’Ã‚Â³n manual por Daniel desde Shopify Admin.

**Siguiente acciÃƒÆ’Ã‚Â³n humana requerida:**

- Daniel debe iniciar sesiÃƒÆ’Ã‚Â³n en Shopify Admin y publicar manualmente `SEO schema hotfix - 2026-06-15`, verificando que no selecciona `SEO-GEO staging - 2026-06-15`.
- Tras la publicaciÃƒÆ’Ã‚Â³n manual, se debe ejecutar inmediatamente el QA post-publicaciÃƒÆ’Ã‚Â³n definido en este lote.
### Actualizacion MW-PUBLISH-HOTFIX-001: QA post-publicacion manual

**Confirmacion recibida de Daniel:** `PUBLICADO HOTFIX`.

**Estado actualizado:** `CORREGIDO Y VERIFICADO`.

**Acciones ejecutadas por Codex tras la confirmacion:**

- Consultas Shopify exclusivamente de lectura.
- QA publico en escritorio y movil.
- No se ejecuto ninguna mutacion GraphQL.
- No se modificaron productos, colecciones, paginas, menus, traducciones, apps, mercados, configuracion general, URLs, handles, precios, inventario, imagenes, variantes ni archivos de tema.

**Estado de temas verificado:**

- `SEO schema hotfix - 2026-06-15`: `gid://shopify/OnlineStoreTheme/178383749496`, rol `MAIN`, `processing: false`, `processingFailed: false`.
- `Production - SEO fix AggregateRating (2026-06-12)`: `gid://shopify/OnlineStoreTheme/178379293048`, rol `UNPUBLISHED`, `processing: false`, `processingFailed: false`.
- `SEO-GEO staging - 2026-06-15`: `gid://shopify/OnlineStoreTheme/178383585656`, rol `UNPUBLISHED`, `processing: false`, `processingFailed: false`.

**Archivos criticos verificados en el tema MAIN:**

- `snippets/microdata-schema.liquid`: checksum `58417e4825aa3d4570a6646f292aaedc`, tamano 10.787.
- `snippets/microdata-schema-original.liquid`: checksum `ae9c62e4abb80d1051cbea73b03f1107`, tamano 10.068. Se conserva como copia auxiliar.
- `config/settings_data.json`: checksum `a1192f2f698d277e0f69f7156a61a90c`, tamano 10.256. App Embeds sin cambio detectado.

**QA publico ejecutado:**

- 35 URLs en escritorio y 35 URLs en movil.
- Tipos de pagina: home, producto principal, producto personalizado, articulo, carrito, contacto y formulario particulares.
- Idiomas: ES, EN, FR, DE y NL.
- Todas las URLs revisadas cargan assets publicos desde `/cdn/shop/t/43/`.
- Errores de parseo JSON-LD: 0.
- `AggregateRating` corporativo fijo detectado: 0.
- GTIN/MPN falsos detectados: 0.
- Productos probados con `Product` y 4 `Offer` completos: 10/10 en escritorio y 10/10 en movil.
- App Embeds detectados publicamente: Forms, GDPR/Pandectes, Inbox, Instafeed, Klaviyo, LangShop y Wishlist.

**Incidencias no bloqueantes y fuera del hotfix:**

- Carrito sin H1 en ES, EN, FR, DE y NL: `VERIFICADO PERO MEJORABLE`.
- Formulario de particulares sin H1 en ES, EN, FR, DE y NL: `VERIFICADO PERO MEJORABLE`.
- Pequeno desbordamiento horizontal movil en algunas plantillas, especialmente DE y productos: `VERIFICADO PERO MEJORABLE`.
- Bloqueos editoriales y de plantilla ya documentados en FAQ, Profesionales, Social/Prensa/Afiliacion, Muestras, Guia y footer: `INCOMPLETO`.

**Documento generado:**

- `qa-post-publicacion-hotfix-2026-06-16-MW-PUBLISH-HOTFIX-001.md`.

**Decision:**

- El hotfix publicado queda en `CORREGIDO Y VERIFICADO`.
- `SEO-GEO staging - 2026-06-15` permanece sin publicar y no debe publicarse dentro de este lote.


### Lote MW-AUDIT-CONTENIDO-I18N-GEO-001: auditoria de contenidos visibles, i18n y GEO

**Aprobacion recibida:** `APROBADO LOTE MW-AUDIT-CONTENIDO-I18N-GEO-001`.

**Fecha:** 16 de junio de 2026.

**Modo:** solo lectura.

**Acciones ejecutadas:**

- Lectura de `AGENTS.md` y registros prioritarios del proyecto.
- Consultas Shopify Admin GraphQL exclusivamente de lectura.
- Verificacion del tema MAIN: `SEO schema hotfix - 2026-06-15`, `gid://shopify/OnlineStoreTheme/178383749496`.
- Lectura de locales, menus, paginas publicadas, articulos publicados, primera pagina de productos activos y colecciones.
- Lectura de archivos criticos de tema: header, footer, FAQ, Profesionales, Muestras, Guia y Social/Prensa/Afiliacion.
- Render publico de 45 URLs prioritarias en ES, EN, FR, DE y NL mediante navegador, sin enviar formularios ni modificar datos.
- Analisis del inventario local `inventario-urls.csv` y `sitemap-urls.txt`.

**Cambios en Shopify:** ninguno. No se ejecutaron mutaciones, publicaciones, ediciones de tema, productos, colecciones, paginas, traducciones, menus, apps, mercados, URLs, handles, precios, imagenes, variantes ni inventario.

**Entregables generados:**

- `auditoria-contenido-i18n-geo-2026-06-16.md`.
- `inventario-problemas-contenido-i18n-geo-2026-06-16.csv`.
- `textos-fijos-plantilla-bloqueantes-2026-06-16.csv`.
- `h1-metadatos-i18n-geo-2026-06-16.csv`.
- `siguientes-lotes-contenido-i18n-geo-2026-06-16.md`.

**Estado final:** `INCOMPLETO` para la optimizacion global; `VERIFICADO PERO MEJORABLE` / `INCORRECTO` / `RIESGO CRITICO` en incidencias documentadas.

**Proximo lote recomendado:** `MW-FOOTER-I18N-001` o `MW-HEADER-CLAIMS-I18N-001`, ambos requieren aprobacion explicita antes de cualquier cambio.


### Auditoria dependencia LangShop: decision previa a eliminar o reducir plan

**Fecha:** 16 de junio de 2026, 11:37:39 +02:00.

**Modo:** solo lectura.

**Acciones ejecutadas:**

- Lectura de `AGENTS.md` y documentos recientes del proyecto.
- Consulta Shopify Admin GraphQL exclusivamente de lectura.
- Verificacion de tienda, tema MAIN, locales publicados, presencias web, conteo de productos y colecciones.
- Lectura de archivos clave del tema MAIN: `config/settings_data.json`, `layout/theme.liquid` y `snippets/localization-selector.liquid`.
- Consulta de muestra de traducciones nativas Shopify para `PAGE`, `PRODUCT` y `COLLECTION`.
- Consulta externa de documentacion publica de Shopify, Shopify App Store y LangShop pricing.

**Cambios en Shopify:** ninguno. No se ejecutaron mutaciones, publicaciones, ediciones de tema, productos, colecciones, paginas, traducciones, menus, apps, mercados, URLs, handles, precios, imagenes, variantes ni inventario.

**Evidencias principales:**

- Tema MAIN: `SEO schema hotfix - 2026-06-15`, `gid://shopify/OnlineStoreTheme/178383749496`.
- Productos: 3.022.
- Colecciones: 109.
- Idiomas publicados: ES primario; EN, FR, DE, NL, IT y PT-PT publicados.
- `config/settings_data.json` conserva App Embed activo `shopify://apps/langshop/blocks/sdk/...`, `disabled:false`.
- `snippets/localization-selector.liquid` usa selector nativo Shopify mediante formulario `localization`.
- `appInstallations` no es accesible con el conector actual (`access denied`).
- `appByHandle(handle:"langshop")` devuelve ficha publica de LangShop, pero `installation:null`; por tanto la instalacion/suscripcion real queda `NO ACCESIBLE` desde esta herramienta.
- Existen traducciones nativas en Shopify para paginas, productos y colecciones, pero tambien deuda editorial grave: productos de prueba, `Lorem ipsum`, `Nan`, traducciones automaticas deficientes y handles incorrectos.

**Documento generado:**

- `auditoria-langshop-dependency-2026-06-16.md`.

**Decision recomendada:**

- No eliminar LangShop ahora.
- No reducir plan ahora sin auditar el panel real de LangShop y exportar traducciones.
- Siguiente lote recomendado: `MW-LANGSHOP-DEPENDENCY-AUDIT-001`, solo lectura.

**Estado final:** `REQUIERE DECISION HUMANA`.


### Lote MW-FOOTER-I18N-001: correcciÃƒÆ’Ã‚Â³n footer global en tema QA

**AprobaciÃƒÆ’Ã‚Â³n recibida:** `APROBADO LOTE MW-FOOTER-I18N-001`.

**Fecha:** 17 de junio de 2026.

**Modo:** ejecuciÃƒÆ’Ã‚Â³n acotada en tema no publicado.

**Acciones ejecutadas:**

- Consulta de respaldo del tema MAIN real `SEO schema hotfix - 2026-06-15`, ID `gid://shopify/OnlineStoreTheme/178383749496`.
- Consulta de menÃƒÆ’Ã‚Âºs globales usados por footer: `footer`, `footer-profesional`, `footer-brand`, `footer-legal`.
- Consulta de recurso traducible del tema para comprobar existencia de claves de footer.
- CreaciÃƒÆ’Ã‚Â³n de respaldo local `respaldo-MW-FOOTER-I18N-001-2026-06-17.md`.
- Duplicado del tema MAIN mediante `themeDuplicate`.
- CreaciÃƒÆ’Ã‚Â³n de tema QA no publicado `MW-FOOTER-I18N-001 - QA - 2026-06-17`, ID `gid://shopify/OnlineStoreTheme/178390401400`.
- EdiciÃƒÆ’Ã‚Â³n mediante `themeFilesUpsert` solo del archivo `sections/footer-group.json` en el tema QA.
- Lectura posterior del archivo QA para confirmar valores almacenados.
- ComprobaciÃƒÆ’Ã‚Â³n de que el tema MAIN conserva el checksum original del footer.

**Cambios ejecutados en Shopify:**

- Tema QA no publicado creado.
- Archivo `sections/footer-group.json` actualizado ÃƒÆ’Ã‚Âºnicamente en el tema QA.

**No ejecutado:**

- No se modificÃƒÆ’Ã‚Â³ el tema MAIN.
- No se publicÃƒÆ’Ã‚Â³ ningÃƒÆ’Ã‚Âºn tema.
- No se modificaron menÃƒÆ’Ã‚Âºs globales.
- No se registraron traducciones EN, FR, DE o NL.
- No se tocaron productos, colecciones, pÃƒÆ’Ã‚Â¡ginas, URLs, handles, redirecciones, precios, inventario, variantes, imÃƒÆ’Ã‚Â¡genes, App Embeds ni Liquid de producciÃƒÆ’Ã‚Â³n.

**Valores principales modificados en QA:**

- `EnvÃƒÆ’Ã‚Â­o gratuito` / `Worldwide.` -> `EnvÃƒÆ’Ã‚Â­o internacional` / `Consulta los plazos y condiciones de envÃƒÆ’Ã‚Â­o disponibles para tu paÃƒÆ’Ã‚Â­s.`
- `Pago seguro` / `Metodos de pago seguros y financiaciÃƒÆ’Ã‚Â³n.` -> `Pagos seguros` / `Consulta los mÃƒÆ’Ã‚Â©todos de pago disponibles en la pantalla de pago.`
- `GarantÃƒÆ’Ã‚Â­a de satisfacciÃƒÆ’Ã‚Â³n` / `Nuestro compromiso tu tranquilidad.` -> `AtenciÃƒÆ’Ã‚Â³n y soporte` / `Te ayudamos antes y despuÃƒÆ’Ã‚Â©s de tu pedido.`
- `PersonalizaciÃƒÆ’Ã‚Â³n` / `Te ayudamos a crear tu diseÃƒÆ’Ã‚Â±o Matchwalls.` -> `PersonalizaciÃƒÆ’Ã‚Â³n` / `Te orientamos para adaptar tu diseÃƒÆ’Ã‚Â±o a medida.`
- `FÃƒÆ’Ã‚Â¡cil instalaciÃƒÆ’Ã‚Â³n` / `Descargate nuestras guÃƒÆ’Ã‚Â­as de fÃƒÆ’Ã‚Â¡cil instlaciÃƒÆ’Ã‚Â³on.` -> `GuÃƒÆ’Ã‚Â­as de instalaciÃƒÆ’Ã‚Â³n` / `Consulta nuestras guÃƒÆ’Ã‚Â­as antes de instalar tu papel pintado o mural.`
- Newsletter superior corregida de `Se el primero... tips...` a una redacciÃƒÆ’Ã‚Â³n mÃƒÆ’Ã‚Â¡s limpia y conservadora.

**Evidencias:**

- MAIN `sections/footer-group.json`: checksum original `e93af9228c8a97dce4ad91e203bf7e75`, sin cambio.
- QA `sections/footer-group.json`: checksum nuevo `17271d0b6b69bdcb1e430bec9e061943`, actualizado `2026-06-17T08:19:11Z`.
- `themeFilesUpsert`: `userErrors: []`.
- `themeDuplicate`: `userErrors: []`.

**QA pÃƒÆ’Ã‚Âºblica:**

- Intentos de preview:
  - `https://www.matchwalls.com/?preview_theme_id=178390401400`
  - `https://matchwalls.myshopify.com/?preview_theme_id=178390401400`
- Resultado: la navegaciÃƒÆ’Ã‚Â³n termina en `https://www.matchwalls.com/` y muestra el tema vivo, no el tema QA.
- Por tanto, QA pÃƒÆ’Ã‚Âºblica de preview: `NO ACCESIBLE` desde este entorno.

**Incidencias y lÃƒÆ’Ã‚Â­mites:**

- Los menÃƒÆ’Ã‚Âºs globales siguen vivos con errores verificados: `FAQÃƒâ€šÃ‚Â´S`, `Black Friday 2024`, `espacios pÃƒÆ’Ã‚Âºbicos`.
- Los menÃƒÆ’Ã‚Âºs no se editaron porque impactan directamente el sitio publicado y no son theme-scoped.
- Las traducciones de tema EN/FR/DE/NL no se editaron porque falta inventario exacto filtrado de claves y `digest`.
- `0 userErrors` solo confirma aceptaciÃƒÆ’Ã‚Â³n tÃƒÆ’Ã‚Â©cnica por Shopify, no publicaciÃƒÆ’Ã‚Â³n ni QA visual pÃƒÆ’Ã‚Âºblica.

**Documentos generados:**

- `propuesta-lote-MW-FOOTER-I18N-001-2026-06-17.md`.
- `respaldo-MW-FOOTER-I18N-001-2026-06-17.md`.
- `ejecucion-lote-MW-FOOTER-I18N-001-2026-06-17.md`.

**Estado final:**

- Archivo footer en tema QA: `CORREGIDO Y VERIFICADO` por lectura Shopify Admin.
- Sitio publicado: `INCOMPLETO`.
- MenÃƒÆ’Ã‚Âºs globales: `INCORRECTO`.
- Traducciones EN/FR/DE/NL del footer: `INCOMPLETO`.
- PublicaciÃƒÆ’Ã‚Â³n: `NO EJECUTADA`.


### Lote MW-FOOTER-NAV-GLOBAL-002: reparaciÃƒÆ’Ã‚Â³n navegaciÃƒÆ’Ã‚Â³n footer publicada

**AprobaciÃƒÆ’Ã‚Â³n recibida:** `APROBADO LOTE MW-FOOTER-NAV-GLOBAL-002`.

**Fecha:** 17 de junio de 2026.

**Modo:** ediciÃƒÆ’Ã‚Â³n acotada de menÃƒÆ’Ã‚Âºs globales publicados.

**Acciones ejecutadas:**

- Lectura previa de menÃƒÆ’Ã‚Âºs `footer`, `footer-profesional`, `footer-brand` y `footer-legal`.
- CreaciÃƒÆ’Ã‚Â³n de respaldo local `respaldo-MW-FOOTER-NAV-GLOBAL-002-2026-06-17.md`.
- ValidaciÃƒÆ’Ã‚Â³n GraphQL de la mutaciÃƒÆ’Ã‚Â³n `menuUpdate`.
- EjecuciÃƒÆ’Ã‚Â³n de `menuUpdate` en cuatro menÃƒÆ’Ã‚Âºs globales.
- Lectura posterior vÃƒÆ’Ã‚Â­a Shopify Admin.
- QA pÃƒÆ’Ã‚Âºblica del footer en ES, EN, FR, DE y NL.

**Cambios ejecutados en Shopify:**

- `footer`: retirados `EnvÃƒÆ’Ã‚Â­os internacionales` y `Black Friday 2024`; etiquetas fuente corregidas.
- `footer-profesional`: corregida errata `espacios pÃƒÆ’Ã‚Âºbicos` -> `espacios pÃƒÆ’Ã‚Âºblicos`; etiquetas B2B normalizadas.
- `footer-brand`: retirado `Tarjeta regalo`; etiquetas `Sobre nosotros` y `Nuestros productos` normalizadas.
- `footer-legal`: capitalizaciÃƒÆ’Ã‚Â³n editorial corregida.

**No ejecutado:**

- No se modificaron temas.
- No se publicÃƒÆ’Ã‚Â³ ningÃƒÆ’Ã‚Âºn tema.
- No se eliminaron pÃƒÆ’Ã‚Â¡ginas, productos ni colecciones.
- No se cambiaron URLs, handles ni redirecciones.
- No se modificaron precios, inventario, variantes, imÃƒÆ’Ã‚Â¡genes ni App Embeds.
- No se escribieron traducciones EN/FR/DE/NL.

**Evidencia Shopify Admin:**

- Todas las mutaciones devolvieron `userErrors: []`.
- Lectura posterior confirma que:
  - `footer` ya no contiene `EnvÃƒÆ’Ã‚Â­os internacionales` ni `Black Friday 2024`.
  - `footer-brand` ya no contiene `Tarjeta regalo`.
  - `footer-profesional` usa `espacios pÃƒÆ’Ã‚Âºblicos`.
  - `footer` usa `FAQ - EnvÃƒÆ’Ã‚Â­os y devoluciones`.

**QA pÃƒÆ’Ã‚Âºblica:**

- ES: corregido y verificado para enlaces retirados y etiquetas fuente.
- EN: enlaces retirados no aparecen, pero persiste traducciÃƒÆ’Ã‚Â³n antigua `FAQÃƒâ€šÃ‚Â´S - Shipping and Returns` y otras traducciones mejorables.
- FR: enlaces retirados no aparecen; persisten cabeceras fuente espaÃƒÆ’Ã‚Â±olas y traducciones mejorables.
- DE: enlaces retirados no aparecen; persisten traducciones mejorables.
- NL: enlaces retirados no aparecen; persisten cabeceras fuente espaÃƒÆ’Ã‚Â±olas, `FAQÃƒâ€šÃ‚Â´s` y traducciÃƒÆ’Ã‚Â³n incorrecta `schaamruimtes`.

**Estado final:**

- `Tarjeta regalo`: `CORREGIDO Y VERIFICADO`.
- `Black Friday 2024`: `CORREGIDO Y VERIFICADO`.
- `EnvÃƒÆ’Ã‚Â­os internacionales`: `CORREGIDO Y VERIFICADO`.
- MenÃƒÆ’Ã‚Âºs fuente ES: `CORREGIDO Y VERIFICADO`.
- Traducciones de navegaciÃƒÆ’Ã‚Â³n EN/FR/DE/NL: `INCOMPLETO`.

**Documento generado:**

- `ejecucion-lote-MW-FOOTER-NAV-GLOBAL-002-2026-06-17.md`.

**Siguiente lote recomendado:**

- `MW-FOOTER-I18N-TRANSLATIONS-003`, para inventariar claves/digest y corregir traducciones visibles del footer EN, FR, DE y NL.


### Lote MW-FOOTER-I18N-TRANSLATIONS-003: traducciones navegaciÃƒÆ’Ã‚Â³n footer EN/FR/DE/NL

**AprobaciÃƒÆ’Ã‚Â³n recibida:** `APROBADO LOTE MW-FOOTER-I18N-TRANSLATIONS-003`.

**Fecha:** 17 de junio de 2026.

**Modo:** escritura acotada de traducciones nativas Shopify mediante `translationsRegister`.

**Acciones ejecutadas:**

- Consulta previa de recursos traducibles de los cuatro menÃƒÆ’Ã‚Âºs de footer.
- IdentificaciÃƒÆ’Ã‚Â³n de tÃƒÆ’Ã‚Â­tulos de menÃƒÆ’Ã‚Âº como recursos `MENU`.
- IdentificaciÃƒÆ’Ã‚Â³n de enlaces de menÃƒÆ’Ã‚Âº como recursos `LINK`.
- ConfirmaciÃƒÆ’Ã‚Â³n de que los IDs `MenuItem` no son vÃƒÆ’Ã‚Â¡lidos para `translatableResourcesByIds`.
- CreaciÃƒÆ’Ã‚Â³n de respaldo local `respaldo-MW-FOOTER-I18N-TRANSLATIONS-003-2026-06-17.md`.
- ValidaciÃƒÆ’Ã‚Â³n GraphQL de la mutaciÃƒÆ’Ã‚Â³n `translationsRegister`.
- Registro de 96 traducciones EN/FR/DE/NL en 24 recursos.
- Lectura posterior por Shopify Admin.
- VerificaciÃƒÆ’Ã‚Â³n de configuraciÃƒÆ’Ã‚Â³n de publicaciÃƒÆ’Ã‚Â³n de idiomas, Markets/web presence, tema MAIN y App Embed LangShop.

**Recursos afectados:**

- MenÃƒÆ’Ã‚Âºs:
  - `gid://shopify/Menu/210266325219`
  - `gid://shopify/Menu/210972311779`
  - `gid://shopify/Menu/210972344547`
  - `gid://shopify/Menu/210972410083`
- Enlaces:
  - `gid://shopify/Link/495449178339`
  - `gid://shopify/Link/495449211107`
  - `gid://shopify/Link/495449243875`
  - `gid://shopify/Link/497161568483`
  - `gid://shopify/Link/497161601251`
  - `gid://shopify/Link/713118876024`
  - `gid://shopify/Link/493556531427`
  - `gid://shopify/Link/493556564195`
  - `gid://shopify/Link/503255138531`
  - `gid://shopify/Link/493556596963`
  - `gid://shopify/Link/493556629731`
  - `gid://shopify/Link/495008121059`
  - `gid://shopify/Link/494947959011`
  - `gid://shopify/Link/494947926243`
  - `gid://shopify/Link/494947991779`
  - `gid://shopify/Link/494950613219`
  - `gid://shopify/Link/493557088483`
  - `gid://shopify/Link/493557022947`
  - `gid://shopify/Link/493557055715`
  - `gid://shopify/Link/496053289187`

**Resultado Shopify Admin:**

- Todas las llamadas `translationsRegister` devolvieron `userErrors: []`.
- Lectura posterior confirmÃƒÆ’Ã‚Â³ traducciones EN/FR/DE/NL con `outdated:false`.
- `Menu.translations` confirmÃƒÆ’Ã‚Â³ tÃƒÆ’Ã‚Â­tulos de menÃƒÆ’Ã‚Âº publicados con valores corregidos.

**ConfiguraciÃƒÆ’Ã‚Â³n de publicaciÃƒÆ’Ã‚Â³n verificada:**

- Dominio primario: `https://www.matchwalls.com`, SSL activo.
- Tema MAIN: `SEO schema hotfix - 2026-06-15`, `gid://shopify/OnlineStoreTheme/178383749496`, `processing:false`, `processingFailed:false`.
- Idiomas prioritarios:
  - ES `published:true`, primario.
  - EN `published:true`, URL `https://www.matchwalls.com/en/`.
  - FR `published:true`, URL `https://www.matchwalls.com/fr/`.
  - DE `published:true`, URL `https://www.matchwalls.com/de/`.
  - NL `published:true`, URL `https://www.matchwalls.com/nl/`.
- LangShop SDK activo como App Embed en MAIN: `shopify://apps/langshop/blocks/sdk/...`, `disabled:false`.

**LangShop:**

- App Embed LangShop: `VERIFICADO PERO MEJORABLE`.
- ConfiguraciÃƒÆ’Ã‚Â³n interna LangShop: `NO ACCESIBLE`.
- `appInstallations` devuelve `access denied`; no se pudo verificar plan, reglas, glosario, auto-sync ni cola de publicaciÃƒÆ’Ã‚Â³n.

**QA pÃƒÆ’Ã‚Âºblica:**

- Navegador interno: `https://www.matchwalls.com/en/` devolviÃƒÆ’Ã‚Â³ pÃƒÆ’Ã‚Â¡gina Shopify de error `Algo saliÃƒÆ’Ã‚Â³ mal`.
- `Invoke-WebRequest`: error de recepciÃƒÆ’Ã‚Â³n.
- `curl.exe -I`: no pudo conectar a `www.matchwalls.com:443` vÃƒÆ’Ã‚Â­a `127.0.0.1`.
- Render pÃƒÆ’Ã‚Âºblico desde este entorno: `NO ACCESIBLE`.

**No ejecutado:**

- No se modificaron temas.
- No se publicaron temas.
- No se modificaron menÃƒÆ’Ã‚Âºs fuente ES.
- No se cambiaron productos, colecciones, pÃƒÆ’Ã‚Â¡ginas, handles, URLs, redirecciones, precios, inventario, variantes, imÃƒÆ’Ã‚Â¡genes ni App Embeds.
- No se modificÃƒÆ’Ã‚Â³ configuraciÃƒÆ’Ã‚Â³n LangShop.
- No se ejecutaron traducciones automÃƒÆ’Ã‚Â¡ticas.

**Estado final por capa:**

- Traducciones almacenadas en Shopify Admin: `CORREGIDO Y VERIFICADO`.
- ConfiguraciÃƒÆ’Ã‚Â³n Shopify para publicaciÃƒÆ’Ã‚Â³n EN/FR/DE/NL: `VERIFICADO Y CORRECTO`.
- LangShop App Embed activo: `VERIFICADO PERO MEJORABLE`.
- ConfiguraciÃƒÆ’Ã‚Â³n interna LangShop: `NO ACCESIBLE`.
- Render pÃƒÆ’Ã‚Âºblico storefront: `NO ACCESIBLE`.

**Documento generado:**

- `ejecucion-lote-MW-FOOTER-I18N-TRANSLATIONS-003-2026-06-17.md`.

---
# 2026-06-25 - Diagnostico MW-TECH-HOME-CRAWLABLE-CSS-010D

## Alcance

`INCOMPLETO`

- Diagnostico de solo lectura.
- No existe aprobacion de escritura para este lote.
- MAIN `178396463480` no fue modificado ni publicado.
- Tema auxiliar `178399019384` no fue modificado.
- Tema de reversion `178383749496` no fue modificado.

## Estado real verificado

`INCORRECTO`

- Archivo afectado: `sections/collection-logo-list.liquid`.
- MD5 en MAIN: `44d02156951a46f0147f3ee3de61f38e`.
- MD5 en QA auxiliar: `44d02156951a46f0147f3ee3de61f38e`.
- MD5 en tema de reversion: `44d02156951a46f0147f3ee3de61f38e`.
- La deuda es compartida por los tres temas revisados y no es una regresion de 010C2.

## Evidencia

- La home activa usa la seccion `collection_logo_list_qwGRVf` de tipo `collection-logo-list`.
- El archivo imprime un `<style>` dentro de cada enlace `.logo-link`.
- La home renderiza 8 enlaces de categoria, por lo que se imprimen 8 bloques CSS duplicados.
- En navegador, el CSS no aparece en `body.innerText`, pero si aparece en `body.textContent` y HTML bruto.

## Estado final

`REQUIERE DECISION HUMANA`

- Propuesta formal creada: `propuesta-lote-MW-TECH-HOME-CRAWLABLE-CSS-010D-2026-06-25.md`.
- Diagnostico creado: `diagnostico-MW-TECH-HOME-CRAWLABLE-CSS-010D-2026-06-25.md`.
- Para ejecutar se requiere aprobacion exacta: `APROBADO LOTE MW-TECH-HOME-CRAWLABLE-CSS-010D`.

---

## 2026-06-17 - Lote MW-LANGSHOP-WEB-RECONCILIATION-005

**Aprobacion Daniel:** `APROBADO LOTE MW-LANGSHOP-WEB-RECONCILIATION-005`.

**Tipo:** auditoria y reconciliacion de solo lectura.

**Objetivo:** contrastar el estado real del footer publico, menus Shopify activos, exportaciones LangShop y residuos legacy antes de cualquier limpieza o importacion.

**Documentos y fuentes leidas:**

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `programa-ejecucion-seo-geo.md`.
- `lista-maestra-errores-cambios-evoluciones-mejoras.md`.
- `auditoria-langshop-dependency-2026-06-16.md`.
- `propuesta-lote-MW-LANGSHOP-NAV-CLEANUP-004-2026-06-17.md`.
- `langshop-export-navigation-raw-2026-06-17/README-NO-REIMPORTAR.md`.
- `navigation_export_es_en.csv`.
- `navigation_export_es_fr.csv`.
- `navigation_export_es_de.csv`.
- `navigation_export_es_nl.csv`.

**Operaciones ejecutadas:**

- Lecturas Shopify Admin GraphQL validadas contra esquema.
- Lectura de tienda, dominio, tema MAIN, locales publicados y App Embed LangShop.
- Lectura de menus activos de footer.
- Lectura compacta de todos los menus Shopify para localizar residuos legacy.
- Lectura de recursos traducibles historicos `gid://shopify/MenuItem/493550371043` y `gid://shopify/MenuItem/493550239971`.
- QA publico del footer en ES, EN, FR, DE y NL.
- Recuento y busqueda local en exportaciones CSV LangShop.

**Estado real verificado:**

- Dominio principal: `https://www.matchwalls.com`, SSL activo.
- Tema MAIN: `SEO schema hotfix - 2026-06-15`, `gid://shopify/OnlineStoreTheme/178383749496`.
- Idiomas ES/EN/FR/DE/NL: publicados.
- LangShop SDK App Embed: activo en MAIN.
- Configuracion interna LangShop: `NO ACCESIBLE`.
- Menus activos del footer:
  - `footer` / `AYUDA Y SOPORTE`.
  - `footer-profesional` / `PROFESIONALES`.
  - `footer-brand` / `EMPRESA`.
  - `footer-legal` / `LEGAL`.
- Footer publico ES/EN/FR/DE/NL: sin `Tarjeta regalo`, sin `Black Friday`, sin `Envios internacionales` o equivalentes como enlace de footer.

**Hallazgo clave:**

- Existe un menu legacy actual en Shopify:
  - `gid://shopify/Menu/210969952483`.
  - Handle `footer-matchwalls`.
  - Titulo `Footer matchwalls`.
- Ese menu conserva elementos antiguos:
  - `gid://shopify/MenuItem/493550371043` - `Tarjeta regalo`.
  - `gid://shopify/MenuItem/493550239971` - `B2B Interiorismo`.
- Esos recursos tambien aparecen en las exportaciones LangShop. Esto explica que LangShop los muestre o exporte aunque no esten visibles en el footer publico actual.

**Resultados por estado:**

- Footer publico ES/EN/FR/DE/NL: `CORREGIDO Y VERIFICADO`.
- Menus activos del footer Shopify: `CORREGIDO Y VERIFICADO`.
- Menu legacy `footer-matchwalls`: `VERIFICADO PERO MEJORABLE`.
- Residuo `Tarjeta regalo` dentro de menu legacy: `INCORRECTO` como inventario operativo, no visible en footer publico.
- Exportaciones LangShop raw: `VERIFICADO PERO MEJORABLE`.
- Importacion directa de CSV raw: `RIESGO CRITICO`.
- Configuracion interna LangShop: `NO ACCESIBLE`.

**No ejecutado:**

- No se modifico Shopify.
- No se modifico LangShop.
- No se importaron CSV.
- No se borraron traducciones.
- No se ejecutaron mutaciones.
- No se modificaron menus, tema, handles, URLs, redirecciones, productos, colecciones ni inventario.

**Documentos generados:**

- `ejecucion-lote-MW-LANGSHOP-WEB-RECONCILIATION-005-2026-06-17.md`.
- `matriz-reconciliacion-langshop-web-005-2026-06-17.csv`.

**Siguiente paso recomendado:**

Preparar lote especifico `MW-LANGSHOP-LEGACY-MENU-CLEANUP-006` para verificar referencias del tema a `footer-matchwalls`, respaldar el menu legacy y, si no esta en uso, limpiar o retirar elementos obsoletos de forma reversible. No ejecutar sin nueva aprobacion exacta.

---

# Ejecucion lote MW-LANGSHOP-LEGACY-MENU-CLEANUP-006

**Fecha y hora:** 2026-06-17 15:22 +02:00.  
**Aprobacion exacta recibida:** `APROBADO LOTE MW-LANGSHOP-LEGACY-MENU-CLEANUP-006`.  
**Estado del alcance aprobado:** `CORREGIDO Y VERIFICADO`.  
**Estado global tras QA publico:** `INCOMPLETO`, porque el HTML publico externo sigue mostrando residuos antiguos que requieren un lote nuevo.

## Recursos e IDs

- Menu legacy afectado: `gid://shopify/Menu/210969952483`.
- Handle: `footer-matchwalls`.
- Titulo anterior: `Footer matchwalls`.
- Titulo nuevo: `ZZ LEGACY - NO USAR - footer-matchwalls`.
- Items anteriores: arbol completo respaldado en `respaldo-MW-LANGSHOP-LEGACY-MENU-CLEANUP-006-2026-06-17.md`.
- Items nuevos: `[]`.

## Operaciones ejecutadas

- Se ejecuto una unica mutacion Shopify Admin GraphQL `menuUpdate`.
- Variables ejecutadas:

```json
{
  "id": "gid://shopify/Menu/210969952483",
  "title": "ZZ LEGACY - NO USAR - footer-matchwalls",
  "items": []
}
```

- Resultado Shopify: `userErrors: []`.

## Pruebas realizadas

- Lectura posterior del menu `footer-matchwalls`: titulo actualizado e items vacios.
- Lectura posterior de menus activos `footer`, `footer-profesional`, `footer-brand`, `footer-legal`: sin cambios.
- Lectura posterior del tema MAIN `SEO schema hotfix - 2026-06-15`: `sections/footer-group.json` sigue usando los cuatro menus activos y no usa `footer-matchwalls`.
- Verificacion renderizada desde Codex: `NO ACCESIBLE`, porque Shopify devolvio pantalla `Algo salio mal`.
- Verificacion HTML publica externa: `INCORRECTO`; siguen apareciendo residuos antiguos en HTML servido publicamente.

## Incidencias

- El HTML publico externo de `https://www.matchwalls.com/en` sigue mostrando residuos antiguos como `Gift Card`, `International shipments` y `Black Friday 2024`.
- El HTML publico externo de `https://www.matchwalls.com/` sigue mostrando residuos equivalentes como `Envios internacionales` / `EnvÃƒÆ’Ã‚Â­os internacionales` y `Black Friday 2024`.
- Tras la limpieza del menu legacy, esos residuos ya no quedan explicados por `footer-matchwalls`.
- Posibles origenes a investigar, sin afirmar todavia: cache/CDN, traducciones publicadas residuales, otra capa del tema, app, HTML servido a fetch externo o configuracion interna LangShop.

## Documentos generados

- `ejecucion-lote-MW-LANGSHOP-LEGACY-MENU-CLEANUP-006-2026-06-17.md`.
- `matriz-lote-MW-LANGSHOP-LEGACY-MENU-CLEANUP-006-2026-06-17.csv`.

## Metodo de reversion

Revertir con `menuUpdate` sobre `gid://shopify/Menu/210969952483`, restaurando titulo `Footer matchwalls` y el arbol original documentado en `respaldo-MW-LANGSHOP-LEGACY-MENU-CLEANUP-006-2026-06-17.md`.

Limitacion: la estructura y enlaces son reversibles; los IDs exactos de MenuItem podrian cambiar si Shopify recrea items.

## Siguiente paso recomendado

Preparar lote `MW-LANGSHOP-PUBLIC-FOOTER-RESIDUE-007` de investigacion y reconciliacion, sin escrituras iniciales, para localizar el origen real de los residuos del footer en HTML publico y decidir una correccion segura.

---

# Diagnostico lote MW-LANGSHOP-PUBLIC-FOOTER-RESIDUE-007

**Fecha y hora:** 2026-06-17 20:57 +02:00.  
**Estado:** `INCOMPLETO`.  
**Tipo:** solo lectura; no aprobado ni ejecutado ningun cambio de escritura.

## Recursos comprobados

- Todos los menus Shopify accesibles por Admin GraphQL.
- Tema MAIN `gid://shopify/OnlineStoreTheme/178383749496` / `SEO schema hotfix - 2026-06-15`.
- Archivos MAIN:
  - `config/settings_data.json`.
  - `sections/header-group.json`.
  - `sections/footer-group.json`.
  - `sections/footer.liquid`.
- Recursos traducibles `MENU` para `en`, `fr`, `de` y `nl`.
- HTML publico externo:
  - `https://www.matchwalls.com/en`.
  - `https://www.matchwalls.com/`.

## Resultado

- Menus activos del footer: `VERIFICADO Y CORRECTO`.
- Menu legacy `footer-matchwalls`: `CORREGIDO Y VERIFICADO`, vacio y no referenciado por `footer-group.json`.
- `sections/footer-group.json`: `VERIFICADO Y CORRECTO`, usa los cuatro menus activos.
- `sections/footer.liquid`: `VERIFICADO Y CORRECTO`, no contiene hardcodeados los enlaces criticos antiguos.
- Traducciones `MENU` activas: `VERIFICADO Y CORRECTO` en EN, FR, DE y NL.
- HTML publico externo EN/ES: `INCORRECTO`; siguen apareciendo residuos antiguos de footer:
  - EN: `Gift Card`, `International shipments`, `Black Friday 2024`.
  - ES: `Tarjeta regalo`, `Envios internacionales`, `Black Friday 2024`.

## Incidencias

- La fuente normal esperada del footer en Admin esta limpia, pero el HTML publico externo sigue contaminado.
- `sections/header-group.json` conserva referencias deshabilitadas a `Gift Card`; esto queda como deuda separada y no explica por si solo el footer publico.
- Una peticion local sin cache desde PowerShell/curl no fue concluyente por error de conexion/proxy/TLS local.

## Acciones no realizadas

- No se modifico Shopify.
- No se modifico LangShop.
- No se importaron CSV.
- No se borraron traducciones.
- No se ejecutaron mutaciones.
- No se modificaron menus, tema, handles, URLs, redirecciones, productos, colecciones ni inventario.

## Documentos generados

- `diagnostico-lote-MW-LANGSHOP-PUBLIC-FOOTER-RESIDUE-007-2026-06-17.md`.
- `matriz-lote-MW-LANGSHOP-PUBLIC-FOOTER-RESIDUE-007-2026-06-17.csv`.

## Siguiente paso recomendado

Continuar el 007 sin escrituras para separar HTML bruto, DOM renderizado y capas de traduccion/tema adicionales. No ejecutar correccion hasta aislar fuente exacta y presentar lote con valores actuales, valores propuestos, respaldo y reversion.

---

# Addendum cierre lote MW-LANGSHOP-PUBLIC-FOOTER-RESIDUE-007

**Fecha y hora:** 2026-06-17 21:44 +02:00.  
**Tipo:** verificacion de solo lectura; no se ejecuto ninguna escritura.  
**Estado actualizado:** `CORREGIDO Y VERIFICADO`.

## Motivo del addendum

El diagnostico inicial del lote 007 marcaba HTML publico ES/EN como `INCORRECTO` por una lectura externa que mostraba residuos antiguos de footer. Se ha repetido la verificacion con dos vias actuales:

- Navegador renderizado real.
- HTTP directo actual con `cache: no-store` desde entorno Node.

## Resultado actual

`CORREGIDO Y VERIFICADO` en footer publico actual para idiomas prioritarios:

- ES `https://www.matchwalls.com/`: sin `Tarjeta regalo`, sin `Envios internacionales`, sin `Black Friday 2024`, sin `PROFESIONALES & SOCIAL`.
- EN `https://www.matchwalls.com/en`: sin `Gift Card`, sin `Gift card`, sin `International shipments`, sin `Black Friday 2024`, sin `Professional & social`.
- FR `https://www.matchwalls.com/fr`: sin `Carte-cadeau`, sin `Envois internationaux`, sin `Black Friday 2024`.
- DE `https://www.matchwalls.com/de`: sin `Geschenkkarte`, sin `Black Friday 2024`.
- NL `https://www.matchwalls.com/nl`: sin `Cadeaubon`, sin `Black Friday 2024`.

## Shopify Admin contrastado

- Los menus vivos accesibles por Admin GraphQL no contienen los IDs ni textos antiguos.
- `footer-matchwalls` sigue vacio y no referenciado por `sections/footer-group.json`.
- `translatableResourcesByIds` no devuelve recursos para:
  - `gid://shopify/Link/493550239971`.
  - `gid://shopify/Link/493550371043`.
  - `gid://shopify/Link/712964669816`.
  - `gid://shopify/Link/713032991096`.
  - `gid://shopify/Link/493556662499`.

## Interpretacion

Hecho verificado:

- La web actual servida por HTTP directo y el DOM renderizado estan limpios para el residuo concreto del footer.

Inferencia:

- La evidencia externa previa con residuos parece corresponder a cache/extraccion stale o no actual.

No afirmado:

- No se afirma que Google, Bing, Search Console o sistemas IA ya hayan recrawleado.
- No se afirma que la web este 100% optimizada fuera del alcance del footer.
- No se afirma mejora de ranking, trafico o citas IA.

## Acciones no realizadas

- No se modifico Shopify.
- No se modifico LangShop.
- No se importaron CSV.
- No se borraron traducciones.
- No se ejecutaron mutaciones.
- No se modificaron menus, tema, handles, URLs, redirecciones, productos, colecciones ni inventario.

## Documentos actualizados

- `diagnostico-lote-MW-LANGSHOP-PUBLIC-FOOTER-RESIDUE-007-2026-06-17.md`.
- `matriz-lote-MW-LANGSHOP-PUBLIC-FOOTER-RESIDUE-007-2026-06-17.csv`.

## Siguiente paso

Cerrar este residuo concreto sin escritura. Continuar con el siguiente bloque tecnico: indexabilidad, canonical/hreflang, sitemaps, 404/redirects y deuda de tema/traducciones que afecte a SEO/GEO real.

---

# Diagnostico preparatorio MW-INDEXABILITY-TECH-008

**Fecha y hora:** 2026-06-17 21:56:58 +02:00.  
**Tipo:** diagnostico de solo lectura; no se ejecuto ninguna escritura.  
**Estado global del bloque:** `INCOMPLETO`.

## Alcance

Se inicio la preparacion del siguiente bloque tecnico para reducir ruido de indexacion y mejorar la comprension SEO/GEO de `matchwalls.com`.

Superficies revisadas:

- Sitemap publico y grupos sospechosos.
- URLs publicas puntuales.
- Shopify Admin en solo lectura para recursos concretos.
- Tema MAIN real.
- Auditorias internas y backlog priorizado.

## Estado real comprobado

### Tema MAIN

`VERIFICADO Y CORRECTO`

- ID: `gid://shopify/OnlineStoreTheme/178383749496`.
- Nombre: `SEO schema hotfix - 2026-06-15`.
- Rol: `MAIN`.
- `processing`: `false`.
- `processingFailed`: `false`.

### Black Friday

`INCORRECTO`

- Coleccion Shopify ID `gid://shopify/Collection/646234440056`.
- Handle ES `papel-pintado-black-friday`.
- Pagina publica indexable 200 con canonical self.
- H1 publico ES: `BLACK FRIDAY 2024`.
- SEO description Shopify contiene `Black Friday 2024`.
- En EN se observo title `Wallpaper Black Friday 2025 - Wallpaper Sale` y H1 `Black Friday 2024`.

### Muestras indexables

`VERIFICADO PERO MEJORABLE`

- Ejemplo verificado: producto `Muestra Abstract Curves Negro`.
- ID `gid://shopify/Product/8554043474147`.
- Estado `ACTIVE`.
- Publicado.
- Template `muestra`.
- Pagina publica 200, canonical self, sin `noindex`.
- Auditoria previa `CAT-01` detecta al menos 541 URLs de muestra.

### Handles con typos

`INCORRECTO`

- `norid/noridcas`: 70 URLs detectadas en inventario/sitemap previo.
- `enchathed`: 19 URLs detectadas.
- Ejemplo Shopify Admin: producto `LÃƒÆ’Ã‚Â­neas NÃƒÆ’Ã‚Â³rdicas Negro`, ID `gid://shopify/Product/8474101645539`, handle `lineas-noridcas-negro`, estado `ACTIVE`.
- URL francesa con `matchalls` responde 200 y canonical self en comprobacion publica previa del bloque.

### Paginas con H1/contenido principal ausente

`INCORRECTO`

Ejemplos publicos puntuales:

- `/en/pages/request-your-sample`: 200, canonical self, H1 count 0.
- `/fr/pages/a-propos-de-nous`: 200, canonical self, H1 count 0.
- `/nl/pages/over-ons`: 200, canonical self, H1 count 0.

Coincide con `CON-05`, `INT-10` y `TEC-02`.

### URLs `facade-variants/test`

`INCOMPLETO`

- Inventario local historico contiene 7 URLs `facade-variants/test`.
- Peticiones puntuales actuales respondieron 301 a home localizada.
- Shopify Admin no encontro pagina publicada ni redireccion manual `facade-variants`.
- Tras el rastreo, `sitemap.xml` empezo a devolver `429 Verifying your connection`; queda pendiente revalidar cuando no haya proteccion temporal.

### Search Console

`DECLARADO PERO NO VERIFICADO`

Daniel aporto capturas con volumen de 404, noindex, canonical, redirects, 5xx y URLs rastreadas/descubiertas sin indexar. No existe acceso directo ni export URL a URL en esta sesion, por lo que se registra como evidencia aportada pendiente de cruce.

## Incidencias

- Al ampliar el muestreo publico, `sitemap.xml` y algunas URLs empezaron a devolver `429 Verifying your connection`.
- Se detuvo el rastreo publico para no sobrecargar ni contaminar mas la medicion.
- Este `429` se clasifica como `NO ACCESIBLE` temporal para esta sesion, no como fallo SEO confirmado.

## Acciones no realizadas

- No se modifico Shopify.
- No se modifico LangShop.
- No se importaron CSV.
- No se borraron traducciones.
- No se ejecutaron mutaciones.
- No se modificaron menus, tema, handles, URLs, redirecciones, productos, colecciones ni inventario.

## Documentos generados

- `diagnostico-lote-MW-INDEXABILITY-TECH-008-2026-06-17.md`.
- `propuesta-lote-MW-INDEXABILITY-TECH-008-2026-06-17.md`.
- `matriz-lote-MW-INDEXABILITY-TECH-008-2026-06-17.csv`.

## Siguiente paso recomendado

Presentar a Daniel el primer sublote ejecutable. Recomendacion: `MW-INDEXABILITY-BLACK-FRIDAY-CLEANUP-008A`, porque es pequeno, actual, visible e indexable. No ejecutarlo hasta decision comercial y aprobacion exacta con `APROBADO LOTE MW-INDEXABILITY-BLACK-FRIDAY-CLEANUP-008A`.

---

# Diagnostico preparatorio MW-THEME-PAGE-H1-SEMANTIC-008E

**Fecha y hora:** 2026-06-17 22:12:59 +02:00.  
**Tipo:** diagnostico de solo lectura; no se ejecuto ninguna escritura.  
**Estado global del bloque:** `INCOMPLETO`.

## Alcance

Se reviso el origen tecnico de paginas publicas con H1 ausente detectadas durante `MW-INDEXABILITY-TECH-008`.

Superficies revisadas:

- Tema MAIN real.
- Archivos `sections/main-page.liquid`, `templates/page.json`, `templates/page.muestras.json`, `templates/page.muestras-2.json`, `templates/page.sobre-nosotros.json` y `templates/page.faq.json`.
- Lista de paginas Shopify y sus `templateSuffix`.

## Estado real comprobado

### Tema MAIN

`VERIFICADO Y CORRECTO`

- ID: `gid://shopify/OnlineStoreTheme/178383749496`.
- Nombre: `SEO schema hotfix - 2026-06-15`.
- Rol: `MAIN`.

### Seccion base `main-page`

`VERIFICADO Y CORRECTO`

- `sections/main-page.liquid` renderiza `<h1 class="h1 text-center">{{ page.title }}</h1>`.
- Tambien renderiza `{{ page.content }}` cuando existe contenido.

### Plantilla de muestras

`INCORRECTO`

- Pagina `Solicita muestras de papel pintado`, ID `gid://shopify/Page/106299195619`, publicada.
- Template suffix: `muestras-2`.
- `templates/page.muestras-2.json` tiene `main-page` con `"disabled": true`.
- Publico EN observado previamente: `/en/pages/request-your-sample` con H1 count 0.

### Plantilla sobre nosotros

`INCORRECTO`

- Pagina `Sobre Nosotros ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â MatchWalls, expertos en papel pintado mural`, ID `gid://shopify/Page/106231464163`, publicada.
- Template suffix: `sobre-nosotros`.
- `templates/page.sobre-nosotros.json` tiene `main-page` con `"disabled": true`.
- El hero principal usa `heading_tag: h2`.
- Publico FR/NL observado previamente: H1 count 0.

### Plantilla FAQ

`VERIFICADO Y CORRECTO`

- `templates/page.faq.json` mantiene `main-page` activo.
- Publico EN observado previamente: H1 presente.

## Interpretacion

Hecho verificado:

- El problema de H1 ausente no es solo LangShop.
- Hay plantillas JSON del tema publicado que desactivan la seccion encargada de renderizar `page.title` como H1.

Inferencia:

- LangShop puede tener textos/traducciones guardados correctamente, pero si la plantilla oculta `main-page`, los buscadores no reciben el HTML semantico esperado.

## Acciones no realizadas

- No se modifico Shopify.
- No se modifico LangShop.
- No se importaron CSV.
- No se ejecutaron mutaciones.
- No se modifico el tema MAIN.
- No se publicaron temas.
- No se cambiaron handles, URLs, redirecciones, productos, colecciones ni inventario.

## Documentos generados

- `diagnostico-lote-MW-THEME-PAGE-H1-SEMANTIC-008E-2026-06-17.md`.
- `propuesta-lote-MW-THEME-PAGE-H1-SEMANTIC-008E-2026-06-17.md`.
- `matriz-lote-MW-THEME-PAGE-H1-SEMANTIC-008E-2026-06-17.csv`.

## Siguiente paso recomendado

Preparar hotfix en tema auxiliar/unpublished con el lote:

`MW-THEME-PAGE-H1-SEMANTIC-008E`

No ejecutar ni publicar nada hasta aprobacion exacta:

`APROBADO LOTE MW-THEME-PAGE-H1-SEMANTIC-008E`

---

# Intento de ejecucion MW-THEME-PAGE-H1-SEMANTIC-008E

**Fecha y hora:** 2026-06-17 22:46:21 +02:00.  
**Aprobacion recibida:** `APROBADO LOTE MW-THEME-PAGE-H1-SEMANTIC-008E`.  
**Estado global del bloque:** `INCOMPLETO`.

## Alcance aprobado

Preparar un hotfix en tema auxiliar no publicado para corregir ausencia de H1 semantico en:

- `templates/page.muestras-2.json`.
- `templates/page.sobre-nosotros.json`.
- `templates/page.muestras.json` solo si se verificaba uso/riesgo real.

No estaba aprobado publicar tema, editar MAIN, cambiar handles, URLs, redirecciones, productos, colecciones, inventario ni ejecutar cambios en LangShop.

## Estado real comprobado antes de cualquier escritura

### Tema MAIN

`VERIFICADO Y CORRECTO`

- ID: `gid://shopify/OnlineStoreTheme/178383749496`.
- Nombre: `SEO schema hotfix - 2026-06-15`.
- Rol: `MAIN`.

### Tema auxiliar seleccionado

`VERIFICADO Y CORRECTO`

- ID: `gid://shopify/OnlineStoreTheme/178390401400`.
- Nombre: `MW-FOOTER-I18N-001 - QA - 2026-06-17`.
- Rol: `UNPUBLISHED`.
- Motivo de seleccion: coincide con MAIN en los archivos objetivo revisados.

### Comparacion de archivos objetivo

`VERIFICADO Y CORRECTO`

El tema auxiliar coincide con MAIN en:

- `sections/main-page.liquid`: checksum `8330fa7d1cd5ce4929978d2599b2062c`.
- `templates/page.muestras-2.json`: checksum `cde44149a1373f45969718e32ba05772`.
- `templates/page.muestras.json`: checksum `e728dd0047cd35df8ab75fed73f90f96`.
- `templates/page.sobre-nosotros.json`: checksum `5841ae151f305c4de246e2044ffa2ed0`.

## Bloqueo tecnico

`REQUIERE DECISION HUMANA`

Shopify Admin API permite leer el archivo `templates/page.muestras-2.json`, pero la herramienta disponible en esta sesion recorta la salida visible del contenido del archivo grande. El archivo tiene tamano `49863` bytes. No hay copia local completa del JSON en la carpeta del proyecto, en `shopify-staging`, ni en las ubicaciones de descarga revisadas. Shopify CLI no esta disponible en el entorno.

El esquema GraphQL de Shopify confirma que para archivos de tema las operaciones disponibles son copiar, borrar o sobrescribir el archivo completo. No existe una mutacion de parche parcial de settings JSON para este caso.

## Acciones ejecutadas

- Consultas de solo lectura a Shopify Admin.
- Comparacion de tema MAIN y tema auxiliar.
- Busqueda local de copias completas de plantillas.
- Verificacion de disponibilidad de Shopify CLI.
- Revision de esquema GraphQL para confirmar ausencia de actualizacion parcial.

## Acciones no realizadas

- No se ejecuto ninguna mutacion.
- No se modifico Shopify.
- No se modifico el tema MAIN.
- No se modifico el tema auxiliar.
- No se publico ningun tema.
- No se duplico ningun tema.
- No se modifico LangShop.
- No se cambiaron handles, URLs, canonicals, redirecciones, productos, colecciones ni inventario.

## Motivo de no ejecucion

Sobrescribir `templates/page.muestras-2.json` sin disponer del cuerpo completo y exacto del archivo supondria riesgo de perdida de secciones, bloques o configuraciones visuales. Por rigor tecnico, el lote se detuvo antes de cualquier escritura.

## Siguiente paso necesario

Para ejecutar el hotfix con seguridad se requiere una de estas vias:

- Descargar/exportar el tema auxiliar completo desde Shopify Admin y colocar el ZIP o las plantillas en el proyecto.
- Instalar/autenticar Shopify CLI para hacer un `theme pull` controlado de los archivos objetivo.
- Autorizar un nuevo lote alternativo que use otro enfoque tecnico, con propuesta previa y riesgos documentados.

Hasta entonces, el estado de `MW-THEME-PAGE-H1-SEMANTIC-008E` queda `INCOMPLETO`.

---

# Continuacion de ejecucion MW-THEME-PAGE-H1-SEMANTIC-008E tras ZIP local

**Fecha y hora:** 2026-06-18 00:21:43 +02:00.  
**Aprobacion recibida:** `APROBADO LOTE MW-THEME-PAGE-H1-SEMANTIC-008E`.  
**Estado global del bloque:** `INCOMPLETO`.

## Archivo recibido y copia de trabajo

`VERIFICADO Y CORRECTO`

- ZIP localizado en proyecto: `theme_export__www-matchwalls-com-mw-footer-i18n-001-qa-2026-06-17__17JUN2026-1115pm.zip`.
- Tamano del ZIP recibido: `3031566` bytes.
- Copia extraida de trabajo: `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E`.
- Respaldo local creado en `auditoria-seo-geo-matchwalls/backups/MW-THEME-PAGE-H1-SEMANTIC-008E-2026-06-17`.

## Valores originales respaldados

`VERIFICADO Y CORRECTO`

- `templates/page.muestras-2.json`: checksum original Shopify/local `cde44149a1373f45969718e32ba05772`.
- `templates/page.sobre-nosotros.json`: checksum original Shopify/local `5841ae151f305c4de246e2044ffa2ed0`.

## Cambios preparados en local

`VERIFICADO Y CORRECTO`

Se preparo en ambas plantillas una seccion `custom-liquid` llamada `seo_page_h1_008e`, situada como primera seccion en `order`, para renderizar:

- `<h1 class="h1 text-center">{{ page.title }}</h1>`.

Se mantuvo `main-page` desactivada para evitar duplicar el contenido completo de pagina.

Checksums locales modificados:

- `templates/page.muestras-2.json`: `B3B958A7CF7D39F154EE4E2B269E92C3`.
- `templates/page.sobre-nosotros.json`: `EE8A590859803459779C7D408DEEE46D`.

Archivos compactados auxiliares usados solo para API:

- `templates/page.muestras-2.compact.json`: `3CE586EB438559814CB201C759F42622`, `31698` bytes.
- `templates/page.sobre-nosotros.compact.json`: `9425E8FA4CDFFBCFB7F8F941BC5CBC8D`, `15550` bytes.

## Escrituras ejecutadas en Shopify

### `templates/page.sobre-nosotros.json`

`CORREGIDO Y VERIFICADO`

- Tema afectado: `gid://shopify/OnlineStoreTheme/178390401400`.
- Nombre del tema: `MW-FOOTER-I18N-001 - QA - 2026-06-17`.
- Rol del tema: `UNPUBLISHED`.
- Mutacion usada: `themeFilesUpsert`.
- Resultado de mutacion: `0 userErrors`.
- Readback posterior:
  - Tamano remoto: `15550` bytes.
  - Checksum remoto: `9425e8fa4cdffbcfb7f8f941bc5cbc8d`.
- Verificacion: coincide con el archivo compacto local preparado.

### `templates/page.muestras-2.json`

`INCOMPLETO`

- Tema afectado: `gid://shopify/OnlineStoreTheme/178390401400`.
- Nombre del tema: `MW-FOOTER-I18N-001 - QA - 2026-06-17`.
- Rol del tema: `UNPUBLISHED`.
- Estado remoto posterior a la verificacion:
  - Tamano remoto: `49863` bytes.
  - Checksum remoto: `cde44149a1373f45969718e32ba05772`.
- Interpretacion: Shopify conserva todavia el archivo original; el H1 semantico no esta aplicado en esta plantilla remota.
- Incidencia previa registrada: un intento de carga por API con base64 ensamblado fallo con `JSON invalido en templates/page.muestras-2.json (files)`. No se aplicaron cambios en ese archivo.

## Validaciones realizadas

- Consulta de esquema Shopify Admin para `OnlineStoreTheme`, `OnlineStoreThemeFile`, `Mutation` y `OnlineStoreThemeFilesUpsertFileInput`.
- Validacion GraphQL de lectura: `VERIFICADO Y CORRECTO`.
- Validacion GraphQL de mutacion `themeFilesUpsert`: `VERIFICADO Y CORRECTO`.
- Busqueda de documentacion Shopify Liquid para secciones en templates JSON: `VERIFICADO Y CORRECTO`.
- Validador oficial del skill Shopify Liquid: `NO ACCESIBLE`; fallo por dependencia ausente `@shopify/theme-check-common`.
- Validacion local JSON: `VERIFICADO Y CORRECTO` en ambas plantillas preparadas.

## Artefactos locales generados

`VERIFICADO Y CORRECTO`

- ZIP limpio preparado para alternativa manual/importacion:
  - `MW-THEME-PAGE-H1-SEMANTIC-008E-patched-QA-2026-06-17-2331.zip`.
  - Tamano: `3031813` bytes.
  - MD5: `323EB696E6052D85D612C99375AD0B26`.
  - Entradas: `306`.
  - No incluye archivos `*.compact.json`.
  - Incluye `templates/page.muestras-2.json`.
  - Incluye `templates/page.sobre-nosotros.json`.
- Artefacto local fallido sin uso:
  - `MW-THEME-PAGE-H1-SEMANTIC-008E-patched-QA-2026-06-17-2329.zip`.
  - Tamano: `0` bytes.
  - Estado: `INCORRECTO`; no debe usarse.

## Acciones no realizadas

- No se modifico el tema MAIN.
- No se publico ningun tema.
- No se importo el ZIP limpio en Shopify.
- No se duplico ni renombro ningun tema.
- No se modifico LangShop.
- No se cambiaron handles, URLs, canonicals, redirecciones, productos, colecciones ni inventario.

## Reversion

`VERIFICADO Y CORRECTO`

- Para `templates/page.sobre-nosotros.json`, revertir en el tema QA subiendo el respaldo `templates__page.sobre-nosotros.original.5841ae151f305c4de246e2044ffa2ed0.json`.
- Para `templates/page.muestras-2.json`, no hay reversion remota necesaria porque el archivo remoto sigue intacto con checksum original `cde44149a1373f45969718e32ba05772`.

## Siguiente decision necesaria

`REQUIERE DECISION HUMANA`

Queda pendiente aplicar `templates/page.muestras-2.json` al tema QA. Opciones seguras:

- Editar manualmente en Shopify Admin solo `templates/page.muestras-2.json` del tema QA usando el archivo local preparado.
- Autorizar importacion controlada del ZIP limpio como nuevo tema no publicado.
- Habilitar una via tecnica estable para subida directa de archivo completo, como Shopify CLI autenticado o una subida temporal verificada.

Hasta completar esa decision y verificar el resultado publico en preview, el lote no puede marcarse como `CORREGIDO Y VERIFICADO`.

---

# 2026-06-18 00:36:43 +02:00 - Continuacion lote MW-THEME-PAGE-H1-SEMANTIC-008E

## Objetivo de la continuacion

`INCOMPLETO`

- Terminar la aplicacion de `templates/page.muestras-2.json` exclusivamente en el tema QA `MW-FOOTER-I18N-001 - QA - 2026-06-17`.
- No publicar tema.
- No modificar tema MAIN.
- No modificar ningun otro archivo del tema.

## Estado real comprobado antes de actuar

`VERIFICADO Y CORRECTO`

- Tema Shopify comprobado por lectura:
  - ID: `gid://shopify/OnlineStoreTheme/178390401400`.
  - Nombre: `MW-FOOTER-I18N-001 - QA - 2026-06-17`.
  - Rol: `UNPUBLISHED`.
  - `processing`: `false`.
  - `processingFailed`: `false`.
- Archivo remoto `templates/page.muestras-2.json`:
  - Tamano: `49863`.
  - Checksum MD5: `cde44149a1373f45969718e32ba05772`.
  - Actualizado: `2026-06-17T08:13:12Z`.
  - Estado: conserva el archivo original; H1 semantico todavia no aplicado.
- Archivo remoto `templates/page.sobre-nosotros.json`:
  - Tamano: `15550`.
  - Checksum MD5: `9425e8fa4cdffbcfb7f8f941bc5cbc8d`.
  - Estado: cambio aplicado previamente.

## Validacion local previa

`VERIFICADO Y CORRECTO`

- Archivo local preparado `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E/templates/page.muestras-2.json`:
  - Tamano: `50111`.
  - MD5: `B3B958A7CF7D39F154EE4E2B269E92C3`.
  - Contiene `seo_page_h1_008e`: `true`.
  - `seo_page_h1_008e` aparece primero en `order`: `true`.
  - `main` queda desactivado: `true`.
  - Prueba UTF-8: `true`.
- Archivo compacto preparado `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E/templates/page.muestras-2.compact.json`:
  - Tamano: `31698`.
  - MD5: `3CE586EB438559814CB201C759F42622`.
  - Contiene `seo_page_h1_008e`: `true`.
  - `seo_page_h1_008e` aparece primero en `order`: `true`.
  - `main` queda desactivado: `true`.
  - Prueba UTF-8: `true`.

## Incidencia

`REQUIERE DECISION HUMANA`

- Se intento abrir el editor de codigo del tema QA en Shopify Admin mediante navegador de Codex:
  - URL: `https://admin.shopify.com/store/www-matchwalls-com/themes/178390401400/code?key=templates%2Fpage.muestras-2.json`.
- Shopify/Admin mostro verificacion previa:
  - Mensaje visible: `Se debe verificar tu conexion antes de poder continuar`.
- No se introdujeron credenciales.
- No se guardo ningun archivo.
- No se ejecuto ninguna mutacion de escritura.

## Estado final de esta continuacion

`INCOMPLETO`

- `templates/page.muestras-2.json` sigue pendiente en Shopify QA.
- Siguiente paso: Daniel debe superar la verificacion del Admin en el navegador visible de Codex o proporcionar una via tecnica alternativa estable para aplicar solo este archivo.

---

# 2026-06-18 - Pausa operativa por iframe Shopify Admin

## Lote

`MW-THEME-PAGE-H1-SEMANTIC-008E`

## Estado

`INCOMPLETO`

## Hechos verificados

- Shopify Admin ya esta autenticado en la tienda `matchwalls`.
- La pagina de temas de Shopify carga dentro de un iframe de `online-store-web.shopifyapps.com`.
- El navegador de Codex puede ver la pagina, pero no puede interactuar dentro de ese iframe por restriccion tecnica de iframe cross-origin.
- No se ha guardado ningun cambio en Shopify en esta pausa.
- No se ha publicado ningun tema.
- No se ha tocado el tema MAIN.

## Archivo preparado para pegado manual

`VERIFICADO Y CORRECTO`

- Archivo copiado al portapapeles del navegador:
  - `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E/templates/page.muestras-2.compact.json`.
- MD5 esperado tras guardar en Shopify:
  - `3CE586EB438559814CB201C759F42622`.
- Validaciones del contenido copiado:
  - Contiene `seo_page_h1_008e`: `true`.
  - `seo_page_h1_008e` aparece primero en `order`: `true`.

## Siguiente accion manual necesaria

`REQUIERE DECISION HUMANA`

- Daniel debe pegar el contenido del portapapeles en `templates/page.muestras-2.json` del tema QA `MW-FOOTER-I18N-001 - QA - 2026-06-17` y guardar.
- Despues, Codex verificara por lectura:
  - checksum remoto,
  - preview publico del tema QA,
  - existencia de un unico H1 semantico,
  - ausencia de H1 duplicado.

---

# 2026-06-18 00:58:01 +02:00 - Verificacion tras guardado manual declarado

## Lote

`MW-THEME-PAGE-H1-SEMANTIC-008E`

## Estado

`INCOMPLETO`

## Resultado de lectura remota Shopify

`INCORRECTO`

- Daniel indico `guardado`.
- Lectura posterior por Shopify Admin API:
  - Tema: `MW-FOOTER-I18N-001 - QA - 2026-06-17`.
  - ID: `gid://shopify/OnlineStoreTheme/178390401400`.
  - Rol: `UNPUBLISHED`.
  - Archivo `templates/page.muestras-2.json`:
    - Tamano remoto: `49863`.
    - Checksum remoto: `cde44149a1373f45969718e32ba05772`.
    - `updatedAt`: `2026-06-17T08:13:12Z`.
- Interpretacion: el archivo remoto no cambio; sigue siendo el original.

## Comprobacion visual

`VERIFICADO PERO MEJORABLE`

- Captura del editor Shopify muestra que `templates/page.muestras-2.json` sigue empezando con el comentario verde inicial de Shopify.
- El archivo compacto preparado no empieza con comentario; empieza por:
  - `{"sections":{"multi_column_TbfrNB":{"typ`

## Portapapeles preparado de nuevo

`VERIFICADO Y CORRECTO`

- Se copio de nuevo al portapapeles de Windows el archivo:
  - `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E/templates/page.muestras-2.compact.json`.
- MD5 esperado: `3CE586EB438559814CB201C759F42622`.
- Validacion oficial Shopify Liquid: `NO ACCESIBLE`, por dependencia ausente `@shopify/theme-check-common`.
- Validacion local JSON previa: `VERIFICADO Y CORRECTO`.

## Acciones no realizadas

- No se publico ningun tema.
- No se modifico el tema MAIN.
- No se verifico preview porque el archivo QA remoto sigue original.

---

# 2026-06-18 01:17:59 +02:00 - Verificacion correcta tras segundo guardado manual

## Lote

`MW-THEME-PAGE-H1-SEMANTIC-008E`

## Estado

`CORREGIDO Y VERIFICADO`

## Recurso modificado

- Tema QA: `MW-FOOTER-I18N-001 - QA - 2026-06-17`.
- ID tema QA: `gid://shopify/OnlineStoreTheme/178390401400`.
- Rol: `UNPUBLISHED`.
- Archivo: `templates/page.muestras-2.json`.
- Pagina Shopify asociada:
  - ID: `gid://shopify/Page/106299195619`.
  - Titulo: `Solicita muestras de papel pintado`.
  - Handle: `muestras`.
  - URL publica: `https://www.matchwalls.com/pages/muestras`.
  - Template suffix: `muestras-2`.
  - Publicada: `true`.

## Resultado de lectura remota Shopify

`VERIFICADO Y CORRECTO`

- Archivo QA `templates/page.muestras-2.json`:
  - Tamano remoto: `31698`.
  - Checksum remoto: `3ce586eb438559814cb201c759f42622`.
  - Checksum esperado local: `3CE586EB438559814CB201C759F42622`.
  - `updatedAt`: `2026-06-17T23:12:10Z`.
- Interpretacion: Shopify guardo exactamente el archivo compacto preparado.

## Verificacion publica en preview QA

`VERIFICADO Y CORRECTO`

- URL verificada: `https://www.matchwalls.com/pages/muestras`.
- Canonical detectado: `https://www.matchwalls.com/pages/muestras`.
- Titulo HTML detectado: `Muestras de papel pintado - MatchWalls`.
- Idioma HTML detectado: `es`.
- H1 encontrados: `1`.
- H1 detectado:
  - `Solicita muestras de papel pintado`.
- HTML H1 detectado:
  - `<h1 class="h1 text-center">Solicita muestras de papel pintado</h1>`.
- Resultado: existe un unico H1 semantico y no se detecta H1 duplicado.

## Comprobacion del tema publicado MAIN

`VERIFICADO Y CORRECTO`

- Tema MAIN: `SEO schema hotfix - 2026-06-15`.
- ID tema MAIN: `gid://shopify/OnlineStoreTheme/178383749496`.
- Rol: `MAIN`.
- Archivo MAIN `templates/page.muestras-2.json`:
  - Tamano remoto: `49863`.
  - Checksum remoto: `cde44149a1373f45969718e32ba05772`.
  - `updatedAt`: `2026-06-15T12:34:18Z`.
- Interpretacion: el tema publicado no fue modificado por este lote.

## Incidencias

`NO ACCESIBLE`

- La validacion oficial local de Shopify Liquid no pudo ejecutarse por dependencia ausente:
  - `@shopify/theme-check-common`.
- Mitigacion aplicada:
  - Validacion JSON local previa.
  - Lectura remota de checksum exacto en Shopify.
  - Verificacion publica del HTML renderizado.

## Acciones no realizadas

- No se publico ningun tema.
- No se edito el tema MAIN.
- No se cambiaron handles, canonicals, redirecciones, productos, inventario ni traducciones.

---

# 2026-06-18 13:04:09 +02:00 - Lote MW-THEME-PAGE-H1-SEMANTIC-008E-ISOLATED-QA

## Aprobacion y alcance

**Aprobacion exacta recibida:** `APROBADO LOTE MW-THEME-PAGE-H1-SEMANTIC-008E-ISOLATED-QA`.

**Estado final del alcance aprobado:** `CORREGIDO Y VERIFICADO`.

- Preparacion y QA de un tema nuevo no publicado derivado del MAIN.
- Aplicacion exclusiva de 17 plantillas de pagina para incorporar un H1 semantico basado en `page.title`.
- Cobertura publica: ES, EN, FR, DE y NL.
- No incluia publicacion, edicion del MAIN, cambios editoriales, traducciones, handles, canonicals ni redirecciones.

## Temas verificados

`VERIFICADO Y CORRECTO`

- MAIN: `SEO schema hotfix - 2026-06-15`.
- ID MAIN: `gid://shopify/OnlineStoreTheme/178383749496`.
- Rol MAIN: `MAIN`.
- Tema aislado: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- ID tema aislado: `gid://shopify/OnlineStoreTheme/178396463480`.
- Rol tema aislado: `UNPUBLISHED`.
- Ningun tema fue publicado durante este lote.

## Archivos autorizados y valores verificados

| Pagina / ID | Archivo | MD5 MAIN | MD5 tema aislado |
|---|---|---|---|
| Murales / `106204922083` | `templates/page.murales.json` | `0d434eddba6c86c8c06bc5dbb6fc445c` | `608718fdd7116e555bdcf5fdf5a7c06f` |
| Crea tu mural / `106205118691` | `templates/page.crea-tu-mural.json` | `360b78a5e2301b5ad02da56946a3e86b` | `eda6842e856f61b10f0fd095d98fd24b` |
| Crea tu papel / `106205151459` | `templates/page.crea-tu-papel-pintado-2.json` | `4e068ae6d3ddb0e17ae9840583fd4196` | `87e61d6d0f4cec45e4fc7127f7c2bad9` |
| Social/prensa / `106205216995` | `templates/page.social_prensa_afiliacion.json` | `78504a72d8cf077256e68dc4bbb1421f` | `7127d1d43815b4dd71b2d409c19f5102` |
| Artistas / `106205315299` | `templates/page.artistas.json` | `73c70d4a07a1db46aa34f43eabf830be` | `f425b1f68bc05472d031caee2ea55546` |
| Medidas paredes / `106229170403` | `templates/page.como-tomar-medidas.json` | `850ff727e452def5bf28ed54282b95d1` | `fdd0b6c621742f3fa10dc8203c2721f2` |
| Medidas techo / `106229203171` | `templates/page.como-medir-el-techo.json` | `3bee4f93ea07d0c27bf0a8954f0b7efe` | `7c5de110da1568f179de7a9363a760d6` |
| Sobre nosotros / `106231464163` | `templates/page.sobre-nosotros.json` | `5841ae151f305c4de246e2044ffa2ed0` | `9425e8fa4cdffbcfb7f8f941bc5cbc8d` |
| Nuestros productos / `106278256867` | `templates/page.nuestros-productos.json` | `1fdb4706790d746f0f066c6c0b37df01` | `e80c1b8fd5ae9f6c89bb94a66e213b89` |
| Metodos de pago / `106278387939` | `templates/page.metodos-de-pago.json` | `11c7e3b186e241125a802bb58e413c39` | `f68ad0141b1faf10c0358d6f9f4576f6` |
| Envios / `106278420707` | `templates/page.envios-y-devoluciones.json` | `e38f3499d781c72026d0fdaa4b74b4fe` | `c53fd09a57a7774d704d71f5ad3d0b14` |
| Estudios profesionales / `106279141603` | `templates/page.estudios-profesionales.json` | `73a1879657b43f3691d9b0bd80750eea` | `0e215a64609cefa10e0186f52a958bcb` |
| Muestras / `106299195619` | `templates/page.muestras-2.json` | `cde44149a1373f45969718e32ba05772` | `3ce586eb438559814cb201c759f42622` |
| Formulario profesional / `107014947043` | `templates/page.formulario-profesionales.json` | `3862897fd55ac071d8d13f5cdf872f7b` | `b707446ef165845fe14955993217916f` |
| Guia instalacion / `107326210275` | `templates/page.guias-de-instalacion.json` | `b42409b2f571e85fb79dac0b4f9a8d1` | `0defa6bf82f44e1600080889dc2e7c21` |
| Tarjeta regalo / `107793481955` | `templates/page.tarjeta-regalo.json` | `1f6b51fbd8bea2cb09b7004434c549ad` | `a7e3115485f46903cc4244d71bc91be3` |
| Formulario particulares / `108429672675` | `templates/page.formulario-particulares.json` | `240cb2b9113019d662277b4d95e11cce` | `689a93338f44f9730632fb5285e58e11` |

## Aislamiento tecnico

`VERIFICADO Y CORRECTO`

- MAIN: `306` archivos.
- Tema aislado: `306` archivos.
- Archivos ausentes: `0`.
- Archivos adicionales: `0`.
- Diferencias funcionales: exclusivamente las 17 plantillas autorizadas.
- Diferencias binarias adicionales generadas por Shopify:
  - `assets/country-flags.css`.
  - `assets/sections.js`.
  - `assets/theme.js`.
- Los tres assets son identicos tras normalizar exclusivamente ID de tema, prefijo `/cdn/shop/t/.../` y versiones CDN `?v=...`; no se detectaron diferencias de logica.
- `config/settings_data.json` coincide exactamente: MD5 `a1192f2f698d277e0f69f7156a61a90c`.
- `layout/theme.liquid` coincide exactamente: MD5 `13cf45059f0dd8095055644fafd3da8d`.
- `sections/footer-group.json` coincide exactamente: MD5 `e93af9228c8a97dce4ad91e203bf7e75`.

## QA publico internacional

`CORREGIDO Y VERIFICADO`

- `85` comprobaciones en escritorio: 17 paginas x ES/EN/FR/DE/NL.
- `85` comprobaciones en movil con viewport `390 x 844`.
- Total: `170` comprobaciones de URL/contexto.
- En todas las comprobaciones:
  - se renderizo el tema `178396463480`;
  - existe exactamente un H1 no vacio;
  - el canonical es self y corresponde a la URL localizada;
  - existen alternates hreflang ES/EN/FR/DE/NL;
  - `html lang` coincide con el idioma;
  - no se detecto `noindex` accidental;
  - el contenido principal no esta vacio;
  - no se mostro pagina de error de Shopify.
- App Embeds y scripts publicos observados coinciden entre MAIN y tema aislado tras completar la carga dinamica: LangShop, Instafeed, formulario de contacto, Pandectes, Wishlist, Inbox, Shopify Forms y Klaviyo.

## Incidencias preexistentes, no atribuibles al lote

`VERIFICADO PERO MEJORABLE`

- Error global JavaScript `Cannot read properties of null (reading 'addEventListener')`: reproducido tambien en MAIN.
- `SyntaxError: Unexpected token ','` en `/nl/pages/onze-producten`: reproducido tambien en MAIN.
- Desbordamiento horizontal movil:
  - FR: `17/17` paginas, ancho `408` frente a viewport cliente `375`.
  - NL: `17/17` paginas, anchos `381` y `405` frente a viewport cliente `375`.
- Los mismos anchos se reprodujeron en MAIN en muestras representativas FR/NL; no son regresion del tema aislado.

## Respaldo y reversion

`VERIFICADO Y CORRECTO`

- Respaldos iniciales: `auditoria-seo-geo-matchwalls/backups/MW-THEME-PAGE-H1-SEMANTIC-008E-2026-06-17`.
- Respaldos del lote ampliado: `auditoria-seo-geo-matchwalls/backups/MW-THEME-PAGE-H1-SEMANTIC-008E-2026-06-18-batch-pages`.
- Reversion: mantener el tema `178396463480` sin publicar y restaurar en el exclusivamente los 17 archivos originales.
- El MAIN no requiere reversion porque no fue modificado.

## Acciones no realizadas

- No se publico ningun tema.
- No se modifico el tema MAIN.
- No se cambiaron titulos, traducciones, handles, canonicals, hreflang, redirecciones ni contenido editorial.
- No se modificaron productos, colecciones, precios, inventario, variantes, imagenes, App Embeds ni configuracion de LangShop.

## Estado final

- Preparacion del tema aislado: `CORREGIDO Y VERIFICADO`.
- QA internacional desktop/mobile: `CORREGIDO Y VERIFICADO`.
- Tema aislado: `UNPUBLISHED`.
- Publicacion: `REQUIERE DECISION HUMANA` y requiere un lote independiente con aprobacion exacta.

## Matriz generada

- `matriz-lote-MW-THEME-PAGE-H1-SEMANTIC-008E-ISOLATED-QA-2026-06-18.csv`.

---

# 2026-06-18 13:35:24 +02:00 - Inicio lote MW-PUBLISH-H1-SEMANTIC-009

## Aprobacion

`VERIFICADO Y CORRECTO`

- Aprobacion exacta recibida:
  `APROBADO LOTE MW-PUBLISH-H1-SEMANTIC-009`.
- Alcance: publicar exclusivamente el tema `178396463480`, conservar el MAIN
  `178383749496` como reversion y repetir 170 pruebas.

## Preflight Shopify

`VERIFICADO Y CORRECTO`

- MAIN `178383749496`: rol `MAIN`, 306 archivos, `processing: false`,
  `processingFailed: false`.
- Candidato `178396463480`: rol `UNPUBLISHED`, 306 archivos,
  `processing: false`, `processingFailed: false`.
- Archivos ausentes: 0. Archivos adicionales: 0.
- Diferencias: 17 plantillas aprobadas y 3 assets generados por Shopify ya
  normalizados en el QA anterior.
- Errores de lectura de archivos: 0.

## Smoke test previo

`VERIFICADO Y CORRECTO`

- Pagina: Muestras.
- Idiomas: ES, EN, FR, DE y NL.
- Tema servido: prefijo `/t/45`, correspondiente a `178396463480`.
- En 5/5: un H1 no vacio, canonical self, `html lang` correcto, sin meta robots
  bloqueante y contenido visible no vacio.

## Bloqueo de publicacion

`REQUIERE DECISION HUMANA`

- Shopify Admin esta autenticado y la tienda Matchwalls es accesible.
- El gestor de temas se carga en un iframe de
  `online-store-web.shopifyapps.com`.
- El navegador de Codex no puede controlar ese iframe y su contenido no queda
  disponible para una publicacion segura.
- La conexion GraphQL disponible bloquea la publicacion de temas.
- No se intento ninguna via alternativa no aprobada.

## Estado posterior

`INCOMPLETO`

- `178383749496` sigue siendo `MAIN`.
- `178396463480` sigue siendo `UNPUBLISHED`.
- No se publico ni modifico ningun tema.
- No se modificaron archivos, contenido, traducciones, URLs, App Embeds,
  LangShop, productos, colecciones ni inventario.

## Accion manual necesaria

Daniel debe publicar en Shopify Admin exclusivamente el tema
`MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`, ID `178396463480`, y
notificar `PUBLICADO`. Codex verificara inmediatamente los roles y ejecutara las
170 pruebas; ante fallo critico, se aplicara la reversion aprobada.

---

# 2026-06-18 19:42:37 +02:00 - Cierre lote MW-PUBLISH-H1-SEMANTIC-009

## Estado final

`CORREGIDO Y VERIFICADO`

## Publicacion y roles

- Tema `178396463480`: rol `MAIN`, prefijo `/t/45`, `processing: false`,
  `processingFailed: false`.
- Tema anterior `178383749496`: rol `UNPUBLISHED`, conservado intacto para
  reversion.
- La publicacion fue ejecutada manualmente por Daniel tras la aprobacion exacta.
- No fue necesaria la reversion.

## QA post-publicacion

`CORREGIDO Y VERIFICADO`

- Escritorio: 85/85 comprobaciones correctas.
- Movil `390 x 844`: 85/85 comprobaciones correctas.
- Total: 170/170.
- Cobertura: 17 paginas, ES/EN/FR/DE/NL.
- En todas: tema `/t/45`, un H1 no vacio, canonical self, hreflang completo,
  `html lang` correcto, sin `noindex` accidental, contenido principal visible y
  sin pagina 404/error Shopify.
- Smoke global: home, producto, coleccion y carrito correctos en escritorio y
  movil; todos sirven `/t/45`.

## Incidencias no atribuibles al lote

`VERIFICADO PERO MEJORABLE`

- Overflow movil: 17/17 FR y 17/17 NL, mismo patron preexistente.
- Error global `addEventListener` reproducido.
- `SyntaxError: Unexpected token ','` observado en Nuestros productos y sus
  cinco idiomas.
- `this.convertToInches is not a function` observado en el customizador de
  producto; `customizer.js` no era una diferencia entre MAIN y candidato.
- Shopify muestra limite de 20 temas. No se elimino ninguno.

## Evidencias

- `qa-post-publicacion-MW-PUBLISH-H1-SEMANTIC-009-2026-06-18.md`.
- `matriz-post-publicacion-MW-PUBLISH-H1-SEMANTIC-009-2026-06-18.csv`.

## Acciones no realizadas

- No se editaron archivos durante la publicacion.
- No se modificaron contenido, traducciones, URLs, handles, canonicals,
  hreflang, redirecciones, productos, colecciones, precios, inventario,
  variantes, imagenes, App Embeds ni LangShop.
- No se elimino ningun tema.

---

# 2026-06-18 19:46:08 +02:00 - Auditoria de biblioteca de temas

## Estado

`VERIFICADO PERO MEJORABLE`

## Cobertura

- 20/20 temas consultados por Shopify Admin GraphQL.
- MAIN, roles, nombres, fechas y estado de publicacion revisados.
- Cinco temas `Copy of Production` comparados por cantidad de archivos.
- Los dos mas antiguos comparados por filename y checksum.

## Resultado

- Shopify ha alcanzado el limite de 20 temas.
- No se elimino ningun tema.
- MAIN `178396463480` y reversion `178383749496` quedan protegidos.
- `MatchWalls/Original/ NO ELIMINAR` queda en `STANDBY`.
- Candidato minimo de limpieza: `142344224995`, `Copy of Production`,
  `UNPUBLISHED`, 289 archivos.
- Su sucesor `142418575587` tiene los mismos 289 filenames y difiere en tres
  assets generados y dos archivos funcionales.

## Siguiente lote propuesto

`REQUIERE DECISION HUMANA`

`MW-THEME-LIBRARY-CLEANUP-009B`: descargar y verificar respaldo ZIP y eliminar
solo `142344224995`. No esta autorizado todavia.

## Evidencias

- `diagnostico-biblioteca-temas-2026-06-18.md`.
- `propuesta-lote-MW-THEME-LIBRARY-CLEANUP-009B-2026-06-18.md`.

---

# 2026-06-18 19:48:51 +02:00 - Inicio lote MW-THEME-LIBRARY-CLEANUP-009B

## Aprobacion

`VERIFICADO Y CORRECTO`

- Aprobacion exacta recibida:
  `APROBADO LOTE MW-THEME-LIBRARY-CLEANUP-009B`.
- Alcance autorizado: respaldar y eliminar solo el tema `142344224995`.

## Preflight

`VERIFICADO Y CORRECTO`

- Biblioteca: 20 temas.
- MAIN: `178396463480`.
- Tema objetivo: `142344224995`, `Copy of Production`, rol `UNPUBLISHED`.
- Procesamiento: finalizado sin fallo.
- Archivos: 289; paginacion completa; 0 errores de lectura.
- Manifiesto local creado:
  `manifiesto-preborrado-theme-142344224995-2026-06-18.csv`.

## Respaldo

`INCOMPLETO`

- Carpeta preparada:
  `backups/MW-THEME-LIBRARY-CLEANUP-009B-2026-06-18`.
- Falta descargar el ZIP real del tema desde Shopify y verificarlo.
- No se eliminara el tema hasta completar esta condicion.

## Estado actual

`INCOMPLETO`

- No se ha eliminado ningun tema.
- MAIN y tema de reversion no se han modificado.

## Respaldo verificado antes del borrado

`VERIFICADO Y CORRECTO`

- ZIP:
  `theme_export__www-matchwalls-com-copy-of-production__18JUN2026-0801pm.zip`.
- Tamano: `2890489` bytes.
- SHA-256:
  `98ED8E69178BAC7A915DA228B4F56499ECF3DC1543B7671569465CD089B3DE74`.
- Entradas: 289.
- Comparacion con manifiesto: 0 ausentes, 0 extras, 0 checksums distintos.
- Copia archivada en
  `backups/MW-THEME-LIBRARY-CLEANUP-009B-2026-06-18`.
- El tema objetivo queda habilitado para eliminacion manual dentro del lote
  aprobado; ningun otro tema esta autorizado.

---

# 2026-06-18 20:15:37 +02:00 - Cierre lote MW-THEME-LIBRARY-CLEANUP-009B

## Operacion ejecutada

`CORREGIDO Y VERIFICADO`

- Daniel confirmÃƒÆ’Ã‚Â³ la eliminaciÃƒÆ’Ã‚Â³n manual del tema autorizado.
- Consulta Shopify posterior: 19 temas; paginaciÃƒÆ’Ã‚Â³n completa.
- `gid://shopify/OnlineStoreTheme/142344224995` devuelve `null`.
- No se eliminÃƒÆ’Ã‚Â³ ningÃƒÆ’Ã‚Âºn otro tema dentro del lote.

## Produccion y reversion

`VERIFICADO Y CORRECTO`

- MAIN `178396463480`: rol `MAIN`, prefijo `/t/45`, procesamiento finalizado
  sin fallo.
- ReversiÃƒÆ’Ã‚Â³n `178383749496`: rol `UNPUBLISHED`, prefijo `/t/43`, procesamiento
  finalizado sin fallo.

## QA publico posterior

`VERIFICADO Y CORRECTO`

- Home, producto, colecciÃƒÆ’Ã‚Â³n y carrito comprobados en escritorio y mÃƒÆ’Ã‚Â³vil.
- 8/8 cargas sirven recursos de `/t/45`, tienen contenido y no presentan 404.
- La portada mÃƒÆ’Ã‚Â³vil necesitÃƒÆ’Ã‚Â³ repeticiÃƒÆ’Ã‚Â³n por carga transitoria; la repeticiÃƒÆ’Ã‚Â³n fue
  correcta, con H1 y sin overflow.

## Incidencias fuera del alcance

`VERIFICADO PERO MEJORABLE`

- El producto representativo mostrÃƒÆ’Ã‚Â³ overflow mÃƒÆ’Ã‚Â³vil `427/375`; se incorpora al
  diagnÃƒÆ’Ã‚Â³stico de deuda tÃƒÆ’Ã‚Â©cnica.
- El carrito no mostrÃƒÆ’Ã‚Â³ H1 en el smoke test; no se alterÃƒÆ’Ã‚Â³ el MAIN y se revisarÃƒÆ’Ã‚Â¡
  por separado.

## Evidencia y reversion

- `qa-post-eliminacion-MW-THEME-LIBRARY-CLEANUP-009B-2026-06-18.md`.
- ZIP verificado y archivado en
  `backups/MW-THEME-LIBRARY-CLEANUP-009B-2026-06-18/`.
- ReversiÃƒÆ’Ã‚Â³n: importar el ZIP como tema nuevo `UNPUBLISHED` y contrastar 289
  archivos; Shopify asignarÃƒÆ’Ã‚Â¡ un ID nuevo.

---

# 2026-06-18 20:15:37 +02:00 - Diagnostico MW-TECH-JS-ADD-EVENT-LISTENER-010A

## Estado

`REQUIERE DECISION HUMANA`

## Resultado de solo lectura

- Error global reproducido en el MAIN `/t/45`.
- Origen: `snippets/srolling_bar_menu.liquid`.
- MD5 remoto y local: `c254cf711a7706dc21ece2f2ad31acea`.
- El snippet se renderiza globalmente desde `sections/header.liquid`.
- Los elementos `external-width` y `external-height` no existen en la mayorÃƒÆ’Ã‚Â­a
  de pÃƒÆ’Ã‚Â¡ginas, pero el cÃƒÆ’Ã‚Â³digo invoca sus listeners sin comprobarlos.
- No se modificÃƒÆ’Ã‚Â³ Shopify.

---

# 2026-06-19 08:01:02 +02:00 - EjecuciÃƒÆ’Ã‚Â³n y QA parcial 010A5

`INCOMPLETO`

- AprobaciÃƒÆ’Ã‚Â³n exacta recibida y aplicada solo al auxiliar `178399019384`.
- `assets/customizer.js`: MD5 `6684ed205824c8ba660bd4c67a5e26fc`,
  40832 bytes, guard 1 y cero `userErrors`.
- MAIN y reversiÃƒÆ’Ã‚Â³n no modificados.
- ComparaciÃƒÆ’Ã‚Â³n funcional con MAIN: 400ÃƒÆ’Ã¢â‚¬â€300 cm, cantidad 12 y precio 402 ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬.
- QA especÃƒÆ’Ã‚Â­fica: 20/20, ES/EN/FR/DE/NL, escritorio/mÃƒÆ’Ã‚Â³vil.
- Matriz mÃƒÆ’Ã‚Â³vil: 85/85.
- Matriz escritorio: 11/15 cargas completas; cuatro quedaron incompletas por
  reinicio del navegador de pruebas. No se infiere su resultado.
- Pendiente completar 74 verificaciones de escritorio vÃƒÆ’Ã‚Â¡lidas.
- Tema auxiliar sigue sin publicar.

---

# 2026-06-19 08:11:57 +02:00 - Cierre 010A5

`CORREGIDO Y VERIFICADO`

- Se completaron las 74 verificaciones de escritorio pendientes: 74/74.
- Matriz final: mÃƒÆ’Ã‚Â³vil 85/85 y escritorio 85/85; total 170/170.
- QA especÃƒÆ’Ã‚Â­fica: 20/20.
- Medidas, cantidad y precio equivalentes a MAIN: 400ÃƒÆ’Ã¢â‚¬â€300 cm, 12 y 402 ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬.
- Errores nuevos `convertToInches` o `addEventListener`: 0.
- Lectura final Shopify: auxiliar `178399019384` `UNPUBLISHED`, MD5
  `6684ed205824c8ba660bd4c67a5e26fc`, 40832 bytes, cero `userErrors`.
- MAIN no modificado. No se publicÃƒÆ’Ã‚Â³ ningÃƒÆ’Ã‚Âºn tema.

## Propuesta

- Duplicar MAIN como tema auxiliar `UNPUBLISHED`.
- AÃƒÆ’Ã‚Â±adir guardas independientes a ambos listeners en un solo archivo.
- Ejecutar las 170 pruebas y validar el evento de `dataLayer`.
- No publicar dentro de 010A.

## Evidencias

- `diagnostico-MW-TECH-JS-ADD-EVENT-LISTENER-010A-2026-06-18.md`.
- `propuesta-lote-MW-TECH-JS-ADD-EVENT-LISTENER-010A-2026-06-18.md`.

## Aprobacion pendiente

`APROBADO LOTE MW-TECH-JS-ADD-EVENT-LISTENER-010A`

---

# 2026-06-18 20:53:52 +02:00 - Ejecucion MW-TECH-JS-ADD-EVENT-LISTENER-010A

## Aprobacion y preflight

`VERIFICADO Y CORRECTO`

- AprobaciÃƒÆ’Ã‚Â³n exacta recibida.
- Preflight: 19 temas; MAIN `178396463480`; reversiÃƒÆ’Ã‚Â³n `178383749496`.
- Archivo original: `snippets/srolling_bar_menu.liquid`, 8.581 bytes, MD5
  `c254cf711a7706dc21ece2f2ad31acea`.

## Operaciones ejecutadas

- Duplicado creado: `178399019384`, `/t/46`, `UNPUBLISHED`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- Modificado ÃƒÆ’Ã‚Âºnicamente `snippets/srolling_bar_menu.liquid` en el auxiliar.
- MD5 auxiliar: `7d6dfb8df5e4b9ef813eca32aaebc237`.
- MAIN sin cambios y con su checksum original.

## Integridad del duplicado

`VERIFICADO PERO MEJORABLE`

- MAIN 306 archivos; auxiliar 299.
- Faltan siete salidas generadas con sus fuentes `.liquid` presentes.
- La vista previa `/t/46` genera y sirve los recursos; no se observaron errores
  de carga. Entre archivos comunes solo difiere el snippet autorizado.

## QA

`VERIFICADO Y CORRECTO`

- Escritorio 85/85 y mÃƒÆ’Ã‚Â³vil 85/85 pruebas crÃƒÆ’Ã‚Â­ticas correctas.
- 170/170: `/t/46`, H1, canonical, cinco hreflang, `html lang`, indexabilidad,
  contenido y ausencia de 404.
- Error `addEventListener`: 0/170.
- Primera pasada: propagaciÃƒÆ’Ã‚Â³n tardÃƒÆ’Ã‚Â­a en 70 H1; repeticiÃƒÆ’Ã‚Â³n 70/70 correcta.

## Incidencias independientes

`VERIFICADO PERO MEJORABLE`

- Overflow mÃƒÆ’Ã‚Â³vil: FR 17, NL 16, resto 0.
- `SyntaxError: Unexpected token ','` permanece.

## Tracking de medidas y estado final

`REQUIERE DECISION HUMANA`

- Auxiliar: 0 eventos `input_mural_outside` al cambiar ancho/alto.
- MAIN original: tambiÃƒÆ’Ã‚Â©n 0 eventos y reproduce la excepciÃƒÆ’Ã‚Â³n original.
- Causa: campos insertados despuÃƒÆ’Ã‚Â©s de `DOMContentLoaded`; no es regresiÃƒÆ’Ã‚Â³n de
  010A, pero el criterio funcional no se cumple.
- Auxiliar permanece `UNPUBLISHED`; no se publicÃƒÆ’Ã‚Â³ ni se modificÃƒÆ’Ã‚Â³ el MAIN.
- Siguiente propuesta: `MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2`.

## Evidencia

- `qa-MW-TECH-JS-ADD-EVENT-LISTENER-010A-2026-06-18.md`.
- `propuesta-lote-MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2-2026-06-18.md`.

---

# 2026-06-18 21:06:50 +02:00 - Ejecucion y reversion MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2

## Aprobacion y preflight

`VERIFICADO Y CORRECTO`

- AprobaciÃƒÆ’Ã‚Â³n exacta recibida.
- Auxiliar `178399019384`, `/t/46`, `UNPUBLISHED`.
- Checksum previo `7d6dfb8df5e4b9ef813eca32aaebc237`.
- MAIN y reversiÃƒÆ’Ã‚Â³n intactos.

## Operacion

- Listener delegado almacenado ÃƒÆ’Ã‚Âºnicamente en
  `snippets/srolling_bar_menu.liquid`.
- Checksum experimental `fc76e23f024cbda9ba30f40aec5c2c1e`.
- Contenido almacenado y renderizado verificados.

## Prueba critica

`INCORRECTO`

- Ancho `401`: 0 eventos `input_mural_outside`.
- Alto `301`: 0 eventos `input_mural_outside`.
- Entrada por teclado: 0 eventos.
- El campo interno sÃƒÆ’Ã‚Â­ recibiÃƒÆ’Ã‚Â³ el valor externo, por lo que la entrada fue real.

## Reversion

`CORREGIDO Y VERIFICADO`

- Restaurado el contenido previo de 010A.
- Checksum final `7d6dfb8df5e4b9ef813eca32aaebc237`.
- Auxiliar `UNPUBLISHED`; MAIN sin cambios.
- No se ejecutaron las 170 pruebas al fallar la prueba crÃƒÆ’Ã‚Â­tica inicial.

## Nuevo hallazgo

`INCORRECTO`

- Producto estÃƒÆ’Ã‚Â¡ndar: `#customImage` inexistente.
- `snippets/product-customizer.liquid` llama
  `fileInput.addEventListener` sin guarda.
- MD5 `3878a24a9bb6cb134247ac6aff707a58`.
- Propuesta siguiente: `MW-TECH-PRODUCT-FILEINPUT-GUARD-010A3`.

## Evidencias

- `qa-MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2-2026-06-18.md`.
- `propuesta-lote-MW-TECH-PRODUCT-FILEINPUT-GUARD-010A3-2026-06-18.md`.

---

# 2026-06-18 21:34:46 +02:00 - Inicio MW-TECH-PRODUCT-FILEINPUT-GUARD-010A3

## Aprobacion y preflight

`VERIFICADO Y CORRECTO`

- AprobaciÃƒÆ’Ã‚Â³n exacta recibida:
  `APROBADO LOTE MW-TECH-PRODUCT-FILEINPUT-GUARD-010A3`.
- Auxiliar `178399019384`, `/t/46`, `UNPUBLISHED`.
- `snippets/product-customizer.liquid`:
  `3878a24a9bb6cb134247ac6aff707a58`.
- Una ÃƒÆ’Ã‚Âºnica llamada directa objetivo; candidato cambia un solo carÃƒÆ’Ã‚Â¡cter.
- MAIN y reversiÃƒÆ’Ã‚Â³n intactos.

## Intentos de ejecucion

`INCOMPLETO`

- El conector Shopify bloqueÃƒÆ’Ã‚Â³ dos escrituras del archivo de 49 KB.
- Ambas operaciones se cancelaron tras confirmar por lectura que el archivo no
  habÃƒÆ’Ã‚Â­a cambiado.
- Lectura final: checksum original, llamada directa presente y tema sin fallo.
- Shopify CLI no estÃƒÆ’Ã‚Â¡ instalado; no se instalÃƒÆ’Ã‚Â³ software.
- El editor Admin no fue controlable desde el navegador integrado.

## Estado actual

- Shopify no ha sido modificado por 010A3.
- Pendiente ediciÃƒÆ’Ã‚Â³n manual de un carÃƒÆ’Ã‚Â¡cter en el auxiliar aprobado.
- No se ha publicado el tema y no se ha modificado el MAIN.

## 2026-06-18 21:37:45 +02:00 - Verificacion tras edicion manual 010A3

`INCOMPLETO`

- Daniel indicÃƒÆ’Ã‚Â³ `GUARDADO 010A3`.
- Dos lecturas separadas confirmaron que el tema objetivo `178399019384`
  conserva el checksum `3878a24a9bb6cb134247ac6aff707a58`.
- La llamada directa permanece y no existe la llamada opcional propuesta.
- No se iniciÃƒÆ’Ã‚Â³ QA porque Shopify no almacenÃƒÆ’Ã‚Â³ el cambio.
- MAIN y reversiÃƒÆ’Ã‚Â³n permanecen intactos; no se publicÃƒÆ’Ã‚Â³ ningÃƒÆ’Ã‚Âºn tema.

## 2026-06-18 21:42:23 +02:00 - Segunda verificacion manual 010A3

`INCOMPLETO`

- Daniel indicÃƒÆ’Ã‚Â³ `GUARDADO 010A3 EN 178399019384`.
- El tema objetivo mantiene checksum
  `3878a24a9bb6cb134247ac6aff707a58`, llamada directa 1 y opcional 0.
- Se auditaron los 20 temas para descartar que el cambio se hubiese guardado
  accidentalmente en otro; ninguno contiene la llamada opcional propuesta.
- No se iniciÃƒÆ’Ã‚Â³ QA y no se publicÃƒÆ’Ã‚Â³ ningÃƒÆ’Ã‚Âºn tema.

---

# 2026-06-18 22:26:25 +02:00 - Verificacion y QA MW-TECH-PRODUCT-FILEINPUT-GUARD-010A3

## Cambio almacenado

`VERIFICADO Y CORRECTO`

- Tema `178399019384`, `/t/46`, `UNPUBLISHED`.
- MD5 `8f8a7d213f04ace77c4003647053f763`.
- Diferencia exacta: un `?`; tamaÃƒÆ’Ã‚Â±o +1 byte.
- Llamada directa 0; llamada opcional 1.
- MAIN y reversiÃƒÆ’Ã‚Â³n intactos.

## QA especifica

`VERIFICADO PERO MEJORABLE`

- 20 cargas: producto estÃƒÆ’Ã‚Â¡ndar y cargador ÃƒÆ’Ã¢â‚¬â€ cinco idiomas ÃƒÆ’Ã¢â‚¬â€ desktop/mÃƒÆ’Ã‚Â³vil.
- `/t/46`, contenido y ausencia de 404: 20/20.
- Producto estÃƒÆ’Ã‚Â¡ndar: error `addEventListener` 0/10.
- Cargador: error `addEventListener` 10/10.
- Seis cargas incompletas no se repitieron al persistir el fallo crÃƒÆ’Ã‚Â­tico.
- No se ejecutÃƒÆ’Ã‚Â³ la matriz de 170.

## Siguiente origen

`INCORRECTO`

- `button[open-modal]` no existe en el cargador.
- `openModalButton.addEventListener` se ejecuta sin guarda.
- Archivo: `snippets/product-customizer.liquid`, lÃƒÆ’Ã‚Â­nea local 605.
- Propuesta: `MW-TECH-UPLOADER-OPENMODAL-GUARD-010A4`.

## Evidencias

- `qa-MW-TECH-PRODUCT-FILEINPUT-GUARD-010A3-2026-06-18.md`.
- `propuesta-lote-MW-TECH-UPLOADER-OPENMODAL-GUARD-010A4-2026-06-18.md`.

---

# 2026-06-18 22:34:48 +02:00 - Inicio MW-TECH-UPLOADER-OPENMODAL-GUARD-010A4

## Aprobacion y preflight

`VERIFICADO Y CORRECTO`

- AprobaciÃƒÆ’Ã‚Â³n exacta recibida.
- Auxiliar `178399019384`, `/t/46`, `UNPUBLISHED`.
- MD5 actual `8f8a7d213f04ace77c4003647053f763`.
- `fileInput?.addEventListener` presente 1 vez.
- `openModalButton.addEventListener` directo presente 1 vez; opcional 0.
- MAIN y reversiÃƒÆ’Ã‚Â³n intactos.

## Estado

`INCOMPLETO`

- Pendiente ediciÃƒÆ’Ã‚Â³n manual de un ÃƒÆ’Ã‚Âºnico carÃƒÆ’Ã‚Â¡cter en el archivo ya abierto por
  Daniel. No se ha publicado ni se ha modificado el MAIN.

---

# 2026-06-18 23:01:11 +02:00 - VerificaciÃƒÆ’Ã‚Â³n tras ediciÃƒÆ’Ã‚Â³n manual 010A4

## Cambio almacenado

`VERIFICADO Y CORRECTO`

- Daniel indicÃƒÆ’Ã‚Â³ `GUARDADO Y CONFIRMADO 010A4` y aportÃƒÆ’Ã‚Â³ captura del cambio.
- Tema `178399019384`, `/t/46`, `UNPUBLISHED`.
- Archivo `snippets/product-customizer.liquid`.
- Checksum Shopify `d5a74ccb15b645eeb79e8c52f7c5a4ac`; tamaÃƒÆ’Ã‚Â±o `49230`.
- El checksum y tamaÃƒÆ’Ã‚Â±o coinciden exactamente con el candidato local calculado.
- Resultado acumulado: `fileInput?.addEventListener` 1,
  `openModalButton?.addEventListener` 1 y llamada directa objetivo 0.
- MAIN `178396463480` y reversiÃƒÆ’Ã‚Â³n `178383749496` conservan checksum
  `3878a24a9bb6cb134247ac6aff707a58` y tamaÃƒÆ’Ã‚Â±o `49228`.
- Los 20 temas siguen presentes; no se publicÃƒÆ’Ã‚Â³, duplicÃƒÆ’Ã‚Â³, renombrÃƒÆ’Ã‚Â³ ni eliminÃƒÆ’Ã‚Â³
  ningÃƒÆ’Ã‚Âºn tema.

## QA dinÃƒÆ’Ã‚Â¡mica

`INCOMPLETO`

- Producto estÃƒÆ’Ã‚Â¡ndar ES de escritorio cargado desde recursos `/t/46`.
- H1 1, contenido 14991 caracteres, `#customImage` 0 y ausencia de 404.
- Error `addEventListener`: 0.
- Error independiente `convertToInches`: 1; fuera del alcance de 010A4.
- La polÃƒÆ’Ã‚Â­tica del navegador rechazÃƒÆ’Ã‚Â³ continuar las siguientes navegaciones.
- Pruebas especÃƒÆ’Ã‚Â­ficas completadas: 1/20; matriz completa: 0/170.
- No se infiere el resultado de las pruebas no ejecutadas.

## Estado final del lote

`INCOMPLETO`

- El cambio de cÃƒÆ’Ã‚Â³digo estÃƒÆ’Ã‚Â¡ verificado, pero falta la QA dinÃƒÆ’Ã‚Â¡mica obligatoria.
- Tema auxiliar permanece `UNPUBLISHED`; MAIN no modificado.
- ReversiÃƒÆ’Ã‚Â³n exacta: retirar el segundo `?` y recuperar checksum
  `8f8a7d213f04ace77c4003647053f763`.
- Evidencia: `qa-MW-TECH-UPLOADER-OPENMODAL-GUARD-010A4-2026-06-18.md`.

# 2026-06-18 23:37:20 +02:00 - Cierre MW-TECH-UPLOADER-OPENMODAL-GUARD-010A4

## QA especÃƒÆ’Ã‚Â­fica completada

`CORREGIDO Y VERIFICADO`

- Producto estÃƒÆ’Ã‚Â¡ndar y cargador en ES/EN/FR/DE/NL, escritorio y mÃƒÆ’Ã‚Â³vil: 20/20.
- Tema `/t/46`, H1 ÃƒÆ’Ã‚Âºnico, contenido y ausencia de 404: 20/20.
- `#customImage`: 0/10 estÃƒÆ’Ã‚Â¡ndar y 10/10 cargador, comportamiento esperado.
- Error `addEventListener`: 0/20.
- Error `convertToInches`: 20/20; deuda independiente.

## Matriz completa

`CORREGIDO Y VERIFICADO`

- 85 URLs por escritorio y mÃƒÆ’Ã‚Â³vil: 170/170.
- H1 exacto y ÃƒÆ’Ã‚Âºnico, canonical propio, cinco hreflang, idioma HTML, ausencia
  de `noindex`, contenido, ausencia de 404 y recursos `/t/46`: correctos.
- Error `addEventListener`: 0.
- Fallos crÃƒÆ’Ã‚Â­ticos: 0.

## Deudas separadas

`VERIFICADO PERO MEJORABLE`

- Desbordamiento mÃƒÆ’Ã‚Â³vil: 34/85, distribuido en 17 FR y 17 NL.
- El histÃƒÆ’Ã‚Â³rico inmediato era 33/85; se analizarÃƒÆ’Ã‚Â¡ la diferencia dentro del
  sublote especÃƒÆ’Ã‚Â­fico de overflow.
- `convertToInches` permanece fuera de 010A4.

## Estado final

`CORREGIDO Y VERIFICADO`

- Tema auxiliar `178399019384` continÃƒÆ’Ã‚Âºa sin publicar.
- MAIN no fue modificado.
- ReversiÃƒÆ’Ã‚Â³n: retirar el segundo `?` y recuperar MD5
  `8f8a7d213f04ace77c4003647053f763`.
- Evidencia: `qa-MW-TECH-UPLOADER-OPENMODAL-GUARD-010A4-2026-06-18.md`.

---

# 2026-06-18 23:47:36 +02:00 - DecisiÃƒÆ’Ã‚Â³n de alcance de buscadores e IA

`REQUIERE DECISION HUMANA` resuelto por Daniel.

- Yandex pasa a `STANDBY` y queda fuera del alcance activo.
- Superficies prioritarias: Google, Edge, Bing, Yahoo y Comet.
- Sistemas IA prioritarios: Copilot, Perplexity, Gemini, Claude, Grok y
  ChatGPT.
- La mediciÃƒÆ’Ã‚Â³n agrupa las dependencias operativas cuando proceda, pero conserva
  resultados separados por superficie.
- No se modificÃƒÆ’Ã‚Â³ Shopify ni ninguna plataforma externa.

---

# 2026-06-18 23:54:38 +02:00 - DiagnÃƒÆ’Ã‚Â³stico 010A5

`VERIFICADO Y CORRECTO`

- `assets/customizer.js` coincide en auxiliar, MAIN y reversiÃƒÆ’Ã‚Â³n: MD5
  `2a26be9d6af37a992526274df431deaa`.
- Llamada `convertToInches()` presente; mÃƒÆ’Ã‚Â©todo inexistente.
- Ocho versiones histÃƒÆ’Ã‚Â³ricas confirman el defecto y no aportan implementaciÃƒÆ’Ã‚Â³n.
- Eliminar solo la llamada serÃƒÆ’Ã‚Â­a inseguro por `unitConverter()` y los campos
  imperiales a cero.
- Candidato con guard validado sintÃƒÆ’Ã‚Â¡cticamente; MD5
  `6684ed205824c8ba660bd4c67a5e26fc`.
- Propuesta: `propuesta-lote-MW-TECH-CUSTOMIZER-CONVERT-INCHES-010A5-2026-06-18.md`.
- No se modificÃƒÆ’Ã‚Â³ Shopify.
# 2026-06-19 - DiagnÃƒÆ’Ã‚Â³stico MW-TECH-NL-SYNTAX-010B

`VERIFICADO Y CORRECTO`

- Tema auxiliar `178399019384`, `/t/46`, `UNPUBLISHED`.
- Shopify confirma `snippets/ultimate-datalayer.liquid` con MD5
  `449db7505f61b2f81c835cc32669c37c` y 57168 bytes.
- MAIN `178396463480` y reversiÃƒÆ’Ã‚Â³n `178383749496` conservan exactamente el mismo
  archivo; no fueron modificados.
- `SyntaxError: Unexpected token ','` reproducido en ES, EN, FR, DE y NL en
  las cinco pÃƒÆ’Ã‚Â¡ginas localizadas Ãƒâ€šÃ‚Â«Nuestros productosÃƒâ€šÃ‚Â».
- JavaScript invÃƒÆ’Ã‚Â¡lido localizado: `variant_id: ,`.
- Causa: tres usos de `template contains 'product'` tratan
  `page.nuestros-productos` como una ficha de producto.
- Candidato: dos condiciones
  `request.page_type == 'product'` y una condiciÃƒÆ’Ã‚Â³n inversa equivalente.
- MD5 candidato `792a7f2c37022db342e1d7a82a8d3679`; 57177 bytes.
- Propuesta formal:
  `propuesta-lote-MW-TECH-NL-SYNTAX-010B-2026-06-19.md`.
- No se modificÃƒÆ’Ã‚Â³ Shopify. Pendiente aprobaciÃƒÆ’Ã‚Â³n exacta.

## Estado

`INCOMPLETO`

- PrÃƒÆ’Ã‚Â³ximo paso: recibir
  `APROBADO LOTE MW-TECH-NL-SYNTAX-010B`, ejecutar solo en el auxiliar y
  completar 20 pruebas especÃƒÆ’Ã‚Â­ficas mÃƒÆ’Ã‚Â¡s 170 de regresiÃƒÆ’Ã‚Â³n.

---

# 2026-06-20 11:29:21 +02:00 - Cierre MW-TECH-NL-SYNTAX-010B

## AprobaciÃƒÆ’Ã‚Â³n y ejecuciÃƒÆ’Ã‚Â³n

`CORREGIDO Y VERIFICADO`

- AprobaciÃƒÆ’Ã‚Â³n exacta recibida dos veces; se ejecutÃƒÆ’Ã‚Â³ una sola mutaciÃƒÆ’Ã‚Â³n.
- Tema auxiliar `178399019384`, `/t/46`, `UNPUBLISHED`.
- Archivo `snippets/ultimate-datalayer.liquid`.
- MD5 anterior `449db7505f61b2f81c835cc32669c37c`; 57168 bytes.
- Se sustituyeron exactamente dos condiciones `if` y una `unless` por
  comprobaciones estrictas de `request.page_type`.
- Shopify devolviÃƒÆ’Ã‚Â³ cero `userErrors`.
- Lectura final: MD5 `792a7f2c37022db342e1d7a82a8d3679`; 57177 bytes;
  tres condiciones estrictas y cero coincidencias amplias.
- MAIN `178396463480` y reversiÃƒÆ’Ã‚Â³n `178383749496` permanecen intactos con el MD5
  original.

## VerificaciÃƒÆ’Ã‚Â³n

`CORREGIDO Y VERIFICADO`

- QA especÃƒÆ’Ã‚Â­fica ES/EN/FR/DE/NL, escritorio y mÃƒÆ’Ã‚Â³vil: 20/20.
- RegresiÃƒÆ’Ã‚Â³n: escritorio 85/85 y mÃƒÆ’Ã‚Â³vil 85/85; total 170/170.
- `SyntaxError: Unexpected token ','`: 0.
- `variant_id: ,`: 0; productos con variante numÃƒÆ’Ã‚Â©rica.
- Errores crÃƒÆ’Ã‚Â­ticos nuevos: 0.

## Deudas no atribuibles a 010B

- Tracking `view_item`: `INCORRECTO`; ausente tanto en auxiliar como en MAIN,
  sin diferencia causada por 010B.
- Overflow mÃƒÆ’Ã‚Â³vil: `VERIFICADO PERO MEJORABLE`; 34/85, 17 FR y 17 NL, igual que
  la lÃƒÆ’Ã‚Â­nea base.
- Validador Liquid empaquetado: `NO ACCESIBLE` por dependencia ausente; no se
  declarÃƒÆ’Ã‚Â³ como superado.

## ReversiÃƒÆ’Ã‚Â³n y evidencia

- Restaurar las tres condiciones originales y comprobar MD5
  `449db7505f61b2f81c835cc32669c37c`, o descartar el auxiliar.
- Evidencia: `qa-MW-TECH-NL-SYNTAX-010B-2026-06-20.md`.
- El tema no fue publicado.

---

# 2026-06-20 - DiagnÃƒÆ’Ã‚Â³stico MW-TECH-MOBILE-OVERFLOW-FR-NL-010C

`VERIFICADO Y CORRECTO`

- Tema auxiliar `178399019384`, `/t/46`, `UNPUBLISHED`.
- `assets/theme.css` coincide en auxiliar, MAIN, reversiÃƒÆ’Ã‚Â³n y copia local: MD5
  `89f4729809a0eaac75a764e0fc41888e`; 241968 bytes.
- Overflow reproducido en 34/34 URLs FR/NL a viewport 390 px y en muestras a
  375 px; controles ES/EN/DE sin overflow.
- Causa global: 96 px de margen derecho aplicado tambiÃƒÆ’Ã‚Â©n al ÃƒÆ’Ã‚Âºltimo enlace legal
  del footer.
- Causa adicional NL `/nl/pages/onze-producten`: palabra
  `Aanpassingsdiensten` de 385 px dentro de un grid de 335 px.
- Candidato de un solo archivo: media query mÃƒÆ’Ã‚Â³vil de 270 bytes.
- MD5 candidato `0ff4bc0320305ef6cda965b1557b6e5f`; 242238 bytes.
- Theme Check: `NO ACCESIBLE` por dependencia empaquetada ausente; no se
  declarÃƒÆ’Ã‚Â³ como superado.
- Propuesta:
  `propuesta-lote-MW-TECH-MOBILE-OVERFLOW-FR-NL-010C-2026-06-20.md`.
- No se modificÃƒÆ’Ã‚Â³ Shopify.

## Estado

`INCOMPLETO`

- Pendiente aprobaciÃƒÆ’Ã‚Â³n exacta, ejecuciÃƒÆ’Ã‚Â³n en auxiliar y 204 renders de QA.

---

---

# 2026-06-25 - EjecuciÃƒÆ’Ã‚Â³n y reversiÃƒÆ’Ã‚Â³n MW-TECH-MOBILE-OVERFLOW-FR-NL-010C

## AprobaciÃƒÆ’Ã‚Â³n y alcance

`APROBADO LOTE MW-TECH-MOBILE-OVERFLOW-FR-NL-010C` recibido.

- Tema auxiliar `178399019384`, `/t/46`, no publicado.
- Archivo objetivo: `assets/theme.css`.
- MAIN no fue publicado ni modificado.
- Exclusiones respetadas: URLs, handles, textos, contenidos comerciales, apps externas y tema MAIN.

## Cambio ejecutado

`VERIFICADO Y CORRECTO` como ejecuciÃƒÆ’Ã‚Â³n almacenada inicial.

- Se aÃƒÆ’Ã‚Â±adiÃƒÆ’Ã‚Â³ el bloque CSS aprobado en el editor de cÃƒÆ’Ã‚Â³digo de Shopify.
- Preview confirmÃƒÆ’Ã‚Â³ recursos `/t/46`.
- El ÃƒÆ’Ã‚Âºltimo enlace legal pasÃƒÆ’Ã‚Â³ a `margin-right: 0px` con el candidato activo.

## QA centinela

`INCORRECTO`

- FR `https://www.matchwalls.com/fr/pages/tout-sur-nos-peintures-murales` a viewport 390:
  - `clientWidth 375`, `scrollWidth 408`, overflow `+33 px`.
  - H1 exacto, canonical propio, hreflang prioritarios, `html lang="fr"`, sin `noindex`.
  - Errores crÃƒÆ’Ã‚Â­ticos de consola: 0.
- NL `https://www.matchwalls.com/nl/pages/onze-producten` a viewport 390:
  - `clientWidth 375`, `scrollWidth 381`, overflow `+6 px`.
  - H1 exacto, canonical propio, hreflang prioritarios, `html lang="nl"`, sin `noindex`.
  - Errores crÃƒÆ’Ã‚Â­ticos de consola: 0.
- Control ES:
  - `clientWidth 375`, `scrollWidth 375`, overflow `0 px`.

## DiagnÃƒÆ’Ã‚Â³stico posterior

`INCORRECTO`

- La regla aprobada solo retiraba el margen del ÃƒÆ’Ã‚Âºltimo enlace legal.
- Los tres primeros `.custom-legal__item` mantenÃƒÆ’Ã‚Â­an `margin-right: 96px`.
- FR: `.custom-legal__list` `clientWidth 335`, `scrollWidth 388`.
- NL: `.custom-legal__list` `clientWidth 335`, `scrollWidth 362`.
- El candidato era insuficiente para cumplir `scrollWidth == clientWidth`.

## ReversiÃƒÆ’Ã‚Â³n

`VERIFICADO Y CORRECTO`

- Se eliminÃƒÆ’Ã‚Â³ el bloque 010C del editor de cÃƒÆ’Ã‚Â³digo.
- Antes de guardar: reglas 010C ausentes, `.facade-wrapper` presente y editor `No Problems`.
- Tras guardar, preview `/t/46` confirmÃƒÆ’Ã‚Â³ vuelta a lÃƒÆ’Ã‚Â­nea base:
  - FR: ÃƒÆ’Ã‚Âºltimo enlace legal `margin-right: 96px`, overflow `+33 px`.
  - NL `/nl/pages/onze-producten`: ÃƒÆ’Ã‚Âºltimo enlace legal `margin-right: 96px`, overflow `+30 px`.
- Checksum final Shopify: `NO ACCESIBLE` en este turno por ausencia de conector GraphQL/CLI; no se declara MD5 restaurado.
- Evidencia: `qa-MW-TECH-MOBILE-OVERFLOW-FR-NL-010C-2026-06-25.md`.

## Estado final

`INCORRECTO`

- 010C queda ejecutado, fallido en QA centinela y revertido.
- Se requiere lote nuevo: `MW-TECH-MOBILE-OVERFLOW-LEGAL-FLEX-010C2`.


# 2026-06-25 - Cierre MW-TECH-MOBILE-OVERFLOW-LEGAL-FLEX-010C2

## AprobaciÃƒÆ’Ã‚Â³n y alcance

`CORREGIDO Y VERIFICADO`

- AprobaciÃƒÆ’Ã‚Â³n exacta recibida: `APROBADO LOTE MW-TECH-MOBILE-OVERFLOW-LEGAL-FLEX-010C2`.
- Tema auxiliar `178399019384`, `/t/46`, `UNPUBLISHED`.
- Archivo objetivo: `assets/theme.css`.
- MAIN `178396463480` no fue modificado ni publicado.
- Tema de reversiÃƒÆ’Ã‚Â³n `178383749496` no fue modificado.
- Exclusiones respetadas: URLs, handles, textos, traducciones, productos, precios, apps externas, tracking y publicaciÃƒÆ’Ã‚Â³n.

## Cambio ejecutado

`CORREGIDO Y VERIFICADO`

- MD5 auxiliar antes: `05810cc93feb785cc81aed10513a297a`; tamaÃƒÆ’Ã‚Â±o `241969` bytes.
- MD5 auxiliar despuÃƒÆ’Ã‚Â©s: `b86a0e260263eed6a2586a3e7bca8e05`; tamaÃƒÆ’Ã‚Â±o `242427` bytes.
- Se aÃƒÆ’Ã‚Â±adiÃƒÆ’Ã‚Â³ el bloque CSS 010C2 exacto una sola vez.
- `.custom-legal__item:last-child` del candidato fallido 010C sigue ausente.
- MAIN y tema de reversiÃƒÆ’Ã‚Â³n conservan MD5 `89f4729809a0eaac75a764e0fc41888e` y no contienen el bloque 010C2.

## QA

`CORREGIDO Y VERIFICADO`

- Centinela a 390 px:
  - FR mural: `clientWidth 375`, `scrollWidth 375`, overflow `0 px`.
  - NL `/nl/pages/onze-producten`: `clientWidth 375`, `scrollWidth 375`, overflow `0 px`.
  - ES control: `clientWidth 375`, `scrollWidth 375`, overflow `0 px`.
- FR/NL a 390 px: 34/34 correctas; overflow mÃƒÆ’Ã‚Â¡ximo `0 px`.
- FR/NL a 375 px: 34/34 correctas; overflow mÃƒÆ’Ã‚Â¡ximo `0 px`.
- Controles ES/EN/DE a 375 px: 51/51 correctas; overflow mÃƒÆ’Ã‚Â¡ximo `0 px`.
- Matriz mÃƒÆ’Ã‚Â³vil total: 85/85 correctas.
- Matriz desktop 1440 px: 85/85 correctas.
- Total estÃƒÆ’Ã‚Â¡ndar verificado: 170/170.
- H1, canonical, hreflang prioritarios, `html lang`, noindex, contenido, recursos `/t/46` y errores crÃƒÆ’Ã‚Â­ticos de consola: correctos en matriz.

## ReversiÃƒÆ’Ã‚Â³n

`VERIFICADO Y CORRECTO`

- ReversiÃƒÆ’Ã‚Â³n exacta: retirar ÃƒÆ’Ã‚Âºnicamente el bloque 010C2 aÃƒÆ’Ã‚Â±adido en `assets/theme.css`.
- Objetivo de reversiÃƒÆ’Ã‚Â³n del auxiliar: MD5 `05810cc93feb785cc81aed10513a297a`.
- Alternativa extrema: descartar el tema auxiliar `178399019384`.

## Evidencia

- Documento QA: `qa-MW-TECH-MOBILE-OVERFLOW-LEGAL-FLEX-010C2-2026-06-25.md`.
- No se publicÃƒÆ’Ã‚Â³ el tema.

---


# 2026-06-25 - Cierre MW-TECH-HOME-CRAWLABLE-CSS-010D

## Aprobacion y alcance

`CORREGIDO Y VERIFICADO` en tema auxiliar.

- Aprobacion exacta recibida: `APROBADO LOTE MW-TECH-HOME-CRAWLABLE-CSS-010D`.
- Tema auxiliar `178399019384`, `/t/46`, `UNPUBLISHED`.
- Archivo objetivo: `sections/collection-logo-list.liquid`.
- MAIN `178396463480` no fue modificado ni publicado.
- Tema de reversion `178383749496` no fue modificado.
- Exclusiones respetadas: URLs, handles, textos, productos, precios, inventario, schema, redirecciones, apps externas y publicacion.

## Cambio ejecutado

`CORREGIDO Y VERIFICADO`

- MD5 auxiliar antes: `44d02156951a46f0147f3ee3de61f38e`; size `6780`.
- Primer candidato: MD5 `07e2ef27cb963166fa189ac4b8ae0f6b`; descartado por regresion visual de cascada CSS, imagen desktop `190.583px`.
- MD5 auxiliar final: `e246746230f64c88b529db9aa370f3e2`; size `5937`.
- Se elimino el `<style>` repetido dentro de cada `.logo-link`.
- Se movio CSS estructural a `{% stylesheet %}` y se fijaron medidas criticas de imagen con atributo `style` para conservar 120px desktop y 70px mobile sin contaminar `body.textContent`.
- MAIN y tema de reversion conservan MD5 `44d02156951a46f0147f3ee3de61f38e`.

## QA

`CORREGIDO Y VERIFICADO`

- Homes ES/EN/FR/DE/NL en desktop y mobile: 10/10 correctas tras retest EN/FR desktop con barra final.
- En todas las vistas finales:
  - assets `/t/46` confirmados;
  - 8 enlaces `.logo-link` conservados;
  - 8 imagenes `.logo-list__image` conservadas;
  - `styleInsideLogoLinkCount = 0`;
  - `badBodyStyleCount = 0`;
  - CSS `.logo-link/.logo-list__image` ausente de `body.textContent` y `body.innerText`;
  - desktop: imagen `120px x 120px`, circular, `object-fit: cover`;
  - mobile 390px: imagen aprox. `70.2px x 70.2px`, circular, sin overflow;
  - canonical, hreflang, `html lang` y `noindex` correctos en vistas validas.

## Validacion y limitaciones

- Documentacion Shopify consultada para `{% stylesheet %}` e `image_tag`.
- Mutacion `themeFilesUpsert` validada contra schema y ejecutada con `0 userErrors`.
- Validador local Shopify Liquid: `NO ACCESIBLE` por dependencia local ausente `@shopify/theme-check-common`; no se uso para certificar el lote.

## Reversion

`VERIFICADO Y CORRECTO`

- Restaurar `sections/collection-logo-list.liquid` del auxiliar al MD5 `44d02156951a46f0147f3ee3de61f38e`.
- Fuente de reversion intacta: MAIN y tema `178383749496` conservan ese MD5.
- Alternativa extrema: descartar el tema auxiliar `178399019384`.

## Evidencia

- Documento QA: `qa-MW-TECH-HOME-CRAWLABLE-CSS-010D-2026-06-25.md`.
- No se publico el tema.

---



