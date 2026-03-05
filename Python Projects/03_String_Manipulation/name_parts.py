#Write a program that takes a full name input and prints
nam=input("Enter your name:")
nam_list=nam.split()
print(f'First name is {nam_list[0]}')
if len(nam_list)>1:
	print(f'Last name is {nam_list[-1]}')
a : str=""
for x in nam_list:
	b=x[0].upper()
	a=a+b+"."
print(a)
