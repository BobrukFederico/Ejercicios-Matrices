def agregar_columna(matriz, columna):

    if type(matriz) and type(columna) != list:
        return None

    if len(matriz) != len(columna):
        print("Error. Tienen que ser de igual tamaño")
        return None
    
    matriz_nueva = []

    for i in range(len(matriz)):
        fila = matriz[i] + [columna[i]]
        matriz_nueva += [fila]

    return matriz_nueva


def imprimir_tamaño_matriz(matriz):

    if type(matriz) != list:
        return None
    filas = len(matriz)

    columnas = len(matriz[0])

    print(f"El tamaño de las filas es: {filas} y de columnas: {columnas}")


def inicializar_matriz():
    matriz = [[0,0,0,0], [0,1,2,3], [0,2,4,6], [0, 3, 6, 9]]

    for i in range(4):
        fila = []
        for j in range(4):
            valor = i * j
            fila += [valor]
        matriz += [fila]
    return matriz


def calcular_media_etaria(nombres,edades,generos):
    hombres_edades = []
    nombres_hombre = []
    media_etaria_h = 0

    mujeres_edades = []
    nombres_mujeres = []
    media_etaria_m = 0

    for i in range(len(generos)):
        if generos[i] == "Hombre":
            print("Hay hombres")
            hombres_edades += [edades[i]]
            nombres_hombre += [nombres[i]]
            media_etaria_h += edades[i]
        else:
            mujeres_edades += [edades[i]]
            nombres_mujeres += [nombres[i]]
            media_etaria_m += edades[i]
    media_etaria_m = media_etaria_m / len(mujeres_edades)
    media_etaria_h = media_etaria_h / len(hombres_edades)
    
    print(f"Media etaria para mujeres: {media_etaria_m}")
    print(f"Media etaria para hombres: {media_etaria_h}")

    return media_etaria_m, media_etaria_h


def calcular_media(lista: list) -> float:
    media = 0

    for i in range(len(lista)):
        if type(lista[i]) != int:
            return None
        
        media += lista[i]

    return media / len(lista)


def calcular_ingresos_horarios(lista:list) -> float:
    n = len(lista)
    veinte_porciento = int(n * 0.2)
    contador = 1
    promedio = 0

    while contador <= veinte_porciento:
        minimo = lista[1]
        for i in range(len(lista)):
            if lista[i] <= minimo:
                minimo = lista[i]


        promedio += minimo
        lista.remove(minimo)
        contador += 1
    print(promedio)
    return promedio / veinte_porciento


def multiplicar_matrices(matriz1, matriz2):
    
    #Matriz 1
    filas1 = 0
    columnas1 = 0

    #Matriz 2
    filas2 = 0
    columnas2 = 0

    for i in range(matriz1):
        filas1 += 1
        for j in range(matriz1[i]):
            columnas1 += 1

    for i in range(matriz2):
        filas2 += 1
        for j in range(matriz2[i]):
            columnas2 += 1


    # if columnas1 == filas2:
        