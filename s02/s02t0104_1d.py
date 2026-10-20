#importar funcion Array como arr

from array import array as arr

#Importar una funcion de otro
#Archivo
from s02t0102_1d import print_array

my_array = arr('i',[2,10,15,20,10])

print("--- Antes de la eliminacion ---")
print_array(my_array)

#Eliminacion
try:
    my_array.remove(30)
except :
    print("El numero no esta en el array")

print("--- Despues de la eliminacion ---")
print_array(my_array)

numero = 10

if numero in my_array:
    while numero in my_array:
        my_array.remove(numero)
else:
    print("El numero no esta en el array")

print("--- Despues de la eliminacion ---")
print_array(my_array)