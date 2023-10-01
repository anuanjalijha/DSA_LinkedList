class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def appendLastNToFirst(head, n):
    if not head or n <= 0:
        return head
    
    # Find the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # If N is greater than or equal to the length, no change is needed
    if n >= length:
        return head
    
    # Traverse the list again to find the (length - N)th node
    current = head
    for _ in range(length - n - 1):
        current = current.next
    
    # Update the new head and the next pointer of the last node in the original list
    new_head = current.next
    current.next = None
    # Find the last node of the new_head list
    last_node = new_head
    while last_node.next:
        last_node = last_node.next

    # Connect the last node of the new_head list to the original head
    last_node.next = head

    return new_head
