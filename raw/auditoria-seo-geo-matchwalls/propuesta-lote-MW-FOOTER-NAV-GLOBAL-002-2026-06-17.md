# Propuesta de lote MW-FOOTER-NAV-GLOBAL-002 - 2026-06-17

Estado: PROPUESTA - NO EJECUTADA

Modo actual: solo lectura y preparación.

Cambios ejecutados en Shopify en este lote: ninguno.

## 1. Motivo

Daniel indica que `Tarjeta regalo`, `Black Friday 2024` y `Envíos internacionales` no deben ser visibles en el footer.

Estado real verificado en Shopify Admin:

- `Envíos internacionales` sigue dentro del menú global `footer`.
- `Black Friday 2024` sigue dentro del menú global `footer`.
- `Tarjeta regalo` sigue dentro del menú global `footer-brand`.

Estos elementos no reaparecen por el cambio del tema QA. Siguen visibles porque el tema publicado llama a menús globales de Shopify:

- `footer-profesional`
- `footer-brand`
- `footer`
- `footer-legal`

## 2. Alcance exacto propuesto

Reparar la navegación visible del footer publicada mediante edición de menús globales.

Este lote no publica tema, no toca productos, no elimina recursos y no cambia URLs.

## 3. Recursos afectados

### Menú `footer`

- ID: `gid://shopify/Menu/210266325219`
- Handle: `footer`
- Título actual: `AYUDA & SOPORTE`
- `isDefault`: `true`

### Menú `footer-profesional`

- ID: `gid://shopify/Menu/210972311779`
- Handle: `footer-profesional`
- Título actual: `PROFESIONALES & SOCIAL`
- `isDefault`: `false`

### Menú `footer-brand`

- ID: `gid://shopify/Menu/210972344547`
- Handle: `footer-brand`
- Título actual: `EMPRESA`
- `isDefault`: `false`

### Menú `footer-legal`

- ID: `gid://shopify/Menu/210972410083`
- Handle: `footer-legal`
- Título actual: `Legal`
- `isDefault`: `false`

## 4. Valores actuales y propuestos

### Menú `footer`

| Estado | Título | URL | Acción propuesta |
| --- | --- | --- | --- |
| Actual | `FAQ´S - Envíos y devoluciones` | `/pages/preguntas-frecuentes` | Cambiar etiqueta a `FAQ - Envíos y devoluciones` |
| Actual | `Crea tu propio papel pintado rollo` | `/pages/crea-tu-papel-pintado-rollo` | Cambiar etiqueta a `Crea tu propio papel pintado` |
| Actual | `Crea tu papel pintado mural personalizado` | `/pages/crea-tu-mural` | Cambiar etiqueta a `Crea tu mural personalizado` |
| Actual | `Cómo tomar medidas de paredes` | `/pages/medidas-paredes` | Mantener |
| Actual | `Cómo tomar medidas del techo` | `/pages/medidas-techo` | Mantener |
| Actual | `Envíos internacionales` | `/pages/envios-internacionales` | Retirar del footer |
| Actual | `Black Friday 2024` | `/collections/papel-pintado-black-friday` | Retirar del footer |
| Actual | `Your Privacy Choices` | `/pages/data-sharing-opt-out` | Mantener sin cambios por posible cumplimiento legal |

Título de menú:

- Actual: `AYUDA & SOPORTE`
- Propuesto: `AYUDA Y SOPORTE`

### Menú `footer-profesional`

| Estado | Título | URL | Acción propuesta |
| --- | --- | --- | --- |
| Actual | `B2B Tiendas interiorismo` | `/pages/tiendas` | Cambiar etiqueta a `B2B tiendas de interiorismo` |
| Actual | `B2B Estudios interiorismo y arquitectura, hoteles y espacios púbicos.` | `/pages/estudios-profesionales` | Cambiar etiqueta a `B2B estudios de interiorismo y arquitectura, hoteles y espacios públicos` |
| Actual | `B2B Hoteles & Contact` | `/pages/horeca` | Cambiar etiqueta a `B2B hoteles y contract` |
| Actual | `Social & Prensa y Afiliación` | `/pages/social-prensa-y-afiliacion` | Cambiar etiqueta a `Social, prensa y afiliación` |
| Actual | `Artistas & Diseñadores` | `/pages/artistas` | Cambiar etiqueta a `Artistas y diseñadores` |
| Actual | `Solicita tu muestra` | `/pages/muestras` | Mantener |

Título de menú:

- Actual: `PROFESIONALES & SOCIAL`
- Propuesto: `PROFESIONALES`

### Menú `footer-brand`

| Estado | Título | URL | Acción propuesta |
| --- | --- | --- | --- |
| Actual | `Sobre Nosotros` | `/pages/sobre-nosotros` | Cambiar etiqueta a `Sobre nosotros` |
| Actual | `Nuestros Productos` | `/pages/nuestros-productos` | Cambiar etiqueta a `Nuestros productos` |
| Actual | `Sostenibilidad` | `/pages/sostenibilidad` | Mantener |
| Actual | `Inspiración` | `/blogs/inspiracion` | Mantener |
| Actual | `Tarjeta regalo` | `/products/tarjeta-regalo` | Retirar del footer |

Título de menú:

- Actual: `EMPRESA`
- Propuesto: `EMPRESA`

### Menú `footer-legal`

| Estado | Título | URL | Acción propuesta |
| --- | --- | --- | --- |
| Actual | `Aviso Legal` | `/pages/aviso-legal` | Cambiar etiqueta a `Aviso legal` |
| Actual | `Política de Cookies` | `/pages/politica-de-cookies` | Cambiar etiqueta a `Política de cookies` |
| Actual | `Condiciones de uso de la web` | `/pages/condiciones-de-uso` | Mantener |
| Actual | `Condiciones de venta online` | `/pages/condiciones-de-venta-online` | Mantener |

Título de menú:

- Actual: `Legal`
- Propuesto: `LEGAL`

## 5. Cambios que NO se harán

- No se eliminarán páginas.
- No se eliminarán productos.
- No se eliminarán colecciones.
- No se crearán redirecciones.
- No se cambiarán handles.
- No se cambiarán URLs destino.
- No se publicará ningún tema.
- No se tocará el tema MAIN.
- No se modificarán precios, inventario, variantes, imágenes ni datos comerciales.
- No se tocará `Your Privacy Choices` sin decisión legal explícita.

## 6. Relación con el lote anterior

El lote `MW-FOOTER-I18N-001` ya dejó corregido `sections/footer-group.json` en el tema QA:

- Tema QA: `MW-FOOTER-I18N-001 - QA - 2026-06-17`
- ID: `gid://shopify/OnlineStoreTheme/178390401400`
- Estado: no publicado

Ese cambio corrige los textos tipo `Worldwide.`, `Metodos`, `instlacióon`, etc. Pero no es visible en producción porque no se ha publicado el tema QA ni se ha tocado el MAIN.

Este nuevo lote corrige solo navegación global del footer, que sí es visible en el sitio publicado al editar menús.

## 7. Riesgos

- Los menús son globales y afectan al footer del sitio publicado.
- Retirar enlaces reduce navegación interna hacia esas URLs, aunque no elimina las páginas/productos/colecciones.
- Las traducciones EN, FR, DE y NL de los menús pueden quedar incompletas o desfasadas si Shopify/LangShop no las sincroniza automáticamente.
- `Your Privacy Choices` puede ser un enlace de cumplimiento legal; se mantiene.
- `B2B hoteles y contract` debe validarse como etiqueta editorial aceptada por marca.

## 8. Respaldo y reversión

Antes de ejecutar, se guardará respaldo local con:

- IDs de menús;
- títulos;
- orden;
- tipos;
- URLs;
- resource IDs;
- traducciones de título disponibles.

Reversión:

- Restaurar los menús con los mismos elementos originales y el mismo orden.
- Volver a añadir:
  - `Envíos internacionales`
  - `Black Friday 2024`
  - `Tarjeta regalo`
- Restaurar etiquetas originales si fuera necesario.

## 9. QA posterior

Verificación mínima:

- Home ES publicada.
- Home EN, FR, DE y NL publicadas.
- Página de producto ES.
- Página de colección ES.
- Comprobar que no aparecen:
  - `Tarjeta regalo`
  - `Black Friday 2024`
  - `Envíos internacionales`
  - `espacios púbicos`
  - `FAQ´S`
- Comprobar que siguen accesibles las páginas de destino mantenidas.
- Comprobar que `Your Privacy Choices` sigue visible si Shopify lo requiere o si permanece en el menú.

## 10. Aprobación requerida

Para ejecutar este lote, Daniel debe responder exactamente:

`APROBADO LOTE MW-FOOTER-NAV-GLOBAL-002`

Hasta recibir esa frase exacta:

- no se editarán menús;
- no se ejecutarán mutaciones;
- no se tocará el sitio publicado.

## 11. Estado final de esta propuesta

Clasificación: `REQUIERE DECISION HUMANA`

Motivo: la reparación es clara y los recursos están verificados, pero impacta navegación global publicada.
