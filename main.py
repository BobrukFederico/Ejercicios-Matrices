from Funciones import *

matriz = [[1,3,6], [5,4,9]]

resultado = agregar_columna(matriz, [74,6])
print(resultado)

imprimir_tamaño_matriz(resultado)

init = inicializar_matriz()

print(init)

nombres = ["Juan", "Ricardo", "Nahuel", "Eugenia", "Jimena"]
edades = [23, 35, 34, 40, 24]
generos = ["Hombre", "Hombre", "Hombre", "Mujer", "Mujer"]


media_etaria = calcular_media_etaria(nombres, edades, generos)

print(media_etaria)

n = [10, 20, 30, 40]

media = calcular_media(n)

print(media)

in_hor = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]


ingresos_horarios = calcular_ingresos_horarios(in_hor)

print(ingresos_horarios)