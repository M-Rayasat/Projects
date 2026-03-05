#Ask the user for a password. Check:
pwd=input("Enter your password: ")
if len(pwd) >=8 and ("@" in pwd or "#" in pwd):
	print("Password is valid")
else:
	print("Password is not valid")