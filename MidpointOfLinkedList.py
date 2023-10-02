class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def midPoint(head) :
    if head is None:
        return head 

    slow = head 
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next 
        fast = fast.next.next 

    return slow    
