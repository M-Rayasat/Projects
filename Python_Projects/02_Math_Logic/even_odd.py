#Ask the user for a number. Print whether it is even or odd using the modulo operator.
num= int(input("Enter a number :"))
if num%2==0:
	print(num, "is Even")
else:
	print(num,"is odd")