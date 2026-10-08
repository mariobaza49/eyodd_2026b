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
    number = 1

    # sumando los "n" numeros
    # Ciclo while
    while number <= n:
        total_sum = total_sum + number
        number = number + 1

    return total_sum


# Variable para guardar
# EL DATA SET
dataset = []  # [(n,time,sum),(n,time,sum)]


# Generando el contenido del dataset
repetition = 1

while repetition <= 10:

    # Tomo el tiempo 1
    # Tomando el tiempo inicial
    timestamp_01 = time.time()

    # Sumo los "n" numeros
    n = repetition * 500

    # Guardo el resultado en result
    result = sum_of_n(n)

    # Tomando el tiempo final
    timestamp_02 = time.time()

    # Calculando el tiempo
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)

    # Agregar la tripleta de los datos al dataset
    dataset.append((n, elapsed_time, result))

    repetition = repetition + 1


# Imprimir el dataset
for tup in dataset:
    print(tup)


# Programa que calcula la suma de los "n" números naturales
n = 500
total_sum = 0

total_sum = sum_of_n(n)


# Impresión del tiempo de ejecución
print(f"Tiempo de ejecución: {(timestamp_02 - timestamp_01) * 1e6:.2f} µs")