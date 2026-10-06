"""
Notas: 
1: Identifico el tamaño de la entrada "n"
el tamaño de la entrada es el numero de estudiantes
2: ES ver cuanto crece el numero de operaciones en el algoritmo conforme
crece el tamaño de la entrada.
Agrego las BigO identificadas 
Teniendo en cuanta la Cota superior asintotica
O(n) + O(4) = O(n+4) = O(n)
"""
#Creando una lista de estudiantes 
student_list_01 = ['Jordan','Pipen','Curry','Shack']
student_list_02 = ['Mike','Saul','Walter','Jessy']

#Verificando la presencia de un estudiante
def check_student(input_student, student_list):
    for student in student_list:
        if input_student == student:
            print("Estudiante encontrando ")
            return student
    #Si no encuentro al estudiante 
    print("Estudiante no encontrado")
    return None 
#Probando el algoritmpo
check_student("Walter", student_list_02)