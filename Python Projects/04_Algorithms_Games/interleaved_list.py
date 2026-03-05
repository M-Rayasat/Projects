#Interleaved element 
# Input lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Empty list to store interleaved elements
interleaved = []

# Using zip() to combine pairs
for x, y in zip(list1, list2):
    interleaved.append(x)
    interleaved.append(y)

# Print all three lists
print("List 1:", list1)
print("List 2:", list2)
print("Interleaved List:", interleaved)