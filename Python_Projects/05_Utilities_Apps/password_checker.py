#Password Strength Checker
pwd=input("Enter the Password: ")
pwd_l=len(pwd)>=8
up_dig=any(ch.isupper() for ch in pwd)
low_dig=any(ch.isupper() for ch in pwd)
digit=any(ch.isdigit() for ch in pwd)
special=any(ch in '@#$_&-+*":;!?()/' for ch in pwd)
list1=[]
if pwd_l==False:
	list1.append("At least 8 characters")
if up_dig==False:
	list1.append("At least 1 upper character")
if low_dig==False:
	list1.append("At least 1 lower character")
if digit==False:
	list1.append("At least 1 Digit")
if special==False:
	list1.append("At least one Special Character")
if len(list1)==0:
	print("Your Password is Correct ")
else:
	print("Your Password Require these things ")
	for x in list1:
		print(x)