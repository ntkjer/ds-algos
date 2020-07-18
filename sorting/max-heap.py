
class MaxPQ(object):
   
    """
    Max Priority Queue that keeps track of items: [1, n]
    
    This implementation keeps the root at position 1 in order to simplify arithmetic involved in preserving the max heap property of our binary tree.
    
    Parent child relationship: (parent): pos = (left child): 2pos , (right child): 2pos+1
    

    """

    def __init__(self):
        self.items = [None]
        self.n = 0


    def size(self):
        return self.n


    def is_empty(self):
        return self.size() == 0

    def insert(self, data):
        self.n += 1
        #self.items[self.n] = data
        self.items.append(data)
        self.swim(self.n)


    def delete_max(self):
        max_item = self.items[1]
        #self.items[1], self.items[n] = self.items[n], self.items[1]
        self.exchange(1, self.n)
        self.n = self.n - 1
        self.sink(1)
        return max_item


    def swim(self, p):
        """
        This is a bottom-up reheapify method. It restores the max heap property of the 
        priority queue from right to left in the item array.
        """
        while p > 1 and self.items[p//2] < self.items[p]:
            self.exchange(p//2, p)
            p = p//2

         
    def sink(self, p):
        """
        Top-down approach to restoring the max heap property of the priority queue. 
        """
        while 2*p <= self.n:
            j = 2*p
            if j < self.n and self.items[j] < self.items[j+1]:
                j += 1
            if not self.items[p] < self.items[j]: break
            self.exchange(p, j)
            p = j


    def exchange(self, j, k):
        self.items[j], self.items[k] = self.items[k], self.items[j]
    

    def get_left_child(self, k):
        return self.items[2*k]


    def get_right_child(self, k):
        return self.items[2*k+1]


    def show_sorted(self):
        while pq.n:
            print(pq.delete_max())

    def show(self, sort=False):
        n = 1
        if not sort:
            while n < self.n:
                print(self.items[n])
                n += 1
        else:
            while self.n > 1:
                print(self.delete_max())

if __name__ == '__main__':
    pq = MaxPQ()
    pq.insert(1)
    pq.insert(2)
    pq.insert(3)
    pq.insert(9)
    pq.insert(10)
    
    pq.show(True)


