class Node(object):

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next 
    

class SequentialSearchST(object):
    
    def __init__(self, first=None):
        self.first = first

    def get(self, key):
        current = self.first
        while current:
            if current.key == key:
                return current.value
            current = current.next

    def put(self, key, value):
        current = self.first
        while current:
            if current.key == key:
                current.value = value
            current = current.next

        self.first = Node(key, value, self.first)

    def keys(self):
        keys = []
        current = self.first
        while current:
            keys.append(current.value)
            current = current.next
        return keys 

    def show(self):
        current = s.first
        while current:
            print(current.key, current.value)
            current = current.next

if __name__ == '__main__':
    s = SequentialSearchST()
    s.put(1, "hello")
    s.put(10, "goodbye")
    s.show()
