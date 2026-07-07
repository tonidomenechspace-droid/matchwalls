# QA MW-QA-HOTFIX-001 - SEO schema hotfix

Fecha: 16 de junio de 2026

## Alcance autorizado

Lote aprobado por Daniel: `APROBADO LOTE MW-QA-HOTFIX-001`.

Alcance ejecutado exclusivamente en modo lectura:

- Comparacion MAIN vs `SEO schema hotfix - 2026-06-15`.
- Validacion de schema en home, productos, articulos, carrito y formularios.
- Revision ES, EN, FR, DE y NL.
- QA escritorio y movil.
- Verificacion de App Embeds por checksum y contenido de `config/settings_data.json`.

No se publico, modifico, renombro ni escribio nada en Shopify.

## Temas verificados

| Tema | ID | Rol | Estado |
|---|---|---|---|
| Production - SEO fix AggregateRating (2026-06-12) | `gid://shopify/OnlineStoreTheme/178379293048` | MAIN | `VERIFICADO Y CORRECTO` |
| SEO schema hotfix - 2026-06-15 | `gid://shopify/OnlineStoreTheme/178383749496` | UNPUBLISHED | `VERIFICADO Y CORRECTO` |

Ambos temas estaban sin procesamiento pendiente.

## Diferencias MAIN vs hotfix

| Archivo | Resultado |
|---|---|
| `snippets/microdata-schema.liquid` | Diferencia intencionada y validada. |
| `snippets/microdata-schema-original.liquid` | Archivo auxiliar adicional; copia exacta del schema MAIN. |
| `assets/country-flags.css` | Checksum distinto, pero semantica identica tras normalizar ID de tema y version CDN. |
| `assets/sections.js` | Checksum distinto, pero semantica identica tras normalizar ID de tema y version CDN. |
| `assets/theme.js` | Checksum distinto, pero semantica identica tras normalizar ID de tema y version CDN. |

Evidencia de normalizacion:

| Archivo compilado | MAIN | Hotfix | Resultado |
|---|---:|---:|---|
| `country-flags.css` | 14.451 caracteres | 14.451 caracteres | `VERIFICADO Y CORRECTO` |
| `sections.js` | 45.779 caracteres | 45.515 caracteres | `VERIFICADO Y CORRECTO` |
| `theme.js` | 148.813 caracteres | 148.813 caracteres | `VERIFICADO Y CORRECTO` |

Tras normalizar `/cdn/shop/t/[id]/` y `?v=[version]`, los tres archivos son equivalentes. No se detecto logica inesperada adicional.

## Schema validado

### Home

Probado en ES, EN, FR, DE y NL.

- JSON-LD parseable: `VERIFICADO Y CORRECTO`.
- Tipos presentes: `BreadcrumbList`, `WebSite`, `Organization`, `SearchAction`.
- `AggregateRating` corporativo fijo: 0 en hotfix.
- H1: 1 por home.
- Hreflang/canonical: presentes en las paginas revisadas.

### Producto

Producto principal probado:

- ES: `https://www.matchwalls.com/products/whispering-woods-azul`
- EN: `https://www.matchwalls.com/en/products/whispering-woods-blue`
- FR: `https://www.matchwalls.com/fr/products/whispering-woods-bleu`
- DE: `https://www.matchwalls.com/de/products/whispering-woods-blau`
- NL: `https://www.matchwalls.com/nl/products/whispering-woods-blauw`

Producto personalizado probado:

- `https://www.matchwalls.com/products/custom-file-uploader`

Resultado:

- `Product`: presente y parseable.
- `Brand`: presente.
- `ImageObject`: presente.
- `QuantitativeValue`: presente.
- `Offer`: 4 ofertas por producto probado.
- Cada `Offer` conserva nombre, disponibilidad, precio, moneda, URL y SKU.
- GTIN falsos: 0.
- MPN falsos: 0.
- H1: 1.

Estado: `VERIFICADO Y CORRECTO`.

### Articulo

Articulo probado en ES, EN, FR, DE y NL:

- ES: `https://www.matchwalls.com/blogs/inspiracion/aprende-a-empapelar-paredes-y-techos-con-calidades-non-woven-vinilicas-y-peel-and-stick`
- EN: `https://www.matchwalls.com/en/blogs/inspiration/learn-how-to-wallpaper-walls-and-ceilings-with-non-woven-vinyl-and-peel-and-stick-types`
- FR: `https://www.matchwalls.com/fr/blogs/inspiration-2/apprenez-a-tapisser-les-murs-et-plafonds-avec-les-qualites-non-tissees-vinyles-et-peel-and-stick`
- DE: `https://www.matchwalls.com/de/blogs/inspiration-1/lernen-sie-tapetenwande-und-dacher-mit-nicht-gewebten-vinyl-und-peel-und-stick-qualitaten`
- NL: `https://www.matchwalls.com/nl/blogs/inspiratie/leer-behangwanden-en-daken-met-niet-geweven-vinyl-en-peel-en-stokkwaliteiten`

Resultado:

- `BlogPosting`: presente y parseable en los cinco idiomas.
- `BreadcrumbList`: presente.
- El tercer breadcrumb usa el titulo real del articulo.
- JSON-LD sin errores de parseo.

Estado: `VERIFICADO Y CORRECTO`.

## QA escritorio y movil

Matriz hotfix revisada:

- Homes ES, EN, FR, DE, NL.
- Productos ES, EN, FR, DE, NL.
- Articulos ES, EN, FR, DE, NL.
- Carrito ES.
- Contacto ES.
- Formulario particulares ES.
- Producto personalizado ES.

Resultados:

- Todas las paginas revisadas cargan desde el tema preview `t/43`.
- No se detectaron errores JSON-LD.
- No se detectaron GTIN/MPN falsos en productos.
- Formularios renderizan y mantienen campos.
- Carrito renderiza sin error JSON-LD.
- Contraste MAIN vs hotfix en escritorio y movil: sin cambios de H1, formularios, ofertas ni estructura funcional, salvo las correcciones esperadas de schema.

Incidencias no bloqueantes y previas al hotfix:

- Carrito y formulario de particulares no tienen H1.
- Algunos productos en movil mantienen desbordamiento horizontal pequeno, tambien observado en MAIN.
- Las traducciones deficientes DE/NL documentadas previamente siguen fuera del alcance de este hotfix.

Estado: `VERIFICADO PERO MEJORABLE`.

## App Embeds

`config/settings_data.json`:

- MAIN checksum: `a1192f2f698d277e0f69f7156a61a90c`.
- Hotfix checksum: `a1192f2f698d277e0f69f7156a61a90c`.

Bloques app embed activos coincidentes:

- Instafeed.
- Shopify Forms.
- Qikify Form Builder.
- Wishlist King.
- LangShop.
- Klaviyo.
- Shopify Inbox.
- GDPR Cookie Consent.

Estado: `VERIFICADO Y CORRECTO`.

## Decision tecnica

El hotfix `SEO schema hotfix - 2026-06-15` queda clasificado como:

`VERIFICADO Y CORRECTO`

Motivo:

- Corrige GTIN/MPN falsos cuando el barcode coincide con el ID interno de variante.
- Elimina `AggregateRating` corporativo fijo no justificable.
- Corrige breadcrumb de articulos.
- Mantiene ofertas, SKU, disponibilidad, precio, moneda, URL, formularios, carrito, App Embeds y estructura visual revisada.
- No se detectan cambios inesperados funcionales tras comparar archivos, schema y render.

Limitacion documentada:

- No se ejecuto una publicacion ni se modifico Shopify.
- La decision de publicar sigue en `REQUIERE DECISION HUMANA`.

## Recomendacion

Recomendacion tecnica: publicable manualmente desde Shopify si Daniel aprueba el lote de publicacion correspondiente.

No publicar `SEO-GEO staging - 2026-06-15`.

Conservar temporalmente `snippets/microdata-schema-original.liquid`, tal como Daniel habia indicado.
