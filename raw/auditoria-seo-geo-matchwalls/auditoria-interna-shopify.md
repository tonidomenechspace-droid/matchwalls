# Auditoría interna de Shopify

Fecha: 15 de junio de 2026.  
Modo de trabajo: acceso de solo lectura. No se ha modificado Shopify, ejecutado mutaciones, cambiado traducciones, URLs, redirecciones, aplicaciones, configuraciones ni archivos del tema.

## Alcance y límites

Esta fase contrasta la auditoría pública con datos internos de Shopify: estructura del catálogo, estados de producto, traducciones, páginas, colecciones, redirecciones y código del tema principal. Se han revisado con detalle superficies críticas, cambios recientes y muestras representativas; no debe interpretarse como una revisión editorial manual individual de los 3.022 productos y todas sus traducciones.

Los eventos consultados no permiten atribuir cambios concretos a Claude. Por tanto, los errores detectados se describen como **trabajo reciente verificado en Shopify**, compatible con el contexto facilitado, pero sin atribución de autor.

## Inventario interno verificado

| Recurso | Dato verificado |
|---|---:|
| Productos totales | 3.022 |
| Productos activos | 1.767 |
| Productos borrador | 904 |
| Productos archivados | 351 |
| Productos tipo `Muestra` | 1.990 |
| Productos tipo `Mural` | 744 |
| Productos tipo `Papel Pintado` | 274 |
| Productos actualizados desde el 1 de junio de 2026 | 304 |
| Colecciones | 109 |
| Páginas | 55 |
| Redirecciones | 635 |
| Artículos recuperados | 11 |
| Idiomas publicados | ES, EN, FR, DE, NL, IT y PT-PT |

## Hallazgos críticos verificados

### 1. `AggregateRating` fijo en el tema principal

El tema publicado `Production - SEO fix AggregateRating (2026-06-12)` incluye en `snippets/microdata-schema.liquid` un `AggregateRating` de Organization fijo con `ratingValue: 4.5` y `reviewCount: 13`.

No se ha verificado en el código revisado una relación visible y demostrable con la fuente de esas reseñas. El schema de producto, en cambio, sí condiciona las valoraciones a metafields reales de reviews.

**Riesgo:** datos estructurados potencialmente no elegibles o engañosos, pérdida de confianza y acciones manuales.  
**Acción recomendada:** validar fuente, entidad, reseñas visibles y elegibilidad; retirar el bloque fijo si no puede demostrarse. No modificar sin autorización.

### 2. Contenido cruzado entre `Métodos de pago` y `Conoce nuestros productos`

- La página `Métodos de pago`, handle `metodos-de-pago`, contiene un cuerpo que comienza con contenido de “Nuestros productos”.
- La página `Conoce nuestros productos`, handle `nuestros-productos`, contiene un cuerpo que comienza con contenido de “Métodos de pago”.
- EN, FR, DE y NL de `Conoce nuestros productos` recibieron contenido y metadatos de métodos de pago, pero mantienen handles propios de la página de productos.
- IT y PT conservan el contenido anterior, creando una matriz internacional incoherente.
- La página real `Métodos de pago` no dispone de traducción de `body_html` en los idiomas revisados.

**Riesgo:** intención equivocada, contenido cruzado, traducciones erróneas, señales hreflang contradictorias y pérdida de conversión.  
**Acción recomendada:** restaurar la correspondencia página-contenido desde una versión validada, revisar las siete localizaciones y comprobar enlaces/canonicals/hreflang antes de publicar.

### 3. Correcciones parciales en Serene Vista y Whispering Woods

Las familias fueron actualizadas en bloque el 12 de junio de 2026, pero no están cerradas editorialmente:

- `Vista Serena Verde` conserva media alt `Unknown`, `bedroom`, `Unknown`.
- Su título SEO español contiene doble espacio.
- Las traducciones IT y PT están marcadas como desactualizadas y contienen contenido de otro producto, `Jungle Rhapsody`.
- La meta description PT está en italiano.
- Existen títulos y handles débiles o incorrectos, incluidos sufijos `-1`.
- En Whispering Woods aparecen formas como `Whispending Woods Green`, traducciones forzadas y handles con sufijos automáticos.
- Una muestra azul de Bosques Susurrantes presenta inventario `-1`.

**Riesgo:** errores visibles multiplicados por idioma, recomendaciones de producto equivocadas y pérdida de confianza.  
**Acción recomendada:** QA manual completo por familia, incluyendo producto principal, muestras, imágenes, metadatos, handles e idiomas publicados.

### 4. Actualización reciente incompleta por idiomas

Numerosas páginas corporativas se actualizaron en ES y, en parte, EN/FR/DE/NL durante el 15 de junio de 2026. IT y PT mantienen con frecuencia contenido de 2024/2025, campos sin `body_html` o traducciones marcadas como desactualizadas.

**Riesgo:** experiencia desigual, contenido obsoleto y baja confianza de motores de búsqueda e IA en la equivalencia entre idiomas.  
**Acción recomendada:** implantar una matriz de publicación obligatoria por recurso e idioma; no considerar una actualización terminada hasta completar o excluir conscientemente todos los idiomas publicados.

### 5. Calidad y gobernanza insuficientes en muestras

Se verifican muestras recientes con descripciones vacías, contenido perteneciente a otros productos, títulos y colores que no coinciden con el handle, duplicados con `-copia`, handles mezclados `muestra-`, `muestra-de-` y `sample-`, vendors inconsistentes y media alt vacía.

**Riesgo:** canibalización, index bloat, errores operativos, recomendaciones incorrectas y baja conversión.  
**Acción recomendada:** definir un modelo único producto principal-familia-muestra y una política de indexación para las 1.990 muestras internas.

### 6. Redirecciones con cadenas y destinos no equivalentes

Cadenas verificadas:

- `/collections/papeles-pintados` → `/collections/papeles-pintados-old` → `/collections/murales`
- `/pages/como-tomar-medidas-paredes-y-techos-boton` → `/pages/medidas-paredes-techos` → `/pages/medidas-paredes`

También se detectaron destinos aparentemente no equivalentes entre productos, como una muestra de Eternal Marble enviada a Aurora Marítima Rosa.

**Riesgo:** pérdida de relevancia, mala experiencia, desperdicio de rastreo y atribución incorrecta de señales.  
**Acción recomendada:** auditar las 635 redirecciones, eliminar cadenas y exigir equivalencia semántica uno-a-uno.

### 7. Arquitectura de colecciones confusa

- `Todos los Papeles Pintados` usa el handle `/collections/murales` y reglas que no coinciden claramente con su título.
- `Papeles Pintados para un Espacio público` usa un handle de murales y reglas amplias.
- Existen numerosas colecciones locales `comprar-papel-pintado-{ciudad}` con conjuntos de productos idénticos, con riesgo de contenido débil o doorway.
- Se observan errores gramaticales y posibles incoherencias entre etiquetas con y sin tilde.

**Riesgo:** intención ambigua, duplicación, mala distribución de autoridad y baja diferenciación local.  
**Acción recomendada:** revisar propósito, reglas, contenido único e indexación de cada colección antes de ampliar esta arquitectura.

### 8. Contenido y blog con deuda editorial

Hay páginas publicadas con cuerpo vacío o dependiente de plantilla, CSS expuesto como texto y errores ortográficos. Los 11 artículos recuperados tienen resúmenes vacíos salvo uno con HTML bruto; existe el handle erróneo `transfroma-tu-cocina...`.

**Riesgo:** menor autoridad temática y menor capacidad para ser citado por motores de IA.  
**Acción recomendada:** corregir primero errores visibles y después crear una estrategia editorial experta, verificable y mantenida.

### 9. Error en Breadcrumb schema de artículos

El snippet de breadcrumb usa `blog.title` como nombre del tercer elemento donde debería identificar el artículo.

**Riesgo:** breadcrumb semánticamente incorrecto y menor claridad para buscadores.  
**Acción recomendada:** preparar corrección a `article.title`, validar en entorno de prueba y desplegar solo con autorización.

## Conclusión interna

El trabajo reciente ha mejorado parcialmente familias y páginas prioritarias, pero no existe todavía una garantía de calidad transversal. El patrón dominante es una actualización por bloques sin control final completo de correspondencia entre recurso, idioma, handle, metadatos e imágenes.

La prioridad inmediata no es producir más traducciones ni cambiar URLs masivamente. Es detener la propagación de errores, restaurar las páginas cruzadas, validar el `AggregateRating`, revisar las familias recientemente tratadas y establecer controles obligatorios antes de publicar.

