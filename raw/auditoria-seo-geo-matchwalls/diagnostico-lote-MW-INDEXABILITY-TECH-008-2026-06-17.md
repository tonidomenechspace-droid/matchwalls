# Diagnostico de indexabilidad tecnica - MW-INDEXABILITY-TECH-008

Fecha: 2026-06-17 21:56:58 +02:00

Estado global del bloque: INCOMPLETO

Este documento registra comprobaciones de solo lectura realizadas para preparar la siguiente reparacion tecnica SEO/GEO. No se han ejecutado mutaciones, imports de LangShop, cambios de tema, publicaciones ni operaciones masivas.

## Documentos leidos

- `auditoria-seo-geo-matchwalls/diagnostico-lote-MW-LANGSHOP-PUBLIC-FOOTER-RESIDUE-007-2026-06-17.md`
- `auditoria-seo-geo-matchwalls/registro-cambios-ejecutados.md`
- `auditoria-seo-geo-matchwalls/auditoria-seo-tecnico.csv`
- `auditoria-seo-geo-matchwalls/auditoria-internacional.csv`
- `auditoria-seo-geo-matchwalls/auditoria-catalogo.csv`
- `auditoria-seo-geo-matchwalls/auditoria-contenidos.csv`
- `auditoria-seo-geo-matchwalls/backlog-priorizado.csv`
- `auditoria-seo-geo-matchwalls/sitemap-urls.txt`

## Estado real comprobado

### Footer residue 007

Estado: CORREGIDO Y VERIFICADO

En el bloque anterior se verifico que el footer publico actual ES/EN/FR/DE/NL ya no muestra `Tarjeta regalo`, `Gift card`, `Black Friday 2024` ni `International shipments` como residuo visible. No se realizaron cambios en Shopify en esta comprobacion.

### Sitemap y proteccion temporal

Estado: INCOMPLETO

Lectura publica inicial del sitemap:

- `sitemap.xml` respondio 200.
- Se detectaron 36 sub-sitemaps.
- Se detectaron 7932 URLs.
- Grupos sospechosos detectados en sitemap o inventario previo:
  - URLs de prueba `facade-variants/test`: 7 en el inventario previo y lectura inicial.
  - URLs de muestra: al menos 541 en auditoria `CAT-01`; una lectura restringida por patron detecto 311.
  - Black Friday: 5 URLs localizadas detectadas en lectura actual.
  - `matchalls`: 1 URL francesa detectada.
  - `enchathed`: 19 URLs detectadas.
  - `norid/noridcas`: 70 URLs detectadas.
  - Sufijo `-1`: 424 URLs detectadas.

Limitacion posterior:

- Tras ampliar el muestreo publico, `https://www.matchwalls.com/sitemap.xml` empezo a devolver `429` con HTML `Verifying your connection...`.
- Esto se clasifica como NO ACCESIBLE temporal por proteccion/rate limit del sitio para esta sesion.
- No se interpreta como sitemap vacio ni como error SEO confirmado.

### Tema Shopify publicado

Estado: VERIFICADO Y CORRECTO

Tema MAIN real consultado via Shopify Admin, solo lectura:

- ID: `gid://shopify/OnlineStoreTheme/178383749496`
- Nombre: `SEO schema hotfix - 2026-06-15`
- Rol: `MAIN`
- Creado: `2026-06-15T12:33:28Z`
- Actualizado: `2026-06-15T22:42:44Z`
- `processing`: `false`
- `processingFailed`: `false`

No se han leido ni modificado archivos Liquid/JSON del tema en este bloque.

## Hallazgos verificados

### 1. Coleccion Black Friday publicada y obsoleta

Estado: INCORRECTO

Evidencia publica:

- `https://www.matchwalls.com/collections/papel-pintado-black-friday` responde 200.
- Canonical self.
- Sin `noindex` detectado.
- H1: `BLACK FRIDAY 2024`.

Evidencia Shopify Admin:

- ID: `gid://shopify/Collection/646234440056`
- Legacy ID: `646234440056`
- Titulo: `Papel Pintado Black Friday`
- Handle: `papel-pintado-black-friday`
- Template: `black-friday`
- SEO title: `Papel Pintado Black Friday - Oferta Papel Pintado`
- SEO description contiene `Black Friday 2024`.
- Actualizado: `2026-04-20T15:23:00Z`

Riesgo:

- Contenido estacional obsoleto e indexable.
- Senal editorial contradictoria para Google y motores IA.
- Puede contaminar snippets, enlazado interno y confianza de marca.

Requiere decision humana:

- Mantener como campana evergreen de ofertas.
- Actualizar a campana 2026 con contenido real.
- Despublicar/noindex/redirect si no existe campana activa.

### 2. Muestras indexables como productos

Estado: VERIFICADO PERO MEJORABLE

Evidencia publica puntual:

- `https://www.matchwalls.com/products/muestra-abstract-curves-negro` responde 200.
- Canonical self.
- Sin `noindex` detectado.
- H1: `Muestra Abstract Curves Negro`.

Evidencia Shopify Admin:

- ID: `gid://shopify/Product/8554043474147`
- Legacy ID: `8554043474147`
- Titulo: `Muestra Abstract Curves Negro`
- Handle: `muestra-abstract-curves-negro`
- Estado: `ACTIVE`
- Publicado: `2024-06-14T15:27:22Z`
- Template: `muestra`
- SEO title/description: `null`

Riesgo:

- Canibalizacion de productos principales.
- Expansion del indice con SKUs auxiliares.
- Posible aterrizaje de trafico en una muestra en lugar del producto principal.

Requiere decision humana:

- Noindex masivo de muestras.
- Canonical a producto principal cuando exista mapeo fiable.
- Mantener indexables solo muestras con contenido propio, si se justifica por demanda.

### 3. Handles con errores de familia

Estado: INCORRECTO

Evidencia publica y de inventario:

- `norid/noridcas`: 70 URLs detectadas.
- `enchathed`: 19 URLs detectadas.

Evidencia Shopify Admin puntual:

- Producto `Líneas Nórdicas Negro`
- ID: `gid://shopify/Product/8474101645539`
- Legacy ID: `8474101645539`
- Handle: `lineas-noridcas-negro`
- Estado: `ACTIVE`
- Publicado: `2024-08-12T20:07:55Z`
- Template: `murales`
- SEO title: `Papel Pintado Líneas Nórdicas Negro`

Riesgo:

- La pagina visible muestra nombre correcto, pero el handle contiene error.
- Cambiar handles sin mapa 301 uno-a-uno puede causar 404, perdida de senales y hreflang roto.

Requiere decision humana:

- Crear diccionario maestro de familias.
- Mapear handle actual -> handle correcto -> redireccion 301.
- Verificar canonical, hreflang y enlaces internos antes de tocar Shopify.

### 4. URL francesa con marca mal escrita

Estado: INCORRECTO

Evidencia publica:

- `https://www.matchwalls.com/fr/collections/nouveaux-matchalls-matchwallsmurals` responde 200.
- Canonical self.
- Sin `noindex` detectado.
- H1: `Nouveaux Papiers Peints`.

Riesgo:

- Marca mal escrita en URL indexable.
- Senal de baja calidad para SEO internacional y sistemas de IA.

Requiere decision humana:

- Confirmar handle frances correcto.
- Crear 301 de `matchalls` a `matchwalls`.
- Verificar hreflang y enlaces internos.

### 5. Paginas con contenido principal/H1 ausente

Estado: INCORRECTO

Evidencia publica puntual:

- `https://www.matchwalls.com/en/pages/request-your-sample`: 200, canonical self, H1 count 0.
- `https://www.matchwalls.com/fr/pages/a-propos-de-nous`: 200, canonical self, H1 count 0.
- `https://www.matchwalls.com/nl/pages/over-ons`: 200, canonical self, H1 count 0.

Coincide con `CON-05`, `INT-10` y `TEC-02`.

Riesgo:

- Paginas indexables sin encabezado principal claro.
- Traducciones guardadas pueden no estar renderizando por plantillas localizadas incompletas.
- Mala comprension para buscadores y sistemas IA.

Requiere reparacion en tema/plantillas o secciones, no en LangShop solamente.

### 6. URLs `facade-variants/test`

Estado: INCOMPLETO

Evidencia historica/local:

- `sitemap-urls.txt` contiene URLs `facade-variants/test` por idioma.
- `TEC-01` las tenia como URLs internas de prueba indexables.

Evidencia publica actual parcial:

- Peticiones puntuales a `/en/pages/facade-variants/test` y `/de/pages/facade-variants/test` respondieron 301 a la home localizada.

Evidencia Shopify Admin:

- No se encontro pagina publicada equivalente.
- No se encontro redireccion manual `facade-variants`.
- Las paginas `Testing Newsletter` y `Test Dick Form Klaviyo` estan sin publicar.

Clasificacion:

- Ya no se puede afirmar que sigan publicadas con 200.
- Queda por revalidar cuando el sitemap vuelva a ser accesible sin 429.

## Relacion con Search Console aportado por Daniel

Estado: DECLARADO PERO NO VERIFICADO

Daniel aporto capturas de Search Console con:

- 481 URLs no encontradas 404.
- 420 URLs excluidas por `noindex`.
- 265 alternativas con canonical adecuado.
- 66 paginas con redireccion.
- 15 errores 5xx.
- 6268 rastreadas actualmente sin indexar.
- 3544 descubiertas actualmente sin indexar.

No hay acceso directo a Search Console desde esta sesion. Se usan como evidencia aportada por Daniel, pendiente de export CSV para cruzar URL a URL.

## Conclusiones

Estado global: INCOMPLETO

No estamos ante un unico problema de LangShop. Para subir autoridad y trafico hay que reparar por capas:

1. Indice limpio: muestras, temporales, test, 404, redirects y 5xx.
2. HTML semantico: H1, contenido visible, canonical, hreflang, schema.
3. Internacionalizacion: handles, traducciones visibles, plantillas localizadas.
4. Autoridad/GEO: contenido factual, FAQs, guias, B2B, entidad de marca, casos reales.

No se puede declarar `CORREGIDO Y VERIFICADO` global hasta completar lotes separados y QA publico posterior.

