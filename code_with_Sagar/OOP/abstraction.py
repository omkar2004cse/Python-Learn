from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        print("This is Parent Class")

class bike(vehicle):
    def start(self):
        print(f'Bike Start with Battery')
        return super().start()
    
class car(vehicle):
    def start(self):
        print("Car Start with key")
        return super().start()
    
c=car()
b=bike()

c.start()

b.start()