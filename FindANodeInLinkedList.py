class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    count = 0 
    index = -1 
    while head is not None:
        if head.data==n:
            index = count
            break 
        else:
            head=head.next 
            count+=1 
    return index       