"""
class Car:
    def start(self):
        print("Car",self,"start")
    def info(self,brand,color):
        print(brand,"is color is:-",color)
    
 
o1=Car()
o1.start()
o1.info("BMW","blue")
print(o1.brand) #not gives output

o2=Car()
o2.start()

"""
# self that point to the each object refer in class
# ----------------------------------------------------------------
class Op:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        
        