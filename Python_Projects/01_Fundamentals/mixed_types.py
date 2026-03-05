#Create a list of mixed data types (strings, numbers, booleans). Print the type of each element.
List= ["Rayasat",121,True]
i=range(len(List))
for x in i:
	print(f"{List[x]} is {type(List[x])}")