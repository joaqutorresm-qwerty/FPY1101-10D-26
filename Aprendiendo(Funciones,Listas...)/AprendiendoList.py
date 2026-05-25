frutas = ["manzana" , "pera"]

#se imprime todos los nombres
print(frutas)

#para decidir solo uno
print(frutas[0])

#para mostrar varias cosas
for i in range (2):
    print(frutas[i])

#otra forma de hacerlo...
for i in frutas:
    print(i)

#mas ejemplos para agregar elementos...
frutas.append("naranja") #agrega un elemento al final de la lista

print(frutas)

frutas.append("manzana verde") # agregar elemento al final

print(frutas)

#insertar datos
frutas.insert(2, "pomelo")

print(frutas)
 
#remover elementos
frutas.remove("manzana")

print(frutas)

#dar vuelta la lista
frutas.reverse()
print(frutas)

#ordenar la lista
frutas.sort()
print(frutas)