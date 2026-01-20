# constructor
class Op:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("addition is:-",self.num1+self.num2)
    def mul(self):
        print("Multiplication is :-",self.num1*self.num2)

o1=Op(12,23)
o1.mul() 
o1.add()
print(o1.num2)
print(o1.num1)

