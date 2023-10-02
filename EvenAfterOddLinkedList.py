class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(head) :
    if head is None or head.next is None:
        return head 

    oh = None
    ot = None
    eh = None
    et = None 
    temp = head 
    while temp is not None:
        val = temp.data
        if val%2!=0:
            if oh is None:
                oh = temp  
                ot  = oh   
            else:
                ot.next  = temp 
                ot = ot.next 
        else:
            if eh is None:
                eh = temp  
                et  = eh  
            else:
                et.next = temp
                et = et.next 
        temp = temp .next 
    


          
    if oh and eh:
        ot.next = eh
        et.next = None 
        head = oh
    return head 
