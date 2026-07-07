# Propuesta de lote MW-FOOTER-I18N-001 - 2026-06-17

Estado: PROPUESTA - NO EJECUTADA

Modo actual: solo lectura.

Cambios en Shopify ejecutados: ninguno.

Mutaciones GraphQL ejecutadas: ninguna.

Publicaciones, traducciones, cambios de tema, inventario, URLs o redirecciones ejecutadas: ninguna.

## 1. Objetivo del lote

Corregir de forma acotada y reversible el footer global visible de `matchwalls.com` en los idiomas prioritarios ES, EN, FR, DE y NL.

El objetivo no es rediseñar el footer ni cambiar arquitectura, sino resolver errores visibles y riesgos editoriales ya verificados:

- mezcla de idiomas;
- erratas;
- evento caducado;
- claims globales no validados;
- traducciones de menú obsoletas o incorrectas;
- textos fijos de plantilla que afectan a múltiples URLs.

## 2. Estado real comprobado

Consulta realizada contra Shopify Admin real en modo lectura.

Tienda:

- Nombre: `Matchwalls`
- Dominio principal: `https://www.matchwalls.com`
- Dominio Shopify: `matchwalls.myshopify.com`

Tema MAIN actual:

- Nombre: `SEO schema hotfix - 2026-06-15`
- ID: `gid://shopify/OnlineStoreTheme/178383749496`
- Estado: MAIN
- `processing`: `false`
- `processingFailed`: `false`

Archivos de tema leídos en MAIN:

- `sections/footer-group.json`
  - checksum: `e93af9228c8a97dce4ad91e203bf7e75`
  - tamaño: `4210`
  - actualizado: `2026-06-15T12:34:21Z`
- `sections/header-group.json`
  - checksum: `671e993b0001e876d7a1bc51d8ccd44d`
  - tamaño: `6939`
  - actualizado: `2026-06-15T12:34:21Z`
- `config/settings_data.json`
  - checksum: `a1192f2f698d277e0f69f7156a61a90c`
  - tamaño: `10256`
  - actualizado: `2026-06-15T12:34:14Z`

Idiomas publicados:

- ES principal
- EN
- FR
- DE
- NL
- IT
- PT-PT

Alcance prioritario de este lote:

- ES
- EN
- FR
- DE
- NL

IT y PT-PT quedan fuera de corrección editorial salvo autorización expresa.

## 3. Documentos locales usados como evidencia

- `AGENTS.md`
- `control-paquete-maestro-2026-06-17.md`
- `siguientes-lotes-contenido-i18n-geo-2026-06-16.md`
- `textos-fijos-plantilla-bloqueantes-2026-06-16.csv`
- `auditoria-contenido-i18n-geo-2026-06-16.md`
- `registro-cambios-ejecutados.md`
- `programa-ejecucion-seo-geo.md`
- `lista-maestra-errores-cambios-evoluciones-mejoras.md`

## 4. Recursos afectados

### Tema

Recurso principal:

- Tema MAIN actual: `SEO schema hotfix - 2026-06-15`
- ID: `gid://shopify/OnlineStoreTheme/178383749496`
- Archivo: `sections/footer-group.json`

Recurso relacionado, solo para no mezclar lotes:

- Archivo: `sections/header-group.json`
- Motivo: contiene announcement bar con claims globales.
- Estado en este lote: fuera de alcance. Se tratará en `MW-HEADER-CLAIMS-I18N-001`.

### Menús Shopify

Menús leídos en modo consulta:

- `footer`
- `footer-profesional`
- `footer-brand`
- `footer-legal`
- `help`
- `footer-matchwalls`

Menús realmente usados por `sections/footer-group.json`:

- `footer-profesional`
- `footer-brand`
- `footer`
- `footer-legal`

El menú `help` contiene elementos aparentemente más limpios, pero no está conectado al footer actual. No se propone sustituirlo sin revisión explícita de estructura.

## 5. Valores actuales verificados

### `sections/footer-group.json`

Newsletter:

- Título: `NOTICIAS, INSPIRACIÓN, REGALOS Y NOVEDADES`
- Texto: `¡Suscríbete a nuestras noticias! Se el primero...`

Bloques visibles tipo iconos/texto:

- Título: `Envío gratuito`
  - contenido: `Worldwide.`
- Título: `Pago seguro`
  - contenido: `Metodos de pago seguros y financiación.`
- Título: `Garantía de satisfacción`
  - contenido: `Nuestro compromiso tu tranquilidad.`
- Título: `Personalización`
  - contenido: `Te ayudamos a crear tu diseño Matchwalls.`
- Título: `Fácil instalación`
  - contenido: `Descargate nuestras guías de fácil instlacióon.`

Estado:

- `INCORRECTO` por mezcla de idiomas y erratas.
- `REQUIERE DECISION HUMANA` para claims de envío gratuito, financiación, garantía y condiciones comerciales.

### Menú `footer`

Elementos visibles verificados:

- `FAQ´S - Envíos y devoluciones`
- `Crea tu propio papel pintado rollo`
- `Crea tu papel pintado mural personalizado`
- `Cómo tomar medidas de paredes`
- `Cómo tomar medidas del techo`
- `Envíos internacionales`
- `Black Friday 2024`
- `Your Privacy Choices`

Traducción de título EN leída:

- `Help &amp; support`
- `outdated: true`

Estado:

- `INCORRECTO` por `FAQ´S` y `Black Friday 2024`.
- `REQUIERE DECISION HUMANA` para decidir si se mantiene, renombra o retira `Your Privacy Choices`.

### Menú `footer-profesional`

Elementos visibles verificados:

- `B2B Tiendas interiorismo`
- `B2B Estudios interiorismo y arquitectura, hoteles y espacios púbicos.`
- `B2B Hoteles & Contact`
- `Social & Prensa y Afiliación`
- `Artistas & Diseñadores`
- `Solicita tu muestra`

Traducción de título EN leída:

- `Professional &amp; social`
- `outdated: true`

Estado:

- `INCORRECTO` por errata `espacios púbicos`.
- `VERIFICADO PERO MEJORABLE` por mezcla ES/EN en `B2B Hoteles & Contact`.

### Menú `footer-brand`

Elementos visibles verificados:

- `Sobre Nosotros`
- `Nuestros Productos`
- `Sostenibilidad`
- `Inspiración`
- `Tarjeta regalo`

Traducción de título EN leída:

- `brand`
- `outdated: true`

Estado:

- `VERIFICADO PERO MEJORABLE`.
- Posible inconsistencia editorial por título EN en minúscula y traducciones obsoletas.

### Traducciones de tema

Se comprobó que existen traducciones publicadas de tema para EN, FR, DE y NL. La consulta devolvió muchas claves y confirmó, entre otras, traducción NL del texto `Worldwide.` como `Wereldwijd.`.

Estado:

- `VERIFICADO PERO MEJORABLE`.
- Antes de escribir, debe exportarse el conjunto exacto de claves de footer por idioma y guardarse respaldo local.

## 6. Alcance propuesto

### Dentro del lote

1. Exportar respaldo exacto de:
   - `sections/footer-group.json`;
   - menús `footer`, `footer-profesional`, `footer-brand`, `footer-legal`;
   - traducciones de footer en ES, EN, FR, DE y NL.

2. Preparar correcciones de textos visibles del footer:
   - erratas;
   - mezcla de idioma;
   - textos caducados;
   - claims no demostrados, sustituidos por formulaciones conservadoras o marcados para decisión humana.

3. Ejecutar, si se aprueba, en un entorno no publicado:
   - opción preferente: duplicado del MAIN actual para QA;
   - opción alternativa: tema staging existente solo si se demuestra que está sincronizado con el MAIN actual.

4. Verificar preview público del tema de QA en ES, EN, FR, DE y NL.

5. Documentar evidencias y resultado.

### Fuera del lote

- Publicar tema.
- Cambiar header announcement bar.
- Cambiar handles.
- Cambiar URLs.
- Crear o eliminar redirecciones.
- Cambiar políticas legales.
- Cambiar precios, inventario, variantes o datos comerciales.
- Editar Liquid de producción.
- Ejecutar cambios masivos.
- Actuar sobre IT o PT-PT.

## 7. Valores propuestos iniciales

Estos textos son una propuesta conservadora para revisión. No están aprobados.

### Bloques de confianza del footer ES

Propuesta:

- `Envío internacional`
  - `Consulta los plazos y condiciones de envío disponibles para tu país.`
- `Pagos seguros`
  - `Consulta los métodos de pago disponibles durante el checkout.`
- `Atención y soporte`
  - `Te ayudamos antes y después de tu pedido.`
- `Personalización`
  - `Te orientamos para adaptar tu diseño a medida.`
- `Guías de instalación`
  - `Consulta nuestras guías antes de instalar tu papel pintado o mural.`

Criterio:

- No prometer envío gratuito si no está validado por mercado.
- No prometer financiación si depende de país, método o checkout.
- No usar garantía de satisfacción sin política exacta validada.
- Mantener mensajes útiles para SEO/GEO sin inflar claims.

### Menú `footer`

Propuestas de decisión:

- `FAQ´S - Envíos y devoluciones`
  - propuesta: `FAQ - Envíos y devoluciones`
- `Black Friday 2024`
  - propuesta: retirar, renombrar o sustituir solo si Daniel confirma la estrategia comercial.
- `Your Privacy Choices`
  - propuesta: mantener hasta validación legal/técnica. No tocar en este lote sin decisión humana.

### Menú `footer-profesional`

Propuestas:

- `B2B Estudios interiorismo y arquitectura, hoteles y espacios púbicos.`
  - propuesta: `B2B estudios de interiorismo y arquitectura, hoteles y espacios públicos`
- `B2B Hoteles & Contact`
  - propuesta: requiere decisión editorial. Posibles opciones:
    - `B2B hoteles y contacto`
    - `Hoteles y proyectos contract`

### Menú `footer-brand`

Propuesta:

- Revisar títulos y traducciones publicadas por idioma.
- No cambiar nombres de secciones sin comprobar destinos y estrategia editorial.

### EN, FR, DE y NL

No se propone usar traducción automática sin revisión.

En ejecución aprobada, cada idioma debe tratarse como texto editorial propio, manteniendo nombres de marca/familia cuando aplique.

## 8. Riesgos

- El footer es global y afecta a todo el sitio.
- Cambiar menús puede afectar navegación, enlaces internos y experiencia de usuario.
- Traducciones del tema pueden estar gestionadas por Shopify, LangShop o una combinación de ambos.
- Algunas claves aparecen con `outdated: true`; escribir sin inventario exacto puede ocultar o sobrescribir contenido esperado.
- `Your Privacy Choices` puede estar relacionado con privacidad o cumplimiento legal.
- Claims comerciales pueden depender de mercado, envío, checkout, Klarna, políticas o promociones activas.
- Un tema de staging desincronizado puede introducir regresiones si se usa como base sin comparar contra MAIN.

## 9. Respaldo obligatorio antes de ejecutar

Antes de cualquier escritura aprobada:

1. Guardar copia local completa de `sections/footer-group.json`.
2. Guardar copia local de los menús afectados con IDs, títulos, handles, URLs y traducciones disponibles.
3. Guardar copia local de las traducciones de tema relacionadas con footer para ES, EN, FR, DE y NL.
4. Registrar checksums y fecha/hora.
5. Confirmar que no se modifican App Embeds ni `config/settings_data.json`.

## 10. Método de reversión

Si falla la QA:

1. Restaurar `sections/footer-group.json` desde el respaldo exacto.
2. Restaurar valores originales de menús y traducciones modificadas.
3. Verificar de nuevo home, colección, producto, página informativa y carrito en ES, EN, FR, DE y NL.
4. Registrar incidencia en `registro-cambios-ejecutados.md`.
5. No publicar ningún tema si el fallo ocurre en QA.

## 11. QA posterior obligatoria

Verificaciones mínimas:

- Home ES, EN, FR, DE y NL.
- Página de producto ES, EN, FR, DE y NL.
- Página de colección ES, EN, FR, DE y NL.
- Página informativa ES, EN, FR, DE y NL.
- Carrito o drawer cart si el footer aparece o puede afectar carga.
- Desktop y mobile.
- Enlaces del footer sin 404.
- No aparición de textos caducados o erratas corregidas.
- No regresión de schema Product/Offer/AggregateRating.
- No cambio en App Embeds.
- No publicación del tema QA.

## 12. Decisión requerida

Para ejecutar este lote, Daniel debe aprobar exactamente:

`APROBADO LOTE MW-FOOTER-I18N-001`

Hasta recibir esa frase exacta:

- no se escribirá en Shopify;
- no se ejecutarán mutaciones;
- no se publicará ni duplicará tema;
- no se modificarán menús ni traducciones;
- no se cambiarán URLs, handles ni redirecciones.

## 13. Estado final de esta propuesta

Clasificación: `REQUIERE DECISION HUMANA`

Motivo: la evidencia confirma errores reales en footer y menús, pero los textos definitivos y las decisiones comerciales/legalmente sensibles deben aprobarse antes de cualquier ejecución.
