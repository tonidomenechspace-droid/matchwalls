# Propuesta formal de lote — MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F

Fecha: 2026-07-03  
Tipo: propuesta formal previa a escritura Shopify  
Estado: `REQUIERE DECISION HUMANA`  
Ejecución Shopify realizada: no  

## 1. Nota crítica sobre la aprobación recibida

Daniel ha escrito:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F`

Esta aprobación queda registrada como intención de avanzar, pero **no debe usarse todavía para ejecutar la escritura**, porque antes de cualquier cambio Shopify el protocolo del proyecto exige presentar esta propuesta formal con:

- recursos e IDs afectados;
- valores actuales;
- valores propuestos;
- riesgos;
- backup;
- rollback;
- pruebas posteriores.

Por tanto, esta propuesta es el paso previo obligatorio. Si Daniel acepta esta propuesta concreta, la aprobación de ejecución deberá repetirse exactamente al final.

## 2. Alcance exacto propuesto

Actualizar las páginas país existentes de España y Francia para sustituir contenido antiguo basado en listados de envíos por contenido país pilar más útil, factual y citable.

Recursos afectados:

| País | Recurso | ID Shopify | URL base | Acción propuesta |
|---|---|---|---|---|
| España | Page | `gid://shopify/Page/687276622200` | `/pages/papel-pintado-espana` | Actualizar título y body HTML base ES |
| Francia | Page | `gid://shopify/Page/687276654968` | `/pages/papel-pintado-francia` | Actualizar título y body HTML base ES, y preparar traducción FR por Shopify Translate/LangShop |

No incluido en este lote:

- No crear páginas nuevas.
- No cambiar handles.
- No cambiar redirects.
- No tocar colecciones geográficas.
- No cambiar `seo.hidden`.
- No tocar tema, Liquid, robots, sitemap, schema, precios, productos ni inventario.
- No ejecutar traducciones masivas EN/DE/NL.
- No resolver Alemania, Países Bajos, UK, Bélgica, USA o México en este lote.

## 3. Estado real actual comprobado

Consulta Shopify Admin GraphQL validada y ejecutada en solo lectura el 2026-07-03.

### España — estado actual

- ID: `gid://shopify/Page/687276622200`
- Handle: `papel-pintado-espana`
- Título actual: `Papel Pintado España`
- Publicada: sí
- Última actualización: `2024-11-06T19:45:27Z`
- Body actual: listado largo de envíos gratis a provincias.
- Público: 200, canonical propio, sin `noindex`.

### Francia — estado actual

- ID: `gid://shopify/Page/687276654968`
- Handle base: `papel-pintado-francia`
- Título actual: `Papel Pintado Francia`
- Publicada: sí
- Última actualización: `2024-11-06T19:47:59Z`
- Body actual: listado de envíos gratis a ciudades de Francia.
- Público ES: 200, canonical propio, sin `noindex`.
- Público FR correcto: `/fr/pages/papier-peint-en-france`
- URL FR incorrecta detectada: `/fr/pages/papier-peint-france` devuelve 404.

## 4. Valores propuestos

### 4.1 España — valores propuestos

Campo `title` propuesto:

`Papel pintado en España para hogares y proyectos profesionales`

Campo `body` propuesto:

```html
<h2>Papel pintado, murales y soluciones a medida en España</h2>
<p>En MatchWalls diseñamos papel pintado, murales decorativos y soluciones a medida para transformar paredes en viviendas, hoteles, restaurantes, oficinas, tiendas y espacios profesionales en España. Puedes explorar diseños contemporáneos, botánicos, artísticos, geométricos, florales o infantiles y elegir el material que mejor encaje con tu proyecto.</p>

<h2>Diseños para viviendas y proyectos profesionales</h2>
<p>Para viviendas particulares, MatchWalls ayuda a decorar salones, dormitorios, habitaciones infantiles, pasillos, comedores, cocinas y espacios de trabajo en casa con papeles pintados y murales pensados para aportar carácter sin perder equilibrio visual.</p>
<p>Para profesionales, interioristas, arquitectos, tiendas, hoteles y restaurantes, MatchWalls ofrece una base de catálogo útil para proyectos residenciales y contract, con muestras, orientación en la selección de diseños y opciones de personalización según el tipo de espacio.</p>

<h2>Muestras, materiales y personalización</h2>
<p>Antes de elegir un papel pintado o mural, recomendamos solicitar muestras para comprobar color, textura y acabado. Según el uso, el tipo de pared y el nivel de exigencia del proyecto, puedes valorar opciones como papel pintado non-woven, vinílico o soluciones autoadhesivas tipo peel and stick.</p>
<p>También puedes preparar un mural personalizado a partir de las medidas de tu pared o adaptar color, escala o composición cuando el proyecto lo requiere.</p>

<h2>Ciudades y zonas estratégicas</h2>
<p>Si buscas papel pintado en Barcelona, Madrid, Valencia, Málaga, Sevilla, Girona, Tarragona, Bizkaia, Gipuzkoa, Granada, Murcia o Zaragoza, MatchWalls puede servir como punto de partida para elegir diseño, material y muestra antes de avanzar con tu proyecto.</p>
<p>Alicante queda pendiente de decisión porque actualmente su landing pública está en noindex/nofollow.</p>

<h2>Preguntas frecuentes</h2>
<h3>¿Puedo pedir muestras antes de comprar?</h3>
<p>Sí. Las muestras ayudan a comprobar color, textura y acabado antes de decidir el papel pintado o mural definitivo.</p>

<h3>¿MatchWalls trabaja con profesionales?</h3>
<p>Sí. MatchWalls trabaja con interioristas, arquitectos, tiendas y proyectos comerciales que necesitan soporte en selección, muestras o personalización.</p>

<h3>¿Puedo crear un mural personalizado?</h3>
<p>Sí. La opción de personalización permite adaptar un mural o trabajar con una propuesta ajustada a las medidas y necesidades del espacio.</p>

<p><a href="/collections/murales">Ver papeles pintados</a> · <a href="/pages/muestras">Solicitar muestras</a> · <a href="/pages/crea-tu-mural">Crear mural personalizado</a> · <a href="/pages/profesionales">Soluciones para profesionales</a></p>
```

### 4.2 Francia — valores propuestos

Campo `title` base ES propuesto:

`Papel pintado en Francia para interiores y proyectos profesionales`

Campo `body` base ES propuesto:

```html
<h2>Papel pintado y murales para proyectos en Francia</h2>
<p>MatchWalls propone papeles pintados, murales decorativos y soluciones murales a medida para viviendas, hoteles, restaurantes, oficinas, tiendas y espacios profesionales en Francia. El objetivo de esta página es ayudar a elegir diseño, material y muestras antes de avanzar con un proyecto decorativo.</p>

<h2>Diseños para particulares y profesionales</h2>
<p>Para particulares, MatchWalls ayuda a crear ambientes decorativos en salones, dormitorios, habitaciones infantiles, pasillos, comedores, cocinas y espacios de trabajo en casa.</p>
<p>Para arquitectos de interior, decoradores, tiendas, hoteles, restaurantes y proyectos contract, MatchWalls ofrece catálogo visual, muestras y opciones de personalización para construir una propuesta decorativa coherente.</p>

<h2>Materiales, muestras y personalización</h2>
<p>La elección del material depende del uso, del soporte mural y del nivel de exigencia del proyecto. Según el contexto, se pueden estudiar opciones como papel pintado non-woven, vinílico o soluciones adhesivas tipo peel and stick.</p>
<p>Antes de confirmar, recomendamos revisar muestras y condiciones de instalación. También es posible preparar un mural personalizado a partir de las dimensiones de la pared.</p>

<h2>Ciudades estratégicas en Francia</h2>
<p>Si buscas papel pintado en París, Lyon, Toulouse, Marsella, Burdeos, Nantes, Lille, Niza, Montpellier o Estrasburgo, MatchWalls puede servir como punto de partida para elegir diseño, material y muestras antes de lanzar tu proyecto.</p>

<h2>Preguntas frecuentes</h2>
<h3>¿Puedo pedir muestras antes de comprar?</h3>
<p>Sí. Las muestras permiten comprobar color, textura y acabado antes de elegir el papel pintado o mural definitivo.</p>

<h3>¿MatchWalls trabaja con profesionales?</h3>
<p>Sí. MatchWalls trabaja con interioristas, decoradores, tiendas y proyectos comerciales en la selección de diseños, materiales y muestras.</p>

<h3>¿Puedo crear un mural personalizado?</h3>
<p>Sí. Las opciones de personalización permiten adaptar un diseño, una escala o una composición a las dimensiones y necesidades del espacio.</p>

<p><a href="/collections/murales">Ver colecciones</a> · <a href="/pages/muestras">Solicitar muestras</a> · <a href="/pages/crea-tu-mural">Crear mural personalizado</a> · <a href="/pages/profesionales">Soluciones para profesionales</a></p>
```

### 4.3 Traducción FR necesaria para Francia

No debe usarse el handle `papier-peint-france`, porque no existe.

La traducción FR debe aplicarse sobre el recurso existente y su handle localizado actual:

`/fr/pages/papier-peint-en-france`

Título FR propuesto:

`Papier peint en France pour intérieurs résidentiels et projets professionnels`

Body FR propuesto:

```html
<h2>Papiers peints, panoramiques et solutions sur mesure en France</h2>
<p>MatchWalls propose des papiers peints, panoramiques décoratifs et solutions murales sur mesure pour les intérieurs résidentiels, hôtels, restaurants, bureaux, boutiques et espaces professionnels en France. Vous pouvez explorer des designs contemporains, botaniques, artistiques, géométriques, floraux ou pour enfants, puis choisir le matériau adapté à votre projet.</p>

<h2>Des designs pour les particuliers et les professionnels</h2>
<p>Pour les particuliers, MatchWalls aide à créer des ambiances décoratives dans le salon, la chambre, la chambre d’enfant, le couloir, la salle à manger, la cuisine ou le bureau à domicile.</p>
<p>Pour les architectes d’intérieur, décorateurs, boutiques, hôtels, restaurants et projets contract, MatchWalls offre un catalogue visuel, des échantillons et des possibilités de personnalisation utiles pour construire une proposition décorative cohérente.</p>

<h2>Matériaux, échantillons et personnalisation</h2>
<p>Le choix du matériau dépend de l’usage, du support mural et du niveau d’exigence du projet. Selon le contexte, vous pouvez étudier des options comme le papier peint intissé, le vinyle ou des solutions adhésives de type peel and stick.</p>
<p>Avant de confirmer, nous recommandons de vérifier les échantillons et les conditions de pose. Vous pouvez aussi préparer un panoramique personnalisé à partir des dimensions de votre mur.</p>

<h2>Villes stratégiques en France</h2>
<p>Si vous recherchez du papier peint à Paris, Lyon, Toulouse, Marseille, Bordeaux, Nantes, Lille, Nice, Montpellier ou Strasbourg, MatchWalls peut servir de point de départ pour choisir un design, un matériau et des échantillons avant de lancer votre projet.</p>

<h2>Questions fréquentes</h2>
<h3>Puis-je commander des échantillons avant d’acheter ?</h3>
<p>Oui. Les échantillons permettent de vérifier la couleur, la texture et le rendu du matériau avant de choisir le papier peint ou le panoramique final.</p>

<h3>MatchWalls travaille-t-il avec les professionnels ?</h3>
<p>Oui. MatchWalls accompagne les architectes d’intérieur, décorateurs, boutiques et projets commerciaux dans la sélection de designs, matériaux et échantillons.</p>

<h3>Puis-je créer un panoramique personnalisé ?</h3>
<p>Oui. Les options de personnalisation permettent d’adapter un design, une échelle ou une composition aux dimensions et aux besoins de votre espace.</p>

<p><a href="/fr/collections/murales">Découvrir les collections</a> · <a href="/fr/pages/echantillons">Commander des échantillons</a> · <a href="/fr/pages/creez-votre-murale">Créer un panoramique personnalisé</a></p>
```

Nota: los enlaces FR exactos del último párrafo deben verificarse en público antes de escritura. Si alguno no existe, se usarán los equivalentes localizados reales.

## 5. Evidencia y motivo técnico

Motivo:

- Las páginas país actuales son pobres como landings SEO/GEO/AEO.
- El contenido actual se limita a listados de envío gratis.
- Los borradores `012D` mejoran intención, utilidad, contenido factual y estructura.
- `012E` confirmó que las páginas existen, están indexables y tienen canonical/hreflang.

Evidencias:

- `diagnostico-MW-GEO-LANDINGS-CONTENT-REVIEW-012E-2026-07-03.md`
- `admin-read-MW-GEO-LANDINGS-CONTENT-REVIEW-012E-2026-07-03.csv`
- `qa-publico-MW-GEO-LANDINGS-CONTENT-REVIEW-012E-2026-07-03.csv`
- lectura Admin prepropuesta `MW012FPrewritePagesRead` ejecutada el 2026-07-03.

## 6. Riesgos y efectos secundarios

| Riesgo | Nivel | Control |
|---|---|---|
| Cambiar base ES puede dejar traducciones EN/DE/NL antiguas o marcadas como obsoletas | Alto | No ejecutar hasta definir si se actualizan ahora o en lote posterior inmediato |
| Enlaces FR propuestos pueden no coincidir con handles localizados reales | Medio/Alto | Verificar cada URL FR antes de escritura |
| Alicante está en noindex/nofollow | Alto | No enlazar Alicante como estratégica en esta propuesta |
| `PageUpdateInput` no expone SEO title/meta description directo | Medio | No prometer cambios de SEO meta vía API sin validación UI/LangShop |
| Copy FR requiere validación nativa | Medio | Daniel debe aceptar riesgo lingüístico o pedir revisión nativa |
| Sitemap no quedó verificado en 012E por timeout local | Medio | Revalidar sitemap tras cualquier cambio |

## 7. Respaldo disponible

Antes de ejecutar cualquier mutación se debe crear backup local completo con:

- ID
- handle
- title
- body
- publishedAt
- updatedAt
- templateSuffix
- traducciones FR/EN/DE/NL actuales

La lectura actual ya permite construir el backup, pero el backup debe guardarse inmediatamente antes de ejecutar para evitar desfase.

## 8. Método exacto de reversión

Si falla cualquier prueba crítica:

1. Ejecutar `pageUpdate` devolviendo `title` y `body` a los valores originales de backup para:
   - `gid://shopify/Page/687276622200`
   - `gid://shopify/Page/687276654968`
2. Si se modifica traducción FR, restaurar con Shopify Translate/LangShop o `translationsRegister` usando los valores FR previos.
3. Verificar público:
   - `/pages/papel-pintado-espana`
   - `/pages/papel-pintado-francia`
   - `/fr/pages/papier-peint-en-france`
4. Registrar reversión en `registro-cambios-ejecutados.md`.

## 9. Pruebas posteriores obligatorias

Después de ejecución:

- Admin: confirmar `0 userErrors`, title/body almacenados y traducción FR si aplica.
- Público ES:
  - España 200.
  - Francia 200.
  - H1 correcto.
  - Canonical propio.
  - Sin `noindex`.
- Público FR:
  - `/fr/pages/papier-peint-en-france` 200.
  - H1 correcto.
  - Canonical propio.
  - Hreflang ES/EN/FR/DE/NL/x-default presente.
- Enlaces internos:
  - muestras;
  - profesionales;
  - crear mural;
  - colecciones;
  - geos estratégicas enlazadas.
- Sitemap:
  - páginas presentes si estaban antes;
  - sin 404 ni URLs `papier-peint-france`.
- Traducciones:
  - EN/DE/NL documentadas como pendientes o actualizadas en lote propio.

## 10. Decisión requerida antes de ejecutar

Esta propuesta **no recomienda ejecutar todavía** hasta que Daniel confirme dos decisiones:

1. ¿Se acepta excluir Alicante de los enlaces internos estratégicos hasta resolver su `noindex,nofollow`?
2. ¿Se acepta ejecutar solo ES + FR ahora, dejando EN/DE/NL para lote posterior inmediato, o prefieres cerrar primero las cinco versiones ES/EN/FR/DE/NL?

Si Daniel decide ejecutar esta propuesta tal como está, debe responder exactamente:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F`

Pero por seguridad, esta aprobación debe darse **después** de leer esta propuesta, no antes.

