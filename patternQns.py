#pyramid pattern
n=int(input("Enter the number of lines : "))
print("Type 1\n")
for i in range(n): #rows
    for j in range (n-i-1): #initial space 
        print(" ",end="")
    for j in range (i+1): #we need i+1 stars
        print("*",end=" ")#space between the stars
    print()
    
# # half triangle(left portion)
n=int(input("Enter the number of lines : "))
print("Type 2\n")
for i in range(n): #rows
    for j in range (n-i-1): #initial space 
        print(" ",end="")
    for j in range (i+1): #we need i+1 stars
        print("*",end="")#no space between the stars
    print()
    
# # odd number of stars (1-3-5-7.....)
n=int(input("Enter the number of lines : "))
print("Type 3\n")
for i in range(n): #rows
    for j in range (n-i-1): #initial space 
        print(" ",end="")
    for j in range (2*i+1): #we need odd stars
        print("*",end="")# no space between the stars
    print()
    
# # inverted pyramid
n=int(input("Enter the number of lines : "))
print("Type 4\n")
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end=" ")
    print()
  
    

# # right angled triangle
n=int(input("Enter the number of rows : "))
print("Type 5\n")
for i in range(n):
    for j in range(i+1): #number of stars
        print("*",end=" ")
    for j in range(n-i): #space
        print(" ",end=" ")
    print()

n=int(input("Enter the number of rows : "))
print("Type 6\n")
for i in range(n):
    for j in range(n-i):
        print("*",end=" ") 
    print()


# # pattern using numbers    
n = int(input("Enter the number of rows: "))
print("Type 7\n")
for i in range(1,n+1):#rows
    for j in range (1,i+1):#columns
        print(j,end=' ')
    print()

#numbers inorder pattern
n=int(input("Enter the number : "))
print("Type 8\n")
count = 1
for i in range(n):
    for j in range(i + 1): #column
        print(count, end=" ")
        count += 1
    print()


