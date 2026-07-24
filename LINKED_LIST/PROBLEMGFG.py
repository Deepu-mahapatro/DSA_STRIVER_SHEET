#SORT 0'S 1'S 2'S IN A ORDER 

# -----------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# -----------------------------------------

class Solution:

    def segregate(self, head):

        # -----------------------------------------
        # If the list is empty or has only one node,
        # it is already sorted.
        # -----------------------------------------
        if not head or not head.next:
            return head

        # -----------------------------------------
        # Create three dummy nodes.
        #
        # They are temporary starting points for
        # three separate linked lists.
        # -----------------------------------------
        zeroDummy = ListNode(-1)
        oneDummy = ListNode(-1)
        twoDummy = ListNode(-1)

        # -----------------------------------------
        # Tail pointers.
        #
        # These always point to the last node
        # of each list.
        # -----------------------------------------
        zero = zeroDummy
        one = oneDummy
        two = twoDummy

        # Start traversing the original list
        current = head

        # -----------------------------------------
        # Divide nodes into three lists.
        # -----------------------------------------
        while current:

            # Store next node before breaking links
            nextNode = current.next

            # Disconnect current node
            current.next = None

            # ----------------------------
            # Node value is 0
            # ----------------------------
            if current.val == 0:

                zero.next = current
                zero = zero.next

            # ----------------------------
            # Node value is 1
            # ----------------------------
            elif current.val == 1:

                one.next = current
                one = one.next

            # ----------------------------
            # Node value is 2
            # ----------------------------
            else:

                two.next = current
                two = two.next

            # Move to next node
            current = nextNode

        # -----------------------------------------
        # Connect the three lists
        # -----------------------------------------

        # Connect Zero list to One list.
        # If One list is empty,
        # connect directly to Two list.
        if oneDummy.next:
            zero.next = oneDummy.next
        else:
            zero.next = twoDummy.next

        # Connect One list to Two list
        one.next = twoDummy.next

        # -----------------------------------------
        # Return the new head.
        #
        # If Zero list exists,
        # it is the answer.
        #
        # Otherwise check One list.
        #
        # Otherwise Two list.
        # -----------------------------------------
        if zeroDummy.next:
            return zeroDummy.next

        elif oneDummy.next:
            return oneDummy.next

        else:
            return twoDummy.next