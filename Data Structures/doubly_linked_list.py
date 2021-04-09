class Node:
    #Constructor
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s" % self.data

class DoublyLinkedList:
    #Constructor
    def __init__(self):
        self.head = None
        self.__count = 0

    #Returns true if list is empty
    def is_empty(self):
        return self.head is None

    #Returns length of list
    def __len__(self):
        return self.__count