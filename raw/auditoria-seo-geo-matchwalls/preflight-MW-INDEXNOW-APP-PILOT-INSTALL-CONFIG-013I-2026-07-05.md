# MW-INDEXNOW-APP-PILOT-INSTALL-CONFIG-013I — preflight

Fecha: 2026-07-05  
Solicitud recibida: `APROBADO LOTE MW-INDEXNOW-APP-PILOT-INSTALL-CONFIG-013I`  
Estado del lote: `REQUIERE DECISION HUMANA` antes de instalar app.  
Modo ejecutado hasta ahora: solo lectura / sin cambios externos.

Actualización Daniel 2026-07-05: plan mensual únicamente. No anual, no lifetime.

## Motivo de parada segura

`REQUIERE DECISION HUMANA`

La aprobación del nombre del lote está recibida, pero el protocolo del proyecto exige que antes de una escritura externa quede definido y aprobado:

- app exacta;
- coste o plan;
- permisos;
- configuración inicial;
- exclusiones;
- whitelist inicial;
- pruebas posteriores;
- reversión.

Instalar una app en Shopify es una acción externa con permisos y posible coste, por lo que no se debe ejecutar solo con el nombre genérico del lote.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `opciones-MW-INDEXNOW-STABLE-IMPLEMENTATION-OPTIONS-013G-2026-07-05.md`
- `decision-matrix-MW-INDEXNOW-STABLE-IMPLEMENTATION-OPTIONS-013G-2026-07-05.csv`
- `public-state-MW-INDEXNOW-STABLE-IMPLEMENTATION-OPTIONS-013G-2026-07-05.csv`
- `registro-cambios-ejecutados.md`

## Estado real comprobado

`CORREGIDO Y VERIFICADO`

Comprobación pública repetida el 2026-07-05 10:34 +02:00:

- `https://www.matchwalls.com/indexnow.txt` → HTTP `404`
- `https://www.matchwalls.com/1fe8851103534006a2a9433fe8b56f2d.txt` → HTTP `404`

Conclusión: no hay key IndexNow activa bajo `www.matchwalls.com`.

## Fuentes actuales revisadas

`VERIFICADO Y CORRECTO`

- Shopify App Store — `IndexNow: for Bing and Yandex`
  - URL: https://apps.shopify.com/indexnow
  - Developer: StoreSpark
  - Rating visible: 5.0 con 19 reseñas
  - Precio visible: desde $5/mes, prueba gratuita disponible
  - Plan Premium visible: $5/mes o $45/año
  - Soporte declarado: unlimited auto-submissions, all content types, intelligent submissions, multi-language & market support, index logs.
  - Accesos visibles: productos, colecciones, páginas de Online Store, Shopify Markets settings y traducciones.

- Shopify App Store — `InstaIndex: IndexNow & AI SEO`
  - URL: https://apps.shopify.com/instaindex
  - Developer: klipp.tech
  - Rating visible: 4.6 con 43 reseñas
  - Precio visible: desde $1/mes inicialmente; Basic $14/mes después; Premium $29/mes después.
  - Ventajas: partner Microsoft Bing declarado, logs, multi-language & market en Premium, AI visibility tracking.
  - Riesgo MatchWalls: incluye schema, RUM, 404 monitor e Instant Navigation; puede solaparse con trabajo técnico/schema ya realizado.

- IndexNow documentation
  - URL: https://www.indexnow.org/documentation
  - Criterio relevante: la key debe alojarse de forma accesible en el host; la ubicación de la key condiciona qué URLs puede cubrir.

## App recomendada para piloto 013I

`VERIFICADO PERO MEJORABLE`

Recomendación: `IndexNow: for Bing and Yandex` de StoreSpark.

Motivo:

- es la opción más enfocada a IndexNow;
- menor superficie funcional que InstaIndex;
- precio más bajo y claro;
- declara soporte multi-language & market;
- declara logs de indexación;
- reduce riesgo de duplicar schema, RUM, AI tracking o cambios de rendimiento.

No se afirma que la app garantice indexación, rankings ni citas en Copilot/IA.

## Configuración inicial propuesta si se aprueba la app exacta

`REQUIERE DECISION HUMANA`

Instalación:

- App: `IndexNow: for Bing and Yandex`
- Plan aprobado por Daniel: Premium mensual de $5/mes durante piloto. No anual. No lifetime.
- Activar solo configuración mínima.

Reglas de configuración:

1. No activar envíos masivos si existe interruptor o modo manual.
2. No enviar automáticamente todo el sitemap inicial sin revisar.
3. Limitar el piloto a una whitelist reducida.
4. Excluir muestras noindex.
5. Excluir URLs de prueba/sin valor.
6. Excluir IT/PT salvo autorización expresa.
7. Excluir filtros, búsquedas internas y parámetros.
8. Excluir URLs con incidencias de caché/render pendientes.
9. No tocar tema, Liquid, schema, robots, `llms.txt`, handles, URLs, redirecciones ni metadatos.

Whitelist inicial propuesta:

- Home canónica: `https://www.matchwalls.com/`
- Sitemap ya existente solo como referencia, no como envío masivo.
- 3-5 páginas/hubs evergreen con valor comercial y sin incidencias.
- 3-5 productos canónicos de alto valor si están limpios.
- Landings geográficas solo cuando el bloqueo 012O quede estable/resuelto.

## Riesgos

`VERIFICADO PERO MEJORABLE`

- La app puede tener auto-submit activado por defecto.
- Puede no permitir suficiente control granular de URLs.
- Puede acceder a traducciones y Markets.
- Puede enviar URLs noindex o de bajo valor si no se configura con cautela.
- Puede no mostrar logs suficientemente exportables.
- Puede tener cambios invisibles de configuración que deban auditarse tras instalación.

## Reversión

`VERIFICADO Y CORRECTO`

Si la app no cumple el checklist:

1. Desinstalar la app desde Shopify Admin.
2. Confirmar que no quedan App Embeds activos.
3. Confirmar que no se añadieron snippets, theme files ni scripts.
4. Confirmar que no se añadieron redirects ni keys.
5. Confirmar que no se enviaron URLs masivas.
6. Registrar desinstalación y estado final.

## Pruebas posteriores necesarias

`VERIFICADO Y CORRECTO`

Tras instalar/configurar, verificar:

- permisos concedidos en Shopify;
- configuración de auto-submit/manual-submit;
- existencia de logs;
- URLs enviadas;
- respuesta de IndexNow/Bing si la app la muestra;
- ausencia de cambios en tema/schema/robots/llms;
- que no se envían muestras noindex;
- que no se envían URLs IT/PT;
- que Bing Webmaster Tools sigue con sitemap correcto.

## Decisión necesaria

`REQUIERE DECISION HUMANA`

Para avanzar con instalación real, Daniel debe confirmar la app exacta y el plan. Texto recomendado:

`APROBADO LOTE MW-INDEXNOW-APP-PILOT-INSTALL-CONFIG-013I-STORESpark-PREMIUM`

Alcance exacto de esa aprobación:

- instalar `IndexNow: for Bing and Yandex` de StoreSpark;
- usar plan Premium mensual de $5/mes si Shopify lo solicita;
- no aceptar plan anual ni lifetime;
- revisar permisos antes de aceptar;
- configurar en modo mínimo/controlado;
- no activar envíos masivos sin revisión;
- no tocar tema, schema, robots, `llms.txt`, URLs, handles ni metadatos.
