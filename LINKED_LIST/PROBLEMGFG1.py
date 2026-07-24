#FOND THE LENGTH OF THE LOOP IN LINKED LIST

# -------------------------------------------------------
# Definition for singly-linked list.
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# -------------------------------------------------------

class Solution:

    def countNodesInLoop(self, head):

        # -----------------------------------------
        # If the list is empty,
        # there cannot be a loop.
        # -----------------------------------------
        if not head:
            return 0

        # -----------------------------------------
        # Initialize slow and fast pointers.
        # Both start from the head.
        # -----------------------------------------
        slow = head
        fast = head

        # -----------------------------------------
        # Floyd's Cycle Detection
        # -----------------------------------------
        while fast and fast.next:

            # Move slow by one step
            slow = slow.next

            # Move fast by two steps
            fast = fast.next.next

            # -------------------------------------
            # If both pointers meet,
            # a loop exists.
            # -------------------------------------
            if slow == fast:

                # -----------------------------
                # Start counting the loop size.
                #
                # Begin from the meeting node.
                # -----------------------------
                count = 1

                # Move one step ahead
                current = slow.next

                # ---------------------------------
                # Keep moving until we reach the
                # same meeting node again.
                # ---------------------------------
                while current != slow:

                    count += 1

                    current = current.next

                # Return the loop length
                return count

        # -----------------------------------------
        # If slow and fast never met,
        # no loop exists.
        # -----------------------------------------
        return 0