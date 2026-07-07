# QA — MW-TECH-PRODUCT-FILEINPUT-GUARD-010A3

Fecha: 2026-06-18 22:26 CEST.

Estado: `VERIFICADO PERO MEJORABLE`.

El cambio está únicamente en el tema `178399019384`, `/t/46`,
`UNPUBLISHED`. No se publicó ni se modificó el MAIN.

## Verificación almacenada

- Archivo: `snippets/product-customizer.liquid`.
- MD5 anterior: `3878a24a9bb6cb134247ac6aff707a58`.
- MD5 nuevo: `8f8a7d213f04ace77c4003647053f763`.
- Tamaño: 49.228 → 49.229 bytes.
- Llamada directa `fileInput.addEventListener`: 0.
- Llamada opcional `fileInput?.addEventListener`: 1.
- El hash coincide exactamente con la copia local original más un único `?`.
- MAIN conserva el checksum original.

## Pruebas específicas

Cobertura inicial: producto estándar y cargador personalizado × ES/EN/FR/DE/NL
× escritorio/móvil = 20 cargas.

- Tema `/t/46`: 20/20.
- Contenido no vacío: 20/20.
- Sin 404: 20/20.
- Producto estándar sin `#customImage`: 10/10.
- Error `addEventListener` en producto estándar: 0/10.
- Cargador con `#customImage`: 8/10 en primera carga; 2 cargas incompletas.
- Error `addEventListener` en cargador: 10/10.

No se repitieron las cargas incompletas ni la matriz de 170 porque el error
crítico permanece en las cinco versiones del cargador.

## Nuevo origen exacto

`INCORRECTO`

- En el cargador, `#customImage` existe.
- `button[open-modal]` no existe; el atributo `open-modal` está en el `<input>`.
- El archivo ejecuta `openModalButton.addEventListener('click', ...)` sin
  comprobar el valor nulo.
- Archivo/línea local: `snippets/product-customizer.liquid:605`.
- La llamada aparece una sola vez.

## Deuda independiente

- `this.convertToInches is not a function` permanece fuera del alcance.
- Tracking dinámico de medidas permanece sin resolver.

