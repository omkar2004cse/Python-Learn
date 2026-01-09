class Operation:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self,):
        print(self.n1+self.n2)
    def mul(self):
        print(self.n1*self.n2)

obj1=Operation(1,2)
obj2=Operation(12,23)

obj1.add()
obj1.mul()
print(obj1.n2)

obj2.add()
obj2.mul()
# print(obj2)