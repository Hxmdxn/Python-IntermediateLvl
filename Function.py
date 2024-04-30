#create a function using 1 argument
def z(fname):
    print("My name is: ",fname)
z("Hamdan") #fn call

#create a function using 2 arguments
def y(fname,age):
    print("My name is ",fname,"and I'm ",age,"Years old")
y("Hamdan",65)

#create a function using 3 arguments
def new(fname,lname,age):#formal paramtrs/placeholders
    print(fname,"",lname,"",age)
new("Hamdan","Mohammed",78) #actual paramtrs

#Arbitrary argument
def fn(*kids):#don't know the number of arguments
    print("The eldest child is: ",kids[0])
fn("Hamdan","Ameen","Ali")  

#Keyword argument
def name(child1, child2, child3):
    print("The eldest child is :",child3)
    print("The youngest child is :",child1)
name(child1="Hamdan",child2="Ameen",child3="Ali")

#Arbitrary keyword argument 
def n(**students):#don't know the number of keyword arguments
    print("First student is :" , students["s1"])
n(s1="Hamdan",s2="Ameen")

#default Parameter
def f(Country="India"):
    print("I'm from",Country)
f("Sweden")
f("Norway")
f() #when argument isnt passed , it uses default value that is
    #assigned to it.

#List as an argument
def l(food):
    for x in food:
        print(x)
fruits=["Chicken","Chips","Fries"]
l(fruits) 

#Tuple as an argument
def q(company):
    for x in company:
        print(x)
companies=("Mercedez","BMW","Ferrari")
q(companies)

#Set as an argument
def e(company):
    for x in company:
        print(x)
companies={"Mercedez","BMW","Ferrari"}
e(companies)

#Dict as an argument
def g(company):
    for x in company:
        print(x,company[x])
companies={"Name":"Ameen","Blood group":"O+","Age":20,"Place":"Melattur"}
g(companies)

#return statement
def r(x,y):
    return 5*x*y
print(r(1,2))
print(r(2,2))
print(r(3,2))

#pass statement
def r():
    pass #no output (error avoided)
