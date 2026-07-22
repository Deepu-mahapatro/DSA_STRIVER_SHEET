#LINKED LIST CYCLE (DETECT THE LOOP OF LL)

#LINKED LIST CYCLE (DETECT A LOOP )

# ---------------------------------------
# Node Definition
# ---------------------------------------
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# ---------------------------------------
# Solution Class
# ---------------------------------------
class Solution:

    def hasCycle(self, head):

        # Empty list
        if not head:
            return False

        # Initialize pointers
        slow = head
        fast = head

        # Traverse the list
        while fast and fast.next:

            # Move slow by 1 step
            slow = slow.next

            # Move fast by 2 steps
            fast = fast.next.next

            # Cycle found
            if slow == fast:
                return True

        # No cycle
        return False


# ---------------------------------------
# Create Linked List
# ---------------------------------------
def createLinkedList(arr):

    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    # Create remaining nodes
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# ---------------------------------------
# Create Cycle
# ---------------------------------------
def createCycle(head, pos):

    # No cycle
    if pos == -1:
        return head

    cycleNode = None
    current = head
    index = 0

    # Find node where cycle starts
    while current.next:

        if index == pos:
            cycleNode = current

        current = current.next
        index += 1

    # If cycle starts at last node
    if index == pos:
        cycleNode = current

    # Connect last node to cycle node
    current.next = cycleNode

    return head


# ---------------------------------------
# Driver Code
# ---------------------------------------

# Input linked list
arr = list(map(int, input("Enter linked list elements: ").split()))

# Create linked list
head = createLinkedList(arr)

# Input cycle position
print("\nCycle Position:")
print("Enter -1 for No Cycle")
print("Enter 0 for Head")
print("Enter 1 for Second Node ...")

pos = int(input("Enter position: "))

# Create cycle
head = createCycle(head, pos)

# Check cycle
obj = Solution()

if obj.hasCycle(head):
    print("\nCycle Detected")
else:
    print("\nNo Cycle")