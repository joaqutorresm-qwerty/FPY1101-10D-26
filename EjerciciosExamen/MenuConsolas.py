consolas = {}
ventas = {}

def menu():
    print("--- MENU PRINCIPAL ---")
    print("1. Agregar consola")
    print("2. Buscar consola por sigla")
    print("3. Eliminar consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")

def opcion():
    print("Escoja su opción..")
    while True:
        try:
            op = int(input("--> "))
        except ValueError:
            print("Elija una opción valida")
        
        if op == 1:
            agregar_consola()
        elif op == 2:
            print
        elif op == 3:
            print
        elif op == 4:
            print
        elif op == 5:
            print("Saliendo del programa..")
            break
        else:
            print("Escoja una opción valida")

def agregar_consola():
    sigla = str(input("Ingrese la sigla de la consola a ingresar: ")).upper().strip()
    if not validacion_siglas(sigla):
        print("")
    nombre = str(input("Ingrese el nombre de la consola: "))
    if not validacion_nombre(nombre):
        print("")
    fabricante = str(input("Ingrese el nombre del fabricante: "))
    if not validacion_fabricante(fabricante):
        print("")
    año_lanzamiento = int(input("Ingrese el año de su lanzamiento: "))
    if not validacion_año_lanz(año_lanzamiento):
        print("")
    precio = float(input("Ingrese el precio de la consola: "))
    if not validacion_precio(precio):
        print("")
    stock = int(input("Ingrese el stock disponible de la consola: "))
    if not validacion_stock(stock):
        print("")
    
    

def validacion_siglas(sigla):
    if len(sigla) < 2 and len(sigla) > 5:
        return False

    if sigla in sigla:
        return False

def validacion_nombre(nombre):
    if len(nombre) < 3 and len(nombre) > 40:
        return False

    if len(nombre) == 0:
        return False

def validacion_fabricante(fabricante):
    if len(fabricante) < 2 and len(fabricante) > 30:
        return False

    if len(fabricante) == 0:
        return False

def validacion_año_lanz(año_lanzamiento):
    if año_lanzamiento > 1972 or año_lanzamiento > 2025:
        return False

    if año_lanzamiento <= 1972 or año_lanzamiento <= 2025:
        return True

def validacion_precio(precio):
    if precio < 0:
        return False

    if precio > 0:
        return True

def validacion_stock(stock):
    if stock < 0:
        return False
    
    if stock >= 0:
        return True

while True:
    menu()
    opcion()