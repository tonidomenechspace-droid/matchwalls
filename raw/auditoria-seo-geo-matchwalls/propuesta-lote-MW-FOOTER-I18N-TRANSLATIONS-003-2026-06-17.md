# Propuesta de lote MW-FOOTER-I18N-TRANSLATIONS-003 - 2026-06-17

Estado: PROPUESTA - NO EJECUTADA

## 1. Motivo

El lote `MW-FOOTER-NAV-GLOBAL-002` corrigió los menús fuente ES y retiró del footer publicado:

- `Tarjeta regalo`
- `Black Friday 2024`
- `Envíos internacionales`

La QA pública confirma que esos enlaces ya no aparecen en ES, EN, FR, DE ni NL.

Pero siguen activas traducciones antiguas o deficientes en EN, FR, DE y NL:

- EN: `FAQ´S - Shipping and Returns`
- FR: cabeceras fuente españolas `PROFESIONALES`, `EMPRESA`, `AYUDA Y SOPORTE`
- DE: traducciones literales/mejorables
- NL: cabeceras fuente españolas, `FAQ´s` y traducción incorrecta `schaamruimtes`

## 2. Alcance propuesto

Corregir solo traducciones visibles de navegación del footer para:

- EN
- FR
- DE
- NL

No se tocará ES porque la fuente ya quedó corregida.

## 3. Recursos afectados

Menús:

- `footer`: `gid://shopify/Menu/210266325219`
- `footer-profesional`: `gid://shopify/Menu/210972311779`
- `footer-brand`: `gid://shopify/Menu/210972344547`
- `footer-legal`: `gid://shopify/Menu/210972410083`

## 4. Preflight obligatorio

Antes de escribir traducciones:

1. Consultar `translatableResource` de cada menú.
2. Exportar claves traducibles y `digest`.
3. Identificar si las traducciones de ítems están bajo el menú o bajo recursos anidados.
4. Guardar respaldo local de traducciones actuales.
5. Validar `translationsRegister`.

Si Shopify no expone claves de ítems de menú mediante este conector, detenerse y marcar `NO ACCESIBLE`.

## 5. Valores propuestos EN

### `footer-profesional`

- Título: `PROFESSIONALS`
- `B2B interior design stores`
- `B2B interior design and architecture studios, hotels and public spaces`
- `B2B hotels and contract projects`
- `Social, press and affiliates`
- `Artists and designers`
- `Request your sample`

### `footer-brand`

- Título: `COMPANY`
- `About us`
- `Our products`
- `Sustainability`
- `Inspiration`

### `footer`

- Título: `HELP AND SUPPORT`
- `FAQ - Shipping and returns`
- `Create your own wallpaper`
- `Create your custom mural`
- `How to measure walls`
- `How to measure the ceiling`
- `Your Privacy Choices`

### `footer-legal`

- Título: `LEGAL`
- `Legal notice`
- `Cookie policy`
- `Website terms of use`
- `Online sales terms`

## 6. Valores propuestos FR

### `footer-profesional`

- Título: `PROFESSIONNELS`
- `Boutiques de décoration intérieure B2B`
- `Studios d’architecture et de décoration intérieure B2B, hôtels et espaces publics`
- `Hôtels et projets contract B2B`
- `Social, presse et affiliation`
- `Artistes et designers`
- `Demander votre échantillon`

### `footer-brand`

- Título: `ENTREPRISE`
- `À propos de nous`
- `Nos produits`
- `Durabilité`
- `Inspiration`

### `footer`

- Título: `AIDE ET SUPPORT`
- `FAQ - Livraison et retours`
- `Créez votre papier peint`
- `Créez votre fresque murale personnalisée`
- `Comment mesurer les murs`
- `Comment mesurer le plafond`
- `Vos choix de confidentialité`

### `footer-legal`

- Título: `LÉGAL`
- `Avis juridique`
- `Politique relative aux cookies`
- `Conditions d’utilisation du site`
- `Conditions de vente en ligne`

## 7. Valores propuestos DE

### `footer-profesional`

- Título: `FÜR FACHKUNDEN`
- `B2B Einrichtungsfachgeschäfte`
- `B2B Innenarchitektur- und Architekturbüros, Hotels und öffentliche Räume`
- `B2B Hotels und Objektprojekte`
- `Social, Presse und Affiliate`
- `Künstler und Designer`
- `Muster anfordern`

### `footer-brand`

- Título: `UNTERNEHMEN`
- `Über uns`
- `Unsere Produkte`
- `Nachhaltigkeit`
- `Inspiration`

### `footer`

- Título: `HILFE UND SUPPORT`
- `FAQ - Versand und Rückgabe`
- `Erstelle deine eigene Tapete`
- `Erstelle dein individuelles Wandbild`
- `Wände richtig messen`
- `Decke richtig messen`
- `Datenschutzoptionen`

### `footer-legal`

- Título: `RECHTLICHES`
- `Impressum`
- `Cookie-Richtlinie`
- `Nutzungsbedingungen der Website`
- `Online-Verkaufsbedingungen`

## 8. Valores propuestos NL

### `footer-profesional`

- Título: `PROFESSIONALS`
- `B2B interieurwinkels`
- `B2B interieur- en architectuurstudio’s, hotels en openbare ruimtes`
- `B2B hotels en contractprojecten`
- `Social, pers en affiliatie`
- `Kunstenaars en ontwerpers`
- `Vraag je staal aan`

### `footer-brand`

- Título: `BEDRIJF`
- `Over ons`
- `Onze producten`
- `Duurzaamheid`
- `Inspiratie`

### `footer`

- Título: `HULP EN SUPPORT`
- `FAQ - Verzending en retouren`
- `Maak je eigen behang`
- `Maak je gepersonaliseerde muurschildering`
- `Zo meet je muren`
- `Zo meet je het plafond`
- `Privacykeuzes`

### `footer-legal`

- Título: `JURIDISCH`
- `Juridische kennisgeving`
- `Cookiebeleid`
- `Gebruiksvoorwaarden van de website`
- `Online verkoopvoorwaarden`

## 9. Riesgos

- Las claves de traducción de ítems de menú podrían no estar accesibles desde el conector actual.
- LangShop puede sobrescribir o interferir con traducciones nativas.
- `Your Privacy Choices` puede tener implicaciones legales; se propone localizarlo de forma descriptiva, pero debe validarse si se prefiere conservarlo en inglés.
- Las etiquetas B2B deben revisarse editorialmente si MatchWalls prefiere otro tono de marca.

## 10. QA posterior

Revisar footer público en:

- `/en`
- `/fr`
- `/de`
- `/nl`

Comprobar ausencia de:

- `FAQ´S`
- `FAQ´s`
- `Professional & social`
- `brand`
- `PROFESIONALES`
- `EMPRESA`
- `AYUDA Y SOPORTE`
- `schaamruimtes`
- `B2B Hotels & Contact`

## 11. Aprobación requerida

Para ejecutar este lote, Daniel debe responder exactamente:

`APROBADO LOTE MW-FOOTER-I18N-TRANSLATIONS-003`

Hasta recibir esa frase exacta:

- no se escribirán traducciones;
- no se ejecutará `translationsRegister`;
- no se tocarán otros recursos.

## 12. Estado final de esta propuesta

Clasificación: `REQUIERE DECISION HUMANA`
