# Given a list of tuples with info(name, subject):

# . list all unique course

# · list students enrolled in English

# · create dictionary (student, set of courses)

info=[
    ("Saurabh","Maths"),
    ("Nivesh","English"),
    ("Dheeraj","Science"),
    ("Ravu","Science"),
    ("Mohit","Science"),
    ("Bob","English")

]

subject=set()

for i in info:
        subject.add(i[1])
print(f"Total subjects: {subject}")

name=[]
for i in info:
    if(i[1]=="English"):
        name.append(i[0])
print(f"The stduent who have taken English : {name}")

dict={}

for name,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
print(dict)


