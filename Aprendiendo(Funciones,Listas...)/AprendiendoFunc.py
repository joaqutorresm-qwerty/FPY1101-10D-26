#Sin datos en los parentesis
def sumarFijo():
    num1 = 2
    num2 = 3
    sumar = num1 + num2
    print(sumar)

#Si se colocan valores en los parentesis se llaman PARAMETROS
def sumar(num1, num2)-> int:
    """Esta función sirve para sumar números cualquiera"""
    sumar = num1 + num2
    print(sumar)

#Restar con def y RETURN
def restar(num1 , num2):
    restar = num1 - num2
    return restar

sumarFijo()
sumar(3,4)
n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))
sumar(n1 , n2)
print(restar(n1 , n2))

#def AreaCirculo():


#radio = float(input("Ingrese el radio de un circulo: "))

#Se puede importar funciones con: import funciones as fn (creadas en otro archivo)

#return es lo que nos va a devolver el resultado

print("Guardar")