#DELETE NODE IN LINKED LIST


print("START")
#DEFINITION FOR SINGLE-LINKED LIST
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def deleteNode(self,node):
        #COPY THE VALUE OF NEXT NODE
        node.val=node.next.val
        #SKIP THE NEXT NODE BY CHANGING THE POINTER
        node.next=node.next.next
#FUNCTION TO PRINT LINKED LIST
def print_list(head):
    current=head
    while current:
        print(current.val,end=" -> ")
        current=current.next
    print("NONE")
#CREATE A LINKED LIST
head=ListNode(4)
head.next=ListNode(5)
head.next.next=ListNode(1)
head.next.next.next=ListNode(9)
print("BEFORE DELETION:")
print_list(head)

#NODE TO DELETE (VALUE 5)
node=head.next

#CALL SOLUTION
obj=Solution()
obj.deleteNode(node)

print("AFTER DELETION:")
print_list(head)
print("END")