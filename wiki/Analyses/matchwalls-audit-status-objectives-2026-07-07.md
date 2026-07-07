---
type: analysis
status: active
created: 2026-07-07
updated: 2026-07-07
sources:
  - "[[wiki/Analyses/shopify-seo-geo-developer-handoff-2026-07-07]]"
tags:
  - wiki
  - shopify
  - seo
  - geo
  - reporting
---

# MatchWalls audit status and completed objectives

## Summary

Este reporte resume que se ha conseguido con la auditoria [[wiki/Concepts/seo|SEO]]/[[wiki/Concepts/geo|GEO]]/[[wiki/Concepts/aeo|AEO]] de [[wiki/Entities/matchwalls|MatchWalls]], por que el trabajo ha requerido muchos tokens y cual es el estado actual verificable de `matchwalls.com` frente a la auditoria.

La conclusion ejecutiva es:

- El trabajo no ha sido una unica modificacion tecnica, sino una reconstruccion documentada del estado SEO/GEO de Shopify.
- Se ha creado una capa de conocimiento util para desarrollo: [[wiki/Analyses/shopify-seo-geo-developer-handoff-2026-07-07|Shopify SEO/GEO developer handoff]].
- Hay un cambio live confirmado en Shopify: exclusion de Black Friday evergreen del hub `/collections`.
- La web publica responde correctamente en comprobaciones ligeras de home, collections, sitemap, robots, `llms.txt` y `agents.md`.
- [[wiki/Entities/indexnow|IndexNow]] sigue sin estar activo: `https://www.matchwalls.com/indexnow.txt` devuelve 404.
- El mayor bloqueo sigue siendo la incidencia de [[wiki/Entities/shopify-engineering-ticket-68731900|Shopify Engineering ticket 68731900]], relacionada con sincronizacion/cache/render en landings geograficas.

## Objectives completed

### 1. Ordenar el estado real del proyecto

Estado: `CUMPLIDO`.

Se ha separado lo que esta aplicado, lo que esta preparado, lo que esta bloqueado y lo que requiere decision humana. Esto evita una lectura peligrosa del tipo "todo esta hecho" cuando la auditoria demuestra que hay cambios cerrados, cambios parciales y bloqueos activos.

Resultado generado:

- [[wiki/Analyses/shopify-seo-geo-developer-handoff-2026-07-07|Shopify SEO/GEO developer handoff]]

### 2. Explicar que esta haciendo el socio con Codex

Estado: `CUMPLIDO`.

Se ha identificado que el socio no esta usando Codex solo para escribir codigo, sino para operar un sistema de lotes auditados:

- lotes con identificadores `MW-...`;
- aprobaciones explicitas antes de escrituras;
- backups antes de tocar Liquid;
- evidencias CSV y reportes Markdown;
- QA publico o Admin;
- decisiones de bloqueo y siguientes pasos.

Este punto es clave para que un desarrollador pueda entrar sin romper la disciplina operativa existente.

### 3. Identificar cambios live confirmados

Estado: `CUMPLIDO`.

Cambio live confirmado en los reportes:

- Tema MAIN/live: `178399019384`.
- Archivo: `sections/main-list-collections.liquid`.
- Lote: `MW-SHOPIFY-CLI-INSTALL-AUTH-THEME-PUSH-013E16E2`.
- Efecto: exclusion visual por ID estable de la coleccion evergreen Black Friday del hub publico `/collections`.
- QA reportado: ES, EN, FR, DE y NL con 200, 47 tarjetas y 0 Black Friday.

### 4. Identificar bloqueos activos

Estado: `CUMPLIDO`.

Bloqueo principal:

- Shopify Engineering ticket `68731900`.
- Caso asociado: `012O`.
- Problema: Admin y storefront publico no sincronizan de forma fiable en landings geograficas.

Decision vigente:

- No seguir escribiendo contenido visible a ciegas.
- No publicar tema ni schema visible.
- No modificar landings Espana/Francia, LangShop, SEO fields, canonicals, redirects, robots, sitemap, `llms.txt`, `agents.md` o IndexNow hasta resolver o acotar el problema.

### 5. Aclarar el estado de IndexNow

Estado: `CUMPLIDO`.

IndexNow no esta implementado.

Comprobacion ligera realizada el 2026-07-07:

| URL | Estado |
|---|---:|
| `https://www.matchwalls.com/indexnow.txt` | 404 |

Interpretacion: falta una key verificable publicada en una ubicacion valida para cubrir `www.matchwalls.com`. No conviene enviar URLs hasta resolver esto.

### 6. Aclarar el estado factual de la entidad MatchWalls

Estado: `CUMPLIDO`.

Se ha documentado que se puede describir MatchWalls de forma prudente como tienda online especializada en papel pintado, murales decorativos y soluciones murales a medida.

Pero siguen bloqueados como claims publicos o schema:

- razon social;
- CIF/NIF/VAT;
- direccion legal;
- telefono/email estructurado;
- `sameAs`;
- "desde 1961";
- Barcelona como sede;
- fabricacion propia;
- certificaciones;
- sostenibilidad;
- Trustpilot/reviews;
- garantias, plazos, devoluciones o envio gratis.

## Why this required many tokens

El consumo alto de tokens fue necesario por cinco motivos tecnicos:

1. Habia muchos documentos raw y reportes de lotes con estados que se corrigen entre si. Ejemplo: un lote dejo Black Friday incompleto y otro posterior lo cerro como corregido.
2. No bastaba con resumir; habia que distinguir evidencia, inferencia, decision humana, bloqueo tecnico y cambio aplicado.
3. La auditoria afecta varias capas a la vez: Shopify theme, LangShop, contenido, schema, Bing, IndexNow, crawlers, entity facts y QA publico.
4. Habia riesgo de dar una conclusion erronea si se ignoraban los documentos de bloqueo. El informe necesitaba preservar la diferencia entre "preparado", "validado", "aplicado" y "publicamente estable".
5. Se siguio el metodo de la boveda Obsidian: leer indice, buscar raw relevantes, crear analisis reutilizable, actualizar indice y log.

En terminos practicos, los tokens se gastaron para reducir riesgo: menos suposiciones, mas trazabilidad y mejor transferencia para desarrollo.

## Current public status of matchwalls.com

Comprobacion ligera realizada el 2026-07-07. No es un crawl completo y respeta la decision de no hacer barridos amplios mientras el ticket Shopify siga abierto.

| URL | HTTP | Content-Type | Lectura |
|---|---:|---|---|
| `https://www.matchwalls.com/` | 200 | `text/html; charset=utf-8` | Home accesible |
| `https://www.matchwalls.com/collections` | 200 | `text/html; charset=utf-8` | Hub de colecciones accesible |
| `https://www.matchwalls.com/sitemap.xml` | 200 | `application/xml; charset=utf-8` | Sitemap accesible |
| `https://www.matchwalls.com/robots.txt` | 200 | `text/plain; charset=utf-8` | Robots accesible |
| `https://www.matchwalls.com/llms.txt` | 200 | `text/markdown; charset=utf-8` | Archivo IA accesible |
| `https://www.matchwalls.com/agents.md` | 200 | `text/markdown; charset=utf-8` | Archivo agentes accesible |
| `https://www.matchwalls.com/indexnow.txt` | 404 | `text/plain; charset=utf-8` | IndexNow no activo |

## Audit status by area

| Area | Estado | Comentario |
|---|---|---|
| Repositorio/wiki | `OPERATIVO` | Informe de handoff creado, indexado y registrado |
| [[wiki/Entities/shopify|Shopify]] MAIN | `PARCIALMENTE MODIFICADO` | Cambio live confirmado en `sections/main-list-collections.liquid` |
| Hub `/collections` | `MEJORADO` | Black Friday evergreen excluido segun reporte postcheck |
| Landings Espana/Francia | `BLOQUEADO` | Caso `012O` por discrepancia Admin/storefront |
| Schema visible | `BLOQUEADO` | No avanzar hasta resolver infraestructura/cache/render |
| LangShop/traducciones | `BLOQUEADO` | No tocar mientras siga el ticket critico |
| [[wiki/Entities/bing|Bing]] base | `DOCUMENTADO` | Hay baseline de Search Performance, sitemap y AI Performance |
| [[wiki/Entities/indexnow|IndexNow]] | `NO ACTIVO` | Falta key verificable; `indexnow.txt` devuelve 404 |
| Entity facts | `PRUDENTE` | Base segura definida; claims corporativos fuertes bloqueados |
| SEM pago | `NO EVIDENCIADO` | No se han visto campanas ads/pago en los raw revisados |

## Recommended report wording

Texto recomendado para comunicar el estado:

> Se ha completado una primera consolidacion tecnica de la auditoria SEO/GEO/AEO de MatchWalls. El trabajo ha permitido separar cambios aplicados, cambios preparados, bloqueos activos y decisiones pendientes. El cambio live confirmado es la exclusion de la coleccion evergreen Black Friday del hub publico de colecciones en el tema Shopify MAIN. La web responde correctamente en comprobaciones ligeras de home, collections, sitemap, robots, `llms.txt` y `agents.md`, pero IndexNow no esta activo y las landings geograficas siguen condicionadas por el ticket Shopify Engineering `68731900`. El siguiente paso no debe ser publicar mas cambios, sino resolver o acotar ese bloqueo y continuar solo con tareas documentales seguras o cambios quirurgicos aprobados.

## Next safe action

La siguiente accion segura es crear una matriz unica de lotes con:

- lote;
- estado;
- archivo resultado;
- si toca Shopify;
- si toca MAIN;
- si es reversible;
- evidencia;
- siguiente decision.

Esto convertiria la auditoria en una cola tecnica accionable para desarrollo.
