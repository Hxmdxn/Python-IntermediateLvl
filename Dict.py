dct={"name":"Jessa","country":"USA","telephone":1178}
#print the dictionary
print(dct)
#print the values from dict
x=dct.values()
print(x)
#print the country value from dict using get method
x=dct.get("country")
print(x)
#print the number of items in the dictionary
print(len(dct))

student={"Name":"Hima","Class":9,"Division":"C","Marks":75}
#print the keys using keys() function
x=student.keys()
print(x)
#add a key value to the dictionary
student["age"]=32
print(student)
#print the items using items() function
print(student.items())
#remove an item from dictionary using pop()
student.pop("Name") #don't use index number like list,tuple
print(student)
#print this dictionary using for loop
for x,y in student.items():
    print(x,y)
#print values only using for loop
for x in student:
    print(student[x])
