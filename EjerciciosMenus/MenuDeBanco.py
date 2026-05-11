#Tarjeta de Credito
Deuda = 100000

menu = True
while menu:

    print("--- BANCO ---")
    print("1-. Pago de Tarjeta de Crédito")
    print("2-. Simulación de Compras")
    print("3-. Salir")
    print("")
    print("¡Escoja una opción!")
    op_menu = int(input(""))

    if op_menu == 1:
        print("Pago de Tarjeta de Crédito")
        pago = int(input("Ingrese monto de pago: "))
        if pago >= 0:
            if pago < Deuda:
                Deuda = Deuda - pago
                print(f"Pago exitoso, su nueva deuda es: ${Deuda}")
            else:
                print("El pago excede la deuda")

    elif op_menu == 2:
        print("Comprando...")
    elif op_menu == 3:
        print("Saliendo...")
        menu = False
    else:
        print("Opción no válida")            
