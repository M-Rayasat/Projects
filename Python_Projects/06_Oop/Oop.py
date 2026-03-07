#Working With OOP 
class Boy():
	name="M_Rayasat"
	f_name="M_Liaqat"
	age=18
	education="BSCS"
	weight="60_Kg"
	mobile="0329-7742837"
"""This is a blue Print of a boy 
and boy have above characterstics
and every ordinary boy have default values"""
#Class is a template e.g., Template of Boy

x=Boy() #x is a boy 
print(x.name) #x ka name (default)
print(x.mobile) #x ka mobile number (default)
print("-"*50)

y=Boy() #y is a boy
y.name= "Rehan" #y ka name
y.mobile="0341-5122519" #y ka number
print(y.name)
print(y.mobile)
print("-"*50)

