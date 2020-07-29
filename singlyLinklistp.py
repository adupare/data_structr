# defining a node object construct
class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        

# making some nodes
a = Node("monday")
b = Node("teusday")
c = Node("wednessday")
d = Node("thursday")
e = Node("friday")
f = Node("saturday")
# linking these nodes
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
e.nextnode = f
#defining a list construct and print function
class linklist:
    def __init__(self):
        self.head = None
    def printlist(self): # to print the list
        headpointer = self.head 
        while(headpointer is not None):
            print(headpointer.value, end = " ")
            headpointer = headpointer.nextnode
    # to add a node in start, end and in between at a specific index
    def atstart(self, value):
        newnode = Node(value)
        newnode.nextnode = self.head
        self.head = newnode

    def atEnd(self, value):
        headpointer = self.head
        newnode = Node(value)
        if(headpointer is None):
            newnode.nextnode = headpointer
            headpointer = newnode
        else:
            while(headpointer.nextnode is not None):
                    headpointer = headpointer.nextnode
                    if(headpointer.nextnode is None):
                        headpointer.nextnode = newnode
                        return 
    def sizeLinklist(self):
            headpointer = self.head
            count = 0
            while(headpointer):
                count+=1
                headpointer = headpointer.nextnode
            return count

    def insertposition(self, value, index):
        if( index < 1 or index > l.sizeLinklist):
            print(" the position is out of range")
        elif( index == 0):
                self.atstart(self, value)
        elif( index == l.sizeLinklist):
                self.atEnd(self, value)
        else:
            headpointer = self.head
            count = 0
            while(headpointer is not None):
                headpointer = 










# the main program of building link list start
l = linklist()
# declaring first node to head
l.head = a
# linking first node
l.head.nextnode = b

l.atstart("sunday")
print("your sinlgly linklist new element added at start is: ")
l.printlist()
print("\nyour singly linklist new element added at end is: ")
l.atEnd("superSunday")
l.printlist()
print("\n the size of the list is: ", l.sizeLinklist())
#l.insertposition("super wednessday", 3)
#print("\nyour list after inserting of new element at 4th position ")
#l.printlist()






