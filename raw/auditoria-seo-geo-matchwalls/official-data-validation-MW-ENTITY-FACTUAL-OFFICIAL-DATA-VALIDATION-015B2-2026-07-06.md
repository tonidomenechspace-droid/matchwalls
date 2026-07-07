# MW-ENTITY-FACTUAL-OFFICIAL-DATA-VALIDATION-015B2

Fecha: 2026-07-06  
Hora de trabajo: 10:15 CEST  
Tipo: validación documental local de datos oficiales aportados por Daniel  
Estado general: `VERIFICADO PERO MEJORABLE`

## Alcance

Este lote valida la entrada oficial recibida de Daniel para continuar construyendo la entidad factual de MatchWalls en ES, EN, FR, DE y NL.

No se ha modificado Shopify, LangShop, Bing Webmaster Tools, IndexNow, Google, Cloudflare, tema, schema público, páginas, traducciones, metadatos, URLs, handles, redirecciones, productos, colecciones ni apps.

## Fuente usada

Fuente directa: mensaje de Daniel en el chat del proyecto, recibido el 2026-07-06.

Importante: esta fuente se considera confirmación interna escrita del responsable del proyecto. No equivale por sí sola a una verificación externa en registro mercantil, certificado fiscal, política pública, documento legal, Trustpilot, ficha técnica o fuente de terceros.

## Datos exactos recibidos

| Campo | Valor aportado | Estado | Uso permitido ahora |
| --- | --- | --- | --- |
| Razón social | Match Projects International S.L | `VERIFICADO Y CORRECTO` | Preparar propuesta de Organization.legalName. No implementar sin lote aprobado. |
| CIF/NIF/VAT | B70959283 | `VERIFICADO Y CORRECTO` | Preparar propuesta de Organization.taxID/vatID. No implementar sin lote aprobado. |
| Dirección legal | Avd Catalunya 9 -08060 | `INCOMPLETO` | No usar todavía en PostalAddress ni LocalBusiness. Falta formato completo. |
| Teléfono | 675916340 | `VERIFICADO PERO MEJORABLE` | No usar todavía en schema público. Falta formato internacional y permiso de uso público. |
| Email oficial para schema | help@matchwalls.com | `VERIFICADO Y CORRECTO` | Preparar propuesta de ContactPoint.email. No implementar sin lote aprobado. |

## Datos mencionados pero no cerrados

| Tema | Estado | Motivo |
| --- | --- | --- |
| Perfiles oficiales sameAs | `INCOMPLETO` | No se han aportado URLs exactas oficiales. |
| "Desde 1961" | `REQUIERE DECISION HUMANA` | Falta fuente, alcance legal y frase exacta aprobada. No está claro si aplica a MatchWalls, grupo, taller, familia o proveedor. |
| Barcelona como sede/origen | `REQUIERE DECISION HUMANA` | Falta frase exacta publicable y relación precisa: sede legal, origen creativo, oficina, estudio, almacén u otra. |
| Fabricación propia | `REQUIERE DECISION HUMANA` | Falta descripción precisa del modelo real de fabricación y límites del claim. |
| Certificaciones y sostenibilidad | `NO ACCESIBLE` | No se han aportado certificados, fichas técnicas ni textos legales verificables. |
| Envío gratis, plazos, devoluciones y garantías | `REQUIERE DECISION HUMANA` | Faltan condiciones por mercado, excepciones, plazos y textos legales vigentes. |
| Trustpilot y reseñas | `NO ACCESIBLE` | Falta URL oficial, rating actual, permisos y criterio de uso. |
| Autores y revisores expertos | `NO ACCESIBLE` | Faltan nombres, cargos, bios, permisos y alcance editorial. |

## Decisiones de seguridad

- No se usará la dirección en schema hasta tener calle normalizada, número, código postal, ciudad, provincia o región, país y confirmación de publicabilidad.
- No se convertirá el teléfono `675916340` a formato internacional sin confirmación explícita.
- No se añadirá ningún perfil `sameAs` sin URL oficial exacta.
- No se usará el claim `desde 1961` sin fuente y frase aprobada.
- No se afirmará fabricación propia, certificaciones, sostenibilidad, envío gratis, garantías ni rating sin evidencia concreta.
- No se implementará ningún dato en Shopify sin `APROBADO LOTE [...]`.

## Impacto sobre schema futuro

Campos que pasan a estar preparados para propuesta, no para publicación automática:

- `Organization.legalName`
- `Organization.taxID`
- `Organization.vatID`
- `ContactPoint.email`

Campos que siguen bloqueados o incompletos:

- `Organization.address`
- `PostalAddress`
- `LocalBusiness`
- `Organization.sameAs`
- `Organization.foundingDate`
- `Product.manufacturer`
- `hasCertification`
- `OfferShippingDetails`
- `MerchantReturnPolicy`
- `AggregateRating`
- `Article.author`
- `Article.reviewedBy`

## Próximo paso recomendado

Opción A, si Daniel quiere completar los datos oficiales antes de preparar schema:

`MW-ENTITY-FACTUAL-OFFICIAL-DATA-COMPLETION-015B3`

Opción B, si Daniel quiere avanzar con solo los campos ya suficientemente seguros:

`MW-ENTITY-FACTUAL-SCHEMA-PROPOSAL-015C`

La opción B debe excluir dirección, teléfono, sameAs, 1961, fabricación, certificaciones, políticas, Trustpilot y autores hasta recibir datos completos.

