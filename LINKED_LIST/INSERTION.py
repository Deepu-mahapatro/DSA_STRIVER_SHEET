#INSERTION AT HEAD OF A LINKED LIST

#NODE CLASS
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#LINKED LIST CLASS
class LinkedList:
    def __init__(self):
        self.head=None
    #FUNCTION TO INSERT AT BEGINNING 
    def insertAtHead(self,data):
        #CREATE A NEW NODE
        newNode=Node(data)
        #POINT THE NEW NODE TO TEH CURRENT HEAD
        newNode.next=self.head
        #MAKE THE NEW NODE AS NEW HEAD
        self.head=newNode
    #FUNCTION TO DISPLAY THE LINKED LIST
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=" -> ")
            current=current.next
        print("NONE")
ll=LinkedList()
#CREATE NODES
ll.insertAtHead(50)
ll.insertAtHead(40)
ll.insertAtHead(30)
ll.insertAtHead(20)
ll.insertAtHead(10)
#DISPLAY THE LINKED LIST
ll.display()
