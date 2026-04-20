user_name = input("Enter your username: ")
if user_name == "admin":
    password = input("enter your password: ")
    if password == "secret":
        print("access granted")
    else:
        print("wrong password")
else:
 print("Uknown user")