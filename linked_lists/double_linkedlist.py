from typing import Optional


class Node:
    __slots__ = ["data", "next", "back"]

    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None
        self.back: Optional[Node] = None

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.data == other.data
        return NotImplemented

    def __repr__(self):
        return f"Node(data = {self.data},next = {self.next},back = {self.back})"


class DoubleLinkedList:
    __slots__ = ["head", "tail", "back", "next"]

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.back: Optional[Node] = None
        self.next: Optional[Node] = None

    def add_head(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.back = new_node
        self.head = new_node

    def add_tail(self, element):
        new_node = Node(element)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
            return
        self.tail.next = new_node
        new_node.back = self.tail
        self.tail = new_node

    def delete(self, element):
        if self.head is None:
            return
        if self.head.data == element and self.head.next is None:
            self.head = None
            self.tail = None
            return
        if self.head.next is None:
            pass
            # haz algo
            return
        if self.head.data == element and self.head.next.back is not None:
            new_head = self.head.next
            if new_head is not None:
                new_head.back = None
                self.head = new_head
                return
        if self.tail is None:
            return
        if self.tail.data == element:
            new_tail: Optional[Node] = self.tail.back
            if new_tail is not None:
                new_tail.next = None
                self.tail = new_tail
            return
        current = self.head
        while current.next:
            if current.next.data == element:
                node = current.next.next
                if node is not None:
                    node.back = current
                    current.next = node
                    return

    def find(self, element) -> bool:
        if self.head is None:
            return False
        current = self.head
        while current:
            if current.data == element:
                return True
            current = current.next
        return False

    def show_head(self):
        if self.head is None:
            print()
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def show_tail(self):
        if self.tail is None:
            print()
        else:
            current = self.tail
            while current:
                print(current.data, end=" -> ")
                current = current.back
            print("None")


if __name__ == '__main__':
    lista = DoubleLinkedList()
    for i in range(20):
        lista.add_tail(i)
    lista.delete(19)
    lista.show_head()
    lista.show_tail()
