# HANDOFF CHATGPT/API — MW-SEO-GEO-MARKET-STRATEGY-AUDIT-012A

**Fecha:** 2026-07-01  
**Origen:** ChatGPT con acceso Shopify Admin GraphQL API  
**Modo:** Solo lectura / diagnóstico estratégico  
**Estado:** INCOMPLETO — diagnóstico inicial realizado, sin cambios Shopify  
**Destino local recomendado:**  
`C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\handoffs-chatgpt-api\`

---

## 1. Objetivo del lote

Ordenar la estrategia SEO/GEO/AEO internacional de MatchWalls sin depender de Codex, dejando un diagnóstico documentado para que Codex lo retome después.

Este lote no modifica Shopify.

Objetivos concretos:

- revisar arquitectura real de mercados, idiomas, páginas y colecciones desde Shopify API;
- separar FASE 1 y FASE 2;
- confirmar ausencia/presencia de landings país;
- identificar riesgo de landings geográficas repetitivas;
- dejar matriz de prioridades para competir mejor contra Photowall, Rebel Walls y Wallism;
- preparar handoff para Codex.

---

## 2. Datos leídos desde Shopify API

Consulta de solo lectura a Shopify Admin GraphQL.

| Elemento | Resultado |
|---|---:|
| Tienda | Matchwalls |
| Dominio principal | https://www.matchwalls.com |
| Productos | 3.022 |
| Colecciones | 109 |
| Páginas | 55 |
| Redirects | 604 |
| Idioma primario | ES |
| Idiomas publicados | ES, EN, FR, DE, NL, IT, PT-PT |

No se han ejecutado mutaciones.  
No se han cambiado productos, colecciones, páginas, redirects, tema, sitemap, robots, schema ni traducciones.

---

## 3. Estrategia de mercados acordada

### FASE 1 — Prioritaria

| Mercado | Idioma / enfoque | Estado estratégico |
|---|---|---|
| España | ES | Prioridad alta |
| Francia | FR | Prioridad alta |
| Alemania | DE | Prioridad alta |
| Países Bajos | NL | Prioridad alta |
| UK | EN-UK | Prioridad alta |
| Bélgica | FR/NL | Prioridad alta bilingüe |
| USA | EN-US | Prioridad internacional |
| México | ES-MX | Prioridad internacional |

### FASE 2 — Posterior

| Mercado | Idioma | Decisión |
|---|---|---|
| Italia | IT | Standby; limpieza mínima defensiva |
| Portugal | PT-PT | Standby; limpieza mínima defensiva |
| Otros países | Según expansión | No trabajar ahora |

---

## 4. Hallazgos de arquitectura actual

### 4.1 Landings país existentes

Desde páginas Shopify se detectan:

| Handle | Título | Estado |
|---|---|---|
| `papel-pintado-espana` | Papel Pintado España | Existe, antigua, necesita reformulación |
| `papel-pintado-francia` | Papel Pintado Francia | Existe, antigua, necesita reformulación |
| `envios-internacionales` | Envíos de papel pintado internacionales | Existe, pero no sustituye una arquitectura SEO país |

Lectura profesional:
Estas páginas son útiles como base, pero no son suficientes para competir contra players maduros. Deben pasar de “página de envíos/listado” a “landing país pilar” con contenido comercial, B2B, materiales, muestras, personalización, FAQ y enlaces internos.

### 4.2 Landings país ausentes

No se detectaron landings país maduras en colecciones/páginas para:

- Alemania;
- Países Bajos;
- UK;
- Bélgica;
- USA;
- México.

Esto es una brecha estratégica importante. Actualmente MatchWalls tiene idiomas publicados, pero no una arquitectura de país/mercado suficientemente trabajada para todos los mercados prioritarios.

### 4.3 Landings geográficas existentes

Se identifican 58 colecciones geográficas del patrón:

`comprar-papel-pintado-*`

Distribución observada:

- 48 landings españolas/provinciales aproximadas;
- 10 landings francesas de ciudad/región:
  - Burdeos,
  - Estrasburgo,
  - Lille,
  - Lyon,
  - Marsella,
  - Montpellier,
  - Nantes,
  - Niza,
  - París,
  - Toulouse.

Patrón común:

- 73 productos exactos en la mayoría/todas las landings geográficas;
- SEO title y description localizados con estructura repetitiva;
- actualización común 2026-06-29;
- posible riesgo de bajo valor diferencial si no hay contenido local real.

Conclusión:
No son basura por definición, pero no deben expandirse ni noindexarse masivamente sin matriz comercial. Las estratégicas deben protegerse y mejorarse.

---

## 5. Decisión sobre Italia y Portugal

Italia y Portugal están publicados en Shopify, pero quedan fuera del foco editorial de FASE 1.

Regla aprobada:

En FASE 1, IT y PT-PT solo pueden recibir limpieza mínima defensiva:

- 404 críticos;
- redirects incorrectos;
- noindex accidental;
- hreflang roto;
- sitemap contaminado;
- contenido vacío;
- errores técnicos graves.

No hacer ahora:

- landings nuevas IT/PT;
- optimización editorial profunda;
- estrategia GEO IT/PT;
- solicitud de indexación manual;
- expansión de clusters.

---

## 6. Safari / Applebot incluido

La auditoría debe incluir explícitamente:

- Safari desktop;
- Safari iOS;
- Applebot;
- Applebot-Extended;
- Siri;
- Spotlight;
- Apple Intelligence;
- acceso a JS/CSS;
- snippets y política de bots.

Safari no debe aparecer como nota secundaria. Debe formar parte del bloque de crawlers, navegadores e IA.

---

## 7. Diagnóstico CMO/SEO/GEO

### Lo que MatchWalls tiene bien

1. Idiomas prioritarios publicados: ES, EN, FR, DE, NL.
2. Base Shopify internacional ya activa.
3. Catálogo amplio: 3.022 productos.
4. 109 colecciones.
5. Landings ES/FR ya existentes como punto de partida.
6. Arquitectura de categorías por estilos, colores, estancias y materiales bastante aprovechable.
7. Base suficiente para construir autoridad temática.

### Lo que falta para competir contra Photowall / Rebel Walls / Wallism

1. Arquitectura país clara para DE, NL, UK, BE, USA y MX.
2. Diferenciación EN-UK vs EN-US.
3. Diferenciación ES-España vs ES-México.
4. Enfoque bilingüe específico para Bélgica.
5. Contenido local real en landings geográficas.
6. Landings país pilar con intención comercial, B2B y muestras.
7. Sistema de enlaces internos desde home, footer, colecciones core y páginas profesionales.
8. Base factual citable para IA.
9. Contenido comparativo y guías útiles.
10. Medición con GSC/GA4/Merchant/Bing no disponible desde aquí.

---

## 8. Propuesta estratégica por olas

### Ola 1 — Consolidación prioritaria Europa

1. Reformular landing España.
2. Reformular landing Francia.
3. Crear briefing para landing Alemania.
4. Crear briefing para landing Países Bajos.
5. Crear briefing para landing UK.
6. Crear briefing para Bélgica bilingüe.
7. Proteger landings geográficas estratégicas:
   - Barcelona,
   - Madrid,
   - Valencia,
   - Málaga,
   - Sevilla,
   - París,
   - Lyon,
   - Toulouse,
   - Amsterdam,
   - Rotterdam,
   - Berlin,
   - Hamburg,
   - London,
   - Manchester,
   - Brussels,
   - Antwerp.

### Ola 2 — Internacional prioridad

1. Crear landing USA.
2. Crear landing México.
3. Definir diferencias de copy, moneda, envío, medidas, FAQ y search intent.
4. Revisar si conviene indexar o no determinadas URLs internacionales según capacidad logística real.

### Ola 3 — FASE 2

1. Italia.
2. Portugal.
3. Suiza/Austria/Irlanda/Nórdicos si hay sentido comercial.
4. Más idiomas solo cuando exista capacidad editorial y logística.

---

## 9. Riesgos actuales

| Riesgo | Nivel | Explicación |
|---|---|---|
| Idiomas IT/PT publicados sin trabajo profundo | Medio | Pueden generar señales de baja calidad si están en sitemap/indexables sin control |
| Landings geo repetitivas 73 productos | Alto | Riesgo de páginas demasiado similares |
| Ausencia landings país DE/NL/UK/BE | Alto | Falta arquitectura para mercados prioritarios |
| UK y USA mezclados bajo EN genérico | Medio/Alto | Intenciones, vocabulario y confianza comercial son distintas |
| México y España mezclados bajo ES genérico | Medio | Debe adaptarse copy y confianza |
| Bélgica sin bilingüismo claro | Medio/Alto | Mercado FR/NL; requiere doble enfoque |
| Medición externa no accesible | Alto | Sin GSC/GA4/Merchant/Bing no se puede priorizar por datos reales |

---

## 10. Próximo lote recomendado

Crear:

`MW-GEO-LANDINGS-PRIORITY-MAP-012B`

Tipo: solo lectura / planificación.

Objetivo:

- listar landings país y ciudad prioritarias;
- separar conservar / mejorar / crear / standby / noindex candidato;
- no tocar Shopify;
- no ejecutar noindex;
- no crear páginas;
- no modificar colecciones.

Salida esperada:

1. mapa de URLs actuales;
2. mapa de URLs faltantes;
3. matriz de prioridad comercial;
4. propuesta de arquitectura de URL;
5. recomendaciones de interlinking;
6. criterios de exclusión IT/PT;
7. handoff para Codex.

---

## 11. Qué debe hacer Codex cuando vuelva

1. Leer este handoff.
2. Guardarlo en `handoffs-chatgpt-api`.
3. No repetir toda la auditoría salvo discrepancia.
4. Contrastar con archivos locales y sitemap.
5. Actualizar plan operativo y cola maestra solo si Daniel lo aprueba.
6. No ejecutar escrituras.
7. STOP si detecta discrepancias entre Shopify, sitemap, Search Console o este handoff.

---

## 12. Estado final

**Estado del lote:** SOLO LECTURA / DIAGNÓSTICO INICIAL COMPLETADO  
**Cambios Shopify:** Ninguno  
**Siguiente paso:** `MW-GEO-LANDINGS-PRIORITY-MAP-012B`  
**Aprobación para escritura:** No aplica en este lote  
