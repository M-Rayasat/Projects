#Write a program that asks the user for numbers until they type stop. At the end, print the average of all numbers entered.
List=[]
while True:
	num = input("Enter the number: ")
	if num.lower()=="stop":
		break
	if num.isdigit():
		num=int(num)
		List.append(num)
avg=sum(List)/len(List)
print("Average is ",avg)
