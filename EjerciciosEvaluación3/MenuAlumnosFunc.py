import time
def agregar_alumno(alumnos):
    nombre = input("Ingrese el nombre del alumno: ").strip()

    if nombre.isdigit():
        print("Debe ingresar letras")
        return

    if nombre == "":
        print("El nombre no puede ser vacío.")
        return
    
    if nombre in alumnos:
        print("El alumno ya esta ingresado..")
        return

    while True:
        try:
            cant_notas = int(input("Ingrese la cantidad de notas: "))
            if cant_notas > 0:
                break
            else:
                print("La cantidad de notas debe ser mayor a cero")
        except ValueError:       
            print("Debe ingresar una nota valida!, vuelva a intentar..")

    nota = []

    while True:
        for i in range(cant_notas):
            print("Ingrese las notas a ingresar..")
            notas = float(input("-> "))
            nota.append(notas)
        if notas < 1 and notas > 7:
            print("Ingrese una nota valida")
            return
        else:
            print("Nota ingresada!")
            break      
    alumnos[nombre] = nota
    print("Alumno y notas agregadas correctamente!!")

def mostrar_alumnos(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados")
        return
    for nombre in alumnos:
        print(nombre, ":", alumnos[nombre])

def ver_promedios(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados, no se pueden ver los promedios")
        return
    
    for nombre in alumnos:
        promedio = sum(alumnos[nombre]) /len(alumnos[nombre])
        print(nombre,"tiene un promedio de ", round(promedio,1)) 

def mejor_alumno(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados")
        return
    
    mejorAlumno = ""
    mejor_promedio = 0
    for nombre in alumnos:
        promedio = sum(alumnos[nombre]) /len(alumnos[nombre])
        
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejorAlumno = nombre
    print("Mejor alumno: ", mejorAlumno)
    print("Promedio del Alumno: ", (mejor_promedio))

def cant_aprobados(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados, no se pueden ver los aprobados")
        return
    
    aprobados = 0
    for nombre in alumnos:
        promedio = sum(alumnos[nombre]) /len(alumnos[nombre])

        if promedio >= 4.0:
            aprobados = aprobados + 1
    print("Los alumnos aprobados son: ", aprobados)

alumnos = {}


while True:
    print("--- MENU ---")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Ver promedios")
    print("4. Mejor alumno")
    print("5. Cantidad de aprobados")
    print("6. Salir")

    while True:
        try:
            op = int(input("Seleccione su opción: "))
            break
        except ValueError:
            print("Debe ingresar un valor entre 1 o 6")

    if op == 1:
        agregar_alumno(alumnos)
    elif op == 2:
        mostrar_alumnos(alumnos)
    elif op == 3:
        ver_promedios(alumnos)
    elif op == 4:
        mejor_alumno(alumnos)
    elif op == 5:
        cant_aprobados(alumnos)
    elif op == 6:
        print("Saliendo del programa...")
        time.sleep(5)
        break
    else:
        print("Opción no valida.")