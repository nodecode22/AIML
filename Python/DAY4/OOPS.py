# there are four major properties of OOP in python
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism
 

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




# inheritence is the property in which we use the attritube and methods of the parent class in child class or sub class

class Employee:
    start_time="10AM"
    end_time="6PM"

    def change_time(self,new_end_time):
        self.end_time=new_end_time

# single level inheritance
class Teacher(Employee):
    def __init__(self,subject):
        self.subject=subject


class Admin(Employee):
    def __init__(self,role):
        self.role=role

t1=Teacher("English")
t1.change_time("4PM")
print(t1.subject,t1.start_time,t1.end_time)

staff1=Admin("Supervisor")

print(staff1.role,staff1.start_time,staff1.end_time)

# multi level inheritance
class Car:
    Company="Toyota"

class SUV(Car):
    def __init__(self,seats):
        self.seats=seats
class Luxury(SUV):
    def __init__(self,material,seats):
        super().__init__(seats)
        self.material=material
# here i have inherit from car to suv to luxury multi level inheritance

luxurious=Luxury("Imported leather",7)
print(luxurious.Company,luxurious.seats,luxurious.material)


# multiple inheritance

class Teacher:
    def __init__(self,salary):
        self.salary=salary

class Student:
    def __init__(self,GPA):
        self.GPA=GPA

class TA(Teacher,Student):
    def __init__(self,salary,GPA,name):
        super().__init__(salary)
        Student.__init__(self,GPA)
        self.name=name
t1=TA(90000,8.9,"Saurabh kumar")

print(t1.salary,t1.GPA,t1.name)