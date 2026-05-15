menu = True

salir = 0

#usuarios
usuario1 = None
usuario2 = None
usuario3 = None
#contraseñas
contrasena1 = None
contrasena2 = None
contrasena3 = None

name = str(input("Ingrese su nombre: "))

while menu:
    print("1. Iniciar sesión")
    print("2. Registrar Usuario")
    print("3. Salir")
    print(f"Bievenido {name}")

    opcion = int(input("Ingrese la opción que desea: "))
    if opcion < 0 or opcion > 3:
        print("Por favor selecione una opción valida")
    else:
        if opcion == 1 and usuario1 == None and usuario2 == None and usuario3 == None:
            print("No existen registros de usuarios, debe registrar uno antes de poder iniciar sesión")
            
    if opcion == 2:

    if opcion == 3:
        print("Cerrando sesión...")
        menu = False

