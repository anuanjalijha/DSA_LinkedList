def lengthRecursive(head):
    if head is None:
        return 0 
    count = 1 
    small_output = lengthRecursive(head.next)
    return count+small_output    
    

