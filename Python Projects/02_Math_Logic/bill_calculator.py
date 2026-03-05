#Bill Calculator 
bill=int(input("Enter Your Bill: "))
tip=float(input("Enter for tip percentage "))
total=((tip/100)*bill)+bill
ch=input("Do you want Split(yes/no): ").lower()
if ch=='yes':
	people=int(input("Enter the number of peoples for split: "))
	split=total/people
	print("Your Total Bill is: ",total)
	print("Each person will get: ", split)
else:
	print("Your Total Bill is ",total)