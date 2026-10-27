from array import array as arr

# Paramentros de mi cuadricula 
rows = 3
columns = 2 * rows - 1

#Funcion para imprimir matrix
def print_matrix(input_matrix):
  for row in matrix:
   print(list(row))   
   
#Creando la reticula(grid) 2D Bidimensional 
matrix = []

#Construyendo la rejilla(grid)
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)  

#Validando la construccionn del grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

#Calculando el centro de la primera fila
center = columns // 2 # cuando ponemos doble // es para que sea divicion entera 

#Estableciendo el centro en 1
matrix[0][center] = 1 #fila es la primera y la columna es la que da pie 

print_matrix(matrix)

#Se calcula el resto de la matrix siguiendo la logica de Sierpinski Gasket
for row in range(1, rows):
  for col in range(0, columns):
   # print(f"[{row}_{col}]",end=" ")
   # print() # nos dio las cordenadas de la cantidad de datos que tenemos y esas iteraciones son de cada elemento uno por uno
   
   left_upper_cell = 0
   right_upper_cell = 0

   #Si la columna donde estamos es mayor a cero
   if col > 0:
     left_upper_cell = matrix[row-1][col-1]

   #Si la columna esta un elemento antes del borde derecho 
   if col < columns - 1:
     right_upper_cell = matrix[row-1][col+1] 

   #Guardando el arreglo
   if left_upper_cell != right_upper_cell:
     matrix[row][col] = 1
   else:
     matrix[row][col] = 0

print()
print_matrix(matrix)