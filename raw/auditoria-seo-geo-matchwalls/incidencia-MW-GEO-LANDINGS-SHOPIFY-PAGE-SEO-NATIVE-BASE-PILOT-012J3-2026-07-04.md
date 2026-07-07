# Incidencia - MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-BASE-PILOT-012J3

Fecha: 2026-07-04  
Estado: `INCORRECTO`  
Accion Shopify ejecutada: declarada por Daniel.  
QA publico: ejecutado.  
Decision operativa: rollback recomendado inmediato.

## 1. Cambio ejecutado declarado

Daniel confirmo:

```text
GUARDADO 012J3 ESPAÑA ES
Title tocado: no
URL tocada: no
Body tocado: no
```

Campo modificado:

- Pagina base ES: `papel-pintado-espana`
- Campo: `Metadescripcion`
- Valor: `Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural.`

## 2. QA publico positivo en ES

URL:

- `https://www.matchwalls.com/pages/papel-pintado-espana?mwqa=012j3-post-20260704a`

Resultado:

- HTTP 200.
- Title publico intacto.
- Meta description publica coincide exactamente con el valor propuesto.
- Canonical propio.
- H1 intacto.
- Sin `noindex`.
- 8 hreflang detectados.

Clasificacion ES:

`VERIFICADO Y CORRECTO`

## 3. Efecto secundario detectado

Control posterior en idiomas prioritarios de la landing Espana:

- FR: mantiene meta en frances/autogenerada. `VERIFICADO PERO MEJORABLE`
- EN: control no concluyente por 503. `NO ACCESIBLE`
- DE: hereda la metadescripcion ES. `INCORRECTO`
- NL: hereda la metadescripcion ES. `INCORRECTO`

Valores problematicos:

- DE `https://www.matchwalls.com/de/pages/spanien-tapete?mwqa=012j3-final-de`
- NL `https://www.matchwalls.com/nl/pages/spanje-behang?mwqa=012j3-final-nl`

Ambas URLs muestran:

`Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural.`

## 4. Interpretacion

La metadescripcion nativa ES se publica correctamente en ES, pero tambien parece actuar como fallback para al menos DE y NL cuando no existe metadescripcion traducida especifica.

Esto invalida el piloto como cambio publicable en solitario.

## 5. Decision recomendada

Ejecutar rollback inmediato:

1. Volver a Shopify Admin nativo > pagina `papel-pintado-espana`.
2. Abrir `Publicacion en motores de busqueda`.
3. Borrar solo `Metadescripcion`.
4. Dejar el campo vacio.
5. No tocar `Titulo de la pagina`.
6. No tocar `Identificador de URL`.
7. Guardar.
8. Ejecutar QA publico post-rollback.

## 6. Siguiente lote seguro posterior

Despues del rollback, no se debe volver a completar la meta ES sola.

Siguiente lote recomendado:

`MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-I18N-META-SAFE-PATH-DIAG-012J4`

Objetivo:

- determinar via segura para metadescripciones por idioma;
- evitar fallback de ES en DE/NL/EN;
- decidir si conviene completar primero todas las traducciones SEO o usar otra capa de traduccion compatible.

## 7. Evidencia

- `qa-publico-post-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-BASE-PILOT-012J3-2026-07-04.csv`

