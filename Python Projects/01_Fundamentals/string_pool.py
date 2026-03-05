#Demonstrate string interning and string pool
n1 = "Rayasat"
n2 = "Rayasat"
ls = "This is very long String as seeing"
ls2 = "This is very long String as seeing"

print(f"These {n1} and {n2} have same address: {n1 is n2} | Address: {id(n1)} & {id(n2)}")
print(f"These {ls} and {ls2} have same address: {ls is ls2} | Address: {id(ls)} & {id(ls2)}")