
#Generators 

#Los generadores son funciones que  pueden pausar su ejecucion

#Cuando se invoca una funcion generadora devuelve un objetivo generador (aka iterador)

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4 
    yield 5
    yield 6
    yield 7
    yield 8 
    yield 9
    yield 10
    yield 11
    yield 12

# Se invoca funcion generadora 
my_iterator = my_generator()

#Se itera manualmente sobre el generador 
# print(next(my_iterator)) # Imprime 1
# print(next(my_iterator)) # Imprime 2
# print(next(my_iterator)) # Imprime 3
# print(next(my_iterator)) # Imprime 4

# Los iteraodres se pueden iterar con un for
for value in my_iterator:
    print(value)