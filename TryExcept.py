try:
    a=2
    b=0
    c=a/b
    print(c)

except Exception as c: #returns the error
    print(c)
except ZeroDivisionError:
    print("Zero div error ! ")
except SyntaxError:
    print('Syntax error')
except: #last "Except" must be empty
    print('Something went wrong!')
finally:  #always gets printed regardless of anything
    print("Proccess Terminated")