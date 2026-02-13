# inheritance is one of the oop concept that used the child class acess the property of its parent class 

class Parent():
    def __init__(self,house,land):
        self.house=house
        self.land=land
    
    def p(self):
        print(f'property are :- {self.house,self.land}')

class child(Parent):
    def property(self):
        return super().p()
        

p=Parent("Two BHK","2 ARC")
p.p()

c=child("three","1 ARC")
c.p()