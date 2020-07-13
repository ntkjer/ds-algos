from node import Node

class CircularLinkedList(object):

    def __init__(self, head=None, next=None, tail=None):
        self.head = head
        self.head.next = next
        self.tail = self.head
    


