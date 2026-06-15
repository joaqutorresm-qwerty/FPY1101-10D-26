def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("=====================================")

modelo = []
año = []
precio = []
disponibilidad = []
consesionaria = {}

def agregar_vehiculo():
    global consesionaria

    agregar_auto = str(input("Ingrese el modelo del Vehículo: "))

    if agregar_auto in modelo:
        print("El vehículo ya existe en el sistema.")

    if agregar_auto == "":
        print("No puede dejar el campo vacío.")
        return
        
    año_auto = int(input("Ingrese el año del Vehículo: "))

    if año_auto < 1900:
        print("El año del vehículo no puede ser menor a 1900.")
        return

    if año_auto == "":
        print("No puede dejar el campo vacío.")
        return

    if not isinstance(año_auto, int):
        print("El año del vehículo debe ser un número entero.")
    
    precio_auto = float(input("Ingrese el precio del Vehículo: "))

    if precio_auto < 0:
        print("El precio del vehículo no puede ser negativo.")

    if not isinstance(precio_auto, (int, float)):
        print("El precio del vehículo debe ser un número.")

    print("Agregando vehículo...")
    modelo.append(agregar_auto)
    año.append(año_auto)
    precio.append(precio_auto)
    disponibilidad.append(True)
    consesionaria[agregar_auto] = {"año": año_auto, "precio": precio_auto, "disponibilidad": True}
    print("Vehículo agregado exitosamente.")

def buscar_vehiculo():
    global consesionaria

    if len(modelo) == 0:
        print("No hay vehículos registrados en el sistema.")
        return

    buscar_auto = str(input("Ingrese el modelo del Vehículo a buscar: "))

    if buscar_auto in modelo:
        print(f"Modelo: {buscar_auto}")
        print(f"Año: {consesionaria[buscar_auto]['año']}")
        print(f"Precio: {consesionaria[buscar_auto]['precio']}")
        print(f"Disponibilidad: {'Disponible' if consesionaria[buscar_auto]['disponibilidad'] else 'No disponible'}")
    else:
        print("El vehículo no se encuentra en el sistema.")
    
def eliminar_vehiculo():
    global consesionaria

    if len(modelo) == 0:
        print("No hay vehículos registrados en el sistema.")
        return

    eliminar_auto = str(input("Ingrese el modelo del Vehículo a eliminar: "))

    if eliminar_auto in modelo:
        index = modelo.index(eliminar_auto)
        del modelo[index]
        del año[index]
        del precio[index]
        del disponibilidad[index]
        del consesionaria[eliminar_auto]
        print("Vehículo eliminado exitosamente.")
    else:
        print("El vehículo no se encuentra en el sistema.")
    
def actualizar_disponibilidad():
    global consesionaria

    if len(modelo) == 0:
        print("No hay vehículos registrados en el sistema.")
        return

    actualizar_auto = str(input("Ingrese el modelo del Vehículo para actualizar su disponibilidad: "))

    if actualizar_auto in modelo:
        index = modelo.index(actualizar_auto)
        disponibilidad[index] = not disponibilidad[index]
        consesionaria[actualizar_auto]['disponibilidad'] = disponibilidad[index]
        print(f"Disponibilidad del vehículo '{actualizar_auto}' actualizada exitosamente.")
    else:
        print("El vehículo no se encuentra en el sistema.")

def mostrar_vehiculos():
    global consesionaria

    if len(modelo) == 0:
        print("No hay vehículos registrados en el sistema.")
        return

    print("========== VEHÍCULOS REGISTRADOS ==========")
    for i in range(len(modelo)):
        print(f"Modelo: {modelo[i]}")
        print(f"Año: {consesionaria[modelo[i]]['año']}")
        print(f"Precio: {consesionaria[modelo[i]]['precio']}")
        print(f"Disponibilidad: {'Disponible' if consesionaria[modelo[i]]['disponibilidad'] else 'No disponible'}")
        print("-----------------------------------------")