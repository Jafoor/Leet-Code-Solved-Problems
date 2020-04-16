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

    #Function to search an element
    def SearchElement(self, value):
        root = self.head
        found = False
        while root is not None:
            if root.dataval == value:
                found = True
                break
            root = root.nextval

        if found == True:
            print("Item found")
        else:
            print("Data is not in the list")


#declearing a LinkedList
list1 = LinkedList()

#insert in the begining
list1.Atbegining("fri")
list1.Atbegining("thr")
list1.Atbegining("wed")

list1.SearchElement("thr")
list1.SearchElement("x")
