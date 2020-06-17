class Myarray:
    def __init__(self):
        self.length=0
        self.data={}
    def get(self,index):
        return self.data[index]
    def push(self,data):
        self.data[self.length]=data
        self.length+=1
        return self.length
    def pop(self):
        temp=self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return temp
    def delete(self,index):
        if self.length<=0:
            return
        for i in range(index,self.length-1):
            self.data[i]=self.data[i+1]
        del self.data[self.length-1]
        self.length-=1
newArray=Myarray()
newArray.push(54)
newArray.push(4)
newArray.push(5)
newArray.push(45)
newArray.push(44)
print(newArray.get(0))
print(newArray.get(1))
print(newArray.get(2))
print(newArray.data)
print(newArray.delete(1))
print(newArray.data)
        
