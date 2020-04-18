class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.pre = None

class doubly_linked_list():

    def __init__(self):
        self.head = None

#Adding data elements
    def push(self, newval):
        NewNode = Node(newval)
        NewNode.next = self.head
        if self.head is not None:
            self.head.pre = NewNode
        self.head = NewNode
#Print doubly linked list
    def listprint(self, node):
        while( node is not None):
            print(node.data)
            node = node.next

dl = doubly_linked_list()
dl.push(12)
dl.push(8)
dl.push(9)
dl.listprint(dl.head)
