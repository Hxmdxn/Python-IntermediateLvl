import datetime as dt

#Write a program in the given number is palindrom or not?
def pal(num):
    x=num[::-1]
    if x==num:
        print("Entered string is a Palindrome")
    else:
        print("Entered string is Not a Palindrome")

p=input("Enter the string : ")
pal(p)

#Print a reversed pyramid pattern in Python.

num=(int(input("Enter the number of rows : ")))
print("Reverse Pyramid\n")
for i in range(num):
    for j in range(i):
        print(" ",end="")
    for j in range (num-i):
        print("*",end= " ")
    print()

#Return the year and name of weekday using strftime().
print(dt.datetime.now().strftime("%Y")) #year
print(dt.datetime.now().strftime("%A")) #name of weekday

#Import the datetime module and display the current date.
print(dt.datetime.now().strftime("%d/%m/%y"))

#Write a Python program to find the sum of all even numbers in a list.
def sum_list(numbers):
    sum=0
    for i in numbers:
        if int(i)%2==0:
            sum+=int(i)
    print(sum)
           
num=input("Enter the numbers comma separated : ").split(',')#to make it a list
sum_list(num)
        
        
#Write a Python program to find the sum of numbers in a Tuple?
def sum_list(numbers):
    sum=0
    for i in numbers:
            sum+=int(i)
    print(sum)
           
numbers=input("Enter the numbers comma separated : ").split(',')
numbers=tuple(map(int,numbers))#convert it into tuple
sum_list(numbers)

#create three classes: Maths, Hindi, and Science,
#and they all have a method called mark() and print the marks calling mark().
class Maths:
    def __init__(self,marks):
        self.marks=marks
    def mark(n):#method
        print(68)
class Hindi:
    def __init__(self,marks):
        self.marks=marks
    def mark(n):
        print(98)
        
class Science:
    def __init__(self,marks):
        self.marks=marks
    def mark(n):
        print(90)
        
        
m=Maths("")
h=Hindi("")
s=Science("")

for x in m,h,s:
    x.mark()
        
        
        
    


        

