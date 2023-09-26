#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None




def printIthNode(head, i):
    count = 0
    
           
    while head is not None and count<i:

        head = head.next 
        count+=1

    if  head is not None:
        print(head.data)       
       