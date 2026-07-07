# Diagnóstico de la biblioteca de temas — 18 de junio de 2026

Estado: `VERIFICADO PERO MEJORABLE`.

Alcance: lectura de los 20 temas existentes. No se eliminó, renombró, duplicó
ni publicó ningún tema durante esta auditoría.

## Hallazgo principal

Shopify muestra `Theme limit reached`: la tienda ha alcanzado el máximo de 20
temas. Es necesario liberar al menos una posición antes de crear un nuevo tema
auxiliar para la deuda técnica.

## Temas protegidos

| ID | Nombre | Motivo | Estado |
| --- | --- | --- | --- |
| `178396463480` | `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...` | MAIN actual | `VERIFICADO Y CORRECTO` |
| `178383749496` | `SEO schema hotfix - 2026-06-15` | Reversión inmediata del MAIN | `STANDBY` |
| `138693968099` | `MatchWalls/Original/ NO ELIMINAR` | Marcado expresamente como no eliminable | `STANDBY` |
| `178390401400` | `MW-FOOTER-I18N-001 - QA - 2026-06-17` | Trabajo reciente con evidencia registrada | `STANDBY` |
| `178383585656` | `SEO-GEO staging - 2026-06-15` | Contiene trabajo histórico no conciliado por completo | `STANDBY` |
| `178379293048` | `Production - SEO fix AggregateRating (2026-06-12)` | Tema SEO reciente; pendiente decidir retención | `STANDBY` |
| `142267973859` | `Production` | Actualizado el 12/06/2026; posible dependencia histórica | `STANDBY` |

## Temas antiguos que requieren decisión

`REQUIERE DECISION HUMANA`

- `138921083107` — `MatchWalls/main OLD`.
- `139013456099` — `Webmefy OLD`.
- `141270778083` — `Dev David`.
- `141368262883` — `Dev David (Pruebas Gloria)`.
- `141375340771` — `Production - 24/08/2024`.
- `141375406307` — `Dev`.
- `141375439075` — `Staging`.
- `176538845560` — `Zoom dev`.
- Cinco temas llamados `Copy of Production`:
  - `142344224995` — actualizado 09/09/2024, 289 archivos.
  - `142418575587` — actualizado 10/09/2024, 289 archivos.
  - `142694351075` — actualizado 24/09/2024, 298 archivos.
  - `176724410744` — actualizado 22/01/2025, 304 archivos.
  - `176746496376` — actualizado 29/01/2025, 311 archivos.

## Comparación de los dos primeros `Copy of Production`

`VERIFICADO PERO MEJORABLE`

Los temas `142344224995` y `142418575587` tienen los mismos 289 nombres de
archivo. Solo difieren cinco checksums:

- tres assets generados por Shopify: `country-flags.css`, `sections.js` y
  `theme.js`;
- `sections/header.liquid`;
- `snippets/navigation-panel.liquid`.

El segundo es posterior al primero. Esto convierte `142344224995` en el mejor
candidato inicial para liberar una plaza, pero no demuestra que sus dos
diferencias funcionales carezcan de valor. Debe descargarse y verificarse un
respaldo antes de eliminarlo.

## Recomendación

Ejecutar un lote mínimo que afecte únicamente a `142344224995`:

1. descargar el tema como ZIP;
2. registrar tamaño y hash del ZIP;
3. confirmar que el ZIP contiene los 289 archivos;
4. eliminar solo ese tema;
5. comprobar que quedan 19 temas y que MAIN/reversión no cambian;
6. repetir smoke test público.

No se recomienda limpiar varios temas a la vez. Tras liberar una plaza, se
continuará con la deuda técnica y la biblioteca restante podrá revisarse por
separado.
