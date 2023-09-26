# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data # Data that the node contains
        self.next = None # Next node that this node points to
        
a = Node(13)
b = Node(15)
a.next = b 
print(a.data)
print(b.data)
print(a.next.data)
print(a)
print(a.next)
print(b)
# print(b.next.data)
        