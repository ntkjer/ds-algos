from node import Node


class LinkedList(object):

    """ A singly-linked list that relies on nodes. """

    def __init__(self, head=None):
        self.head = head
        self.n = 0
        if self.head is not None: self.set_size()


    def reset_data(self, head : Node):
        self.delete_list()
        self.head = head
        self.n = self.size()

    def print_nodes(self):
        curr = self.head
        while curr is not None:
            print("node data-->", curr.data)
            curr = curr.next

    def print_links(self, head : Node):
        while head:
            print("data->", head.data)
            head = head.next

    def set_size(self):
        self.n = self.size()

    def size(self):
        n = 0
        curr = self.head
        while curr is not None:
            n += 1
            curr = curr.next
        return n

    def append(self, data):
        """ Creates a new node instance from data and appends it at the tail of the list. """
        newLast = Node(data)
        if self.head:
            current = self.head
            while (current.next):
                current = current.next
            current.next = newLast
            newLast.next = None
            self.n += 1
        else:
            self.head = newLast
            self.n += 1


    def push(self, data):
        """ Creates a new node instance from 'data' and places it at the head of the list. """
        newFirst = Node(data) 
        if self.head:
            current = self.head
            newFirst.next = current
            self.head = newFirst
            self.n += 1
        else:
            self.head = newFirst
            self.n += 1

    def delete_first(self):
        new_first = self.head.next
        self.head = new_first
   

    """Deletes the node immediately after pos."""
    def delete_after(self, pos):
        if pos > self.n: return False
        current = self.head
        for i in range(pos):
            current = current.next
            print("range: ", i)
            i += 1
        current.next = current.next.next
        self.n -= 1
        return True


    def isEmpty(self):
        return self.size() == 0


    def find(self, key):
        result, count = -1, 0
        if not self.isEmpty():
            current = self.head
            while current:
                if current.data == key: 
                    result = count
                    break
                count += 1
                current = current.next
        return result
   

    def remove(self, key):
        position = self.find(key)
        if index == -1: return
        l.delete_after(position)


    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    def recursive_reverse(self, first):
        """ Warning: uses stack size proportional to length of linked list."""
        if first == nil: return nil
        if first.next == nil:
            return first
        second = first.next
        rest = self.recursive_reverse(second)
        return rest


    def pop(self):
        if self.head:   
            result = self.head.data
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
        return result

    """
    A bunch of cool methods for interview prep.
    These exercises are from Stanford's linked list problems:
    http://cslibrary.stanford.edu/105/LinkedListProblems.pdf
    """
    def alternating_split(self):
        """ 
        Splits items in a linked list a->b->c->d to a->c and b->d.
        Returns the head node of both splits e.g. a and b 
        """
        current = self.head
        a, b = None, None
        while current:
            # Move a node to a
            newNode = current
            current = current.next
            
            newNode.next = a
            a = newNode

            if current:
                # Move a node to b
                newNode = current
                current = current.next

                newNode.next = b
                b = newNode

        return a, b



    def alternating_split_linked_lists(self):
        """
        Splits items in a linked list a->b->c->d but returns two LinkedList objects instead of head nodes.
        """
        first = LinkedList()
        second = LinkedList()

        current = self.head
        alternate = False
        while current:
            if alternate:
                first.append(current.data)
            else:
                second.append(current.data)

            current = current.next
            alternate = not alternate
        return first, second
    
     
    def split_front_back(self):
        """ 
        Splits items in a linked list into two sublists, which is a front half and back half. 
        For example: a->b->c->d to a->b and c->d.
        If the current LinkedList is of odd length, maintain a longer first half. 
        
        Returns the front and back half, and mutates the current LinkedList instance.
        """
        current = self.head
        slow = current
        fast = slow.next
        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next
        front = current
        back = slow.next
        slow.next = None
        return front, back
   
    
    def merge_sort_top_down(self):
        # Sort each half recursively
        length = self.n
        if length == 1: return
        left, right = self.split_front_back()

        left = self.merge_sort_top_down()
        right = self.merge_sort_top_down()
        
        return sorted_merge(left, right)



    """
    Mergesort but exploits naturally sorted inputs, merges them, and makes one single pass through the input list.
    Time complexity is O(n lg n) but space complexity is O(1).
    Not a stable sort, as it wont preserve equal value comparisons or orderings. 
    """    
    def natural_merge_sort(self):
        if self.n <= 1: return

        offset = 0
        while True:
            stop1 = self.find_next_stop(offset)
            offset = stop1
            stop2 = self.find_next_stop(stop1)
            self.merge_from_k(stop1, stop2)
            # Find sorted stop1
            # Find sorted stop2
            # merge two sorted 
        return

    def find_next_stop(self):
        if self.n <= 1: return
        current = self.head
        position, result = 0, None
        while current:
            next = current.next
            if next:
                if next.data > current.data:
                    result = position
                    break
            position += 1
            current = next
        return result
   

    def merge_from_k(self, stop1, stop2):
        return


    def remove_duplicates(self):
        if not self.is_sorted():
            self.merge_sort()

        current = self.head
        while current and current.next: 
            if current.data == current.next.data: 
                current.next = current.next.next
                self.n -= 1
            current = current.next


    def is_sorted(self):
        current = self.head
        while current and current.next:
            if current.data > current.next.data:
                return false
            current = current.next   
        return True


       
    def delete_list(self):
        current = self.head
        while current:
            current = current.next
            self.n -= 1
            self.head = current

	
    def merge(self, to_merge):
        """
	given two linked lists, merge their nodes together to make one list of alternate nodes from list a and b.
	a : {1 , 2, 3}
	b : {0, 4}
        t : {1, 0, 2, 4, 3}
        
        this function will mutate the source list ref 'self.head' for this class method. 
        """
	
        current = self.head
        mergable = to_merge.head

        while current and mergable:

            # Save next pointers
            head_next = current.next
            mergable_next = mergable.next
            
            # Update next values to swap refs
            mergable.next = head_next
            current.next = mergable
            
            # Advance current ponters 
            current = head_next
            mergable = mergable_next

        current = to_merge.head


    def sorted_merge(self, to_merge):
        """
	Given two sorted linked lists, this merges both of them in sorted order in O(n) time.
	a : {1 , 2, 3}
	b : {0, 4}

        t : {0, 1, 2, 3, 4}

        """
        current  = self.head
        mergable = to_merge.head
        
        dummy = tail = Node()

        while not (current is None or mergable is None):
            if current.data < mergable.data:
                tmp = current
                current = current.next
            else:
                tmp = mergable
                mergable = mergable.next

            tail.next = tmp
            tail = tail.next

        tail.next = current or mergable
        self.head = dummy.next


"""
#######################################################################
##############      General utility functions. ########################
######################################################################


"""



def merge_sort_recursive(links : LinkedList):
    """
    Sorts the list using recursive mergesort.
    This is clean, but uses stack space proportional to the input size and can introduce a stack overflow.

    Time complexity O(n lg n), space is O(n)
    """
    if links.head is None or links.n == 1: 
        return links # list of len 1 is sorted.

    left, right = links.split_front_back()
    
    left = merge_sort_recursive(LinkedList(left))
    right = merge_sort_recursive(LinkedList(right))
    
    return merge(left.head, right.head)


""" 
Takes two sorted lists and merges them in sorted order. 
O(n) running time wiht T(n) = c * 2n.
"""
def merge(headA: Node, headB: Node):
    if headA is None: return headB
    if headB is None: return headA
    
    dummy = tail = Node()

    while not (headA is None or headB is None):
        if headA.data < headB.data:
            current = headA
            headA = headA.next
        else:
            current = headB
            headB = headB.next

        tail.next = current
        tail = tail.next

    tail.next = headA or headB

    return LinkedList(dummy.next)


def build_example(*args):
    """ Builds a linked list arg1->arg2->arg3..->argn in [arg1.... argN)"""
    result = LinkedList()
    for arg in args:
        result.push(arg)
    result.set_size()
    return result

def move_node(dest: Node, source: Node):
    """
    Takes the head of the second list 'source' and puts it at the front of first list 'dest'. 
    source will point its head to the first list, inclusive of its original head item
    A : {1, 2, 3}
    B : {4, 5, 6}
    result = { 4, 1, 2, 3}
    """
    assert(source)
    toMove = source
    source = source.next
    toMove.next = dest
    dest = toMove



if __name__ == '__main__':
    a = build_example(1, 2, 8)
    b = build_example(3, 4, 5)

    #b = LinkedList()
    #b.push(3)
    #b.push(0)

    #d = move_node(a.head, b.head)
    #c = unsorted_merge(a.head, b.head)
    #a.print_links(c)
    
    #a.merge(b)

    print("doing a sorted merge")
    #a.sorted_merge(b)
    #a.print_nodes()
    

    b = build_example(-2, -3, -4, 0, -1, -1239, 12, 19, -12, 93)
    c = merge_sort_recursive(b)
    c.print_nodes()
    #c = merge_sort(b)
    #c.print_nodes()
    #b.merge_sort_top_down()
    
    
