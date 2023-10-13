class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseList(head):
	
	# If our current head is None, return None
	if(head == None):
		return None
		
	# If our list has just one node, return that node.
	if(head.next == None):
		return head
		
	# Declare three local node pointers as 'prev', 'temp' and 'current' and initialize them with 'None', 'head', and 'None' respectively.
	prev = None
	temp = head
	current = None
	
	# Loop to reverse the list
	while(temp != None):
		current = temp
		temp = temp.next
		
		# Reversing the direction of the list
		current.next = prev
		prev = current
		
	# Set head as prev
	head = prev
	
	# return head
	return head


def nextNumber(head):
	
	# Generate a function that will reverse the list and return the new head.
    head = reverseList (head)
    f = True
    curr = head
	
    

	
	
    while(curr != None and f == True):
        if (curr.next==None and curr.data==9):
            curr.data = 1
            temp = Node(0)
            temp.next = head
            head = temp
            curr = curr.next
        elif curr.data==9:
            curr.data = 0
            curr = curr.next
        else:
            curr.data= curr.data+1
            curr = curr.next
            f = False


