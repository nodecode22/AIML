class Student:
    college="Arka jain university"
    year="4th year"

stu1=Student()
stu2=Student()
print(stu1.college, stu1.year)
print(stu2.college, stu2.year)



class Teacher:

    def __init__(self): #this is a default constructor
        print("Default constructor has been called!!")
    #creating constructor in class teacher
    def __init__(self,name,subject,salary): # it is a parameterized constructor
        self.name=name
        self.subject=subject
        self.salary=salary
    #creating new constructor which will retun teacher salary
    def get_salary(self):
        return self.salary 
tech1=Teacher("saurabh","English",50000)

print(f"{tech1.name} is getting paid a salary of {tech1.get_salary()}")


#attribute(class and instance)

class Car:
    car_company="KIA" # class attribute can be accesed using class name or object name

    def __init__(self,model,year):
        self.model=model # instance attribute
        self.year=year

c1=Car("nexon",2017)

print(c1.year)
print(c1.model)

#here we are accessing class attribute using object name and class name too
print(Car.car_company)
print(c1.car_company)


# instance method

class Laptop:
    storage_type="SSD"

    def __init__(self,RAM,Storage):
        self.RAM=RAM
        self.Storage=Storage
    
    def get_info(self):
        print(f"The Laptop has {self.RAM} RAM and {self.Storage} {self.storage_type}")

l1=Laptop("12GB","512GB")
l2=Laptop("4GB","256GB")

l1.get_info()


# class method

class Bike:
    company="TVS"
    def __init__(self,model,milage):
        self.model=model
        self.milage=milage

    @classmethod # its a decorator which convert the method to class method
    def get_company(cls):
        print(f"The bike is of the {cls.company} company.")

    def get_info(self):
        print(f"the Bike is {self.model} model and it has {self.milage}km/pl milage")

    @staticmethod
    def cal_discount(price,discount):
        new_price=price-(price*discount)/100
        print(f"The new price after discount of {discount}% is Rs {new_price}")
b1=Bike("Jupiter",40)
Bike.get_company()
Bike.cal_discount(100000,15)