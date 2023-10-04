class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def kReverse(head, k) :
    if head == None:
        return None
    if k == 0:
        return head

    current = head
    next = None
    prev = None
    count = 0
  
        # Reverse first k nodes of the linked list
    while(current is not None and count < k):
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1
  
        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current. And make rest of the list as
        # next of first node
    if next is not None:
        head.next = kReverse(next, k)
  
        # prev is new head of the input list
    return prev
  
