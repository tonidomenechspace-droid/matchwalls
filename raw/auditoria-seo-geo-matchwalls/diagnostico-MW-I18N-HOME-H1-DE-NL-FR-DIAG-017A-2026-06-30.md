# Diagnostico MW-I18N-HOME-H1-DE-NL-FR-DIAG-017A

Fecha: 2026-06-30  
Tipo: diagnostico de solo lectura  
Estado final: `INCORRECTO`  
Shopify modificado: no

## 1. Objetivo

Revalidar la home en idiomas prioritarios, con foco en:

- H1 de DE y NL.
- Posibles errores 500 transitorios en FR/EN.
- Title y meta description.
- Canonical, hreflang, robots y `html lang`.
- Origen probable del problema respetando que las traducciones se trabajan con Shopify Translate & Adapt y LangShop.

## 2. Documentos y contexto revisados

- `plan-operativo-vigente-y-cola-lotes-seo-geo-2026-06-30.md`.
- `cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`.
- `estado-operativo-consolidado-seo-geo-2026-06-30.md`.
- `registro-cambios-ejecutados.md`.
- Historico local de tema `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E`.
- Evidencias historicas `auditoria-contenido-i18n-geo-2026-06-16.md` e `inventario-problemas-contenido-i18n-geo-2026-06-16.csv`.

## 3. Estado publico verificado

Archivo:

- `qa-publico-MW-I18N-HOME-H1-DE-NL-FR-DIAG-017A-2026-06-30.csv`.

Resumen:

| Idioma | Estado | H1 | Title | Nota |
|---|---|---|---|---|
| ES | `VERIFICADO Y CORRECTO` | `Papeles pintados para paredes y murales` | Correcto ES | Control correcto |
| EN | `VERIFICADO PERO MEJORABLE` | `Wallpapers and photomurals for all spaces` | Correcto EN | 2 errores 500 iniciales; 10/10 reintentos posteriores 200 |
| FR | `VERIFICADO PERO MEJORABLE` | `Papiers peints pour murs et peintures murales` | Correcto FR | 1 error 500 transitorio; reintentos posteriores 200 |
| DE | `INCORRECTO` | `Bemalten Papiere für Wände und Wandgemälde` | Correcto DE | H1 gramaticalmente deficiente |
| NL | `INCORRECTO` | `Matchwalls: Papeadra Papel -specialisten` | Title ES | H1 incorrecto y metadatos NL heredados en español |

## 4. Hallazgos tecnicos

### 4.1 MAIN real

Consulta Admin Shopify de solo lectura:

- Tema MAIN: `gid://shopify/OnlineStoreTheme/178399019384`.
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`.
- LangShop app embed detectado activo en `config/settings_data.json`.

Estado: `VERIFICADO Y CORRECTO`.

### 4.2 Origen del H1

El H1 de la home se renderiza dentro de `sections/slideshow.liquid` mediante:

`{{ 'general.logo.seo' | t }}`

En el historico local del tema, la clave `general.logo.seo` contiene:

| Idioma | Valor |
|---|---|
| ES | `Papeles pintados para paredes y murales` |
| EN | `Wallpapers and photomurals for all spaces` |
| FR | `Papiers peints pour murs et peintures murales` |
| DE | `Bemalten Papiere für Wände und Wandgemälde` |
| NL | `Matchwalls: Papeadra Papel -specialisten` |

La lectura Admin del MAIN confirma en `locales/de.json` el valor DE incorrecto para `general.logo.seo`.

Estado:

- DE: `INCORRECTO`.
- NL: `INCORRECTO`.

Interpretacion:

- No es un fallo de JavaScript.
- No es un problema de redireccion.
- Es deuda de traduccion/locale/theme translation.
- Debe corregirse mediante Shopify Translate & Adapt / LangShop o el flujo autorizado de traducciones, no parcheando HTML renderizado.

### 4.3 Title/meta description NL

Consulta Admin Shopify de solo lectura sobre `shop.translations`:

| Idioma | `meta_title` | `meta_description` | Estado |
|---|---|---|---|
| DE | existe | existe | `VERIFICADO Y CORRECTO` |
| FR | existe | existe | `VERIFICADO Y CORRECTO` |
| EN | existe, marcado `outdated=true` | existe, marcado `outdated=true` | `VERIFICADO PERO MEJORABLE` |
| NL | no existe | no existe | `INCORRECTO` |

Efecto publico:

- Home NL renderiza title y meta description en español.

Estado: `INCORRECTO`.

## 5. Impacto SEO/GEO

Impacto: alto.

Motivo:

- La home es una URL central de entidad y navegacion internacional.
- DE y NL son idiomas prioritarios.
- Un H1 incorrecto reduce claridad semantica para Google, Bing, Yahoo, Brave Search y sistemas IA.
- En NL, title y description en español pueden reducir relevancia, CTR, snippets y comprension de idioma.
- Los 500 transitorios EN/FR no se consideran caida estable, pero deben monitorizarse porque afectan rastreo si se repiten.

## 6. Riesgos

- Si se corrige el archivo Liquid o locale directamente sin respetar Shopify Translate & Adapt/LangShop, LangShop o el editor de idioma puede sobrescribir el cambio.
- Si se corrige solo el H1 y no el title/meta NL, el problema de snippet NL permanece.
- Si se toca la home desde el editor visual sin control, puede alterarse contenido del slideshow y no solo la traduccion.

## 7. Recomendacion

Crear lote de correccion acotado:

`MW-I18N-HOME-H1-DE-NL-META-FIX-017B`

Alcance propuesto:

- Corregir `general.logo.seo` en DE.
- Corregir `general.logo.seo` en NL.
- Crear traducciones NL de `shop.meta_title` y `shop.meta_description`.
- Revalidar EN porque sus traducciones shop-level existen pero aparecen `outdated=true`.
- No tocar FR salvo monitorizacion del 500 transitorio.
- No tocar ES.
- No modificar tema Liquid salvo que se demuestre que Shopify Translate & Adapt/LangShop no puede gestionar la clave.

## 8. Valores propuestos para revisar antes de aprobar

Estos valores son propuesta inicial y deben validarse editorialmente antes de escritura:

| Campo | Actual | Propuesto |
|---|---|---|
| DE `general.logo.seo` | `Bemalten Papiere für Wände und Wandgemälde` | `Tapeten und Wandbilder für jeden Raum` |
| NL `general.logo.seo` | `Matchwalls: Papeadra Papel -specialisten` | `Behang en fotobehang voor elke ruimte` |
| NL `meta_title` | heredado en ES | `MatchWalls - Behang en fotobehang die je ruimtes transformeren` |
| NL `meta_description` | heredado en ES | `Gepersonaliseerd behang en fotobehang op maat, perfect voor je project met zelfklevend vinyl. Unieke ontwerpen, gratis internationale verzending.` |

Nota:

- La propuesta evita inventar claims nuevos.
- Mantiene la intencion comercial de ES/EN/FR.
- Debe aplicarse en el sistema de traducciones correcto: Shopify Translate & Adapt / LangShop.

## 9. Siguiente aprobacion requerida

Para preparar y ejecutar la correccion, Daniel debe aprobar exactamente:

`APROBADO LOTE MW-I18N-HOME-H1-DE-NL-META-FIX-017B`

Antes de ejecutar escritura se debe presentar propuesta formal con:

- recurso exacto;
- claves;
- valores actuales;
- valores propuestos;
- via de escritura: Shopify Translate & Adapt, LangShop o Admin translation API;
- respaldo;
- reversion;
- QA posterior ES/EN/FR/DE/NL desktop/mobile.
