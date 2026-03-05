#write a program demonstrating chained comparison operators:
num=int(input("Enter the number: "))
if 10 < num < 20:
	print(f"{num} is between 10 & 20")
else:
	print(f"{num} is not between 10 & 20")
if 5 <= num <= 15:
	print(f"{num} is less then 5 or Greater then 15")
else:
	print(f"{num} is between 5 & 15")