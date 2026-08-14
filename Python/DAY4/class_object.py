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

