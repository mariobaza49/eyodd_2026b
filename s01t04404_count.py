# Creamos una lista de estudiantes
#O(1)
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # ?

def random_function(students):
    first = students[0] # ? accediendo a un miembro de la lista y no afecta la operacion 
    total = 0 # ?
    new_list = [] # ?

    for student in students:
        total += 1 # ?
        new_list.append(student) # ?

    print(new_list) # ?
    return total # ?

print(random_function(student_list_01))

# Calcular O(2n)+O(5) = O(2n+5) = O(n)

# student_list_01 = O(1)
# first = O(1)
# total = O(1)
# new_list = O(1)
# total += 1 = O(n)
# new_list.append(student) = O(n)
# print(new_list) = O(1)
# return total = O(1)

