# Ejecución lote MW-FOOTER-I18N-001 - 2026-06-17

Estado: EJECUCIÓN PARCIAL EN QA - NO PUBLICADO

## Aprobación

Daniel aprobó literalmente:

`APROBADO LOTE MW-FOOTER-I18N-001`

## Alcance ejecutado

Se ejecutó solo la parte segura y reversible del lote:

1. Respaldo de estado actual.
2. Duplicado del tema MAIN a un tema QA no publicado.
3. Corrección de `sections/footer-group.json` en el tema QA.
4. Lectura posterior del archivo guardado.
5. Comprobación de que el MAIN no cambió.

No se modificaron:

- tema MAIN;
- publicación de temas;
- menús globales;
- traducciones EN, FR, DE o NL;
- URLs;
- handles;
- redirecciones;
- productos;
- colecciones;
- páginas;
- inventario;
- precios;
- App Embeds;
- Liquid de producción.

## Tema MAIN verificado

- Nombre: `SEO schema hotfix - 2026-06-15`
- ID: `gid://shopify/OnlineStoreTheme/178383749496`
- Rol: `MAIN`
- `processing`: `false`
- `processingFailed`: `false`

Archivos clave después de la ejecución:

| Archivo | Checksum MD5 | Tamaño | Actualizado |
| --- | --- | ---: | --- |
| `config/settings_data.json` | `a1192f2f698d277e0f69f7156a61a90c` | `10256` | `2026-06-15T12:34:14Z` |
| `sections/footer-group.json` | `e93af9228c8a97dce4ad91e203bf7e75` | `4210` | `2026-06-15T12:34:21Z` |
| `sections/header-group.json` | `671e993b0001e876d7a1bc51d8ccd44d` | `6939` | `2026-06-15T12:34:21Z` |
| `snippets/microdata-schema.liquid` | `58417e4825aa3d4570a6646f292aaedc` | `10787` | `2026-06-15T20:19:10Z` |

Resultado: MAIN intacto.

## Tema QA creado

Mutación ejecutada:

- `themeDuplicate`

Origen:

- `gid://shopify/OnlineStoreTheme/178383749496`

Tema creado:

- Nombre: `MW-FOOTER-I18N-001 - QA - 2026-06-17`
- ID: `gid://shopify/OnlineStoreTheme/178390401400`
- Rol: `UNPUBLISHED`
- Resultado de duplicado: `userErrors: []`
- Estado final: `processing=false`, `processingFailed=false`

El tema QA quedó alineado con MAIN en archivos clave antes de la edición:

| Archivo | Checksum MD5 |
| --- | --- |
| `config/settings_data.json` | `a1192f2f698d277e0f69f7156a61a90c` |
| `sections/footer-group.json` | `e93af9228c8a97dce4ad91e203bf7e75` |
| `sections/header-group.json` | `671e993b0001e876d7a1bc51d8ccd44d` |
| `snippets/microdata-schema.liquid` | `58417e4825aa3d4570a6646f292aaedc` |

## Archivo modificado en QA

Mutación ejecutada:

- `themeFilesUpsert`

Tema afectado:

- `gid://shopify/OnlineStoreTheme/178390401400`

Archivo afectado:

- `sections/footer-group.json`

Resultado:

- `userErrors: []`
- Checksum nuevo QA: `17271d0b6b69bdcb1e430bec9e061943`
- Tamaño nuevo QA: `6709`
- Actualizado: `2026-06-17T08:19:11Z`

## Valores modificados en QA

### Newsletter superior

Antes:

`<p>¡Suscríbete a nuestras noticias! Se el primero en enterarte de las últimas tendencias, novedades de nuestros papeles pintados y art prints además de divertidos tips que te ayudarán a decorar tu espacio particular o residencial. #BeMatchWalls</p>`

Después:

`<p>¡Suscríbete a nuestras noticias! Sé la primera persona en conocer las últimas tendencias, novedades de nuestros papeles pintados y art prints, además de consejos útiles para decorar tu espacio. #BeMatchWalls</p>`

### Bloques de confianza

| Bloque | Antes | Después |
| --- | --- | --- |
| Envío | `Envío gratuito` / `Worldwide.` | `Envío internacional` / `Consulta los plazos y condiciones de envío disponibles para tu país.` |
| Pago | `Pago seguro` / `Metodos de pago seguros y financiación.` | `Pagos seguros` / `Consulta los métodos de pago disponibles en la pantalla de pago.` |
| Garantía | `Garantía de satisfacción` / `Nuestro compromiso tu tranquilidad.` | `Atención y soporte` / `Te ayudamos antes y después de tu pedido.` |
| Personalización | `Personalización` / `Te ayudamos a crear tu diseño Matchwalls.` | `Personalización` / `Te orientamos para adaptar tu diseño a medida.` |
| Instalación | `Fácil instalación` / `Descargate nuestras guías de fácil instlacióon.` | `Guías de instalación` / `Consulta nuestras guías antes de instalar tu papel pintado o mural.` |

## Verificación posterior

Lectura de vuelta vía Shopify Admin:

- Tema QA leído correctamente.
- Archivo `sections/footer-group.json` leído correctamente.
- Textos nuevos presentes en el archivo QA.
- Checksum QA nuevo confirmado: `17271d0b6b69bdcb1e430bec9e061943`.
- MAIN sigue con checksum original `e93af9228c8a97dce4ad91e203bf7e75`.

## QA pública

Intentos:

- `https://www.matchwalls.com/?preview_theme_id=178390401400`
- `https://matchwalls.myshopify.com/?preview_theme_id=178390401400`

Resultado:

- La navegación termina en `https://www.matchwalls.com/`.
- El DOM público leído corresponde al tema vivo, no al tema QA.
- El footer público sigue mostrando valores antiguos de menús globales como `FAQ´S`, `Black Friday 2024` y `espacios púbicos`.

Clasificación:

- QA por Admin GraphQL: `CORREGIDO Y VERIFICADO` para el archivo QA almacenado.
- QA pública de preview: `NO ACCESIBLE`.
- Estado del sitio publicado: `INCOMPLETO`.

## Menús y traducciones

No se modificaron menús porque son recursos globales de tienda y no se pueden validar en un tema QA sin impacto en el sitio vivo.

No se registraron traducciones EN/FR/DE/NL porque Shopify devuelve las traducciones de tema como una lista amplia sin filtro directo por clave. Se requiere inventario exacto de claves y `digest` antes de cualquier escritura con `translationsRegister`.

## Reversión

Como el cambio está solo en tema QA no publicado, la reversión inmediata consiste en:

1. No publicar el tema QA.
2. Restaurar en el QA el `sections/footer-group.json` original desde `respaldo-MW-FOOTER-I18N-001-2026-06-17.md`, si se quiere conservar el QA limpio.
3. O eliminar manualmente el tema QA desde Shopify Admin si Daniel decide descartarlo.

No hay reversión necesaria en el tema MAIN porque no fue modificado.

## Estado final

- Tema QA creado: `CORREGIDO Y VERIFICADO` a nivel de almacenamiento Shopify Admin.
- Sitio público: `INCOMPLETO`.
- Menús globales: `INCORRECTO`.
- Traducciones EN/FR/DE/NL del footer: `INCOMPLETO`.
- Publicación: `NO EJECUTADA`.

Siguiente decisión necesaria:

- Definir si el siguiente paso será:
  - inventario técnico de claves/digest de traducción de footer;
  - propuesta cerrada de menús globales;
  - o QA manual desde el editor/preview autenticado de Shopify antes de publicar.
