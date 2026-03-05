#Write a program that finds the largest and smallest numbers in a list entered by the user.
list1=[]
while True:
	a=input("Enter the Number, Q for end: ")
	if a.isdigit():
		list1.append(a)
	else:
		break
large=max(list1)
small=min(list1)
print(f"Larger is {large} and Smallest is {small}")	
