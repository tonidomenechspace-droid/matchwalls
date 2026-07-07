# HANDOFF CHATGPT/API — MW-GEO-LANDINGS-PRIORITY-MAP-012B

**Fecha:** 2026-07-01  
**Origen:** ChatGPT con lectura de auditorías + Shopify Admin GraphQL API  
**Modo:** SOLO LECTURA / MAPA DE PRIORIDAD / SIN CAMBIOS SHOPIFY  
**Estado:** COMPLETADO COMO PROPUESTA ESTRATÉGICA, NO EJECUTADA  
**Destino local recomendado:**  
`C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\auditoria-seo-geo-matchwalls\handoffs-chatgpt-api\`

---

## 1. Aprobación recibida

Daniel escribe: “aprobado”.

Interpretación segura:
- Aprobado para continuar diagnóstico y planificación en solo lectura.
- No se interpreta como aprobación de escritura.
- No es aprobación exacta para mutaciones Shopify.

Cualquier escritura futura requerirá la fórmula literal:
`APROBADO LOTE [NOMBRE EXACTO]`.

---

## 2. Objetivo del lote

Crear un mapa de prioridad para landings país y geográficas de MatchWalls, cruzando:
- auditorías y cola vigente;
- estado Shopify real leído por API;
- estrategia de mercados aprobada por Daniel;
- criterio de no romper nada.

Este lote no modifica Shopify.

---

## 3. Base de referencia

El plan operativo vigente declara el programa global como `INCOMPLETO`, con idiomas prioritarios ES, EN, FR, DE y NL, e IT/PT publicados fuera de prioridad activa. El objetivo controlable incluye que las URLs valiosas sean indexables y que las URLs sin valor no contaminen sitemap/resultados.

La cola vigente incluye `MW-INDEXABILITY-GEO-COLLECTIONS-ROLLING-DIAG-011E2` y `MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-ROLLING-011E3`. Este último sería escritura y exige aprobación exacta.

Codex cerró `011E2` como `VERIFICADO PERO MEJORABLE`: 235 URLs geográficas en idiomas prioritarios, con 147 candidatas a decisión humana y 88 en STANDBY. IT/PT quedan fuera de alcance prioritario y en STANDBY.

---

## 4. Shopify real cruzado

Shopify API confirma:
- 3.022 productos;
- 109 colecciones;
- 55 páginas;
- 604 redirects;
- idiomas publicados: ES, EN, FR, DE, NL, IT, PT-PT.

Landings país existentes:
- `papel-pintado-espana`;
- `papel-pintado-francia`;
- `envios-internacionales`.

Landings país no detectadas como maduras:
- Alemania;
- Países Bajos;
- UK;
- Bélgica;
- USA;
- México.

Landings geográficas existentes observadas:
- 48 aprox. en España/provincias;
- 10 en Francia/ciudades;
- patrón común: 73 productos exactos en la mayoría/todas.

---

## 5. Decisión estratégica

### 5.1 No ejecutar noindex masivo

No se debe ejecutar `011E3` todavía.

Motivos:
1. Hay landings estratégicas indexables como Barcelona y París.
2. Muchas landings geográficas son repetitivas, pero algunas pueden tener valor comercial.
3. Faltan datos GSC/ventas por URL.
4. Algunas landings deben pasar a mejora editorial, no a noindex.
5. Italia y Portugal quedan fuera de prioridad, salvo limpieza mínima defensiva.

### 5.2 Proteger landings estratégicas existentes

Proteger y mejorar, no noindexar:

España:
- Barcelona, Madrid, Valencia, Málaga, Sevilla, Alicante, Girona, Tarragona, Bizkaia, Gipuzkoa, Granada, Murcia, Zaragoza.

Francia:
- París, Lyon, Toulouse, Marsella, Burdeos, Nantes, Lille, Niza, Montpellier, Estrasburgo.

Estas URLs no deben entrar en un lote de noindex sin revisión humana, GSC y decisión comercial.

### 5.3 STANDBY para el resto

El resto de landings geográficas ES debe quedar en STANDBY hasta revisar:
- GSC;
- impresiones;
- clics;
- ventas/leads;
- valor B2B local;
- intención real de búsqueda;
- posibilidad de enriquecer contenido local.

---

## 6. Arquitectura país recomendada

### Ola 1 — Europa prioritaria

1. Reformular `papel-pintado-espana` como landing país pilar.
2. Reformular `papel-pintado-francia` como landing país pilar.
3. Crear briefing para Alemania: Tapeten Deutschland / Wandtapeten / Fototapeten nach Maß.
4. Crear briefing para Países Bajos: Behang Nederland / Fotobehang op maat.
5. Crear briefing para UK: wallpaper UK / mural wallpaper UK.
6. Crear briefing para Bélgica: papier peint Belgique / behang België.

### Ola 2 — Internacional

1. USA: wallpaper USA / custom mural wallpaper.
2. México: papel pintado México / murales a medida México.

### Ola 3 — FASE 2

1. Italia.
2. Portugal.
3. Otros países.

---

## 7. Reglas para Italia y Portugal

Permitido en FASE 1:
- detectar 404 críticos;
- detectar redirects incorrectos;
- detectar noindex accidental;
- detectar hreflang roto;
- detectar contaminación grave en sitemap;
- detectar contenido vacío;
- detectar fallos técnicos graves.

No permitido en FASE 1:
- crear landings IT/PT;
- optimizar editorialmente IT/PT;
- ejecutar GEO IT/PT;
- solicitar indexación manual IT/PT;
- gastar trabajo en clusters IT/PT.

---

## 8. Qué NO se ha hecho

No se ha:
- creado ninguna página;
- cambiado ninguna colección;
- aplicado noindex;
- eliminado redirects;
- editado SEO title/meta;
- tocado tema;
- tocado robots;
- tocado sitemap;
- tocado schema;
- tocado canonicals/hreflang.

---

## 9. Próximo paso recomendado

Antes de escribir en Shopify:

`MW-GEO-LANDINGS-BRIEF-COUNTRY-PILLARS-012C`

Tipo:
- planificación editorial;
- sin cambios Shopify.

Objetivo:
- redactar briefing de contenido para landings país pilar:
  España, Francia, Alemania, Países Bajos, UK, Bélgica, USA y México.

No crear páginas todavía.

---

## 10. Qué debe hacer Codex cuando vuelva

1. Leer este handoff.
2. Guardarlo en `handoffs-chatgpt-api`.
3. No ejecutar `011E3` automáticamente.
4. No noindexar geográficas protegidas.
5. Cruzar con GSC/sitemap/archivos locales antes de cualquier escritura.
6. Actualizar cola solo si Daniel lo aprueba.
7. Tratar este lote como mapa estratégico, no como evidencia de ejecución.

---

## 11. Archivo asociado

Matriz CSV asociada:
`matriz-MW-GEO-LANDINGS-PRIORITY-MAP-012B-2026-07-01.csv`

Incluye:
- landings país existentes;
- landings país faltantes;
- IT/PT fase 2;
- geográficas ES/FR existentes;
- geográficas futuras para DE/NL/UK/BE/USA/MX;
- decisión recomendada por cada fila.

---

## 12. Estado final

**Estado:** SOLO LECTURA / MAPA DE PRIORIDAD COMPLETADO  
**Cambios Shopify:** NINGUNO  
**Riesgo de rotura:** 0 por ejecución, porque no se ha ejecutado nada.  
**Siguiente lote recomendado:** `MW-GEO-LANDINGS-BRIEF-COUNTRY-PILLARS-012C`.
