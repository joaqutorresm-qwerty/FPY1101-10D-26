catalogo_steam = [
{"titulo" : "Elden Ring", "precio" : 45499},
{"titulo" : "Cyberpunk 2077", "precio" : 39999},
{"titulo" : "Stardew Valley", "precio" : 7500},
{"titulo" : "Hollow Knight", "precio" : 8300},
{"titulo" : "Sekiro: Shadows Die Twice", "precio" : 47650},
{"titulo" : "Resident Evil 4", "precio" : 27600},
{"titulo" : "Dead by Daylight", "precio" : 11994},
{"titulo" : "Clair Obscur: Expedition 33", "precio" : 39990},
{"titulo" : "Project Zomboid", "precio" : 10500},
{"titulo" : "Backrooms: Escape Together", "precio" : 5750},
{"titulo" : "Lethal Company", "precio" : 5750},
{"titulo" : "Helldivers 2", "precio" : 28000},
{"titulo" : "Red Dead Redemption 2", "precio" : 35948},
{"titulo" : "God of War", "precio" : 35000}
]

carrito_compras = []
biblioteca_juegos = []

def mostrar_menu():
    print("1. Ver Catálogo de Tienda")
    print("2. Agregar juego al Carrito")
    print("3. Ver mi Carrito")
    print("4. Cargar fondos a la Cartera")
    print("5. Pagar Carrito")
    print("6. Ver mi Biblioteca")
    print("7. Salir")

def mostrar_juegos(lista_generica):
    print("Wip")

def calcular_total(lista_generica):
    print("WIP")

def buscar_juego(catalogo, nombre_buscado):
    busca_juego = input("Ingresa el nombre del juego a buscar: ").lower()
    carrito_compras.append(busca_juego)

    if busca_juego not in catalogo_steam:
        print("El juego que buscas no existe.")
    
    if busca_juego in carrito_compras:
        print("Este juego ya esta en tu carrito")
    
    