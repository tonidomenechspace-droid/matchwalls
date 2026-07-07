# MW-INDEXNOW-APP-I18N-LANGUAGES-ACTIVATION-013I3

Fecha: 2026-07-05  
Aprobación: `APROBADO LOTE MW-INDEXNOW-APP-I18N-LANGUAGES-ACTIVATION-013I3`  
Confirmación Daniel: `GUARDADO 013I3`  
Estado final: `CORREGIDO Y VERIFICADO`.

## Objetivo

Activar en la app IndexNow los idiomas prioritarios de la estrategia SEO/GEO/AEO:

- English
- French
- German
- Dutch

Manteniendo:

- Spanish default activo.
- Italian inactivo.
- European Portuguese inactivo.
- resto de idiomas inactivos.

## Ejecución

`CORREGIDO Y VERIFICADO`

Daniel ejecutó manualmente la activación en Shopify Admin > App IndexNow > Settings.

Capturas aportadas por Daniel mostraron:

- Spanish default: activo y bloqueado/no editable.
- Dutch: activo.
- German: activo.
- French: activo.
- English: activo.
- Italian: inactivo.
- European Portuguese: inactivo.
- resto visible: inactivo.

## Verificación post-guardado

`CORREGIDO Y VERIFICADO`

Captura posterior en Home/logs de la app mostró:

- Last 30 Days Submissions: `1`
- Failed Submissions: `0`
- Failure Rate: `0.0%`
- Evento visible: `Home updated`
- URL visible: `www.matchwalls.com`
- Estado visible: `Submitted`

Conclusión: activar EN/FR/DE/NL no disparó envíos retroactivos masivos. El contador siguió en `1`.

## Recursos afectados

`CORREGIDO Y VERIFICADO`

App:

- `IndexNow: for Bing and Yandex`
- Shopify Admin route observada: `https://admin.shopify.com/store/matchwalls/apps/indexnow-18/app`

Configuración afectada:

- Languages.

No se modificaron:

- API Key.
- Products.
- Collections.
- Pages.
- Blog posts.
- Manual submissions.
- Pricing.
- Tema Shopify.
- Liquid.
- Robots.
- Sitemap.
- `llms.txt`.
- URLs.
- Handles.
- Redirecciones.
- Metadatos.
- Traducciones.

## Riesgo residual

`VERIFICADO PERO MEJORABLE`

La app mantiene auto-submit activo para cambios futuros en productos, colecciones, páginas y blog posts. Esto es coherente con la finalidad de IndexNow, pero implica disciplina operativa: evitar cambios masivos no revisados o asumir que esos cambios podrán enviarse automáticamente.

## Próximo lote recomendado

`MW-INDEXNOW-APP-BING-RECEPTION-RECHECK-013I4`

Objetivo:

1. esperar una ventana razonable;
2. revisar logs de app;
3. revisar Bing Webmaster Tools si aparece señal de recepción/IndexNow;
4. decidir si se permite un piloto manual con whitelist pequeña o si se mantiene solo auto-submit por cambios futuros.
