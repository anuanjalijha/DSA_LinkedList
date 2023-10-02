class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def findNodeRec(head, n) :
    if head is None:
        return -1 
    if head.data==n:
        return 0 
    small_output = findNodeRec(head.next,n)
    if small_output==-1:
        return -1 
    else:
        return small_output+1             
