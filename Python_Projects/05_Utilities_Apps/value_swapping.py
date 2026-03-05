#Swapping values of Variable 
a=int(input("Enter the first Value of A: "))
b=int(input("Enter second value of B: "))
print("{:^40}".format("swap using temporary var\n"))
temp=a #temporary variable method
a=b
b=temp
print(f"Value of A: {a}\nValue of B: {b}")
print("{:^40}".format("Swap value by Python method\n"))
a,b=b,a #pyhton method
print(f"Value of A: {a}\nValue of B: {b}")
print("{:^40}".format("Swap value by Algebraic Method\n"))
a=a+b #sum of both
b=a-b #second=total-first
a=a-b #first=first-total
print(f"Value of A: {a}\nValue of B: {b}")