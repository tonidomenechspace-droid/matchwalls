# MW-INDEXNOW-APP-POSTINSTALL-SETTINGS-LOGS-QA-013I1

Fecha: 2026-07-05  
Modo: solo lectura.  
Estado final: `VERIFICADO PERO MEJORABLE`.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `postinstall-MW-INDEXNOW-APP-PILOT-INSTALL-CONFIG-013I-STORESpark-PREMIUM-2026-07-05.md`
- `preflight-MW-INDEXNOW-APP-PILOT-INSTALL-CONFIG-013I-2026-07-05.md`
- `app-shortlist-MW-INDEXNOW-APP-PILOT-INSTALL-CONFIG-013I-2026-07-05.csv`
- `registro-cambios-ejecutados.md`

## Estado real comprobado

`VERIFICADO Y CORRECTO`

Pantalla actual indicada por Daniel:

- `https://admin.shopify.com/store/matchwalls/apps/indexnow-18/settings`

Título visible:

- `Matchwalls · IndexNow: for Bing and Yandex 💎 · Shopify`

## Settings leídos

`VERIFICADO PERO MEJORABLE`

La app muestra:

- `API Key`
- Estado: `Connected`
- `Submission settings`
- `Control which types of content changes are automatically submitted to IndexNow.`
- Tipos de contenido:
  - Products
  - Collections
  - Pages
  - Blog posts
- `Languages`
- `Enable or disable languages for your submissions.`

La API key apareció en un campo tipo password. No se registra en este documento ni en el registro por seguridad.

## Estado de tipos de contenido

`VERIFICADO Y CORRECTO`

Todos los tipos principales aparecen activos:

- Products: activo
- Collections: activo
- Pages: activo
- Blog posts: activo

Interpretación: la app puede enviar automáticamente cambios de productos, colecciones, páginas y artículos.

## Estado de idiomas

`VERIFICADO PERO MEJORABLE`

Idiomas prioritarios MatchWalls:

- Spanish (default): activo, bloqueado/no editable.
- English: inactivo.
- French: inactivo.
- German: inactivo.
- Dutch: inactivo.

Otros idiomas visibles e inactivos:

- Italian
- European Portuguese
- Norwegian
- Polish
- Chinese (China)
- Danish
- Finnish
- Hindi
- Korean
- Russian
- Arabic
- Swedish
- Hebrew
- Japanese
- Greek
- Hungarian

Interpretación: el piloto está funcionando solo para ES/default. Para la estrategia SEO/GEO prioritaria falta decidir si activar EN, FR, DE y NL en un lote específico.

## Logs de envío observados

`VERIFICADO Y CORRECTO`

En la pantalla Home/postinstall de la app se había observado:

- Last 30 Days Submissions: `1`
- Failed Submissions: `0`
- Failure Rate: `0.0%`
- URL: `www.matchwalls.com`
- Event: `Home updated`
- Submitted at: `05/07/2026, 10:45`
- Status: `Success / Submitted`

No se observó envío masivo.

## Pricing / plan

`DECLARADO PERO NO VERIFICADO`

Daniel confirmó dos veces que solo acepta pago mensual 5 €/mes y no anual/lifetime.

La pantalla de Pricing no pudo verificarse dentro de la app por timeout de navegación. Por tanto:

- plan mensual: `DECLARADO PERO NO VERIFICADO`;
- no anual/no lifetime: `DECLARADO PERO NO VERIFICADO`.

Recomendación: confirmar en Shopify Admin > Configuración > Facturación > apps/cargos que el cargo corresponde a mensual, no anual ni lifetime.

## Riesgos detectados

`VERIFICADO PERO MEJORABLE`

1. Auto-submit activo para Products, Collections, Pages y Blog posts.
2. Solo ES/default está activo; EN, FR, DE y NL están inactivos.
3. La app no muestra en la pantalla leída exclusiones granulares para muestras noindex, IT/PT, URLs de prueba o landings con incidencias.
4. Plan/cargo mensual no verificado dentro de Pricing por timeout.

## Decisión recomendada

`REQUIERE DECISION HUMANA`

No tocar todavía Manual submissions.

Siguiente lote recomendado:

`MW-INDEXNOW-APP-I18N-LANGUAGES-DECISION-013I2`

Objetivo:

- decidir si activar EN, FR, DE y NL en la app;
- dejar IT/PT inactivos salvo autorización expresa;
- decidir si se mantienen activos Products, Collections, Pages y Blog posts;
- antes de activar idiomas, comprobar si la app enviará retroactivamente contenido ya existente o solo cambios futuros.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó ningún ajuste. No se pulsó Save, Discard, Manual submissions, bulk submit, submit all, sync all ni controles de idiomas/tipos de contenido.
