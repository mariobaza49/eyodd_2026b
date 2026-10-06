# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # ?

def random_function(students):
    first = students[0] # ?
    total = 0 # ?
    new_list = [] # ?

    for student in students:
        total += 1 # ?
        new_list.append(student) # ?

    print(new_list) # ?
    return total # ?

print(random_function(student_list_01))

# Calcular O(?)

# student_list_01 = O(1)
# first = O(1)
# total = O(1)
# new_list = O(1)
# for = O(n)
# total += 1 = O(1)
# new_list.append(student) = O(1)
# print(new_list) = O(n)
# return total = O(1)
# print(random_function) = O(n)

# Big O = O(n)