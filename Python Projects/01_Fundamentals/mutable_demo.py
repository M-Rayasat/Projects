#Demonstrate the difference between mutable and immutable types:
List=[1,2,3,True,"Rayasat"]
List.append("Ali")
List.pop(1)
print(List) #List is mutable (can be change)
tup=(1,2,3,True,"Rayasat")
#tup.append("Ali") 
#tup.pop()
#Represent an error that append is not able to use
print(tup)
#Result:
	#Tuple is immutable and Table so mutable 