#Leap Year
year=int(input("Enter the year: "))
if ((year%4==0 and year%100!=0) or year%400==0):
	print(f"{year} is leap year")
	if year%4==0:
		print(f"{year} is divisible by 4")
	if year%100!=0:
		print(f"{year} is not Divisible by 100")
	if year%400==0:
		print(f"{year} is Divisible by 400")
else:
	print(f"{year} is not leap year")
	if year%4!=0:
		print(f"{year} is not Divisible by 4")
	if year%100==0:
		print(f"{year} is Divisible by 100")
	if year%400!=0:
		print(f"{year} is not Divisible by 400")