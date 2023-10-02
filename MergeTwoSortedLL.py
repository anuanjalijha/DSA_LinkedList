class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def mergeTwoSortedLinkedLists(head1, head2):
    if head1 is None and head2 is None:
        return None
    elif head1 is None and head2 is not None:
        return head2 

    elif head1 is not  None and head2 is  None:
        return head1 
            
    
    head3 = Node(0)
    tmp1 = head1 
    tmp2 = head2 
    tmp3 = head3
    while tmp1 is not None and tmp2 is not None: 
        if tmp1.data<=tmp2.data:
            tmp3.next = tmp1 
            tmp1 = tmp1.next 

        else:
            tmp3.next = tmp2 
            tmp2 = tmp2.next 
        tmp3 = tmp3.next 

    if tmp1 is not None:
        tmp3.next = tmp1

    if tmp2 is not None:
        tmp3.next = tmp2
    

    head3 = head3.next 
    return head3 
