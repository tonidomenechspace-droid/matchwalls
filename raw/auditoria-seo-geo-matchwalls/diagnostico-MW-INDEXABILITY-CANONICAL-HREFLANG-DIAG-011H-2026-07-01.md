# Diagnostico MW-INDEXABILITY-CANONICAL-HREFLANG-DIAG-011H

Fecha: 2026-07-01  
Estado final: `VERIFICADO PERO MEJORABLE`  
Tipo: diagnostico de solo lectura  
Shopify: sin cambios

## Alcance

Auditoria prioritaria post-limpieza de canonicals y hreflang en ES, EN, FR, DE y NL.

La muestra se construyo desde:

- Home ES/EN/FR/DE/NL.
- Pagina informativa de muestras ES/EN/FR/DE/NL.
- Producto tecnico `custom-file-uploader` ES/EN/FR/DE/NL.
- Colecciones prioritarias y recientemente tratadas:
  - `murales`.
  - `murales-estilo-a-rayas`.
  - `kids-murales`.
  - `papeles-pintados-para-banos` / `salles-de-bain-peintes`.

## Estado Admin Shopify comprobado

- Dominio principal: `https://www.matchwalls.com`.
- SSL activo: `true`.
- Idioma principal: ES.
- Idiomas prioritarios publicados: ES, EN, FR, DE, NL.
- IT y PT-PT tambien publicados, pero fuera de prioridad activa.
- Web presence principal: `www.matchwalls.com`.

Evidencia: `admin-read-MW-INDEXABILITY-CANONICAL-HREFLANG-DIAG-011H-2026-07-01.csv`.

## Estado sitemap comprobado

- Sitemap index: 29 archivos.
- URLs totales: 7.274.
- Errores de lectura: 0.

Evidencia: `sitemap-MW-INDEXABILITY-CANONICAL-HREFLANG-DIAG-011H-2026-07-01.csv`.

## Resultado publico

- URLs auditadas: 39.
- 39/39 devuelven 200 tras recheck.
- 39/39 tienen canonical.
- 35/39 tienen canonical exacto.
- 4/39 normalizan la version con slash final hacia canonical sin slash:
  - `/en/` -> canonical `/en`.
  - `/fr/` -> canonical `/fr`.
  - `/de/` -> canonical `/de`.
  - `/nl/` -> canonical `/nl`.
- 39/39 incluyen hreflang para ES, EN, FR, DE, NL y `x-default`.
- 39/39 tienen H1.
- 30/39 estan en sitemap.
- 5/39 no estan en sitemap porque son productos `custom-file-uploader` con `noindex,nofollow`, estado coherente.
- 4/39 no estan en sitemap porque son variantes con slash final de las homes localizadas; su canonical apunta a la version sin slash.

Evidencia: `qa-publico-MW-INDEXABILITY-CANONICAL-HREFLANG-DIAG-011H-2026-07-01.csv`.

## Incidencias

### 1. No hay fallo critico canonical/hreflang en la muestra prioritaria

Estado: `VERIFICADO Y CORRECTO`

No se detectan canonicals a 404, hreflang ausentes en idiomas prioritarios, `noindex` dentro del sitemap ni URLs canonicas prioritarias sin H1.

### 2. Normalizacion con slash final en homes localizadas

Estado: `VERIFICADO PERO MEJORABLE`

Las rutas `/en/`, `/fr/`, `/de/` y `/nl/` responden 200 y canonizan a `/en`, `/fr`, `/de` y `/nl`. No estan en sitemap y las versiones canonicas si aparecen.

No se recomienda abrir escritura ahora. Se recomienda dejarlo como observacion de bajo riesgo y revisarlo solo si GSC/Bing detectan duplicacion por trailing slash.

Lote opcional en `STANDBY` si hubiera evidencia externa:

`MW-INDEXABILITY-CANONICAL-HREFLANG-ROOT-SLASH-011H1`

### 3. Handles legacy `matchwallsmurals`

Estado: `STANDBY`

En varias colecciones localizadas los handles mantienen `matchwallsmurals`. En esta muestra no generan fallo canonical/hreflang: devuelven 200, canonical propio, hreflang completo y presencia en sitemap.

No cambiar handles sin mapa 301 aprobado.

## Conclusion

El lote `MW-INDEXABILITY-CANONICAL-HREFLANG-DIAG-011H` queda cerrado como `VERIFICADO PERO MEJORABLE`:

- No hay bloqueador critico para seguir.
- No se propone escritura inmediata.
- La siguiente prioridad operativa puede pasar a geo collections restantes o crawlers IA segun orden del plan.

## Siguiente lote recomendado

`MW-INDEXABILITY-GEO-COLLECTIONS-ROLLING-DIAG-011E2`

Tipo: solo lectura.

Objetivo: clasificar colecciones geograficas restantes en ES, EN, FR, DE y NL antes de proponer cualquier noindex rolling.
