def loginSystem(usr,pwd):
    if usr=="Hamdan" and pwd=="123":
        return True
    else:
        return False

username=input("Enter the username : ")
password=input("Enter the password : ")

verified=loginSystem(username,password)
if verified == True:
    print('Access Granted')
else:
    print('Access Denied')