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
def reverse3(head):
    if head is None or head.next is None:
        return head
    smallHead=reverse3(head.next)
    tail=head.next
    tail.next=head
    head.next=None
    return smallHead

head=takeInput()
printLL(head)
head=reverse3(head)
printLL(head)