# MW-ENTITY-FACTUAL-SOURCE-VALIDATION-015B

Fecha: 2026-07-05 22:05 CEST  
Estado del documento: `VERIFICADO Y CORRECTO`  
Estado de fuentes oficiales de entidad: `INCOMPLETO`  
Tipo: validación documental de fuentes para entidad MatchWalls  
Ámbito: ES, EN, FR, DE, NL  

## Resumen ejecutivo

015B valida la fuente de los datos corporativos que podrían alimentar schema, página “Sobre nosotros”, panel CEO/CMO, perfiles IA y contenido factual.

Resultado: existe una base segura para describir la actividad comercial de MatchWalls, pero no existe todavía una fuente oficial suficiente para publicar datos legales, contacto estructurado, sameAs, certificaciones, fabricación propia, ubicación corporativa, historia, garantías, plazos o reseñas.

La decisión operativa correcta es mantener esos campos fuera de schema y copy público hasta que Daniel aporte o autorice una fuente oficial actual.

## Documentos y fuentes locales leídas

`VERIFICADO Y CORRECTO`

- `entity-factual-brief-MW-ENTITY-FACTUAL-BRIEF-ES-EN-FR-DE-NL-015A-2026-07-05.md`
- `entity-factual-claims-matrix-MW-ENTITY-FACTUAL-BRIEF-ES-EN-FR-DE-NL-015A-2026-07-05.csv`
- `infra-hold-replan-MW-MASTER-QUEUE-INFRA-HOLD-REPLAN-014B-2026-07-05.md`
- `registro-cambios-ejecutados.md`
- `auditoria-contenido-i18n-geo-2026-06-16.md`
- `auditoria-contenidos.csv`
- `auditoria-schema.md`
- `diagnostico-MW-GEO-LANDINGS-CONTENT-REVIEW-012E-2026-07-03.md`
- `ejecucion-MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F-2026-07-03.md`
- `copy-map-MW-GEO-LANDINGS-I18N-COPY-MAP-SPAIN-FRANCE-012G1-2026-07-03.md`
- backups de tema relacionados con `sobre-nosotros`, `envios-y-devoluciones`, `estudios-profesionales`, `formulario-profesionales` y `social_prensa_afiliacion`
- búsquedas locales acotadas de: CIF, NIF, VAT, razón social, dirección, teléfono, email, Trustpilot, 1961, Barcelona, certificaciones, sostenibilidad, envío, devoluciones y garantías

## Estado real comprobado

`VERIFICADO Y CORRECTO`

- No se modificó Shopify ni ninguna plataforma externa.
- El ticket Shopify Engineering `68731900` sigue condicionando los crawls públicos amplios.
- La base factual segura de 015A sigue siendo válida: MatchWalls como tienda online especializada en papel pintado, murales decorativos y soluciones murales a medida.

`INCOMPLETO`

- No se encontró fuente local actual y suficiente para validar razón social, CIF/NIF/VAT, dirección legal, teléfono oficial, perfiles oficiales, certificaciones, fabricación, historia o Trustpilot.
- Varios datos aparecen en backups o auditorías antiguas, pero esos backups no son fuente de verdad publicable.

## Fuentes aceptables para usar un dato como verdad de entidad

`VERIFICADO Y CORRECTO`

Para poder usar un dato en schema, página corporativa o contenido citable, debe estar validado por al menos una de estas fuentes:

1. Fuente oficial actual de Shopify Admin o configuración de tienda.
2. Documento legal o mercantil aportado por Daniel.
3. Política pública vigente y revisada en Shopify.
4. Perfil oficial controlado por MatchWalls.
5. Certificado/documento técnico verificable.
6. Respuesta escrita de Shopify/LangShop/servicio externo cuando aplique.
7. Evidencia pública estable tras resolución del ticket `68731900`.

`INCORRECTO`

No aceptar como fuente suficiente:

- backups antiguos del tema;
- copy corregido o retirado;
- textos automáticos de traducción;
- screenshots aislados;
- contenido de plantillas con claims ya marcados como deuda;
- respuestas genéricas de herramientas IA;
- datos visibles en páginas no auditadas o afectadas por caché/render.

## Datos validados para uso inmediato

`VERIFICADO Y CORRECTO`

- Nombre de marca: `MatchWalls`.
- Dominio trabajado: `https://www.matchwalls.com/` / propiedad Bing `matchwalls.com`.
- Tipo operativo seguro: tienda online.
- Oferta segura: papel pintado, murales decorativos y soluciones murales a medida.
- Público seguro: hogares y proyectos profesionales.
- Idiomas prioritarios: ES, EN, FR, DE, NL.
- Temas informativos seguros: muestras, medición de paredes, personalización, materiales como opciones generales.

`VERIFICADO PERO MEJORABLE`

- Segmentos B2B: interioristas, arquitectos, tiendas, hoteles, restaurantes y oficinas.
- Materiales: non-woven/no tejido, vinílico y peel & stick/autoadhesivo.
- Personalización avanzada: adaptación de color, escala o composición.

Estos datos pueden usarse en copy prudente, pero conviene reforzarlos con páginas de materiales, casos B2B y procesos reales.

## Datos no validados para uso público/schema

`REQUIERE DECISION HUMANA`

- Razón social.
- CIF/NIF/VAT/tax ID.
- Dirección legal.
- Dirección de estudio, fábrica, almacén o showroom.
- Teléfono oficial.
- Email oficial para `ContactPoint`.
- Perfiles oficiales para `sameAs`.
- Fecha de fundación o claim “desde 1961”.
- Claims de Barcelona como sede oficial.
- Fabricación propia o país/lugar de fabricación.
- Certificaciones de materiales, sostenibilidad, FSC, ignifugación, tintas, lavabilidad o normativas.
- Trustpilot, reseñas, puntuaciones, testimonios o `aggregateRating`.
- Políticas de envío, devolución, garantías, plazos y aduanas.
- Autores, expertos, revisores editoriales o responsables técnicos.

## Hallazgos delicados

`DECLARADO PERO NO VERIFICADO`

1. `help@matchwalls.com` aparece en backups antiguos y páginas profesionales antiguas. No queda validado como email oficial estructurable.
2. “Desde 1961” aparece en backup antiguo de `sobre-nosotros`. No queda validado como historia corporativa.
3. Barcelona aparece en backups y claims visuales antiguos. No queda validado como sede legal o claim corporativo.
4. Envío gratis, plazos, garantías y devoluciones aparecen en contenido antiguo o plantillas marcadas como deuda. No deben usarse.
5. Trustpilot aparece como elemento de confianza en histórico visual, pero no hay dato auditado vigente para schema.

## Impacto en schema

`VERIFICADO Y CORRECTO`

Hasta completar fuentes oficiales, el schema de entidad debe limitarse a:

- `Organization.name`
- `Organization.url`
- descripción prudente por idioma;
- `WebSite.name`
- `WebSite.url`
- `WebPage` para páginas con contenido visible coherente;
- `BreadcrumbList` solo donde exista correspondencia visible;
- `FAQPage` solo con FAQ visible y validada.

`REQUIERE DECISION HUMANA`

Mantener bloqueados:

- `legalName`
- `taxID`
- `vatID`
- `address`
- `contactPoint`
- `telephone`
- `email`
- `foundingDate`
- `founder`
- `sameAs`
- `aggregateRating`
- `review`
- `hasCertification`
- `award`
- `manufacturer`
- `LocalBusiness`

## Datos que necesito de Daniel para cerrar 015B como fuente completa

`REQUIERE DECISION HUMANA`

Para pasar de `INCOMPLETO` a una entidad robusta y publicable, necesito confirmación o documento de:

1. Razón social exacta.
2. CIF/NIF/VAT, si debe publicarse o usarse solo internamente.
3. Dirección legal y si es publicable.
4. Email oficial de atención al cliente.
5. Teléfono oficial, si existe y si es publicable.
6. Perfiles oficiales: Instagram, Pinterest, TikTok, YouTube, LinkedIn, Facebook, Trustpilot u otros.
7. Claim histórico: si “desde 1961” pertenece legalmente a MatchWalls, a otra empresa del grupo o no debe usarse.
8. Relación real con Barcelona: sede, estudio, origen creativo, almacén o solo claim de marca.
9. Fabricación: propia, bajo pedido, proveedor externo, país de producción y qué puede publicarse.
10. Certificaciones y documentación técnica de materiales.
11. Políticas actuales de envío, devoluciones, garantías y muestras.
12. Nombres/cargos de autores, expertos o revisores si se quiere reforzar E-E-A-T.

## Decisión operativa

`VERIFICADO Y CORRECTO`

015B no autoriza publicación ni schema nuevo. Autoriza únicamente usar la base factual prudente de 015A en documentos internos y propuestas.

El siguiente paso seguro es preparar una ficha de datos pendientes para Daniel o, si Daniel aporta los datos, ejecutar un lote de validación de fuente oficial antes de pasar a schema.

## Próximo lote recomendado

`REQUIERE DECISION HUMANA`

Opción A, si Daniel puede aportar datos oficiales:

`MW-ENTITY-FACTUAL-OFFICIAL-DATA-INTAKE-015B1`

Opción B, si seguimos sin datos oficiales:

`MW-ENTITY-FACTUAL-SCHEMA-MINIMAL-PROPOSAL-015C`

La opción B solo debe usar campos mínimos: name, url y descripción prudente. Nada de address, contactPoint, sameAs, rating, legalName o foundingDate.

