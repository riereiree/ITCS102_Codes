#if else condition

import getpass

username = "mingyukalbo"
password = "imissyou"

u = input("Enter your Username ---->  ")
p = getpass.getpass ("Enter your Password ---->  ")

if username == u and password == p :
	print("YOU'VE SUCCESSFULLY LOGGED IN")
else:
	print("LOG IN DENIED, ENTER THE CORRECT USERNAME AND PASSWORD")