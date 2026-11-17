
# Creando la clase nodo
from s02t0201_linked_list import Node
# Creando la clase de una lista enlazada
class SinglyLinkedList:
    #Constructor
    def __init__(self):
      self.head = None
    #Metodo de insercion de Nodo en la lista
    def append(self, data):
        #Creo el nodo
        new_node = Node(data)
        #Si la lista está vacía, apuntamos el head
        if not self.head:
            self.head = new_node
            return
        #Si la lista no esta vacia, recorremos la lista hasta el ultimo nodo y apuntamos el ultimo nodo al nuevo nodo
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        #Apuntamos el último nodo al nuevo nodo
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
    for value in my_list:
        print(value)




# Evalúo el valor de __name__
if __name__ == "__main__":
    main()
