# HANDOFF CHATGPT/API — MATCHWALLS SEO/GEO

**Lote:** MW-CHATGPT-API-OPERATING-HANDOFF-000  
**Fecha:** 2026-07-01  
**Origen:** ChatGPT con acceso Shopify Admin GraphQL API en modo controlado  
**Destino documental local recomendado:**  
`C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\handoffs-chatgpt-api\`

---

## 1. Estado de trabajo

Daniel no dispone actualmente de créditos suficientes de Codex, por lo que el trabajo operativo se reorganiza así:

- ChatGPT trabajará desde aquí con Shopify API y estrategia SEO/GEO/AEO.
- Codex quedará en pausa hasta disponer de créditos.
- Todo trabajo realizado aquí se documentará en archivos handoff para que Codex pueda retomarlo más adelante sin perder contexto.
- No se ejecutarán escrituras en Shopify sin aprobación exacta de Daniel.
- La carpeta local de Codex seguirá siendo la fuente documental maestra cuando vuelva a estar disponible.

---

## 2. Reglas de gobierno

Reglas vigentes:

1. Lecturas y auditorías: autorizadas.
2. Escrituras Shopify, tema, robots, redirects, schema, contenidos o integraciones: requieren propuesta formal.
3. La aprobación debe ser exacta: `APROBADO LOTE [NOMBRE]`.
4. Ningún lote debe mezclar tema, productos, redirects, contenidos y medición externa.
5. Cada lote debe cerrar con evidencia, QA y reversión documentada.
6. ES, EN, FR, DE y NL son idiomas prioritarios.
7. IT y PT-PT quedan en FASE 2, salvo limpieza mínima defensiva.
8. Safari / Applebot / Apple Intelligence deben incluirse en la auditoría de crawlers.
9. No se deben crear, noindexar ni modificar landings geográficas estratégicas sin decisión humana.

---

## 3. Datos Shopify API comprobados desde ChatGPT

Consulta de solo lectura ejecutada contra Shopify Admin GraphQL API.

| Elemento | Resultado |
|---|---:|
| Tienda | Matchwalls |
| Dominio principal | https://www.matchwalls.com |
| Moneda | EUR |
| Zona horaria | Europe/Madrid |
| Productos | 3.022 |
| Colecciones | 109 |
| Páginas | 55 |
| Redirects | 604 |
| Idioma primario | ES |
| Idiomas publicados | ES, EN, FR, DE, NL, IT, PT-PT |
| Idiomas no publicados detectados | AR, DA, EL, FI, HE, HI, HU, JA, KO, NO, PL, RU, SV, ZH-CN |

---

## 4. Estrategia de mercados acordada

### FASE 1 — Prioritaria

Mercados principales:

- España — ES
- Francia — FR
- Alemania — DE
- Países Bajos — NL
- UK — EN-UK
- Bélgica — FR/NL
- USA — EN-US
- México — ES-MX

### FASE 2 — Posterior

- Italia — IT
- Portugal — PT-PT
- Otros países europeos o internacionales

### Regla para IT/PT en FASE 1

Italia y Portugal quedan en STANDBY / FASE 2.  
En FASE 1 solo se permite limpieza mínima defensiva:

- 404 críticos;
- redirects incorrectos;
- noindex accidental;
- hreflang roto;
- sitemap contaminado;
- contenido vacío;
- fallos técnicos graves.

No crear landings nuevas IT/PT.  
No optimizar contenido editorial IT/PT.  
No ejecutar estrategia GEO IT/PT.  
No solicitar indexación manual IT/PT.

---

## 5. Alcance SEO/GEO/AEO multientorno

La auditoría debe cubrir:

- Google / Chrome / Gemini / AI Overviews
- Bing / Edge / Copilot
- Yahoo
- Opera
- Brave Search
- Safari / Applebot / Siri / Spotlight / Apple Intelligence
- ChatGPT / OAI-SearchBot
- Claude / Claude-SearchBot
- Perplexity / Comet
- Grok / xAI
- Meta AI
- Otros motores IA con web-search

Safari no debe quedar fuera. Debe existir bloque específico para Applebot, Applebot-Extended, iOS Safari, snippets y acceso a JS/CSS.

---

## 6. Hallazgos relevantes ya observados desde Shopify API

1. IT y PT-PT están publicados aunque no son fase prioritaria.
2. No se detectaron landings país maduras en colecciones para Alemania, Países Bajos, UK, Bélgica o México mediante búsquedas API iniciales.
3. Existen páginas antiguas:
   - `papel-pintado-espana`
   - `papel-pintado-francia`
   - `envios-internacionales`
4. Existen múltiples landings provinciales ES del patrón `comprar-papel-pintado-*`, muchas con 73 productos exactos.
5. Ese patrón sugiere riesgo de landings repetitivas o de bajo valor si no se enriquecen editorialmente.
6. No se debe noindexar masivamente sin separar:
   - estratégicas,
   - candidatas a mejora,
   - candidatas a noindex,
   - standby.

---

## 7. Próximo trabajo recomendado desde ChatGPT/API

Crear lote:

`MW-SEO-GEO-MARKET-STRATEGY-AUDIT-012A`

Tipo: solo lectura / diagnóstico.

Objetivo:

- auditar arquitectura de mercados e idiomas en Shopify;
- identificar landings existentes y ausentes;
- separar FASE 1 vs FASE 2;
- detectar riesgo IT/PT sin optimizarlos todavía;
- mapear landings prioritarias por país;
- definir plan capaz de competir con Photowall, Rebel Walls y Wallism;
- preparar handoff para Codex.

No ejecutar escrituras.

---

## 8. Qué debe hacer Codex cuando vuelva

Cuando Codex vuelva a estar disponible:

1. Leer este handoff.
2. Guardarlo en:
   `C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\handoffs-chatgpt-api\`
3. No repetir diagnósticos ya cerrados salvo discrepancia.
4. No ejecutar escrituras sin aprobación exacta.
5. Actualizar la cola maestra y el plan operativo solo con evidencias reales.
6. Usar este handoff como contexto adicional, no como sustituto de evidencias Shopify/GSC/sitemap.
7. STOP si detecta discrepancias con Shopify, sitemap, Search Console o archivos locales.

---

## 9. Pendiente de decisión humana

- Confirmar lista exacta de landings país/city FASE 1.
- Confirmar si UK y USA tendrán URLs diferenciadas o contenido market-specific bajo idioma EN.
- Confirmar si México tendrá contenido ES-MX diferenciado o landing país inicial.
- Confirmar política IT/PT: mantener publicado con limpieza mínima o aplicar noindex parcial si hay ruido crítico.
- Confirmar política de bots IA: permitir search/citation bots y decidir qué hacer con training bots.

---

## 10. STOP

Este archivo no implica cambios en Shopify.  
Es un handoff documental para preservar contexto mientras Codex no está disponible.
