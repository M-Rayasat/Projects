#Write a program using logical operators (and, or, not)
num=int(input("Enter the number: "))
if num>10 and num<20:
	print(f"{num} is between 10 & 20")
else:
	print(f"{num} is not between 10 & 20")
if num<5 or num>15:
	print(f"{num} is less then 5 or Greater then 15")
else:
	print(f"{num} is between 5 & 15")
positive= num>0
print(f"{num} is positive: {positive} but reverse boolean with 'Not' is {not positive}")