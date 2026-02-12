# the self variable that indicate the current object of the class

# these program are createrd the set details method because we not used the constructor
class Car():
    def set_details(self,name,color):
        self.name=name
        self.color=color
    def show(self):
        print(f'the brand of Car is {self.name} and colour is {self.color}')

bmw=Car()
bmw.set_details("BMW","RED")

bmw.show()