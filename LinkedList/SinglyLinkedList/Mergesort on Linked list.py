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
        
    def sort(self,h):
        if h==None or h.next==None:
            return h
        middle=self.getmiddle(h)
        nexttomiddle=middle.next
        middle.next=None
        left=self.sort(h)
        right=self.sort(nexttomiddle)
        sortedList=self.sortedMerge(left,right)    
        return sortedList
    
    def sortedMerge(self,a,b):
        result=None
        if a==None:
            return b
        if b==None:
            return a
        if a.data<=b.data:
            result=a
            result.next=self.sortedMerge(a.next,b)
        else:
            result=b
            result.next=self.sortedMerge(a,b.next)
        return result
    
    def getmiddle(self,head):
        if head==None:
            return head
        slow=head
        fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
        
llist = LinkedList()
for i in range(5,-1,-1):
    llist.InsertAtEnd(i)
llist.printList()

llist.head=llist.sort(llist.head)

llist.printList()















