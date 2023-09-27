def deleteNodeRec(head, pos) :
    # Base case: If the list is empty, return None.
    if head is None:
        return None

    # Special case: If the position is 0, delete the head node.
    if pos == 0:
        head = head.next
        # del head  # Delete the old head
        return head

    # Recursively call the function on the remaining list.
    small_head = deleteNodeRec(head.next,pos-1)
    head.next = small_head
    return head