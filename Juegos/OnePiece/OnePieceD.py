def elegir_raza():
    print("Bienvenido al mundo de One Piece, para empezar, escoje tu RAZA")
    print("--- RAZAS DISPONIBLES ---")
    print("1. Humano")
    print("2. Skypiean")
    print("3. Gyojin")
    print("4. Mink")

    raza = input("- ")

def minijuego():
    print("Escoje un número del 1 al 5")
    num = int(input("-" ))

    if num == 1:
        print("Obtienes una Katana")
        Katana = 500
    elif num == 2:
        print("Obtienes un Tirachinas")
        Tira_Chinas = 350
    elif num == 3:
        print("Obtienes la Gomu Gomu no Mi")
        GomuG = 1000
    elif num == 4:
        print("Obtienes un tesoro con $5.000 Berries")
        Dinero =+ 5000
    elif num == 5:
        print("No obtienes nada!")
        return
    else:
        print("Escoje un número del 1 al 5!")
        return

def revisar_inventario():
    print(personaje)


personaje = {}

elegir_raza()

minijuego()

while True:
    print("Bien, ahora veamos, que quieres hacer??")
    print("1. Revisar inventario")

    while True:
        try:
            op = int(input("Escoje tu opción: "))
            break
        except ValueError:
            print("Escoje una opción valida")
    
    if op == 1:
        revisar_inventario()