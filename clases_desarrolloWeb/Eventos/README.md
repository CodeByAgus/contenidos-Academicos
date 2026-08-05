# Eventos en JavaScript

## Descripción
Ejercicios prácticos sobre **Eventos en JavaScript**. Los eventos son acciones que el usuario realiza en el navegador (clicks, movimiento del mouse, presionar teclas, etc.). Aprender a detectar y responder a estos eventos es fundamental para crear aplicaciones web interactivas.

## Conceptos Practicados

### Tipos de Eventos
- **click**: cuando el usuario hace clic con el mouse
- **mouseenter/mouseleave**: cuando el mouse entra/sale de un elemento
- **keydown/keyup**: cuando se presiona/suelta una tecla
- **focus/blur**: cuando un input recibe/pierde el foco
- **change/input**: cambios en valores de inputs

### Métodos para Manejar Eventos
- **addEventListener()**: agregar un evento a un elemento
- **Event object**: propiedades del evento (e.key, e.target, etc.)
- **this**: referencia al elemento que dispara el evento

### Manipulación del DOM
- **textContent**: cambiar el texto de un elemento
- **style**: cambiar estilos CSS dinámicamente
- **classList**: agregar/quitar clases CSS

## Ejercicios Incluidos

1. **EJ-1**: Contador con Botón
   - Incrementar un contador al hacer clic
   - Mostrar el valor actualizado en pantalla

2. **EJ-2**: Cambio de Color de Fondo
   - Alternar color entre azul y rojo
   - Usar variable de estado (flag)

3. **EJ-3**: Detector de Mouse en Cuadro
   - Mostrar "Entraste" al entrar el mouse
   - Mostrar "Aquí" al salir el mouse
   - Eventos: mouseenter, mouseleave

4. **EJ-4**: Detector de Teclas Presionadas
   - Mostrar la tecla presionada en pantalla
   - Usar el evento keydown y la propiedad e.key

5. **EJ-5**: Círculo que Alterna Entre Encendido/Apagado
   - Cambiar entre amarillo (encendido) y gris (apagado)
   - Usar estado booleano

6. **EJ-6**: Cuadrado con Detector de Mouse
   - Mostrar "Mouse dentro" cuando entra el mouse
   - Mostrar "Mouse fuera" cuando sale el mouse

7. **EJ-7**: Input con Cambio de Borde en Foco
   - Borde verde cuando el input está enfocado
   - Borde gris (#ccc) cuando pierde el foco
   - Eventos: focus, blur

8. **EJ-8**: Cuadrado Interactivo
   - Cambiar de color al hacer clic
   - Agrandarse al pasar el mouse (scale 1.2)
   - Volver al tamaño original al salir
   - Usar transform para animaciones

9. **EJ-9**: Semáforo con Botón
   - Ciclar entre colores: Rojo → Amarillo → Verde
   - Reutilizar el último color para reiniciar ciclo
   - Usar array de colores

10. **EJ-10**: Simulador de Cajero
    - Botón "Depositar" aumenta el saldo
    - Botón "Retirar" disminuye el saldo
    - Validar saldo disponible al retirar
    - Usar prompt() para entrada de datos

## Competencias Adquiridas

- Entender cómo funcionan los eventos en JavaScript
- Usar addEventListener para vincular eventos a elementos
- Acceder a propiedades del evento (e.key, e.target)
- Manipular propiedades de estilo dinámicamente
- Implementar lógica condicional basada en eventos
- Usar variables de estado para controlar comportamiento
- Crear interacciones simples pero funcionales
- Validar datos del usuario en aplicaciones web

## Archivos Incluidos

- **EJ-1.html** a **EJ-10.html**: 10 ejercicios progresivos de eventos
- Cada archivo contiene HTML, CSS y JavaScript completamente funcional
