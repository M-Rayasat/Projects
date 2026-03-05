#Demonstrate identity operators (is, is not)
list1=[1234,"Rayasat",True,9-5j]
list2=[1234,"Rayasat",True,9-5j]
R1=list1==list2 #compare Data 
print(f"List1 is equal to List2: {R1}")
R2=list1 is list2 #compare addresses 
print(f"List1 are on same address List2: {R2}")
print(f"Address of List1 is {id(list1)}\nAddress of List2 is {id(list2)}")