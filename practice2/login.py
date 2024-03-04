# Simple Snippet of Python Code for a login interface
createpassword = input("Create a password: ")
password = createpassword

while True:
    Login = input("Login with your password: ")
    if Login == (password):
            print("Access Granted")
            break
    else:
            print("Access Denied, try again. ")
    
