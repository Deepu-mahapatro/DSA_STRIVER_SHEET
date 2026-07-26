#REVERSE THE DOUBLY LINKED LIST

# -----------------------------
# Node of Doubly Linked List
# -----------------------------
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# -----------------------------------
# Reverse a Doubly Linked List
# -----------------------------------
def reverse_dll(head):

    # If the list is empty, return None.
    if head is None:
        return None

    # Start traversal from the head.
    current = head

    # This variable will store the last processed node.
    # After reversing, this node becomes the new head.
    new_head = None

    # Traverse until all nodes are processed.
    while current is not None:

        # ---------------------------------------
        # Step 1:
        # Save the previous pointer temporarily.
        # ---------------------------------------
        temp = current.prev

        # ---------------------------------------
        # Step 2:
        # Reverse the previous pointer.
        # prev now points to the original next.
        # ---------------------------------------
        current.prev = current.next

        # ---------------------------------------
        # Step 3:
        # Reverse the next pointer.
        # next now points to the original previous.
        # ---------------------------------------
        current.next = temp

        # ---------------------------------------
        # Step 4:
        # Current node is now the latest processed node.
        # Save it because the last processed node
        # will become the new head.
        # ---------------------------------------
        new_head = current

        # ---------------------------------------
        # Step 5:
        # Move to the next node.
        #
        # IMPORTANT:
        # After swapping,
        # current.prev actually points
        # to the ORIGINAL next node.
        # ---------------------------------------
        current = current.prev

    # Return the new head.
    return new_head