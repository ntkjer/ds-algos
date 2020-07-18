from node import Node 
import random

__author__ = "Niels Kjer @ntkjer"


class Bag(object):
    """
    A list-based bag ADT.

    """
    def __init__(self):
        self.items = list()
        self.n = 0 

    def __len__(self):
        return len(self.items)

    def __contains__(self):
        return item in self.items
    
    def __iter__(self, item):
        return _BagIterator(self.items)

    def add(self, data):
        self.items.append(data) 

    def size(self):
        return self.__len__()

    def remove(self, item):
        assert item in self.items, "item must be in bag."
        result = self.items.index(item)
        return self.items.pop(result)


    def shuffle(self):
        """
        Performs a Fisher-Yates shuffle of the elements in the Bag.
        Creates unbiased permutations of the bag in O(n) time.

        """
        for i in range self.size():
            j = random.randrange(0, i)
            self.items[j], self.items[i] = self.items[i], self.items[j]

    
class _BagIterator(object):
    """
    Iterator for the Bag ADT above, which uses a list.

    In Python a foreach loop for the bag ADT will iteratore an instance of the bag class as follows:
    
    while True:
        try:
            item = iterator.next()
            ... do something with item.. 
        except StopIteration:
            break 
    
    This example iterator is influcenced by 1. 

    [1]: https://github.com/streethacker/Data-Structures-and-Algorithms-Using-Python/blob/master/linearbag.py

    """    
    def __init__(self, bag_items):
        self._bag_items =  bag_items
        self._cur_items = 0

    def __iter__(self):
        return self
    
    def next(self):
        if self._cur_items < len(self._bag_items):
            item = self._bag_items[self._cur_items]
            self._cur_items += 1
            return item
        else:
            raise StopIteration



