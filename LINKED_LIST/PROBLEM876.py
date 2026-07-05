#MIDDLE ELEMENT OF A LINKED LIST


from typing import List, Optional
# Definition of a Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # Store the value
        self.next = next    # Store the address of the next node


class Solution:

    def middleNode(self, head):

        # Step 1: Both pointers start from the first node
        slow = head
        fast = head

        # Step 2: Continue until fast reaches the end
        while fast and fast.next:

            # Slow moves one node
            slow = slow.next

            # Fast moves two nodes
            fast = fast.next.next

        # Step 3: Slow is now at the middle node
        return slow


# ---------------- DRIVER CODE ----------------

# Take input from the user
nums = list(map(int, input("Enter the values: ").split()))

# Create the first node
head = ListNode(nums[0])

# Current pointer is used to build the linked list
current = head

# Create remaining nodes
for value in nums[1:]:

    # Create a new node and connect it
    current.next = ListNode(value)

    # Move current to the newly created node
    current = current.next


# Create object of Solution class
obj = Solution()

# Find the middle node
middle = obj.middleNode(head)

# Print only the middle element
print("THE MIDDLE ELEMENT IS:",middle.val)