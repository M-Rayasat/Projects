#Convertion of binary to decimal 
bina=input("Enter binary code: ")
deci=0
for x in bina:
	deci=deci*2
	if x=='1':
		deci+=1
print(f"Decimal Value is {deci}")