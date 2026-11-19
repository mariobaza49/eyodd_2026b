
# Creando la clase nodo
from s02 s02t0201_linked_list import Node
# Creando la clase de una lista enlazada
class SinglyLinkedList:
    #Constructor
    def __init__(self):
      self.head = None
      self.tail = None
      self.size = 0
    #Metodo de insercion de Nodo en la lista
    def append(self, data):
        #Creo el nodo
        new_node = Node(data)
        #Si hay un tail, apuntamos el tail al nuevo nodo
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        #Si no hay un tail
        else:
            self.head = new_node
            self.tail = new_node
        #Se incrementa size en 1
        self.size += 1
        # #Si la lista está vacía, apuntamos el head
        # if not self.head:
        #     self.head = new_node
        #     return
        # #Si la lista no esta vacia, recorremos la lista hasta el ultimo nodo y apuntamos el ultimo nodo al nuevo nodo
        # current_node = self.head
        # while current_node.next:
        #     current_node = current_node.next
        #Esto ya no es necesario porque tenemos el tail, pero lo dejo comentado para que se vea la logica

        #Apuntamos el último nodo al nuevo nodo
        current_node.next = new_node

#Insertando en posicion intermedia
# [A->B->C] 0 4
# [1  2  3]
# size = 3 
def append_at_location(self, data, index):
    if index < 1 or index > self.size + 1:
        raise IndexError(f"Indice {index} fuera de rango")

    # Crear un nuevo nodo
    new_node = Node(data)


    #  Insertar al inicio de la lista
    if index == 1:
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = new_node
        # Incremento el tamaño de la lista en 1
        self.size += 1
        # Creando variables de control para las inserciones intermedias
        current_node = self.head
        prev = None
        position = 1

        # Tranversal (recorrido) de la lista hasta la posición deseada
        while current is not None and position < index:
            prev = current
            current_node = current_node.next
            position += 1
        # Llegando a la posicion Estoy al final ?
        if current_node is None:
            prev.next = new_node
            self.tail = new_node
            self.size += 1
            return
        #Si llegamos a la posicion intermedia
        # TODO: Pendiente de terminar 
            raise IndexError("Position out of bounds")
        current_node = current_node.next
    new_node.next = current_node.next
    current_node.next = new_node

# Creo función principal
def main():
    #creando una instancia de una lists enlazada
    my_list = SinglyLinkedList()
    #agregar elementos de la lista
    my_list.append(30)
    my_list.append(59)
    my_list.append(80)
    my_list.append(100)
    #recorrer la lista 
    for value in my_list.head.iter:
        print(f"{value},", end="")
    print()




# Evalúo el valor de __name__
if __name__ == "__main__":
    main()
