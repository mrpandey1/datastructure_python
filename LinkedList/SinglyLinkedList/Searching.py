class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def search(self,target):
        temp=self.head
        while temp.next and temp.data!=target:
            temp=temp.next
        if temp.data!=target:
            print("Not found")
            return
        print("Found")
llist=LinkedList()
llist.head=Node(1)
second=Node(2)
llist.head.next=second
llist.printlist()
llist.search(4)
