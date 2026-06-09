def ingresar_reserva():
    nombre = input("Ingrese su nombre: ").strip().lower()
    
    if nombre == "":
        print("El nombre no puede estar vacío")
        return
    
    if nombre.isdigit():
        print("Por favor, ingrese un nombre valido")
        return
    
    if nombre in reservas:
        print("El nombre ya existe")
        return
    
    pelicula = input("Introduzca el nombre de la pelicula: ")

    if pelicula == "":
        print("La pelicula no puede estar vacía")
        return

    if pelicula.isdigit():
        print("Por favor, ingrese un nombre valido")
        return

    try:
        cant_reservas = int(input("Ingrese la cantidad de reservas: "))
    except ValueError:
        print("Ingrese un número valido")
        return

    if cant_reservas > 10 or cant_reservas < 1:
        print("Por favor, escoja mas de 1 reservas y menos de 10 reservas.")
        return
    
    reservas[nombre] = [pelicula,cant_reservas]
    print("Reserva realizada exitosamente!")

def buscar_reserva():
    if len(reservas) == 0:
        print("No hay usuarios ingresados")
    
    nombre = input("Nombre a buscar: ").strip().lower()

    if nombre in reservas:
        print("Usuario encontrado:")
        print(f"Pelicula: {reservas[nombre][0]}")
        print(f"Reservas: {reservas[nombre][1]}")
    else:
        print("Usuario no encontrado")

def eliminar_reserva():
    if len(reservas) == 0:
        print("No hay reservas ingresadas")
    
    quitar = input("Igrese la reserva a eliminar: ").strip().lower()

    if quitar in reservas:
        print("Reserva eliminada")
        del reservas[quitar]
    else:
        print("Reserva no encontrada")

def mostrar_reservas():
    if len(reservas) == 0:
        print("No existen reservas")
        return
    
    for nombre, datos in reservas.items():
        print("-", nombre, "Pelicula:", datos[0], "Reservas:", datos[1])


reservas = {}

while True:
    print("------------")
    print("--- MENU ---")
    print("1. Reservar Entrada")
    print("2. Buscar Reserva")
    print("3. Cancelar Reserva")
    print("4. Ver todas las Reservas")
    print("5. Salir")

    while True:
        try:
            op = int(input("Ingrese una opción: "))
            break
        except ValueError:
            print("Escoja una opción valida")
    
    if op == 1:
        ingresar_reserva()
    elif op == 2:
        buscar_reserva()
    elif op == 3:
        eliminar_reserva()
    elif op == 4:
        mostrar_reservas()
    elif op == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Escoja una opción valida.")