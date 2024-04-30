#mul of 2 numbers using function
def mul_numbers(num1, num2):
    print(num1*num2)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
mul_numbers(num1, num2) #fn. call

# fibanocci
n=int(input("Enter the Limit : "))
a,b=0,1
print("The fibanocci series ")
print(a)
print(b)
for i in range (3,n+1):
    q=a+b 
    print(q)
    a,b=b,q


#prime numbers
num=int(input("Enter a number : "))
if num > 1:
    # Iterate from 2 to num / 2 + 1
    for i in range(2,int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# factorial using recursion
def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return (n*fact(n-1)) 
# print(fact(5))
num = int(input("Enter a number: "))
# using  user-defined 
result = fact(num)
print("Factorial of", num, "is", result)

# pgm to check whether a number is pos neg or zero
num=int(input("Enter the number to check : "))
if num>0:
    print("Entered Numbered is positive")
elif num<0:
    print("Entered Numbered is Negative")
else:
    print("Entered number is zero")

# number of words in a sentence
def count_words(sentence):
    words = sentence.split()
    return len(words)

s= input("Enter a sentence: ")
x = count_words(s)
print("Number of words in the sentence: " ,x)

# or

x=(input("enter the sentence:"))
wordcount=1

for i in x:
    if i.isspace():
        wordcount+=1

print(wordcount)

# uppercase letters
x=input("Enter the sentence : ")
uppercase=0

for i in x:
    if i.isupper():
        uppercase+=1

print(uppercase)


# calculate the number of digits
num=input("Enter a number : ")
digits=0

for i in num:
    if num.isdigit():
        digits+=1
        
print(digits)

# Write a Python program using function to find the sum and average of the elements in a list
# without using in-built functions (use loop instead)
lst=[1,2,3,4,5]
total=0
for x in lst:
    total=total+x
print(total)
avg=total/len(lst)
print(avg)

# LCM of 2 numbers
def findlcm(x,y):
    greater = max(x, y)
    while (True):
        if (greater % x==0 and greater % y==0):
            lcm=greater
            break
        greater=greater+1
    return lcm

num1=int(input("Enter the first number : "))
num2=int(input("Enter the second Number : "))

obj=findlcm(num1,num2)
print("The LCM of two numbers is ",obj)


# write a program to find the area and perimeter of a rectangle
l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
area=(l*b)
peri=2*(l+b)
print("The area is",area)
print("The perimeter is ",peri)

# write a program to find the area and perimeter of a rectangle using class and objects
class rectangle:
    def __init__(self,b,l):
        self.b=b
        self.l=l
    #use 2 methods each
    def area(self):
        return self.b*self.l #axb
    def perimeter(self):
        return 2*(self.b+self.l) #2(a+b)

a=int(input('enter the breadth :'))
b=int(input('enter the length :'))

myfunc=rectangle(a,b)

print("The area is : ",myfunc.area())
print("The Perimeter is :",myfunc.perimeter())

# palindrome
def pal(num):
    x=num[::-1]
    if x==num:
        print("Entered string is a Palindrome")
    else:
        print("Entered string is Not a Palindrome")

p=input("Enter the string : ")
pal(p)

# mul table
x=int(input("Enter the limit: "))
for i in range(1,x+1):
    print(x,"x",i,"=",i*x)

# leap year pgm
year = int(input('enter year'))
if year % 400 == 0:
  print('it is a leap year')
elif year % 4 == 0:
  print('it is a leap year')
elif year % 100 == 0:
  print('not a leap year')
else:
  print('not a leap year')

# Armstrong

n=int(input("Enter the number to check : "))
sum=0
temp=n

while(n>0):
    r=n%10
    sum=sum+(r*r*r)
    n//=10

if sum==temp:
        print("It's an armstrong number")
else:
        print("Not an Armstrong number")

# Find the sum of digits #dsn

n=int(input("Enter the number : ")) 
sum=0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print(sum)

# Reverse the number
# Write a Python program to reverse a number and find the sum of the digits in the reversed number.
# Prompt the user for input.
number = int(input("Enter a number: "))

rev = 0
while number > 0:
    digit = number % 10
    rev = rev * 10 + digit
    number //= 10
print(rev)

# Find the sum of digits in the reversed number
sum = 0
while rev > 0:
    digit = rev % 10
    sum += digit
    rev //= 10
print(sum)

#odd or even
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print(num," is Even")
else:
   print(num," is Odd")


#pgm to check greatest among 3 numbers using operators
a=int(input("Enter the First Number : "))
b=int(input("Enter the Second Number : "))
c=int(input("Enter the Third Number : "))
if (a>b and a>c):
    print(a ,"is greater than", b ,"and", c)
elif (b>a and b>c):
    print(b ,"is greater than",a,"and",c)
elif (c>a and c>b):
    print(c ,"is greater than" ,a,"and",b)
else :
    print("Error")
    