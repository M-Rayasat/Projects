#Arithmatic Calculator
while (num:=(input("Enter the Expresion (a+b): ")))!="exit":
	num1,op,num2=num.split()
	num1=float(num1)
	num2=float(num2)
	if op=="+":
		print(f"Your Addition is :{num1+num2}")
	elif op=="-":
		print(f"Your Subtraction is :{num1-num2}")
	elif op=="*":
		print(f"Your Multiplication is :{num1*num2}")
	elif op=="/":
		print(f"Your Division is :{num1/num2}")
	elif op=="**":
		print(f"Your exponential is :{num1**num2}")
	else:
		print("Enter correct Operator")
		continue
		