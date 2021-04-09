class Node:
    """ 
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """

    data = None                         # Holds on to data we are storing
    next_node = None                    # Points to next node in list

    # Constructor
    def __init__(self, data):
        self.data = data
        
    # Function that returns value stored in node 
    def __repr__(self):
        return "<Node data: %s>" % self.data 

class LinkedList:
    """ 
    Singly Linked List
    """

    #Constructor
    def __init__(self):
        self.head = None
        

    #Checks if list is empty
    def is_empty(self):
        return self.head == None 

    #Returns the number of nodes in the list. Takes O(n) time 
    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    #Adds a new node containing data at the head of the list. Takes O(1)
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head                  #Points to previous head in order to keep the link 
        self.head = new_node

    #Search for the first node containing data that matches the key. Returns the node or 'None' if not found. Takes O(n)
    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    #Inserts a new node containing data at index position. Takes O(1) but finding node at insertion point takes O(n). Overall runtime = O(n)
    def insert(self, data, index):

        if index >= self.__count:
            raise IndexError('Index out of range')
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

        self.__count += 1

    #Removes node containing data that matches the key. Returns the node or 'None' if key doesn't exist. Takes O(n)
    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current


    #Returns a string representation of the list. Takes O(n)
    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return ' -> '.join(nodes)


l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
print(l)

m = LinkedList()
m.add(10)
m.add(22)
m.add(213)
m.add(2)
searched = m.search(22)
print(m)
print(searched)
