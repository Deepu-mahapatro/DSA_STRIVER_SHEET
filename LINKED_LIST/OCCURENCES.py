#DELETE ALL OCCURRENCES OF A KEY OF DOUBLY LINKED LIST

def deleteAllOccurrences(head, key):

    current = head          # Start from head

    # Traverse the DLL
    while current:

        next_node = current.next      # Save next node

        # If current node contains the key
        if current.data == key:

            # If current is not the head
            if current.prev:
                current.prev.next = current.next
            else:
                head = current.next   # Update head

            # If current is not the last node
            if current.next:
                current.next.prev = current.prev

        # Move to the next node
        current = next_node

    return head