# function are the block of code which is used to perform same task without writing the same code them again and again we use function instead and call them using the function name whenever its needed

# def keyword is used to define function 
def hi():
    print("This is executed by the hi function")

# function called by the name if function
hi()

# function to calculate the sum of two number
def sum(a,b):
    sum=a+b
    return sum
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
value=sum(a,b)
print(value)


# function to find avg of three number

def avg(a,b,c):
    avg=(a+b+c)/3
    return avg

print(avg(1,34,2))

# function with default parameter

def sum1(a,b=2): # here value of b is 2 as a default parameter 
    sum=a+b
    return sum
print(sum1(5))
print(sum1(4,9))


# there are two type of function 
#1. built-in function: print(), input(), lower() etc...
#2. user defined : sum(), sum1(), avg(), which are defiend by user.....


# lambda function

avg=lambda a,b:(a+b)/2
print(avg(12,24))

# factorial function

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
n=int(input("Enter the value of n: "))
print(factorial(n))