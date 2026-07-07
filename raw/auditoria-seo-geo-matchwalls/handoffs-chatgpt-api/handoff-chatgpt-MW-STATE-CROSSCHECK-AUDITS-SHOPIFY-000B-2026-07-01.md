# HANDOFF CHATGPT/API — MW-STATE-CROSSCHECK-AUDITS-SHOPIFY-000B

**Fecha:** 2026-07-01  
**Origen:** ChatGPT con acceso Shopify Admin GraphQL API  
**Modo:** SOLO LECTURA / CRUCE AUDITORÍAS vs SHOPIFY REAL  
**Estado:** COMPLETADO COMO DIAGNÓSTICO PREVENTIVO  
**Cambios Shopify:** NINGUNO  
**Destino local recomendado:**  
`C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\handoffs-chatgpt-api\`

---

## 1. Motivo del lote

Daniel interrumpe correctamente antes de continuar con nuevas landings y pide:

> “antes lee auditorías y cruza con Shopify real para tener claro dónde estamos. Es muy importante no romper nada.”

Se crea este handoff preventivo para evitar trabajar sobre una cola desactualizada o repetir un lote ya corregido.

---

## 2. Regla de seguridad

No se ha ejecutado ninguna mutación.

No se han modificado:

- redirects;
- colecciones;
- páginas;
- productos;
- metadatos;
- traducciones;
- sitemap;
- robots;
- schema;
- tema;
- handles;
- canonicals;
- hreflang.

Todo lo realizado es lectura desde Shopify API y cruce con el plan/cola vigentes subidos por Daniel.

---

## 3. Auditorías/documentos cruzados

Documentos usados como referencia de auditoría:

- `plan-operativo-vigente-y-cola-lotes-seo-geo-2026-06-30.md`
- `cola-maestra-vigente-lotes-seo-geo-2026-06-30.csv`
- handoff previo `MW-SEO-GEO-MARKET-STRATEGY-AUDIT-012A`

El plan operativo indica:

- estado global `INCOMPLETO`;
- idiomas prioritarios: ES, EN, FR, DE, NL;
- idiomas publicados fuera de prioridad activa: IT, PT;
- lecturas y auditorías autorizadas;
- escrituras Shopify/tema/robots/redirects/schema/contenido requieren propuesta formal y aprobación exacta;
- ningún lote debe mezclar tema, productos, redirects, contenidos y medición externa;
- cada lote debe cerrar con evidencia, QA y reversión.

---

## 4. Shopify real leído ahora por API

| Elemento | Shopify real API |
|---|---:|
| Tienda | Matchwalls |
| Dominio principal | https://www.matchwalls.com |
| Productos | 3.022 |
| Colecciones | 109 |
| Páginas | 55 |
| Redirects | 604 |
| Idioma primario | ES |
| Idiomas publicados | ES, EN, FR, DE, NL, IT, PT-PT |

Conclusión:
La base de idiomas coincide con el plan, pero IT/PT están publicados y deben tratarse como FASE 2 / limpieza defensiva, no como prioridad editorial.

---

## 5. Cruces críticos

### 5.1 Black Friday

Auditoría/cola:
- Black Friday obsoleto: `CORREGIDO Y VERIFICADO`.

Shopify real:
- Collection `papel-pintado-black-friday` existe.
- Productos: 0.
- Metafield `seo.hidden` = `1`.

Lectura:
- Coherente con noindex a nivel Shopify.
- No tocar.

---

### 5.2 Landings geográficas estratégicas

Shopify real:

- `comprar-papel-pintado-barcelona`
  - título: Papel pintado Barcelona
  - productos: 73
  - `seo.hidden`: null

- `comprar-papel-pintado-paris`
  - título: Papel Pintado París
  - productos: 73
  - `seo.hidden`: null

Lectura:
- Confirma que hay landings geográficas indexables estratégicas.
- También confirma patrón repetitivo de 73 productos.
- No deben noindexarse masivamente.
- Primero hay que clasificar: proteger / mejorar / standby / noindex candidato.

---

### 5.3 Landings país

Shopify real ya leído:

Páginas existentes:
- `papel-pintado-espana`
- `papel-pintado-francia`
- `envios-internacionales`

No detectadas como landings país maduras:
- Alemania;
- Países Bajos;
- UK;
- Bélgica;
- USA;
- México.

Lectura:
- España y Francia tienen base antigua.
- DE/NL/UK/BE/USA/MX son brecha estratégica.
- No crear ahora sin mapa 012B.
- Primero arquitectura.

---

### 5.4 Redirects Rayas — punto crítico

Cola vigente indica:

`MW-INDEXABILITY-REDIRECTS-COLLECTIONS-CHAIN-RAYAS-011G7C`
- Estado: `REQUIERE DECISION HUMANA`.
- Acción: ejecutar solo con aprobación exacta.

Shopify real API leído ahora:

- `/collections/rayas-rollos` → `/collections/murales-estilo-a-rayas`
- `/collections/papel-pintado-rayas` → `/collections/murales-estilo-a-rayas`

Lectura:
- En Shopify real, ambos redirects ya apuntan directamente al destino final.
- Esto contradice o actualiza la cola que sugería una cadena pendiente.
- No debe ejecutarse 011G7C sin revalidación adicional pública/sitemap.
- Posible explicación: 011G7C ya fue ejecutado fuera de la cola, o la cola quedó desactualizada.

Decisión preventiva:
**NO ejecutar 011G7C.**
Marcar como:
`REQUIERE REVALIDACIÓN / POSIBLEMENTE YA CORREGIDO`.

---

## 6. Riesgos principales identificados

| Riesgo | Nivel | Motivo |
|---|---|---|
| Ejecutar sobre cola desactualizada | Alto | 011G7C parece ya resuelto en Shopify real |
| Noindex masivo geo | Alto | Barcelona/París y otras pueden ser estratégicas |
| IT/PT publicados sin trabajo profundo | Medio | Pueden contaminar si están indexables sin control |
| Crear landings sin arquitectura | Alto | Riesgo de duplicidad y baja calidad |
| Confundir Shopify API con estado público Google | Medio | API no sustituye GSC, sitemap público ni render real |

---

## 7. Regla operativa nueva

Antes de cualquier lote de escritura:

1. Leer cola/auditoría.
2. Cruzar con Shopify API real.
3. Si hay discrepancia, STOP.
4. Validar público/sitemap/GSC si aplica.
5. Solo después preparar propuesta formal.
6. Escritura solo con aprobación exacta de Daniel.

---

## 8. Próximo paso recomendado

Antes de `MW-GEO-LANDINGS-PRIORITY-MAP-012B`, crear o considerar cerrado este lote como control previo.

Siguiente paso seguro:

`MW-GEO-LANDINGS-PRIORITY-MAP-012B`

Tipo:
- solo lectura;
- planificación;
- sin cambios Shopify.

Pero con la nueva regla:
- no tocar 011G7C;
- no ejecutar noindex;
- no crear páginas;
- no cambiar redirects.

---

## 9. Qué debe hacer Codex cuando vuelva

1. Leer este handoff.
2. Cruzarlo con los archivos locales.
3. Revisar si 011G7C ya fue ejecutado o si la cola quedó desactualizada.
4. No ejecutar 011G7C sin revalidación.
5. Actualizar cola maestra solo con evidencia real y aprobación de Daniel.
6. Mantener este handoff como alerta de seguridad.

---

## 10. Estado final

**Estado:** Diagnóstico preventivo completado.  
**Cambios:** Ninguno.  
**Conclusión:** No romper nada implica no ejecutar lotes de escritura sin cruzar auditoría + Shopify real + público/sitemap/GSC cuando proceda.
