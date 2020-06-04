class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def addatstart(self,data):
        new=Node(data)
        new.next=self.head
        new.prev=None
        if self.head is not None:
            self.head.prev=new
        self.head=new
    def deletestart(self):
        temp=self.head
        if self.head is None:
            print("Deletion from empty Linked list is not possible")
            return
        self.head=self.head.next
        self.head.prev=None
    def deleteend(self):
        temp=self.head
        if self.head is None:
            print("Deletion from empty Linked list is not possible")
            return
        while temp.next is not None:
            pre=temp
            temp=temp.next
        pre.next=None
    def deleteelement(self,target):
        temp=self.head
        if self.head is None:
            print("Deletion from empty Linked list is not possible")
            return
        while temp.next and temp.data != target:
            pre=temp
            temp=temp.next
        if temp.data!=target or temp.next is None:
            print("Not Found")
            return
        pre.next=temp.next
        pre.next.prev=pre
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()
llist=DoublyLinkedList()
llist.addatstart(1)
llist.addatstart(2)
llist.addatstart(3)
llist.addatstart(4)
llist.addatstart(5)
llist.addatstart(3)
llist.addatstart(4)
llist.addatstart(5)
llist.printList()
llist.deletestart()
llist.deleteelement(1)
llist.deleteend()
llist.printList()
