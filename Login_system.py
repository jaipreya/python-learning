def validate_user(username,password):

    if username!="admin":
        return "Invalid username"
    elif password!="1234":
        return "Invalid password"
    else:
        return "Login successfull"


   

i=0
while i<3:
    
    username=input("Enter Username:")
    password=input("Enter Password:")
    login=validate_user(username,password)
    if login == "Login successfull":
        print(login)
        break
    else:
        print(login)
        i+=1
if i==3:
    print("Account Locked")
    
        

    
    


    
