#DELETE THE HEAD OF THE DOUBLY LINKED LIST

# -----------------------------
# Node of Doubly Linked List
# -----------------------------
class Node:

    def __init__(self, data):
        self.data = data      # Stores the value
        self.prev = None      # Points to previous node
        self.next = None      # Points to next node


# ----------------------------------------
# Delete the head node
# ----------------------------------------
def delete_head(head):

    # Step 1: If the list is empty,
    # there is nothing to delete.
    if head is None:
        return None

    # Step 2: If there is only one node,
    # deleting it makes the list empty.
    if head.next is None:
        return None

    # Step 3: Move the head to the second node.
    head = head.next

    # Step 4: Since this is now the first node,
    # its previous pointer must be NULL.
    head.prev = None

    # Step 5: Return the new head.
    return head