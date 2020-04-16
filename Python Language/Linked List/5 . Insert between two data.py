class Node:
    def __init__ (self, dataval):
        self.dataval = dataval #stores data
        self.nextval = None #initialize next as null


class LinkedList:

    #function to initialize the LinkedList object
    def __init__(self):
        self.head = None

    #Fuction to add value between two node
    def InBetween(self, before, newdata):
        if before is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = before.nextval
        before.nextval = NewNode

    #printing the list
    def listprint(self):
        printval = self.head

        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval



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

#Insert Between

list1.InBetween(list1.head,"Fri")

#Calling function to print the values
list1.listprint()
