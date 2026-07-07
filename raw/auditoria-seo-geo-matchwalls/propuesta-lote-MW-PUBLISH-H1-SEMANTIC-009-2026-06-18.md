# Propuesta de lote — MW-PUBLISH-H1-SEMANTIC-009

Fecha: 18 de junio de 2026.

Estado: `CORREGIDO Y VERIFICADO`.

Publicación ejecutada manualmente tras aprobación exacta: sí.

## 1. Nombre y alcance exacto

Publicar como MAIN el tema aislado `178396463480`, sin editar archivos antes o
durante la publicación. Conservar el MAIN actual `178383749496` como reversión
inmediata y repetir las 170 comprobaciones del lote aislado.

Quedan excluidos: JavaScript global, error NL, overflow FR/NL, CSS visible,
contenido, traducciones, handles, redirecciones, indexación, inventario, precios,
imágenes, App Embeds y LangShop.

## 2. Recursos, IDs, URLs e idiomas afectados

### Temas

- MAIN actual: `gid://shopify/OnlineStoreTheme/178383749496` —
  `SEO schema hotfix - 2026-06-15`.
- Candidato: `gid://shopify/OnlineStoreTheme/178396463480` —
  `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.

### Páginas y plantillas

| Recurso | Page ID | Plantilla |
| --- | --- | --- |
| Murales | `106204922083` | `templates/page.murales.json` |
| Crea tu mural | `106205118691` | `templates/page.crea-tu-mural.json` |
| Crea tu papel | `106205151459` | `templates/page.crea-tu-papel-pintado-2.json` |
| Social/prensa | `106205216995` | `templates/page.social_prensa_afiliacion.json` |
| Artistas | `106205315299` | `templates/page.artistas.json` |
| Medidas paredes | `106229170403` | `templates/page.como-tomar-medidas.json` |
| Medidas techo | `106229203171` | `templates/page.como-medir-el-techo.json` |
| Sobre nosotros | `106231464163` | `templates/page.sobre-nosotros.json` |
| Nuestros productos | `106278256867` | `templates/page.nuestros-productos.json` |
| Métodos de pago | `106278387939` | `templates/page.metodos-de-pago.json` |
| Envíos | `106278420707` | `templates/page.envios-y-devoluciones.json` |
| Estudios profesionales | `106279141603` | `templates/page.estudios-profesionales.json` |
| Muestras | `106299195619` | `templates/page.muestras-2.json` |
| Formulario profesional | `107014947043` | `templates/page.formulario-profesionales.json` |
| Guía de instalación | `107326210275` | `templates/page.guias-de-instalacion.json` |
| Tarjeta regalo | `107793481955` | `templates/page.tarjeta-regalo.json` |
| Formulario particulares | `108429672675` | `templates/page.formulario-particulares.json` |

Idiomas: ES, EN, FR, DE y NL.

Las 85 combinaciones exactas página/idioma están en
`matriz-lote-MW-THEME-PAGE-H1-SEMANTIC-008E-ISOLATED-QA-2026-06-18.csv`.
No se crearán URLs nuevas.

## 3. Valores actuales

`VERIFICADO Y CORRECTO`

- `178383749496`: `MAIN`, sin fallo de procesamiento.
- `178396463480`: `UNPUBLISHED`, sin fallo de procesamiento.
- Los 17 checksums de ambos temas coinciden con el registro del lote aislado.
- El candidato contiene las 17 diferencias funcionales autorizadas.
- En el QA aislado coincidían `config/settings_data.json`,
  `layout/theme.liquid` y `sections/footer-group.json`.

## 4. Valores propuestos

- `178396463480`: de `UNPUBLISHED` a `MAIN`.
- `178383749496`: de `MAIN` a `UNPUBLISHED`, conservado intacto.
- Archivos, contenido y configuración: sin modificaciones.

## 5. Evidencia y motivo técnico

`CORREGIDO Y VERIFICADO`

- 85 comprobaciones de escritorio y 85 móviles sobre el candidato.
- En 170/170: tema correcto, un H1 no vacío, canonical self, hreflang
  ES/EN/FR/DE/NL, `html lang` correcto, sin `noindex` accidental, contenido
  principal no vacío y sin error Shopify.
- App Embeds y scripts observados coincidieron con MAIN tras carga dinámica.
- La lectura Shopify de esta sesión confirmó roles y los 17 checksums.

Motivo: publicar una corrección semántica ya aislada y probada sin mezclarla con
la deuda técnica preexistente.

## 6. Riesgos y efectos secundarios

Riesgo alto por tratarse de un cambio global de tema.

- La publicación afecta todo el storefront, no solo las 17 URLs.
- Apps o configuración externa podrían haber cambiado después del QA.
- Los errores globales preexistentes seguirán presentes.
- Deben probarse home, producto, colección, carrito y formularios.
- Si la conexión no permite publicar, Daniel deberá realizar la publicación
  manual del tema aprobado en Shopify Admin.

## 7. Respaldo disponible

`VERIFICADO Y CORRECTO`

- MAIN completo `178383749496`.
- `backups/MW-THEME-PAGE-H1-SEMANTIC-008E-2026-06-17`.
- `backups/MW-THEME-PAGE-H1-SEMANTIC-008E-2026-06-18-batch-pages`.
- Matriz de checksums MAIN/candidato registrada.

## 8. Método exacto de reversión

1. Volver a publicar `178383749496`.
2. Confirmar que recupera el rol `MAIN` y no presenta fallo de procesamiento.
3. Probar home, producto, colección, carrito, formularios y una página afectada
   en ES/EN/FR/DE/NL, escritorio y móvil.
4. Mantener `178396463480` sin publicar para diagnóstico.
5. Registrar hora, causa, pruebas y resultado.

## 9. Pruebas posteriores

### Antes de publicar

- Revalidar roles, procesamiento y 17 checksums.
- Confirmar que el candidato no contiene cambios no autorizados.
- Confirmar disponibilidad del MAIN anterior para reversión.
- Smoke test del preview y rutas críticas.

### Inmediatamente después

- Repetir 85 URLs en escritorio y las mismas 85 en móvil.
- Verificar tema servido, status, H1, canonical, hreflang, `html lang`, robots,
  contenido principal y errores Shopify.
- Comprobar home, producto, colección, carrito, formularios y App Embeds.
- Distinguir incidencias preexistentes de regresiones nuevas.

Fallo crítico: H1 ausente/duplicado, `noindex` accidental, canonical/hreflang
incorrecto, página vacía/error, carrito o formulario roto, tema equivocado o
regresión global. Cualquier fallo crítico activa reversión.

## Aprobación recibida

Aprobación exacta recibida y consumida para este lote:

`APROBADO LOTE MW-PUBLISH-H1-SEMANTIC-009`

El resultado post-publicación se documenta en
`qa-post-publicacion-MW-PUBLISH-H1-SEMANTIC-009-2026-06-18.md`.
