#Temprature Converter
while True:
	temp=float(input("Enter your Temperature: "))
	ch=int(input("Choose Convertion:\n1.Convert Celsius to Fahrenheit\n2.Convert Fahrenheit to Celsius\n"))
	if ch == 1:
		f=(temp*9/5)+32
		print(f"Temperature in Fahrenheit: {f:.2f}")
		break
	elif ch == 2:
		c=(temp-32)*5/9
		print(f"Temperature in Celsius: {c:.2f}")
		break
	else:
		print("Enter correct Data")