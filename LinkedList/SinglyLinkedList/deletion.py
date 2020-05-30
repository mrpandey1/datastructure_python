class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def deleteNode(self,key):
        temp=self.head
        while temp and temp.data!=key:
            prev=temp
            temp=temp.next
        if temp.data!=key:
            print(f'{key} not found')
            return
        prev.next=temp.next
    def deleteFirst(self):
        temp=self.head
        self.head=temp.next
    def deleteLast(self):
        temp=self.head
        while temp.next:
            prev=temp
            temp=temp.next
        prev.next=None
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()
llist = LinkedList()  
llist.push(7)  
llist.push(1)  
llist.push(3)  
llist.push(2)
print ("Created Linked List: ") 
llist.printList()
llist.deleteNode(1)  
llist.printList()
llist.deleteFirst()
llist.printList()
llist.deleteLast()
llist.printList()
