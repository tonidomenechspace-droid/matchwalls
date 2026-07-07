# Incidencia post-rollback - MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-BASE-PILOT-012J3

Fecha: 2026-07-04  
Estado: `INCORRECTO`  
Accion declarada: rollback manual ejecutado por Daniel.  
QA publico: ejecutado.  
Cambios adicionales: no.

## 1. Rollback declarado

Daniel confirmo:

```text
ROLLBACK 012J3 HECHO
Title tocado: no
URL tocada: no
Body tocado: no
Meta description ES: VACIO
```

## 2. Resultado publico post-rollback

QA post-rollback con cache-buster:

- ES: sigue mostrando la metadescripcion del piloto. `INCORRECTO`
- FR: no muestra la metadescripcion ES; mantiene descripcion autogenerada FR. `VERIFICADO PERO MEJORABLE`
- EN: no muestra la metadescripcion ES; mantiene descripcion autogenerada EN. `VERIFICADO PERO MEJORABLE`
- DE: sigue mostrando la metadescripcion ES del piloto. `INCORRECTO`
- NL: no muestra la metadescripcion ES; mantiene descripcion autogenerada NL. `VERIFICADO PERO MEJORABLE`

Segunda comprobacion:

- ES y DE siguen mostrando el valor del piloto.
- Respuesta Cloudflare `DYNAMIC`, por lo que no se cierra como simple cache estatica.
- NL permanece limpio.

## 3. Valor que sigue apareciendo publicamente

`Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural.`

## 4. Interpretacion

El rollback declarado no queda verificado publicamente. Hay dos posibilidades principales:

1. El campo nativo ES sigue persistido aunque la interfaz parezca vacia.
2. Existe una capa de traduccion/fallback para ES/DE que conserva el valor del piloto.

No se puede afirmar la causa exacta sin nueva comprobacion visual/admin.

## 5. Siguiente accion segura

No ejecutar mas escrituras a ciegas.

Comprobacion manual de solo lectura ejecutada mediante captura de Daniel:

- Reabrir Shopify nativo pagina `papel-pintado-espana`.
- Abrir `Publicacion en motores de busqueda`.
- Verificar si `Metadescripcion` esta realmente vacia o contiene el texto del piloto.
- No guardar.
- No tocar title ni URL.

Resultado:

- `Metadescripcion` visible como vacia: `VERIFICADO Y CORRECTO`.
- Contador visible: `0 de 160 caracteres usados`.
- `Titulo de la pagina` visible e intacto.
- `Identificador de URL` visible e intacto.
- Boton `Guardar` gris/inactivo.
- Guardado adicional: no.

Interpretacion actualizada:

- Shopify nativo muestra el campo base ES vacio.
- El HTML publico ES y DE seguia mostrando el valor del piloto en QA post-rollback.
- La causa queda `NO ACCESIBLE`; puede existir una capa de render/fallback/traduccion/caché de app no visible desde el campo nativo.
- El lote 012J3 no queda cerrado como corregido; queda `INCORRECTO` hasta diagnostico 012J4.

## 6. Evidencia

- `qa-publico-post-rollback-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-BASE-PILOT-012J3-2026-07-04.csv`
- `evidencias/captura-012J3-postrollback-shopify-nativo-meta-vacia-2026-07-04.png`
