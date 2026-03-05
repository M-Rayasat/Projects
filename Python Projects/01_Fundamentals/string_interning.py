#Demonstrate string interning and string pool
n1 = 140      
n2 = 140
n3 = 19000
n4 = 19000

print(f"These {n1} and {n2} have same address: {n1 is n2} | Address: {id(n1)} & {id(n2)}")
print(f"These {n3} and {n4} have same address: {n3 is n4} | Address: {id(n3)} & {id(n4)}")