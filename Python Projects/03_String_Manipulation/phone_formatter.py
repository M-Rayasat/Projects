#Phone Number Formatter
lis=["03123456789", "03001234567"]
num=[]
for x in lis:
	a=f"+92-{x[1:4]}-{x[4:]}"
	num.append(a)
	print(a)
for x,y in zip(lis,num):
	print(f"{x}\t{y}")	