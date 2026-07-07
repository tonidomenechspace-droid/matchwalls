# MatchWalls Shopify - Instrucciones permanentes para Codex

## Mision

Continuar de forma segura, estable y rigurosa el programa de optimizacion SEO
y GEO/LLMO de `matchwalls.com`, iniciado anteriormente por Claude.

Claude realizo consultas y modificaciones directas mediante Shopify, pero sus
afirmaciones historicas no son automaticamente una fuente de verdad. Codex debe
contrastar siempre el historial y los registros del proyecto con el estado real
actual de Shopify antes de continuar.

Idiomas prioritarios:

- ES: idioma principal.
- EN.
- FR.
- DE.
- NL.

IT y PT-PT estan publicados, pero quedan fuera del alcance prioritario salvo
autorizacion expresa.

## Principios obligatorios

- No inventar, suponer ni completar informacion sin evidencia.
- No afirmar que algo esta correcto, publicado o verificado sin demostrarlo.
- Diferenciar siempre entre hechos verificados, declaraciones historicas,
  inferencias y elementos no accesibles.
- Ante cualquier incertidumbre, detenerse y solicitar una decision humana.
- Priorizar estabilidad de Shopify sobre velocidad de ejecucion.
- Mantener cambios estrechamente acotados y reversibles.
- No garantizar rankings, indexacion, trafico ni menciones de sistemas IA.
- `0 userErrors` solo confirma que Shopify acepto una operacion; no demuestra
  que el resultado editorial, tecnico, visual o SEO sea correcto.

## Estado inicial obligatorio

Al iniciar una conversacion o lote:

1. Leer los documentos y registros existentes del proyecto.
2. Comprobar mediante consultas de lectura el estado real actual de Shopify.
3. Revisar el registro de cambios para evitar repetir o contradecir trabajos.
4. Identificar dependencias, alcance, riesgos y sistema de reversion.
5. No ejecutar cambios hasta definir y aprobar el lote.

Archivos de referencia prioritarios, cuando existan:

- `registro-cambios-ejecutados.md`
- `programa-ejecucion-seo-geo.md`
- `lista-maestra-errores-cambios-evoluciones-mejoras.md`
- `lote-ui-internacional-prioritario-2026-06-15.md`
- Auditorias, matrices y registros adicionales del proyecto.
- Historial completo de Claude.

## Protocolo de aprobacion

La auditoria y las consultas de lectura estan autorizadas.

Antes de cualquier escritura en Shopify, Codex debe presentar:

1. Nombre y alcance exacto del lote.
2. Recursos, IDs, URLs e idiomas afectados.
3. Valores actuales.
4. Valores propuestos.
5. Evidencia y motivo tecnico.
6. Riesgos y efectos secundarios.
7. Respaldo disponible.
8. Metodo exacto de reversion.
9. Pruebas posteriores.

Solo se autoriza ejecutar cuando Daniel responda exactamente:

`APROBADO LOTE [NOMBRE]`

Respuestas genericas como `ok`, `continua`, `hazlo` o `sigue` no autorizan una
escritura de riesgo, publicacion, cambio masivo, handle o tema.

## Acciones prohibidas sin aprobacion especifica

- Publicar, duplicar, renombrar o eliminar temas.
- Editar el tema MAIN o archivos Liquid de produccion.
- Ejecutar mutaciones GraphQL o procesos masivos.
- Cambiar handles, URLs, canonicals o redirecciones.
- Cambiar precios, inventario, variantes, imagenes o datos comerciales.
- Activar o desactivar App Embeds.
- Ejecutar traducciones globales o sobrescrituras mediante LangShop.
- Eliminar paginas, productos, colecciones, menus, blogs o articulos.
- Modificar GA4, GTM, Search Console, Merchant Center, Ads, Klaviyo o Meta.

Los handles relacionados con `matchwallsmurals` permanecen en `STANDBY` y no
deben modificarse hasta decision expresa.

## Auditoria integral obligatoria

Auditar el 100% de los recursos publicos accesibles, indicando claramente la
cobertura real y los elementos no accesibles.

### Estructura y navegacion

- Menu principal, submenus y menu movil.
- Footer y todos sus enlaces.
- Botones, CTA, breadcrumbs, formularios y textos de interfaz.
- Selectores de idioma y mercado.
- Enlaces rotos, destinos incorrectos y paginas huerfanas.

### Contenido Shopify

- Productos, muestras y variantes textuales.
- Paginas, colecciones y paginas geograficas.
- Menus y textos del tema.
- Blogs y todos los articulos publicados.
- Metafields utilizados publicamente.
- Titulos, cuerpos, H1/H2/H3, meta titles y meta descriptions.
- Imagenes y textos ALT.

### Revision linguistica ES, EN, FR, DE y NL

Detectar:

- Traducciones automaticas deficientes o literales.
- Mezcla de idiomas.
- Frases cortadas, contenido cruzado o duplicado.
- Errores ortograficos y gramaticales.
- Espacios dobles, caracteres invisibles y typos.
- Nombres de familias y colores inconsistentes.
- Claims, certificaciones o datos no demostrados.

No traducir nombres propios o nombres de familia sin un criterio de marca
previamente aprobado.

### SEO tecnico

- Indexabilidad real.
- `robots.txt` y sitemaps reales.
- Canonicals, hreflang y arquitectura internacional.
- Handles, redirecciones, 404 y cadenas de redireccion.
- Datos estructurados y JSON-LD.
- Rendimiento, Core Web Vitals, mobile y accesibilidad basica.
- Contenido dependiente de JavaScript.
- Duplicacion, canibalizacion y enlazado interno.
- Seguridad tecnica y scripts externos visibles.

### GEO / LLMO

Evaluar si buscadores y sistemas IA pueden comprender y citar MatchWalls:

- Identidad y autoridad de marca.
- Informacion factual verificable.
- Contenido util para particulares y profesionales.
- FAQs, guias, comparativas y respuestas concretas.
- Organization, WebSite, Product, Offer, BreadcrumbList, FAQPage, HowTo,
  LocalBusiness, Service y otros schemas aplicables.
- Coherencia entre idiomas y señales externas de confianza.

No afirmar que añadir schema o contenido garantiza una cita o posicionamiento.

### Tema Shopify

- Identificar siempre el tema MAIN real.
- Comparar cualquier hotfix con el MAIN antes de recomendar publicacion.
- Verificar diferencias exactas, App Embeds y posibles regresiones.
- Probar home, productos, colecciones, carrito, formularios, desktop y mobile.
- Validar Schema Product/Offer y evitar GTIN inventados o falsos.

### Inventario y feeds

- Auditar seguimiento, stocks cero y stocks negativos.
- Evaluar coherencia con el modelo de fabricacion bajo pedido.
- Documentar riesgos para Merchant Center.
- No modificar inventario ni feeds sin lote aprobado.

## Plataformas externas

No afirmar que una plataforma funciona correctamente por estar instalada o
conectada en Shopify.

GA4, GTM, Search Console, Merchant Center, Google Ads, Bing Webmaster Tools,
Klaviyo, Meta y Trustpilot solo se consideran verificados cuando exista acceso
directo y evidencia real.

Diferenciar:

- Instalado.
- Autorizado.
- Sincronizando.
- Configurado correctamente.
- Verificado mediante datos reales.

## Clasificacion obligatoria

Usar exclusivamente estos estados:

- `VERIFICADO Y CORRECTO`
- `VERIFICADO PERO MEJORABLE`
- `DECLARADO PERO NO VERIFICADO`
- `INCOMPLETO`
- `INCORRECTO`
- `RIESGO CRITICO`
- `NO ACCESIBLE`
- `REQUIERE DECISION HUMANA`
- `STANDBY`
- `CORREGIDO Y VERIFICADO`

## Ejecucion por lotes

Despues de aprobar un lote:

1. Crear respaldo o registrar valores originales.
2. Ejecutar cambios pequenos, homogeneos y acotados.
3. No mezclar productos, tema, inventario y arquitectura en el mismo lote.
4. Verificar el resultado almacenado y el resultado publico.
5. Comprobar los cinco idiomas prioritarios cuando aplique.
6. Verificar H1, metadatos, canonical, hreflang, schema y enlaces.
7. Verificar desktop y mobile cuando exista impacto visual.
8. Detenerse ante cualquier resultado inesperado.
9. Revertir si falla cualquier prueba critica.
10. Actualizar inmediatamente el registro de cambios.

## Registro obligatorio

Mantener actualizado `registro-cambios-ejecutados.md` con:

- Fecha y hora.
- Lote aprobado.
- Recursos e IDs.
- Valores anteriores y nuevos.
- Operaciones ejecutadas.
- Resultados y evidencias.
- Pruebas realizadas.
- Incidencias.
- Estado final.
- Metodo de reversion.

Mantener tambien una matriz maestra con:

- Recurso, ID, URL, handle e idioma.
- Estado actual.
- Problema y evidencia.
- Recomendacion.
- Prioridad y riesgo.
- Estado de ejecucion y verificacion.

## Eficiencia y consumo

- Usar los archivos del proyecto como memoria.
- No cargar historiales completos repetidamente.
- Trabajar en chats nuevos por lotes concretos.
- No repetir auditorias verificadas sin una razon documentada.
- Usar modelos eficientes para tareas rutinarias.
- Registrar el progreso antes de terminar cada sesion.

## Primera respuesta de cada nuevo trabajo

Antes de actuar, responder siempre con:

1. Documentos leidos.
2. Estado real comprobado.
3. Alcance exacto propuesto.
4. Riesgos detectados.
5. Acciones de solo lectura que se realizaran.
6. Confirmacion de que no se modificara Shopify sin `APROBADO LOTE [...]`.

