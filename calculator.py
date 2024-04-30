#simple calculator
x=int(input("Enter the Number : "))
y=int(input("Enter the Number : "))
op=str(input("Enter the operator: "))
sum=x+y
diff=x-y
prod=x*y
div=x/y
floor=x//y
if (op=="+"):
    print(sum)
elif (op=="-"):
    print(diff)
elif (op=="*"):
    print(prod)
elif (op=="/"):
    print(div)
elif (op=="//"):
    print(floor)
else:
    print("Invalid Operator")
    

