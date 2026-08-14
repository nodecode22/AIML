class Student:
    college="Arka jain university"
    year="4th year"

stu1=Student()
stu2=Student()
print(stu1.college, stu1.year)
print(stu2.college, stu2.year)



class Teacher:
    def __init__(self,name,subject,salary):
        self.name=name
        self.subject=subject
        self.salary=salary

tech1=Teacher("saurabh","English",50000)

