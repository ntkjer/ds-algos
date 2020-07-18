
class Node(object):

    def __init__(self, key=None, value=None,n=0):
        self.key = key
        self.value = value
        self.size = n #Number of subtrees rooted at this node
        self.left = None
        self.right = None


class BST(object):

    def __init__(self, key=None, value=None):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size


    def __iter__(self):
        return self.root.__iter__()


    def get(self, key):
        return self._get(self.root, key)

    def _get(self, x, key):
        if x is None:
            return None
        if key > x.key:
            return self._get(x.right, key)
        elif key < x.key:
            return self._get(x.left, key)
        else:
            return x.value


    def put(self, key, value):
        if self.root:
            self._put(self.root, key, value)
        else:
            self.root = Node(key, value)
        self.size += 1


    def _put(self, x:Node, key, value):
        """

        """
        if x is None: 
            return Node(key, value, 1) #We're referencing a non-existent node, so lets create it. 
        if key > x.key:
            return self._put(x.right, key, value)
        elif key < x.key:
            return self._put(x.left, key, value)
        else:
            x.value = value

        x.size = self._size(x.left) + self._size(x.right) + 1


    def size(self):
        return self._size(self.root)


    def _size(self, x:Node):
        if x is None: 
            return 0
        else:
            return x.n



if __name__ == '__main__':
    b = BST()
    b.put(0, "hello")
    b.put(1, "yo")
    b.put(2, "ahhh")
    print(b.get(0))
    print(b.get(1))
    print(b.get(2))


