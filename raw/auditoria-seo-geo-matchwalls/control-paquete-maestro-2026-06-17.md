# Control del paquete maestro SEO/GEO - 2026-06-17

## Alcance de esta sesion

Modo: solo lectura.

Objetivo: iniciar la revision del paquete maestro de auditoria SEO/GEO y contrastar los puntos criticos con el estado real actual de Shopify.

Cambios en Shopify: ninguno.

Mutaciones GraphQL: ninguna.

Publicaciones, traducciones, cambios de tema, inventario, URLs o redirecciones: ninguno.

## Documentos leidos

- `AGENTS.md`
- `resumen-ejecutivo.md`
- `backlog-priorizado.csv`
- `registro-cambios-ejecutados.md`
- `programa-ejecucion-seo-geo.md`
- `lista-maestra-errores-cambios-evoluciones-mejoras.md`
- Cabeceras de `auditoria-schema.md`, `auditoria-geo.md`, `analisis-competencia.md`, `roadmap-12-meses.md`
- Cabeceras de `auditoria-contenido-i18n-geo-2026-06-16.md`
- Cabeceras de `siguientes-lotes-contenido-i18n-geo-2026-06-16.md`

## Estado real comprobado en Shopify

Consulta realizada mediante Shopify Admin GraphQL en modo lectura.

- Tienda: `Matchwalls`
- Dominio principal: `https://www.matchwalls.com`
- Dominio Shopify: `matchwalls.myshopify.com`
- Tema MAIN actual: `SEO schema hotfix - 2026-06-15`
- ID tema MAIN: `gid://shopify/OnlineStoreTheme/178383749496`
- Estado del tema MAIN: `processing: false`, `processingFailed: false`
- Tema anterior `Production - SEO fix AggregateRating (2026-06-12)`: `UNPUBLISHED`
- Tema `SEO-GEO staging - 2026-06-15`: `UNPUBLISHED`

Idiomas:

- Principal: `es`
- Publicados: `es`, `en`, `fr`, `de`, `nl`, `it`, `pt-PT`
- Prioritarios segun AGENTS.md: `es`, `en`, `fr`, `de`, `nl`

Recursos comprobados como consultables:

- Productos activos y traducciones
- Paginas y traducciones
- Colecciones y traducciones
- Redirecciones
- Temas
- Locales publicados

## Estado del paquete de entregables

Los 11 entregables maestros existen en `auditoria-seo-geo-matchwalls`.

| Archivo | Estado | Observacion |
| --- | --- | --- |
| `resumen-ejecutivo.md` | Existe | Incluye actualizacion del hotfix publicado. |
| `inventario-urls.csv` | Existe | 7.932 filas. |
| `auditoria-seo-tecnico.csv` | Existe | 8 filas. |
| `auditoria-internacional.csv` | Existe | 10 filas. |
| `auditoria-catalogo.csv` | Existe | 13 filas. |
| `auditoria-contenidos.csv` | Existe | 11 filas. |
| `auditoria-schema.md` | Existe | Incluye seccion de actualizacion 2026-06-16. |
| `auditoria-geo.md` | Existe | Auditoria GEO/AEO base. |
| `analisis-competencia.md` | Existe | Analisis cualitativo inicial. |
| `backlog-priorizado.csv` | Existe | 41 filas. |
| `roadmap-12-meses.md` | Existe | Roadmap base. |

## Lectura del backlog

Distribucion por horizonte:

- `0-30 dias`: 27 acciones
- `31-90 dias`: 13 acciones
- `3-6 meses`: 1 accion

Estados actuales del campo `estado_evidencia`:

- `Verificado`: 37
- `Verificado con limitacion`: 1
- `Hipotesis respaldada`: 1
- `Verificado y preparado`: 1
- `CORREGIDO Y VERIFICADO`: 1

Observacion de gobernanza: el backlog conserva estados historicos que no coinciden exactamente con la clasificacion obligatoria de `AGENTS.md`. No se normalizaron en esta sesion para evitar alterar documentos maestros sin una tarea especifica de normalizacion.

## Conciliacion inicial

1. El estado real actual de Shopify confirma que el hotfix `SEO schema hotfix - 2026-06-15` esta publicado como MAIN.
2. `resumen-ejecutivo.md` y `registro-cambios-ejecutados.md` reflejan correctamente esa publicacion posterior.
3. Algunas secciones antiguas de `programa-ejecucion-seo-geo.md` y documentos iniciales aun mencionan el hotfix como preparado o pendiente. Deben leerse como historico, no como estado actual.
4. El registro mas reciente prevalece sobre secciones antiguas cuando haya contradiccion temporal.
5. Los bloqueos de contenido y plantilla siguen abiertos: footer, header claims, home DE/NL, muestras, FAQ, Sobre nosotros, Social/Prensa/Afiliacion, Guia de instalacion y blog.

## Riesgos detectados antes de ejecutar cambios

- La conexion Shopify tiene permisos de escritura disponibles, aunque esta sesion solo uso lectura.
- El paquete mezcla estados historicos y estados posteriores; cualquier lote debe reconciliar documentos antes de actuar.
- Varios documentos usan etiquetas antiguas como `Verificado`, no la taxonomia estricta de `AGENTS.md`.
- Hay tareas del backlog ya corregidas parcialmente, especialmente schema hotfix, que no deben repetirse.
- Los proximos cambios recomendados afectan tema, footer/header o contenido fijo de plantilla; son de alto riesgo y requieren lote aprobado.

## Proximos lotes sugeridos por los documentos

Sin ejecutar cambios:

1. `MW-FOOTER-I18N-001` - corregir footer global ES/EN/FR/DE/NL.
2. `MW-HEADER-CLAIMS-I18N-001` - revisar claims comerciales globales.
3. `MW-HOME-DE-NL-I18N-001` - corregir home DE/NL.
4. `MW-MUESTRAS-I18N-H1-001` - resolver H1 y contenido de muestras.
5. `MW-FAQ-TEMPLATE-I18N-001` - migrar FAQ desde bloques fijos a contenido gobernado.

## Decision operativa

No ejecutar ninguna escritura en Shopify hasta presentar un lote con:

- alcance exacto;
- recursos e IDs;
- valores actuales;
- valores propuestos;
- riesgos;
- respaldo;
- metodo de reversion;
- QA posterior;
- aprobacion literal `APROBADO LOTE [NOMBRE]`.

Estado final de esta sesion: `VERIFICADO PERO MEJORABLE`.
