#Create and call a function
def z(lname):
    print("I'm "+ lname)
z("Hamdan")

#create and call a function passing 2 values
def z(fname,age):
    print("My name is ",fname,"I'm",age,"Years old")
z("Hamdan",20)

#create and call a function -pass two arguments.using *arg and **kwargs
def p(*students):#*arg
    print("First student is",students[0])
p("Hamdan","Ali")
def p(**student):#**kwargs
    print("First student is " + student["fname"])
p(fname="Hamdan",lname="Ali")\

#create and call a function-default parameter value.
def new(place="Mexico"):
    print("I'm from ",place)
new()

#create and call a function -print using tuple and set data type.
def test(lst):
    for x in lst:
        print (x)

tup=("Hamdan","Ali","Ameen")
test(tup)

set={"Hamdan","Ali","Ameen"}
test(set)

#create function passing pass statement.
def testing():
    pass

#create and print the lambda function passing number of arguments.(add,multiply,subtract)
def fn(n,b):
    return lambda a,b:(a*b*a)+(n-a)

d=fn(2,1)
print(d(6,1))

#create an array  and print the values.
x=["Hamdan","Ali","Ameen"]
print(x)

#print length of an array.
print(len(x))

#Lopping an array
for a in x:
    print(a)

#adding an array element
x.append("Sahal")
print(x)

#removing array elements
x.remove("Hamdan")
print(x)

#create a class and print the values.
class Qn:
    x=5
p=Qn()
print(p.x)

#create a class and objects and print the numbers 200, 105.
class Qn2:
    x=200
    y=105
p=Qn2()
print(p.x,",",p.y)

#Create a class named Car, use the __init__() function to assign values for Name and color.
class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
p=Car("Mercedez-Benz","Black")
print(p.name,p.color)

#Create a class and object also add methods to print the Bike and its price.
class Car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def fn(self):
        print("The name of the Bike is ",self.name," & Price is ",self.price)
p2=Car("Kawazaki",100000)
p2.fn() #object.method()
#modify object property.
p2.price=250000
p2.fn()
#delete object property.
del p2.price
#delete object
del p2
#print will return error

#Create a class named "School", with "class" and "rollnumber" properties, and a "printname" method.
class School:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def printname(self):
        print("The name of the student is ",self.name," & the roll number is",self.rollno)

#Create a class named Student, which will inherit the properties and methods from the "School"class:
class Student(School):
    def __init__(self,name,rollno,age):
        School.__init__(self,name,rollno)
#add a properties in a Student class and print the values
        self.age=age
#add method in Student class and print the method proprty values.
    def printname2(self):
        print("The name of the student is ",self.name,"  the roll number is",self.rollno," & Age is ",self.age)

p3=School("Hamdan",39)
p3.printname()

p4=Student("Hamdan",39,20)
p4.printname2()

#create a tuple values("hai","hello","Bye") and iterate this values.
t=("Hi","Hello","Bye")
myt=iter(t)
print(next(myt))
print(next(myt))
print(next(myt))


#To print “Good Morning  All” using iterator method?
t=("Good morning all")
myt=iter(t)
for t in myt:
    print(t)

#looping the iterator
t=("Hamdan","Mohammed",20)
myt=iter(t)
for t in myt:
    print(t)

#create three classes: Maths, Hindi, and Science,and they all have a method called mark() and print the marks calling mark().
class Maths:
    def __init__(self,marks):
        self.marks=marks
    def mark(self):
        print("Passed")

class Hindi:
    def __init__(self,marks):
        self.marks=marks
    def mark(self):
        print("Passed")

class Science:
    def __init__(self,marks):
        self.marks=marks
    def mark(self):
        print("Passed")

p1=Maths("92")
p2=Hindi("88")
p3=Science("97")

for x in (p1,p2,p3):
    x.mark()

#create a file save with "food.py" extension. in another file Import the module named "food", and call the "items" function.
import food as x #renaming the module using as keyword
x.items("Apple")
#Import the datetime module and display the current date.
import datetime
x=datetime.datetime.now()
#Return the year and name of weekday using strftime().
print(x.year)
print(x.strftime("%A"))
#Return the month  using strftime().
print(x.strftime("%B"))
import math
#13, 2, 5, 60, 100 find the "min" and "max" values.
x=min(13,2,5,60,100)
print(x)
x=max(13,2,5,60,100)
print(x)

#"-20245"  print the positive value using "abs()".
print(abs(-20245))

#pow(5,2)
print(pow(5,2))

#import math module and find the square root of "25"
x=math.sqrt(25)
print(x)

#create a  file and read to another file .
# f=open("newfile.txt","x")
# f=open("newfile1.txt","r")
# print(f.read())
# #Return the 3 first characters of the file.
# f=open("newfile1.txt","r")
# print(f.read(3))
# #Read three lines of the file.
# f=open("newfile1.txt","r")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# #Open the file and append content to that file.
# f=open("newfile1.txt","a")
# f.write("I'm from India")
# f=open("newfile1.txt","r")
# print(f.read())
#to check if a file exists and to delete if it exists
import os
if os.path.exists("newfile1.txt"):
    os.remove("newfile1.txt")
else:
    print("The file doesn't exist !")
#to delete a file
os.remove("new.txt")
#to delete a folder
os.rmdir("testfolder")












