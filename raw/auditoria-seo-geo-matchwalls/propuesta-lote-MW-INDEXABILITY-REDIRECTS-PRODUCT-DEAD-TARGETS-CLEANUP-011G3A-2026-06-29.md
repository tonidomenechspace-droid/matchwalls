# Propuesta de lote: MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-CLEANUP-011G3A

Fecha: 2026-06-29  
Estado: REQUIERE DECISION HUMANA  
Tipo: propuesta de escritura acotada en Shopify Admin  

## 1. Alcance exacto propuesto

Eliminar exclusivamente 6 redirecciones de producto cuyo destino final esta verificado como 404.

No se propone:

- Cambiar productos.
- Cambiar handles.
- Crear nuevas redirecciones comerciales.
- Modificar colecciones.
- Modificar paginas.
- Modificar sitemaps.
- Modificar tema Shopify.
- Modificar la redireccion de muestra que queda en STANDBY.

## 2. Estado real comprobado antes de propuesta

Comprobacion Admin de solo lectura realizada el 2026-06-29:

- Total de redirecciones Shopify: 620 EXACT.
- Los 6 redirects candidatos siguen existiendo en Shopify Admin.
- El redirect de muestra `/products/muestra-desnudos-blanco-y-negro` -> `/collections/muestras` sigue existiendo y queda excluido.

## 3. Recursos afectados

| ID Shopify | Path actual | Target actual | Estado actual | Valor propuesto |
|---|---|---|---|---|
| `gid://shopify/UrlRedirect/408237834467` | `/products/poster-de-papel-mate-calidad-museo-con-marco-de-madera` | `/products/echoing-corridor-3` | INCORRECTO | Eliminar redirect |
| `gid://shopify/UrlRedirect/408370151651` | `/products/endless-horizon-3` | `/products/echoing-corridor` | INCORRECTO | Eliminar redirect |
| `gid://shopify/UrlRedirect/408474484963` | `/products/rusted-horizon-marron-copia` | `/products/ember-glow-marron` | INCORRECTO | Eliminar redirect |
| `gid://shopify/UrlRedirect/408525930723` | `/products/urban-geometrico` | `/products/urban-geometrico-beige` | INCORRECTO | Eliminar redirect |
| `gid://shopify/UrlRedirect/408525996259` | `/products/urban-geometrico-beige-copia` | `/products/urban-geometrico-gris` | INCORRECTO | Eliminar redirect |
| `gid://shopify/UrlRedirect/408514429155` | `/products/urban-sketch-beige-copia` | `/products/melodic-flow` | INCORRECTO | Eliminar redirect |

## 4. Recurso excluido expresamente

| ID Shopify | Path actual | Target actual | Motivo de exclusion |
|---|---|---|---|
| `gid://shopify/UrlRedirect/412616229091` | `/products/muestra-desnudos-blanco-y-negro` | `/collections/muestras` | STANDBY. El producto fuente existe como DRAFT y afecta a la politica de muestras. Requiere decision separada. |

## 5. Evidencia usada

Archivos de soporte:

- `diagnostico-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3-2026-06-29.md`
- `clasificacion-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3-2026-06-29.csv`
- `admin-redirects-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3-2026-06-29.csv`
- `admin-resource-existence-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3-2026-06-29.csv`
- `qa-publico-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3-2026-06-29.csv`
- `qa-sitemap-exact-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-DIAG-011G3-2026-06-29.csv`
- `backup-pre-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-CLEANUP-011G3A-2026-06-29.csv`

Hallazgo resumido:

- Las 6 URLs fuente no estan en sitemap.
- Los 6 targets no estan en sitemap.
- Las 6 redirecciones llevan a destinos 404.
- No se ha verificado una pagina comercial equivalente que justifique repuntar estas redirecciones.

## 6. Motivo tecnico

Estas redirecciones no recuperan autoridad ni usuarios hacia una URL valida. Actualmente convierten una URL antigua en una cadena de navegacion negativa: `301 -> 404`.

La limpieza propuesta evita que Shopify mantenga reglas obsoletas hacia destinos muertos. Tras la eliminacion, esas URLs antiguas pasarian previsiblemente a responder 404 directo, sin salto intermedio.

## 7. Riesgos y efectos secundarios

Riesgo principal:

- Las 6 URLs antiguas dejaran de hacer 301 y pasaran previsiblemente a 404 directo.

Evaluacion:

- RIESGO CONTROLADO, porque actualmente ya terminan en 404.
- No se ha encontrado exposicion en sitemap para fuentes ni targets.
- Si Daniel conoce una URL comercial equivalente real para alguna de estas rutas, debe indicarse antes de aprobar este lote; en ese caso no se eliminaria, se prepararia un lote de repuntado especifico.

## 8. Respaldo disponible

Backup previo preparado:

`backup-pre-MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-CLEANUP-011G3A-2026-06-29.csv`

Contiene:

- ID original.
- Path original.
- Target original.

## 9. Metodo exacto de ejecucion si se aprueba

Ejecutar eliminacion secuencial con `urlRedirectDelete`, una redireccion cada vez.

Orden:

1. `gid://shopify/UrlRedirect/408237834467`
2. `gid://shopify/UrlRedirect/408370151651`
3. `gid://shopify/UrlRedirect/408474484963`
4. `gid://shopify/UrlRedirect/408525930723`
5. `gid://shopify/UrlRedirect/408525996259`
6. `gid://shopify/UrlRedirect/408514429155`

Condicion de parada:

- Si Shopify devuelve cualquier `userErrors`, detener ejecucion y no continuar con el resto.

## 10. Metodo exacto de reversion

Si es necesario revertir, recrear cada redirect con `urlRedirectCreate` usando el backup:

- Mismo `path`.
- Mismo `target`.

Nota:

- Shopify puede asignar IDs nuevos tras recrear las redirecciones. La reversion funcional se verificaria por `path` y `target`, no por conservar el mismo ID.

## 11. Pruebas posteriores obligatorias

Admin:

- Confirmar que los 6 IDs eliminados devuelven `null`.
- Confirmar que cada `path` eliminado tiene conteo 0 en redirects.
- Confirmar total esperado de redirects: 614 EXACT, salvo cambios externos simultaneos.
- Confirmar que `gid://shopify/UrlRedirect/412616229091` sigue existiendo y no se ha tocado.

Publico:

- Verificar que las 6 URLs fuente ya no hacen `301 -> 404`.
- Verificar respuesta esperada 404 directa o comportamiento equivalente sin redireccion muerta.
- Verificar que los targets siguen fuera de sitemap.
- Verificar que las fuentes siguen fuera de sitemap.

Registro:

- Actualizar `registro-cambios-ejecutados.md` con resultado, evidencias, incidencias y metodo de reversion.

## 12. Frase exacta necesaria para ejecutar

Para autorizar la escritura en Shopify, Daniel debe responder exactamente:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-PRODUCT-DEAD-TARGETS-CLEANUP-011G3A`

