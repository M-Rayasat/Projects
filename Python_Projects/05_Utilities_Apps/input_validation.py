x=input("Enter the number: ")
if x.isdigit():
	y=int(x)
	print(f"You Entered this number: {y}\nIs it Integer: {isinstance(y,int)}")
elif x.replace('.','',1).isdigit() and x.count('.')==1:
	y=float(x)
	print(f"You Entered this number: {x}\nis it float: {isinstance(y,float)}")