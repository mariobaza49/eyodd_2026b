#importar funcion Array como arr

from array import array as arr

#Importar una funncion de otro
#Archivo
from s02t0102_1d import print_array

my_array = arr('i',[2,10,15,20])

print("--- Antes de la insercion ---")
print_array(my_array)

#Insercion 
my_array.insert(1,90)
print("--- Despues de la insercion ---")
print_array(my_array)

my_array.insert(1,90)
print("--- Despues del append ---")
my_array.append(1000)
print_array(my_array)
#ES como el append pero con insert el len es por que tiene que ser la longitud del arreglo
my_array.insert(1,90)
print("--- Simular un append con un insert ---")
my_array.insert(len(my_array),90000)
print_array(my_array)