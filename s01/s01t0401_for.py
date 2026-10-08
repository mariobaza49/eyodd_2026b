"""
Escribir un programa que calcule la suma de los "n" números naturales.
Por ejemplo, si n = 100, el programa calculará la suma del 1 al 100.
"""

# Importamos biblioteca
import time

# Funcion que suma los primeros "n" numeros naturales
# Creando una marca de tiempo
def sum_of_n(n):
    total_sum = 0
    # sumando los "n" numeros
    # Ciclo for
    for number in range(1, n + 1):
        total_sum = total_sum + number
    return total_sum


#Variable para guardar 
# EL DATA SET
dataset = [] #[(n,time,sum),(n,time,sum)]


#generando el contenido del dataset
for repetition in range(1,11):

    # tomo el tiempo 1 
    # Tomando el tiempo inicial
    timestamp_01 = time.time()
    #sumo los "n" numeros 
    n = repetition*500
    #guardo el resultado en result
    result = sum_of_n(n)

    # Tomando el tiempo final
    timestamp_02 = time.time()

    #Calculando el tiempo 
    elapsed_time =  round((timestamp_02 - timestamp_01) * 1e6,2)

    # Agregar la tripleta de los datos al dataset
    dataset.append( (n,elapsed_time,result) )

#imprimir el dataset
for tup in dataset:
    print(tup)

# Programa que calcula la suma de los "n" números naturales
n = 500
total_sum = 0

total_sum = sum_of_n(n)

    # 1: sum <- 0 + 1
    # sum = 1
    # 2: sum <- 1 + 2
    # sum = 3
    # 3: sum <- 3 + 3
    # ...
    # 100: sum <- suma anterior + 100




# Impresión del tiempo de ejecución
print(f"Tiempo de ejecución: {(timestamp_02 - timestamp_01) * 1e6:.2f} µs")