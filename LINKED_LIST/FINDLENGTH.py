#TO FIND THE LENGTH OF THE LINKED LIST 

#NODE CLASS 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#LINKED LIST CLASS
class LinkedList:
    def __init__(self):
        self.head=None
    #FUNCTION TO FIND THE LENGTH OF THE LINKED LIST
    def findLength(self):
        #START FROM THE HEAD NODE
        current=self.head
        #COUNTER TO STORE THE NUMBER OF NODES
        count=0
        #TRAVERSE UNTIL WE REACH THE END OF THE LIST
        while current is not None:
            count+=1
            current=current.next
        return count

#CREATE A LINKED LIST
ll=LinkedList()
#CREATE NODES
ll.head=Node(10)
ll.head.next=Node(20)
ll.head.next.next=Node(30)
ll.head.next.next.next=Node(40)
#PRINT THE LENGTH
print("LENGTH IF THE LINKED LIST:",ll.findLength())        