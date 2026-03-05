#Sub string finder from main string
strin=input("Enter the string: ")
sub=input("Enter string to find: ")
start=0
print(f"{sub} is found in string")
while True:
	pos=strin.find(sub,start)
	if pos==-1:
		break
	print(f"Found {sub} at index={pos}")
	start=pos+1