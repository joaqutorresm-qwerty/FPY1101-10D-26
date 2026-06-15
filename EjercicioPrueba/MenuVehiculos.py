import Funciones as fn

while True:
    fn.menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        fn.agregar_vehiculo()
    elif opcion == "2":
        fn.buscar_vehiculo()
    elif opcion == "3":
        fn.eliminar_vehiculo()
    elif opcion == "4":
        fn.actualizar_disponibilidad()
    elif opcion == "5":
        fn.mostrar_vehiculos()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")