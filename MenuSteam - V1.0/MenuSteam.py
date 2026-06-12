import FuncionesSteam as fn

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




print("Bienvenido a Steam, por favor ingrese su nombre de Usuario.")
nombre_usuario = input("-> ")
saldo_inicial = 0


while True:
    print("--- MENU STEAM ---")
    fn.mostrar_menu()

    op = int(input("Ingrese el número de la opción que desea realizar: "))

    if op == 1:
        print("TEST")
    elif op == 2:
        fn.buscar_juego(catalogo_steam, carrito_compras) 
    elif op == 3:
        print("W")
    elif op == 4:
        print("W")
    elif op == 5:
        print("W")
    elif op == 6:
        print("W")
    elif op == 7:
        print("¡Saliendo del programa!")
        break
    else:
        print("Escoja una opción valida.")   