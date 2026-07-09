def mostrar_menu ():
    print("====MENÚ PRINCIPAL ====")
    print("1. agregar estudiantes")
    print("2. buscar estudiantes")
    print("3. eliminar estudiantes")
    print("4. actualizar estados")
    print("5. mostrar estudiantes")
    print("6. salir")
    print("========================")
def leer_opcion ():
    while True:
        try:
            opcion = int(input("Elige una opción:"))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("opcion invalida. elige entre 1 y 6.")
        except ValueError:
            print("debes ingresar un numero entero.")
def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    return True
def validar_nota(texto):
    try:
        valor = float(texto)
        return valor >= 1 and valor <= 7
    except ValueError:
        return False
def validar_edad(texto):
    try:
        edad = int(texto)
        return edad > 0
    except ValueError:
       return False
def agregar_estudiante(lista):
    nombre = input("nombre del estudiante: ")
    texto_edad = input("edad del estudiante: ")
    texto_nota = input("notas del estudiante: ")
    if not validar_nombre(nombre):
        print("el nombre no puede estar vacio.")
        return
    if not validar_nota(texto_nota):
        print("La nota debe ser un número decimal entre 1.0 y 7.0.")
        return
    if not validar_edad(texto_edad):
        print("la edad debe ser un numero entero mayor que zero.")
        return
    estudiantes = {
        "nombre": nombre.strip(),
        "nota": float(texto_nota),
        "edad": int(texto_edad),
        "aprobado": False
    }
    lista.append(estudiantes)
    print("estudiante agregado correctamente.")
def buscar_estudiante(lista, nombre):
    for indice, estudiantes in enumerate(lista):
        if estudiantes["nombre"] == nombre:
            return indice 
    return -1
def eliminar_estudiante(lista):
    nombre = input("nombre de el estudiante que quiere eliminar: ")
    posicion = buscar_estudiante(lista, nombre)
    if posicion != -1:
        del lista[posicion]
        print(f"el estudiante '{nombre}' fue eliminado correctamente.")
    else:
        print(f"el estudiante '{nombre}' no se encuentra registrado.")
def actualizar_estados(lista):
    for estudiantes in lista:
        if estudiantes["nota"] >= 4.0:
            estudiantes["aprobado"] = True
        else:
            estudiantes ["aprobado"] = False
def mostrar_estudiantes(lista):
    actualizar_estados(lista)
    print("=== LISTA DE ESTUDIANTES ===\n")
    for estudiantes in lista:
        if estudiantes["aprobado"] == True:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"
        print(f"Nombre: {estudiantes['nombre']}")
        print(f"Edad: {estudiantes['edad']}")
        print(f"Nota: {estudiantes['nota']}")
        print(f"Estado: {estado}")
        print("*"  * 40)
opcion = 0
estudiantes = []
while opcion != 6:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        agregar_estudiante(estudiantes)
    elif opcion == 2:
        nombre = input("nombre del estudiante que busca: ")
        posicion = buscar_estudiante(estudiantes, nombre)
        if posicion != -1:
            print(f"estudiante encontrado en la posicion {posicion}:")
            print(estudiantes[posicion])
        else:
            print(f"el estudiante '{nombre}' no se encuentra registrado.")
    elif opcion == 3:
        eliminar_estudiante(estudiantes)
    elif opcion == 4:
        actualizar_estados(estudiantes)
    elif opcion == 5:
        mostrar_estudiantes(estudiantes)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")

   




            

