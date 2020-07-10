
class Node:
    """ A node class to be used as an underlying abstraction for ADTs. """ 
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.nextNode
    
    def set_next(self, newNext):
        self.nextNode = newNext

