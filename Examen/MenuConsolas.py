consolas = {}
ventas = {}

def menu():
    print("##### MENU CONSOLAS ####")
    print("1. Agregar consola")
    print("2. Buscar consola por sigla")
    print("3. Eliminar consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")
    print("#"*30)

def opcion():
    while True:
        try:
            op = int(input("Seleccione su opción: "))
            return op
        except ValueError:
            print("Seleccione una opción valida")

def agregar_consola(consolas, ventas):
    sigla = input("Ingrese la sigla: ").strip()
    if not validacion_sigla(sigla):
        print("Ingrese una sigla valida")
        return
    if validacion_sigla_existente(consolas, sigla):
        print("Esta sigla ya existe")
        return
    
    nombre = input("Ingrese el nombre: ")
    if not validacion_nombre(nombre):
        print("Ingrese un nombre valido")
        return
    
    fabricante = input("Ingrese el fabricante: ")
    if not validacion_fabricante(fabricante):
        print("Ingrese un fabricante valido")
        return
    
    ano_lanzamiento = convertir_entero(input("Ingrese el ano de lanzamiento: "))
    if ano_lanzamiento is False or not validacion_anolanzamiento(ano_lanzamiento):
        print("Ingrese un ano valido")
        return
    
    precio = convertir_float(input("Ingrese el precio: "))
    if precio is False or not validacion_precio(precio):
        print("Ingrese un precio valido")
        return
    
    stock = convertir_entero(input("Ingrese el stock disponible: "))
    if stock is False or not validacion_stock(stock):
        print("Ingrese un stock valido..")
        return
    
    consolas[sigla] = [nombre, fabricante, ano_lanzamiento] # se puede hacer de tal manera: consolas[sigla] = [nombre, fabricante, int(ano_lanzamiento)]
    ventas[sigla] = [precio, stock] 
    print("Se ha agregado la consola.")
    

def validacion_sigla(sigla):
    if not (2 <= len(sigla) <= 5):
        return False
    if not sigla.isalnum():
        return False
    if not sigla.isupper():
        return False
    else:
        return True

def validacion_sigla_existente(consolas, sigla):
    if sigla in consolas:
        return True
    

def validacion_nombre(nombre):
    if not (3 <= len(nombre) <= 40):
        return False
    else:
        return True

def validacion_fabricante(fabricante):
    if not (2 <= len(fabricante) <= 30):
        return False
    else:
        return True

def validacion_anolanzamiento(ano_lanzamiento): # .isdigit
    if not (1972 <= ano_lanzamiento <= 2025):
        return False
    else:
        return True

def validacion_precio(precio): 
    try:
        if not precio > 0:
            return False
        else:
            return True
    except ValueError:
        return False

def validacion_stock(stock): # if not stock.isdigit return false, same as ano
    if not stock >= 0:
        return False
    else:
        return True
    
def convertir_entero(input):
    try:
        return int(input)
    except ValueError:
        return False 

def convertir_float(input):
    try:
        return float(input)
    except ValueError:
        return False

def buscar_interactivo(consolas, ventas):
    sigla = input("Ingrese la consola a buscar (SIGLA): ")
    busqueda = buscar_consola(consolas, ventas, sigla)
    if not busqueda:
        print("No hay consolas")

def buscar_consola(consolas, ventas, sigla):
    if not sigla in consolas:
        return False
    else:
        print("###### Consola Encontrada #####")
        print(f"Sigla: {sigla}")
        print(f"Nombre: {consolas[sigla][0]}")
        print(f"Fabricante: {consolas[sigla][1]}")
        print(f"Ano Lanz: {consolas[sigla][2]}")
        print(f"Precio: {ventas[sigla][0]}")
        print(f"Stock: {ventas[sigla][1]}")
        return True

def eliminar_consola(consolas, ventas):
    sigla = input("Ingrese la sigla a eliminar: ")
    consola = buscar_consola(consolas, ventas, sigla)
    
    if consola:
        decision = input("Desea eliminar la consola? s/n: ")
        if decision == "s":
            del consolas[sigla]
            del ventas[sigla]
            print("### Consola eliminada ###")
        else:
            print("La consola no se ha eliminado")
    else:
        print("No se ha encontado la consola")
    
def mostrar_consola(consolas, ventas):
    if not consolas:
        print("No hay consolas registradas")
    else:
        print("==============================")
        print("LISTADO COMPLETO DE CONSOLAS")
        print("==============================")
        for sigla in consolas:
            nombre, fabricante, ano = consolas[sigla]
            precio, stock = ventas[sigla]
            print(f" {sigla} - {nombre} - {fabricante} - {ano} - {precio} - {stock}")
            print("==============================")
        print(f"Total de consolas: {len(consolas)}")

while True:
    menu()
    op = opcion()
    if op == 1:
        agregar_consola(consolas, ventas)
    elif op == 2:
        buscar_interactivo(consolas, ventas)
    elif op == 3:
        eliminar_consola(consolas, ventas)
    elif op == 4:
        mostrar_consola(consolas, ventas)
    elif op == 5:
        print("Saliendo...")
        break
    else:
        print("Escoja una opcion valida")