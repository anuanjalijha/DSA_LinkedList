class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def skipMdeleteN(head, M, N) :
    if M is 0:
        return 
    t1 = head
    t2 = t1

    while t1:
        count1 = 1
        count2 = 1

        while count1 < M and t1:
            t1 = t1.next
            count1 += 1

        if not t1:
            return head  # Reached the end of the list

        t2 = t1.next

        while count2 <= N and t2:
            t2 = t2.next
            count2 += 1

        # Delete N nodes
        t1.next = t2
        t1 = t2

    return head
