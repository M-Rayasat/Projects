#Instructor Function 
class Boy:
	def __init__(self,a,b): #a,b are positional arguments
		#print("This is Constructor Fun")
		self.name=a
		self.age=b
	def info(self):
		print(f"I'm {self.name}  \nMy age is {self.age}")
#------------------------------------------------

A=Boy("Muhammad Rayasat",18)
B=Boy("Rehan",15)
C=Boy("Sohail",10)

print(A.name)
print(A.age)
A.info()
print("-"*40)

print(B.name)
print(B.age)
B.info()
print("-"*40)

print(C.name)
print(C.age)
C.info()
print("-"*40)
#------------------------------------------------
class Girl:
	def __init__(self,name="No-Name",age="Not Found"): #default values
		self.name=name
		self.age=age
	def info(self):
		print(f"I'm {self.name}  \nMy age is {self.age}")
#-----------------------------------------------
F=Girl(name="Fatima",age=21) #G is Girl now (Object)
#G.info() check and try to understand
 
#G.name="Ayesha" (It is possible too) 

print(F.name)
print(F.age)
F.info()
print("-"*40)

K=Girl(name="Kainat",age=19)
print(K.name)
print(K.age)
A.info()
print("-"*40)