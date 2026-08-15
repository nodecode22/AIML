
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        # 1. Encapsulation has three type of data hiding public, protected, private
        self.__balance=balance #here if we use _ its protected which can not be accesed outside class and __ for private 

    def get_bal(self):
        return (self.__balance)

    def set_bal(self,newBalance):
        self.__balance=newBalance

B1=BankAccount("Saurabh Agarwal",120000)
print(B1.name,B1.get_bal())
B1.set_bal(300000)

print(B1.get_bal())

# we can access private attribute by B1._BankAccount__balance

print(B1._BankAccount__balance)

