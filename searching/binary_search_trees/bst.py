
class BST(object):

    class _Node(object):

        def __init__(self, key, value, n):
            self.key = key
            self.value = value 
            self.n = n
            self.left, self.right = None, None

        def __str__(self):
            return "{K}\nv={V} N={N}".format(
                    K=self.key, V=self.value, N=self.n)

    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, curr_node):
        if curr_node is None: return 0
        else: return curr_node.n

    def is_empty(self):
        return self.size() == 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, k, v):
        self.put(k,v)


    def put(self, key, value):
        if key is None: 
            raise Exception("Can't put a value with no key!'")
        if value is None:
            self.delete(key)
            return
        self.root = self._put(self.root, key, value)
   

    def _put(self, curr_node, key, value):
        if curr_node is None:
            return self._Node(key, value, 1)

        if key > curr_node.key:
            curr_node.right = self._put(curr_node.right, key, value)
        elif key < curr_node.key:
            curr_node.left = self._put(curr_node.left, key, value)
        else:
            curr_node.value = value

        curr_node.n = 1 + self._size(curr_node.left) + self._size(curr_node.right)
        return curr_node

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, curr_node, key):
        if curr_node is None: return None
        if key > curr_node.key:
            return self._get(curr_node.right, key)
        elif key < curr_node.key:
            return self._get(curr_node.left, key)
        else:
            return curr_node.value

    def min(self):
        if self.is_empty(): raise Exception("Tree is empty!")
        x = self._min(self.root)
        return x.key
     
    def _min(self, curr_node):
        if curr_node.left is None: return curr_node
        return self._min(curr_node.left)


    def floor(self, key):
        x = self._floor(self.root, key)
        if x is None: raise Exception("No such element in the tree")
        return x.key


    def _floor(self, curr_node, key):
        if curr_node is None: return None
        if curr_node.key == key: return x
        elif key < curr_node.key: return self._floor(curr_node.left, key)

        x = self._floor(curr_node.right, key)
        if x is not None: 
            return x
        else: 
            return curr_node 

    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, curr_node, key):
        if curr_node is None: 
            return 0

        if key < curr_node.key:
            return self._rank(curr_node.left, key)
        elif key > curr_node.key:
            return 1 + self._size(curr_node.left) + self._rank(curr_node.right, key)
        else:
            return self._size(curr_node.left)

    
    def select(self, k):
        if k < 0 or k >= self.size(): raise Exception("Illegal key used as argument.")
        x = self._select(self.root, k)
        return x.key

    def _select(self, curr_node, k):
        if curr_node is None: return None
        t = self._size(curr_node.left)
        if t > k: return self._select(curr_node.left, k)
        elif t < k: return self._select(curr_node.right, k)
        else: return curr_node

    def delete_min(self):
        if self.is_empty(): raise Exception("Tree is empty, no such element to be deleted.")
        root = self._delete_min(self.root)

    def _delete_min(self, curr_node):
        if curr_node.left is None: return curr_node.right
        curr_node.left = self._delete_min(self, curr_node.left)
        curr_node.n = self._size(curr_node.left) + self._size(curr_node.right) + 1 
        return curr_node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, curr_node, key):
        if curr_node is None: return None
        if key < curr_node.key:
            curr_node.left = self._delete(curr_node.left, key)
        elif key > curr_node.key:
            curr_node.right = self._delete(curr_node.right, key)
        else:
            if curr_node.right is None: 
                return curr_node.left
            if curr_node.left is none: 
                return curr_node.right

            t = curr_node
            curr_node = self._min(t.right) #Point the current node to its successor
            curr_node.right = self._delete_min(t.right) 
            curr_node.left = t.left

        curr_node.n = self._size(curr_node.left) + self._size(curr_node.right) + 1
        return curr_node
    
    def print(self):
        self._print(self.root)

    def _print(self, curr_node):
        if curr_node is None: return
        self._print(curr_node.left)
        print(curr_node.key)
        self._print(curr_node.right)

if __name__ == '__main__':
    b = BST()
    b.put(3, "boo")
    b.put(2, "foo")
    b.put(-2, "yo")
    b.put(4, "yep")
    b.print()
