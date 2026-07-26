#REMOVE THE DUPLICATES FROM SORTED DOUBLY LINKED LIST

def removeDuplicates(head):

    # If the list is empty, return it
    if head is None:
        return None

    current = head    # Start from the head

    # Traverse until the last node
    while current and current.next:

        # Check if the current and next nodes have the same value
        if current.data == current.next.data:

            duplicate = current.next      # Node to be removed

            current.next = duplicate.next # Skip the duplicate node

            # Fix the previous pointer of the next node
            if duplicate.next:
                duplicate.next.prev = current

        else:
            # Move to the next node if no duplicate
            current = current.next

    # Return the updated head
    return head