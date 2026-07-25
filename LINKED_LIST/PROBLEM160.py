#INTERSECTION OF TWO LINKED LISTS

# Definition for Linked List Node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def getIntersectionNode(self, headA, headB):

        # If either list is empty,
        # intersection is not possible
        if not headA or not headB:
            return None

        # Pointer starts from List A
        ptrA = headA

        # Pointer starts from List B
        ptrB = headB

        # Keep moving until both pointers
        # become equal
        while ptrA != ptrB:

            # If pointer reaches end,
            # move it to other list
            if ptrA:
                ptrA = ptrA.next
            else:
                ptrA = headB

            # If pointer reaches end,
            # move it to other list
            if ptrB:
                ptrB = ptrB.next
            else:
                ptrB = headA

        # Returns intersection node
        # or None
        return ptrA


# --------------------------------------------------
# Create Linked List
# --------------------------------------------------
def createLinkedList(arr):

    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for value in arr[1:]:
        curr.next = ListNode(value)
        curr = curr.next

    return head


# --------------------------------------------------
# Get Last Node
# --------------------------------------------------
def getTail(head):

    while head.next:
        head = head.next

    return head


# --------------------------------------------------
# Print Linked List
# --------------------------------------------------
def printList(head):

    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next

    print()


# --------------------------------------------------
# Driver Code
# --------------------------------------------------

# First Linked List
listA = list(map(int, input("Enter List A: ").split()))

# Second Linked List
listB = list(map(int, input("Enter List B: ").split()))

# Common Part
common = list(map(int, input("Enter Common Nodes: ").split()))

# Create all lists
headA = createLinkedList(listA)
headB = createLinkedList(listB)
commonHead = createLinkedList(common)

# Connect List A to Common List
tailA = getTail(headA)
tailA.next = commonHead

# Connect List B to Common List
tailB = getTail(headB)
tailB.next = commonHead

print("\nList A:")
printList(headA)

print("\nList B:")
printList(headB)

# Find Intersection
solution = Solution()

intersection = solution.getIntersectionNode(headA, headB)

print("\nIntersection Node:")

if intersection:
    print(intersection.val)
else:
    print("No Intersection")