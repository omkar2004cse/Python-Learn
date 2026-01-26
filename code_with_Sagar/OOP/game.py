class Character():
    def __init__(self,name,attack,health,blood):
        self.name=name
        self.attack=attack
        self.health=health
        self.blood=blood
    
    def power(self):
        print(f'Character is {self.name} its attack power is {self.attack} its health is {self.health} blood is weast is {self.blood}')

thor=Character("Thor",80,75,"Red")
hulk=Character("Hulk",76,60,"Blue")


thor.power()
hulk.power()

# Using the function we do not access the varable out of the class insted of the Global variable
# but using the class we can access the variable outside class 
print(hulk.attack)
print(f'Thor Blood Color is:- {thor.blood}')
