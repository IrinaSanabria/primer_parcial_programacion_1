def cargar_matriz_notas(n, m): # Función para cargar una matriz de n alumnos por m exámenes
    matriz = []  # Una lista vacía para guardar la matriz
    for i in range(n): # Recorremos cada fila (alumno)
        fila = []  # Lista vacía donde se almacenan las notas de un alumno
        for j in range(m):# Recorremos cada columna (examen)
            nota_valida = False  # Bandera para repetir la carga si no es válida
            while not nota_valida: 
                nota = input(f"Ingrese la nota del alumno {i+1}, examen {j+1}: ")
                if nota.isdigit():  # Verifica que es un número
                    nota = int(nota)
                    if 1 <= nota <= 10: # Validamos que sea un número entero entre 1 y 10
                        nota_valida = True
                        fila.append(nota) # Agregamos la nota validada
                    else:
                        print("La nota debe estar entre 1 y 10.")
                else:
                    print("Debe ingresar un número entero.")
        matriz.append(fila)  # Agregamos la fila completa a la matriz
    return matriz

def porcentaje_aprobados(matriz): # Función para calcular el porcentaje de aprobados
    for i in range(len(matriz)):
        total_examenes = 0
        aprobados = 0
        for j in range(len(matriz[i])):
            nota = matriz[i][j]
            total_examenes += 1
            if nota >= 6:
                aprobados += 1
        porcentaje = (aprobados * 100) / total_examenes # Se calcula el porcentaje
        print(f"Alumno {i+1}: {porcentaje}% de exámenes aprobados.")

def mejor_promedio(matriz): # Función que calcula el mejor promedio entre los alumnos
    indice_mayor = -1
    mayor_promedio = 0.0
    for i in range(len(matriz)):
        total = 0
        suma = 0
        for j in range(len(matriz[i])):
            suma += matriz[i][j]  # Acumulamos las notas
            total += 1
        promedio = suma / total  # El promedio de alumno
        if indice_mayor == -1 or promedio > mayor_promedio:
            mayor_promedio = promedio  # Se guarda el mejor promedio
            indice_mayor = i  # También guardo el indice del alumno
    return indice_mayor, mayor_promedio # Retorna el indice del alumno y su promedio (el mejor promedio)

def buscar_nota(matriz, buscada): # Función para buscar la posición de alguna nota
    posiciones = []  # Lista que guarda las posiciones
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == buscada:
                posiciones.append((i, j))
    return posiciones # Devuelve la posicion de la nota
