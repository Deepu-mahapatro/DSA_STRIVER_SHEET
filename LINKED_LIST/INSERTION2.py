#INSERT NODE BEFORE THE DOUBLY LINKED LIST

# -----------------------------
# Node of Doubly Linked List
# -----------------------------
class Node:

    def __init__(self, data):
        self.data = data      # Stores the value
        self.prev = None      # Points to previous node
        self.next = None      # Points to next node


# ----------------------------------------
# Insert a node before the head
# ----------------------------------------
def insert_before_head(head, value):

    # Step 1: Create a new node
    new_node = Node(value)

    # Step 2: If the list is empty,
    # the new node itself becomes the head.
    if head is None:
        return new_node

    # Step 3: Connect the new node to the current head.
    new_node.next = head

    # Step 4: Make the current head point back to the new node.
    head.prev = new_node

    # Step 5: Update the head reference to the new node.
    head = new_node

    # Step 6: Return the new head.
    return head