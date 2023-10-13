''' 
    Following is the node structure

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

'''

def deleteAlternateNodes(head):
    if(head == None) :
        return None
    
    # The variable cur stores the current node
    p = head
    c = head.next
    while c is not None and c.next is not None:
        p.next = c.next 
        p = c.next 
        c = p.next
    p.next = None    


    
    
