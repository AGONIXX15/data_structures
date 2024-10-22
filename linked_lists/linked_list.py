from typing import Optional


class Node:
    __slots__ = ['data', 'next']
    def __init__(self, data):
        self.data = data
        self.next : Optional[Node] = None


class LinkedList:
    __slots__ = ["head"]
    def __init__(self):
        self.head : Optional[Node] = None 

    def add(self,element):
        new_node = Node(element)
        if self.head == None:
            self.head = new_node
        else:
            current : Optional[Node] = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find(self,element) -> bool:
        if self.head == None:
            return False
        current  = self.head
        while current:
            if current.data == element:
                return True 
            current = current.next
        return False


    def delete(self,element):
        if self.head == None:
            return 
        else: 
            if self.head.data == element:
                self.head = self.head.next
            else: 
                current = self.head
                while current.next:
                    if current.next.data == element:
                        current.next = current.next.next
                        return
                    current = current.next

    def __str__(self) -> str:
        if self.head == None:
            return ""
        else:
            current = self.head  
            cadena = ""
            while current:
                cadena += str(current.data)
                cadena += " -> "
                current = current.next
            cadena += "None"
            return cadena


if __name__ == '__main__':
    lista_enlazada = LinkedList()
    for i in range(50):
        lista_enlazada.add(i)
    print(lista_enlazada)
    print(lista_enlazada.find(49))
    print(lista_enlazada.find(50))
    

