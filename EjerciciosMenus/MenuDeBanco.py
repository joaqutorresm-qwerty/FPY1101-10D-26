#Tarjeta de Credito
Deuda = -100000

menu = True
while menu:

    print("--- BANCO ---")
    print("1-. Pago de Tarjeta de Crédito")
    print("2-. Simulación de Compras")
    print("3-. Salir")
    print("")
    print("¡Escoja una opción!")
    op_menu = int(input(""))
    
    try:
        if op_menu == 1:
            print("Si desea pagar su deuda, aprete 1, sino 2")
            op_tarjetacredito = int(input(""))
        else:
            if op_tarjetacredito == 1:
                pago = int(input("Ingrese la cantidad a pagar: "))
    except ValueError:
        print("Ingrese un número valido")
