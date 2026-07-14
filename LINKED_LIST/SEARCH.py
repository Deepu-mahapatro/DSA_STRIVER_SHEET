#SEARCHING IN LINKED LIST

#NODE CLASS
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#LINKED LIST CLASS
class LinkedList:
    def __init__(self):
        self.head=None
    #FUNCTION TO SEARCH AN ELEMENT IN THE LINKED LIST
    def search(self,key):
        #START FROM THE HEAD NODE
        current=self.head
        #TRAVERSE THE LINKED LIST
        while current is not None:
            #IF VALUE IS FOUND 
            if current.data==key:
                return True
            #MOVE TO NEXT NODE
            current = current.next
        #VALUE NOT FOUND
        return False
#CREATE A LINKED LIST
ll=LinkedList()
#CREATE NODES
ll.head=Node(10)
ll.head.next=Node(20)
ll.head.next.next=Node(30)
ll.head.next.next.next=Node(40)
print("IS 30 PRESENT:",ll.search(30))