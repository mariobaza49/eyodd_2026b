# Importando el modulo arrays 
from array import array as arr

#Creando un arreglo 
array_01 = arr('i',[3,8,5,1,6])
# i:entero con signo
# I:entero sin signo 
# f: úmero decimal
# d: numero decimal doble
# u : Caracteres unicode
my_array = arr.array('i',[10,22,300,3,7,40,55,80,700,644,34])
# Iterando automaticamente
for data in array_01:
    print(data,end =",")
print(num)
#Acceso individual a los elementos 
print(my_array[0]) # primer elemento
print(my_array[1]) # segundo elemento 
print(my_array[1]) #tercer elemento

#tamaño de arreglo 
#Lenght
#print(len(my_array))

#iterscione por indices
for i in range(len(my_array)):
    print(f"Elemento {i+1}: {my_array[i]}")