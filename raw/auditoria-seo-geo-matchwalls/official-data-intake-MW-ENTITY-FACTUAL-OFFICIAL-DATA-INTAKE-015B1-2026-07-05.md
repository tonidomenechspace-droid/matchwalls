# MW-ENTITY-FACTUAL-OFFICIAL-DATA-INTAKE-015B1

Fecha: 2026-07-05 23:27 CEST  
Estado del documento: `VERIFICADO Y CORRECTO`  
Estado de datos oficiales: `INCOMPLETO`  
Tipo: plantilla de recogida de datos oficiales para entidad MatchWalls  
Ámbito: ES, EN, FR, DE, NL  

## Objetivo

Preparar una recogida segura de datos oficiales de MatchWalls para que, cuando Daniel los confirme, puedan alimentar futuros lotes de:

- schema `Organization` / `WebSite` / `ContactPoint` / `sameAs`;
- página corporativa o bloque “Sobre MatchWalls”;
- contenidos citables SEO/GEO/AEO;
- panel CEO/CMO;
- coherencia multidioma ES, EN, FR, DE y NL.

Este lote no valida datos nuevos porque Daniel todavía no ha aportado fuentes oficiales en esta conversación. Deja preparada la ficha exacta que debe rellenarse.

## Estado de partida

`VERIFICADO Y CORRECTO`

015B confirmó que sí se puede usar:

- nombre de marca: `MatchWalls`;
- dominio trabajado: `https://www.matchwalls.com/`;
- tipo operativo seguro: tienda online;
- oferta segura: papel pintado, murales decorativos y soluciones murales a medida;
- público seguro: hogares y proyectos profesionales;
- idiomas prioritarios: ES, EN, FR, DE y NL.

`INCOMPLETO`

Siguen pendientes:

- razón social;
- CIF/NIF/VAT;
- dirección legal;
- email oficial;
- teléfono oficial;
- perfiles oficiales;
- Trustpilot/reseñas;
- relación real con Barcelona;
- historia / “desde 1961”;
- fabricación / producción;
- certificaciones;
- políticas de envío, devolución y garantía;
- autores o revisores expertos.

## Cómo debe rellenarse la ficha

`VERIFICADO Y CORRECTO`

Cada dato debe venir con:

1. valor exacto;
2. fuente;
3. si es publicable o solo interno;
4. fecha o vigencia;
5. idioma o mercado afectado;
6. permiso de uso en schema/copy si aplica.

Si un dato es verdadero pero no debe publicarse, se marca como `VERIFICADO Y CORRECTO` para uso interno y `NO ACCESIBLE` o `REQUIERE DECISION HUMANA` para uso público/schema.

## Datos críticos que Daniel debe aportar

`REQUIERE DECISION HUMANA`

### 1. Legal

- Razón social exacta.
- CIF/NIF/VAT/tax ID.
- Si esos datos deben publicarse o solo conservarse internamente.
- Dirección legal.
- Si la dirección es publicable.

### 2. Contacto

- Email oficial de atención al cliente.
- Teléfono oficial, si existe.
- Idiomas de atención reales: ES, EN, FR, DE, NL u otros.
- Horario si debe publicarse.

### 3. Perfiles oficiales

- Instagram.
- Pinterest.
- TikTok.
- YouTube.
- LinkedIn.
- Facebook.
- Trustpilot.
- Otros perfiles oficiales.

### 4. Historia y ubicación

- Si puede decirse “desde 1961”.
- A qué entidad pertenece ese claim histórico.
- Si MatchWalls puede decir “Barcelona”, “desde Barcelona” o “from Barcelona”.
- Fórmula exacta aprobada por marca/legal.

### 5. Fabricación y materiales

- Si MatchWalls fabrica, diseña, produce bajo pedido, trabaja con proveedor externo o una combinación.
- País/lugar de producción publicable.
- Materiales con nombre oficial.
- Certificados o fichas técnicas.
- Claims permitidos: lavable, ignífugo, sostenible, PVC-free, FSC, tintas, etc.

### 6. Políticas comerciales

- Envío gratis: sí/no, mercados, condiciones.
- Plazos de producción.
- Plazos de entrega.
- Aduanas.
- Devoluciones.
- Garantías.
- Política específica de muestras.

### 7. Autoridad editorial

- Persona o equipo responsable de contenidos.
- Expertos/revisores técnicos.
- Cargo y permiso de publicación.
- Bio breve por idioma si se quiere reforzar E-E-A-T.

## Regla de decisión

`VERIFICADO Y CORRECTO`

- Si el dato tiene fuente oficial y permiso público: puede proponerse para copy y schema.
- Si el dato tiene fuente oficial pero es interno: no se publica, pero se usa para gobernanza.
- Si el dato aparece en backups antiguos: no se usa.
- Si el dato aparece en páginas afectadas por deuda/caché: no se usa hasta QA estable.
- Si el dato es una inferencia: no se usa.

## Uso permitido antes de recibir datos

`VERIFICADO Y CORRECTO`

Mientras no recibamos datos oficiales, el siguiente lote sí puede preparar un schema mínimo:

- `Organization.name`
- `Organization.url`
- `Organization.description` prudente
- `WebSite.name`
- `WebSite.url`
- `WebPage.about` con contenido factual 015A

## Uso bloqueado antes de recibir datos

`REQUIERE DECISION HUMANA`

No preparar como implementación:

- `legalName`
- `taxID`
- `vatID`
- `PostalAddress`
- `LocalBusiness`
- `ContactPoint`
- `sameAs`
- `foundingDate`
- `manufacturer`
- `aggregateRating`
- `review`
- `hasCertification`
- `award`
- claims de envío/devoluciones/garantías

## Siguiente decisión

`REQUIERE DECISION HUMANA`

Daniel puede elegir:

1. Rellenar la plantilla de 015B1 y continuar con `MW-ENTITY-FACTUAL-OFFICIAL-DATA-VALIDATION-015B2`.
2. No aportar aún datos oficiales y continuar con `MW-ENTITY-FACTUAL-SCHEMA-MINIMAL-PROPOSAL-015C`, limitado a campos seguros.

## Exclusiones respetadas

`VERIFICADO Y CORRECTO`

No se modificó Shopify, LangShop, Bing Webmaster Tools, IndexNow, Google, GA4, GSC, Cloudflare, tema, páginas, traducciones, schema, robots, sitemap, URLs, handles, redirecciones, productos, colecciones ni apps.

