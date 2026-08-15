# create a bank account class with attributes account_number,owner_name,and balance
# add methods to deposit, withdraw, and check balance

class BankAccount:
    def __init__(self,acc_no,name,bal):
        self.acc_no=acc_no
        self.name=name
        self.bal=bal
    def deposit(self,amount):
        self.bal=self.bal+amount

    def withdraw(self,amount):
        self.bal=self.bal-amount

    def check_bal(self):
        print(f"Balance:{self.bal}")

ac1=BankAccount(1000101010,"Saurabh Agarwal",200000)
ac1.deposit(10000)
ac1.check_bal()

ac1.withdraw(100000)
ac1.check_bal()


"""
 Create a class Book with the following attributes:
• title
• author
• list of reviews
And add methods to:
• add a new review
• count reviews
• display all review
"""

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.__review=[]

    def add_review(self,star):
        self.__review.append(star)

    def count_review(self):
        print(len(self.__review))

    def display_review(self):
        print("reviews:")
        for i in self.__review:
            print(i,"\n")
b1=Book("Musafir cafe","Rajat adalal")

b1.add_review("this book is so good")
b1.add_review("this book is so good")
b1.add_review("this book is so good")
b1.add_review("this book is so good")

b1.count_review()

b1.display_review()


"""
Create a class with private attributes _name, _roll_no, and _marks.
Provide getter and setter methods with validation (e.g., marks cannot be
negative, roll number has to be between 1 & 100 & name cannot be empty).
"""


class Student:
    def __init__(self):
        self._name=""
        self._roll=0
        self._marks=0


    def getter(self):
        print(f"The student {self._name} whose roll no. is {self._roll} got {self._marks}.")


    def setter(self,name,roll,marks):
        if marks>0 and roll>1 and roll<100 and name!="":
            self._name=name
            self._roll=roll
            self._marks=marks
            print("Student data upadted successfully!!")
s1=Student()
s1.setter("saurabh",25,89)
s1.getter()


# create a class shape with a method area() create a subclass circle, rectangle and triangle that override the area()

class Shape:
    def Area():
        pass


class Circle(Shape):
    def Area(self,r):
        print(f"The area of circle is {3.14*r*r}")


class Rectangle(Shape):
    def Area(self,l,b):
        print(f"The area of Rectangle is {l*b}")


class Triangle(Shape):
    def Area(self,b,h):
        print(f"The area of the triangle is {0.5*b*h}")

c1=Circle()
c1.Area(7)

r1=Rectangle()
r1.Area(10,20)

t1=Triangle()
t1.Area(5,9)


# Create a base class vehicle with attributes like brand and model. Create two subclass Car and Bike that add extra attributes - seats (in Car) & engine_cc (in Bike).


class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class Car(Vehicle):
    def __init__(self,seats,brand,model):
        super().__init__(brand,model)
        self.seats=seats
class Bike(Vehicle):
    def __init__(self,cc,brand,model):
        super().__init__(brand,model)
        self.cc=cc

c1=Car("Mercedes","Benz",6)
print(c1.brand,c1.model,c1.seats)

b1=Bike(770,"TVS","jupiter")
print(b1.brand,b1.model,b1.cc)

