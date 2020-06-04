class Node(object):

    def __init__(self, data):
        self.data = data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.length=0
    def push_back(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data,end=' ')
            temp = temp.next
        print()
llist=Linkedlist()
for i in range(3,0,-1):
    llist.push_back(i)
llist.printList()
