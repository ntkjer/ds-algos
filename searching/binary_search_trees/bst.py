import collections



class BST(object):

    class _Node(object):

        def __init__(self, key, value, n):
            self.key = key
            self.value = value 
            self.n = n #Number of subtrees rooted at this node.
            self.left, self.right = None, None

        def __str__(self):
            return "{K}\nv={V} N={N}".format(
                    K=self.key, V=self.value, N=self.n)

    def __init__(self):
        self.root = None
        self.visited = None #Keeps track of the most recently visited node

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, k, v):
        self.put(k,v)

    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self._size(self.root)

    def _size(self, curr_node):
        if curr_node is None: return 0
        else: return curr_node.n

    def put(self, key, value):
        if key is None: 
            raise Exception("Can't put a value with no key!'")
        if value is None:
            self.delete(key)
            return
        self.root = self._put(self.root, key, value)

    def _put(self, curr_node, key, value):
        self.visited = curr_node
        if curr_node is None:
           curr_node = self._Node(key, value, 1)
           return curr_node
        
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
        self.visited = curr_node
        if curr_node is None: return None
        if key > curr_node.key:
            return self._get(curr_node.right, key)
        elif key < curr_node.key:
            return self._get(curr_node.left, key)
        else:
            return curr_node.value
    
    def max(self):
        if self.is_empty(): raise Exception("Tree is empty!")
        x = self._max(self.root)
        return x.key

    def _max(self, curr_node):
        if curr_node.right is None: return curr_node 
        return self._max(curr_node.right)

    def min(self):
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
        if curr_node.key == key: return curr_node
        elif key < curr_node.key: return self._floor(curr_node.left, key)

        x = self._floor(curr_node.right, key)
        if x is not None: 
            return x
        else: 
            return curr_node 

    def ceiling(self, key):
        x = self._ceiling(self.root, key)
        if x is None: raise Exception("No such element in the tree.")
        return x.key

    def _ceiling(self, curr_node, key):
        if curr_node is None: return None
        if curr_node.key == key: return curr_node
        elif key > curr_node.key: return self._ceiling(curr_node.right, key)

        x = self._ceiling(curr_node.left, key)
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
        """
        prints using in-order traversal.
        """
        self._print(self.root)

    def _print(self, curr_node):
        if curr_node is None: return
        self._print(curr_node.left)
        print(curr_node.key)
        self._print(curr_node.right)

    def keys(self):
        q = queue.Queue()
        self._keys(self.root, q, self.min(), self.max())
        return q

    def _keys(self, curr_node, queue, lo, hi):
        if curr_node is None:
            return
        if lo < curr_node.key:
            self._keys(curr_node.left, queue, lo, hi)
        if lo <= curr_node.key and hi >= curr_node.key:
            queue.put(curr_node.key)
        if hi > curr_node.key:
            self._keys(curr_node.right, queue, lo, hi)


    def has_right_child(self, curr_node):
        return curr_node.right is not None


    def has_left_child(self, curr_node):
        return curr_node.left is not None

    def height(self):
        return self._height(self.root)


    def _height(self, curr_node):
        if not curr_node: return 0
        if not self.has_right_child(curr_node) and not self.has_left_child(curr_node):
            return curr_node.n
        if self.has_right_child(curr_node) and self.has_left_child(curr_node):
            return 1 + self._height(curr_node.right) + self._height(curr_node.left)
        if self.has_right_child(curr_node):
            return 1 + self._height(curr_node.right)
        if self.has_left_child(curr_node):
            return 1 + self._height(curr_node.left)

    
    def level_order(self):
        """ 
        Returns the keys of the BST in level-order, starting from the root and ending with the furtherst (right-most) leaf. 
        """
        keys = collections.deque()
        q = collections.deque()
        q.append(self.root)
        while q:
            curr_node = q.popleft()
            if curr_node is None: break
            keys.append(curr_node.key)
            q.append(curr_node.left)
            q.append(curr_node.right)
        return keys

"""
Programming exercises.

"""     
def build_perfectly_balanced_bst(keys=[]):
    """
    builds a perfectly balanced BST with O(lg n) lookup time for searching keys by inserting from the median and inserting outwars from the first and second half.
    Utilizes n auxilary space proportional to the number of keys. We copy the keys into two separate halves. 

    Problem 3.2.25 in Sedgewick's Algorithms vol.4 
    """
    n = len(keys)

    assert(keys), "keys cannot be empty"
    assert(sorted(keys)), "keys are not sorted"
    assert(n%2!=0), "number of keys need to be odd"
    
    median_pos = n // 2 
    median = keys[median_pos]
    first_half = keys[:median_pos]
    second_half = keys[median_pos+1:]

    b = BST()
    b.put(keys[median_pos], "")
    i = 0
    j = len(first_half)-1
    print("items are ", first_half, second_half)
    while j >= 0:
        b.put(second_half[i], "")
        b.put(first_half[j],"")
        i += 1
        j -= 1
    return b


if __name__ == '__main__':
    b = BST()
    b.put(3, "boo")
    b.put(2, "foo")
    b.put(-2, "yo")
    b.put(4, "yep")
    b.print()
    print(b.height()) 
    print(b.get(3))
    print("printing visited..")
    print(b.visited.key)

    print("testing get..")
    print(b[4])
    b[-100] = "poopie"

    print("arranging in level order..")
    print(b.level_order())
    print("building build_perfectly_balanced_bst")
    c = build_perfectly_balanced_bst([-2, 5, 6, 7, 9])
    c.print()
    print("last visit..")
    print(c.visited)
    print("visiting..")
    c.get(5)
    print(c.visited)


