from typing import Optional


class Node: 
    __slots__ = ['data', 'next']
    def __init__(self, data):
        self.data = data
        self.next : Optional[Node] = None

class Circular_LinkedList:
    __slots__ = ["head"]
    def __init__(self):
        self.head : Optional[Node] = None
    
    def add(self,element):
        new_node = Node(element)
        if self.head == None:
            self.head = new_node 
            new_node.next = self.head
            return
        else:
            current : Optional[Node] = self.head 
            while current.next != self.head:
                current = current.next
            current.next = new_node 
            new_node.next = self.head

    def find(self,element):
        if self.head == None:
            return 
        current : Optional[Node] = self.head 
        while True:
            if current.data == element:
                return True
            current = current.next
            if current == self.head:
                return False

    def delete(self,element):
        if self.head == None:
            return 
        else:
            # si la cabeza es el nodo a eliminar
            current : Optional[Node] = self.head 
            if current.data == element:
                # si la cabeza es el unico elemento
                if current.next == self.head:
                    self.head = None
                    return
                else:
                    # si la cabeza no es el unico elemento
                    while current.next != self.head:
                        current = current.next 
                    current.next = self.head.next
                    self.head = self.head.next
            else:
                previous = None
                while True: 
                    previous = current
                    current = current.next
                    if current.data == element:
                        previous.next = current.next
                        return
                    if current == self.head:
                        break

        

                    
                    
    def show(self):
        if self.head == None:
            return 
        else:
            current = self.head
            while current.next != self.head:
                print(current.data, end=" -> ")
                current = current.next
            print(current.next.data)

if __name__ == '__main__':
    lista = Circular_LinkedList()
    for i in range(20):
        lista.add(i)
    lista.delete(0)
    print(lista.find(5))
    print(lista.find(100))
    lista.show()
            
    
