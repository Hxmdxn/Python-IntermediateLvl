# Example program using break and continue in a for loop
# Using break
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num == 6:
        print("Found 6, exiting the loop.")
        break
    print(num)
print("Execution completed !")

# Using continue
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num == 6:
        print("Found 6, Skipped.")
        continue
    print(num)
print("Execution completed !")
 
#Using while loop
num=0
while(num<=100):
    print(num)
    if num==50:
        print("break reached")
        break
    num=num+1

