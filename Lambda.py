x = lambda a,b,c: a*b*c #argument(s) : expression (only 1)
print(x(5,6,7)) 
print(x(1,2,3))

#lamda inside a function
def myfunc(n):#n decalred here
    return lambda a:a%n #a declared here

d=myfunc(2) #value of n stored in d
print(d(11)) #d printed with a 

#Another example
def myfunc(r):
    return lambda a,b:a*b*r

d=myfunc(6)
print(d(4,5))
