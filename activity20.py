from getpass import getpass

isLogin = False

while isLogin == False:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if username == "owner" and password == "strongpassword123":
        print("Login successful!")
        isLogin = True
    else:
        print("Invalid username or password. Please try again.")
        isLogin = False
