import os
# f = open("sample.txt","r") 
# print(f.read())
# f.seek(0)#to reset the file pointer to the beginning
# print(f.read(5))
# f.seek(0)#to read specific value
# print(f.readline())#reads each line
# print(f.readline())
# print(f.readline())
# f.close()

# #to append at the last
# f=open("sample.txt","a")
# f.write("ABC")
# f=open("sample.txt","r")
# print(f.read())
# f.close()

# # to overwrite everything
# f=open("sample.txt","w")
# f.write("DEF")
# f=open("sample.txt","r")
# print(f.read())

# f=open("Sample2.txt","x") to create a file
# f=open("Sample2.txt","a") 
# f.write("Hello Hi") appended
# f=open("Sample2.txt","r")
# print(f.read())
# os.remove("Sample.txt") # to delete a file

# # pgm to check if file exists
# if os.path.exists("Sample2.txt"):
#     os.remove("Sample2.txt")
# else:
#     print("File doesn't exist")

# #to del a folder
# os.rmdir("test")