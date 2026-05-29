productos = {
    "Mouse": [10, 15000],
    "Teclado": [5, 25000],
    "Monitor": [3, 180000]
}

#Definiendo funciones
def agregar_producto(productos):
    nombre = input("Nombre del producto: ").strip()

    if nombre == "":
        print("El nombre no puede ser vacío.")
        return
    
    if nombre in productos:
        print("El producto ya existe..")
        return

    stock = int(input("Ingrese stock: "))
    precio = int(input("Ingrese el precio$: "))

    productos[nombre] = [stock,precio]
    print("Productos agregados correctamente!")

opcion_menu = 0

while True:
    print("---MENU---")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Producto mas caro")
    print("5. Salir")
    while True:
        try:
            opcion_menu = int(input("Ingrese su opción: "))
            break
        except ValueError:
            print("Ingrese un número valido e intentelo nuevamente")
    
    if opcion_menu == 1:
        agregar_producto(productos)
    #elif opcion_menu == 2:
        #mostrar_productos(productos)
    #elif opcion_menu == 3:
        #buscar_productos(productos)
    #elif opcion_menu == 4:
        #producto_mas_caro(productos)
    #elif opcion_menu == 5:
        #print("Fin del programa...")
        #break
    else:
        print("Opción inválida!")