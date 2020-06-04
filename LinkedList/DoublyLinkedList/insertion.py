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
    def addatend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    def insertAfter(self,target,data):
        new_node=Node(data)
        temp=self.head
        if self.head is None:
            print(f'{target} not found')
            return
        while temp.next and temp.data!=target:
            temp=temp.next
        if temp.data==target:
            new_node.next=temp.next
            temp.next=new_node
            new_node.prev=temp
        else:
            print(f'{target} not found')
            return
    def insertBefore(self,target,data):
        new_node=Node(data)
        temp=self.head
        if self.head is None:
            print(f'{target} not found')
            return
        while temp.next and temp.data!=target:
            pre=temp
            temp=temp.next
        if temp.data==target:
            new_node.next=temp
            temp.prev=new_node
            pre.next=new_node
            new_node.prev=pre
        else:
            print(f'{target} not found')
            return
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
llist.addatend(5)
llist.addatend(4)
llist.addatend(3)
llist.addatend(2)
llist.addatend(1)
llist.insertAfter(3,32)
llist.insertBefore(32,34)
llist.printList()
