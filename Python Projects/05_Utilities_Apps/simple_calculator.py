#Build a simple calculator:
while True: 
	num1=input('Enter the number: ')
	if num1.lower()=="exit":
		break
	else:
		num1=float(num1)
	num2=input('Enter the Number: ')
	if num2.lower()=="exit":
		break
	else:
		num2=float(num2)
	op=input("Enter the operator (+-/*): ")
	if op=="exit":
		break
	if op=="+":
		print("Result is",num1+num2)
	if op=="/":
		if num2==0:
			print("Number not divisible by zero")
		else:
			print("Result is", num1/num2)
	if op=="*":
		print("Result is",num1*num2)
	if op=="-":
		print("Result is", num1-num2)
print("Program finished")