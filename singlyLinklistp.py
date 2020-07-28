# defining a node object construct
class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None

# making some nodes
a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)
f = Node(60)
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
        current = self.head
        while(current is not None):
            print(current.value, end = " ")
            current = current.nextnode
    # to add a node in start, end and in between at a specific index
    def atstart(self, value):
        newnode = Node(value)
        newnode.nextnode = self.head
        self.head = newnode

# the main program of building link list start
l = linklist()
# declaring first node to head
l.head = a
# linking first node
l.head.nextnode = b

l.atstart(5)
print("your sinlgly linklist")
l.printlist()






