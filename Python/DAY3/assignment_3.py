# #1 Ask the user for a string and check whether it is a palindrome or not. A palindrome is a string which is same when we read it forward & backward. Eg - “madam”, “racecar” etc.

# x=input("Enter a string to check whether it is palindrome or not: ")
# s=[]
# for i in x:
#     s.append(i)

# s.reverse()
# new_string=""
# for i in s:
#     new_string+=i

# if x==new_string:
#     print("This is a palindroome string!!")
# else:
#     print("This is not a palindrome string!!")


# #2. Given a list of integers compute the average of all numbers in the list

# list1=[12,2,22,4,57,8,97]
# sum=0
# for i in list1:
#     sum+=i
# print(f"the Average of elements of the list is {sum/len(list1)}")


# #3.  Input two lists of integers from the user. Merge them into one list and sort the result.
# q=int(input("Enter number of elements: "))

# x1=[]
# x2=[]

# for i in range(0,q):
#     print(f"Enter the value for list1 element at index {i}")
#     c=int(input("Enter the value: "))
#     x1.append(c)

# for i in range(0,q):
#     print(f"Enter the value for list2 element at index {i}")
#     c=int(input("Enter the value: "))
#     x2.append(c)

# for i in x2:
#     x1.append(i)

# x1.sort()
# print(x1)

# # Given a tuple of integers, create:
# # • A tuple of all even numbers
# # • A tuple of all odd numbers

# t1=(1,2,3,4,5,6,7,8,9,10)

# t_even=()
# t_odd=()

# for num in t1:
#     if num % 2 == 0:
#         t_even += (num,)
#     else:
#         t_odd += (num,)

# print("Even numbers:", t_even)
# print("Odd numbers:", t_odd)


# #Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key (’A’, ‘B’, ‘C’, ‘D’)
# depending on the operation they want to perform on the dictionary:
# 1. A - Add a student
# 2. B - Update marks
# 3. C - Search for a student
# 4. D - Display all students and marks

student={}

def Add_student():
    name=input("Enter the name: ")
    marks=int(input("Enter marks: "))
    student.update({name:marks})
    

def marks_updt():
    name=input("enter the student name whose marks you wanna change: ")
    if name in student:
        marks=int(input("Enter the marks: "))
        student[name]=marks
        
    else:
        print("Sorry this entity does not exist!!")
        
def search():
    name=input("enter the student name to check: ")
    if name in student:
        print(f"the stduent {name} having marks {student[name]}")
        
    else:
        print("Sorry this stduent does not exist!!")
        
def display():
    print(student.items())
    print("")
while True:
    print("A - Add a student\nB - Update marks\nC - Search for a student\nD - Display all students and marks")
    value=input("Enter the option:(A,B,C,D): ")
    if (value=='A'or value=='a'):
        Add_student()
        
    elif (value=='B' or value=='b'):
        marks_updt()
        
    elif (value=='c' or value=='C'):
        search()
        
    elif (value=='d' or value=='D'):
        display()
        
    else:
        print("Wrong input Try again")
        continue
    x=input("Do you want to continue?(Y/N): ")
    if(x=='Y' or x=='y'):
        continue
    else:
        break