#Formatted Table
lis=[
("Apple",256.8),
("Banana",280.28),
("Cake",576.83),
("Cream",239.73)
]
print(f"List is \n{lis}")
print("index\tItem\tPrice")
z=1
for x,y in lis:
	print(f"{z}\t{x}\t{y} ")
	z+=1