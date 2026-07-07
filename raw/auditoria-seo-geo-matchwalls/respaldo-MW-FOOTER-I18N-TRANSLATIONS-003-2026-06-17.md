# Respaldo lote MW-FOOTER-I18N-TRANSLATIONS-003 - 2026-06-17

Fecha y hora local: 2026-06-17 10:45:11 +02:00

Estado: respaldo previo a escritura.

Lote aprobado por Daniel:

`APROBADO LOTE MW-FOOTER-I18N-TRANSLATIONS-003`

## Alcance

Traducciones de navegación del footer para EN, FR, DE y NL.

No incluye:

- Tema Shopify.
- Publicación de tema.
- ES fuente.
- Productos, colecciones, páginas, handles, URLs, redirecciones, precios, inventario, variantes, imágenes ni App Embeds.

## Hallazgo de preflight

Shopify expone:

- Títulos de menús como recursos `MENU`.
- Títulos de enlaces como recursos `LINK`.

Los IDs `gid://shopify/MenuItem/...` no son válidos para `translatableResourcesByIds`.
La forma traducible correcta para los enlaces es `gid://shopify/Link/...`, usando el mismo ID numérico del ítem.

## Menús: valores actuales antes de escritura

| Recurso | Handle | Fuente ES | Digest | EN actual | FR actual | DE actual | NL actual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gid://shopify/Menu/210266325219` | `footer` | `AYUDA Y SOPORTE` | `33c1af6aa950dd4b794e245ab90254e995b6411c26d190cf5160518c40909814` | `Help &amp; support` / outdated `true` | sin traducción | `Hilfe Unterstützung` / outdated `true` | sin traducción |
| `gid://shopify/Menu/210972311779` | `footer-profesional` | `PROFESIONALES` | `4e6cf2cd629bfbf00458bc16e50190c6fa018e8b123d5568e2132b3527636226` | `Professional &amp; social` / outdated `true` | sin traducción | `Professionell und sozial` / outdated `true` | sin traducción |
| `gid://shopify/Menu/210972344547` | `footer-brand` | `EMPRESA` | `a75d07f844b6377e17c603eadd920d87685677c3016a9c55e563a0fec84dbd1a` | `brand` / outdated `true` | sin traducción | `Marke` / outdated `true` | sin traducción |
| `gid://shopify/Menu/210972410083` | `footer-legal` | `LEGAL` | `ab0730acb114a4ef42c2b4e3d80cf0f3a580ff5d4cd54a2d6c2a3d75c05c952b` | sin traducción | sin traducción | sin traducción | sin traducción |

## Enlaces: valores actuales antes de escritura

| Recurso | Fuente ES | Digest | EN actual | FR actual | DE actual | NL actual |
| --- | --- | --- | --- | --- | --- | --- |
| `gid://shopify/Link/495449178339` | `FAQ - Envíos y devoluciones` | `0546594d31729745c358a2fab4e370fe3e08b0279900cc2be10cc16357532cbd` | `FAQ´S - Shipping and Returns` / outdated `true` | `FAQ - Expédition et retours` / outdated `true` | `FAQs - Versand und Rückgaben` / outdated `true` | `FAQ´s - Verzending en retouren` / outdated `true` |
| `gid://shopify/Link/495449211107` | `Crea tu propio papel pintado` | `00bdfd5296abb31e546954e7a15372b3e5bb2ca8cd2c912fa4eb2ce1f69507a9` | `Create your own roll wallpaper` / outdated `true` | `Créez votre propre rouleau de papier peint` / outdated `true` | `Erstellen Sie Ihre eigene Tapetenrolle` / outdated `true` | `Maak je eigen wallpaper roll` / outdated `true` |
| `gid://shopify/Link/495449243875` | `Crea tu mural personalizado` | `2d692e04762de6d06815f35471c8e15ce43a3fc0a5bbc0d8d67896763edd9223` | `Create your personalized wallpaper` / outdated `true` | `Créez votre papier peint mural personnalisé` / outdated `true` | `Erstellen Sie Ihr personalisiertes Wandbild` / outdated `true` | `Creëer uw gepersonaliseerde muurschildering Wallpaper` / outdated `true` |
| `gid://shopify/Link/497161568483` | `Cómo tomar medidas de paredes` | `7dc43e274f1f56717e3d6cbe184660e5216b6b2b9903e45df2e2eb58de3f3225` | `How to take wall measurements` / outdated `false` | `Comment prendre des mesures murales` / outdated `false` | `Wie man Wandmessungen durchnimmt` / outdated `false` | `Hoe u muurmetingen kunt uitvoeren` / outdated `false` |
| `gid://shopify/Link/497161601251` | `Cómo tomar medidas del techo` | `f5c332111976cb358ed38f47f888083165bc1d07427e73ba4fc0edec3f1c527a` | `How to measure the ceiling` / outdated `false` | `Comment prendre des mesures de plafond` / outdated `false` | `Wie man Deckenmaßnahmen ergriffen` / outdated `false` | `Hoe plafondmaatregelen te nemen` / outdated `false` |
| `gid://shopify/Link/713118876024` | `Your Privacy Choices` | `001864d2932255db0a3819bc170a979c88acd17878ac849c0cf1c16994f309a4` | `Do not Sell or Share My Personal Information` / outdated `true` | `Ne vendez ni ne partagez mes informations personnelles` / outdated `true` | `Verkaufen oder teilen Sie meine persönlichen Daten nicht oder teilen Sie sie nicht` / outdated `true` | `Verkoop of deel mijn persoonlijke informatie niet` / outdated `true` |
| `gid://shopify/Link/493556531427` | `B2B tiendas de interiorismo` | `ebab313e68fc14d1651de245b699fa13104e85c8ed5ee0ecc430373d17f23854` | `B2B Interior design stores` / outdated `true` | `Magasins de design d'intérieur B2B` / outdated `true` | `B2B Innenarchitekturgeschäfte` / outdated `true` | `B2B interieurontwerpwinkels` / outdated `true` |
| `gid://shopify/Link/493556564195` | `B2B estudios de interiorismo y arquitectura, hoteles y espacios públicos` | `372fca333612b326e0a2ef4a071d5ccb1c44d4e71936fef4dea9388eb79ccf65` | `B2B Interior design and architecture studies, hotels and public spaces.` / outdated `true` | `Études de design d'intérieur et d'architecture B2B, hôtels et espaces publics.` / outdated `true` | `B2B Innenarchitektur- und Architekturstudien, Hotels und öffentliche Räume.` / outdated `true` | `B2B interieurontwerp en architectuurstudies, hotels en schaamruimtes.` / outdated `true` |
| `gid://shopify/Link/503255138531` | `B2B hoteles y contract` | `dd9a9d28c3e22cf08dca773d412ce14a9dd31bc0cf3bfe8a94565caee31fa590` | `B2B Hotels & Contact` / outdated `true` | `Hôtels et contact B2B` / outdated `true` | `B2B -Hotels & Kontakt` / outdated `true` | `B2B Hotels & Contact` / outdated `true` |
| `gid://shopify/Link/493556596963` | `Social, prensa y afiliación` | `5a41626da3c935bc58b4c7bf9597ed9178a019ae26bc60d259333c715491162a` | `Social & Press and Affiliation` / outdated `true` | `Social & Press and Affiliation` / outdated `true` | `Sozial- und Presse und Zugehörigkeit` / outdated `true` | `Sociale en pers en aansluiting` / outdated `true` |
| `gid://shopify/Link/493556629731` | `Artistas y diseñadores` | `7efa51a3dde643c1611d7a69077e36fe370faef74c109ebb89fd62f5a6ecd2c4` | `Artists and Designers` / outdated `true` | `Artistes et designers` / outdated `true` | `Künstler und Designer` / outdated `true` | `Kunstenaars en ontwerpers` / outdated `true` |
| `gid://shopify/Link/495008121059` | `Solicita tu muestra` | `fe8fb1bb7458ab047ca4ad1f9965e9b808c1233253f9cc5c0669dc5865c02be2` | `Request your sample` / outdated `false` | `Demandez votre échantillon` / outdated `false` | `Fordern Sie Ihr Beispiel an` / outdated `false` | `Vraag uw monster aan` / outdated `false` |
| `gid://shopify/Link/494947959011` | `Sobre nosotros` | `75e53f49d8f698c34386adc8564dba06d0b175412d1d790afa5e5b1e88b08c79` | `About us` / outdated `true` | `À propos de nous` / outdated `true` | `Über uns` / outdated `true` | `Over ons` / outdated `true` |
| `gid://shopify/Link/494947926243` | `Nuestros productos` | `acaef4d60ec7fa6fe1ee009ec7e507da8c79c2dd80271fdc5f9a6ac6d4bb5795` | `Our products` / outdated `true` | `Nos produits` / outdated `true` | `Unsere Produkte` / outdated `true` | `Onze producten` / outdated `true` |
| `gid://shopify/Link/494947991779` | `Sostenibilidad` | `2e1996a743abd49c428ef8c8d2c52429a14489eed4fb39cb21f9f72fd4c7e696` | `Sustainability` / outdated `false` | `Durabilité` / outdated `false` | `Nachhaltigkeit` / outdated `false` | `Duurzaamheid` / outdated `false` |
| `gid://shopify/Link/494950613219` | `Inspiración` | `47bd2491f5923ad105c41a9591dc03e346b61f08b8b6ab76d936e8ae83c6b07b` | `Inspiration` / outdated `false` | `Inspiration` / outdated `false` | `Inspiration` / outdated `false` | `Inspiratie` / outdated `false` |
| `gid://shopify/Link/493557088483` | `Aviso legal` | `79e539a703dbcb93b5edab76fee0201eeaf39b11582b9fe214c63df6ee2623bf` | `Legal notice` / outdated `true` | `Avis juridique` / outdated `true` | `Rechtliche Bekanntmachung` / outdated `true` | `Wettelijke kennisgeving` / outdated `true` |
| `gid://shopify/Link/493557022947` | `Política de cookies` | `31477853657732c997c1ddc1d3482bd57bf24f0f96ec8b801e4d23d39217ce0f` | `Cookies policy` / outdated `true` | `Politique des cookies` / outdated `true` | `Cookies -Richtlinien` / outdated `true` | `Cookiesbeleid` / outdated `true` |
| `gid://shopify/Link/493557055715` | `Condiciones de uso de la web` | `738200897cbfbc7830e541442fd1b69f58aacb96d13023bed566570a0636680c` | `Web use conditions` / outdated `false` | `Conditions d'utilisation du Web` / outdated `false` | `Webnutzungsbedingungen` / outdated `false` | `Webgebruikomstandigheden` / outdated `false` |
| `gid://shopify/Link/496053289187` | `Condiciones de venta online` | `ab258807a2199695621ea90f9beb1704e465a4c0688a9c73ed5bcabbda7a1343` | `Online sales conditions` / outdated `false` | `Conditions de vente en ligne` / outdated `false` | `Online -Umsatzbedingungen` / outdated `false` | `Online verkoopvoorwaarden` / outdated `false` |

## Método de reversión

Ejecutar `translationsRegister` sobre los mismos recursos con:

- Misma `key`: `title`.
- Mismo `locale`.
- Valor anterior registrado en este respaldo.
- `translatableContentDigest` actualizado mediante una consulta previa a `translatableResource` o `translatableResourcesByIds`.

No usar este respaldo como sustituto del `digest` vigente si la fuente ES cambia después del lote.

## Estado

Clasificación previa a ejecución: `INCOMPLETO`.
