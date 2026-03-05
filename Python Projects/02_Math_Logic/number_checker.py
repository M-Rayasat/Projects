#Number Pattern Checker
num=float(input("Enter the number: "))
if num>0:
	print(f"Number: {num} is Positive")
else:
	print(f"Number: {num} is Negative")
if num%2==0:
	print(f"Number: {num} is Even")
else:
	print(f"Number: {num} is Odd")
if (num%3==0 and num%5==0):
	print(f"Number: {num} is Divisible by 3 and 5")
else:
	print(f"Number: {num} is not Divisible by 3 and 5")