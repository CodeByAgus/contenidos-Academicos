# 8. Módulo del Desafío Integrador

def crear_catalogo_inicial():
    return ["Halo", "Minecraft", "Zelda", "Metroid", "Mario", "Fortnite", "Valorant", "Hades", "Celeste", "Portal"]

def mostrar_catalogo(lista):
    print(f"Catálogo ({len(lista)} elementos):")
    for j in lista:
        print(f" - {j}")

def buscar_titulo(lista, titulo):
    return lista.index(titulo) if titulo in lista else -1

def agregar_titulo(lista, titulo):
    if titulo not in lista:
        lista.append(titulo)
        return True
    return False

def aplicar_filtro_longitud(lista):
    return [j for j in lista if len(j) > 8]

es_titulo_largo = lambda titulo: len(titulo) > 8
