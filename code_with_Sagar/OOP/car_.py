# class is blueprint of the Object
# Object is actual instance of of the class

class Car():
    def __init__(self,name):
        self.name=name
    def start(self):
        print(f'Car is Stating.....{self.name}')
    
    def stop(self):
        print(f'Car is Stopped?..{self.name}')
    

bmw=Car("BMW")

Wagnar=Car("Wagnar")

bmw.start()
bmw.stop()

Wagnar.start()
Wagnar.stop()