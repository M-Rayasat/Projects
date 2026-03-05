#Create a program that checks if a number is positive, negative, or zero.
num=int(input("Enter the number: "))
if num==0:
	print("Number is zero")
elif num>0:
	print(num, "is positive")
else:
	print(num, "is negative")