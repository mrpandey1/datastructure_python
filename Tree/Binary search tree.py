class Node:
    def __init__(self,item):
        self.item=item
        self.leftChild=None
        self.rightChild=None
    def add(self,root,data):
        temp=root
        if temp==None:
            return Node(data)
        if (data<root.item):
            root.leftChild=self.add(root.leftChild,data)
        elif (data>root.item):
            root.rightChild=self.add(root.rightChild,data)
        return root
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.leftChild)
        print(root.item,end='->')
        self.inorder(root.rightChild)
root=Node(1)
root.add(root,3)
root.add(root,1)
root.add(root,6)
root.add(root,7)
root.add(root,10)
root.add(root,14)
root.add(root,4)
root.inorder(root)
