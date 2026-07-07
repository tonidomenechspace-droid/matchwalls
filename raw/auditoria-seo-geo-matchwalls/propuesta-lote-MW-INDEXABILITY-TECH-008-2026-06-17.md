# Propuesta de lote - MW-INDEXABILITY-TECH-008

Estado: REQUIERE DECISION HUMANA

## Objetivo

Preparar la primera reparacion tecnica de indexabilidad para reducir ruido en Google y mejorar la comprension de MatchWalls por buscadores y sistemas IA, sin tocar contenido comercial sensible ni hacer cambios masivos sin mapa de reversion.

## Alcance propuesto

Este lote NO debe mezclar todos los problemas a la vez. Propongo dividir `MW-INDEXABILITY-TECH-008` en sublotes:

### 008A - Black Friday obsoleto

Recurso afectado:

- Tipo: Collection
- ID: `gid://shopify/Collection/646234440056`
- Legacy ID: `646234440056`
- Handle ES: `papel-pintado-black-friday`
- URL ES: `https://www.matchwalls.com/collections/papel-pintado-black-friday`

Valores actuales verificados:

- H1 publico: `BLACK FRIDAY 2024`
- SEO description Shopify contiene `Black Friday 2024`
- EN publico observado: title `Wallpaper Black Friday 2025 - Wallpaper Sale`, H1 `Black Friday 2024`
- Estado: pagina 200, indexable, canonical self.

Decision necesaria:

1. Convertir la pagina en una pagina evergreen de ofertas sin ano.
2. Actualizar a Black Friday 2026 solo si hay campana real y aprobada.
3. Retirar de indexacion o redirigir a una pagina de ofertas equivalente si no debe existir.

No se ejecutara nada hasta que Daniel elija una opcion y apruebe el lote exacto.

### 008B - URLs de prueba `facade-variants/test`

Recursos afectados:

- URLs detectadas historicamente en sitemap/inventario:
  - `/pages/facade-variants/test`
  - `/en/pages/facade-variants/test`
  - `/fr/pages/facade-variants/test`
  - `/de/pages/facade-variants/test`
  - `/nl/pages/facade-variants/test`
  - `/it/pages/facade-variants/test`
  - `/pt/pages/facade-variants/test`

Estado actual:

- Publico puntual: 301 a home localizada.
- Shopify Admin: sin pagina publicada y sin redireccion manual encontrada.
- Sitemap actual no se pudo revalidar tras 429.

Accion propuesta:

- Revalidar sitemap cuando deje de devolver 429.
- Si siguen en sitemap, localizar origen y retirarlas.
- No crear redirecciones nuevas si Shopify ya redirige y no existe sustituto equivalente.

### 008C - Muestras indexables

Recursos afectados:

- Ejemplo Shopify Admin:
  - Producto: `Muestra Abstract Curves Negro`
  - ID: `gid://shopify/Product/8554043474147`
  - Handle: `muestra-abstract-curves-negro`
  - Template: `muestra`

Estado actual:

- Producto activo, publicado, indexable.
- Auditoria previa detecta al menos 541 URLs de muestra.

Decision necesaria:

1. Definir muestras como no indexables.
2. Definir canonical desde muestra a producto principal, solo con mapa fiable.
3. Mantener algunas muestras indexables si existe demanda especifica y contenido unico.

Riesgo:

- No debe hacerse masivo sin mapa producto principal -> muestra.

### 008D - Handles con typos

Recursos afectados:

- `norid/noridcas`: 70 URLs detectadas.
- `enchathed`: 19 URLs detectadas.
- `matchalls`: 1 URL francesa.

Accion propuesta:

- Crear mapa maestro antes de tocar handles.
- Cambiar handles solo con 301 uno-a-uno.
- Validar canonical, hreflang, sitemap y enlaces internos tras cada grupo.

Riesgo:

- Alto si se ejecuta sin mapa.

### 008E - HTML semantico de paginas prioritarias

Recursos afectados:

- `https://www.matchwalls.com/en/pages/request-your-sample`
- `https://www.matchwalls.com/fr/pages/a-propos-de-nous`
- `https://www.matchwalls.com/nl/pages/over-ons`
- Otras paginas de `TEC-02`, `CON-05`, `INT-10`.

Tema MAIN verificado:

- ID: `gid://shopify/OnlineStoreTheme/178383749496`
- Nombre: `SEO schema hotfix - 2026-06-15`
- Rol: `MAIN`

Accion propuesta:

- Leer archivos de plantilla/secciones en solo lectura.
- Identificar por que no se renderiza H1/contenido localizado.
- Preparar hotfix en tema auxiliar, no directamente en MAIN.
- Publicar solo tras QA desktop/mobile ES/EN/FR/DE/NL y aprobacion exacta.

## Riesgos

- Cambios de handle sin redireccion pueden crear 404.
- Noindex/canonical masivo en muestras puede afectar URLs que ya convierten.
- Editar tema MAIN directamente puede provocar regresiones visuales.
- Cambiar Black Friday sin decision comercial puede eliminar una pagina de venta util.
- LangShop no basta si el problema esta en plantillas JSON/Liquid del tema.

## Respaldo y reversion

Antes de cualquier escritura futura:

- Guardar valores actuales de cada recurso.
- Exportar IDs, handles, SEO title, SEO description, estado, template y URL.
- Para handles: registrar mapa `actual -> nuevo -> redirect`.
- Para tema: trabajar en tema auxiliar y conservar MAIN intacto hasta aprobacion.
- Para noindex/canonical: registrar metafields/theme snippets afectados y forma de revertir.

## Pruebas posteriores obligatorias

- Shopify Admin: confirmar valores almacenados.
- Publico: status HTTP, title, H1, meta robots, canonical, hreflang.
- Sitemap: comprobar entrada o retirada.
- Search Console: validar solo cuando Daniel aporte export o se tenga acceso directo.
- Desktop/mobile: validar home, coleccion, producto, muestra y paginas corporativas.
- ES/EN/FR/DE/NL: comprobar contenido visible y coherencia lingüistica.

## Recomendacion de ejecucion

El siguiente lote ejecutable no debe ser masivo. Recomiendo empezar por:

`MW-INDEXABILITY-BLACK-FRIDAY-CLEANUP-008A`

Motivo:

- Alcance pequeno.
- Evidencia directa y actual.
- Pagina publica indexable con ano obsoleto.
- Menor riesgo que tocar cientos de muestras o handles.

Pero requiere decision editorial/comercial antes de preparar valores nuevos.

