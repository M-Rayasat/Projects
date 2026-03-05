#Write a program that keeps asking for numbers until the user enters 0, then prints the sum of all entered numbers.
num=[]
while True:
	N=int(input("Enter the number (zero to end): "))
	if N!=0:
		num.append(N)
	else:
		print("Sum is",sum(num))