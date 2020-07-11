from node import Node

class Queue(object):

    """Node-based queue where we keep reference to the first item of the queue."""
    def __init__(self,first=None,last=None,n=0):
        self.head = first
        self.tail = last
        self.n = n


    def copy(self):
        result = []
        current = self.head
        while current:
            result.append(current)
            current = current.next
        return result


    def peek(self):
        return self.head.data


    def enqueue(self, data):
        new_tail = Node(data)
        if self.n < 1:
            self.head = new_tail
            self.tail = self.head
        elif self.n == 1:
            self.head.next = new_tail
            self.tail = new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        self.n += 1


    def dequeue(self):
        old_head = self.head
        self.head = self.head.next
        self.n -= 1
        return old_head


    def size(self):
        return self.n


    def isEmpty(self):
        return self.size() == 0


    def show(self):
        current = self.head
        print("Items in the Queue:")
        while current:
            print(current.data)
            current = current.next
        


if __name__ == '__main__':
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("carrot")
    q.show()
    print(q.size())


