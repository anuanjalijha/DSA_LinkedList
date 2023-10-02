class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def swapNodes(head, i, j) :
    if i == j:
        return head  # Nothing to swap if i and j are the same

    prev_i = None
    curr_i = head
    prev_j = None
    curr_j = head

    # Find nodes at positions i and j
    index = 0
    while curr_i and index != i:
        prev_i = curr_i
        curr_i = curr_i.next
        index += 1

    index = 0
    while curr_j and index != j:
        prev_j = curr_j
        curr_j = curr_j.next
        index += 1

    # If either i or j is out of bounds, or both are the same, return the original list
    if not curr_i or not curr_j:
        return head

    # Update the previous nodes to point to the new positions
    if prev_i:
        prev_i.next = curr_j
    else:
        head = curr_j

    if prev_j:
        prev_j.next = curr_i
    else:
        head = curr_i

    # Swap the next pointers of the nodes at positions i and j
    temp = curr_i.next
    curr_i.next = curr_j.next
    curr_j.next = temp

    return head
