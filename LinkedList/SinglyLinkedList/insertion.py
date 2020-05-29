class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data,end=' ')
            temp = temp.next
        print()
    def InsertAtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def InsertAtStart(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def InsertAfter(self,prev,data):
        temp=self.head
        while temp.next and temp.data!=prev:
            temp=temp.next
        if temp.data!=prev:
            print("Not Found")
            return
        new_node=Node(data)
        new_node.next=temp.next
        temp.next=new_node
    def InsertBefore(self,key,data):
        temp=self.head
        new_node=Node(data)
        if temp.data==key:
            new_node.next=self.head
            self.head=new_node
            return 
        while temp.next and temp.data!=key:
            prev=temp 
            temp=temp.next
        if temp.data!=key:
            print("Notound")
            return 
        new_node.next=temp
        prev.next=new_node
        
llist = LinkedList()
llist.InsertAtEnd(6)
for i in range(4):
    llist.InsertAtStart(i)
llist.InsertAfter(6,5)
llist.InsertBefore(6,433)
llist.printList()
