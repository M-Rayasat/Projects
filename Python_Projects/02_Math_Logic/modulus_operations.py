#Write a program that uses the modulus operator to determine:
n1=int(input("Enter the Number: "))
l_digit=n1%10
if n1%2==0:
	print(n1,"is Even Number")
else:
	print(n1,"is Odd Number")
print(f"Last Digit of the number is {l_digit}")