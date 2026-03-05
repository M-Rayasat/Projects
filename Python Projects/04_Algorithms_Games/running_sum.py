#Running Sum List
lis=[10,15,20,25,30,35,30,40]
new=[]
sum=0
for x in lis:
	sum+=x
	new.append(sum)
print("Original List: ",lis)
print("Sum List: ",new)