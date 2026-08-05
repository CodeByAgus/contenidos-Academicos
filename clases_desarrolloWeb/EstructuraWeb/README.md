# Estructura Web - Componentes Base

## Descripción
Ejemplos de **componentes fundamentales** que forman la estructura típica de un sitio web. Estos componentes se pueden reutilizar y personalizar para crear diferentes tipos de páginas web.

## Conceptos Practicados

### Estructura Semántica
- **`<header>`**: encabezado de la página con navegación
- **`<main>`**: contenido principal de la página
- **`<footer>`**: pie de página con información adicional
- **`<aside>`**: barra lateral (sidebar) para contenido secundario
- **`<section>`**: secciones temáticas de contenido

### Técnicas de Diseño CSS
- **Flexbox**: alineación y distribución flexible de elementos
- **Grid**: layouts de múltiples columnas
- **Box-shadow**: efectos de profundidad
- **Responsive design**: adaptación a diferentes tamaños de pantalla
- **Transiciones**: animaciones suaves

### Patrones de Interfaz
- **Card layout**: contenedores independientes para información
- **Navigation bar**: menú de navegación horizontal
- **Sidebar**: barra lateral con widgets
- **Carousel/Slider**: galería de imágenes deslizable
- **Grid system**: distribución de contenido en columnas

## Componentes Incluidos

### 1. Header (Encabezado)
**Archivo:** `Header/Base.html`

Componente superior de la página con:
- Logo con icono gradiente
- Menú de navegación horizontal
- Botones de login/signup a la derecha
- Diseño sticky (se queda fijo al scrollear)
- Estilos hover con animaciones
- Responsive para dispositivos móviles

**Características CSS:**
- Flexbox para alineación
- Pseudo-elemento `::after` para efecto de subrayado
- Gradients para el icono del logo
- Media queries para mobile

### 2. Main (Contenido Principal)
**Archivo:** `Main/Base.html`

Estructura para el contenido central con:
- Título y párrafos con jerarquía tipográfica
- Artículos en tarjetas (cards) con sombra
- Secciones organizadas
- Grid responsive para múltiples tarjetas
- Botones con estilos hover
- Imágenes responsive
- Listas ordenadas y desordenadas

**Características CSS:**
- Layout centrado con max-width
- Cards con sombra y hover effect
- Grid auto-responsive
- Reset de estilos por defecto

### 3. Footer (Pie de Página)
**Archivo:** `Footer/Base.html`

Pie de página completo con:
- 3 columnas de enlaces (Company, Support, Legal)
- Sección de copyright y bottom links
- Diseño oscuro profesional
- Efectos hover en enlaces
- Grid layout para columnas
- Responsive (una columna en mobile)

**Características CSS:**
- Grid de 3 columnas
- Colores oscuros contrastados
- Flex para footer-bottom
- Separador con border-top

### 4. Sidebar (Barra Lateral)
**Archivo:** `Sidebar/Base.html`

Componente lateral con widgets:
- Buscador
- Lista de categorías
- Widgets en cards
- Layout flexbox
- Ancho fijo
- Ejemplos de inputs con focus states

**Características CSS:**
- Flex layout vertical
- Width fijo de 300px
- Widgets con sombra
- Border-bottom en títulos

### 5. Carousel (Carrusel de Imágenes)
**Archivo:** `Carousel/Base.html`

Galería deslizable de imágenes con:
- Botones de navegación (anterior/siguiente)
- Indicadores de slides
- Altura fija (400px)
- Imágenes responsive
- Transiciones suaves
- z-index para capas

**Características CSS:**
- Position relative/absolute para botones
- Overflow hidden para clipping
- Flex para centrar contenido
- Object-fit para imágenes

## Estructura HTML Común

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Título de la página</title>
    <style>
        /* Reset */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        /* Estilos... */
    </style>
</head>
<body>
    <!-- Contenido HTML -->
</body>
</html>
```

## Competencias Adquiridas

- Comprender la estructura semántica de un sitio web
- Usar Flexbox y Grid para layouts modernos
- Crear componentes reutilizables
- Aplicar responsive design
- Trabajar con pseudo-elementos y pseudo-clases
- Crear animaciones y transiciones suaves
- Diseñar interfaces profesionales
- Optimizar código CSS con reset y variables

## Notas Importantes

- Cada archivo contiene **comentarios detallados** explicando cada propiedad CSS
- Los comentarios especifican **alternativas** para cada valor
- Todos los componentes son **responsive** para mobile
- Los archivos pueden ser usados como **base/template** para proyectos reales

## Uso de Estos Componentes

Estos componentes pueden ser:
1. Combinados para crear una página completa
2. Personalizados con colores y fuentes propias
3. Extendidos con más funcionalidad JavaScript
4. Usados como referencia para otros proyectos
