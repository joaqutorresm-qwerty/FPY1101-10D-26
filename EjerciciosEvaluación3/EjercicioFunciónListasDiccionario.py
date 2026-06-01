#productos = {
#    "Mouse": [10, 15000],
#    "Teclado": [5, 25000],
#    "Monitor": [3, 180000]
#}

productos = {}

#Definiendo funciones
def agregar_producto(productos):
    nombre = input("Nombre del producto: ").strip()

    if nombre.isdigit():
        print("Debe ingresar letras")
        return

    if nombre == "":
        print("El nombre no puede ser vacío.")
        return
    
    if nombre in productos:
        print("El producto ya existe..")
        return

    while True:
        try:
            stock = int(input("Ingrese stock: "))
            if stock > 0:
                break
            else:
                print("El stock debe ser mayor a cero")
        except ValueError:       
            print("Debe ingresar un número!! vuelva a intentar..")

    while True:
        try:
            precio = int(input("Ingrese el precio: $"))
            if precio > 0:
                break
            else:
                print("Debe ingresar un número!! intentelo de nuevo...")
        except ValueError: 
            print("Debe ingresar un número!! vuelva a intentar..")


    productos[nombre] = [stock,precio]
    print("Productos agregados correctamente!")

def mostrar_productos(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    
    for nombre in productos:
        print(nombre, "-Stock:", productos[nombre][0], "-Precio:", productos[nombre][1])

def buscar_productos(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    
    nombre = input("Nombre producto a buscar: ").strip()

    if nombre in productos:
        print("Producto encontrado")
        print(f"-Stock: {productos[nombre][0]}")
        print(f"-Precio $: {productos[nombre][1]}")
    else:
        print("Producto no encontrado")

def producto_mas_caro(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    
    mayor = 0
    mayorname = ""

    for nombre in productos:
        precio = productos[nombre][1]
        if precio > mayor:
            mayor = precio
            mayorname = nombre
    print(f"Su producto mas caro es: {mayorname}")
    print(f"El precio es: {mayor}")        

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
    elif opcion_menu == 2:
        mostrar_productos(productos)
    elif opcion_menu == 3:
        buscar_productos(productos)
    elif opcion_menu == 4:
        producto_mas_caro(productos)
    elif opcion_menu == 5:
        print("Fin del programa...")
        break
    else:
        print("Opción inválida!")