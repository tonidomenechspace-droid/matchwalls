# MW-INDEXABILITY-REDIRECTS-PRODUCTS-PAGES-DIAG-011G7

Fecha: 2026-06-30  
Tipo: diagnostico de solo lectura  
Estado final: `VERIFICADO PERO MEJORABLE`

## 1. Alcance

Diagnostico actual de redirecciones Shopify restantes con fuente:

- `/products/*`
- `/pages/*`
- `/collections/*`

No se han modificado redirecciones, productos, paginas, colecciones, handles, tema, traducciones, canonicals ni sitemaps.

## 2. Documentos leidos

- `registro-cambios-ejecutados.md`.
- `cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`.
- `plan-operativo-vigente-y-cola-lotes-seo-geo-2026-06-30.md`.
- `diagnostico-MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G-2026-06-29.md`.
- `diagnostico-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3-2026-06-29.md`.
- `ejecucion-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-CLEANUP-011G3A-2026-06-29.md`.
- `ejecucion-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-CLEANUP-011G5A-2026-06-30.md`.
- `ejecucion-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-CLEANUP-011G5B1-2026-06-30.md`.

## 3. Estado Admin Shopify comprobado

Consulta GraphQL Admin validada contra schema y ejecutada en modo lectura.

Conteos actuales:

| Bloque | Conteo |
|---|---:|
| Total redirects Shopify | 609 |
| `path:/products/*` | 18 |
| `path:/pages/*` | 3 |
| `path:/collections/*` | 37 |
| `target:/` | 31 |

Interpretacion:

- El conteo refleja las limpiezas ya ejecutadas: 011G1, 011G3A, 011G5A y 011G5B1.
- Los numeros historicos de 011G ya no deben reutilizarse sin recalculo.

## 4. QA publico y sitemap

QA publico:

- Alcance comprobado: 58 redirects.
- 58/58 fuentes tienen `source_first = 301`.
- Sitemaps actuales: 29 ficheros, 7.274 URLs `loc`, 0 errores.
- 0/58 fuentes aparecen en sitemap.

Limitacion:

- En la carga masiva de colecciones, varias URLs finales devolvieron temporalmente `429 / Verifying your connection...`.
- Para no sobreinterpretar esos 429, la clasificacion usa:
  - primer estado HTTP sin seguir redireccion;
  - presencia exacta en sitemap;
  - existencia de recurso en Admin para targets candidatos a 404.

## 5. Clasificacion

| Grupo | Conteo | Estado | Decision |
|---|---:|---|---|
| Productos con target 200 | 17 | `VERIFICADO PERO MEJORABLE` | Conservar sin escritura |
| Producto muestra con target 404 | 1 | `REQUIERE DECISION HUMANA` | Resolver en sublote de muestras |
| Paginas con target 200 | 3 | `VERIFICADO Y CORRECTO` | Conservar |
| Colecciones con target 200 | 31 | `VERIFICADO PERO MEJORABLE` | Conservar por ahora |
| Coleccion con cadena | 1 | `INCORRECTO` | Consolidar si se aprueba |
| Colecciones con target 404 | 5 | `INCORRECTO` | Decidir eliminar o repuntar con equivalencia aprobada |

## 6. Hallazgos criticos

### 6.1 Producto muestra hacia target 404

Redirect:

- `gid://shopify/UrlRedirect/412616229091`
- `/products/muestra-desnudos-blanco-y-negro -> /collections/muestras`

Evidencia:

- Fuente: 301.
- Target: 404.
- La fuente existe en Admin como producto `DRAFT`: `gid://shopify/Product/8561719247075`.
- Target `/collections/muestras` no existe por handle comprobado.
- Fuente y target no aparecen en sitemap.

Estado: `REQUIERE DECISION HUMANA`.

No se recomienda repuntar automaticamente porque afecta a la politica de muestras.

### 6.2 Colecciones hacia target 404

Redirects:

| ID | Path | Target |
|---|---|---|
| `gid://shopify/UrlRedirect/405254897891` | `/collections/kids` | `/collections/kids-rollos` |
| `gid://shopify/UrlRedirect/408478843107` | `/collections/patrones-grandes-rollos` | `/collections/papel-pintado-estampado-grande` |
| `gid://shopify/UrlRedirect/408478974179` | `/collections/semi-lisos-rollos` | `/collections/semi-lisos-papel-pintado` |
| `gid://shopify/UrlRedirect/408479006947` | `/collections/moderno-rollos` | `/collections/moderno-papel-pintado` |
| `gid://shopify/UrlRedirect/408719425763` | `/collections/lienzos-artista` | `/collections/lienzos-abstractos` |

Evidencia:

- Targets devuelven 404.
- Handles target no aparecen como colecciones existentes en Admin.
- Fuentes y targets no aparecen en sitemap.

Candidatos vivos encontrados, no aprobados:

- Para `kids`, existe `/collections/kids-murales`.
- Para patrones pequenos, existe `/collections/papel-pintado-estampados-pequenos`, pero no es equivalente demostrado para `patrones-grandes-rollos`.
- No hay candidato claro encontrado para semi-lisos, moderno ni lienzos.

Estado: `INCORRECTO`.

No se recomienda repuntar sin mapa semantico aprobado.

### 6.3 Cadena de redireccion

Redirect:

- `gid://shopify/UrlRedirect/408478908643`
- `/collections/rayas-rollos -> /collections/papel-pintado-rayas`

Cadena publica:

- `/collections/rayas-rollos`
- `/collections/papel-pintado-rayas`
- `/collections/murales-estilo-a-rayas`

Destino final:

- `/collections/murales-estilo-a-rayas`
- Admin: `gid://shopify/Collection/439174496483`
- Titulo: `Papel Pintado Rayas`
- Productos: 87

Estado: `INCORRECTO`.

Recomendacion: si se aprueba, consolidar el primer redirect para apuntar directamente a `/collections/murales-estilo-a-rayas`.

## 7. No accion inmediata

Los siguientes grupos no requieren escritura inmediata:

- 17 redirects de producto con target 200.
- 3 redirects de pagina con target 200.
- 31 redirects de coleccion con target 200.

Motivo:

- Las fuentes no estan en sitemap.
- Los targets viven o aparecen como canonicos actuales.
- Cambiarlos sin un mapa comercial/editorial puede crear mas riesgo que beneficio.

## 8. Lotes derivados recomendados

1. `MW-INDEXABILITY-REDIRECTS-SAMPLE-DEAD-TARGET-DECISION-011G7A`
   - Tipo: decision/diagnostico.
   - Objetivo: decidir que hacer con `/products/muestra-desnudos-blanco-y-negro -> /collections/muestras`.
   - No ejecutar escritura hasta decidir politica exacta.

2. `MW-INDEXABILITY-REDIRECTS-COLLECTIONS-DEAD-TARGETS-DECISION-011G7B`
   - Tipo: decision/diagnostico.
   - Objetivo: decidir si las 5 colecciones con target 404 se eliminan o se repuntan a equivalencias reales.

3. `MW-INDEXABILITY-REDIRECTS-COLLECTIONS-CHAIN-RAYAS-011G7C`
   - Tipo: escritura Shopify acotada si se aprueba.
   - Objetivo: consolidar `/collections/rayas-rollos` directamente hacia `/collections/murales-estilo-a-rayas`.

## 9. Evidencias

- `admin-redirects-MW-INDEXABILITY-REDIRECTS-PRODUCTS-PAGES-DIAG-011G7-2026-06-30.csv`.
- `qa-publico-MW-INDEXABILITY-REDIRECTS-PRODUCTS-PAGES-DIAG-011G7-2026-06-30.csv`.
- `clasificacion-MW-INDEXABILITY-REDIRECTS-PRODUCTS-PAGES-DIAG-011G7-2026-06-30.csv`.

