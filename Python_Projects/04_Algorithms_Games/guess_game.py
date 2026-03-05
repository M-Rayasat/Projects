#Make a guess game
import random
scrt=random.choice(range(1,21))
atm=0
while True:
	num=int(input("Pick the random number between 1 to 20: "))
	atm+=1
	if num>scrt:
		print("Too High")
	elif num<scrt:
		print("Too Low")
	elif num==scrt:
		print(f"You got it {scrt} after {atm} Attempts")
		break