# Importando el modulo arrays
from array import array as arr

#Creando un arreglo
array_01 = arr('i',[3,8,5,1,6])
# i:entero con signo
# I:entero sin signo
# f: número decimal
# d: numero decimal doble
# u : Caracteres unicode

my_array = arr('i',[10,22,300,3,7,40,55,80,200,644,34])

# Iterando automaticamente
# for data in array_01:
#     print(data,end = ",")

#Acceso individual a los elementos
# print(my_array[0]) # primer elemento
# print(my_array[1]) # segundo elemento
# print(my_array[2]) #tercer elemento

#tamaño de arreglo
#Lenght
#print(len(my_array))

#itersecion por indices
#for i in range(len(my_array)):
#    if my_array [i] % 2 == 0:
#        print(f"Elemento {i+1}: {my_array[i]}")

#Busqueda de un elemento
print(f"Localizando 200: {my_array.index(200)}")