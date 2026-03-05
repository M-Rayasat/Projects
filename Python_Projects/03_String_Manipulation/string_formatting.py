#Create a program using string formatting
nam="Muhammad Rayasat"
age=18
marks=81.5833
#with % operator 
print("My name is %s, Age is %d & Marks are %.2f"%(nam,age,marks))
#with .format()
print("My name is {}, Age is {} & Marks are {:.2f}".format(nam,age,marks))
#with f-string
print(f"My name is {nam}, Age is {age} & Marks are {marks:.2f}")