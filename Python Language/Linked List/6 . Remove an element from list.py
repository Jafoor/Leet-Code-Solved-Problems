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

    #Insert in the begining in the linked list
    def Atbegining(self, newdata):
        NewNode = Node(newdata)

        #Now update
        NewNode.nextval = self.head
        self.head = NewNode

    #Function to remove element
    def RemoveNode(self, removekey):

        root = self.head

        if root is not None:
            if root.dataval == removekey:
                self.head = root.nextval
                root = None
                return

        while root is not None:
            if root.dataval == removekey:
                break
            pre = root
            root = root.nextval

        if root == None:
            return

        pre.nextval = root.nextval
        root = None

#declearing a LinkedList
list1 = LinkedList()

#insert in the begining
list1.Atbegining("fri")
list1.Atbegining("thr")
list1.Atbegining("wed")

list1.RemoveNode("thr")

list1.Atbegining("x")
list1.Atbegining("y")

list1.RemoveNode("y")

#Calling function to print the values
list1.listprint()
