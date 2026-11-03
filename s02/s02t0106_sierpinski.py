
from array import array as arr
from enum import Enum

# Encapsulado de los valores ANSI
# para colores en un enumerado
class AnsiColor(Enum):
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"


# Parametros de mi cuadricula
rows = 5
columns = 2 * rows - 1

# Funcion para imprimir matrix
def print_matrix(input_matrix):
    for row in input_matrix:
        print(list(row))


# Funcion para borrar pantalla
def clear_screen():
    print("\033[2J\033[H", end="")


# Creando la reticula (grid) 2D Bidimensional
matrix = []

# Construyendo la rejilla (grid)
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)

# Calculando el centro de la primera fila
center = columns // 2

# Estableciendo el centro en 1
matrix[0][center] = 1

# Se calcula el resto de la matriz
# siguiendo la logica de Sierpinski Gasket
for row in range(1, rows):
    for col in range(0, columns):

        left_upper_cell = 0
        right_upper_cell = 0

        # Si la columna donde estamos es mayor a cero
        if col > 0:
            left_upper_cell = matrix[row-1][col-1]

        # Si la columna esta un elemento antes del borde derecho
        if col < columns - 1:
            right_upper_cell = matrix[row-1][col+1]

        # Asignando valor al arreglo
        if left_upper_cell != right_upper_cell:
            matrix[row][col] = 1
        else:
            matrix[row][col] = 0


# Funcion para dibujar la matriz
def draw_matrix(input_matrix, symbol="*"):
    for row in input_matrix:
        for cell in row:
            if cell == 1:
                print(AnsiColor.CYAN.value + symbol + AnsiColor.RESET.value, end="")
            else:
                print(AnsiColor.RED.value + " ", end="")
        print()


# Mostrando la cantidad de filas y columnas
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

# Mostrando la matriz
print_matrix(matrix)

# Limpiando la pantalla antes de dibujar
clear_screen()

# Dibujando el triangulo
draw_matrix(matrix, symbol="■")
