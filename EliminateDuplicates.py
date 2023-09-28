class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None




def removeDuplicates(head) :

    if head is None:
        return head

    t1 = head
    t2 = t1.next

    while t2 is not None:
        if t1.data == t2.data:
            t2 = t2.next
        else:
            t1.next = t2
            t1 = t2
            t2 = t2.next

    t1.next = None  # Set the next of the last unique node to None
    return head
 
