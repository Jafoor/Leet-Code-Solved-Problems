class Node:
    def __init__ (self, dataval):
        self.dataval = dataval #stores data
        self.nextval = None #initialize next as null


class LinkedList:

    #function to initialize the LinkedList object
    def __init__(self):
        self.head = None

list1 = LinkedList()

list1.head = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")

#Link first node to second Node
list1.head.nextval = e2

#link second node to third element
e2.nextval = e3
