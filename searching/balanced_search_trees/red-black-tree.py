
class REDBLACKTree(object):
    """
    A balanced search tree that maintains near perfect balance and 1:1 correspondence between 2-3 trees.
    
    The node representations for all linked items in the tree utilize the internal class _Node. 
    The _Node internal class maintains two links, each to a left or right child, and one k:v mapped internally.

    Colored links: 
    Blank links define a normal parent child relationship (2 node), while red links represent a 3 node structure.

    3-nodes:
    The abstraction behind a 3 node (a node that has two keys and 3 links) is maintained with red links between each node.
    A 3 node means that all values to the left are less than first key, links to middle are between the two keys, and to the right are greater than the larger key.
    
    Maintaining balance:
    There are three local transformations that maintain the balanced tree:
    rotate_left, rotate_right, and flip_colors.

    """
    class _Node(object):

        def __init__(self, key=None, value=None, n=0, color=Black):
            self.key = key
            self.value = value
            self.n = n
            self.color = color
            self.left, self.right = None, None


    RED = True
    BLACK = False

    def __init__(self, key, val, color):
        self.root = None

        if key and val and color:
            assert(color == RED or color == BLACK)
            self.root = self._Node()
            self.root.key = key
            self.root.value = value
            self.root.color = color

    def is_red(self, x : _Node):
        return x.color == RED


    def size(self):
        return self._size(self.root)


    def _size(self, x : _Node):
        if x is None:
            return 0
        else:
            return x.n


    def rotate_left(self, h: _Node ):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        x.n = h.n
        h.n = 1 + self._size(h.right) + self._size(h.left)
        return h


    def rotate_right(self, h: _Node):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        x.n = h.n
        h.n = 1 + self._size(h.left) + self._size(h.right)
        return h


    def flip_colors(self, h: _Node):
        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK

    
    def size(self):
        return self._size(self.root)

    def _size(self, x : _Node):
        if x is None: return 0
        return x.n
    
    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.color = BLACK

    def _put(self, h : _Node, key, value):
        if h is None:
            return _Node(key, value, 1, RED)

        comparison = self.compare(key, h.key)
        if comparison < 0: h.left = self._put(h.left, key, value)
        elif comparison > 0: h.right = self._put(h.right, key, value)
        else: h.value = value

        #Checking our local properties s.t. our tree maintains balance.
        # If the right child is red and left is black
        if self.is_red(h.right) and not self.is_red(h.left):
            h = self.rotate_left(h)
        # Two consecutive red children on left
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        # Both children cant be red, flip em if they are.
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)
        
        #Update the number of subtrees rooted at this node
        h.n = self._size(h.left) + self._size(h.right) + 1
        return h


    def compare(self, a, b):
        if a > b: return 1
        elif a==b: return 0
        else: return -1





