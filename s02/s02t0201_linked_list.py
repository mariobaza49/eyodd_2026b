# Creando la clase Nodo
class Node:
  # Constructor 
  def __init__(self, data=None):
    self.data = data
    self.next = None

  def inter(self):
    current = self
    while current: 
      value = current.data
      current = current.next
      yield value


#creando una funcion principal
def main():
  #codigo de prueba 

  # Testear nuestra clase nodo 
  node_01 = Node("eggs")
  node_02 = Node("ham")
  node_03 = Node("bacon")

  #print("🔗NODES SIN ENLAZAR🔗")
  #print (f"Node 01: D:{node_01.data} - N:{node_01.next}")
  #print (f"Node 02: D:{node_02.data} - N:{node_02.next}")
  #print (f"Node 03: D:{node_03.data} - N:{node_03.next}")

  # Enlazando los nodos 
  node_01.next = node_02
  node_02.next = node_03

  #print("🔗NODE ENLAZADOSS🔗")
  #print (f"Node 01: D:{node_01.data} - N:{node_01.next}")
  #print (f"Node 02: D:{node_02.data} - N:{node_02.next}")
  #print (f"Node 03: D:{node_03.data} - N:{node_03.next}")

  #list traversaol(recorrido de la lista)
  for node_value in node_01.inter():
    print(node_value)


#invicando a main 
if __name__ == "__main__":
 main()