t=("Hamdan","Ali","Ameen")#Iterable (list,tuple,dict)
f=(20,21,19)
x=iter(t)#use iter function
y=iter(f)

print(next(x))
print(next(x))
print(next(x))#3 values , so give next thrice. if given more than thrice , it will print print error "Stop iteration" 

print(next(y),next(y),next(y)) 

s=("Hello")
w=iter(s)
#using for loop for one by one
for s in w:
    print(s)
# or provide "print(next(myt))" 5 times to print each letter "
d=("ALI") #simple 
for x in d:
    print(x)