# string 

str1="Python"
str2="I love "

print(str2+str1)
print(len(str1))

# indexing in string
word="python is best language"
# p-0,y-1,t-2,h-3,o-4,n-5

# #lets suppose we have get the 4th letter in the string

# print(word[3])

# for ch in word:
#     print(ch)

#slicing the string

#syntax for slicing 
# str[start_indx:end_indx:step_indx]

print(word[0:14])

print(word[3:])

print(word[::-1])

# formatting in python

a=5
b=10
sum=a+b

# normal formatting
print("Language is {}".format("python"))
print("Sum of {} & {} is {}".format(a,b,sum))

# index based formatting
print("Sum of {1} & {0} is {2}".format(a,b,sum))

#value based formatting 
print("value of vars {a}".format(a=2))
x=12
print(f"the value of x is {x}")


# list in python (mutuable = can be modified) and string are immutable(can't be moodified)

# let's suppose we have to store marks of 10 stduents 

marks=[89,78,54,76,98,76,98,54,33,23]

# as similar as in python here the indexing starts from 0 to n-1

# for the above list 89 at 0, 78 at 1 and so on......

# here we have some functions that are used for list

# accessing a specific element in the list

print(marks[4])

# to get the length of the list we use len() function

print(f"The length of the list : {len(marks)}")

# if we try to acces the index which is not the part of list then it will giive out of index error

#for example

# print(marks[11]) it will cause an error 

# list is mutable that's why we can assign new values to it

marks[2]=88
print(marks)


# if we check the type of the list we get <class 'list'>

print(type(marks))

#just like string slicing we can slice the list too

print(marks[0:6:2])# list[start_index:end_index:step_index]


# list methods

#list.append(val)
#list.insert(index,val)
#list.sort()
#list.reverse()


#lets use them all on the marks list

marks.append(90) # it will add 90 in the end of the list as new element

print(marks)
print(len(marks))


# insert can be used where we need to add the data at a specific place in the list and push the previous data to +1 index

marks.insert(3,44)
print(marks)

# it is used to sort the lsit in assending order
marks.sort()
print(marks)

# to reverse the list elements we use reverse() function
marks.reverse()

print(marks)


# # using loop to find an element in list
# # this is also called linear search 
# x=[10,20,30,40,50,60,70]
# n=int(input("Enter the number to find in the list: "))
# index=0
# for val in x:
#     if(n==val):
#         print(f"{n} is found at {index}")
#     index+=1
     

# tuple in python
# it is same as list but its immutable
v=(1,2,3,4,5,6,7)

print(v)
print(len(v))
print(type(v))

# note : if we assign single value to a tuple then it will recognize it as the data type entered in it
# for example

c=(2)
# to correct this we use single ',' at the lst for single element in tuple
cc=(3,)
print(type(c))
print(type(cc))


# similar as list it has slicing method

print(v[1:4])



# similar as list we can use find sum using for loop

b=(12,23,3,12,4,6,12,4,55,6,7)

sum=0
for x in b:
    sum+=x
print(f"The sum of all values: {sum}")


# tuple functions or methods

# t.index(element) is used to find index of the element

print(b.index(3))

#t.count(element) is used to find occurrences of that element

print(f"The count of 12 in the tuple {b.count(12)}")

# dictionary in pyhton

info={
    "name":"saurabh agarwal",
    "CGPA":9.9,
    "Subject":["Maths","English","Chemistry"],
    3.14:"PI"
}

print(type(info))

print(info["name"])
print(info[3.14])

# we can reassign vales of keys because it is a mutable data type

info["name"]="Saurabh Kumar agarwal"

print(info["name"])


# dictionary methods or functions

#d.keys() : return all keys

print(info.keys())

#d.values() : return all values

print(info.values())

#d.items() : retrun all key value pair

print(info.items())

#d.get(key) : retrun value according to key
# we use this because if the does exist then it give none but in normal method it will throw an error

print(info.get("name"))


# d.update(key:value) : to add new kay:value pair in the existing dictionary

info.update({
    "college":"Arka Jain University"
})

print(info.items())

# sets in python

# set is the collection of immutable data type elements here we have repeated some elements but when we print the set we get only the unique elements

s={1,2,3,4,5,2,3,1,2}

print(s)
print(type(s))
print(len(s))

#create an empty set

# ss={} it is going to create a empty dictionary to create an empty set we need to write cc=set()

ss=set()

# to add some element in set we use add() method
# functions to use with set

# s.add(val) : add value to set
ss.add(223)
ss.add(12)
ss.add(3)
ss.add(54)
ss.add(67)
ss.add(654)
print(ss)

# s.remove(val) : used to remove any value in set 

ss.remove(223)
print(ss)

#s.pop() : removes the random val
ss.pop()

#s.clear() : make the set empty

ss.clear()
print(ss)

#just like sets in maths here we have union and intersection
s1={1,2,3,4,5,6}
s2={2,3,4,6,7,98,1}

print(s1.union(s2))


print(s2.intersection(s1))


