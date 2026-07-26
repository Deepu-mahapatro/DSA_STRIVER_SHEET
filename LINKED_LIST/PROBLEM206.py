#REVERSE A SINGLE LINKED LIST

# ------------------------------------
# Node of Singly Linked List
# ------------------------------------
class Node:

    def __init__(self, data):
        self.data = data      # Store node data
        self.next = None      # Pointer to next node


# ------------------------------------
# Insert node at the end
# ------------------------------------
def insert(head, data):

    # Create a new node
    new_node = Node(data)

    # If list is empty
    if head is None:
        return new_node

    # Traverse to the last node
    current = head
    while current.next:
        current = current.next

    # Connect last node to new node
    current.next = new_node

    return head


# ------------------------------------
# Display the Linked List
# ------------------------------------
def display(head):

    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# ------------------------------------
# Reverse the Linked List
# ------------------------------------
def reverse_list(head):

    prev = None            # Previous node
    current = head         # Current node

    # Traverse the entire list
    while current:

        next_node = current.next     # Save next node

        current.next = prev          # Reverse the link

        prev = current               # Move prev forward

        current = next_node          # Move current forward

    # prev becomes the new head
    return prev


# ------------------------------------
# Main Program
# ------------------------------------

head = None

# Create the linked list
head = insert(head, 10)
head = insert(head, 20)
head = insert(head, 30)
head = insert(head, 40)
head = insert(head, 50)

print("Original Linked List:")
display(head)

# Reverse the list
head = reverse_list(head)

print("\nReversed Linked List:")
display(head)