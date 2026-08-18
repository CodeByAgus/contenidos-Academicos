# 2. Creación del módulo

def mostrar_juegos(juegos):
    """Solamente muestra la lista."""
    for juego in juegos:
        print("-", juego)

def buscar_juego(juegos, titulo):
    """Retorna la posición o -1."""
    if titulo in juegos:
        return juegos.index(titulo)
    return -1

def agregar_juego(juegos, titulo):
    """Modifica la lista y retorna True o False."""
    if titulo not in juegos:
        juegos.append(titulo)
        return True
    return False

def cantidad_juegos(juegos):
    """Retorna un número entero."""
    return len(juegos)
