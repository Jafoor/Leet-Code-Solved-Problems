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

#appending into linked list
    def append(self, NewVal):


          NewNode = Node(NewVal)
          NewNode.next = None
          if self.head is None:
             NewNode.pre = None
             self.head = NewNode
             return
          last = self.head
          while (last.next is not None):
             last = last.next
          last.next = NewNode
          NewNode.pre = last
          return

#Print doubly linked list
    def listprint(self, node):
        while( node is not None):
            print(node.data)
            node = node.next

dl = doubly_linked_list()
dl.push(12)
dl.push(8)
dl.push(9)
dl.append(111)
dl.listprint(dl.head)
