# MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-DECISION-011G7A

Fecha: 2026-06-30  
Tipo: diagnostico y decision de solo lectura  
Estado final: `REQUIERE DECISION HUMANA`

## 1. Alcance

Analizar exclusivamente el redirect de muestra detectado en 011G7:

- ID: `gid://shopify/UrlRedirect/412616229091`
- Fuente: `/products/muestra-desnudos-blanco-y-negro`
- Target actual: `/collections/muestras`

No se han modificado redirecciones, productos, paginas, colecciones, handles, tema, traducciones, canonicals ni sitemaps.

## 2. Documentos leidos

- `registro-cambios-ejecutados.md`.
- `cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`.
- `diagnostico-MW-INDEXABILITY-REDIRECTS-PRODUCTS-PAGES-DIAG-011G7-2026-06-30.md`.
- Politica vigente `MW-INDEXABILITY-SAMPLES-POLICY-011B`.

Politica aplicable:

- Productos muestra confirmados: `noindex` por defecto.
- Paginas informativas de muestras: indexables.
- Excepciones: solo con evidencia.

## 3. Estado real en Shopify Admin

Consulta Admin GraphQL validada contra schema y ejecutada en modo lectura.

### Redirect

`VERIFICADO Y CORRECTO` como recurso existente, pero `INCORRECTO` por destino:

- `gid://shopify/UrlRedirect/412616229091`
- path: `/products/muestra-desnudos-blanco-y-negro`
- target: `/collections/muestras`

### Producto fuente

`VERIFICADO PERO MEJORABLE`

- ID: `gid://shopify/Product/8561719247075`
- titulo: `Muestra de Desnudos Blanco y negro`
- handle: `muestra-desnudos-blanco-y-negro`
- status: `DRAFT`
- publishedAt: `null`
- onlineStoreUrl: `null`
- productType: `Muestra`
- tags: `blanco`, `muestra-mural`, `negro`

Interpretacion:

- El producto existe en Admin, pero no esta publicado.
- No debe usarse como target publico.
- Encaja con la politica de no promover productos muestra como URLs indexables salvo evidencia.

### Target actual

`INCORRECTO`

- `/collections/muestras`
- No existe coleccion con handle `muestras`.
- Publicamente devuelve 404.
- No aparece en sitemap.

### Candidato vivo

`VERIFICADO Y CORRECTO`

- ID: `gid://shopify/Page/106299195619`
- titulo: `Solicita muestras de papel pintado`
- handle: `muestras`
- URL: `/pages/muestras`
- isPublished: `true`
- publishedAt: `2024-03-15T16:13:53Z`
- updatedAt: `2026-06-15T08:15:22Z`
- templateSuffix: `muestras-2`
- Publicamente devuelve 200.
- Aparece 1 vez en sitemap.

## 4. QA publico

| URL | Resultado | Estado |
|---|---|---|
| `/products/muestra-desnudos-blanco-y-negro` | `301 -> /collections/muestras -> 404` | `INCORRECTO` |
| `/collections/muestras` | `404` | `INCORRECTO` |
| `/pages/muestras` | `200` | `VERIFICADO Y CORRECTO` |

Sitemap:

- 29 ficheros revisados.
- 7.274 URLs `loc`.
- 0 errores.
- `/products/muestra-desnudos-blanco-y-negro`: 0 apariciones.
- `/collections/muestras`: 0 apariciones.
- `/pages/muestras`: 1 aparicion.

## 5. Decision tecnica

No se recomienda mantener el redirect actual porque envia a un 404.

No se recomienda repuntar al producto fuente porque esta en `DRAFT` y no tiene URL publica.

La opcion tecnica recomendada es repuntar el redirect a `/pages/muestras`, porque:

- es una pagina informativa publicada;
- aparece en sitemap;
- es coherente con la politica aprobada de muestras;
- resuelve el 301 -> 404 sin crear una URL de producto muestra indexable;
- preserva una experiencia util para posibles enlaces antiguos hacia esa muestra.

Riesgo:

- `/pages/muestras` es un destino generico, no la muestra exacta `Desnudos Blanco y negro`.
- Si Daniel considera que no debe preservarse ningun trafico de esa muestra concreta, la alternativa es eliminar el redirect y dejar 404 directo.

## 6. Lote recomendado para escritura

Nombre:

`MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-REPOINT-PAGE-011G7A1`

Alcance exacto:

- Recurso: `gid://shopify/UrlRedirect/412616229091`.
- Path: `/products/muestra-desnudos-blanco-y-negro`.
- Target actual: `/collections/muestras`.
- Target propuesto: `/pages/muestras`.

Operacion propuesta:

- Actualizar el redirect existente para que apunte a `/pages/muestras`.

Recursos e idiomas afectados:

- 1 redireccion ES.
- No afecta EN/FR/DE/NL.
- No modifica producto, pagina, coleccion, handle ni tema.

Respaldo:

- Valor actual documentado en `admin-MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-DECISION-011G7A-2026-06-30.csv`.

Metodo de reversion:

- Actualizar de nuevo el redirect a `/collections/muestras`, o eliminar el redirect si se decide no conservarlo.

Pruebas posteriores:

- Admin: `urlRedirect(id)` debe conservar path `/products/muestra-desnudos-blanco-y-negro` y target `/pages/muestras`.
- Publico: `/products/muestra-desnudos-blanco-y-negro` debe devolver `301 -> /pages/muestras -> 200`.
- Publico: `/pages/muestras` debe devolver 200.
- Sitemap: fuente antigua 0 apariciones; `/pages/muestras` 1 aparicion.

Autorizacion necesaria:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-REPOINT-PAGE-011G7A1`

## 7. Alternativa no recomendada salvo decision expresa

Lote alternativo:

`MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-CLEANUP-011G7A2`

Accion:

- Eliminar el redirect `gid://shopify/UrlRedirect/412616229091`.

Resultado esperado:

- `/products/muestra-desnudos-blanco-y-negro` devolveria 404 directo.

Esta opcion es mas limpia si el producto no debe tener sustituto, pero pierde una ruta util hacia la pagina informativa de muestras.

## 8. Evidencias generadas

- `admin-MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-DECISION-011G7A-2026-06-30.csv`.
- `qa-publico-MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-DECISION-011G7A-2026-06-30.csv`.

