# Repaso - Proyecto Completo

## Descripción
Proyecto práctico que **integra todos los conceptos aprendidos** en las clases anteriores. Consiste en una página de perfil personal que combina:
- Estructura HTML semántica completa
- Estilos CSS avanzados
- Componentes como tablas y formularios
- Diseño responsive

## Conceptos Practicados

### HTML
- Estructura semántica: `<header>`, `<main>`, `<footer>`
- Elementos de contenido: headings, párrafos, enlaces, imágenes
- Tablas: `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>`
- Formularios: `<input>`, `<label>`, `<button>`
- Atributos: `for`, `id`, `name`, `type`, `placeholder`, `target`

### CSS
- **Reset de estilos**: eliminación de márgenes y padding por defecto
- **Flexbox**: layouts flexibles para header, footer y listas
- **Box-shadow**: efectos de profundidad
- **Border-radius**: esquinas redondeadas
- **Transiciones**: animaciones en hover
- **Media queries**: diseño responsive
- **Selectores avanzados**: `nth-child`, `hover`, `focus`

### Diseño
- Paleta de colores coherente (#667eea, #2c3e50)
- Jerarquía visual con tamaños y colores
- Espaciado consistente (padding, margin)
- Elementos interactivos con feedback visual

## Archivos Incluidos

### 1. Tw.HTML
Página de perfil personal con:

#### Header (Encabezado)
- Título del perfil
- Foto circular con borde
- Nombre de la persona
- Enlace externo

#### Main (Contenido)
- Sección de habilidades con listas
  - Unordered list (ul/li)
  - Ordered list con letras (type="A")
- Tabla de experiencia profesional
  - Encabezados en thead
  - Datos en tbody
  - Estilos alternados de filas
  - Hover effect

#### Footer (Pie de página)
- Formulario de contacto con:
  - Input texto (nombre)
  - Input texto (apellido)
  - Input email
  - Botón de envío
- Centrado y diseño profesional

### 2. TS.css
Hoja de estilos completa con:

#### Secciones
- **Reset global**: `*` elimina márgenes/padding
- **Body**: fuentes y color de fondo
- **Header**: encabezado con sombra y borde inferior
- **Main**: contenedor central con sombra
- **Tablas**: estilos con hover y filas alternadas
- **Footer**: fondo coloreado, formulario centrado
- **Responsive**: diseño adaptable a móviles

#### Características CSS
- Variables de color reutilizables
- Transiciones suaves en hover
- Focus states para inputs
- Flexbox para layouts
- Grid básico para tablas

## Estructura Visual

```
┌─────────────────────────────────┐
│         HEADER                  │
│      [Foto de Perfil]           │
│      Nombre: Ana María          │
│    [Visitar Google]             │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│         MAIN                    │
│  Habilidades de Servicio        │
│  - Lista 1      - Lista 2       │
│                                 │
│  Experiencia                    │
│  ┌─────────────────────────────┐│
│  │ Cargo | Empresa | Años      ││
│  ├─────────────────────────────┤│
│  │ ...                         ││
│  └─────────────────────────────┘│
└─────────────────────────────────┘

┌─────────────────────────────────┐
│         FOOTER                  │
│  [Input Nombre]                 │
│  [Input Apellido]               │
│  [Input Email]                  │
│  [Botón Enviar]                 │
└─────────────────────────────────┘
```

## Competencias Adquiridas

- Integrar múltiples elementos HTML en una página funcional
- Crear diseños visuales coherentes con CSS
- Usar Flexbox para layouts responsivos
- Diseñar tablas con estilos profesionales
- Crear formularios funcionales y accesibles
- Aplicar responsive design
- Usar pseudo-clases (hover, focus, nth-child)
- Organizar código CSS de forma clara

## Instrucciones de Uso

1. Abre `Tw.HTML` en un navegador
2. El navegador cargará automáticamente `TS.css` para los estilos
3. Completa el formulario en el footer con tus datos
4. Personaliza el contenido editando los archivos HTML y CSS

## Mejoras Aplicadas

### Correcciones Realizadas
- ✅ Eliminado comentario mal formado en HTML
- ✅ Agregado atributo `alt` a la imagen
- ✅ Completada la tabla con datos reales
- ✅ Reparado atributo `aria-rowspan` → `border="1"`
- ✅ Agregado campo de email al formulario
- ✅ Agregado botón de envío

### Mejoras de CSS
- ✅ Reset completo de estilos
- ✅ Paleta de colores coherente
- ✅ Layout profesional con flexbox
- ✅ Estilos hover en elementos interactivos
- ✅ Focus states para inputs
- ✅ Responsive design para móviles
- ✅ Comentarios explicativos en el CSS

## Notas Importantes

- La imagen (`fotomia.jpg`) debe estar en la misma carpeta que los HTML/CSS
- Los inputs se pueden personalizar con placeholders diferentes
- Los colores pueden cambiarse modificando las variables en CSS
- El diseño se adapta automáticamente a pantallas pequeñas
