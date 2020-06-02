class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()
llist=DoublyLinkedList()
for i in range(1,6):
    llist.push(i)
llist.printList()
