from funciones import cargar_matriz_notas, porcentaje_aprobados, mejor_promedio, buscar_nota

def menu():
    matriz = []  # Inicializamos la matriz vacía
    while True:
        print("\n----- MENÚ -----")
        print("1. Cargar matriz de notas")
        print("2. Mostrar porcentaje de aprobados por alumno")
        print("3. Mostrar mejor promedio")
        print("4. Buscar nota exacta")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                n = int(input("Ingrese la cantidad de alumnos: "))
                m = int(input("Ingrese la cantidad de exámenes: "))
                matriz = cargar_matriz_notas(n, m)  # Llamamos a la función que carga la matriz
            case "2":
                if matriz:
                    porcentaje_aprobados(matriz) # Llamamos a la función que calcula el porcentaje de aprobados
                else:
                    print("Debe cargar la matriz primero.")
            case "3":
                if matriz:
                    indice_mayor, mayor_promedio = mejor_promedio(matriz) # Se llama a la función que devuelve el mejor promedio
                    print(f"El alumno con mejor promedio es {indice_mayor + 1} con un promedio de {mayor_promedio}.")
                else:
                    print("Primero debe cargar las notas.")
            case "4":
                if matriz:
                    nota = int(input("Ingrese la nota a buscar: "))
                    posiciones = buscar_nota(matriz, nota) # Llamado a la función que busca la nota
                    if posiciones:
                        for fila, col in posiciones:
                            print(f"Se encontro la nota en la fila {fila+1}, columna {col+1}")
                    else:
                        print("La nota no se encontro en la matriz.")
                else:
                    print("Primero debe cargar las notas.")
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")

menu() # Llamado a la función