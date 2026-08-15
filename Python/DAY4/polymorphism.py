# polymorphism

class Employee:
    def get_designation(self):
        print("Designation is Employee")


class Teacher(Employee):
    def get_designation(sellf):
        print("Designation is Teacher")

teach=Teacher()
teach.get_designation()


# polymorphism byy duck typing method
# we can put same method name in two differnt class but having the same type of use 

class car:
    def get_wheel(self):
        print("Wheels=4")

class Truck:
    def get_wheel(self):
        print("Wheels=8")

c1=car()
c1.get_wheel()

t1=Truck()
t1.get_wheel()

