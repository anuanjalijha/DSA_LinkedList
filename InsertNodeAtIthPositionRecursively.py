class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end='')
        head=head.next
    print("None")
    return
def length(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count
def insertAtIR(head,i,data):
    if i<0:
        return head
    if i==0:
        newNode=Node(data)
        newNode.next=head
        return newNode
    if head is None:
        return None
    smallHead=insertAtIR(head.next,i-1,data)
    head.next=smallHead
    return head
def insertAtI(head,i,data):
    if i<0 or i>length(head):
        return head
    count=0
    prev=None
    curr=head
    while count<i:
        
        
        prev=curr
        curr=curr.next
        count=count+1
    newNode=Node(data)
    if prev is not None:
        prev.next=newNode
    else:
        head=newNode
    
    newNode.next=curr
    return head
def takeInput():
    inputList=[int (ele) for ele in input().split()]
    head=None
    tail=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head
head=takeInput()
printLL(head)
head=insertAtI(head,2,6)
printLL(head)
head=insertAtI(head,0,9)
printLL(head)
head=insertAtI(head,7,10)
printLL(head)