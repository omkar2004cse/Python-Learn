# encapsulation is used for the hidding the internal detsils

class Bank():
    def __init__(self,ac_no,blance):
        self.ac_no=ac_no
        self.__blance=blance
    
    def deposite(self,amount):
        self.__blance+=amount
        print(f'{amount} is Deposited in your bank Ac_no is{self.ac_no}')
        # print(self.__blance)

    def balance_check(self):
        print("Your balance is:-",self.__blance)
my=Bank(161518110001242,27400)

my.deposite(101)
my.balance_check()
print(my.ac_no)

#print(my.self.__blance)  # these is the private variable not access the by object creation