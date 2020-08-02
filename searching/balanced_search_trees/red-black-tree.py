import math

class RedBlackTree(object):
    """
    A left-leaning red-black tree that maintains 1:1 correspondence between 2-3 trees.
    
    Caveats:

    We use the left-leaning convention to simplify our code. Note that this has slightly worse performance than
    the classic red-black tree implementation, as it does not have parent pointers, making insertion lg n. 

    For red-black trees with parent pointers, insert should be O(1). This implementation is overly judicious on rotations
    but that helps us out in the long-run with maintainable code.

   

    The node representations for all linked items in the tree utilize the internal class _Node. 
    The _Node internal class maintains two links, each to a left or right child, and one k:v mapped internally.

    The max tree height f(n)= c*lg n, where c is between 1.0 and 2.0 on average, with 2 being the worst case.

    This property will gurantee efficient put, get, and delete in our symbol table.

    Colored links: 
    Blank links define a normal parent child relationship (2 node), while red links represent a 3 node structure.

    3-nodes:
    The abstraction behind a 3 node (a node that has two keys and 3 links) is maintained with red links between each node.
    A 3 node means that all values to the left are less than first key, links to middle are between the two keys, and to the right are greater than the larger key.
    
    Maintaining balance:
    There are three local transformations that maintain the balanced tree:
    rotate_left, rotate_right, and flip_colors.
    
    Satisfying these properties ensures that our tree's worst-case height is at most 2 lg(n + 1). 

    
    @doctest
    >>> tree = RedBlackTree()
    >>> tree.root
    None
    >>> tree.insert(0, "apple")
    >>> tree.insert(3, "banana")
    >>> tree.insert(-2, "orange")
    """
    class _Node(object):

        def __init__(self, key=None, value=None, n=0, color=None):
            self.key = key
            self.value = value
            self.n = n
            self.color = color
            self.left, self.right = None, None


    RED = True
    BLACK = not RED


    def __init__(self, key=None, val=None, color=BLACK):
        self.root = None

        if key and val and color:
            assert(color == RED or color == BLACK)
            self.root = self._Node()
            self.root.key = key
            self.root.value = value
            self.root.color = color

    def is_red(self, x : _Node):
        if x is None: 
            return False
        else: 
            return x.color == self.RED
    
    def height(self):
        return self._height(self.root)


    def _height(self, x : _Node):
        if x is None: return -1 #-1 + 1 = 0, s.t:  1 element tree has height 0
        return 1 + max(self._height(x.left), self._height(x.right))


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
        #if h.color is self.RED:
        #    h.color = self.BLACK
        #else:
        #    h.color = self.RED
        h.color = not self.color
        h.left.color = not self.left.color
        h.right.color = not self.right.color
        return h

    
    def size(self):
        return self._size(self.root)

    def _size(self, x : _Node):
        if x is None: return 0
        return x.n
    
    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.color = self.BLACK

    def _put(self, h : _Node, key, value):
        if h is None:
            return self._Node(key, value, 1, self.RED)

        comparison = self.compare(key, h.key)
        if comparison < 0: h.left = self._put(h.left, key, value)
        elif comparison > 0: h.right = self._put(h.right, key, value)
        else: h.value = value

        #Checking our local properties s.t. our tree maintains balance.
        # If the right child is red and left is black
        #if self.is_red(h.right) and not self.is_red(h.left):
        #    h = self.rotate_left(h)
        ## Two consecutive red children on left
        #if self.is_red(h.left) and self.is_red(h.left.left):
        #    h = self.rotate_right(h)
        ## Both children cant be red, flip em if they are.
        #if self.is_red(h.left) and self.is_red(h.right):
        #    self.flip_colors(h)
        #
        h = self.balance(h)

        return h



    def balance(self, h: _Node ):
        """
        Preverses balanced property of the red black tree.
        """
        if self.is_red(h.right):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)
        h.n = self._size(h.left) + self._size(h.right) + 1
        return h
    
    def contains(self, key):
        return self.get(key) is not None
    
    def get(self, key):
        assert(key is not None)
        return self._get(self.root, key)

    def _get(self, x : _Node, key):
        if x is None: return
        if key > x.key: return self._get(x.right, key)
        elif key < x.key: return self._get(x.left, key)
        else: return x.key

    
    def delete_max(self):
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = self.RED

        self.root = self._delete_max(self.root)

        if not self.is_empty():
            self.root.color = self.BLACK
        
    def _delete_max(self, h : _Node):
        if self.is_red(h.left): 
            h = self.rotate_right(h)
        if h.right is None: 
            return None
        if not self.is_red(h.right) and not self.is_red(h.right.left): 
            h = self.move_red_right(h)
        h.right = self._delete_max(h.right)
        return self.balance(h)


    def move_red_right(self, h : _Node):
        self.flip_colors(h)
        if self.is_red(h.left.left):
            h = self.rotate_right(h)
            self.flip_colors(h)
        return h

    def delete_min(self):
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = self.RED

        self.root = self._delete_min(self.root)

        if not self.is_empty():
            self.root.color = self.BLACK

        if self.root is not None: print("root is now", self.root.key, "size: ", self.size())

    def _delete_min(self, h:_Node): 
        if h.left is None:
            return None
        
        if not self.is_red(h.left) and not self.is_red(h.left.left):
            h = self.move_red_left(h)

        h.left = self._delete_min(h.left)
        return self.balance(h)


    def delete(self, key):
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = self.RED
        self.root = self._delete(self.root, key)
        if not self.is_empty():
            self.root.color=self.color.BLACK

    def _delete(self, h: _Node, key):
        if self.compare(key, h.key) < 0:
            if not self.is_red(h.left) and not self.is_red(h.left.left):
                h = self.move_red_left(h)
            h.left = self._delete(h.left, key)
        else:
            if self.is_red(h.left):
                h = self.rotate_right(h)
            if self.compare(key, h.key) == 0 and h.right is None:
                return None
            if not self.is_red(h.right) and not self.is_red(h.right.left):
                h = self.move_red_right(h)
            if self.compare(key, h.key) == 0:
                x = self._min(right)
                h.key = x.key
                h.val = x.val
                h.right = self._delete_min(h.right)
            else:
                h.right = self._delete(h.right, key)

    def move_red_right(self, h: _Node):
        self.flip_colors(h)
        if self.is_red(h.left.right):
            h.left = self.rotate_left(h.left)
            h = self.rotate_right(h)
            self.flip_colors(h)
        return h
    

    def move_red_left(self, h: _Node):
        self.flip_colors(h)
        if self.is_red(h.right.left):
            h.right = self.rotate_right(h.right)
            h = self.rotate_left(h)
            self.flip_colors(h)
        return h

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self._size(self.root)

    def _size(self, h: _Node):
        if h is None: return 0
        return h.n

    def compare(self, a, b):
        if a > b: return 1
        elif a==b: return 0
        else: return -1

    def draw(self):
        return


if __name__ == '__main__':
    r = RedBlackTree()
    r.put(0, 1)
    print(r.root.key)
    r.put(-2, 2)
    print(r.root.left.key)
    print("size is", r.size())
    r.delete_min()
    print("size is", r.size())
    r.delete_min()

     
