# Backup previo - MW-I18N-HOME-H1-DE-NL-META-FIX-017B

Fecha: 2026-06-30  
Tienda: Matchwalls  
MAIN verificado: `gid://shopify/OnlineStoreTheme/178399019384`  
Nombre MAIN: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`

## Alcance aprobado

Lote aprobado por Daniel:

`APROBADO LOTE MW-I18N-HOME-H1-DE-NL-META-FIX-017B`

## Recursos Shopify

| Recurso | GID |
|---|---|
| Theme locale content MAIN | `gid://shopify/OnlineStoreThemeLocaleContent/178399019384` |
| Shop meta | `gid://shopify/Shop/67753083107` |

## Valores base y digests

| Recurso | Key | Locale base | Valor base | Digest |
|---|---|---:|---|---|
| Theme locale content | `general.logo.seo` | ES | `Papeles pintados para paredes y murales` | `b2099354e32a248fa31fbac631b9137744d347cc9c1d17cde71a07009e0116f9` |
| Shop | `meta_title` | ES | `MatchWalls - Papeles pintados que transforman tus espacios` | `7c521302d65b98579d0fe18500f65f5259446595396aa7a65947d9b0763d5b63` |
| Shop | `meta_description` | ES | `Papeles pintados y murales personalizados y a medida, perfectos para tu proyecto en vinilo autoadhesivo. Diseños únicos, envíos internacionales gratuitos.` | `72116edaa29618316c4604512acb1ea282bbf737dad99430abffb4b8cdc1446d` |

## Valores actuales antes de ejecutar

| Idioma | Key | Estado actual |
|---|---|---|
| DE | `general.logo.seo` | `Bemalten Papiere für Wände und Wandgemälde` |
| NL | `general.logo.seo` | `Matchwalls: Papeadra Papel -specialisten` |
| NL | `meta_title` | Sin traducción Shopify; render público heredaba ES |
| NL | `meta_description` | Sin traducción Shopify; render público heredaba ES |
| EN | `meta_title` / `meta_description` | Existe traducción, pero `outdated=true`; solo documentado, no incluido en escritura 017B |

## Valores propuestos

| Idioma | Key | Valor nuevo |
|---|---|---|
| DE | `general.logo.seo` | `Tapeten und Wandbilder für jeden Raum` |
| NL | `general.logo.seo` | `Behang en fotobehang voor elke ruimte` |
| NL | `meta_title` | `MatchWalls - Behang en fotobehang die je ruimtes transformeren` |
| NL | `meta_description` | `Gepersonaliseerd behang en fotobehang op maat, perfect voor je project met zelfklevend vinyl. Unieke ontwerpen, gratis internationale verzending.` |

## Método de reversión

Aplicar `translationsRegister` sobre los mismos recursos, claves y digests, restaurando los valores de la sección "Valores actuales antes de ejecutar".  
Para NL `meta_title` y `meta_description`, si se requiere reversión exacta al estado previo, usar `translationsRemove` para eliminar esas dos claves en locale `nl` del recurso `gid://shopify/Shop/67753083107`.

Nota técnica: el valor base ES de `general.logo.seo` contiene un espacio no separable (`U+00A0`) antes de `murales`. El primer digest calculado con espacio normal fue rechazado por Shopify y no aplicó cambios.

## Pruebas posteriores previstas

- QA público de home ES, EN, FR, DE y NL.
- Validar HTTP 200, H1, title, meta description, canonical, lang y hreflang.
- Confirmar que ES/EN/FR no cambian en contenido crítico.
- Confirmar en Admin que NL shop meta queda registrada.
