class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def getMid(currNode):
    slow = currNode
    fast = currNode 
    while fast.next is not None and fast.next.next  is not None:
        slow=slow.next
        fast = fast.next.next 
    return slow 

def reverseList(currNode):
    prev = None 
    next = None 
    while currNode is not None:
        next = currNode.next 
        currNode.next  = prev
        prev = currNode
        currNode = next 

    return prev    

def isPalindrome(head) :
    if head is None or head.next is None:
        return True
    

    mid = getMid(head) 
    revHead = reverseList(mid)  

    while revHead is not None and head is not None:
        if revHead.data !=head.data:
            return False 
        revHead = revHead.next
        head = head.next 

    return True         
 