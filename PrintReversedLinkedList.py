class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None




def printReverse(head) :
    if head is None:
        return 
    printReverse(head.next)
    print(head.data,end=" ")    
