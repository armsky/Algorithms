"""
A linked list is a dynamic data structure. The number of nodes in a list is not fixed and can grow and shrink on demand.
It is useful when dealling with an unknown number of objects 
"""

class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class SingleList:
    head = None
    tail = None

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
        self.tail = node

    def remove(self, data):
        if self.head:
            current = head
            previous = None
            while current is not None:
                if current.data == data:
                    # Incase this is the head
                    if previous is not None:
                        previous.next = current.next
                    else:
                        self.head = current.next
                previous = current
                current = current.next

class DoublyList:
    head = None
    tail = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            tail = node

    def remove(self, data):
        if self.head:
            current = self.head
            while current is not None:
                if current.data == data:
                    # Current is not head
                    if current.prev is not None:
                        current.prev.next = current.next
                        # Current is not tail
                        if current.next is not None:
                            current.next.prev = current.prev
                    else:
                        self.head = current.next
                        current.next.prev = None
                current = current.next
