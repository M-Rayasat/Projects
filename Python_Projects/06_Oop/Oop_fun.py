#Functions in Classes
class Boy:
	name="M_Rayasat"
	f_name="M_Liaqat"
	age=18
	education="BSCS"
	weight="60_Kg"
	mobile="0329-7742837"
	def info(self):
		print(f"My Name is {self.name}\nAge is {self.age}\nFather Name is {self.f_name}\nMy Qualification is {self.education}")
b1=Boy() #1st boy #default values

b2=Boy() #2nd boy
b2.name="Rehan"
b2.education="Matric"
b2.age=15
b2.f_name="M_Liaqat"

b3=Boy() #3rd Boy 
b3.name="Sohail"
b3.education="5th"
b3.age=10
#b3.f_name no assigning because default M_Liaqat

b1.info()
print("-"*40) 
b2.info()
print("-"*40) 
b3.info()
print("-"*40) 