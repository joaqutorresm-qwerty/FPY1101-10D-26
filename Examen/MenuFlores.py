arreglos = {}
bodega = {}

def menu():
    print("====== MENU PRINCIPAL ======")
    print("1. Unidades por tipo de arreglo")
    print("2. Busqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=" * 30)

def leer_opcion():
    while True:
        try:
            opcion = int(input("Escoja la opcion que desea ver/usar: "))
            return opcion
        except ValueError:
            print("Escoja una opcion valida")

def unidades_tipo(arreglos, bodega):
    tipo = input("Ingrese el tipo de arreglo: ").casefold()
    total = 0
    for codigo, datos in arreglos.items():
        if datos[1].casefold() == tipo.casefold():
            unidades = bodega[codigo][1]
            total += unidades
    print(f"Total de unidades para el tipo {tipo}: {total}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for codigo, datos in bodega.items():
        precio = datos[0]
        unidades = datos[1]
        if p_min <= precio <= p_max and unidades != 0:
            nombre = arreglos[codigo][0]
            resultados.append(f"{nombre}--{codigo}")
    
    resultados.sort()
    
    if not resultados:
        print("No hay arreglos en ese rango de precios.")
    else:
        for arreglo in resultados:
            print(arreglo)

def busqueda_precio_menu():
    while True:
        try:
            p_min = int(input("Ingrese el precio minimo: "))
            p_max = int(input("Ingrese el precio maximo: "))
        except ValueError:
            print("Debe ingresar valores enteros")
            continue

        if p_min < 0 or p_max < 0 or p_min > p_max:
            print("Los valores deben ser mayores o iguales a cero y el minimo no puede ser mayor al maximo")
            continue

        break

    busqueda_precio(p_min, p_max)

def buscar_codigo(codigo):
    for clave in bodega:
        if clave.casefold() == codigo.casefold():
            return True
    return False

def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo):
        for clave in bodega:
            if clave.casefold() == codigo.casefold():
                bodega[clave][0] = nuevo_precio
                return True
    return False

def actualizar_precio_menu():
    while True:
        codigo = input("Ingrese el codigo del arreglo: ")

        while True:
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                if nuevo_precio <= 0:
                    print("El precio debe ser un numero entero positivo")
                    continue
                break
            except ValueError:
                print("Debe ingresar un valor entero")

        if actualizar_precio(codigo, nuevo_precio):
            print("Precio actualizado")
        else:
            print("El codigo no existe")

        repetir = input("¿Desea actualizar otro precio (s/n)? ").casefold()
        if repetir == "n":
            break

def agregar_arreglo(arreglos, bodega):
    print("A continuacion se le pediran diferentes datos para agregar su arreglo..")

    codigo = input("Ingrese el codigo de su arreglo: ")
    if not validar_codigo(codigo) or validar_codigo_existente(arreglos, codigo):
        print("El codigo no puede estar vacio ni con espacios en blanco (Si ya existe, tampoco se puede registrar)")
        return
    
    nombre = input("Nombre del arreglo: ")
    if not validar_nombre(nombre):
        print("El nombre no puede estar vacio ni tener solo espacios en blanco")
        return
    
    tipo = input("Tipo del arreglo: ").casefold()
    if not validar_tipo(tipo):
        print("El tipo no puede estar vacio ni tener solo espacios en blanco")
        return
    
    color_principal = input("Color de arreglo: ")
    if not validar_color(color_principal):
        print("El color no puede estar vacio ni tener solo espacios en blanco")
        return
    
    tamano = input("Tamano del arreglo (S/M/L): ")
    if not validar_tamano(tamano):
        print("El tamano solo puede ser: S, M o L")
        return
    
    incluye_tarjeta = input("Incluye tarjeta? s/n: ").lower()
    if validar_tarjeta(incluye_tarjeta):
        print("Tarjeta agregada")
    elif not validar_tarjeta(incluye_tarjeta):
        print("Tarjeta no agregada")

    temporada = input("Temporada del arreglo: ")
    if not validar_temporada(temporada):
        print("La temporada no puede estar vacio ni tener solo espacios en blanco")
        return
    
    precio = input("Precio del arreglo: ")
    if not validar_precio(precio):
        print("El precio debe ser un numero entero mayor que cero")
        return

    unidades = input("Unidades del arreglo: ")
    if not validar_unidades(unidades):
        print("Las unidades deben ser un numero entero mayor o igual que cero")

    arreglos[codigo] = [nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada]
    bodega[codigo] = [int(precio), int(unidades)]


def validar_codigo(codigo):
    if not codigo.strip():
        return False
    else:
        return True
def validar_codigo_existente(arreglos, codigo):
    if codigo in arreglos:
        return True

def validar_nombre(nombre):
    if not nombre.strip():
        return False
    else:
        return True

def validar_tipo(tipo):
    if not tipo.strip():
        return False
    else:
        return True

def validar_color(color_principal):
    if not color_principal.strip():
        return False
    else:
        return True

def validar_tamano(tamano):
    if tamano == "S" or tamano == "M" or tamano == "L":
        return True
    else:
        return False

def validar_tarjeta(incluye_tarjeta):
    if incluye_tarjeta == "s":
        return True
    elif incluye_tarjeta == "n":
        return False

def validar_temporada(temporada):
    if not temporada.strip():
        return False
    else:
        return True

def validar_precio(precio):
    try:
        precio = int(precio)
        if not precio > 0:
            return False
        else:
            return True
    except ValueError:
        return False

def validar_unidades(unidades):
    try:
        unidades = int(unidades)
        if not unidades >= 0:
            return False
        else:
            return True
    except ValueError:
        return False

def eliminar_arreglo(codigo):
    if buscar_codigo(codigo):
        for clave in bodega:
            if clave.casefold() == codigo.casefold():
                del arreglos[clave]
                del bodega[clave]
                return True
    return False

def eliminar_arreglo_menu():
    codigo = input("Ingrese el codigo del arreglo a eliminar: ")

    if eliminar_arreglo(codigo):
        print("Arreglo eliminado")
    else:
        print("El codigo no existe")

while True:
    menu()
    opcion = leer_opcion()

    if opcion == 1:
        unidades_tipo(arreglos, bodega)
    elif opcion == 2:
        busqueda_precio_menu()
    elif opcion == 3:
        actualizar_precio_menu()
    elif opcion == 4:
        agregar_arreglo(arreglos, bodega)
    elif opcion == 5:
        eliminar_arreglo_menu()
    elif opcion == 6:
        print("Saliendo del sistema...")
        break
    else:
        print("Escoja una opcion valida")
    