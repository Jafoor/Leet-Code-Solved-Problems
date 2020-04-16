class Node:
    def __init__ (self, dataval):
        self.dataval = dataval #stores data
        self.nextval = None #initialize next as null


class LinkedList:

    #function to initialize the LinkedList object
    def __init__(self):
        self.head = None


    #printing the list
    def listprint(self):
        printval = self.head

        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    #insert at the end
    def Atend(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        next = self.head
        while(next.nextval):
            next = next.nextval
        next.nextval = NewNode

#declearing a LinkedList
list1 = LinkedList()

#putting a value in head
list1.head = Node("Mon")

#creating nodes
e2 = Node("Tue")
e3 = Node("Wed")

#Link first node to second Node
list1.head.nextval = e2

#link second node to third element
e2.nextval = e3

#Insert at end
list1.Atend("Fri")
#Calling function to print the values
list1.listprint()
