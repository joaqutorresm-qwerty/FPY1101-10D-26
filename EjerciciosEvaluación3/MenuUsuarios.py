def ingresar_usuario():
    usuario = input("Ingrese el nombre del usuario: ").strip()
    if usuario == "":
        print("El nombre no puede estar vacio")
    
    if usuario in usuarios:
        print("Este usuario ya esta ingresado")
    
    sexo = []

    while True:
        try:
            sexo = (input("Ingrese el sexo del usuario (F/M): "))
            break
        except ValueError:
            print("Ingrese una letra")

    if sexo == "":
        print("El sexo no puede estar vacio")
    
    if sexo.upper() != "F" and sexo.upper() != "M":
        print("El sexo debe ser F o M")
        return
    
    contrasena = input("Ahora ingrese su contraseña: ")

    if len(contrasena) < 8:
        print("La contraseña debe tener al menos 8 caracteres")
        return
    
    if contrasena == "":
        print("La contraseña no puede estar vacia")
    
    if contrasena.isalpha() or contrasena.isdigit():
        print("La contraseña debe contener letras y números")
        return

    usuarios[usuario] = [sexo,contrasena]
    


def buscar_usuario(usuarios):
    if len(usuarios) == "":
        print("No hay usuarios ingresados")
    
    usuario = input("Nombre del usuario: ").strip()

    if usuario in usuarios:
        print("Usuario encontrado:")
        print(f"-Sexo: {usuarios[usuario][0]}")
        print(f"-Contraseña: {usuarios[usuario][1]}")
    else:
        print("Usuario no encontrado")

def eliminar_usuario(usuarios):
    if len(usuarios) == "":
        print("No hay usuarios ingresados")
    
    usuario = input("Nombre del usuario a eliminar: ").strip()

    if usuario in usuarios:
        del usuarios[usuario]
        print("Usuario eliminado")
    else:
        print("Usuario no encontrado")
    
usuarios = {}


while True:
    print("-- MENU USUARIOS --")

    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

    while True:
        try:
            op = int(input("Ingrese una opción: "))
            break
        except ValueError:
            print("Por favor, introduzca una opción valida.")
    
    if op == 1:
        ingresar_usuario()
    elif op == 2:
        buscar_usuario(usuarios)
    elif op == 3:
        eliminar_usuario(usuarios)
    elif op == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Por favor, escoja una opción valida")