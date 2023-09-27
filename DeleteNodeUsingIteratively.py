# Following is the Node class already written for the Linked List.
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def deleteNode(head, pos) :
    if head is None:
        return 
    if pos == 0:
        return head.next 

    count = 0
    temp = head 
    prev = head  
    while temp is not None:
        if count==pos:
            prev.next = temp.next 
            break 
        else:
            prev = temp 
            temp = temp.next 
            count+=1 

    return head                
