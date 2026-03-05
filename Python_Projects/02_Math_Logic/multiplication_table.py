#Create a program that generates a multiplication table for any number entered by the user.
num=int(input("Enter the number :"))
i=int(input("Enter where you want to end: "))
for x in range(1,i+1):
	a=num*x
	print(f'{num} × {x} = {a}')