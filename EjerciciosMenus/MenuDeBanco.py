#Tarjeta de Credito
deuda = 100000
total = 0
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
            if pago < deuda:
                deuda = deuda - pago
                print(f"Pago exitoso, su nueva deuda es: ${deuda}")
            else:
                print("El pago excede la deuda")

    elif op_menu == 2:
        print("Comprando...")
        articulo = int(input("Ingrese la cantidad que desea comprar: "))
        for i in range (articulo):
            compra = int(input("Coloque el precio del producto: "))
            if compra >= 0:
                total += compra
            else:
                print("Ingrese un número valido")          
        print("Se ha realizado tu compra")
        print(f"el total es de: {total}")

    elif op_menu == 3:
        print("Saliendo...")
        menu = False
    else:
        print("Opción no válida")            
