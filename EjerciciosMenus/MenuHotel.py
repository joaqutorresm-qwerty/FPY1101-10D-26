menu = True

while True:
    try:
        habitaciones = int(input("Ingrese el número de habitaciones a registrar: "))
        if habitaciones < 0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        else:
            break
    except Exception:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

contador_ejecut = 0
contador_estand = 0

for i in range (habitaciones):
    while True:
        numero_habitacion = input(f"Ingrese el número de habitación {i + 1}: ")
        if (len(numero_habitacion) < 6 or " " in numero_habitacion):
            print("El número de habitación debe tener al menos 6 caracteres")
            print("El número de habitación no debe tener espacios")
        else:
            break
    while True:
        try:
            precio_habitacion = int(input(f"Ingrese el precio de la habitación {i + 1}: "))
            if precio_habitacion > 0:
                break
            else:
                print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna")
        except Exception:
            print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna")
    if (precio_habitacion < 90000):
        contador_estand += 1
    else:
        contador_ejecut += 1

print(f"¡El hotel cuenta con {contador_ejecut} Suites Ejecutivas y {contador_estand} Habitaciones Estándar! ¡Check-in disponible!")