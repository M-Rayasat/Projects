#Write a program using the walrus operator (:=)
if (nam :=input("Enter Your name: ")) =="Rayasat" or nam== "rayasat" :
	print(f"You're Authorized {nam.title()}")
else:
	print(f"You are spy {nam.title()}")