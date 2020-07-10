class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
    
    def set_data(self, data):
        self.data = data

class Queue:

    """Node-based queue where we keep reference to the first item of the queue."""
    def __init__(self,first=None,N=None):
        self.first = first
        self.N = N

    def copy(self):
        result = []
        current = self.first
        while first:
            result.append(current)
        return result

    def enqueue(self, data):
        return data

    def dequeue(self):
        return

    def size(self):
        return self.N

    def isEmpty(self):
        return self.size() == 0




