from array import array as arr 


# Impresion de una tabla
def print_table(input_table):
    # Imprimiendo cada elemento 
    for row in input_table:
        for column in row:
            print(column, end=",")
        print("\b ")


table = [
    arr('i',[1,2,3]),
    arr('i',[4,5,6]),
    arr('i',[7,8,9]),
]

print_table(table)

#insercion
row = 1
column = 2
value = 99

# Insertar en la fila 1 columna 2 el valor 99
table[row].insert(column, value)

# imprimiendo mensaje 
print("--- Despues de la insercion del elemento ---")
print_table(table) #Dont repeat yourself o DRY

# Insertando 
new_row = arr('i',[100,200,300])
pos = 1
table.insert(pos, new_row)

# Imprimiendo mensaje
print("--- Despues de la insercion de fila ---")
print_table(table) #DRY

#Eliminacion de elementos
del table[2]
 
# Imprimiendo mensaje
print("--- Despues de la eliminacion de fila 2 ---")
print_table(table) #DRY