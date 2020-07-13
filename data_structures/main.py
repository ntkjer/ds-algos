from linkedlist import LinkedList
from queue import Queue
from bag import Bag

l = LinkedList()
l.push(1)
l.print_nodes()


q = Queue()
q.enqueue(3)
q.enqueue(4)
q.show()

b = Bag()
b.add("hello")
b.add("i")
b.add(1)
print(b.items)
