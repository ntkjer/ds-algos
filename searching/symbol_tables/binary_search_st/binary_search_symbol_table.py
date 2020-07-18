__author__ = "niels kjer"

class BinarySearchST(object):
    
    def __init__(self, k=[], v=[], n=0):
        self.keys = k
        self.values = v
        self.n = n

    def is_empty(self):
        return self.n == 0
    
    def size(self):
        return self.n

    def get(self, key):
        if self.is_empty(): return

        pos = self.rank(key)
        if pos < self.n and s.keys[pos] == key:
            return self.values[pos]
    
    def put(self, key, value):
        # check if key exists, if it does, update the value
        # put k,v in n pos 
        pos = self.rank(key)
        if pos == 0:
            self.values[pos] = value
            return 

        if pos == self.size():
            self.keys.append(pos)    
            self.values.append(value)
            self.n += 1
            return

        self.keys[pos], self.values[pos] = key, value
        self.n += 1

    def rank(self, key):
        """ 
        This method uses binary search as a dive and conquer approach 
        to finding the position of a key in a given array. 
        
        Time complexity for looking up an item is O(lg n). 

        If the key exists, it returns 0.
        If the key is greater than all the other keys, it returns the number of keys.
        """
        lo = 0
        hi = self.size() - 1
        while lo <= hi:
            mid = hi // 2 
            if key > self.values[mid]:
                lo = mid+1
            elif key < self.values[mid]:
                hi = mid-1
            elif key == self.values[mid]:
                return mid
        return lo
            
