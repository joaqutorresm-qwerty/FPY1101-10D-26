def mostrar_menu():
    print("--- MENU TAREAS ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver tareas ordenadas")
    print("4. Salir")

def agregar_tarea(tareasD):
    
    while True:
        try:
            cant_tareas = int(input("Ingrese la cantidad de tareas: "))
            if cant_tareas > 0:
                break
            else:
                print("La cantidad de tareas debe ser mayor a cero")
        except ValueError:       
            print("Debe ingresar una nota valida!, vuelva a intentar..")

    tarea = []

    for i in range(cant_tareas): 
        print("Ingrese el nombre de la tarea")
        tarea = (input("-> "))
        tareasD.append(tarea)
        print("Tarea ingresada!")

def imprimir_tareas(tareasD):
    if len(tareasD) == 0:
        print("No hay tareas pendientes")
        return
    
    print(tareasD)

def eliminar_tarea(tareasD):
    quitar = input("Igrese la tarea que quiere eliminar: ").strip().capitalize()
    if quitar in tareasD:
        print("Tarea eliminada")
        tareasD.remove(quitar)

tareasD = []

while True:
    mostrar_menu()
    while True:
        try:
            op = int(input("Escoja una opción: "))
            break
        except ValueError:
            print("Escoja un número valido.")
    
    if op == 1:
        agregar_tarea(tareasD)
    elif op == 2:
        eliminar_tarea(tareasD)
    elif op == 3:
        imprimir_tareas(tareasD)
    elif op == 4:
        print("Saliendo...")
        break
    else:
        print("Opcioón invalida")