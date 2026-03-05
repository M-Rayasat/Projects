#Format Number
num=input("Enter the number: ")
new_n=num.replace(" ",""). replace("-","")
if len(new_n)==10 and new_n.isdigit():
	format=f"({new_n[:3]}){new_n[3:6]}-{new_n[6:10]}"
	print(format)
else:
	print("Enter the correct number of 10 Digit")