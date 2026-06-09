def agregar_contacto():
    contacto = input("Ingrese el contacto a registrar: ")

    if contacto == "":
        print("El contacto no puede ser vacío")
    
    if contacto in contactos:
        print("El contacto ya existe")
    
    if contacto not in contactos:
        contactos.append(contacto)
        agenda[contacto] = []
        print("Contacto agregado exitosamente")
    
    numero = input("Ingrese el número de teléfono del contacto: ")
    if len(numero) < 10:
        print("El número de teléfono debe tener al menos 10 dígitos")

    if numero == "":
        print("El número de teléfono no puede ser vacío")
    else:
        agenda[contacto].append(numero)

def buscar_contacto():
    contacto = input("Ingrese el contacto a buscar: ")
    if contacto in contactos:
        print("Contacto encontrado: ",contacto)
        print("Número de teléfono: +",agenda[contacto])
    else:
        print("Contacto no encontrado")

contactos = []
agenda = {}

while True:
    print("----------------------")
    print("--- MENU CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Buscar contactos")
    print("3. Salir")

    while True:
        try:
            op = int(input("Escoja su opción: "))
            break
        except ValueError:
            print("Escoja una opción valida")
    
    if op == 1:
        agregar_contacto()
    elif op == 2:
        buscar_contacto()
    elif op == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo")
