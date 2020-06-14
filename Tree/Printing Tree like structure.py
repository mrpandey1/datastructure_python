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
            root.leftChildChild=self.add(root.leftChild,data)
        elif (data>root.item):
            root.rightChild=self.add(root.rightChild,data)
        return root
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.leftChild)
        print(root.item,end='   ')
        self.inorder(root.rightChild)
    def traverse(self,rootnode):
        thislevel = [rootnode]
        a = '                                 '
        while thislevel:
            nextlevel = list()
            a = a[:int(len(a)/2)]
            for n in thislevel:
                print(a+str(n.item))
                if n.leftChild: nextlevel.append(n.leftChild)
                if n.rightChild: nextlevel.append(n.rightChild)
            print()
            thislevel = nextlevel

root=Node(1)
root.add(root,3)
root.add(root,5)
root.add(root,6)
root.add(root,7)
root.add(root,10)
root.add(root,2)
root.add(root,4)
root.inorder(root)
root.traverse(root)

