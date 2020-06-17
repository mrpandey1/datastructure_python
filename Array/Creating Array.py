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
    def delete(self,target):
        for j in self.data:
            if self.data[j]==target:
                return "Found"
        return "Not Found"
newArray=Myarray()
newArray.push(54)
newArray.push(4)
newArray.push(5)
newArray.push(45)
newArray.push(44)
print(newArray.get(0))
print(newArray.get(1))
print(newArray.get(2))
print(newArray.delete(44))
print(newArray.data)
        
