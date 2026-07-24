#SEGREGATE ODD EVEN NODES LINKED LIST 

# -----------------------------------------
# Definition for singly-linked list.
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# -----------------------------------------

class Solution:

    def divide(self, head):

        # -----------------------------------------
        # If the list is empty or has only one node,
        # it is already segregated.
        # -----------------------------------------
        if not head or not head.next:
            return head

        # -----------------------------------------
        # Create two dummy nodes.
        #
        # One for even numbers.
        # One for odd numbers.
        # -----------------------------------------
        evenDummy = Node(-1)
        oddDummy = Node(-1)

        # -----------------------------------------
        # Tail pointers.
        #
        # They always point to the last node
        # in each list.
        # -----------------------------------------
        even = evenDummy
        odd = oddDummy

        # Start traversing the original list.
        current = head

        # -----------------------------------------
        # Traverse every node.
        # -----------------------------------------
        while current:

            # Save next node before breaking links.
            nextNode = current.next

            # Disconnect the current node
            # from the original list.
            current.next = None

            # -------------------------------------
            # If current node value is even,
            # add it to the Even List.
            # -------------------------------------
            if current.data % 2 == 0:

                even.next = current
                even = even.next

            # -------------------------------------
            # Otherwise,
            # add it to the Odd List.
            # -------------------------------------
            else:

                odd.next = current
                odd = odd.next

            # Move to the next node
            current = nextNode

        # -----------------------------------------
        # Connect Even List with Odd List.
        # -----------------------------------------
        even.next = oddDummy.next

        # -----------------------------------------
        # Return the head of the Even List.
        #
        # If there are no even nodes,
        # return the Odd List.
        # -----------------------------------------
        if evenDummy.next:
            return evenDummy.next

        return oddDummy.next
