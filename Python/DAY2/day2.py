# conditional statements (if,else,elif)

# write a program to check voter eligibilty
age=int(input("Enter your age: "))
if age>=18:
    print("you can vote!")
else:
    print("you can not vote!")



# progranm to check the child, teenage, adult by their age

x=int(input("Enter the age: "))

if x<13:
    print("You are a child!")
elif x>13 and x<18:
    print("You are a teenager!")
else:
    print("You are an Adult!")

#username password example 

user=input("Enter your username: ")
password=input("Enter yout password: ")

if user=="admin" and password=="pass":
    print("login successfull!")
elif user=="admin":
    print("wrong password!")
elif password=="pass":
    print("Wromg username!")
else:
    print("Wrong credentials!")


#check multiple of 5

q=int(input("Enter the number: "))
if q%5==0:
    print("Multiple of 5!")
else:
    print("not a multiple of 5!")

#odd or even 

s=int(input("Enter the number: "))
if (s%2==0):
    print("EVEN")
else:
    print("ODD")



# nesting of conditional statements

#user-password example 

username=input("Enter username: ")
password=input("Enter Password: ")


if(username=="admin" and password=="pass"):
    print("login successful!")
else:
    if(username=="admin"):
        print("Wrong password!")
    else:
        print("Wrong username!")

# match case statement in python

color=input("Enter a color: ")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Slow")
    case "Red":
        print("Stop")
    case _:
        print("Wrong Color!")


#while loop

count=1
while count<=10:
    print(f"god exists!{count}")
    count+=1
print("The loops exits after 10 iteration!")

#print from 1 to 5 using while loop

c=1

while c<=5:
    print(c)
    c+=1
print("Execution Done !")

# print 5 to 1 using while loop

c1=5
while c1>=1:
    print(c1)
    c1-=1
print("Execution done !")

# table of 6

st=0
while st<10:
    print(f"6x{st+1}={6*(st+1)}")
    st+=1


#using of break and continue

n=1
while (n<=10):
    print(n)
    if(n%6==0):
        break
    n+=1
print("Outside loop now!")

#use of continue to skip multiple of 3
x=1
while (x<=10):
    if(x%3==0):
        x+=1
        continue
    print(x)
    x+=1
print("outside loop....")


#print odd number form 1 to 10 using continue 

p=1
while(p<=10):
    if(p%2==0):
        p+=1
        continue
    print(p)
    p+=1


#for loop

str="saurabh"

for v in str:
    print(v)

str1="saurabh_agarwal"

if 'O' in str1:
    print("O exists in str1")
else:
    print("no O does not exists!!")

for i in range(10): #range(start_value,end_value-1,step_value)
    print(i)


# print any thing n number of times

txt="Hello saurabh Agarwal"
for i in range(8):
	print(txt)

count no. of letters in a word

word="Artificial intelligence"

count=0

for i in word:
	if(i=='i'or i=='I'):
		count+=1
print("Total number of letter 'i' in the word: ,",count)


# count number of vowels in a word or sentence

wrd="artiificial intelligence"
coun=0
for i in wrd.lower():
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
		coun+=1

print("The total number of vowels in the given word:",coun)

# range function range(start,end-1,step)

for i in range(0,31,3):
	print(i)


# sum of n first natural numbers
n=int(input("enter the value of n: "))
sum=0
for i in range(1,n+1,1):
	sum+=i
print(f"The sum of first {n} natural number is",sum)



