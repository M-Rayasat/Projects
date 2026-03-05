#Discount Calculator
lis=[19.99, 5.50, 100.0]
dis=[]
i=0
for x in lis:
	a=0.15*lis[i]
	b=x-a
	dis.append(b)
	i+=1
print(f"Original List:\n{lis}\nDiscounted List:\n{dis}")
print("Original\tDiscount\n")
for x,y in zip(lis,dis):#zip is used to make tuple pair and store them in list
	print(f"{x}\t{y:.2f}")
