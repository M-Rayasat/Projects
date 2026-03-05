#Write a program to make a new list containing the squares of numbers from 1 to 10 using list comprehension
z=[]
for x in range(1,11):
 z.append(x**2)
print(z)
#list comprehension 
z=[ y**2 for y in range(1,11) ]
print(z)