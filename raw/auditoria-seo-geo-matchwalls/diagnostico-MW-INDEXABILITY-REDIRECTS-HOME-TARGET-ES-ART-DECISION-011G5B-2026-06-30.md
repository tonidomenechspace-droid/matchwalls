# MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-DECISION-011G5B

Fecha: 2026-06-30  
Tipo: diagnostico y decision de solo lectura  
Estado final: `REQUIERE DECISION HUMANA`

## 1. Alcance

Se revisan exclusivamente 4 redirecciones antiguas ES de lienzos/cuadros que actualmente apuntan a la home:

| ID | Path | Target actual |
|---|---|---|
| `gid://shopify/UrlRedirect/1518269596024` | `/collections/lienzos` | `/` |
| `gid://shopify/UrlRedirect/1518269628792` | `/collections/cuadros-rollos` | `/` |
| `gid://shopify/UrlRedirect/1518269661560` | `/collections/nuevos-cuadros-matchwalls` | `/` |
| `gid://shopify/UrlRedirect/1518269694328` | `/collections/nuevos-lienzos-matchwalls` | `/` |

No se han modificado redirecciones, paginas, colecciones, productos, handles, tema, traducciones ni sitemaps.

## 2. Documentos leidos

- `registro-cambios-ejecutados.md`.
- `cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`.
- `plan-operativo-vigente-y-cola-lotes-seo-geo-2026-06-30.md`.
- `diagnostico-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-DIAG-011G5-2026-06-30.md`.
- Evidencias 011G5/011G5A y busquedas locales de historico de lienzos/cuadros.

## 3. Estado real comprobado en Shopify Admin

Consulta GraphQL Admin validada contra schema y ejecutada en modo lectura.

Resultado:

- Las 4 redirecciones existen.
- Las 4 apuntan a `/`.
- El contador actual de redirecciones con `target:/` es 35, coherente con la limpieza ya ejecutada en 011G5A.
- No existen colecciones activas equivalentes encontradas para los handles revisados.
- Paginas candidatas:
  - `Page/106204954851`, handle `lienzos`, titulo `Todo sobre nuestros lienzos`, `isPublished=false`.
  - `Page/106205085923`, handle `crea-tu-lienzo`, titulo `Crea tu propio lienzo`, `isPublished=false`.
  - `Page/108605243619`, handle `envio-gratuito-internacional-lienzos`, titulo `Envio gratuito Internacional Lienzos`, `isPublished=true`.
- Producto encontrado relacionado con canvas:
  - `gid://shopify/Product/8558260420835`, `Muestra de Industrial Canvas Blanco`, estado `DRAFT`, no publicado en Online Store.

## 4. QA publico

| URL | Resultado publico | Interpretacion |
|---|---|---|
| `/collections/lienzos` | `301 -> / -> 200` | Redireccion a home; no equivalencia semantica demostrada |
| `/collections/cuadros-rollos` | `301 -> / -> 200` | Redireccion a home; no equivalencia semantica demostrada |
| `/collections/nuevos-cuadros-matchwalls` | `301 -> / -> 200` | Redireccion a home; no equivalencia semantica demostrada |
| `/collections/nuevos-lienzos-matchwalls` | `301 -> / -> 200` | Redireccion a home; no equivalencia semantica demostrada |
| `/pages/lienzos` | `404` | Pagina existe en Admin pero no esta publicada |
| `/pages/crea-tu-lienzo` | `404` | Pagina existe en Admin pero no esta publicada |
| `/pages/envio-gratuito-internacional-lienzos` | `200` | Pagina informativa de envio, no landing comercial equivalente |
| `/en/pages/free-international-shipping-canvases` | `200` | Pagina informativa EN, no landing comercial ES equivalente |
| `/collections/lienzos-abstractos` | `404` | No usable como target |
| `/collections/lienzos-artista` | `301 -> 404` | Cadena muerta relacionada, fuera de escritura 011G5B |
| `/pages/nuestros-productos` | `200` | Pagina general; demasiado amplia para sustituir colecciones de lienzos/cuadros |

Sitemaps:

- 29 ficheros sitemap revisados.
- 7.274 URLs `loc` leidas.
- 0 errores.
- 0 apariciones de las 4 colecciones antiguas.
- 0 apariciones de `/pages/lienzos` y `/pages/crea-tu-lienzo`.
- 1 aparicion de `/pages/envio-gratuito-internacional-lienzos`.
- 1 aparicion de `/en/pages/free-international-shipping-canvases`.

Enlaces internos visibles revisados en home y paginas candidatas:

- 0 enlaces encontrados hacia las 4 colecciones antiguas.
- 0 enlaces encontrados hacia `/pages/lienzos`.
- 0 enlaces encontrados hacia `/pages/crea-tu-lienzo`.

## 5. Decision tecnica

No hay evidencia suficiente para repuntar estas 4 redirecciones a un destino existente.

No se recomienda:

- mantenerlas hacia la home como solucion SEO estable;
- repuntarlas a paginas de envio;
- repuntarlas a paginas no publicadas;
- repuntarlas a una pagina corporativa generica;
- publicar paginas de lienzos solo para resolver redirects, sin decision comercial y editorial previa.

## 6. Opciones

### Opcion A recomendada si lienzos/cuadros no son linea comercial activa

Eliminar las 4 redirecciones para que las fuentes antiguas devuelvan 404 directo.

Motivo:

- No estan en sitemap.
- No hay enlaces internos visibles encontrados.
- No existe target comercial equivalente.
- Evita pasar senales antiguas a la home sin equivalencia semantica.

Lote propuesto:

`MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-CLEANUP-011G5B1`

Recursos a eliminar:

- `gid://shopify/UrlRedirect/1518269596024`.
- `gid://shopify/UrlRedirect/1518269628792`.
- `gid://shopify/UrlRedirect/1518269661560`.
- `gid://shopify/UrlRedirect/1518269694328`.

Valores actuales:

- Todos: target `/`.

Valores propuestos:

- Eliminar los 4 redirects.

Riesgos:

- Si estas URLs reciben enlaces externos con valor, pasaran a 404.
- Si Daniel quiere recuperar la linea lienzos/cuadros, eliminar ahora obliga a crear una nueva estrategia de landing antes de recuperar redirecciones.

Respaldo:

- IDs, paths y targets quedan documentados en `admin-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-DECISION-011G5B-2026-06-30.csv`.

Reversion:

- Recrear los 4 redirects con los mismos paths y target `/`, o con un nuevo target canonico aprobado.

Pruebas posteriores:

- Admin: `urlRedirect(id)` debe devolver `null` para los 4 IDs eliminados.
- Admin: `urlRedirectsCount(query:"target:/")` debe bajar de 35 a 31.
- Publico: las 4 fuentes deben devolver 404 directo, sin 301 a home.
- Sitemap: 0 apariciones de las 4 URLs.

Autorizacion necesaria:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-CLEANUP-011G5B1`

### Opcion B si lienzos/cuadros siguen siendo linea comercial activa

No tocar los redirects todavia.

Crear primero una landing comercial canonica y multilingue, o publicar/reconstruir una pagina existente, con:

- objetivo comercial claro;
- H1, meta title, meta description y contenido visible coherentes;
- enlaces internos;
- decision de indexabilidad;
- equivalencias EN/FR/DE/NL si aplica.

Solo despues se debe proponer un lote de repunte de redirects.

Estado recomendado hasta entonces: `STANDBY` o `REQUIERE DECISION HUMANA`.

## 7. Evidencias generadas

- `admin-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-DECISION-011G5B-2026-06-30.csv`.
- `qa-publico-candidatos-MW-INDEXABILITY-REDIRECTS-HOME-TARGET-ES-ART-DECISION-011G5B-2026-06-30.csv`.

