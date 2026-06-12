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

print(f"¡Hola {nombre_usuario}! Tu saldo inicial es de ${saldo_inicial}.")

while True:
    print("--- MENU STEAM ---")
    fn.mostrar_menu()

    op = int(input("Ingrese el número de la opción que desea realizar: "))

    if op == 1:
        fn.mostrar_juegos(catalogo_steam)
    elif op == 2:
        nombre_buscado = input("Ingresa el nombre del juego a buscar: ").strip()
        juego_encontrado = fn.buscar_juego(catalogo_steam, nombre_buscado)

        if juego_encontrado == None:
            print("Juego no encontrado.")
        else:
            if juego_encontrado in carrito_compras:
                print("Este juego ya se encuentra en el carrito.")
            elif juego_encontrado in biblioteca_juegos:
                print("Este juego ya se encuentra en tu biblioteca.")
            else:
                carrito_compras.append(juego_encontrado)
                print(f"{juego_encontrado['titulo']} ha sido agregado al carrito.")
    elif op == 3:
        fn.mostrar_juegos(carrito_compras)
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