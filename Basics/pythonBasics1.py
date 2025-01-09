# Basic data Types 

import math
print("hello soni")
# String
name="Soni Rathore"
print(name)

print(type(name))

first="Soni"
last="Rathore"
# concatination
full=first+last
print(full)


# float and int 
age =56.78
print(type(age))


# boolean 
flag=True
print(flag)


# one line of code 
name,age,branch={"Soni",56,"IT"}
print(name)


# type casting

a=89
b=56.67
c="error"
print(a)
print(b)
print(c)

a=str(a)
# c=float(c)
print(a)
b=int(b)
print(b)
# print(c)


# taking input from user 
# n=input("Enter your name")
# print(type(n))

# string functions
 
s="testing"
print(s)
print(s.upper())
print(s.lower())
print(len(s))
print(s.find("s"))



# math functions

val1=1.5
val2=2.6
val3=4.8
print(max(val1,val2,val3))
print(min(val1,val2,val3))
print(math.floor(val1))
print(math.ceil(val2))


# slicing 

Myname="Soni Rathore"

print(Myname)
print(Myname[1:4])
print(Myname[4:6:1])


for i in range(10):
    print(i)

for i in range(10,0,-2):
    print(i)

for i in range(1,6):
    for j in range(1,6):
        print(i,j)


# lists - used to store multiple values in a single vriables

fruits=["Apple","Mango","Banana","Strawberry","PineApple"]
fruits.append("3")
for i in fruits:
    print(i)


a=[1,2,3,4,5]
b=[11,12,13,14,15]
c=[21,22,23,24,25]

merge=[a,b,c]

for i in merge:
    for j in i:
     print(j)


# tuples 

t1=("Soni",21,"IT")
for i in t1:
    print(i)
# collections -single variable that store multiple values

# 1.lists - mutable, ordered,duplicates allowed
fruits=["apple","banana","mango","r","t"]
fruits.append("s")
fruits.remove("mango")
fruits.append("s")
print(fruits[0::2])
for i in fruits:
    print(i)


# 2. tuples - immutable,ordered,duplictes allowed

veg=("potato","tomoto","onion","onion")
for i in veg:
    print(i)


# 3 sets -duplicates not allowed, unorderd, mutable

temp={"kite","f","we","o","o"}
for i in temp:
    print(i)
print(temp)

    

# dictionary
details={
    "name":"Soni Rathore",
    "email":"soni.@gmail.com",
    "phone":"1234567890"
}

print(details)
print(dir(details))


# functions 

def saySomething(temp):
    print(f"Hii {temp}")


saySomething("Soni")

# keyword arguments
def fun1(name , age):
    print(f"{name} , {age}")

fun1(age=67,name="Soni")


def fun2(v1,v2):
    return f"{v1},{v2}"


var=fun2(v2="hee",v1="twwe")
print(var)


# *args and *kargs  are used for multiple arguments
# args - tuple 
def fun3(*args):
   sum=0
   for i in args:
      sum+=i
   return f"{sum}"
ans=fun3(1,2,3,4,5,6)
print(ans)


# kwargs - used for key-value pairs


# arguments - positional, default, keyword, arbitary
def fun4(**kwargs):
    for i in kwargs:
        print(i)

fun4(name1="soni",
      name2="vini")

dict={
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4"
}

for i in dict.keys():
    print(i)


for i in dict.values():
    print(i)

# membership opertor - in , not in -indicates if a variable is present or not

str="hello buddy , I am here "
letter="k"
if letter in str:
    print(f"{letter} is found")
else :
    print(f"{letter} is not found")

# match case 

         
#def fun5(day):
#    match day:
#        case 1:
 #           print("Monday")
 #           return
  #      case 2:
  #          print("Tuesday")
   #         return
    #    case 3:
    #        print("Wednesday")
    #        return
   #     case _:
   #         print("Invalid")



# modules 

print(help("modules"))

