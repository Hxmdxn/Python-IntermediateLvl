t1=("A","B","D","K","M","D","C")
print(t1)
print(len(t1))
t2=("apple","banana","cherry","kiwi","orange","melon")
#access an item
print(t2[2])
#negative indexing
print(t2[-1])
#range of indexing- show only last 3 items
print(t2[3:])
#range of negative indexing- show index number 3,4,5 items only
print(t2[-3:])
#count the number of elements
b=t1.count("A")
print(b)
#find the first occurance
z=t1.index("D")
print(z)
#change tuple value
y=list(t2)
y[1]="grapes"
x=tuple(y)
print(x)
#add an item into tuple
y=list(t2)
y.append("banana")
x=tuple(y)
print(x)
#remove an item from tuple
y=list(t2)
y.remove("apple")
x=tuple(y)
print(x)
#Join Tuples
L1=("a","b","c")
L2=(1,2,3,4,5)
L3=L1+L2
print(L3)
