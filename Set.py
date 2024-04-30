#set
set1={"Manu","Raju","Appu","Balu","Manu"}
print(set1)
#to add items
set1.add("Ali")
print(set1)
#to add 2 sets
set2={"a","b","c","d"}
set3={"Book","pen","bag"}
set2.update(set3)
print(set2)
#remove an item from set3
set3.remove("bag")
print(set3)
#or use discard
#clear the set
set2.clear()
print(set2) 
#delete the set
del set2
#print elements in set3 using for loop
for x in set3:
    print(x)

set4={"AD","GH","FI","KL"}
set5={1,2,3,4,5}
#join the sets using update()
set4.update(set5)
print(set4)
#join the sets using union()
set4.union(set5) #union doesn't allow duplicates
print(set4)