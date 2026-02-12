# polymorphism
# one word and its different funstion
# same method name but perform different operations

class Bird():
    def sound(self):
        print("bird make Sound")

class parroat(Bird):
    def sound(self):
        print("Parroat Sound Swak Swak")  
class Crow(Bird):
    def sound(self):
        print("Crow make sound Crow crow")
        return super().sound()

b=Bird()  
p=parroat()
cr=Crow()

b.sound()
p.sound()

cr.sound()