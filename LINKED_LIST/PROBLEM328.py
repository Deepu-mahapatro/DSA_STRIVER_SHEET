#ODD EVEN LIST IN LINKED LIST

# -----------------------------
# Node class
# -----------------------------
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# -----------------------------
# Solution class
# -----------------------------
class Solution:

    def oddEvenList(self, head):

        # If the list is empty or has only one node
        if not head or not head.next:
            return head

        # First node (Odd Position)
        odd = head

        # Second node (Even Position)
        even = head.next

        # Save the first even node
        evenHead = even

        # Process until there are no more even nodes
        while even and even.next:

            # Connect current odd node to next odd node
            odd.next = even.next

            # Move odd pointer
            odd = odd.next

            # Connect current even node to next even node
            even.next = odd.next

            # Move even pointer
            even = even.next

        # Attach even list after odd list
        odd.next = evenHead

        # Return the modified list
        return head


# -----------------------------
# Create Linked List
# -----------------------------
def createLinkedList(arr):

    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# -----------------------------
# Print Linked List
# -----------------------------
def printLinkedList(head):

    current = head

    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next

    print()


# -----------------------------
# Main Program
# -----------------------------

# Number of nodes
n = int(input("Enter number of nodes: "))

# Node values
arr = list(map(int, input("Enter node values: ").split()))

# Create linked list
head = createLinkedList(arr)

print("\nOriginal Linked List:")
printLinkedList(head)

# Solve
solution = Solution()
head = solution.oddEvenList(head)

print("\nOdd-Even Linked List:")
printLinkedList(head)