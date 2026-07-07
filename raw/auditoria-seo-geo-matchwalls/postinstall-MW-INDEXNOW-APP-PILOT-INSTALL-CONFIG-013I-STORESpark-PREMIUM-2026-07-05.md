# MW-INDEXNOW-APP-PILOT-INSTALL-CONFIG-013I-STORESpark-PREMIUM — postinstall

Fecha: 2026-07-05  
Aprobación exacta: `APROBADO LOTE MW-INDEXNOW-APP-PILOT-INSTALL-CONFIG-013I-STORESpark-PREMIUM`  
Restricción Daniel: solo plan mensual de 5 €/mes o equivalente mensual. No anual. No lifetime.  
Estado: `VERIFICADO PERO MEJORABLE`.

## Acción ejecutada por Daniel

`DECLARADO PERO NO VERIFICADO` para el pago/aceptación exacta del plan.  
`VERIFICADO Y CORRECTO` para app abierta e instalada/conectada según Shopify Admin visible.

Daniel indicó: `ya esta`.

La URL actual del admin mostraba:

- `https://admin.shopify.com/store/matchwalls/apps/indexnow-18?charge_id=75009851768`

El título de la pestaña confirmaba:

- `Matchwalls · IndexNow: for Bing and Yandex 💎 · Shopify`

## Estado visible de la app

`VERIFICADO Y CORRECTO`

Pantalla de app:

- Mensaje: `Your store is now connected to IndexNow`.
- Mensaje operativo: `Every time a page changes, we will automatically submit your updates to Bing, ChatGPT, Yandex, etc.`
- Last 30 Days Submissions: `1`
- Failed Submissions: `0`
- Failure Rate: `0.0%`

Registro visible:

- URL: `www.matchwalls.com`
- Evento: `Home updated`
- Fecha visible: `05/07/2026, 10:45`
- Estado: `Success / Submitted`

## Interpretación

`VERIFICADO PERO MEJORABLE`

La app quedó activa y ha enviado una única actualización: home canónica. No se observó envío masivo ni fallos en la pantalla visible.

Punto crítico: la app indica auto-submit para cambios de página. Esto puede ser aceptable para un piloto si se limita operativamente a no hacer cambios editoriales masivos mientras se observa el comportamiento. No se ha verificado aún si existe un ajuste granular para desactivar o limitar el auto-submit.

## Configuración / Settings

`NO ACCESIBLE`

Se detectaron rutas internas de la app:

- Home
- Manual submissions
- Pricing
- Settings
- FAQ

La pestaña `Settings` aparecía como ruta interna `/app/settings`, pero no visible/clicable en la vista responsive embebida. Al intentar abrirla por ruta, la navegación tardó demasiado y se detuvo para evitar forzar acciones sobre la app.

Conclusión: queda pendiente revisar manualmente o con nueva sesión la pantalla de Settings antes de hacer más cambios en Shopify.

## Comprobación pública posterior

`VERIFICADO Y CORRECTO`

Comprobación pública tras instalación:

- `https://www.matchwalls.com/indexnow.txt` → HTTP `404`
- `https://www.matchwalls.com/1fe8851103534006a2a9433fe8b56f2d.txt` → HTTP `404`
- `https://www.matchwalls.com/robots.txt` → HTTP `200`
- `https://www.matchwalls.com/sitemap.xml` → HTTP `200`

Conclusión: no apareció key pública nueva bajo las rutas revisadas y robots/sitemap siguen disponibles.

## Riesgos pendientes

`VERIFICADO PERO MEJORABLE`

- Auto-submit activo por defecto para cambios de páginas/contenido.
- Settings no revisado todavía.
- No se ha comprobado si la app permite excluir muestras noindex, URLs IT/PT, filtros, pruebas o landings con incidencias pendientes.
- No se ha comprobado si existen logs exportables.
- No se ha comprobado todavía recepción en Bing Webmaster Tools fuera de la pantalla de la app.

## Acciones prohibidas hasta cerrar postcheck

`VERIFICADO Y CORRECTO`

No realizar cambios masivos en páginas, productos, colecciones, traducciones o tema mientras se observa la app, porque podría enviar URLs automáticamente.

No usar `Manual submissions`, `bulk submit`, `submit all`, `sync all`, `resubmit all` o equivalente hasta aprobación específica.

## Próximo lote recomendado

`MW-INDEXNOW-APP-POSTINSTALL-SETTINGS-LOGS-QA-013I1`

Objetivo:

1. revisar `Settings`;
2. confirmar plan mensual activo;
3. confirmar si hay control de auto-submit;
4. confirmar logs y URL enviada;
5. comprobar en Bing Webmaster Tools si la home aparece recibida o si solo consta en la app;
6. decidir whitelist/manual submissions posterior.
