"""
Write a program that takes as input. Using conditional statements,
calculate the based on these rules:
Q1 salary
final tax rate
• If salary < 30,000 → 5%
• If salary is 30,000–70,000 → 15%
• If salary > 70,000 → 25%

"""

salary=int(input("Enter your salary to k now your tax rate: "))
if salary<30000:
    print("Your tax rate is 5%!")
elif (salary>30000 and salary<70000):
    print("Your tax rate is 15%!")
elif (salary>70000):
    print("Your tax rate is 25%!")
else:
    print("Enter correct salary!!!!")



#Write a function that takes two integers a and b and prints all even numbers between them (inclusive).
def evenbtw(a,b):
    for i in range(a,b+1):
        if(i%2==0):
            print(i)
print(evenbtw(10,20))



#Write a function to return the count the number of digits in a number, n .

def count(n):
    x=len(str(n))
    return x
print(count(1422432))


# Write a function to return the sum of digits of a number, n 

def sumofdigit(n):
    sum=0
    while n>0:
        sum+=(n%10)
        n=n//10
    return sum
print(sumofdigit(1235))


# Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5

for i in range(1,101):
    if(i%3==0 and i%5==0):
        print(i)

# Design a program to continuously input a number from user & print if it is positive or negative until the user enters “Quit”.

while True:
    x=int(input("Enter a number: "))
    if(x>=0):
        print("Its a positive Number!!")
    else:
        print("Its a negative Number!!")

    print("Do you want to retry!!......(Y/N)")
    val=input()
    if(val=='y' or val=='Y'):
        continue
    else:
        break


"""
Lets create a Simple Calculator that performs arithmetic operations. Create
a function that performs addition, subtraction,
multiplication, or division based on the parameter.
[ operation parameter can have values + , - , '* & / .
"""

def calculator(a,op,b):
    if(op=='+'):
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b
    elif op=="**":
        return a**b
    elif op=='%':
        return a%b
    else:
        return a//b
print(calculator(25,'**',3))


# Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.

def is_prime(n):
    count=0
    if(n>2):
        for i in range(2,n-1):
            if(n%i==0):
                count+=1
        if count>0:
            print(f"False, {n} is not a prime number!!")
        else:
            print(f"True, {n} is prime number!!")
    elif n==2:
        print("True, 2 is a prime number!!")
    else:
        print("Enter a value greater than 2")
n=int(input("Enter a number check prime: "))
is_prime(n)
    

""" 
Let's create a “ ”. Given a secret number (already
decided by you), write a program that asks the user to guess it and prints:
Q10 Number Guessing Game
•
"Too high" if the guess is above the number
•
"Too low" if the guess is below
•
"Correct!" if the guess matcheskwbkjwbcvivb
"""

secret_number=26
while True:
    guess=int(input("Guess the number: "))
    if guess==secret_number:
        print("Congrats!! you guessed it right!!")
        break
    elif guess>secret_number:
        print("Try with a lower number!!")
    elif guess<secret_number:
        print("Try with a larger number!!")
    else:
        print("Error occured!!")