print("Its first day of my aiml journey")

# variables in python
X=22

name="Saurabh"

pi=3.14


print(X,name,pi)


#data type in python

#string boolean integer none float

str="Saurabh agarwal"

bool=True

intr=34

non=None

flt=21.5

print(str,bool,intr,flt,non)


# comment in python - with # symbol (single line comment)
'''
its a multi line comment and its get ignored while the code runs 
'''

#type function to check the variable type

print(type(str))
print(type(bool))
print(type(non))
print(type(flt))
print(type(int))



#style guide to write a varibale name in python

#always write the name of variable like the given one "total_sales"

total_sales=100000

print("Total sales of the year is",total_sales,"units")


#operators in python

"""
There are four types of operator and those are listed below

1.arithmetic operator
2.relational operator
3.Assignment operator
4.Logical operator
"""

a=12
b=3

# Arithmetic operators

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

# Relational operators (gives boolean value)

print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)


# Assignment Operator
a+=1
print(a)
a-=1
print(a)
a*=1
print(a)
a/=1
print(a)

# Logiical Operator

var=True
var1=False

print(not var)
print(var and var1)
print(var or var1)
print(not (4>6))

# Operator Precedence

"""
    ()
    **
    *,/,%
    +,-
    ==,!=,>,>=,<,<=,
    NOT
    AND
    OR

"""


# type conversion and type casting 

"""
There are two type of conversion of varibale type 
1. compiler does impliciltly(automatically) its called type conversion
2. The compatiable type will be converted explicitely(manually)
"""

#type conversion

dec=10+23.5
print(type(dec))


x=int("123")
print(type(x))


# taking user input in python

Username=input("Enter your username: ")
password=int(input("Enter your password: "))
print(f"username:{Username}\npassword:{password}")


num1=float(input("enter your age: "))
print("Age:",num1)


# average of two numbers

n1=float(input("entre 1st number: "))
n2=float(input("entre 2nd number: "))

avg=(n1+n2)/2

print(f"The average of {n1} & {n2} is {avg}")