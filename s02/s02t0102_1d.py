#Importando el modulo Array de la biblioteca array y renombrando como arr
from array import array as arr

def print_array(input):
    print("[",end="")
    for element in input:
        print(element,end=',')
    print("\b]")

my_array = arr('i',[2,10,15,20])
print_array(my_array)
#Buscar elemento 15
number_to_search = 100
counter = 0
print(f"Se busca {number_to_search} en el arreglo.")
for intenger in my_array:

if intenger == number_to_search:
    print("Numero encontrado")
# Sirve para termninar el ciclo
break
#incrementa el contador 
couter+=1
if counter == len(my_array):
    print("😡")
