# take user input of name and age and print "hello saurabh, you are 21 years old!"

age=int(input("Enter your age: "))
name=input("Enter your Name: ")

print(f"Hello {name}, you are {age} years old!")


num1=float(input("Enter 1st number: "))
num2=float(input("Enter 2nd number: "))

print(f"sum={num1+num2}\nDiff={num1-num2}\nProduct={num1*num2}\nQuotient={num1/num2} ")

# Ask the user to enter two integers and one float. Convert them all to floats and print their average.

int1=int(input("Enter a integer: "))
int2=int(input("Enter a integer: "))
flt=float(input("Enter a decimal value: "))

avg=(float(int1)+float(int2)+flt)/3

print("The average value of all three is",avg)

"""
The user enters a string containing a number (e.g., "45" ). Convert it to:
• an integer
• a float
• a string again
Print all three values with their types
"""

user_in=input("Enter a value: ")
print(user_in,type(int(user_in)))
print(user_in,type(float(user_in)))
print(user_in,type(str(user_in)))

#Evaluate and print the result of the following expression:

x = 10 + 3 * 2 ** 2
print(x)#the answer will be 22 first exponent>product>sum


# write a program to swap values of twp numbers

a=12
b=65
print("Before swapping")

print(f"a:{a} b:{b}")
#swapping
a=a+b
b=a-b
a=a-b
print("After swapping")
print(f"a:{a} b:{b}")

#tempreature calculation

celcius=input("Enter the temp.: ")
newTemp=float(celcius)

fahrenheit=(newTemp*9/5)+32
print(f"The temp. {celcius}'C is {fahrenheit}'F")

#Take the radius (r) as user input and print the area.

radius=float(input("Enter the radius of the circle: "))
pi=3.14
area=pi*radius*radius
print(f"The area of the circle of radius {radius} is {area}")

#Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and compute simple interest:
# SI = (P ∗ R ∗ T)/100

P=float(input("Enter the principle amount: "))
R=float(input("Enter the Intrest rate: "))
T=float(input("Enter the Time: "))

SI=(P*R*T)/100

print(f"SI:{SI}")

number=float(input("Ente a number: "))
z=number%1
y=number//1

print(z,int(y))