class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def mergeSort(head) :
    if head is None or head.next is None:
        return head

    # Find the middle of the linked list
    middle = find_middle(head)

    # Split the linked list into two halves
    left_head = head
    right_head = middle.next
    middle.next = None

    # Recursively sort the two halves
    left_sorted = mergeSort(left_head)
    right_sorted = mergeSort(right_head)

    # Merge the sorted halves
    return mergeTwoSortedLinkedLists(left_sorted, right_sorted)

def find_middle(head):
    slow = head
    fast = head
    prev = None

    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    return prev

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
