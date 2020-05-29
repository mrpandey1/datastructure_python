class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
linkedlist=LinkedList()
linkedlist.head=Node(1)
second=Node(2)
linkedlist.head.next=second
linkedlist.print()
