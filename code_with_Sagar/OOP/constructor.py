# constructor is one python method they are automatically called when the oject of class is created

class car():
    def __init__(self,brand,color,speed):
        self.brand=brand
        self.color=color
        self.speed=speed
    def show(self):
        print(f'Car brand is {self.brand} and color of car is {self.color} and its speed is {self.speed}')


tesla=car("Tesla","white","200")
bmw=car("BMW","Blue",180)
tesla.show()
bmw.show()

print(bmw.speed)