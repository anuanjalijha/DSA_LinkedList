def reverse(head):
    if head is None:
        return head
    curr = head
    prev = None    
    while curr is not None:
        next = curr.next
        curr.next = prev 
        prev = curr
        curr = next 

    head = prev 
    return head         
