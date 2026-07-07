# MW-INDEXNOW-STABLE-IMPLEMENTATION-OPTIONS-013G

Fecha: 2026-07-05  
Modo: solo lectura / propuesta técnica.  
Estado del lote: `VERIFICADO Y CORRECTO` como análisis documental y técnico.  
Estado de ejecución IndexNow: `REQUIERE DECISION HUMANA`.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `resultado-MW-INDEXNOW-CDN-REDIRECT-MANUAL-VALIDATION-013F3-2026-07-05.md`
- `resultado-MW-INDEXNOW-CDN-REDIRECT-STABILITY-RECHECK-013F4-2026-07-05.md`
- `resultado-MW-INDEXNOW-CDN-REDIRECT-TEMP-ROLLBACK-013F4R-2026-07-05.md`
- `registro-cambios-ejecutados.md`

## Estado público comprobado

`CORREGIDO Y VERIFICADO`

Comprobación realizada el 2026-07-05 10:27 +02:00:

- `https://www.matchwalls.com/indexnow.txt` → HTTP `404`, no contiene key.
- `https://www.matchwalls.com/1fe8851103534006a2a9433fe8b56f2d.txt` → HTTP `404`, no contiene key.
- URL directa antigua de Shopify CDN → HTTP `200`, todavía contiene la key por caché residual directa.

Conclusión: no queda key activa bajo `www.matchwalls.com`. La incidencia residual directa de CDN queda como `VERIFICADO PERO MEJORABLE`, pero no afecta a la propiedad pública del dominio porque el redirect fue eliminado en `013F4R`.

Evidencia: `public-state-MW-INDEXNOW-STABLE-IMPLEMENTATION-OPTIONS-013G-2026-07-05.csv`.

## Restricciones técnicas verificadas

`VERIFICADO Y CORRECTO`

- IndexNow requiere demostrar propiedad alojando una key UTF-8 en el host. La vía preferida es `/{key}.txt` en raíz.
- Si la key se aloja en una ruta interna y se usa `keyLocation`, esa ubicación limita el conjunto de URLs que pueden enviarse al prefijo de la key. Por eso una key bajo `/apps/` no cubriría de forma fiable `/products/`, `/pages/` o `/collections/`.
- Bing indica que IndexNow ayuda a notificar cambios, pero no garantiza rastreo, indexación ni ranking.
- En Shopify, la vía probada `Shopify Files + URL Redirect` quedó descartada por el resultado `INCORRECTO` del lote `013F4`: la ruta raíz pública devolvía `429`.

Fuentes consultadas:

- IndexNow documentation: https://www.indexnow.org/documentation
- Bing IndexNow get started: https://www.bing.com/indexnow/getstarted
- Shopify App Store — IndexNow: for Bing and Yandex: https://apps.shopify.com/indexnow
- Shopify App Store — InstaIndex: IndexNow & AI SEO: https://apps.shopify.com/instaindex

## Opciones evaluadas

### 1. Shopify Files + URL Redirect a CDN

Estado: `INCORRECTO`.

Fue aceptado puntualmente en `013F3`, pero `013F4` demostró que no es estable: la ruta pública bajo `www.matchwalls.com/{key}.txt` devolvía `429`. Ya fue revertido en `013F4R`.

Decisión 013G: descartado para producción.

### 2. Página o Liquid simulando archivo TXT

Estado: `INCORRECTO`.

No es una vía limpia porque mezcla tema con infraestructura técnica, no garantiza un archivo raíz real ni un `text/plain` estable, y añade riesgo sobre el tema publicado.

Decisión 013G: no usar.

### 3. App Shopify especializada en IndexNow

Estado: `VERIFICADO PERO MEJORABLE`.

Es la vía recomendada para un piloto controlado, siempre que la app confirme por escrito:

1. cómo valida/aloja la key IndexNow para un dominio Shopify;
2. soporte real para multi-idioma y mercados;
3. exclusión de URLs noindex, muestras, filtros, URLs de prueba, IT/PT y URLs en standby;
4. logs exportables de URLs enviadas y respuestas;
5. que no modifica tema, schema, `llms.txt`, robots, handles, URLs ni metadatos sin permiso explícito.

Candidatos revisados:

- `IndexNow: for Bing and Yandex`: candidato preferente para piloto por foco específico, soporte multi-language/market declarado, coste bajo y menor superficie funcional.
- `InstaIndex: IndexNow & AI SEO`: candidato potente, pero más amplio; incluye schema, RUM, 404 monitor y AI visibility, por lo que exige más cautela para no duplicar trabajo ya hecho en MatchWalls.

Decisión 013G: preparar selección/piloto, no instalar todavía.

### 4. Endpoint/proxy/CDN externo bajo `www.matchwalls.com`

Estado: `VERIFICADO PERO MEJORABLE`.

Técnicamente sería la solución más limpia si se puede servir `https://www.matchwalls.com/{key}.txt` como HTTP `200` y `text/plain` sin pasar por redirects inestables. Pero requiere infraestructura externa, control DNS/proxy/CDN y pruebas para no afectar Shopify.

Decisión 013G: reservar como alternativa si ninguna app pasa el checklist.

### 5. App proxy o key bajo `/apps/...`

Estado: `INCORRECTO` para el objetivo global.

Por la regla de `keyLocation`, una key ubicada bajo `/apps/...` no cubriría de forma fiable las URLs importantes bajo `/products/`, `/pages/` y `/collections/`.

Decisión 013G: no usar como vía global de MatchWalls.

### 6. No activar IndexNow todavía

Estado: `VERIFICADO PERO MEJORABLE`.

Es aceptable temporalmente. Bing Webmaster Tools ya tiene sitemap detectado y la web puede seguir rastreándose por sitemap/enlaces. Pero IndexNow sigue pendiente como capa Bing/Copilot para notificar cambios valiosos.

Decisión 013G: aceptable solo como pausa, no como solución final.

## Recomendación 013G

`REQUIERE DECISION HUMANA`

No volver a usar el redirect CDN. La ruta estable recomendada es:

1. seleccionar app IndexNow con checklist de seguridad;
2. instalar solo tras aprobación exacta;
3. desactivar cualquier auto-submit masivo inicial si la app lo permite;
4. enviar primero una whitelist pequeña de URLs canónicas y valiosas;
5. verificar en Bing Webmaster Tools recepción de URLs;
6. excluir muestras noindex, URLs sin valor, filtros, pruebas, IT/PT y cualquier URL con incidencia de render/cache pendiente.

Whitelist inicial sugerida para futuro piloto:

- home canónica;
- hubs/categorías evergreen prioritarias;
- páginas informativas principales;
- productos top canónicos sin incidencias;
- landings geográficas solo cuando estén estables y verificadas tras la incidencia Shopify 012O.

## Riesgos

`VERIFICADO PERO MEJORABLE`

- App con permisos excesivos o funciones adicionales que modifiquen schema, rendimiento, `llms.txt` o tema.
- Auto-submit masivo de URLs no valiosas o noindex.
- Duplicación de señales si se envían variantes de idioma/mercado incorrectas.
- Coste mensual sin logs suficientes.
- IndexNow recibido no equivale a indexación ni cita en Copilot.

## Próximo lote recomendado

`MW-INDEXNOW-APP-PILOT-SELECTION-013H`

Objetivo: elegir la app candidata y preparar checklist de instalación segura, sin instalar todavía.

Si Daniel decide instalar una app después de la selección, el lote de escritura deberá ser independiente y aprobarse exactamente como:

`APROBADO LOTE MW-INDEXNOW-APP-PILOT-INSTALL-CONFIG-013I`

Ese lote deberá incluir app exacta, coste, permisos, configuración inicial, exclusiones, whitelist, pruebas y rollback.
