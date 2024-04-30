import re
txt="The student walked to the school"
x=re.search("^The.+school$",txt)
if x:
    print("Matches")
else:
    print("No match")

x=re.findall("to",txt)
print(x)

x=re.sub("to","in",txt)
print(x)

x=re.split("\s",txt)
print(x)


