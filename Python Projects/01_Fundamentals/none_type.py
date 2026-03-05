#Create a program demonstrating the None type

x=None
print(f"Type of this variable is {type(x)}")
if x == None:
	print(f"Variable consist of {x}")
a=None
b=None
c=None
print(f"First variable: {a} and address is {id(a)}")
print(f"First variable: {b} and address is {id(b)}")
print(f"First variable: {c} and address is {id(c)}")
print(f"All variable consist of None and have same id")