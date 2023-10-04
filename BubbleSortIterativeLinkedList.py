class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length(head):
    temp = head
    len = 0 
    while temp is not None:
        len+=1 
        temp = temp.next 
    return len    

def bubbleSort(head) :
    if head is None or head.next is None:
        return head

    i = 0 
    len = length(head)
    while i<len-1:
        prev = None
        curr = head
        next = curr.next
        while curr.next is not None:
            if curr.data>curr.next.data:
                if prev==None:
                    curr.next = next.next
                    next.next = curr
                    prev = next
                    head = prev  
                else:

                    next = curr.next
                    curr.next = next.next
                    prev.next = next
                    next.next = curr
                    prev = next 
            else:
                prev = curr
                curr = curr.next
        i+=1 
    return head            
