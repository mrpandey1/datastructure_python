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
llist.printList()
