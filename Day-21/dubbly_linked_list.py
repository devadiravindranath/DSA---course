class node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class doublylinkedlist:
    def __init__(self):
        self.head = None
    
    #inserting operation
    #inserting begining

    def inser_begin(self,data):
        new_node = node(data)

        if self.head:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    def insert_end(self,data):
        new_node = node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp
