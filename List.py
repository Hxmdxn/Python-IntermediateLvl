List=["John","Kavya","Babu","Abu","Hari","Devu"]
#Access item in a list
print(List[1])
#Take a second last element in using negative indexing to the list
print(List[-2])
#Change the item value in a list
List[3]="Ameen"
print(List)
#Length of the list
print("Length of the list is",len(List))
#Add an item into the list
List.append("Hamdan")
print(List)
#Insert an item into the list
List.insert(4,"Ali")
print(List)
#remove the specified item from the list
List.remove("Hamdan")
print(List)
#remove the specified index number from the list
List.pop(0)
print(List)
#remove the specified index number from the list using del function
del List[1]
print(List)
#show empty List
List.clear()
print(List)

L1=[10,30,40,60]
L2=[2,90,7,50,100,3]
#add both lists using extend fn.
L1.extend(L2)
print(L1)
#append the lists together
L1.append(L2)
print(L1)
#sort the list L2
L2.sort()
print(L2)

L3=["Hey","Welcome","Sky","Moon"]
#sort the elements
L3.sort()
print(L3)
#remove last one from the list using negative index
L3.pop(-1)
print(L3)
#add an element in index number 3
L3.insert(3,10)
print(L3)

L4=[2,90,7,50,100,3]
#sort the elements in descending order
L4.sort(reverse=True)
print(L4)
#show maximum value
print(max(L4))
#show minimum value
print(min(L4))
#show sum 
print(sum(L4))

L5=["Bag","Pencil","Book","Pen","Bag","Scale","Bag"]
#Show the number of repeated Word
print(L5.count("Bag"))
#Copy the items into new list
L6=[]
L6=L5.copy()
print(L6)
#To show the repeated element
L5=["Bag","Pencil","Book","Pen","Bag","Scale","Bag"]
y=set()
for i in L5:
    if L5.count(i)>1:
       y.add(i)
        
    print(y)
    
#To Join the lists
S1=["a","b","c"]
S2=[5,6,7,8,9]
S3=S1+S2
print(S3)




