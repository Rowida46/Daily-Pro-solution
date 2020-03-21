



def reverseRecursively(head):
    if (head == None or  head.next == None):
         return head
    
    tmp =  reverse(head.next)
    head.next.next = head
    head.next = None
    return tmp
    
#######################################################

def reverse_iterative(head):
    ### firrst we gonna make head poisnt to NONE 
    cur = head 
    next_node = head.next
    cur.next = None 
    
    while next_node :
        ### our strategy is to save the next_node and play woth the current pointer
        tmp = next_node.next
        next_node.next = cur ### to make next_node point to the pre node
        head = cur = next_node
        next_node = tmp
    return head 
