
class MinPQ(object):
    
    def __init__(self, keys=[]):
        self.items = keys
        self.n = len(keys)-1


    def size(self):
        return self.n


    def is_empty(self):
        return self.size() == 0


    def insert(self, data):
        self.n += 1
        self.items.append(data)
        self.swim(self.n)


    def delete_min(self):
        min_item = self.items[1]
        self.exchange(1, self.n)
        self.n = self.n - 1
        self.sink(1)
        return min_item


    def swim(self, p):
        while p > 1 and self.items[p//2] > self.items[p]:
            self.exchange(p//2, p)
            p = p//2

         
    def sink(self, p):
        while 2*p <= self.n:
            j = 2*p
            if j < self.n and self.items[j] > self.items[j+1]:
                j += 1
            if not self.items[p] > self.items[j]: break
            self.exchange(p, j)
            p = j


    def exchange(self, j, k):
        self.items[j], self.items[k] = self.items[k], self.items[j]

    def show_sorted(self):
        while pq.n:
            print(pq.delete_min())

    def show(self, sort=False):
        n = 1
        if not sort:
            while n < self.n:
                print(self.items[n])
                n += 1
        else:
            while self.n > 1:
                print(self.delete_min())

if __name__ == '__main__':
    pq = MinPQ([-1, 82, 1010, 8888, 8123, -2123, 4500])
    pq.show(True)
    
    print("deleting items..")
    print("init size: ", pq.size())
    while pq.size() > 0:
        print(pq.delete_min())


